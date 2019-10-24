# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLTexture(SwigPyObject):
    """ Describes the details of a texture. """
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

    depthReadChannel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The channel to read from in a depth-stencil texture.

``-1`` for non depth-stencil textures.

``0`` if depth should be read.

``1`` if stencil should be read.

"""

    firstMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for textures - the first mip that is available."""

    numMips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for textures - the number of mips that are available."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the underlying resource the view refers to."""

    swizzle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Four :class:`TextureSwizzle` elements indicating the swizzle applied to this texture."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureType` of the texture."""


    __dict__ = None # (!) real value is ''


