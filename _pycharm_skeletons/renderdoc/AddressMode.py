# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class AddressMode(__enum.IntEnum):
    """
    A texture addressing mode in a single direction (U,V or W).
    
    .. data:: Wrap
    
      The texture is tiled at every multiple of 1.0.
    
    .. data:: Repeat
    
      Alias of :data:`Wrap`.
    
    .. data:: Mirror
    
      The texture is tiled as with :data:`Wrap`, but with the absolute value of the texture co-ordinate.
    
    .. data:: MirrorRepeat
    
      Alias of :data:`Mirror`.
    
    .. data:: MirrorOnce
    
      The texture is mirrored with :data:`Mirror`, but the texture does not tile as with
      :data:`ClampEdge`.
    
    .. data:: MirrorClamp
    
      Alias of :data:`MirrorOnce`.
    
    .. data:: ClampEdge
    
      The texture is clamped to the range of ``[0.0, 1.0]`` and the texture value at each end used.
    
    .. data:: ClampBorder
    
      The texture is clamped such that texture co-ordinates outside the range of ``[0.0, 1.0]`` are set
      to the border color specified in the sampler.
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

    ClampBorder = 4
    ClampEdge = 3
    Mirror = 1
    MirrorClamp = 2
    MirrorOnce = 2
    MirrorRepeat = 1
    Repeat = 0
    Wrap = 0
    _member_map_ = {
        'ClampBorder': 4,
        'ClampEdge': 3,
        'Mirror': 1,
        'MirrorClamp': 2,
        'MirrorOnce': 2,
        'MirrorRepeat': 1,
        'Repeat': 0,
        'Wrap': 0,
    }
    _member_names_ = [
        'Wrap',
        'Mirror',
        'MirrorOnce',
        'ClampEdge',
        'ClampBorder',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


