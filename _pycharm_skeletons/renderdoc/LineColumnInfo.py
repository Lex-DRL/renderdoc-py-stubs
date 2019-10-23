# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class LineColumnInfo(SwigPyObject):
    """ Details the current region of code that an instruction maps to """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    callstack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A ``list`` of ``str`` with each function call in the current callstack at this line.

The oldest/outer function is first in the list, the newest/inner function is last.

"""

    colEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The column number (starting from 1) of the end of the code on the line specified by
:data:`lineEnd`. If set to 0, no column information is available and the whole lines should be
treated as covering the code.

"""

    colStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The column number (starting from 1) of the start of the code on the line specified by
:data:`lineStart`. If set to 0, no column information is available and the whole lines should be
treated as covering the code.

"""

    fileIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current file, as an index into the list of files for this shader."""

    lineEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line-number (starting from 1) of the end of the current section of code."""

    lineStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line-number (starting from 1) of the start of the current section of code."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


