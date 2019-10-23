# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class FilterMode(__enum.IntEnum):
    """
    The texture filtering mode for a given direction (minification, magnification, or
    between mips).
    
    .. data:: NoFilter
    
      No filtering - this direction is disabled or there is no sampler.
    
    .. data:: Point
    
      Point or nearest filtering - the closest pixel or mip level to the sample location is used.
    
    .. data:: Linear
    
      Linear filtering - a linear interpolation happens between the pixels or mips on either side of the
      sample location in each direction.
    
    .. data:: Cubic
    
      Similar to linear filtering but with a cubic curve used for interpolation instead of linear.
    
    .. data:: Anisotropic
    
      This sampler is using anisotropic filtering.
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

    Anisotropic = 4
    Cubic = 3
    Linear = 2
    NoFilter = 0
    Point = 1
    _member_map_ = {
        'Anisotropic': 4,
        'Cubic': 3,
        'Linear': 2,
        'NoFilter': 0,
        'Point': 1,
    }
    _member_names_ = [
        'NoFilter',
        'Point',
        'Linear',
        'Cubic',
        'Anisotropic',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


