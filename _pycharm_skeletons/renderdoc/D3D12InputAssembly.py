# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12InputAssembly(SwigPyObject):
    """ Describes the input assembler state in the PSO. """
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

    indexBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`D3D12IndexBuffer` describing the index buffer."""

    indexStripCutValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The index value to use for cutting strips. Either ``0``, ``0xffff`` or ``0xffffffff``.
If the value is 0, strip cutting is disabled.

"""

    layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D12Layout` describing the input layout elements in this layout."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vertexBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D12VertexBuffer` with the vertex buffers that are bound."""


    __dict__ = None # (!) real value is ''


