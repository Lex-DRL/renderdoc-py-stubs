# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class LocalVariableMapping(SwigPyObject):
    """
    Maps the contents of a high-level local variable to one or more shader variables in a
    :class:`ShaderDebugState`, with type information.
    
    A single high-level variable may be represented by multiple mappings but only along regular
    boundaries, typically whole vectors. For example an array may have each element in a different
    mapping, or a matrix may have a mapping per row. The properties such as :data:`rows` and
    :data:`elements` reflect the *parent* object.
    
    Since locals don't always map directly this can change over time.
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

    builtin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The shader builtin this variable corresponds to."""

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of columns in this variable."""

    elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of array elements in this variable."""

    localName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name and member of this local variable that's being mapped from."""

    regCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of valid entries in :data:`registers`."""

    registers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The registers that the components of this variable map to. Multiple ranges could refer
to the same register if a contiguous range is mapped to - the mapping is component-by-component to
greatly simplify algorithms at the expense of a small amount of storage space.

"""

    rows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of rows in this variable - 1 for vectors, >1 for matrices."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The variable type of the local being mapped from, if the register is untyped."""


    __dict__ = None # (!) real value is ''


