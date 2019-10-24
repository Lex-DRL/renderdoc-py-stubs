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


def _file_lines_gen(file_path: _str_h, repl_funcs: _t.Iterable[_str_func]):
	"""
	Generator returning processed lines for a single submodule.
	No trailing newline characters.
	"""
	if not file_path:
		return
	with open(file_path, 'rt', encoding='utf-8') as out_fl:
		for ln in out_fl:
			ln = ln.rstrip('\n\r').rstrip()
			if not ln:
				yield ln

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

	return replacer


_global_replacements = tuple(
	(re.compile(match_re), repl) for match_re, repl in (
		('\\s*{}.*'.format(re.escape('# real signature unknown; restored from __doc__')), ''),
		('\\s*from\\s+\\.?SwigPyObject\\s+import\\s+SwigPyObject\\s*', ' '),
		('\\s*import\\s+enum\\s+as\\s+__enum\\s*', ' '),
		('\\s*# imports\\s*', ' '),
		# other replacements go here
	)
)
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
	return tuple(
		_replacer_factory(re_comp, repl) for re_comp, repl in replacements
	)


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
	if _pth.exists(trg_fl):
		trg_obj = 'File'
		if _pth.isdir(trg_fl):
			trg_obj = 'Folder'
			shutil.rmtree(trg_fl)
		else:
			os.remove(trg_fl)
		print(f'{trg_obj} removed: {trg_fl}')
	# at least, source and target paths are as expected; target file - not exist

	src_files = {  # filename (no extension): file path (with ext)
		fl_nm[:-3]: fl_pth for fl_nm, fl_pth in (
			(f, f'{src_pkg}/{f}') for f in os.listdir(src_pkg)
		) if _pth.isfile(fl_pth) and fl_nm.lower().endswith('.py')
	}  # type: _t.Dict[_str_h, _str_h]
	init_file = src_files.pop('__init__', None)

	# generate substring-replacing functions:
	repl_funcs = replacers(src_files.keys())

	# each file has it's own generator with processed lines:
	all_generators: _t.List[_t.Generator[str, _t.Any, None]] = list()
	if init_file:
		all_generators.append(_file_lines_gen(init_file, repl_funcs))
	for fl_nm, fl_pth in sorted(src_files.items()):
		all_generators.append(_file_lines_gen(fl_pth, repl_funcs))

	with open(trg_fl, 'wt', encoding='utf-8', newline='') as out_fl:
		out_fl.writelines(l + '\n' for l in chain(*all_generators))
