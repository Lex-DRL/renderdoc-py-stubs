# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ResourceUpdateStats(SwigPyObject):
    """
    Contains the statistics for resource updates in a frame.
    
    .. data:: BucketType
    
      The type of buckets being used. See :class:`BucketRecordType`.
    
    .. data:: BucketCount
    
      How many buckets there are in the arrays.
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

    calls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many function calls were made."""

    clients = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many of :data:`calls` were mapped pointers written by the CPU."""

    servers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many of :data:`calls` were batched updates written in the command queue."""

    sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`bucketed <BucketType>` list over the number of bytes in the update."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A list with one element for each type in :class:`TextureType`.

The Nth element contains the number of times a resource of that type was updated.

"""


    BucketCount = 31
    BucketType = 1
    __dict__ = None # (!) real value is ''


