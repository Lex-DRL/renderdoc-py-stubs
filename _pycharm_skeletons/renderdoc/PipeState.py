# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class PipeState(SwigPyObject):
    """
    An API-agnostic view of the common aspects of the pipeline state. This allows simple
    access to e.g. find out the bound resources or vertex buffers, or certain pipeline state which is
    available on all APIs.
    
    For more detailed or precise information without abstraction, access the specific pipeline state
    for the capture that's open.
    """
    def Abbrev(self, stage): # real signature unknown; restored from __doc__
        """
        Abbrev(stage)
        
        Retrieves a suitable two or three letter abbreviation of the given shader stage.
        
        :param ShaderStage stage: The shader stage to abbreviate.
        :return: The abbreviation of the stage.
        :rtype: ``str``
        """
        pass

    def GetBindpointMapping(self, stage): # real signature unknown; restored from __doc__
        """
        GetBindpointMapping(stage)
        
        Retrieves the current bindpoint mapping for a shader stage.
        
        This returns an empty bindpoint mapping if no shader is bound.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The bindpoint mapping for the given shader.
        :rtype: ShaderBindpointMapping
        """
        pass

    def GetComputePipelineObject(self): # real signature unknown; restored from __doc__
        """
        GetComputePipelineObject()
        
        Retrieves the the compute pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass

    def GetConstantBuffer(self, stage, BufIdx, ArrayIdx): # real signature unknown; restored from __doc__
        """
        GetConstantBuffer(stage, BufIdx, ArrayIdx)
        
        Retrieves the constant buffer at a given binding.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :param int BufIdx: The index in the shader's ConstantBlocks array to look up.
        :param int ArrayIdx: For APIs that support arrays of constant buffers in a single binding, the index
          in that array to look up.
        :return: The constant buffer at the specified binding.
        :rtype: BoundCBuffer
        """
        pass

    def GetDepthTarget(self): # real signature unknown; restored from __doc__
        """
        GetDepthTarget()
        
        Retrieves the read/write resources bound to the depth-stencil output.
        
        :return: The currently bound depth-stencil resource.
        :rtype: BoundResource
        """
        pass

    def GetGraphicsPipelineObject(self): # real signature unknown; restored from __doc__
        """
        GetGraphicsPipelineObject()
        
        Retrieves the the graphics pipeline state object, if applicable.
        
        :return: The object ID for the given pipeline object.
        :rtype: ResourceId
        """
        pass

    def GetIBuffer(self): # real signature unknown; restored from __doc__
        """
        GetIBuffer()
        
        Retrieves the current index buffer binding.
        
        :return: A :class:`BoundVBuffer` with the index buffer details. The stride is always 0.
        :rtype: ``BoundVBuffer``
        """
        pass

    def GetOutputTargets(self): # real signature unknown; restored from __doc__
        """
        GetOutputTargets()
        
        Retrieves the resources bound to the color outputs.
        
        :return: The currently bound output targets.
        :rtype: ``list`` of :class:`BoundResource`.
        """
        pass

    def GetReadOnlyResources(self, stage): # real signature unknown; restored from __doc__
        """
        GetReadOnlyResources(stage)
        
        Retrieves the read-only resources bound to a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :return: The currently bound read-only resoruces.
        :rtype: ``list`` of :class:`BoundResourceArray` entries
        """
        pass

    def GetReadWriteResources(self, stage): # real signature unknown; restored from __doc__
        """
        GetReadWriteResources(stage)
        
        Retrieves the read/write resources bound to a particular shader stage.
        
        :param ShaderStage stage: The shader stage to fetch from.
        :return: The currently bound read/write resoruces.
        :rtype: ``list`` of :class:`BoundResourceArray` entries
        """
        pass

    def GetResourceLayout(self, id): # real signature unknown; restored from __doc__
        """
        GetResourceLayout(id)
        
        For APIs that have explicit barriers, retrieves the current layout of a resource.
        
        :return: The name of the current resource layout.
        :rtype: ``str``
        """
        pass

    def GetScissor(self, index): # real signature unknown; restored from __doc__
        """
        GetScissor(index)
        
        Retrieves the scissor region for a given index.
        
        :param int index: The index to retrieve.
        :return: The scissor region for the given index.
        :rtype: Scissor
        """
        pass

    def GetShader(self, stage): # real signature unknown; restored from __doc__
        """
        GetShader(stage)
        
        Retrieves the object ID of the shader bound at a shader stage.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The object ID for the given shader.
        :rtype: ResourceId
        """
        pass

    def GetShaderEntryPoint(self, stage): # real signature unknown; restored from __doc__
        """
        GetShaderEntryPoint(stage)
        
        Retrieves the name of the entry point function for a shader stage.
        
        For some APIs that don't distinguish by entry point, this may be empty.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The entry point name for the given shader.
        :rtype: ``str``
        """
        pass

    def GetShaderReflection(self, stage): # real signature unknown; restored from __doc__
        """
        GetShaderReflection(stage)
        
        Retrieves the shader reflection information for a shader stage.
        
        This returns ``None`` if no shader is bound.
        
        :param ShaderStage stage: The shader stage to fetch.
        :return: The reflection data for the given shader.
        :rtype: :class:`ShaderReflection` or ``None``
        """
        pass

    def GetStripRestartIndex(self): # real signature unknown; restored from __doc__
        """
        GetStripRestartIndex()
        
        Retrieves the primitive restart index.
        
        :param int indexByteWidth: The width in bytes of the indices.
        :return: The index value that represents a strip restart not a real index.
        :rtype: ``int``
        """
        pass

    def GetVBuffers(self): # real signature unknown; restored from __doc__
        """
        GetVBuffers()
        
        Retrieves the currently bound vertex buffers.
        
        :return: The list of bound vertex buffers.
        :rtype: ``list`` of :class:`BoundVBuffer`.
        """
        pass

    def GetVertexInputs(self): # real signature unknown; restored from __doc__
        """
        GetVertexInputs()
        
        Retrieves the currently specified vertex attributes.
        
        :return: The list of current vertex attributes.
        :rtype: ``list`` of :class:`VertexInputAttribute`.
        """
        pass

    def GetViewport(self, index): # real signature unknown; restored from __doc__
        """
        GetViewport(index)
        
        Retrieves the viewport for a given index.
        
        :param int index: The index to retrieve.
        :return: The viewport for the given index.
        :rtype: Viewport
        """
        pass

    def HasAlignedPostVSData(self, stage): # real signature unknown; restored from __doc__
        """
        HasAlignedPostVSData(stage)
        
        Determines whether or not the PostVS data is aligned in the typical fashion (ie.
        vectors not crossing ``float4`` boundaries). APIs that use stream-out or transform feedback have
        tightly packed data, but APIs that rewrite shaders to dump data might have these alignment
        requirements.
        
        :param MeshDataStage stage: The mesh data stage for the output data.
        :return: A boolean indicating if post-VS data is aligned.
        :rtype: ``bool``
        """
        pass

    def IsCaptureD3D11(self): # real signature unknown; restored from __doc__
        """
        IsCaptureD3D11()
        
        Determines whether or not a D3D11 capture is currently loaded.
        
        :return: A boolean indicating if a D3D11 capture is currently loaded.
        :rtype: ``bool``
        """
        pass

    def IsCaptureD3D12(self): # real signature unknown; restored from __doc__
        """
        IsCaptureD3D12()
        
        Determines whether or not a D3D12 capture is currently loaded.
        
        :return: A boolean indicating if a D3D12 capture is currently loaded.
        :rtype: ``bool``
        """
        pass

    def IsCaptureGL(self): # real signature unknown; restored from __doc__
        """
        IsCaptureGL()
        
        Determines whether or not an OpenGL capture is currently loaded.
        
        :return: A boolean indicating if an OpenGL capture is currently loaded.
        :rtype: ``bool``
        """
        pass

    def IsCaptureLoaded(self): # real signature unknown; restored from __doc__
        """
        IsCaptureLoaded()
        
        Determines whether or not a capture is currently loaded.
        
        :return: A boolean indicating if a capture is currently loaded.
        :rtype: ``bool``
        """
        pass

    def IsCaptureVK(self): # real signature unknown; restored from __doc__
        """
        IsCaptureVK()
        
        Determines whether or not a Vulkan capture is currently loaded.
        
        :return: A boolean indicating if a Vulkan capture is currently loaded.
        :rtype: ``bool``
        """
        pass

    def IsStripRestartEnabled(self): # real signature unknown; restored from __doc__
        """
        IsStripRestartEnabled()
        
        Determines whether or not primitive restart is enabled.
        
        :return: A boolean indicating if primitive restart is enabled.
        :rtype: ``bool``
        """
        pass

    def IsTessellationEnabled(self): # real signature unknown; restored from __doc__
        """
        IsTessellationEnabled()
        
        Determines whether or not tessellation is currently enabled.
        
        :return: A boolean indicating if tessellation is currently enabled.
        :rtype: ``bool``
        """
        pass

    def MultiviewBroadcastCount(self): # real signature unknown; restored from __doc__
        """
        MultiviewBroadcastCount()
        
        Returns the number of views being broadcast to simultaneously during rendering.
        """
        pass

    def OutputAbbrev(self): # real signature unknown; restored from __doc__
        """
        OutputAbbrev()
        
        Retrieves a suitable two or three letter abbreviation of the output stage. Typically
        'OM' or 'FBO'.
        
        :return: The abbreviation of the output stage.
        :rtype: ``str``
        """
        pass

    def SupportsBarriers(self): # real signature unknown; restored from __doc__
        """
        SupportsBarriers()
        
        Determines whether or not the current capture uses explicit barriers.
        
        :return: A boolean indicating if explicit barriers are used.
        :rtype: ``bool``
        """
        pass

    def SupportsResourceArrays(self): # real signature unknown; restored from __doc__
        """
        SupportsResourceArrays()
        
        Determines whether or not the current capture supports binding arrays of resources.
        
        :return: A boolean indicating if binding arrays of resources is supported.
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


