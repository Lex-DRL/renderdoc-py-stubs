# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SDFile(SwigPyObject):
    """ Contains the structured information in a file. Owns the buffers and chunks. """
    def Swap(self, other): # real signature unknown; restored from __doc__
        """
        Swap(other)
        
        The version of this structured stream, typically only used internally.
        """
        pass

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

    buffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A ``list`` of serialised buffers stored as ``bytes`` objects"""

    chunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A ``list`` of :class:`SDChunk` objects with the chunks in order."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of this structured stream, typically only used internally."""


    __dict__ = None # (!) real value is ''


