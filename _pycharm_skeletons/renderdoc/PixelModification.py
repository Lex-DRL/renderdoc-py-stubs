# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class PixelModification(SwigPyObject):
    """ An attempt to modify a pixel by a particular event. """
    def Passed(self): # real signature unknown; restored from __doc__
        """
        Passed()
        
        Determine if this fragment passed all tests and wrote to the texture.
        
        :return: ``True`` if it passed all tests, ``False`` if it failed any.
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

    backfaceCulled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the backface culling test eliminated this fragment."""

    depthClipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if depth near/far clipping eliminated this fragment."""

    depthTestFailed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if depth testing eliminated this fragment."""

    directShaderWrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this event came as part of an arbitrary shader write."""

    eventId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :data:`eventId <APIEvent.eventId>` where the modification happened."""

    fragIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A 0-based index of which fragment this modification corresponds to, in the case that
multiple fragments from a single draw wrote to a pixel.

"""

    postMod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ModificationValue` of the texture after this fragment ran."""

    predicationSkipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if predicated rendering skipped this call."""

    preMod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ModificationValue` of the texture before this fragment ran.

This is valid only for the first fragment if multiple fragments in the same event write to the same
pixel.

"""

    primitiveID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The primitive that generated this fragment."""

    sampleMasked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the sample mask eliminated this fragment."""

    scissorClipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if scissor clipping eliminated this fragment."""

    shaderDiscarded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the pixel shader executed a discard on this fragment."""

    shaderOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ModificationValue` that this fragment wrote from the pixel shader."""

    stencilTestFailed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if stencil testing eliminated this fragment."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unboundPS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if no pixel shader was bound at this event."""

    viewClipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if viewport clipping eliminated this fragment."""


    __dict__ = None # (!) real value is ''


