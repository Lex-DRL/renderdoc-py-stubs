# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ShaderEncoding(__enum.IntEnum):
    """
    Identifies a shader encoding used to pass shader code to an API.
    
    .. data:: Unknown
    
      Unknown or unprocessable format.
    
    .. data:: DXBC
    
      DXBC binary shader, used by D3D11 and D3D12.
    
    .. data:: GLSL
    
      GLSL in string format, used by OpenGL.
    
    .. data:: SPIRV
    
      SPIR-V binary shader, used by Vulkan and with an extension by OpenGL.
    
    .. data:: SPIRVAsm
    
      Canonical SPIR-V assembly form, used (indirectly via :data:`SPIRV`) by Vulkan and with an
      extension by OpenGL.
    
    .. data:: HLSL
    
      HLSL in string format, used by D3D11, D3D12, and Vulkan/GL via compilation to SPIR-V.
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

    Count = 6
    DXBC = 1
    First = 0
    GLSL = 2
    HLSL = 5
    SPIRV = 3
    SPIRVAsm = 4
    Unknown = 0
    _member_map_ = {
        'Count': 6,
        'DXBC': 1,
        'First': 0,
        'GLSL': 2,
        'HLSL': 5,
        'SPIRV': 3,
        'SPIRVAsm': 4,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'DXBC',
        'GLSL',
        'SPIRV',
        'SPIRVAsm',
        'HLSL',
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
    }


