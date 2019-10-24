# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ShaderBindpointMapping(SwigPyObject):
    """
    This structure goes hand in hand with :class:`ShaderReflection` to determine how to map
    from bindpoint indices in the resource lists there to API-specific binding points. The ``bindPoint``
    member in :class:`ShaderResource` or :class:`ConstantBlock` refers to an index in these associated
    lists, which then map potentially sparsely and potentially in different orders to the appropriate
    API registers, indices, or slots.
    
    API specific details:
    
    * Direct3D11 - All :data:`Bindpoint.bindset` values are 0 as D3D11 has no notion of sets, and the
      only namespacing that exists is by shader stage and object type. Mostly this already exists with
      the constant block, read only and read write resource lists.
    
      :data:`Bindpoint.arraySize` is likewise unused as D3D11 doesn't have arrayed resource bindings.
    
      :data:`Bindpoint.bind` refers to the register/slot binding within the appropriate type (SRVs for
      read-only resources, UAV for read-write resources, samplers/constant buffers in each type).
    
    * OpenGL - Similarly to D3D11, :data:`Bindpoint.bindset` and :data:`Bindpoint.arraySize` are
      unused as OpenGL does not have true binding sets or array resource binds.
    
      For OpenGL there may be many more duplicate :class:`Bindpoint` objects as the
      :data:`Bindpoint.bind` refers to the index in the type-specific list, which is much more
      granular on OpenGL. E.g. ``0`` may refer to images, storage buffers, and atomic buffers all within
      the :data:`readWriteResources` list. The index is the uniform value of the binding. Since no
      objects are namespaced by shader stage, the same value in two shaders refers to the same binding.
    
    * Direct3D12 - Since D3D12 doesn't have true resource arrays (they are linearised into sequential
      registers) :data:`Bindpoint.arraySize` is not used.
    
      :data:`Bindpoint.bindset` corresponds to register spaces, with :data:`Bindpoint.bind` then
      mapping to the register within that space. The root signature then maps these registers to
      descriptors.
    
    * Vulkan - For Vulkan :data:`Bindpoint.bindset` corresponds to the index of the descriptor set,
      and :data:`Bindpoint.bind` refers to the index of the descriptor within that set.
      :data:`Bindpoint.arraySize` also is used as descriptors in Vulkan can be true arrays, bound all
      at once to a single binding.
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
    """
Provides a list of :class:`Bindpoint` entries for remapping the
:data:`ShaderReflection.constantBlocks` list.

"""

    inputAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
This maps input attributes as a simple swizzle on the
:data:`ShaderReflection.inputSignature` indices for APIs where this mapping is mutable at runtime.

"""

    readOnlyResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Provides a list of :class:`Bindpoint` entries for remapping the
:data:`ShaderReflection.readOnlyResources` list.

"""

    readWriteResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Provides a list of :class:`Bindpoint` entries for remapping the
:data:`ShaderReflection.readWriteResources` list.

"""

    samplers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Provides a list of :class:`Bindpoint` entries for remapping the
:data:`ShaderReflection.samplers` list.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


