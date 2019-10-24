# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class APIEvent(SwigPyObject):
    """ An individual API-level event, generally corresponds one-to-one with an API call. """
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
    """A list of addresses in the CPU callstack where this function was called."""

    chunkIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The chunk index for this function call in the structured file."""

    eventId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The API event's Event ID.

This is a 1-based count of API events in the capture. The eventId is used as a reference point in
many places in the API to represent where in the capture the 'current state' is, and to perform
analysis in reference to the state at a particular point in the frame.

eventIds are always increasing and positive, but they may not be contiguous - in some circumstances
there may be gaps if some events are consumed entirely internally, such as debug marker pops which
only modify the internal drawcall tree structures.

Also eventIds may not correspond directly to an actual function call - sometimes a function such as
a multi draw indirect will be one function call that expands to multiple events to allow inspection
of results part way through the multi draw.

"""

    fileOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A byte offset in the data stream where this event happens.

.. note:: This should only be used as a relative measure, it is not a literal number of bytes from
  the start of the file on disk.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


