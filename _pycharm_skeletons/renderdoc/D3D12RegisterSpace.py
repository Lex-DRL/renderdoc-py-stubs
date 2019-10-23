# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12RegisterSpace(SwigPyObject):
    """ Contains all of the registers in a single register space mapped to by a root signature. """
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

    constantBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of :class:`D3D12ConstantBuffer` containing the constant buffers."""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of :class:`D3D12Sampler` containing the samplers."""

    spaceIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of this space, since space indices can be sparse"""

    srvs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of :class:`D3D12View` containing the SRVs."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uavs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of :class:`D3D12View` containing the UAVs."""


    __dict__ = None # (!) real value is ''


