# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderDebugTrace(SwigPyObject):
    """
    This stores the whole state of a shader's execution from start to finish, with each
    individual debugging step along the way, as well as the immutable global constant values that do not
    change with shader execution.
    """
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

    constantBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Constant variables for this shader as a list of :class:`ShaderValue` lists.

Each entry in this list corresponds to a constant block with the same index in the
:data:`ShaderBindpointMapping.constantBlocks` list, which can be used to look up the metadata.

"""

    hasLocals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A flag indicating whether this trace has locals information"""

    inputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The input variables for this shader as a list of :class:`ShaderValue`."""

    lineInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A ``list`` of :class:`LineColumnInfo` detailing which source lines each instruction
corresponds to

"""

    states = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A list of :class:`ShaderDebugState` states representing the state after each
instruction was executed

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


