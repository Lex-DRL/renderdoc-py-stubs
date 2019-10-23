# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SectionProperties(SwigPyObject):
    """ Properties of a section in a renderdoc capture file. """
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

    compressedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes of data in this section when compressed on disk."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The flags describing how this section is stored."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this section."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The type of this section, if it is a known pre-defined section."""

    uncompressedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes of data contained in this section, once uncompressed."""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The version of this section - the meaning of which is up to the type."""


    __dict__ = None # (!) real value is ''


