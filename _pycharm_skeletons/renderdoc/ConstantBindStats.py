# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ConstantBindStats(SwigPyObject):
    """
    Contains the statistics for constant binds in a frame.
    
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

    bindslots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list where the Nth element contains the number of calls that bound N buffers."""

    calls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many function calls were made."""

    nulls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many objects were unbound."""

    sets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many objects were bound."""

    sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`bucketed <BucketType>` list over the sizes of buffers bound."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BucketCount = 31
    BucketType = 1
    __dict__ = None # (!) real value is ''


