# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class CompareFunction(__enum.IntEnum):
    """
    A comparison function to return a ``bool`` result from two inputs ``A`` and ``B``.
    
    .. data:: Never
    
      ``False``
    
    .. data:: AlwaysTrue
    
      ``True``
    
    .. data:: Less
    
      ``A < B``
    
    .. data:: LessEqual
    
      ``A <= B``
    
    .. data:: Greater
    
      ``A > B``
    
    .. data:: GreaterEqual
    
      ``A >= B``
    
    .. data:: Equal
    
      ``A == B``
    
    .. data:: NotEqual
    
      ``A != B``
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

    AlwaysTrue = 1
    Equal = 6
    Greater = 4
    GreaterEqual = 5
    Less = 2
    LessEqual = 3
    Never = 0
    NotEqual = 7
    _member_map_ = {
        'AlwaysTrue': 1,
        'Equal': 6,
        'Greater': 4,
        'GreaterEqual': 5,
        'Less': 2,
        'LessEqual': 3,
        'Never': 0,
        'NotEqual': 7,
    }
    _member_names_ = [
        'Never',
        'AlwaysTrue',
        'Less',
        'LessEqual',
        'Greater',
        'GreaterEqual',
        'Equal',
        'NotEqual',
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
    }


