# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11BlendState(SwigPyObject):
    """ Describes a blend state object. """
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

    alphaToCoverage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if alpha-to-coverage should be used when blending to an MSAA target."""

    blendFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The constant blend factor to use in blend equations."""

    blends = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ColorBlend` describing the blend operations for each target."""

    independentBlend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if independent blending for each target should be used.

``False`` if the first blend should be applied to all targets.

"""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the blend state object."""

    sampleMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mask determining which samples are written to."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


