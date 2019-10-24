# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12Shader(SwigPyObject):
    """ Describes a D3D12 shader stage. """
    def FindSpace(self, spaceIndex): # real signature unknown; restored from __doc__
        """
        FindSpace(spaceIndex)
        
        Return the index in the :data:`spaces` array of a given register space.
        
        :return: The index if the space exists, or ``-1`` if it doesn't.
        :rtype: ``int``
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

    bindpointMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A :class:`ShaderBindpointMapping` to match :data:`reflection` with the bindpoint
mapping data.

"""

    reflection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderReflection` describing the reflection data for this shader."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the shader object itself."""

    spaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`D3D12RegisterSpace` with the register spaces for this stage."""

    stage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A :class:`ShaderStage` identifying which stage this shader is bound to."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


