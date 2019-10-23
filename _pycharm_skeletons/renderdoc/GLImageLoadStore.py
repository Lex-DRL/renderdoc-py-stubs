# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLImageLoadStore(SwigPyObject):
    """ Describes the properties of a load/store image. """
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

    imageFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` that the image is bound as."""

    layered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if multiple layers are bound together to the image.
``False`` if only one layer is bound.

"""

    mipLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mip of the texture that's used in the attachment."""

    readAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if loading from the image is allowed."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the texture object."""

    slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The slice of the texture that's used in the attachment."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureType` of the texture."""

    writeAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if storing to the image is allowed."""


    __dict__ = None # (!) real value is ''


