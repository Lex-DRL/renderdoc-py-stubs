# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderDebugState(SwigPyObject):
    """
    This stores the current state of shader debugging at one particular step in the shader,
    with all mutable variable contents.
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

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A set of :class:`ShaderEvents` flags that indicate what events happened on this step."""

    indexableTemps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indexable temporary variables for this shader as a list of :class:`ShaderVariable`."""

    locals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
An optional list of :class:`ShaderVariableRef` indicating which high-level locals map
to which registers, and their type

"""

    modified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of registers that were modified."""

    nextInstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The next instruction to be executed after this state. The initial state before any
shader execution happened will have ``nextInstruction == 0``.

"""

    outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The output variables for this shader as a list of :class:`ShaderVariable`."""

    registers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The temporary variables for this shader as a list of :class:`ShaderVariable`."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


