"""
Step 0:
Combine the raw PyCharm  skeletons to a single mock skeleton-module.
"""

__author__ = 'Lex Darlog (DRL)'

# region the regular Type-Hints stuff

try:
	# support type hints in Python 3:
	# noinspection PyUnresolvedReferences
	import typing as _t
except ImportError:
	pass

# noinspection PyBroadException
try:
	# noinspection PyUnresolvedReferences
	_str_t = (str, unicode)
except:
	_str_t = (bytes, str)

# noinspection PyBroadException
try:
	# noinspection PyUnresolvedReferences
	_str_h = _t.Union[str, unicode]
except:
	# noinspection PyBroadException
	try:
		_str_h = _t.Union[bytes, str]
	except:
		_str_h = str

_str_func = _t.Callable[[_str_h], _str_h]
_h_module_dependencies = _t.Dict[_str_h, _t.Set[_str_h]]

# endregion

import re
from os import path as _pth
from itertools import chain as _chain

PRINT_DEBUG = True

repo_dir = _pth.dirname(__file__)  # 'stubs_generator' dir
repo_dir = _pth.abspath(_pth.join(repo_dir, '..'))
repo_dir = repo_dir.replace('\\', '/')  # 'py-renderdoc-stubs' abs-path
# repo_dir = 'P:/1-Scripts/_Python/py-renderdoc-stubs'

src_pkg = repo_dir + '/_pycharm_skeletons/renderdoc'
trg_dir = repo_dir + '/_skeletons_combined'
trg_fl = trg_dir + '/renderdoc.py'

print(f'Repo path:\n{repo_dir}\n')
print(f'PyCharm skeletons dir:\n{src_pkg}\n')
print(f'Output combined-skeletons file:\n{trg_fl}\n')


class _CommonData(object):
	"""A data class, containing the detected options from the imported files."""
	def __init__(self):
		super(_CommonData, self).__init__()
		self.imported_enum = False
		self.imported_SwigPyObject = False


_comments_line_match = re.compile('\\s*(#.*)').match
_SwigPyObject_import_match = re.compile(
	'\\s*from\\s+\\.?SwigPyObject\\s+import\\s+SwigPyObject\\s*(#.*)?'
).match
_SwigPyObject_import_replace = (
	"\n"
	"###########################\n"
	"# Mock SwigPyObject class\n"
	"###########################\n"
	"\n"
	"class SwigPyObject(object):\n"
	"    pass\n"
	"\n"
	"###########################\n"
)
_enum_import_match = re.compile(
	'\\s*import\\s+enum\\s+as\\s+__enum\\s*(#.*)?'
).match
_enum_import_replace = '\nimport enum as __enum\n'
_all_funcs_prefix = [
	"\n",
	"\n",
	"###########################\n",
	"# All extracted functions\n",
	"###########################\n",
	"\n"
]


def _extract_1st_comment_block_gen(
	file_lines: _t.Iterable[_str_h],
	extracted_block: _t.List[_str_h],
):
	"""
	Separate the initial comment block (containing file encoding)
	from the rest of the file lines.
	"""
	assert isinstance(extracted_block, list)
	extract_pre_comments = True

	for ln in file_lines:
		if not ln:
			yield ln
			continue

		if extract_pre_comments:
			match_comment = _comments_line_match(ln)
			if match_comment:
				ln = match_comment.group(1)
				if ln:
					extracted_block.append(ln)
				continue
			extract_pre_comments = False

		yield ln


# a valid py-object name:
_py_name_re = '[A-Za-z_][A-Za-z_0-9]*'

# 'def AnyFuncName ( whatever) -> maybe_outHint : # maybe comment '
_match_func_start = re.compile(
	'^def\\s+{0}\\s*\\(.*\\)\\s*'
	'(\\s*->.*)?\\s*:(\\s*#.*)?$'.format(_py_name_re)
).match
_match_func_end = re.compile('^[^\s]+').match


