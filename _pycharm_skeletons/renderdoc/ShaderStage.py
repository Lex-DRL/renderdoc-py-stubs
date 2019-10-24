# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ShaderStage(__enum.IntEnum):
    """
    The stage in a pipeline where a shader runs
    
    .. data:: Vertex
    
      The vertex shader.
    
    .. data:: Hull
    
      The hull shader. See also :data:`Tess_Control`.
    
    .. data:: Tess_Control
    
      The tessellation control shader. See also :data:`Hull`.
    
    .. data:: Domain
    
      The domain shader. See also :data:`Tess_Eval`.
    
    .. data:: Tess_Eval
    
      The tessellation evaluation shader. See also :data:`Domain`.
    
    .. data:: Geometry
    
      The geometry shader.
    
    .. data:: Pixel
    
      The pixel shader. See also :data:`Fragment`.
    
    .. data:: Fragment
    
      The fragment shader. See also :data:`Pixel`.
    
    .. data:: Compute
    
      The compute shader.
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

    Compute = 5
    Count = 6
    Domain = 2
    First = 0
    Fragment = 4
    Geometry = 3
    Hull = 1
    Pixel = 4
    Tess_Control = 1
    Tess_Eval = 2
    Vertex = 0
    _member_map_ = {
        'Compute': 5,
        'Count': 6,
        'Domain': 2,
        'First': 0,
        'Fragment': 4,
        'Geometry': 3,
        'Hull': 1,
        'Pixel': 4,
        'Tess_Control': 1,
        'Tess_Eval': 2,
        'Vertex': 0,
    }
    _member_names_ = [
        'Vertex',
        'Hull',
        'Domain',
        'Geometry',
        'Pixel',
        'Compute',
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


