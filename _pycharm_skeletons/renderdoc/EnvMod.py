# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class EnvMod(__enum.IntEnum):
    """
    How to modify an environment variable.
    
    .. data:: Set
    
      Set the variable to the given value.
    
    .. data:: Append
    
      Add the given value to the end of the variable, using the separator.
    
    .. data:: Prepend
    
      Add the given value to the start of the variable, using the separator.
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

    Append = 1
    Prepend = 2
    Set = 0
    _member_map_ = {
        'Append': 1,
        'Prepend': 2,
        'Set': 0,
    }
    _member_names_ = [
        'Set',
        'Append',
        'Prepend',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


