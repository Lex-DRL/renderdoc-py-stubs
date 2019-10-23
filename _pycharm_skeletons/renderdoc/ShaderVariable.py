# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderVariable(SwigPyObject):
    """
    Holds a single named shader variable. It contains either a primitive type (up to a 4x4
    matrix of a :class:`basic type <VarType>`) or a list of members, which can either be struct or array
    members of this parent variable.
    
    Matrices are always stored row-major. If necessary they are transposed when retrieving from the raw
    data bytes when they are specified to be column-major in the API/shader metadata.
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

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of columns in this matrix."""

    displayAsHex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the contents of this variable should be displayed as hex."""

    isStruct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this variable is a structure and not an array or basic type."""

    members = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The members of this variable as a list of :class:`ShaderVariable`."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this variable."""

    rowMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this variable is stored in rows in memory. Only relevant for matrices."""

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of rows in this matrix."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`basic type <VarType>` of this variable."""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`contents <ShaderValue>` of this variable if it has no members."""


    __dict__ = None # (!) real value is ''


