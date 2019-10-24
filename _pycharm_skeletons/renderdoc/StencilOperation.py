# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class StencilOperation(__enum.IntEnum):
    """
    A stencil operation to apply in stencil processing.
    
    .. data:: Keep
    
      Keep the existing value unmodified.
    
    .. data:: Zero
    
      Set the value to ``0``.
    
    .. data:: Replace
    
      Replace the value with the stencil reference value.
    
    .. data:: IncSat
    
      Increment the value but saturate at the maximum representable value (typically ``255``).
    
    .. data:: DecSat
    
      Decrement the value but saturate at ``0``.
    
    .. data:: IncWrap
    
      Increment the value and wrap at the maximum representable value (typically ``255``) to ``0``.
    
    .. data:: DecWrap
    
      Decrement the value and wrap at ``0`` to the maximum representable value (typically ``255``).
    
    .. data:: Invert
    
      Invert the bits in the stencil value (bitwise ``NOT``).
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

    DecSat = 4
    DecWrap = 6
    IncSat = 3
    IncWrap = 5
    Invert = 7
    Keep = 0
    Replace = 2
    Zero = 1
    _member_map_ = {
        'DecSat': 4,
        'DecWrap': 6,
        'IncSat': 3,
        'IncWrap': 5,
        'Invert': 7,
        'Keep': 0,
        'Replace': 2,
        'Zero': 1,
    }
    _member_names_ = [
        'Keep',
        'Zero',
        'Replace',
        'IncSat',
        'DecSat',
        'IncWrap',
        'DecWrap',
        'Invert',
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


