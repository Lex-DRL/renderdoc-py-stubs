# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class BoundResource(SwigPyObject):
    """ Information about a single resource bound to a slot in an API-specific way. """
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

    dynamicallyUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if this binding element is dynamically used.

Some APIs provide fine-grained usage based on dynamic shader feedback, to support 'bindless'
scenarios where only a small sparse subset of bound resources are actually used.

"""

    firstMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For textures, the highest mip level available on this binding, or -1 for all mips"""

    firstSlice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For textures, the first array slice available on this binding. or -1 for all slices."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`~renderdoc.ResourceId` identifying the bound resource."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For textures, a :class:`~renderdoc.CompType` hint for how to interpret typeless textures."""


    __dict__ = None # (!) real value is ''


