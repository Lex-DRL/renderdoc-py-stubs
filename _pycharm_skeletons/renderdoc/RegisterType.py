# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class RegisterType(__enum.IntEnum):
    """
    Represents the type of register a local variable maps to.
    
    .. data:: Undefined
    
      No defined register.
    
    .. data:: Input
    
      An input register.
    
    .. data:: Temporary
    
      A normal temporary register.
    
    .. data:: IndexedTemporary
    
      An indexed temporary register.
    
    .. data:: Output
    
      An output register.
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

    IndexedTemporary = 3
    Input = 1
    Output = 4
    Temporary = 2
    Undefined = 0
    _member_map_ = {
        'IndexedTemporary': 3,
        'Input': 1,
        'Output': 4,
        'Temporary': 2,
        'Undefined': 0,
    }
    _member_names_ = [
        'Undefined',
        'Input',
        'Temporary',
        'IndexedTemporary',
        'Output',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


