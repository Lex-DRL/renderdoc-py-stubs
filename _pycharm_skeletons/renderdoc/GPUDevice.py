# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class GPUDevice(SwigPyObject):
    """ Describes a single GPU at replay time. """
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

    apis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The list of APIs that this device supports."""

    deviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The PCI deviceID of this GPU."""

    driver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of the driver of this GPU, if multiple drivers are available for it."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The human-readable name of this GPU."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`GPUVendor` of this GPU."""


    __dict__ = None # (!) real value is ''


