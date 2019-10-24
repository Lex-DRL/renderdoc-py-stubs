# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLRasterizerState(SwigPyObject):
    """ Describes the rasterizer state toggles. """
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

    alphaToCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if alpha-to-coverage should be used when blending to an MSAA target."""

    alphaToOne = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if alpha-to-one should be used when blending to an MSAA target."""

    cullMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`CullMode`."""

    depthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed depth bias value to apply to z-values."""

    depthClamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if pixels outside of the near and far depth planes should be clamped and
to ``0.0`` to ``1.0`` and not clipped.

"""

    fillMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The polygon :class:`FillMode`."""

    frontCCW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if counter-clockwise polygons are front-facing.
``False`` if clockwise polygons are front-facing.

"""

    lineWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed line width in pixels."""

    minSampleShadingRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum sample shading rate."""

    multisampleEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if multisampling should be used during rendering."""

    offsetClamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The clamp value for calculated depth bias from :data:`depthBias` and
:data:`slopeScaledDepthBias`

"""

    pointFadeThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The threshold value at which points are clipped if they exceed this size."""

    pointOriginUpperLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the point sprite texture origin is upper-left. ``False`` if lower-left."""

    pointSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The fixed point size in pixels."""

    programmablePointSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the point size can be programmably exported from a shader."""

    sampleCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if a temporary mask using :data:`sampleCoverageValue` should be used to
resolve the final output color.

"""

    sampleCoverageInvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the temporary sample coverage mask should be inverted."""

    sampleCoverageValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sample coverage value used if :data:`sampleCoverage` is ``True``."""

    sampleMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the generated samples should be bitwise ``AND`` masked with
:data:`sampleMaskValue`.

"""

    sampleMaskValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The sample mask value that should be masked against the generated coverage."""

    sampleShading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if rendering should happen at sample-rate frequency."""

    slopeScaledDepthBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The slope-scaled depth bias value to apply to z-values."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


