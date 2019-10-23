# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11OutputMerger(SwigPyObject):
    """ Describes the current state of the output-merger stage of the D3D11 pipeline. """
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

    blendState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11BlendState` with the details of the blend state."""

    depthReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if depth access to the depth-stencil target is read-only."""

    depthStencilState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11DepthStencilState` with the details of the depth-stencil state."""

    depthTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D11View` with details of the bound depth-stencil target."""

    renderTargets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11View` describing the bound render targets."""

    stencilReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if stencil access to the depth-stencil target is read-only."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uavs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11View` describing the bound UAVs."""

    uavStartSlot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Which slot in the output targets is the first UAV."""


    __dict__ = None # (!) real value is ''


