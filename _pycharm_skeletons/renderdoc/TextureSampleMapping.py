# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TextureSampleMapping(SwigPyObject):
    """
    How to map multisampled textures for saving to non-multisampled file formats.
    
    .. data:: ResolveSamples
    
      Value for :data:`sampleIndex` if the samples should be averaged.
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

    mapToArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

``True`` if the samples should be mapped to array slices. A multisampled array expands each slice
in-place, so it would be slice 0: sample 0, slice 0: sample 1, slice 1: sample 0, etc.

This then follows the mapping for array slices as with any other array texture. :data:`sampleIndex`
is ignored.

"""

    sampleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

If :data:`mapToArray` is ``False`` this selects which sample should be extracted to treat as a
normal 2D image. If set to :data:`ResolveSamples` then instead there's a default average resolve.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    ResolveSamples = 4294967295
    __dict__ = None # (!) real value is ''


