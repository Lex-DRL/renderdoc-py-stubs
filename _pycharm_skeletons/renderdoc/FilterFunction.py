# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class FilterFunction(__enum.IntEnum):
    """
    The function used to process the returned value after interpolation.
    
    .. data:: Normal
    
      No special processing is used, the value is returned directly to the shader.
    
    .. data:: Comparison
    
      The value from interpolation is compared to a reference value and the comparison result is
      returned to the shader.
    
    .. data:: Minimum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a min filter is
      used instead to find the minimum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the min function.
    
    .. data:: Maximum
    
      Instead of interpolating between sample points to retrieve an interpolated value, a max filter is
      used instead to find the maximum sample value.
    
      Texels that were weight to 0 during interpolation are not included in the max function.
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

    Comparison = 1
    Maximum = 3
    Minimum = 2
    Normal = 0
    _member_map_ = {
        'Comparison': 1,
        'Maximum': 3,
        'Minimum': 2,
        'Normal': 0,
    }
    _member_names_ = [
        'Normal',
        'Comparison',
        'Minimum',
        'Maximum',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


