# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class CounterUnit(__enum.IntEnum):
    """
    The unit that GPU counter data is returned in.
    
    .. data:: Absolute
    
      The value is an absolute value and should be interpreted as unitless.
    
    .. data:: Seconds
    
      The value is a duration in seconds.
    
    .. data:: Percentage
    
      The value is a floating point percentage value between 0.0 and 1.0.
    
    .. data:: Ratio
    
      The value describes a ratio between two separate GPU units or counters.
    
    .. data:: Bytes
    
      The value is in bytes.
    
    .. data:: Cycles
    
      The value is a duration in clock cycles.
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

    Absolute = 0
    Bytes = 4
    Cycles = 5
    Percentage = 2
    Ratio = 3
    Seconds = 1
    _member_map_ = {
        'Absolute': 0,
        'Bytes': 4,
        'Cycles': 5,
        'Percentage': 2,
        'Ratio': 3,
        'Seconds': 1,
    }
    _member_names_ = [
        'Absolute',
        'Seconds',
        'Percentage',
        'Ratio',
        'Bytes',
        'Cycles',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }


