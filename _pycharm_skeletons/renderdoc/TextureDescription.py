# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TextureDescription(SwigPyObject):
    """ A description of a texture resource. """
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

    arraysize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many array elements this texture has, will be at least 1."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many bytes would be used to store this texture and all its mips/slices."""

    creationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The way this texture will be used in the pipeline."""

    cubemap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this texture is used as a cubemap or cubemap array."""

    depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The depth of the texture, or 1 if not applicable."""

    dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The base dimension of the texture - either 1, 2, or 3."""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` that describes the format of each pixel in the texture."""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the texture, or 1 if not applicable."""

    mips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many mips this texture has, will be at least 1."""

    msQual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quality setting of this texture, or 0 if not applicable."""

    msSamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many multisampled samples this texture has, will be at least 1."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique :class:`ResourceId` that identifies this texture."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureType` of the texture."""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the texture, or length for buffer textures."""


    __dict__ = None # (!) real value is ''


