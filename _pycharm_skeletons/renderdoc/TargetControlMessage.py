# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TargetControlMessage(SwigPyObject):
    """ A message from a target control connection. """
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

    apiUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`API use data <APIUseData>`."""

    busy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`busy signal data <BusyData>`."""

    capProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The progress of an on-going capture.

When valid, will be in the range of 0.0 to 1.0 (0 - 100%). If not valid when a capture isn't going
or has finished, it will be -1.0

"""

    capturableWindowCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of the capturable windows"""

    newCapture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`new capture data <NewCaptureData>`."""

    newChild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`new child process data <NewChildData>`."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`type <TargetControlMessageType>` of message received"""


    __dict__ = None # (!) real value is ''


