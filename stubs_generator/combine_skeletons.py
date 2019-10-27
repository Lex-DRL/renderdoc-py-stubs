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

# endregion

from os import path as _pth
import re

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
		self.extract_pre_comments = True
		self.pre_comments = list()  # type: _t.List[_str_h]
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


def _file_lines_gen(
	file_path: _str_h, repl_funcs: _t.Iterable[_str_func], comm_data: _CommonData
):
	"""
	Generator returning processed lines for a single submodule.
	No trailing newline characters.
	"""
	if not file_path:
		return
	if PRINT_DEBUG:
		print(file_path)

	file_name = file_path.split('/')[-1]
	if not file_name[:-3]:
		return

	if file_name.lower() != '__init__.py':
		line_of_dashes = '#' * max(len(file_name), 40)
		yield (
			'\n'
			f'##{line_of_dashes}\n'
			f'# {file_name}\n'
			f'##{line_of_dashes}'
		)

	with open(file_path, 'rt', encoding='utf-8') as out_fl:
		for ln in out_fl:
			ln = ln.rstrip('\n\r').rstrip()
			if not ln:
				yield ln

			if comm_data.extract_pre_comments:
				# we need to separate the very 1st block of comments - to insert
				# any common code after it, if needed:
				match_comment = _comments_line_match(ln)
				if match_comment:
					comm_data.pre_comments.append(match_comment.group(1))
					continue
				comm_data.extract_pre_comments = False

			# detect the common external dependencies, skipping the line:
			if _enum_import_match(ln):
				comm_data.imported_enum = True
				continue
			if _SwigPyObject_import_match(ln):
				comm_data.imported_SwigPyObject = True
				continue

			# the regular replacements:
			for repl_f in repl_funcs:
				ln = repl_f(ln)
			ln = ln.rstrip()
			if not ln:
				# the line is cleaned-up to nothing, skip it
				continue
			yield ln


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


def combine():
	import errno
	import os
	import shutil
	from itertools import chain

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
	# at least, source and target paths are as expected

	src_files = {  # filename (no extension): file path (with ext)
		fl_nm[:-3]: fl_pth for fl_nm, fl_pth in (
			(f, f'{src_pkg}/{f}') for f in os.listdir(src_pkg)
		) if _pth.isfile(fl_pth) and fl_nm.lower().endswith('.py')
	}  # type: _t.Dict[_str_h, _str_h]
	init_file = src_files.pop('__init__', None)

	# generate substring-replacing functions:
	repl_funcs = replacers(src_files.keys())

	if PRINT_DEBUG:
		print('\nProcessing files:')

	comm_data = _CommonData()

	if init_file:
		init_lines = list(_file_lines_gen(init_file, repl_funcs, comm_data))
	else:
		init_lines = list()
		comm_data.extract_pre_comments = False

	# clean lines, per module
	modules_lines = {
		fl_nm: list(_file_lines_gen(fl_pth, repl_funcs, comm_data))
		for fl_nm, fl_pth in sorted(src_files.items())
	}  # type: _t.Dict[_str_h, _t.List[_str_h]]

	# TODO: sort modules by their dependencies
	# TODO: re-extract the very 1st comment block after sorting, if no init_file

	# each file has it's own list of processed lines:
	all_files_text = [
		fl_lines for fl_nm, fl_lines in sorted(modules_lines.items())
	]  # type: _t.List[_t.List[_str_h]]

	prefixes = [
		lines for lines, do_include in(
			(comm_data.pre_comments, comm_data.pre_comments),
			([_enum_import_replace], comm_data.imported_enum),
			([_SwigPyObject_import_replace], comm_data.imported_SwigPyObject),
			(init_lines, init_lines),
		) if do_include
	]
	all_files_text = prefixes + all_files_text

	with open(trg_fl, 'wt', encoding='utf-8', newline='') as out_fl:
		out_fl.writelines(
			l + '\n'
			for l in chain(*all_files_text)
		)

	print(f'\nCombined skeleton saved:\n{trg_fl}')
