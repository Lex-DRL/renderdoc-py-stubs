# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderDebugInfo(SwigPyObject):
    """
    Contains the information about a shader contained within API-specific debugging
    information attached to the shader.
    
    Primarily this means the embedded original source files.
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

    compileFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderCompileFlags` containing the flags used to compile this shader."""

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ShaderEncoding` of the source. See :data:`files`."""

    files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A list of :class:`ShaderSourceFile`, encoded in the form denoted by :data:`encoding`.

The first entry in the list is always the file where the entry point is.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


