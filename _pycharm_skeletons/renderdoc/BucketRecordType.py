# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class BucketRecordType(__enum.IntEnum):
    """
    The type of bucketing method for recording statistics.
    
    .. data:: Linear
    
      Each bucket contains a fixed number of elements. The highest bucket also accumulates any values
      too high for any of the buckets.
    
    .. data:: Pow2
    
      Each bucket holds twice as many elements as the previous one, with the first bucket containing
      just 1 (bucket index is ``log2(value)``).
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

    Linear = 0
    Pow2 = 1
    _member_map_ = {
        'Linear': 0,
        'Pow2': 1,
    }
    _member_names_ = [
        'Linear',
        'Pow2',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
    }


