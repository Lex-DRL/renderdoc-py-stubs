# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11InputAssembly(SwigPyObject):
    """ Describes the input assembler data. """
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

    bytecode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderReflection` describing the bytecode used to create the input layout."""

    indexBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`D3D11IndexBuffer` describing the index buffer."""

    layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11Layout` describing the input layout elements in this layout."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the layout object."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertexBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11VertexBuffer` with the vertex buffers that are bound."""


    __dict__ = None # (!) real value is ''


