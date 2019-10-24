# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SigParameter(SwigPyObject):
    """
    The information describing an input or output signature element describing the interface
    between shader stages.
    
    .. data:: NoIndex
    
      Value for an index that means it is invalid or not applicable for this parameter.
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

    arrayIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If this element is part of an array, indicates the index, or :data:`NoIndex` if not."""

    channelUsedMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A bitmask indicating which components in the shader register are actually used by the
shader itself, for APIs that pack signatures together.

"""

    compCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of components used to store this element. See :data:`compType`."""

    compType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`component type <CompType>` of data that this element stores."""

    needSemanticIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A convenience flag - ``True`` if the semantic name is unique and no index is needed."""

    regChannelMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A bitmask indicating which components in the shader register are stored, for APIs that
pack signatures together.

"""

    regIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The index of the shader register/binding used to store this signature element.

This may be :data:`NoIndex` if the element is system-generated and not consumed by another shader
stage. See :data:`systemValue`.

"""

    semanticIdxName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The combined semantic name and index."""

    semanticIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The semantic index of this variable - see :data:`semanticName`."""

    semanticName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The semantic name of this variable, if the API uses semantic matching for bindings."""

    stream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Selects a stream for APIs that provide multiple output streams for the same named output."""

    systemValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ShaderBuiltin` value that this element contains."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    varName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this variable - may not be present in the metadata for all APIs."""


    NoIndex = 4294967295
    __dict__ = None # (!) real value is ''


