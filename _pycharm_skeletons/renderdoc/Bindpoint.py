# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class Bindpoint(SwigPyObject):
    """
    Declares the binding information for a single resource binding.
    
    See :class:`ShaderBindpointMapping` for how this mapping works in detail.
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

    arraySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this is an arrayed binding, the number of elements in the array."""

    bind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The binding index."""

    bindset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The binding set."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    used = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the shader actually uses this resource, otherwise it's declared but unused."""


    __dict__ = None # (!) real value is ''


