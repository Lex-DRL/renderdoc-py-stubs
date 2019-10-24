# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12Layout(SwigPyObject):
    """
    Describes a single D3D12 input layout element for one vertex input.
    
    .. data:: TightlyPacked
    
      Value for :data:`byteOffset` that indicates this element is tightly packed.
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

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The byte offset from the start of the vertex data in the vertex buffer from
:data:`inputSlot`.

If the value is :data:`TightlyPacked` then the element is packed tightly after the previous element, or 0
if this is the first element.

"""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` describing how the input data is interpreted."""

    inputSlot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The vertex buffer input slot where the data is sourced from."""

    instanceDataStepRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
If :data:`perInstance` is ``True`` then this is how many times each instance data is
used before advancing to the next instance.

E.g. if this value is two, then two instances will be drawn with the first instance data, then two
with the next instance data.

"""

    perInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the vertex data is instance-rate."""

    semanticIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The semantic index for this input."""

    semanticName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The semantic name for this input."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    TightlyPacked = 4294967295
    __dict__ = None # (!) real value is ''


