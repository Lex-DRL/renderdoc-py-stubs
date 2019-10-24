# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKXFBBuffer(SwigPyObject):
    """ Describes a single transform feedback binding. """
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
    """A flag indicating if this buffer is active or not."""

    bufferResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the bound data buffer."""

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset in bytes to the start of the data in the :data:`bufferResourceId`."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size in bytes of the data buffer."""

    counterBufferOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset in bytes to the counter in the :data:`counterBufferResourceId`."""

    counterBufferResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the buffer storing the counter value (if set)."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


