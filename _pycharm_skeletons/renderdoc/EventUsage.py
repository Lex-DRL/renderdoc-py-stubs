# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class EventUsage(SwigPyObject):
    """ Describes a particular use of a resource at a specific :data:`eventId <APIEvent.eventId>`. """
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

    eventId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :data:`eventId <APIEvent.eventId>` where this usage happened."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    usage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceUsage` in question."""

    view = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An optional :class:`ResourceId` identifying the view through which the use happened."""


    __dict__ = None # (!) real value is ''


