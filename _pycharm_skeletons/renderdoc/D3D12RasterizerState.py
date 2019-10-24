# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12RasterizerState(SwigPyObject):
    """ Describes the rasterizer state in the PSO. """
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

    antialiasedLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if lines should be anti-aliased. Ignored if :data:`multisampleEnable` is ``False``."""

    conservativeRasterization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current :class:`ConservativeRaster` mode."""

    cullMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`CullMode`."""

    depthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed depth bias value to apply to z-values."""

    depthBiasClamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

"""

    depthClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if pixels outside of the near and far depth planes should be clipped."""

    fillMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`FillMode`."""

    forcedSampleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A sample count to force rasterization to when UAV rendering or rasterizing, or 0 to
not force any sample count.

"""

    frontCCW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if counter-clockwise polygons are front-facing.
``False`` if clockwise polygons are front-facing.

"""

    multisampleEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the quadrilateral MSAA algorithm should be used on MSAA targets."""

    slopeScaledDepthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The slope-scaled depth bias value to apply to z-values."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


