# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SDChunkMetaData(SwigPyObject):
    """ The metadata that goes along with a :class:`SDChunk` to detail how it was recorded. """
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

    callstack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The frames of the CPU-side callstack leading up to the chunk."""

    chunkID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The internal chunk ID - unique given a particular driver in use."""

    durationMicro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The duration in microseconds that this chunk took. This is the time for the actual
work, not the serialising.
Since 0 is a possible value for this (for extremely fast calls), -1 is the invalid/not present value.

"""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`SDChunkFlags` for this chunk."""

    length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The length in bytes of this chunk - may be longer than the actual sum of the data if a
conservative size estimate was used on creation to avoid seeking to fix-up the stored length.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    threadID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The ID of the thread where this chunk was recorded."""

    timestampMicro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The point in time when this chunk was recorded, in microseconds since program start."""


    __dict__ = None # (!) real value is ''


