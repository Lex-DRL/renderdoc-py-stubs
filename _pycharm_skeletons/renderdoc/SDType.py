# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SDType(SwigPyObject):
    """ Details the name and properties of a structured type """
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

    basetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`SDBasic` category that this type belongs to."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The size in bytes that an instance of this type takes up.

This is only valid for whole chunks (where it contains the whole chunk size), for buffers that have
an arbitrary size, or for basic types such as integers and floating point values where it gives the
size/precision of the type.

For variable size types like structs, arrays, etc it will be set to 0.

"""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`SDTypeFlags` flags for this type."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this type."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


