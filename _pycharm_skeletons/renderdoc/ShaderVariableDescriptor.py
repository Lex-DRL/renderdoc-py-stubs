# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderVariableDescriptor(SwigPyObject):
    """ Describes the storage characteristics for a basic :class:`ShaderConstant` in memory. """
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

    arrayByteStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes between the start of one element in the array and the next."""

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of columns in this matrix."""

    elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of elements in the array, or 1 if it's not an array."""

    matrixByteStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes between the start of one column/row in a matrix and the next."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the type of this constant, e.g. a ``struct`` name."""

    rowMajorStorage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the matrix is stored as row major instead of column major."""

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of rows in this matrix."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`VarType` that this basic constant stores."""


    __dict__ = None # (!) real value is ''


