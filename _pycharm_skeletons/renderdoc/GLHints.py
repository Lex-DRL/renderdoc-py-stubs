# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLHints(SwigPyObject):
    """ Describes the current state of GL hints and smoothing. """
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

    derivatives = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`QualityHint` with the derivatives hint."""

    lineSmoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`QualityHint` with the line smoothing hint."""

    lineSmoothingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if line smoothing is enabled."""

    polySmoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`QualityHint` with the polygon smoothing hint."""

    polySmoothingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if polygon smoothing is enabled."""

    textureCompression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`QualityHint` with the texture compression hint."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


