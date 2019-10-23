# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderResource(SwigPyObject):
    """
    Contains the information for a shader resource that is made accessible to shaders
    directly by means of the API resource binding system.
    
    .. note:: that constant blocks and samplers will not have a shader resource entry, see
      :class:`ConstantBlock` and :class:`ShaderSampler`.
    """
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

    bindPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The bindpoint for this block. This is an index in either the
:data:`ShaderBindpointMapping.readOnlyResources` list or
:data:`ShaderBindpointMapping.readWriteResources` list as appropriate (see :data:`isReadOnly`).

"""

    isReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if this resource is available to the shader for reading only, otherwise it is
able to be read from and written to arbitrarily.

"""

    isTexture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this resource is a texture, otherwise it is a buffer."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this resource."""

    resType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`TextureType` that describes the type of this resource."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    variableType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderVariableType` describing type of each element of this resource."""


    __dict__ = None # (!) real value is ''


