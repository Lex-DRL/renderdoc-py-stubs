# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TextureSave(SwigPyObject):
    """ Describes a texture to save and how to map it to the destination file format. """
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

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Controls handling of alpha channel, mostly relevant for file formats that without
alpha.

It is an :class:`AlphaMapping` that controls what behaviour to use.

"""

    alphaCol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The background color if :data:`alpha` is set to :attr:`AlphaMapping.BlendToColor`"""

    channelExtract = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Selects a single component out of a texture to save as grayscale, or -1 to save all."""

    comp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Controls black/white point mapping for output formats that are normal
:attr:`8-bit SRGB <CompType.UNorm>`, values are

"""

    destType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`FileType` to use when saving to the destination file."""

    jpegQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The quality to use when saving to a ``JPG`` file. Valid values are between 1 and 100."""

    mip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Selects the mip to be written out.

If set to ``-1`` then all mips are written, where allowed by file format. If not allowed, mip 0 is
written

"""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the texture to save."""

    sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls mapping for multisampled textures (ignored if texture is not multisampled)"""

    slice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls mapping for arrayed textures (ignored if texture is not arrayed)"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    typeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """An optional :class:`CompType` hint to use when saving a typeless texture."""


    __dict__ = None # (!) real value is ''


