# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ShaderBuiltin(__enum.IntEnum):
    """
    Annotates a particular built-in input or output from a shader with a special meaning to
    the hardware or API.
    
    Some of the built-in inputs or outputs can be declared multiple times in arrays or otherwise indexed
    to apply to multiple related things - see :data:`ClipDistance`, :data:`CullDistance` and
    :data:`ColorOutput`.
    
    .. data:: Undefined
    
      Undefined built-in or no built-in is attached to this shader variable.
    
    .. data:: Position
    
      As an output from the final vertex processing shader stage, this feeds the vertex position to the
      rasterized. As an input to the pixel shader stage this receives the position from the rasterizer.
    
    .. data:: PointSize
    
      An output that controls the size of point primitives.
    
    .. data:: ClipDistance
    
      An output for the distance to a user-defined clipping plane. Any pixel with an interpolated value
      that is negative will not be rasterized. Typically there can be more than one such output.
    
    .. data:: CullDistance
    
      An output for the distance to a user-defined culling plane. Any primitive with all vertices having
      negative values will not be rasterized. Typically there can be more than one such output.
    
    .. data:: RTIndex
    
      An output for selecting the render target index in an array to render to. Available in geometry
      shaders and possibly earlier stages depending on hardware/API capability.
    
    .. data:: ViewportIndex
    
      An output for selecting the viewport index to render to. Available in geometry shaders and
      possibly earlier stages depending on hardware/API capability.
    
    .. data:: VertexIndex
    
      An input to the vertex shader listing the vertex index. The exact meaning of this index can vary
      by API but generally it refers to either a 0-based counter for non-indexed draws, or the index
      value for indexed draws. It may or may not be affected by offsets, depending on API semantics.
    
    .. data:: PrimitiveIndex
    
      A built-in indicating which primitive is being processed. This can be read by all primitive stages
      after the vertex shader, and written by the geometry shader.
    
    .. data:: InstanceIndex
    
      This built-in is defined similar to :data:`VertexIndex` but for instances within an instanced
      drawcall. It counts from 0 and as with :data:`VertexIndex` it may or may not be affected by
      drawcall offsets.
    
    .. data:: DispatchSize
    
      An input in compute shaders that gives the number of workgroups executed by the dispatch call.
    
    .. data:: DispatchThreadIndex
    
      An input in compute shaders giving a 3D shared index across all workgroups, such that the index
      varies across each thread in the workgroup up to its size, then the indices for workgroup
      ``(0,0,1)`` begin adjacent to where workgroup ``(0,0,0)`` ended.
    
      This is related to :data:`GroupThreadIndex` and :data:`GroupIndex`.
    
    .. data:: GroupIndex
    
      An input in compute shaders giving a 3D index of this current workgroup amongst all workgroups,
      up to the dispatch size.
    
      The index is constant across all threads in the workgroup.
    
      This is related to :data:`GroupThreadIndex` and :data:`DispatchThreadIndex`.
    
    .. data:: GroupFlatIndex
    
      An input in compute shaders giving a flat 1D index of the thread within the current workgroup.
      This index increments first in the ``X`` dimension, then in the ``Y`` dimension, then in the ``Z``
      dimension.
    
    .. data:: GroupThreadIndex
    
      An input in compute shaders giving a 3D index of this thread within its workgroup, up to the
      workgroup size.
    
      The input does not vary between one thread in a workgroup and the same thread in another
      workgroup.
    
      This is related to :data:`GroupIndex` and :data:`DispatchThreadIndex`.
    
    .. data:: GSInstanceIndex
    
      An input to the geometry shader giving the instance being run, if the geometry shader was setup to
      be invoked multiple times for each input primitive.
    
    .. data:: OutputControlPointIndex
    
      An input to the tessellation control or hull shader giving the output control point index or patch
      vertex being operated on.
    
    .. data:: DomainLocation
    
      An input to the tessellation evaluation or domain shader, giving the normalised location on the
      output patch where evaluation is occuring. E.g. for triangle output this is the barycentric
      co-ordinates of the output vertex.
    
    .. data:: IsFrontFace
    
      An input to the pixel shader indicating whether or not the contributing triangle was considered
      front-facing or not according to the API setup for winding order and backface orientation.
    
    .. data:: MSAACoverage
    
      An input or an output from the pixel shader. As an input, it specifies a bitmask of which samples
      in a pixel were covered by the rasterizer. As an output, it specifies which samples in the
      destination target should be updated.
    
    .. data:: MSAASamplePosition
    
      An input to the pixel shader that contains the location of the current sample relative to the
      pixel, when running the pixel shader at sample frequency.
    
    
    .. data:: MSAASampleIndex
    
      An input to the pixel shader that indicates which sample in the range ``0 .. N-1`` is currently
      being processed.
    
    .. data:: PatchNumVertices
    
      An input to the tessellation stages, this gives the number of vertices in each patch.
    
    .. data:: OuterTessFactor
    
      An output from the tessellation control or hull shader, this determines the level to which the
      outer edge of each primitive is tessellated by the fixed-function tessellator.
    
      It is also available for reading in the tessellation evaluation or domain shader.
    
    .. data:: InsideTessFactor
    
      Related to :data:`OuterTessFactor` this functions in the same way to determine the tessellation
      level inside the primitive.
    
    .. data:: ColorOutput
    
      An output from the pixel shader, this determines the color value written to the corresponding
      target. There will be as many color output built-ins as there are targets bound.
    
    .. data:: DepthOutput
    
      An output from the pixel shader, writes the depth of this pixel with no restrictions.
    
      Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutputLessEqual`.
    
    .. data:: DepthOutputGreaterEqual
    
      An output from the pixel shader, writes the depth of this pixel with the restriction that it will
      be greater than or equal to the original depth produced by the rasterizer.
    
      Related to :data:`DepthOutput` and :data:`DepthOutputLessEqual`.
    
    .. data:: DepthOutputLessEqual
    
      An output from the pixel shader, writes the depth of this pixel with the restriction that it will
      be less than or equal to the original depth produced by the rasterizer.
    
      Related to :data:`DepthOutputGreaterEqual` and :data:`DepthOutput`.
    
    .. data:: BaseVertex
    
      The first vertex processed in this draw, as specified by the ``firstVertex`` / ``baseVertex``
      parameter to the draw call.
    
    .. data:: BaseInstance
    
      The first instance processed in this draw call, as specified by the ``firstInstance`` parameter.
    
    .. data:: DrawIndex
    
      For indirect or multi-draw commands, the index of this draw call within the overall draw command.
    
    .. data:: StencilReference
    
      The stencil reference to be used for stenciling operations on this fragment.
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

    BaseInstance = 30
    BaseVertex = 29
    ClipDistance = 3
    ColorOutput = 25
    Count = 33
    CullDistance = 4
    DepthOutput = 26
    DepthOutputGreaterEqual = 27
    DepthOutputLessEqual = 28
    DispatchSize = 10
    DispatchThreadIndex = 11
    DomainLocation = 17
    DrawIndex = 31
    First = 0
    GroupFlatIndex = 13
    GroupIndex = 12
    GroupThreadIndex = 14
    GSInstanceIndex = 15
    InsideTessFactor = 24
    InstanceIndex = 9
    IsFrontFace = 18
    MSAACoverage = 19
    MSAASampleIndex = 21
    MSAASamplePosition = 20
    OuterTessFactor = 23
    OutputControlPointIndex = 16
    PatchNumVertices = 22
    PointSize = 2
    Position = 1
    PrimitiveIndex = 8
    RTIndex = 5
    StencilReference = 32
    Undefined = 0
    VertexIndex = 7
    ViewportIndex = 6
    _member_map_ = {
        'BaseInstance': 30,
        'BaseVertex': 29,
        'ClipDistance': 3,
        'ColorOutput': 25,
        'Count': 33,
        'CullDistance': 4,
        'DepthOutput': 26,
        'DepthOutputGreaterEqual': 27,
        'DepthOutputLessEqual': 28,
        'DispatchSize': 10,
        'DispatchThreadIndex': 11,
        'DomainLocation': 17,
        'DrawIndex': 31,
        'First': 0,
        'GSInstanceIndex': 15,
        'GroupFlatIndex': 13,
        'GroupIndex': 12,
        'GroupThreadIndex': 14,
        'InsideTessFactor': 24,
        'InstanceIndex': 9,
        'IsFrontFace': 18,
        'MSAACoverage': 19,
        'MSAASampleIndex': 21,
        'MSAASamplePosition': 20,
        'OuterTessFactor': 23,
        'OutputControlPointIndex': 16,
        'PatchNumVertices': 22,
        'PointSize': 2,
        'Position': 1,
        'PrimitiveIndex': 8,
        'RTIndex': 5,
        'StencilReference': 32,
        'Undefined': 0,
        'VertexIndex': 7,
        'ViewportIndex': 6,
    }
    _member_names_ = [
        'Undefined',
        'Position',
        'PointSize',
        'ClipDistance',
        'CullDistance',
        'RTIndex',
        'ViewportIndex',
        'VertexIndex',
        'PrimitiveIndex',
        'InstanceIndex',
        'DispatchSize',
        'DispatchThreadIndex',
        'GroupIndex',
        'GroupFlatIndex',
        'GroupThreadIndex',
        'GSInstanceIndex',
        'OutputControlPointIndex',
        'DomainLocation',
        'IsFrontFace',
        'MSAACoverage',
        'MSAASamplePosition',
        'MSAASampleIndex',
        'PatchNumVertices',
        'OuterTessFactor',
        'InsideTessFactor',
        'ColorOutput',
        'DepthOutput',
        'DepthOutputGreaterEqual',
        'DepthOutputLessEqual',
        'BaseVertex',
        'BaseInstance',
        'DrawIndex',
        'StencilReference',
        'Count',
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
    }


