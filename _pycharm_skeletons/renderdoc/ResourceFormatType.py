# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ResourceFormatType(__enum.IntEnum):
    """
    A resource format's particular type. This accounts for either block-compressed textures
    or formats that don't have equal byte-multiple sizes for each channel.
    
    .. data:: Regular
    
      This format has no special layout, so its format is described by a number of components, a
      :class:`CompType` and a byte width per component.
    
    .. data:: Undefined
    
      This format is undefined or unknown, or does not map to any known regular format.
    
    .. data:: BC1
    
      A block-compressed texture in ``BC1`` format (RGB with 1-bit alpha, 0.5 bytes per pixel)
    
      Formerly known as ``DXT1``, commonly used for color maps.
    
    .. data:: BC2
    
      A block-compressed texture in ``BC2`` format (RGB with 4-bit alpha, 1 byte per pixel)
    
      Formerly known as ``DXT3``, rarely used.
    
    .. data:: BC3
    
      A block-compressed texture in ``BC3`` format (RGBA, 1 byte per pixel)
    
      Formerly known as ``DXT5``, commonly used for color + alpha maps, or color with attached
      single channel data.
    
    .. data:: BC4
    
      A block-compressed texture in ``BC4`` format (Single channel, 0.5 bytes per pixel)
    
      Commonly used for single component data such as gloss or height data.
    
    .. data:: BC5
    
      A block-compressed texture in ``BC5`` format (Two channels, 1 byte per pixel)
    
      Commonly used for normal maps.
    
    .. data:: BC6
    
      A block-compressed texture in ``BC6`` format (RGB floating point, 1 byte per pixel)
    
      Commonly used for HDR data of all kinds.
    
    .. data:: BC7
    
      A block-compressed texture in ``BC7`` format (RGB or RGBA, 1 byte per pixel)
    
      Commonly used for high quality color maps, with or without alpha.
    
    .. data:: ETC2
    
      A block-compressed texture in ``ETC2`` format (RGB with 1-bit alpha, 0.5 bytes per pixel)
    
      Commonly used on mobile or embedded platforms.
    
      Note that the mode added in ``EAC`` with 1 byte per pixel and full 8-bit alpha is
      grouped as ``EAC``, with a component count of 4. See :data:`EAC`.
    
    .. data:: EAC
    
      A block-compressed texture in ``EAC`` format, expanded from ``ETC2``.
    
      Commonly used on mobile or embedded platforms.
    
      The single and dual channel formats encode 11-bit data with 0.5 bytes per channel (so
      the single channel format is 0.5 bytes per pixel total, and the dual channel format is 1 byte per
      pixel total). The four channel format is encoded similarly to ETC2 for the base RGB data and
      similarly to the single channel format for the alpha, giving 1 byte per pixel total.
      See :data:`ETC2`.
    
    .. data:: ASTC
    
      A block-compressed texture in ``ASTC`` format (Representation varies a lot)
    
      The ASTC format encodes each block as 16 bytes, but the block size can vary from 4x4 (so 1 byte
      per pixel) up to 12x12 (0.11 bytes per pixel).
    
      Each block can encode between one and three channels of data, either correlated or uncorrelated,
      in low or high dynamic range.
    
      Commonly used on mobile or embedded platforms.
    
    .. data:: R10G10B10A2
    
      Each pixel is stored in 32 bits. Red, green and blue are stored in 10-bits each and alpha in 2
      bits. The data can either be :data:`unsigned normalised <CompType.UNorm>` or
      :data:`unsigned integer <CompType.UInt>`.
    
    .. data:: R11G11B10
    
      Each pixel is stored in 32 bits. Red and green are stored as an 11-bit float with no sign bit,
      5-bit exponent and 6-bit mantissa. Blue is stored with 5-bit exponent and 5-bit mantissa.
    
    .. data:: R5G6B5
    
      Each pixel is stored in 16 bits. Red and blue are stored as 5 bits, and green is stored as six.
      The data is :data:`unsigned normalised <CompType.UNorm>`.
    
    .. data:: R5G5B5A1
    
      Each pixel is stored in 16 bits. Red, green, and blue are stored as 5 bits, with 1-bit alpha.
      The data is :data:`unsigned normalised <CompType.UNorm>`.
    
    .. data:: R9G9B9E5
    
      Each pixel is stored in 32 bits. Red, green, and blue are stored with individual 9-bit mantissas
      and a shared 5-bit exponent. There are no sign bits.
    
    .. data:: R4G4B4A4
    
      Each pixel is stored in 16 bits. Red, green, blue, and alpha are stored as 4-bit
      :data:`unsigned normalised <CompType.UNorm>` values.
    
    .. data:: R4G4
    
      Each pixel is stored in 8 bits. Red and green are stored as 4-bit
      :data:`unsigned normalised <CompType.UNorm>` values.
    
    .. data:: D16S8
    
      Each pixel is considered a packed depth-stencil value with 16 bit normalised depth and 8 bit
      stencil.
    
    .. data:: D24S8
    
      Each pixel is considered a packed depth-stencil value with 24 bit normalised depth and 8 bit
      stencil.
    
    .. data:: D32S8
    
      Each pixel is considered a packed depth-stencil value with 32 bit floating point depth and 8 bit
      stencil.
    
    .. data:: S8
    
      Each pixel is an 8 bit stencil value.
    
    .. data:: YUV8
    
      The pixel data is 8-bit in YUV subsampled format. More information about subsampling setup is
      stored separately
    
    .. data:: YUV10
    
      The pixel data is 10-bit in YUV subsampled format. More information about subsampling setup is
      stored separately
    
    .. data:: YUV12
    
      The pixel data is 12-bit in YUV subsampled format. More information about subsampling setup is
      stored separately
    
    .. data:: YUV16
    
      The pixel data is 16-bit in YUV subsampled format. More information about subsampling setup is
      stored separately
    
    .. data:: PVRTC
    
      PowerVR properitary texture compression format.
    
    .. data:: A8
    
      8-bit unsigned normalised alpha - equivalent to standard R8 with a pre-baked swizzle.
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

    A8 = 28
    ASTC = 11
    BC1 = 2
    BC2 = 3
    BC3 = 4
    BC4 = 5
    BC5 = 6
    BC6 = 7
    BC7 = 8
    D16S8 = 19
    D24S8 = 20
    D32S8 = 21
    EAC = 10
    ETC2 = 9
    PVRTC = 27
    R10G10B10A2 = 12
    R11G11B10 = 13
    R4G4 = 18
    R4G4B4A4 = 17
    R5G5B5A1 = 15
    R5G6B5 = 14
    R9G9B9E5 = 16
    Regular = 0
    S8 = 22
    Undefined = 1
    YUV10 = 24
    YUV12 = 25
    YUV16 = 26
    YUV8 = 23
    _member_map_ = {
        'A8': 28,
        'ASTC': 11,
        'BC1': 2,
        'BC2': 3,
        'BC3': 4,
        'BC4': 5,
        'BC5': 6,
        'BC6': 7,
        'BC7': 8,
        'D16S8': 19,
        'D24S8': 20,
        'D32S8': 21,
        'EAC': 10,
        'ETC2': 9,
        'PVRTC': 27,
        'R10G10B10A2': 12,
        'R11G11B10': 13,
        'R4G4': 18,
        'R4G4B4A4': 17,
        'R5G5B5A1': 15,
        'R5G6B5': 14,
        'R9G9B9E5': 16,
        'Regular': 0,
        'S8': 22,
        'Undefined': 1,
        'YUV10': 24,
        'YUV12': 25,
        'YUV16': 26,
        'YUV8': 23,
    }
    _member_names_ = [
        'Regular',
        'Undefined',
        'BC1',
        'BC2',
        'BC3',
        'BC4',
        'BC5',
        'BC6',
        'BC7',
        'ETC2',
        'EAC',
        'ASTC',
        'R10G10B10A2',
        'R11G11B10',
        'R5G6B5',
        'R5G5B5A1',
        'R9G9B9E5',
        'R4G4B4A4',
        'R4G4',
        'D16S8',
        'D24S8',
        'D32S8',
        'S8',
        'YUV8',
        'YUV10',
        'YUV12',
        'YUV16',
        'PVRTC',
        'A8',
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
    }


