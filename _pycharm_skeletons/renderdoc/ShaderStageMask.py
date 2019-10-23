# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ShaderStageMask(__enum.IntFlag):
    """
    A set of flags for ``ShaderStage`` stages
    
    .. data:: Unknown
    
      No flags set for any shader stages.
    
    .. data:: Vertex
    
      The flag for :data:`ShaderStage.Vertex`.
    
    .. data:: Hull
    
      The flag for :data:`ShaderStage.Hull`.
    
    .. data:: Tess_Control
    
      The flag for :data:`ShaderStage.Tess_Control`.
    
    .. data:: Domain
    
      The flag for :data:`ShaderStage.Domain`.
    
    .. data:: Tess_Eval
    
      The flag for :data:`ShaderStage.Tess_Eval`.
    
    .. data:: Geometry
    
      The flag for :data:`ShaderStage.Geometry`.
    
    .. data:: Pixel
    
      The flag for :data:`ShaderStage.Pixel`.
    
    .. data:: Fragment
    
      The flag for :data:`ShaderStage.Fragment`.
    
    .. data:: Compute
    
      The flag for :data:`ShaderStage.Compute`.
    
    .. data:: All
    
      A shorthand version with flags set for all stages together.
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

    All = 63
    Compute = 32
    Domain = 4
    Fragment = 16
    Geometry = 8
    Hull = 2
    Pixel = 16
    Tess_Control = 2
    Tess_Eval = 4
    Unknown = 0
    Vertex = 1
    _member_map_ = {
        'All': 63,
        'Compute': 32,
        'Domain': 4,
        'Fragment': 16,
        'Geometry': 8,
        'Hull': 2,
        'Pixel': 16,
        'Tess_Control': 2,
        'Tess_Eval': 4,
        'Unknown': 0,
        'Vertex': 1,
    }
    _member_names_ = [
        'Unknown',
        'Vertex',
        'Hull',
        'Domain',
        'Geometry',
        'Pixel',
        'Compute',
        'All',
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
        63: 63,
    }


