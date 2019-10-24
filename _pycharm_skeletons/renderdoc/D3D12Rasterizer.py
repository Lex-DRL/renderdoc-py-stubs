# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12Rasterizer(SwigPyObject):
    """ Describes the rasterization state of the D3D12 pipeline. """
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

    sampleMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mask determining which samples are written to."""

    scissors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`Scissor` with the bound scissor regions."""

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`D3D12RasterizerState` with the details of the rasterization state."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    viewports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`Viewport` with the bound viewports."""


    __dict__ = None # (!) real value is ''


