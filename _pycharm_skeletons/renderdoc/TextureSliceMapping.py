# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TextureSliceMapping(SwigPyObject):
    """
    How to map array textures for saving to non-arrayed file formats.
    
    If :data:`sliceIndex` is -1, :data:`cubeCruciform` == :data:`slicesAsGrid` == ``False`` and the file
    format doesn't support saving all slices, only slice 0 is saved.
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

    cubeCruciform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Write out 6 slices in a cruciform pattern::

          +----+
          | +y |
          |    |
     +----+----+----+----+
     | -x | +z | +x | -z |
     |    |    |    |    |
     +----+----+----+----+
          | -y |
          |    |
          +----+

With the gaps filled in with transparent black.

"""

    sliceGridWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of a grid if :data:`slicesAsGrid` is ``True``."""

    sliceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Selects the (depth/array) slice to save.

If this is -1, then all slices are written out as detailed below. This is only supported in formats
that don't support slices natively, and will be done in RGBA8.

"""

    slicesAsGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

If ``True``, write out the slices as a 2D grid with the width given in :data:`sliceGridWidth`. Any
empty slices in the grid are written as transparent black.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


