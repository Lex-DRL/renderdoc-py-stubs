# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11View(SwigPyObject):
    """ Describes the details of a D3D11 resource view - any one of UAV, SRV, RTV or DSV. """
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

    bufferFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for buffers - the flags for additional view properties."""

    bufferStructCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the view has a hidden counter, this stores the current value of the counter."""

    elementByteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The byte size of a single element in the view. Either the byte size of
:data:`viewFormat`, or the structured buffer element size, as appropriate.

"""

    firstElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for buffers - the first element to be used in the view."""

    firstMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for textures - the first mip that is available through the view."""

    firstSlice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for texture arrays or 3D textures - the first slice available through the view."""

    numElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for buffers - the number of elements to be used in the view."""

    numMips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for textures - the number of mip levels in the view."""

    numSlices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Valid for texture arrays or 3D textures - the number of slices in the view."""

    resourceResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the underlying resource the view refers to."""

    structured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this view describes a structured buffer."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureType` of the view type."""

    viewFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` that the view uses."""

    viewResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the view itself."""


    __dict__ = None # (!) real value is ''


