# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ResourceUsage(__enum.IntEnum):
    """
    How a resource is being used in the pipeline at a particular point.
    
    Note that a resource may be used for more than one thing in one event, see :class:`EventUsage`.
    
    .. data:: Unused
    
      The resource is not being used.
    
    .. data:: VertexBuffer
    
      The resource is being used as a fixed-function vertex buffer input.
    
    .. data:: IndexBuffer
    
      The resource is being used as an index buffer.
    
    .. data:: VS_Constants
    
      The resource is being used for constants in the :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_Constants
    
      The resource is being used for constants in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_Constants
    
      The resource is being used for constants in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_Constants
    
      The resource is being used for constants in the :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_Constants
    
      The resource is being used for constants in the :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_Constants
    
      The resource is being used for constants in the :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: All_Constants
    
      The resource is being used for constants in all shader stages.
    
    .. data:: StreamOut
    
      The resource is being used for stream out/transform feedback storage after geometry processing.
    
    .. data:: VS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_Resource
    
      The resource is being used as a read-only resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_Resource
    
      The resource is being used as a read-only resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_Resource
    
      The resource is being used as a read-only resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: All_Resource
    
      The resource is being used as a read-only resource in all shader stages.
    
    .. data:: VS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`vertex shader <ShaderStage.Vertex>`.
    
    .. data:: HS_RWResource
    
      The resource is being used as a read-write resource in the tessellation control or
      :data:`hull shader <ShaderStage.Hull>`.
    
    .. data:: DS_RWResource
    
      The resource is being used as a read-write resource in the tessellation evaluation or
      :data:`domain shader <ShaderStage.Domain>`.
    
    .. data:: GS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`geometry shader <ShaderStage.Geometry>`.
    
    .. data:: PS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`pixel shader <ShaderStage.Pixel>`.
    
    .. data:: CS_RWResource
    
      The resource is being used as a read-write resource in the
      :data:`compute shader <ShaderStage.Compute>`.
    
    .. data:: All_RWResource
    
      The resource is being used as a read-write resource in all shader stages.
    
    .. data:: InputTarget
    
      The resource is being read as an input target for reading from the target currently being written.
    
    .. data:: ColorTarget
    
      The resource is being written to as a color output.
    
    .. data:: DepthStencilTarget
    
      The resource is being written to and tested against as a depth-stencil output.
    
    .. data:: Indirect
    
      The resource is being used for indirect arguments.
    
    .. data:: Clear
    
      The resource is being cleared
    
    .. data:: GenMips
    
      The resource is having mips generated for it.
    
    .. data:: Resolve
    
      The resource is being resolved or blitted, as both source and destination.
    
    .. data:: ResolveSrc
    
      The resource is being resolved or blitted from.
    
    .. data:: ResolveDst
    
      The resource is being resolved or blitted to.
    
    .. data:: Copy
    
      The resource is being copied, as both source and destination.
    
    .. data:: CopySrc
    
      The resource is being copied from.
    
    .. data:: CopyDst
    
      The resource is being copied to.
    
    .. data:: Barrier
    
      The resource is being specified in a barrier, as defined in Vulkan or Direct3D 12.
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

    All_Constants = 9
    All_Resource = 17
    All_RWResource = 24
    Barrier = 37
    Clear = 29
    ColorTarget = 26
    Copy = 34
    CopyDst = 36
    CopySrc = 35
    CS_Constants = 8
    CS_Resource = 16
    CS_RWResource = 23
    DepthStencilTarget = 27
    DS_Constants = 5
    DS_Resource = 13
    DS_RWResource = 20
    GenMips = 30
    GS_Constants = 6
    GS_Resource = 14
    GS_RWResource = 21
    HS_Constants = 4
    HS_Resource = 12
    HS_RWResource = 19
    IndexBuffer = 2
    Indirect = 28
    InputTarget = 25
    PS_Constants = 7
    PS_Resource = 15
    PS_RWResource = 22
    Resolve = 31
    ResolveDst = 33
    ResolveSrc = 32
    StreamOut = 10
    Unused = 0
    VertexBuffer = 1
    VS_Constants = 3
    VS_Resource = 11
    VS_RWResource = 18
    _member_map_ = {
        'All_Constants': 9,
        'All_RWResource': 24,
        'All_Resource': 17,
        'Barrier': 37,
        'CS_Constants': 8,
        'CS_RWResource': 23,
        'CS_Resource': 16,
        'Clear': 29,
        'ColorTarget': 26,
        'Copy': 34,
        'CopyDst': 36,
        'CopySrc': 35,
        'DS_Constants': 5,
        'DS_RWResource': 20,
        'DS_Resource': 13,
        'DepthStencilTarget': 27,
        'GS_Constants': 6,
        'GS_RWResource': 21,
        'GS_Resource': 14,
        'GenMips': 30,
        'HS_Constants': 4,
        'HS_RWResource': 19,
        'HS_Resource': 12,
        'IndexBuffer': 2,
        'Indirect': 28,
        'InputTarget': 25,
        'PS_Constants': 7,
        'PS_RWResource': 22,
        'PS_Resource': 15,
        'Resolve': 31,
        'ResolveDst': 33,
        'ResolveSrc': 32,
        'StreamOut': 10,
        'Unused': 0,
        'VS_Constants': 3,
        'VS_RWResource': 18,
        'VS_Resource': 11,
        'VertexBuffer': 1,
    }
    _member_names_ = [
        'Unused',
        'VertexBuffer',
        'IndexBuffer',
        'VS_Constants',
        'HS_Constants',
        'DS_Constants',
        'GS_Constants',
        'PS_Constants',
        'CS_Constants',
        'All_Constants',
        'StreamOut',
        'VS_Resource',
        'HS_Resource',
        'DS_Resource',
        'GS_Resource',
        'PS_Resource',
        'CS_Resource',
        'All_Resource',
        'VS_RWResource',
        'HS_RWResource',
        'DS_RWResource',
        'GS_RWResource',
        'PS_RWResource',
        'CS_RWResource',
        'All_RWResource',
        'InputTarget',
        'ColorTarget',
        'DepthStencilTarget',
        'Indirect',
        'Clear',
        'GenMips',
        'Resolve',
        'ResolveSrc',
        'ResolveDst',
        'Copy',
        'CopySrc',
        'CopyDst',
        'Barrier',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
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
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
    }


