# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLVertexAttribute(SwigPyObject):
    """
    Describes the configuration for a single vertex attribute.
    
    .. note:: If old-style vertex attrib pointer setup was used for the vertex attributes then it will
      be decomposed into 1:1 attributes and buffers.
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

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The byte offset from the start of the vertex data in the vertex buffer from
:data:`vertexBufferSlot`.

"""

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this vertex attribute is enabled."""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` of the vertex attribute."""

    genericValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`PixelValue` containing the generic value of a vertex attribute."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertexBufferSlot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex buffer input slot where the data is sourced from."""


    __dict__ = None # (!) real value is ''


