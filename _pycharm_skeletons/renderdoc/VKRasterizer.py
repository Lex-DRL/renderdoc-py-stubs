# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKRasterizer(SwigPyObject):
    """ Describes the rasterizer state in the pipeline. """
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

    conservativeRasterization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The active conservative rasterization mode."""

    cullMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`CullMode`."""

    depthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed depth bias value to apply to z-values."""

    depthBiasClamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

"""

    depthClampEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0``.

"""

    depthClipEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if pixels outside of the near and far depth planes should be clipped.

.. note::
  In Vulkan 1.0 this value was implicitly set to the opposite of :data:`depthClampEnable`, but with
  later extensions & versions it can be set independently.

"""

    extraPrimitiveOverestimationSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The extra size in pixels to increase primitives by during conservative rasterization,
in the x and y directions in screen space.

See :data:`conservativeRasterizationMode`

"""

    fillMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`FillMode`."""

    frontCCW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if counter-clockwise polygons are front-facing.
``False`` if clockwise polygons are front-facing.

"""

    lineRasterMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line rasterization mode."""

    lineStippleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line stipple factor, or 0 if line stipple is disabled."""

    lineStipplePattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The line stipple bit-pattern."""

    lineWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed line width in pixels."""

    rasterizerDiscardEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if primitives should be discarded during rasterization."""

    slopeScaledDepthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The slope-scaled depth bias value to apply to z-values."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