def _extract_global_funcs_gen(
	file_lines: _t.Iterable[_str_h],
	extracted_funcs: _t.List[_t.List[_str_h]],
):
	"""
	Extract each global function to it's own separate block of code.
	The function definition is detected vary basically: only for functions
	declaring their name and all the arguments on the same line.

	The end of function is also detected only in simplest case: when a line
	starts from any non-whitespace character. Technically, such line could be
	inside a function (within a multiline string), but we don't catch that edge case.

	Thankfully, PyCharm outputs to skeletons exactly this simplistic formatting.
	"""
	assert isinstance(extracted_funcs, list)
	assert not extracted_funcs or (
		isinstance(extracted_funcs[0], list) and
		isinstance(extracted_funcs[-1], list)
	)

	in_func = False
	cur_func_lines: _t.List[_str_h] = list()
	funcs_num_found = 0

	for ln in file_lines:
		ln = ln.rstrip()
		if in_func:
			if not(ln and _match_func_end(ln)):
				# empty line or still inside a function - add the line and continue
				cur_func_lines.append(ln)
				continue

			# the func is ended, but we still need to process the line
			in_func = False

		def_match = _match_func_start(ln)
		if not def_match:
			# we wasn't in a function and the current line doesn't start a new one -
			# so it's just a regular line
			yield ln
			continue

		# we've found a new function start
		in_func = True
		funcs_num_found += 1
		cur_func_lines = list([ln])
		extracted_funcs.append(cur_func_lines)

	print(f"Functions extracted ({funcs_num_found})")


def _clean_file_lines_gen(
	file_path: _str_h, repl_funcs: _t.Iterable[_str_func], comm_data: _CommonData
):
	"""
	Generator returning processed lines for a single submodule.
	No trailing newline characters + all replacements performed.
	"""
	if not file_path:
		return
	if PRINT_DEBUG:
		print(file_path)

	file_name = file_path.split('/')[-1]
	if not file_name[:-3]:
		return

	def _cleanup(line: _str_h):
		"""The regular replacements"""
		for repl_f in repl_funcs:
			line = repl_f(line)
		return line.rstrip()

	with open(file_path, 'rt', encoding='utf-8') as out_fl:
		for ln in out_fl:
			ln = ln.rstrip('\n\r').rstrip()
			if not ln:
				yield ln
				continue

			# detect the common external dependencies, skipping the line:
			if _enum_import_match(ln):
				comm_data.imported_enum = True
				continue
			if _SwigPyObject_import_match(ln):
				comm_data.imported_SwigPyObject = True
				continue

			ln = _cleanup(ln)
			if not ln:
				# the line is cleaned-up to nothing, skip it
				continue
			yield ln


# a regex detecting class definition (if on single line):
_class_def_match = re.compile(
	'\\s*'.join([
		'',
		'class\\s+{0}',
		'\\(',
		'({0})',
		'\\)',
		':'
	]).format(_py_name_re)
).match


def _base_classes(module_lines: _t.List[_str_h], all_modules: _t.Set[_str_h]):
	"""
	Detect all the base-class names that the classes defined in the
	given file lines inherit from.

	Detects with a regexp, only if `class DefinedClassName(InheritedName):`
	is on a single line, no matter what's the indent.
	"""
	res = list()  # type: _t.List[_str_h]
	for line in module_lines:
		line = line.rstrip()
		if not line:
			continue
		match = _class_def_match(line)
		if not match:
			continue
		base_class_name = match.group(1)
		if base_class_name in all_modules:
			res.append(base_class_name)
	return res


def _replacer_factory(re_comp: _t.Pattern, repl: _str_h):
	"""
	Generate a line-processing function from a single pair of:
		* re.compile
		* replacement string / re pattern
	"""
	re_sub = re_comp.sub  # reduce dot operator

	def replacer(line: _str_h):
		return re_sub(repl, line)

	if PRINT_DEBUG:
		print((re_comp, repl),)
	return replacer


