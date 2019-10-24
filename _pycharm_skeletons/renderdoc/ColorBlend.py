# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ColorBlend(SwigPyObject):
    """ Describes the blend configuration for a given output target. """
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

    alphaBlend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`BlendEquation` describing the blending for alpha values."""

    colorBlend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`BlendEquation` describing the blending for color values."""

    enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if blending is enabled for this target."""

    logicOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`LogicOperation` to use for logic operations, if
:data:`logicOperationEnabled` is ``True``.

"""

    logicOperationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the logic operation in :data:`logicOperation` should be used."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writeMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mask for writes to the render target."""


    __dict__ = None # (!) real value is ''


