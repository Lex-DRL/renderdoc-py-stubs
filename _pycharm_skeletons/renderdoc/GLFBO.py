# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GLFBO(SwigPyObject):
    """ Describes the contents of a framebuffer object. """
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

    colorAttachments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of :class:`GLAttachment` with the framebuffer color attachments."""

    depthAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`GLAttachment` with the framebuffer depth attachment."""

    drawBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of draw buffer indices into the :data:`colorAttachments` attachment list."""

    readBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The read buffer index in the :data:`colorAttachments` attachment list."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the framebuffer."""

    stencilAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`GLAttachment` with the framebuffer stencil attachment."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


