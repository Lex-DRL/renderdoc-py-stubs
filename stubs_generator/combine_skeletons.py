"""
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

# endregion

from os import path as _pth

repo_dir = _pth.dirname(__file__)  # 'stubs_generator' dir
repo_dir = _pth.abspath(_pth.join(repo_dir, '..'))
repo_dir = repo_dir.replace('\\', '/')  # 'py-renderdoc-stubs' abs-path

src_pkg = repo_dir + '/_pycharm_skeletons/renderdoc'
trg_dir = repo_dir + '/_skeletons_combined'
trg_fl = trg_dir + '/renderdoc.py'

print(f'Repo path:\n{repo_dir}')
print(f'PyCharm skeletons dir:\n{src_pkg}')
print(f'Output combined-skeletons file:\n{trg_fl}')


def combine():
	pass

