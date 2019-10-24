# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class CaptureFileFormat(SwigPyObject):
    """ The format for a capture file either supported to read from, or export to """
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

    convertSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates whether captures or structured data can be saved out in this format."""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A human readable long-form description of the file format."""

    extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The file of the format as a single minimal string, e.g. ``rdc``."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A human readable short phrase naming the file format."""

    openSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Indicates whether or not files in this format can be opened and processed as
structured data.

"""

    requiresBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Indicates whether exporting to this format requires buffers or just structured data.
If it doesn't require buffers then it can be exported directly from an opened capture, which by
default has structured data but no buffers available.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


