# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class PathEntry(SwigPyObject):
    """ Properties of a path on a remote filesystem. """
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

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The filename of this path. This contains only the filename, not the full path."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`PathProperty` flags for this path."""

    lastmod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The last modified date of this path, as a unix timestamp in UTC."""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The size of the path in bytes."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


