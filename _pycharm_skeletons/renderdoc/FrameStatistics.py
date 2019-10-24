# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class FrameStatistics(SwigPyObject):
    """
    Contains all the available statistics about the captured frame.
    
    Currently this information is only available on D3D11 and is fairly API-centric.
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

    blends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about blend state binds."""

    constants = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of constant buffer bind statistics, one per each :class:`stage <ShaderStage>`."""

    depths = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about depth-stencil state binds."""

    dispatches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about compute dispatches."""

    draws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about drawcalls."""

    indices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about index buffer binds."""

    layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about vertex layout binds."""

    outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about output merger and UAV binds."""

    rasters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about rasterizer state binds."""

    recorded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the statistics in this structure are valid."""

    resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of resource bind statistics, one per each :class:`stage <ShaderStage>`."""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of sampler bind statistics, one per each :class:`stage <ShaderStage>`."""

    shaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of shader bind statistics, one per each :class:`stage <ShaderStage>`."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    updates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about resource contents updates."""

    vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Information about vertex buffer binds."""


    __dict__ = None # (!) real value is ''


