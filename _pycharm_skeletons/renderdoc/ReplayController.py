# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ReplayController(SwigPyObject):
    """
    The primary interface to access the information in a capture and the current state, as
    well as control the replay and analysis functionality available.
    
    .. data:: NoPreference
    
      No preference for a particular value, see :meth:`ReplayController.DebugPixel`.
    """
    def AddFakeMarkers(self): # real signature unknown; restored from __doc__
        """
        AddFakeMarkers()
        
        Add fake marker regions to the list of drawcalls in the capture, based on which
        textures are bound as outputs.
        """
        pass

    def BuildCustomShader(self, entry, sourceEncoding, source, compileFlags, type): # real signature unknown; restored from __doc__
        """
        BuildCustomShader(entry, sourceEncoding, source, compileFlags, type)
        
        Builds a shader suitable for running on the local replay instance as a custom shader.
        
        See :data:`TextureDisplay.customShaderId`.
        
        :param str entry: The entry point to use when compiling.
        :param ShaderEncoding sourceEncoding: The encoding of the source data.
        :param bytes source: The source data itself.
        :param int compileFlags: API-specific compilation flags.
        :param ShaderStage type: The stage that this shader will be executed at.
        :return: A ``tuple`` with the id of the new shader if compilation was successful,
          :meth:`ResourceId.Null` otherwise, and a ``str`` with any warnings/errors from compilation.
        :rtype: ``tuple`` of :class:`ResourceId` and ``str``.
        """
        pass

    def BuildTargetShader(self, entry, sourceEncoding, source, flags, type): # real signature unknown; restored from __doc__
        """
        BuildTargetShader(entry, sourceEncoding, source, flags, type)
        
        Builds a shader suitable for running in the capture's API as a replacement shader.
        
        :param str entry: The entry point to use when compiling.
        :param ShaderEncoding sourceEncoding: The encoding of the source data.
        :param bytes source: The source data itself.
        :param ShaderCompileFlags compileFlags: API-specific compilation flags.
        :param ShaderStage type: The stage that this shader will be executed at.
        :return: A ``tuple`` with the id of the new shader if compilation was successful,
          :meth:`ResourceId.Null` otherwise, and a ``str`` with any warnings/errors from compilation.
        :rtype: ``tuple`` of :class:`ResourceId` and ``str``.
        """
        pass

    def CancelReplayLoop(self): # real signature unknown; restored from __doc__
        """
        CancelReplayLoop()
        
        Cancels a replay loop begun in :meth:`ReplayLoop`. Does nothing if no loop is active.
        """
        pass

    def CreateOutput(self, window, type): # real signature unknown; restored from __doc__
        """
        CreateOutput(window, type)
        
        Creates a replay output of the given type to the given native window
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ReplayOutputType type: What type of output to create
        :return: A handle to the created output, or ``None`` on failure
        :rtype: ReplayOutput
        """
        pass

    def CreateRGPProfile(self, window): # real signature unknown; restored from __doc__
        """
        CreateRGPProfile(window)
        
        Uses the given output window to create an RGP Profile.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :return: The path to the created RGP profile, or empty on failure
        :rtype: str
        """
        pass

    def DebugPixel(self, x, y, sample, primitive): # real signature unknown; restored from __doc__
        """
        DebugPixel(x, y, sample, primitive)
        
        Retrieve a debugging trace from running a pixel shader.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param int x: The x co-ordinate.
        :param int y: The y co-ordinate.
        :param int sample: The multi-sampled sample. Ignored if non-multisampled texture.
        :param int primitive: Debug the pixel from this primitive if there's ambiguity. If set to
          :data:`NoPreference` then a random fragment writing to the given co-ordinate is debugged.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass

    def DebugThread(self, groupid, threadid): # real signature unknown; restored from __doc__
        """
        DebugThread(groupid, threadid)
        
        Retrieve a debugging trace from running a compute thread.
        
        :param groupid: A list containing the 3D workgroup index.
        :param threadid: A list containing the 3D thread index within the above workgroup.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass

    def DebugVertex(self, vertid, instid, idx, instOffset, vertOffset): # real signature unknown; restored from __doc__
        """
        DebugVertex(vertid, instid, idx, instOffset, vertOffset)
        
        Retrieve a debugging trace from running a vertex shader.
        
        :param int vertid: The vertex ID as a 0-based index up to the number of vertices in the draw.
        :param int instid: The instance ID as a 0-based index up to the number of instances in the draw.
        :param int idx: The actual index used to look up vertex inputs, either from the vertex ID for non-
          indexed draws or drawn from the index buffer. This must have all drawcall offsets applied.
        :param int instOffset: The value from :data:`DrawcallDescription.instanceOffset`.
        :param int vertOffset: The value from :data:`DrawcallDescription.vertexOffset`.
        :return: The resulting trace resulting from debugging. Destroy with
          :meth:`FreeTrace`.
        :rtype: ShaderDebugTrace
        """
        pass

    def DescribeCounter(self, counter): # real signature unknown; restored from __doc__
        """
        DescribeCounter(counter)
        
        Get information about what a counter actually represents, in terms of a human-readable
        understanding as well as the type and unit of the resulting information.
        
        :param GPUCounter counter: The counter to query about.
        :return: The description of the counter.
        :rtype: CounterDescription
        """
        pass

    def DisassembleShader(self, pipeline, refl, target): # real signature unknown; restored from __doc__
        """
        DisassembleShader(pipeline, refl, target)
        
        Retrieve the disassembly for a given shader, for the given disassembly target.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ShaderReflection refl: The shader reflection details of the shader to disassemble
        :param str target: The name of the disassembly target to generate for. Must be one of the values
          returned by :meth:`GetDisassemblyTargets`, or empty to use the default generation.
        :return: The disassembly text, or an error message if something went wrong.
        :rtype: ``str``
        """
        pass

    def EnumerateCounters(self): # real signature unknown; restored from __doc__
        """
        EnumerateCounters()
        
        Retrieve a list of which counters are available in the current capture analysis
        implementation.
        
        :return: The list of counters available.
        :rtype: ``list`` of :class:`GPUCounter`
        """
        pass

    def FetchCounters(self, counters): # real signature unknown; restored from __doc__
        """
        FetchCounters(counters)
        
        Retrieve the values of a specified set of counters.
        
        :param list counters: The list of :class:`GPUCounter` to fetch results for.
        :return: The list of counter results generated.
        :rtype: ``list`` of :class:`CounterResult`
        """
        pass

    def FileChanged(self): # real signature unknown; restored from __doc__
        """
        FileChanged()
        
        Notify the interface that the file it has open has been changed on disk.
        """
        pass

    def FreeCustomShader(self, id): # real signature unknown; restored from __doc__
        """
        FreeCustomShader(id)
        
        Free a previously created custom shader.
        
        See :meth:`BuildCustomShader`.
        
        :param ResourceId id: The id of the custom shader to free.
        """
        pass

    def FreeTargetResource(self, id): # real signature unknown; restored from __doc__
        """
        FreeTargetResource(id)
        
        Free a previously created target shader.
        
        See :meth:`BuildTargetShader`.
        
        :param ResourceId id: The id of the target shader to free.
        """
        pass

    def FreeTrace(self, trace): # real signature unknown; restored from __doc__
        """
        FreeTrace(trace)
        
        Free a debugging trace from running a shader invocation debug.
        
        :param ShaderDebugTrace trace: The shader debugging trace to free.
        """
        pass

    def GetAPIProperties(self): # real signature unknown; restored from __doc__
        """
        GetAPIProperties()
        
        Retrieve a :class:`APIProperties` object describing the current capture.
        
        :return: The properties of the current capture.
        :rtype: APIProperties
        """
        pass

    def GetBufferData(self, buff, offset, len): # real signature unknown; restored from __doc__
        """
        GetBufferData(buff, offset, len)
        
        Retrieve the contents of a range of a buffer as a ``bytes``.
        
        :param ResourceId buff: The id of the buffer to retrieve data from.
        :param int offset: The byte offset to the start of the range.
        :param int len: The length of the range, or 0 to retrieve the rest of the bytes in the buffer.
        :return: The requested buffer contents.
        :rtype: ``bytes``
        """
        pass

    def GetBuffers(self): # real signature unknown; restored from __doc__
        """
        GetBuffers()
        
        Retrieve the list of buffers alive in the capture.
        
        :return: The list of buffers in the capture.
        :rtype: ``list`` of :class:`BufferDescription`
        """
        pass

    def GetCBufferVariableContents(self, pipeline, shader, entryPoint, cbufslot, buffer, offs): # real signature unknown; restored from __doc__
        """
        GetCBufferVariableContents(pipeline, shader, entryPoint, cbufslot, buffer, offs)
        
        Retrieve the contents of a constant block by reading from memory or their source
        otherwise.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ResourceId shader: The id of the shader to use for metadata.
        :param str entryPoint: The entry point of the shader being used. In some APIs, this is ignored.
        :param int cbufslot: The index in the :data:`ShaderReflection.constantBlocks` list to look up.
        :param ResourceId buffer: The id of the buffer to use for data. If
          :data:`ConstantBlock.bufferBacked` is ``False`` this is ignored.
        :param int offs: Retrieve buffer contents starting at this byte offset.
        :return: The shader variables with their contents.
        :rtype: ``list`` of :class:`ShaderVariable`
        """
        pass

    def GetCustomShaderEncodings(self): # real signature unknown; restored from __doc__
        """
        GetCustomShaderEncodings()
        
        Retrieve the list of supported :class:`ShaderEncoding` which can be build using
        :meth:`BuildCustomShader`.
        
        The list is sorted in priority order, so if the caller has a shader in a form but could
        compile/translate it to another, prefer to satisfy the first encoding before later encodings.
        
        This typically means the 'native' encoding is listed first, and then subsequent encodings are
        compiled internally - so compiling externally could be preferable as it allows better customisation
        of the compile process or using alternate/updated tools.
        
        :return: The list of target shader encodings available.
        :rtype: ``list`` of :class:`ShaderEncoding`
        """
        pass

    def GetD3D11PipelineState(self): # real signature unknown; restored from __doc__
        """
        GetD3D11PipelineState()
        
        Retrieve the current :class:`D3D11State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D11 API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current D3D11 pipeline state.
        :rtype: D3D11State
        """
        pass

    def GetD3D12PipelineState(self): # real signature unknown; restored from __doc__
        """
        GetD3D12PipelineState()
        
        Retrieve the current :class:`D3D12State` pipeline state.
        
        The return value will be ``None`` if the capture is not using the D3D12 API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current D3D12 pipeline state.
        :rtype: D3D12State
        """
        pass

    def GetDebugMessages(self): # real signature unknown; restored from __doc__
        """
        GetDebugMessages()
        
        Retrieve a list of any newly generated diagnostic messages.
        
        Every time this function is called, any debug messages returned will not be returned again. Only
        newly generated messages will be returned after that.
        
        :return: The list of the :class:`DebugMessage` messages.
        :rtype: ``list`` of :class:`DebugMessage`
        """
        pass

    def GetDisassemblyTargets(self): # real signature unknown; restored from __doc__
        """
        GetDisassemblyTargets()
        
        Retrieve the list of possible disassembly targets for :meth:`DisassembleShader`. The
        values are implementation dependent but will always include a default target first which is the
        native disassembly of the shader. Further options may be available for additional diassembly views
        or hardware-specific ISA formats.
        
        :return: The list of disassembly targets available.
        :rtype: ``list`` of ``str``
        """
        pass

    def GetDrawcalls(self): # real signature unknown; restored from __doc__
        """
        GetDrawcalls()
        
        Retrieve the list of root-level drawcalls in the capture.
        
        :return: The list of root-level drawcalls in the capture.
        :rtype: ``list`` of :class:`DrawcallDescription`
        """
        pass

    def GetFrameInfo(self): # real signature unknown; restored from __doc__
        """
        GetFrameInfo()
        
        Retrieve the information about the frame contained in the capture.
        
        :return: The frame information.
        :rtype: FrameDescription
        """
        pass

    def GetGLPipelineState(self): # real signature unknown; restored from __doc__
        """
        GetGLPipelineState()
        
        Retrieve the current :class:`GLState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the OpenGL API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current OpenGL pipeline state.
        :rtype: GLState
        """
        pass

    def GetPipelineState(self): # real signature unknown; restored from __doc__
        """
        GetPipelineState()
        
        Retrieve the current :class:`PipeState` pipeline state abstraction.
        
        This pipeline state will always be valid, and allows queries that will work regardless of the
        capture's API.
        
        :return: The current pipeline state abstraction.
        :rtype: PipeState
        """
        pass

    def GetPostVSData(self, instance, view, stage): # real signature unknown; restored from __doc__
        """
        GetPostVSData(instance, view, stage)
        
        Retrieve the generated data from one of the geometry processing shader stages.
        
        :param int instance: The index of the instance to retrieve data for, or 0 for non-instanced draws.
        :param int view: The index of the multiview view to retrieve data for, or 0 if multiview is disabled.
        :param MeshDataStage stage: The stage of the geometry processing pipeline to retrieve data from.
        :return: The information describing where the post-transform data is stored.
        :rtype: MeshFormat
        """
        pass

    def GetResources(self): # real signature unknown; restored from __doc__
        """
        GetResources()
        
        Retrieve the list of all resources in the capture.
        
        This includes any object allocated a :class:`ResourceId`, that don't have any other state or
        are only used as intermediary elements.
        
        :return: The list of resources in the capture.
        :rtype: ``list`` of :class:`ResourceDescription`
        """
        pass

    def GetShader(self, pipeline, shader, entry): # real signature unknown; restored from __doc__
        """
        GetShader(pipeline, shader, entry)
        
        Retrieve the information about the frame contained in the capture.
        
        :param ResourceId pipeline: The pipeline state object, if applicable, that this shader is bound to.
        :param ResourceId shader: The shader to get reflection data for.
        :param ShaderEntryPoint entry: The entry point within the shader to reflect. May be ignored on some
          APIs
        :return: The frame information.
        :rtype: ShaderReflection
        """
        pass

    def GetShaderEntryPoints(self, shader): # real signature unknown; restored from __doc__
        """
        GetShaderEntryPoints(shader)
        
        Retrieve a list of entry points for a shader.
        
        If the given ID doesn't specify a shader, an empty list will be return. On some APIs, the list will
        only ever have one result (only one entry point per shader).
        
        :param ResourceId shader: The shader to look up entry points for.
        :return: The list of the :class:`ShaderEntryPoint` messages.
        :rtype: ``list`` of :class:`ShaderEntryPoint`
        """
        pass

    def GetStructuredFile(self): # real signature unknown; restored from __doc__
        """
        GetStructuredFile()
        
        Fetch the structured data representation of the capture loaded.
        
        :return: The structured file.
        :rtype: SDFile
        """
        pass

    def GetSupportedWindowSystems(self): # real signature unknown; restored from __doc__
        """
        GetSupportedWindowSystems()
        
        Retrieves the supported :class:`WindowingSystem` systems by the local system.
        
        :return: The list of supported systems.
        :rtype: ``list`` of :class:`WindowingSystem`
        """
        pass

    def GetTargetShaderEncodings(self): # real signature unknown; restored from __doc__
        """
        GetTargetShaderEncodings()
        
        Retrieve the list of supported :class:`ShaderEncoding` which can be build using
        :meth:`BuildTargetShader`.
        
        The list is sorted in priority order, so if the caller has a shader in a form but could
        compile/translate it to another, prefer to satisfy the first encoding before later encodings.
        
        This typically means the 'native' encoding is listed first, and then subsequent encodings are
        compiled internally - so compiling externally could be preferable as it allows better customisation
        of the compile process or using alternate/updated tools.
        
        :return: The list of target shader encodings available.
        :rtype: ``list`` of :class:`ShaderEncoding`
        """
        pass

    def GetTextureData(self, tex, arrayIdx, mip): # real signature unknown; restored from __doc__
        """
        GetTextureData(tex, arrayIdx, mip)
        
        Retrieve the contents of one subresource of a texture as a ``bytes``.
        
        For multi-sampled images, they are treated as if they are an array that is Nx longer, with each
        array slice being expanded in-place so it would be slice 0: sample 0, slice 0: sample 1, slice 1:
        sample 0, etc.
        
        :param ResourceId tex: The id of the texture to retrieve data from.
        :param int arrayIdx: The slice of an array or 3D texture, or face of a cubemap texture.
        :param int mip: The mip level to pick from.
        :return: The requested texture contents.
        :rtype: ``bytes``
        """
        pass

    def GetTextures(self): # real signature unknown; restored from __doc__
        """
        GetTextures()
        
        Retrieve the list of textures alive in the capture.
        
        :return: The list of textures in the capture.
        :rtype: ``list`` of :class:`TextureDescription`
        """
        pass

    def GetUsage(self, id): # real signature unknown; restored from __doc__
        """
        GetUsage(id)
        
        Retrieve a list of ways a given resource is used.
        
        :param ResourceId id: The id of the texture or buffer resource to be queried.
        :return: The list of usages of the resource.
        :rtype: ``list`` of :class:`EventUsage`
        """
        pass

    def GetVulkanPipelineState(self): # real signature unknown; restored from __doc__
        """
        GetVulkanPipelineState()
        
        Retrieve the current :class:`VKState` pipeline state.
        
        The return value will be ``None`` if the capture is not using the Vulkan API.
        You should use :meth:`GetAPIProperties` to determine the API of the capture.
        
        See also :meth:`GetPipelineState`.
        
        :return: The current Vulkan pipeline state.
        :rtype: VKState
        """
        pass

    def PixelHistory(self, texture, x, y, slice, mip, sampleIdx, typeHint): # real signature unknown; restored from __doc__
        """
        PixelHistory(texture, x, y, slice, mip, sampleIdx, typeHint)
        
        Retrieve the history of modifications to the selected pixel on the selected texture.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param ResourceId texture: The texture to search for modifications.
        :param int x: The x co-ordinate.
        :param int y: The y co-ordinate.
        :param int slice: The slice of an array or 3D texture, or face of a cubemap texture.
        :param int mip: The mip level to pick from.
        :param int sampleIdx: The multi-sampled sample. Ignored if non-multisampled texture.
        :param CompType typeHint: A hint on how to interpret textures that are typeless.
        :return: The list of pixel history events.
        :rtype: ``list`` of :class:`PixelModification`
        """
        pass

    def RemoveReplacement(self, id): # real signature unknown; restored from __doc__
        """
        RemoveReplacement(id)
        
        Remove any previously specified replacement for an object.
        
        See :meth:`ReplaceResource`.
        
        :param ResourceId id: The id of the original resource that was previously being substituted.
        """
        pass

    def ReplaceResource(self, original, replacement): # real signature unknown; restored from __doc__
        """
        ReplaceResource(original, replacement)
        
        Replace one resource with another for subsequent replay and analysis work.
        
        This is commonly used for modifying the capture by selectively replacing resources with newly
        created resources.
        
        See :meth:`BuildTargetShader`, :meth:`RemoveReplacement`.
        
        :param ResourceId original: The id of the original resource that should be substituted.
        :param ResourceId replacement: The id of the new resource that should be used instead.
        """
        pass

    def ReplayLoop(self, window, texid): # real signature unknown; restored from __doc__
        """
        ReplayLoop(window, texid)
        
        Goes into a blocking loop, repeatedly replaying the open capture as fast as possible,
        displaying the selected texture in a default unscaled manner to the given output window.
        
        The function won't return until :meth:`CancelReplayLoop` is called. Since this function is blocking, that
        function must be called from another thread.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ResourceId texid: The id of the texture to display.
        """
        pass

    def SaveTexture(self, saveData, path): # real signature unknown; restored from __doc__
        """
        SaveTexture(saveData, path)
        
        Save a texture to a file on disk, with possible transformation to map a complex
        texture to something compatible with the target file format.
        
        :param TextureSave saveData: The configuration settings of which texture to save, and how
        :param str path: The path to save to on disk.
        :return: ``True`` if the texture was saved successfully, ``False`` otherwise.
        :rtype: ``bool``
        """
        pass

    def SetFrameEvent(self, eventId, force): # real signature unknown; restored from __doc__
        """
        SetFrameEvent(eventId, force)
        
        Move the replay to reflect the state immediately *after* the given
        :data:`eventId <APIEvent.eventId>`.
        
        :param int eventId: The :data:`eventId <APIEvent.eventId>` to move to.
        :param bool force: ``True`` if the internal replay should refresh even if the ``eventId`` is
          already current. This can be useful if external factors might cause the replay to vary.
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Shutdown and destroy the current interface and all outputs that have been created.
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


    NoPreference = 4294967295
    __dict__ = None # (!) real value is ''


