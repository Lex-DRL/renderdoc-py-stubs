# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLFixedVertexProcessing(SwigPyObject):
    """ Describes the setup for fixed vertex processing operations. """
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

    clipNegativeOneToOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the clip-space Z goes from ``-1`` to ``1``.

``False`` if the clip-space Z goes from ``0`` to ``1``.

"""

    clipOriginLowerLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the clipping origin should be in the lower left.

``False`` if it's in the upper left.

"""

    clipPlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``bool`` determining which user clipping planes are enabled."""

    defaultInnerLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``float`` giving the default inner level of tessellation."""

    defaultOuterLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``float`` giving the default outer level of tessellation."""

    discard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if primitives should be discarded during rasterization."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


