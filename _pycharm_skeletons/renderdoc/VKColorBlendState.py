# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKColorBlendState(SwigPyObject):
    """ Describes the pipeline blending state. """
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

    alphaToCoverageEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if alpha-to-coverage should be used when blending to an MSAA target."""

    alphaToOneEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if alpha-to-one should be used when blending to an MSAA target."""

    blendFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The constant blend factor to use in blend equations."""

    blends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of :class:`ColorBlend` with the blending configuration per-attachment."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


