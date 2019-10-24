# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12State(SwigPyObject):
    """ The full current D3D12 pipeline state. """
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

    computeShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the compute shader stage."""

    domainShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the domain shader stage."""

    geometryShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the geometry shader stage."""

    hullShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the hull shader stage."""

    inputAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12InputAssembly` describing the input assembly pipeline stage."""

    outputMerger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12OM` describing the output merger pipeline stage."""

    pipelineResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the pipeline state object."""

    pixelShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the pixel shader stage."""

    rasterizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Rasterizer` describing the rasterizer pipeline stage."""

    resourceStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D12ResourceData` entries, one for each resource."""

    rootSignatureResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the root signature object."""

    streamOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12StreamOut` describing the stream-out pipeline stage."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertexShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12Shader` describing the vertex shader stage."""


    __dict__ = None # (!) real value is ''


