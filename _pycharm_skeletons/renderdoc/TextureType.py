# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class TextureType(__enum.IntEnum):
    """
    The dimensionality of a texture binding.
    
    .. data:: Unknown
    
      An unknown type of texture.
    
    .. data:: Buffer
    
      A texel buffer.
    
    .. data:: Texture1D
    
      A 1D texture.
    
    .. data:: Texture1DArray
    
      A 1D texture array.
    
    .. data:: Texture2D
    
      A 2D texture.
    
    .. data:: TextureRect
    
      A rectangle texture, a legacy format for non-power of two textures.
    
    .. data:: Texture2DArray
    
      A 2D texture array.
    
    .. data:: Texture2DMS
    
      A multi-sampled 2D texture.
    
    .. data:: Texture2DMSArray
    
      A multi-sampled 2D texture array.
    
    .. data:: Texture3D
    
      A 3D texture.
    
    .. data:: TextureCube
    
      A Cubemap texture.
    
    .. data:: TextureCubeArray
    
      A Cubemap texture array.
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

    Buffer = 1
    Count = 12
    First = 0
    Texture1D = 2
    Texture1DArray = 3
    Texture2D = 4
    Texture2DArray = 6
    Texture2DMS = 7
    Texture2DMSArray = 8
    Texture3D = 9
    TextureCube = 10
    TextureCubeArray = 11
    TextureRect = 5
    Unknown = 0
    _member_map_ = {
        'Buffer': 1,
        'Count': 12,
        'First': 0,
        'Texture1D': 2,
        'Texture1DArray': 3,
        'Texture2D': 4,
        'Texture2DArray': 6,
        'Texture2DMS': 7,
        'Texture2DMSArray': 8,
        'Texture3D': 9,
        'TextureCube': 10,
        'TextureCubeArray': 11,
        'TextureRect': 5,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'Buffer',
        'Texture1D',
        'Texture1DArray',
        'Texture2D',
        'TextureRect',
        'Texture2DArray',
        'Texture2DMS',
        'Texture2DMSArray',
        'Texture3D',
        'TextureCube',
        'TextureCubeArray',
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
    }


