# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class GraphicsAPI(__enum.IntEnum):
    """
    Identifies a Graphics API.
    
    .. data:: D3D11
    
      Direct3D 11.
    
    .. data:: D3D12
    
      Direct3D 12.
    
    .. data:: OpenGL
    
      OpenGL.
    
    .. data:: Vulkan
    
      Vulkan.
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

    D3D11 = 0
    D3D12 = 1
    OpenGL = 2
    Vulkan = 3
    _member_map_ = {
        'D3D11': 0,
        'D3D12': 1,
        'OpenGL': 2,
        'Vulkan': 3,
    }
    _member_names_ = [
        'D3D11',
        'D3D12',
        'OpenGL',
        'Vulkan',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


