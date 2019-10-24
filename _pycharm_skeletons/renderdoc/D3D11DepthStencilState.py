# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11DepthStencilState(SwigPyObject):
    """ Describes a depth-stencil state object. """
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

    backFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`StencilFace` describing what happens for back-facing polygons."""

    depthEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if depth testing should be performed."""

    depthFunction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`CompareFunction` to use for testing depth values."""

    depthWrites = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if depth values should be written to the depth target."""

    frontFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`StencilFace` describing what happens for front-facing polygons."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the depth-stencil state object."""

    stencilEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if stencil operations should be performed."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


