# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class DebugMessage(SwigPyObject):
    """ A debugging message from the API validation or internal analysis and error detection. """
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

    category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`category <MessageCategory>` of this debug message."""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The string contents of the message."""

    eventId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :data:`eventId <APIEvent.eventId>` where this debug message was found."""

    messageID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An ID that identifies this particular debug message uniquely."""

    severity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`severity <MessageSeverity>` of this debug message."""

    source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`source <MessageSource>` of this debug message."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


