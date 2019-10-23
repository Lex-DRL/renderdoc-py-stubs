# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class GPUCounter(__enum.IntEnum):
    """
    Pre-defined GPU counters that can be supported by a given implementation.
    
    GPU counters actually available can be queried by :meth:`ReplayController.EnumerateCounters`. If any
    in this list are supported they will be returned with these counter IDs. More counters may be
    enumerated with IDs in the appropriate ranges.
    
    .. data:: EventGPUDuration
    
      Time taken for this event on the GPU, as measured by delta between two GPU timestamps.
    
    .. data:: InputVerticesRead
    
      Number of vertices read by input assembler.
    
    .. data:: IAPrimitives
    
      Number of primitives read by the input assembler.
    
    .. data:: GSPrimitives
    
      Number of primitives output by a geometry shader.
    
    .. data:: RasterizerInvocations
    
      Number of primitives that were sent to the rasterizer.
    
    .. data:: RasterizedPrimitives
    
      Number of primitives that were rendered.
    
    .. data:: SamplesPassed
    
      Number of samples that passed depth/stencil test.
    
    .. data:: VSInvocations
    
      Number of times a :data:`vertex shader <ShaderStage.Vertex>` was invoked.
    
    .. data:: HSInvocations
    
      Number of times a :data:`hull shader <ShaderStage.Hull>` was invoked.
    
    .. data:: TCSInvocations
    
      Number of times a :data:`tessellation control shader <ShaderStage.Tess_Control>` was invoked.
    
    .. data:: DSInvocations
    
      Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    
    .. data:: TESInvocations
    
      Number of times a :data:`tessellation evaluation shader <ShaderStage.Tess_Eval>` was invoked.
    
    .. data:: GSInvocations
    
      Number of times a :data:`domain shader <ShaderStage.Domain>` was invoked.
    
    .. data:: PSInvocations
    
      Number of times a :data:`pixel shader <ShaderStage.Pixel>` was invoked.
    
    .. data:: FSInvocations
    
      Number of times a :data:`fragment shader <ShaderStage.Fragment>` was invoked.
    
    .. data:: CSInvocations
    
      Number of times a :data:`compute shader <ShaderStage.Compute>` was invoked.
    
    .. data:: FirstAMD
    
      The AMD-specific counter IDs start from this value.
    
    .. data:: LastAMD
    
      The AMD-specific counter IDs end with this value.
    
    .. data:: FirstIntel
    
      The Intel-specific counter IDs start from this value.
    
    .. data:: LastIntel
    
      The Intel-specific counter IDs end with this value.
    
    .. data:: FirstNvidia
    
      The nVidia-specific counter IDs start from this value.
    
    .. data:: LastNvidia
    
      The nVidia-specific counter IDs end with this value.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    Count = 14
    CSInvocations = 13
    DSInvocations = 10
    EventGPUDuration = 1
    First = 1
    FirstAMD = 1000000
    FirstIntel = 2000000
    FirstNvidia = 3000000
    FSInvocations = 12
    GSInvocations = 11
    GSPrimitives = 4
    HSInvocations = 9
    IAPrimitives = 3
    InputVerticesRead = 2
    LastAMD = 1999999
    LastIntel = 2999999
    LastNvidia = 4000000
    PSInvocations = 12
    RasterizedPrimitives = 6
    RasterizerInvocations = 5
    SamplesPassed = 7
    TCSInvocations = 9
    TESInvocations = 10
    VSInvocations = 8
    _member_map_ = {
        'CSInvocations': 13,
        'Count': 14,
        'DSInvocations': 10,
        'EventGPUDuration': 1,
        'FSInvocations': 12,
        'First': 1,
        'FirstAMD': 1000000,
        'FirstIntel': 2000000,
        'FirstNvidia': 3000000,
        'GSInvocations': 11,
        'GSPrimitives': 4,
        'HSInvocations': 9,
        'IAPrimitives': 3,
        'InputVerticesRead': 2,
        'LastAMD': 1999999,
        'LastIntel': 2999999,
        'LastNvidia': 4000000,
        'PSInvocations': 12,
        'RasterizedPrimitives': 6,
        'RasterizerInvocations': 5,
        'SamplesPassed': 7,
        'TCSInvocations': 9,
        'TESInvocations': 10,
        'VSInvocations': 8,
    }
    _member_names_ = [
        'EventGPUDuration',
        'InputVerticesRead',
        'IAPrimitives',
        'GSPrimitives',
        'RasterizerInvocations',
        'RasterizedPrimitives',
        'SamplesPassed',
        'VSInvocations',
        'HSInvocations',
        'DSInvocations',
        'GSInvocations',
        'PSInvocations',
        'CSInvocations',
        'Count',
        'FirstAMD',
        'FirstIntel',
        'LastAMD',
        'FirstNvidia',
        'LastIntel',
        'LastNvidia',
    ]
    _member_type_ = int
    _value2member_map_ = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        1000000: 1000000,
        1999999: 1999999,
        2000000: 2000000,
        2999999: 2999999,
        3000000: 3000000,
        4000000: 4000000,
    }


