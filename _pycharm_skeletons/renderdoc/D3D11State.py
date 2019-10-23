# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11State(SwigPyObject):
    """ The full current D3D11 pipeline state. """
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
    """A :class:`D3D11Shader` describing the compute shader stage."""

    domainShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Shader` describing the domain shader stage."""

    geometryShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Shader` describing the geometry shader stage."""

    hullShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Shader` describing the hull shader stage."""

    inputAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11InputAssembly` describing the input assembly pipeline stage."""

    outputMerger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11OutputMerger` describing the output merger pipeline stage."""

    pixelShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Shader` describing the pixel shader stage."""

    predication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Predication` describing the predicated rendering state."""

    rasterizer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Rasterizer` describing the rasterizer pipeline stage."""

    streamOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11StreamOut` describing the stream-out pipeline stage."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertexShader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11Shader` describing the vertex shader stage."""


    __dict__ = None # (!) real value is ''


