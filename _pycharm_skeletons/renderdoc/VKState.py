# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKState(SwigPyObject):
    """ The full current Vulkan pipeline state. """
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

    colorBlend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKColorBlendState` describing color blending."""

    compute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKPipeline` with the currently bound compute pipeline, if any."""

    computeShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the compute shader stage."""

    conditionalRendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ConditionalRendering` describing the current conditional rendering state."""

    currentPass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKCurrentPass` describing the current renderpass, subpass and framebuffer."""

    depthStencil = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKDepthStencil` describing the depth-stencil stage."""

    fragmentShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the fragment shader stage."""

    geometryShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the geometry shader stage."""

    graphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKPipeline` with the currently bound graphics pipeline, if any."""

    images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`VKImageData` entries, one for each image."""

    inputAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKInputAssembly` describing the input assembly stage."""

    multisample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKMultiSample` describing the multisample setup."""

    pushconsts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A ``bytes`` containing the raw push constant data."""

    rasterizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKRasterizer` describing rasterization."""

    tessControlShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the tessellation control shader stage."""

    tessellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKTessellation` describing the tessellation stage."""

    tessEvalShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the tessellation evaluation shader stage."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transformFeedback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKTransformFeedback` describing the tessellation stage."""

    vertexInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKVertexInput` describing the vertex input stage."""

    vertexShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKShader` describing the vertex shader stage."""

    viewportScissor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`VKViewState` describing the viewport setup."""


    __dict__ = None # (!) real value is ''


