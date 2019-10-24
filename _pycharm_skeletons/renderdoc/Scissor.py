# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class Scissor(SwigPyObject):
    """ Describes a single scissor region. """
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

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this scissor region is enabled."""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height of the scissor region."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Width of the scissor region."""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X co-ordinate of the scissor region."""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y co-ordinate of the scissor region."""


    __dict__ = None # (!) real value is ''