_global_replacements = tuple(
	(re.compile(match_re), repl) for match_re, repl in (
		('\\s*{}.*'.format(re.escape('# real signature unknown')), ''),
		('\\s*{}.*'.format(re.escape('# known case of __new__')), ''),
		('\\s*{}.*'.format(re.escape('# reliably restored by inspect')), ''),
		('\\s*# imports\\s*', ' '),
		('^\\s*#\\s*from\\s+.*[\\\/]renderdoc\\.pyd$', ''),
		# other replacements go here
	)
)
# formatted string, detecting a pattern of other built-in imports:
# 'from .BlendEquation import BlendEquation'
# 'from BlendEquation import BlendEquation'
_import_repl = '\\s*from\\s+\\.?{0}\\s+import\\s+{0}\\s*'


def replacers(submodules: _t.Iterable[_str_h]):
	"""
	Generate the full tuple of replacing functions:
	combining pre-defined global ones and per-module imports removal.
	"""
	replacements = list(_global_replacements)
	replacements.extend([
		(
			re.compile(_import_repl.format(re.escape(module))),
			' '
		)
		for module in submodules
	])
	if PRINT_DEBUG:
		print('\nReplacements:')

	# turn to the actual functions: (str) -> str
	repl_funcs = [
		_replacer_factory(re_comp, repl) for re_comp, repl in replacements
	]
	return tuple(repl_funcs)


def _detect_dependencies_recursively(
	depending_on: _h_module_dependencies,
	base_for: _t.Dict[_str_h, _t.Set[_str_h]],
	module_name: _str_h,
	base_classes: _t.Set[_str_h],
	classes_stack: _t.Optional[_t.List[_str_h]] = None
):
	if not(classes_stack and isinstance(classes_stack, list)):
		classes_stack = [module_name, ]
	if module_name in classes_stack[1:]:
		raise RecursionError(f'Circular dependency detected: {classes_stack}')
	for base_class in base_classes:
		base_for[base_class].add(module_name)
		bases_of_base = depending_on[base_class]
		if bases_of_base:
			_detect_dependencies_recursively(
				depending_on, base_for, module_name, bases_of_base,
				classes_stack + [base_class, ]
			)


def _prepend_module_name(
	module_name: _str_h,
	file_lines: _t.List[_str_h],
):
	"""
	Attach a comment containing the source skeleton name to the beginning
	of the file lines
	"""
	file_name = f'Skeleton: {module_name}.py'
	line_of_hashes = '#' * max(len(file_name), 40)
	prepend = [
		'',
		f'##{line_of_hashes}',
		f'# {file_name}',
		f'##{line_of_hashes}',
	]
	return prepend + file_lines


def _check_fs():
	"""Make sure the in/out file structure is as expected. Raise an error if not."""
	import errno
	import os
	import shutil

	if not _pth.exists(src_pkg):
		raise FileNotFoundError(errno.ENOENT, 'Skeletons dir is missing', src_pkg)
	if not _pth.isdir(src_pkg):
		raise NotADirectoryError(
			errno.ENOTDIR, 'Skeletons path is taken by the file', src_pkg
		)
	if _pth.exists(trg_dir):
		if not _pth.isdir(trg_dir):
			raise NotADirectoryError(
				errno.ENOTDIR, 'Skeletons out-dir is taken by the file', trg_dir
			)
	else:
		os.makedirs(trg_dir)
	if _pth.isdir(trg_fl):
		shutil.rmtree(trg_fl)
		print(f'Folder removed: {trg_fl}')


def source_module_files() -> _t.Dict[_str_h, _str_h]:
	"""
	The dictionary with source module names as key and a full filepath as a value.
	"""
	import os
	# first, make sure the source and target paths are as expected:
	_check_fs()
	return {  # filename (no extension): file path (with ext)
		fl_nm[:-3]: fl_pth for fl_nm, fl_pth in (
			(f, f'{src_pkg}/{f}') for f in os.listdir(src_pkg)
		) if _pth.isfile(fl_pth) and fl_nm.lower().endswith('.py')
	}


