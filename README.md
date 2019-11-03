# Python stubs for RenderDoc

[RenderDoc](https://renderdoc.org)'s python module already has all the type hints in it's sphinx docstrings. Unfortunately, the IDE I use ([PyCharm](https://www.jetbrains.com/pycharm/), which in turn uses [MyPy](http://mypy-lang.org)) can't parse them, so there are (almost) no autocompletes by default.

To fix it, this repo is designed to generate [PEP-484 stubs](https://www.python.org/dev/peps/pep-0484/#stub-files) for that python module. It's done by:
* Extracting so-called [binary skeletons](https://github.com/JetBrains/python-skeletons) directly from PyCharm caches.
* Combining and processing them with custom scripts and third-party modules to produce the actual stub file.

Basically, this repo is just a wrapper on top of great tools provided by other people, so most of credits goes to them.
