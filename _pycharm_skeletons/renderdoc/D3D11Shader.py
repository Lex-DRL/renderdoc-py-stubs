# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D11Shader(SwigPyObject):
    """ Describes a D3D11 shader stage. """
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

    bindpointMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A :class:`ShaderBindpointMapping` to match :data:`reflection` with the bindpoint
mapping data.

"""

    classInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of ``str`` with the bound class instance names."""

    constantBuffers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11ConstantBuffer` with the bound constant buffers."""

    reflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderReflection` describing the reflection data for this shader."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the shader itself."""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11Sampler` with the bound samplers."""

    srvs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11View` with the bound SRVs."""

    stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderStage` identifying which stage this shader is bound to."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    uavs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D11View` with the bound UAVs - only valid for the compute stage."""


    __dict__ = None # (!) real value is ''