def _sorted_modules(
	module_text: _t.Dict[_str_h, _t.List[_str_h]]
):
	"""
	From already cleanup'ed per-module lines, generate a list of modules
	sorted by their dependency.
	Each element in the result is a tuple of (ModuleName, LinesList)
	"""
	print('\nDetecting dependencies order...')

	all_module_names_set = set(module_text.keys())

	# dependent module -> it's bases
	module_use: _h_module_dependencies = {
		mdl_nm: set(_base_classes(lines, all_module_names_set))
		for mdl_nm, lines in module_text.items()
	}
	# the opposite: base module -> modules depending on it
	module_used_by: _h_module_dependencies = {
		mdl_nm: set() for mdl_nm in all_module_names_set
	}
	# populate the downstream dependencies (to `module_base_for`):
	for mdl_nm, base_classes in module_use.items():
		_detect_dependencies_recursively(
			module_use, module_used_by, mdl_nm, base_classes
		)
	# use downstream dependencies to detect
	# which classes the module code is used for:
	module_sort_keys: _t.Dict[_str_h, _t.List[_str_h]] = {
		mdl_nm: sorted(
			list(used_by - {mdl_nm, }) + [mdl_nm + ':current', ]
		) for mdl_nm, used_by in module_used_by.items()
	}
	modules_sorted_text: _t.List[_t.Tuple[_str_h, _t.List[_str_h]]] = [
		(m_nm, m_lines) for m_nm, m_lines, m_k in sorted(
			(
				(mod_nm, module_text[mod_nm], mod_sort_key)
				for mod_nm, mod_sort_key in module_sort_keys.items()
			),
			key=lambda tpl: tpl[-1]
		)
	]

	print('Dependencies found, modules re ordered according to them.')
	return modules_sorted_text


def combine():
	src_files = source_module_files()  # FS is error-checked inside the func
	init_file = src_files.pop('__init__', None)

	# generate substring-replacing functions:
	all_module_names = set(src_files.keys())
	repl_funcs = replacers(sorted(all_module_names))

	if PRINT_DEBUG:
		print('\nProcessing files:')

	comm_data = _CommonData()

	# the very 1st nlock of comments is special: it needs to stay the 1st.
	first_comment_block = list()  # type: _t.List[_str_h]
	func_definitions = list()  # type: _t.List[_t.List[_str_h]]

	if init_file:
		init_lines_gen = _clean_file_lines_gen(init_file, repl_funcs, comm_data)
		init_lines_gen = _extract_1st_comment_block_gen(init_lines_gen, first_comment_block)
		init_lines_gen = _extract_global_funcs_gen(init_lines_gen, func_definitions)
		init_lines = list(init_lines_gen)
	else:
		init_lines = list()

	# clean lines, per module
	module_text: _t.Dict[_str_h, _t.List[_str_h]] = {
		mdl_nm: list(_clean_file_lines_gen(fl_pth, repl_funcs, comm_data))
		for mdl_nm, fl_pth in sorted(src_files.items())
	}

	modules_sorted_text = _sorted_modules(module_text)

	print('\nExtracting functions:')
	for mdl_nm, mdl_lines in modules_sorted_text:
		print(mdl_nm)
		mdl_lines[:] = _extract_global_funcs_gen(mdl_lines, func_definitions)
	if func_definitions:
		func_definitions = [_all_funcs_prefix, ] + func_definitions

	if modules_sorted_text and not init_file:
		modules_sorted_text[0][1] = list(_extract_1st_comment_block_gen(
			modules_sorted_text[0][1], first_comment_block
		))

	# each file has it's own list of processed lines:
	all_files_text = [
		_prepend_module_name(mdl_nm, mdl_lines)
		for mdl_nm, mdl_lines in modules_sorted_text
	]

	prefixes: _t.List[_t.List[_str_h]] = [
		lines for lines, do_include in(
			(first_comment_block, first_comment_block),
			([_enum_import_replace], comm_data.imported_enum),
			([_SwigPyObject_import_replace], comm_data.imported_SwigPyObject),
			(init_lines, init_lines),
		) if do_include
	]
	all_files_text = prefixes + all_files_text + func_definitions

	with open(trg_fl, 'wt', encoding='utf-8', newline='') as out_fl:
		out_fl.writelines(
			l + '\n'
			for l in _chain(*all_files_text)
		)

	print(f'\nCombined skeleton saved:\n{trg_fl}')
