# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12StreamOutBind(SwigPyObject):
    """ Describes a binding on the D3D12 stream-out stage. """
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

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The byte offset in :data:`resourceId` where the buffer view starts in the underlying
buffer.

"""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many bytes are in this stream-out buffer view."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the buffer."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writtenCountByteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The byte offset in :data:`writtenCountResourceId` where the stream-out count will be
written.

"""

    writtenCountResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the buffer where the written count will be stored."""


    __dict__ = None # (!) real value is ''


