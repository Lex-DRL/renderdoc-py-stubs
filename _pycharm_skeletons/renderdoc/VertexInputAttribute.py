# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VertexInputAttribute(SwigPyObject):
    """ Information about a vertex input attribute feeding the vertex shader. """
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

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The byte offset from the start of the vertex data for this VB to this attribute."""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`~renderdoc.ResourceFormat` with the interpreted format of this attribute."""

    genericEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this attribute is using :data:`genericValue` for its data."""

    genericValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A :class:`~renderdoc.PixelValue` with the generic value for this attribute if it has
no VB bound.

"""

    instanceRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
If :data:`perInstance` is ``True``, the number of instances that source the same value
from the vertex buffer before advancing to the next value.

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this input. This may be a variable name or a semantic name."""

    perInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this attribute runs at instance rate."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    used = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this attribute is enabled and used by the vertex shader."""

    vertexBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the vertex buffer used to provide this attribute."""


    __dict__ = None # (!) real value is ''


