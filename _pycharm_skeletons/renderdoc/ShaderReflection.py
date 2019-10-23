# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderReflection(SwigPyObject):
    """
    The reflection and metadata fully describing a shader.
    
    The information in this structure is API agnostic, and is matched up against a
    :class:`ShaderBindpointMapping` instance to map the information here to the API's binding points
    and resource binding scheme.
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

    constantBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ConstantBlock` with the shader's constant bindings."""

    debugInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderDebugInfo` containing any embedded debugging information in this shader."""

    dispatchThreadsDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 3D dimensions of a compute workgroup, for compute shaders."""

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ShaderEncoding` of this shader. See :data:`rawBytes`."""

    entryPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The entry point in the shader for this reflection, if multiple entry points exist."""

    inputSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`SigParameter` with the shader's input signature."""

    interfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of strings with the shader's interfaces. Largely an unused API feature."""

    outputSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`SigParameter` with the shader's output signature."""

    rawBytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A raw ``bytes`` dump of the original shader, encoded in the form denoted by
:data:`encoding`.

"""

    readOnlyResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ShaderResource` with the shader's read-only resources."""

    readWriteResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ShaderResource` with the shader's read-write resources."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of this shader."""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`ShaderSampler` with the shader's samplers."""

    stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ShaderStage` that this shader corresponds to, if multiple entry points exist."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


