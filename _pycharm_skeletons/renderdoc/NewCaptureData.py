# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class NewCaptureData(SwigPyObject):
    """ Information about the a new capture created by the target. """
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

    api = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The API used for this capture, if available.

.. note::
  May be empty if running with an older version of RenderDoc

"""

    captureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An identifier to use to refer to this capture."""

    frameNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The frame number that this capture came from."""

    local = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the target is running on the local system."""

    path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The local path on the target system where the capture is saved."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thumbHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The height of the image contained in :data:`thumbnail`."""

    thumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw bytes that contain the capture thumbnail, as RGB8 data."""

    thumbWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width of the image contained in :data:`thumbnail`."""

    timestamp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The time the capture was created, as a unix timestamp in UTC."""


    __dict__ = None # (!) real value is ''


