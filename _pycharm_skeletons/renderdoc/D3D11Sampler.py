# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11Sampler(SwigPyObject):
    """ Describes a sampler state object. """
    def UseBorder(self): # real signature unknown; restored from __doc__
        """
        UseBorder()
        
        Check if the border color is used in this D3D11 sampler.
        
        :return: ``True`` if the border color is used, ``False`` otherwise.
        :rtype: ``bool``
        """
        pass

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

    addressU = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`AddressMode` in the U direction."""

    addressV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`AddressMode` in the V direction."""

    addressW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`AddressMode` in the W direction."""

    borderColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The RGBA border color."""

    compareFunction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`CompareFunction` for comparison samplers."""

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureFilter` describing the filtering mode."""

    maxAnisotropy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum anisotropic filtering level to use."""

    maxLOD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum mip level that can be used."""

    minLOD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum mip level that can be used."""

    mipLODBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A bias to apply to the calculated mip level before sampling."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the sampler state object."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


