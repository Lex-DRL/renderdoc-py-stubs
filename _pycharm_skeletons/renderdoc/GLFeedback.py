# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLFeedback(SwigPyObject):
    """ Describes the current feedback state. """
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

    active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the transform feedback object is currently active."""

    bufferResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ResourceId` with the buffer bindings."""

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``int`` with the buffer byte offsets."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``int`` with the buffer byte sizes."""

    feedbackResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the transform feedback binding."""

    paused = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the transform feedback object is currently paused."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


