# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TextureDisplay(SwigPyObject):
    """
    Describes how to render a texture preview of an image. Describes the zoom and pan settings for the
    texture when rendering on a particular output, as well as the modification and selection of a
    particular subresource (such as array slice, mip or multi-sampled sample).
    
    .. note::
      X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
      APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
      fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
      bottom-left co-ordinates, care must be taken to translate them.
    
    .. data:: ResolveSamples
    
      Value for :data:`sampleIdx` if the samples should be averaged.
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

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the alpha channel should be visible. If enabled with any of RGB, the
texture will be blended to the background color or checkerboard.

If only one channel is selected, it will be rendered in grayscale

"""

    backgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The background color to use behind the texture display.

If set to (0, 0, 0, 0) the global checkerboard colors are used.

"""

    blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the blue channel should be visible.

If only one channel is selected, it will be rendered in grayscale

"""

    customShaderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ResourceId` of a custom shader to use when rendering.

See :meth:`ReplayController.BuildCustomShader` for creating an appropriate custom shader.

"""

    decodeYUV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the texture should be decoded as if it contains YUV data."""

    flipY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the texture should be flipped vertically when rendering."""

    green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the green channel should be visible.

If only one channel is selected, it will be rendered in grayscale

"""

    hdrMultiplier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If ``>= 0.0`` the RGBA values will be viewed as HDRM with this as the multiplier."""

    linearDisplayAsGamma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the texture should be interpreted as gamma.

See :ref:`the FAQ entry <gamma-linear-display>`.

"""

    mip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Select the mip of the texture to display."""

    overlay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Selects a :class:`DebugOverlay` to draw over the top of the texture."""

    rangeMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value in each channel to map to the white point."""

    rangeMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The value in each channel to map to the black point."""

    rawOutput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the rendered image should be as close as possible in value to the input.

This is primarily useful when rendering to a floating point target for retrieving pixel data from
the input texture in cases where it isn't easy to directly fetch the input texture data.

"""

    red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the red channel should be visible.

If only one channel is selected, it will be rendered in grayscale

"""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the texture to display."""

    sampleIdx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Select the sample of the texture to display if it's a multi-sampled texture.

If this is set to :data:`ResolveSamples` then a default resolve will be performed that averages all
samples.

"""

    scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The scale to apply to the texture when rendering as a floating point value.

``1.0`` corresponds to ``100%``

"""

    sliceFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Select the slice or face of the texture to display if it's an array, 3D, or cube tex."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An optional :class:`CompType` hint to use when displaying a typeless texture."""

    xOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset to pan in the X axis."""

    yOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset to pan in the Y axis."""


    ResolveSamples = 4294967295
    __dict__ = None # (!) real value is ''


