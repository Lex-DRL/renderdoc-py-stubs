# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class VarType(__enum.IntEnum):
    """
    Represents the base type of a shader variable in debugging or constant blocks.
    
    .. data:: Float
    
      A single-precision (32-bit) floating point value.
    
    .. data:: Double
    
      A double-precision (64-bit) floating point value.
    
    .. data:: Half
    
      A half-precision (16-bit) floating point value.
    
    .. data:: SInt
    
      A signed 32-bit integer value.
    
    .. data:: UInt
    
      An unsigned 32-bit integer value.
    
    .. data:: SShort
    
      A signed 16-bit integer value.
    
    .. data:: UShort
    
      An unsigned 16-bit integer value.
    
    .. data:: SLong
    
      A signed 64-bit integer value.
    
    .. data:: ULong
    
      An unsigned 64-bit integer value.
    
    .. data:: SByte
    
      A signed 8-bit integer value.
    
    .. data:: UByte
    
      An unsigned 8-bit integer value.
    
    .. data:: Unknown
    
      An unknown type.
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

    Double = 1
    Float = 0
    Half = 2
    SByte = 9
    SInt = 3
    SLong = 7
    SShort = 5
    UByte = 10
    UInt = 4
    ULong = 8
    Unknown = -1
    UShort = 6
    _member_map_ = {
        'Double': 1,
        'Float': 0,
        'Half': 2,
        'SByte': 9,
        'SInt': 3,
        'SLong': 7,
        'SShort': 5,
        'UByte': 10,
        'UInt': 4,
        'ULong': 8,
        'UShort': 6,
        'Unknown': -1,
    }
    _member_names_ = [
        'Float',
        'Double',
        'Half',
        'SInt',
        'UInt',
        'SShort',
        'UShort',
        'SLong',
        'ULong',
        'SByte',
        'UByte',
        'Unknown',
    ]
    _member_type_ = int
    _value2member_map_ = {
        -1: -1,
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
    }


