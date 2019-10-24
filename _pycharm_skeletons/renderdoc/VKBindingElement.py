# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKBindingElement(SwigPyObject):
    """ The contents of a single binding element within a descriptor set, possibly in an array. """
    def UseBorder(self): # real signature unknown; restored from __doc__
        """
        UseBorder()
        
        For samplers - check if the border color is used in this Vulkan sampler.
        
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
    """For samplers - the :class:`AddressMode` in the U direction."""

    addressV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the :class:`AddressMode` in the V direction."""

    addressW = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the :class:`AddressMode` in the W direction."""

    borderColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the RGBA border color."""

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For buffers - the byte offset where the buffer view starts in the underlying buffer."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For buffers - how many bytes are in this buffer view."""

    chromaFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - the :class:`FilterMode` describing the chroma filtering mode."""

    compareFunction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the :class:`CompareFunction` for comparison samplers."""

    dynamicallyUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if this binding element is dynamically used.

If set to ``False`` this means that the binding was available to the shader but during execution it
was not referenced. The data gathered for setting this variable is conservative, meaning that only
accesses through arrays will have this calculated to reduce the required feedback bandwidth - single
non-arrayed descriptors may have this value set to ``True`` even if the shader did not use them,
since single descriptors may only be dynamically skipped by control flow.

"""

    filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the :class:`TextureFilter` describing the filtering mode."""

    firstMip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For textures - the first mip level used in the view."""

    firstSlice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For 3D textures and texture arrays - the first slice used in the view."""

    forceExplicitReconstruction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - ``True`` if explicit reconstruction is force enabled."""

    immutableSampler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this is an immutable sampler binding."""

    maxAnisotropy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the maximum anisotropic filtering level to use."""

    maxLOD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the maximum mip level that can be used."""

    minLOD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - the minimum mip level that can be used."""

    mipBias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - a bias to apply to the calculated mip level before sampling."""

    numMips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For textures - the number of mip levels in the view."""

    numSlices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For 3D textures and texture arrays - the number of array slices in the view."""

    resourceResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the current underlying buffer or image object."""

    samplerResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the current sampler object."""

    swizzle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Four :class:`TextureSwizzle` elements indicating the swizzle applied to this texture."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unnormalized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For samplers - ``True`` if unnormalized co-ordinates are used in this sampler."""

    viewFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` that the view uses."""

    viewResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the current view object, if one is in use."""

    xChromaOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - the :class:`ChromaSampleLocation` X-axis chroma offset."""

    ycbcrModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - the :class:`YcbcrConversion` used for conversion."""

    ycbcrRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - the :class:`YcbcrRange` used for conversion."""

    ycbcrSampler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
For samplers - the :class:`ResourceId` of the ycbcr conversion object associated with
this sampler.

"""

    ycbcrSwizzle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
For ycbcr samplers - Four :class:`TextureSwizzle` elements indicating the swizzle
applied before conversion.

"""

    yChromaOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For ycbcr samplers - the :class:`ChromaSampleLocation` Y-axis chroma offset."""


    __dict__ = None # (!) real value is ''


