# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ConstantBlock(SwigPyObject):
    """
    Contains the information for a block of constant values. The values are not present,
    only the metadata about how the variables are stored in memory itself and their type/name
    information.
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

    bindPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The bindpoint for this block. This is an index in the
:data:`ShaderBindpointMapping.constantBlocks` list.

"""

    bufferBacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the contents are stored in a buffer of memory. If not then they are set by
some other API-specific method, such as direct function calls or they may be compile-time
specialisation constants.

"""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total number of bytes consumed by all of the constants contained in this block."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this constant block, may be empty on some APIs."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    variables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The constants contained within this block as a list of :class:`ShaderConstant`."""


    __dict__ = None # (!) real value is ''


