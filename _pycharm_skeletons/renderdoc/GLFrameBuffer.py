# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLFrameBuffer(SwigPyObject):
    """ Describes the current state of the framebuffer stage of the pipeline. """
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

    blendState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLBlendState` with the details of the blending state."""

    dither = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if dithering should be used when writing to color buffers."""

    drawFBO = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLFBO` with the information about a draw framebuffer."""

    framebufferSRGB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if sRGB correction should be applied when writing to an sRGB-formatted texture."""

    readFBO = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`GLFBO` with the information about a read framebuffer."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


