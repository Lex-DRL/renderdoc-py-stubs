# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class DrawFlags(__enum.IntFlag):
    """
    A set of flags describing the properties of a particular drawcall.
    
    .. data:: NoFlags
    
      The drawcall has no special properties.
    
    .. data:: Clear
    
      The drawcall is a clear call. See :data:`ClearColor` and :data:`ClearDepthStencil`.
    
    .. data:: Drawcall
    
      The drawcall renders primitives using the graphics pipeline.
    
    .. data:: Dispatch
    
      The drawcall issues a number of compute workgroups.
    
    .. data:: CmdList
    
      The drawcall calls into a previously recorded child command list.
    
    .. data:: SetMarker
    
      The drawcall inserts a single debugging marker.
    
    .. data:: PushMarker
    
      The drawcall begins a debugging marker region that has children.
    
    .. data:: PopMarker
    
      The drawcall ends a debugging marker region.
    
      .. note::
    
        Drawcalls with this flag will not be exposed and it is only used internally for tracking
        markers.
    
    .. data:: Present
    
      The drawcall is a presentation call that hands a swapchain image to the presentation engine.
    
    .. data:: MultiDraw
    
      The drawcall is a multi-draw that contains several specified child draws.
    
    .. data:: Copy
    
      The drawcall performs a resource copy operation.
    
    .. data:: Resolve
    
      The drawcall performs a resource resolve or blit operation.
    
    .. data:: GenMips
    
      The drawcall performs a resource mip-generation operation.
    
    .. data:: PassBoundary
    
      The drawcall marks the beginning or end of a render pass. See :data:`BeginPass` and
      :data:`EndPass`.
    
    .. data:: UseIBuffer
    
      The drawcall uses an index buffer.
    
    .. data:: Instanced
    
      The drawcall uses instancing. This does not mean it renders more than one instanced, simply that
      it uses the instancing feature.
    
    .. data:: Auto
    
      The drawcall interacts with stream-out to render all vertices previously written. This is a
      Direct3D 11 specific feature.
    
    .. data:: Indirect
    
      The drawcall uses a buffer on the GPU to source some or all of its parameters in an indirect way.
    
    .. data:: ClearColor
    
      The drawcall clears a color target.
    
    .. data:: ClearDepthStencil
    
      The drawcall clears a depth-stencil target.
    
    .. data:: BeginPass
    
      The drawcall marks the beginning of a render pass.
    
    .. data:: EndPass
    
      The drawcall marks the end of a render pass.
    
    .. data:: APICalls
    
      The drawcall does not contain any work directly, but is a 'virtual' draw inserted to encompass
      non-draw API calls that happened within a region, so they are included within the region where
      they occurred and not grouped into the next drawcall outside that region.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initital start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    APICalls = 16777216
    Auto = 262144
    BeginPass = 4194304
    Clear = 1
    ClearColor = 1048576
    ClearDepthStencil = 2097152
    CmdList = 8
    Copy = 512
    Dispatch = 4
    Drawcall = 2
    EndPass = 8388608
    GenMips = 2048
    Indexed = 65536
    Indirect = 524288
    Instanced = 131072
    MultiDraw = 256
    NoFlags = 0
    PassBoundary = 4096
    PopMarker = 64
    Present = 128
    PushMarker = 32
    Resolve = 1024
    SetMarker = 16
    _member_map_ = {
        'APICalls': 16777216,
        'Auto': 262144,
        'BeginPass': 4194304,
        'Clear': 1,
        'ClearColor': 1048576,
        'ClearDepthStencil': 2097152,
        'CmdList': 8,
        'Copy': 512,
        'Dispatch': 4,
        'Drawcall': 2,
        'EndPass': 8388608,
        'GenMips': 2048,
        'Indexed': 65536,
        'Indirect': 524288,
        'Instanced': 131072,
        'MultiDraw': 256,
        'NoFlags': 0,
        'PassBoundary': 4096,
        'PopMarker': 64,
        'Present': 128,
        'PushMarker': 32,
        'Resolve': 1024,
        'SetMarker': 16,
    }
    _member_names_ = [
        'NoFlags',
        'Clear',
        'Drawcall',
        'Dispatch',
        'CmdList',
        'SetMarker',
        'PushMarker',
        'PopMarker',
        'Present',
        'MultiDraw',
        'Copy',
        'Resolve',
        'GenMips',
        'PassBoundary',
        'Indexed',
        'Instanced',
        'Auto',
        'Indirect',
        'ClearColor',
        'ClearDepthStencil',
        'BeginPass',
        'EndPass',
        'APICalls',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
        128: 128,
        256: 256,
        512: 512,
        1024: 1024,
        2048: 2048,
        4096: 4096,
        65536: 65536,
        131072: 131072,
        262144: 262144,
        524288: 524288,
        1048576: 1048576,
        2097152: 2097152,
        4194304: 4194304,
        8388608: 8388608,
        16777216: 16777216,
    }


