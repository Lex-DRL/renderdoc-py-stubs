# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLState(SwigPyObject):
    """ The full current OpenGL pipeline state. """
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

    atomicBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLBuffer` with the currently bound atomic buffers."""

    computeShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the compute shader stage."""

    depthState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLDepthState` describing depth processing."""

    fragmentShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the fragment shader stage."""

    framebuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLFrameBuffer` describing the framebuffer."""

    geometryShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the geometry shader stage."""

    hints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLHints` describing the hint state."""

    images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLImageLoadStore` with the currently bound load/store images."""

    pipelineResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the program pipeline (if active)."""

    rasterizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLRasterizer` describing rasterization."""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLSampler` with the currently bound samplers."""

    shaderStorageBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLBuffer` with the currently bound shader storage buffers."""

    stencilState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLStencilState` describing stencil processing."""

    tessControlShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the tessellation control shader stage."""

    tessEvalShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the tessellation evaluation shader stage."""

    textures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLTexture` with the currently bound textures."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    transformFeedback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLFeedback` describing the transform feedback stage."""

    uniformBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`GLBuffer` with the currently bound uniform buffers."""

    vertexInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLVertexInput` describing the vertex input stage."""

    vertexProcessing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLFixedVertexProcessing` describing the fixed-function vertex processing stage."""

    vertexShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLShader` describing the vertex shader stage."""


    __dict__ = None # (!) real value is ''


