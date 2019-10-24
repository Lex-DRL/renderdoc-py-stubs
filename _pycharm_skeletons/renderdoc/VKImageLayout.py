# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKImageLayout(SwigPyObject):
    """ Contains the layout of a range of subresources in an image. """
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

    baseLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For 3D textures and texture arrays, the first slice used in the range."""

    baseMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The first mip level used in the range."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the current image state."""

    numLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For 3D textures and texture arrays, the number of array slices in the range."""

    numMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of mip levels in the range."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''

