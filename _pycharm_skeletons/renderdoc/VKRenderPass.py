# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKRenderPass(SwigPyObject):
    """ Describes the setup of a renderpass and subpasses. """
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
    """A list of indices into the framebuffer attachments for color attachments."""

    depthstencilAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
An index into the framebuffer attachments for the depth-stencil attachment.

If there is no depth-stencil attachment, this index is ``-1``.

"""

    fragmentDensityAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
An index into the framebuffer attachments for the fragment density attachment.

If there is no fragment density attachment, this index is ``-1``.

"""

    inputAttachments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of indices into the framebuffer attachments for input attachments."""

    multiviews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
If multiview is enabled, contains a list of view indices to be broadcast to during
rendering.

If the list is empty, multiview is disabled and rendering is as normal.

"""

    resolveAttachments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of indices into the framebuffer attachments for resolve attachments."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the render pass."""

    subpass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the current active subpass."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


