# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class FrameDescription(SwigPyObject):
    """ Contains frame-level global information """
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

    captureTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time when the capture was created, as a unix timestamp in UTC."""

    compressedFileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total file size of the whole capture in bytes, before decompression."""

    debugMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of debug messages that are not associated with any particular event."""

    fileOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The offset into the file of the start of the frame.

.. note:: Similarly to :data:`APIEvent.fileOffset` this should only be used as a relative measure,
  as it is not a literal number of bytes from the start of the file on disk.

"""

    frameNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Starting from frame #1 defined as the time from application startup to first present,
this counts the frame number when the capture was made.

.. note:: This value is only accurate if the capture was triggered through the default mechanism, if
  it was triggered from the application API it doesn't correspond to anything.

"""

    initDataSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The byte size of the section of the file that contains frame-initial contents."""

    persistentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The byte size of the section of the file that must be kept in memory persistently."""

    stats = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`frame statistics <FrameStatistics>`."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uncompressedFileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The total file size of the whole capture in bytes, after decompression."""


    __dict__ = None # (!) real value is ''


