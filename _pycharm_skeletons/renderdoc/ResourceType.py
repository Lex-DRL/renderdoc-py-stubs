# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ResourceType(__enum.IntEnum):
    """
    The type of a resource referred to by binding or API usage.
    
    In some cases there is a little overlap or fudging when mapping API concepts - this is primarily
    just intended for e.g. fuzzy user filtering or rough categorisation. Precise mapping would require
    API-specific concepts.
    
    .. data:: Unknown
    
      An unknown type of resource.
    
    .. data:: Device
    
      A system-level object, typically unique.
    
    .. data:: Queue
    
      A queue representing the ability to execute commands in a single stream, possibly in parallel to
      other queues.
    
    .. data:: CommandBuffer
    
      A recorded set of commands that can then be subsequently executed.
    
    .. data:: Texture
    
      A texture - one- to three- dimensional, possibly with array layers and mip levels. See
      :class:`TextureDescription`.
    
    .. data:: Buffer
    
      A linear (possibly typed) view of memory. See :class:`BufferDescription`.
    
    .. data:: View
    
      A particular view into a texture or buffer, e.g. either accessing the underlying resource through
      a different type, or only a subset of the resource.
    
    .. data:: Sampler
    
      The information regarding how a texture is accessed including wrapping, minification/magnification
      and other information. The precise details are API-specific and listed in the API state when
      bound.
    
    .. data:: SwapchainImage
    
      A special class of :data:`Texture` that is owned by the swapchain and is used for presentation.
    
    .. data:: Memory
    
      An object corresponding to an actual memory allocation, which other resources can then be bound
      to.
    
    .. data:: Shader
    
      A single shader object for any shader stage. May be bound directly, or used to compose into a
      :data:`PipelineState` depending on the API.
    
    .. data:: ShaderBinding
    
      An object that determines some manner of shader binding. Since this varies significantly by API,
      different concepts used for shader resource binding fall under this type.
    
    .. data:: PipelineState
    
      A single object containing all information regarding the current GPU pipeline, containing both
      shader objects, potentially some shader binding information, and fixed-function state.
    
    .. data:: StateObject
    
      A single object encapsulating some amount of related state that can be set together, instead of
      setting each individual state separately.
    
    .. data:: RenderPass
    
      An object related to collecting render pass information together. This may not be an actual
      explicit render pass object if it doesn't exist in the API, it may also be a collection of
      textures in a framebuffer that are bound together to the API for rendering.
    
    .. data:: Query
    
      A query for retrieving some kind of feedback from the GPU, either as a fixed number or a boolean
      value which can be used in predicated rendering.
    
    .. data:: Sync
    
      A synchronisation object used for either synchronisation between GPU and CPU, or GPU-to-GPU work.
    
    .. data:: Pool
    
      An object which pools together other objects in an opaque way, either for runtime allocation and
      deallocation, or for caching purposes.
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

    Buffer = 5
    CommandBuffer = 3
    Device = 1
    Memory = 9
    PipelineState = 12
    Pool = 17
    Query = 15
    Queue = 2
    RenderPass = 14
    Sampler = 7
    Shader = 10
    ShaderBinding = 11
    StateObject = 13
    SwapchainImage = 8
    Sync = 16
    Texture = 4
    Unknown = 0
    View = 6
    _member_map_ = {
        'Buffer': 5,
        'CommandBuffer': 3,
        'Device': 1,
        'Memory': 9,
        'PipelineState': 12,
        'Pool': 17,
        'Query': 15,
        'Queue': 2,
        'RenderPass': 14,
        'Sampler': 7,
        'Shader': 10,
        'ShaderBinding': 11,
        'StateObject': 13,
        'SwapchainImage': 8,
        'Sync': 16,
        'Texture': 4,
        'Unknown': 0,
        'View': 6,
    }
    _member_names_ = [
        'Unknown',
        'Device',
        'Queue',
        'CommandBuffer',
        'Texture',
        'Buffer',
        'View',
        'Sampler',
        'SwapchainImage',
        'Memory',
        'Shader',
        'ShaderBinding',
        'PipelineState',
        'StateObject',
        'RenderPass',
        'Query',
        'Sync',
        'Pool',
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
    }


