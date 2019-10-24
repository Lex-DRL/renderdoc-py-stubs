# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class StencilFace(SwigPyObject):
    """ Describes the details of a stencil operation. """
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

    compareMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mask for testing stencil values."""

    depthFailOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the :class:`StencilOperation` to apply if the depth-test fails."""

    failOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`StencilOperation` to apply if the stencil-test fails."""

    function = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the :class:`CompareFunction` to use for testing stencil values."""

    passOperation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the :class:`StencilOperation` to apply if the stencil-test passes."""

    reference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The current stencil reference value."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    writeMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The mask for writing stencil values."""


    __dict__ = None # (!) real value is ''


