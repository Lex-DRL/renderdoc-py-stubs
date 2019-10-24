# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKMultiSample(SwigPyObject):
    """ Describes the multisampling state in the pipeline. """
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

    minSampleShading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum sample shading rate."""

    rasterSamples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many samples to use when rasterizing."""

    sampleLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`VKSampleLocations` with any custom sample locations that are configured."""

    sampleMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A mask that generated samples should be masked with using bitwise ``AND``."""

    sampleShadingEnable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if rendering should happen at sample-rate frequency."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


