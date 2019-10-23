# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class TextureSwizzle(__enum.IntEnum):
    """
    A single source component for a destination texture swizzle.
    
    .. data:: Red
    
      The Red component.
    
    .. data:: Green
    
      The Green component.
    
    .. data:: Blue
    
      The Blue component.
    
    .. data:: Alpha
    
      The Alpha component.
    
    .. data:: Zero
    
      The fixed value ``0``.
    
    .. data:: One
    
      The fixed value ``1``.
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

    Alpha = 3
    Blue = 2
    Green = 1
    One = 5
    Red = 0
    Zero = 4
    _member_map_ = {
        'Alpha': 3,
        'Blue': 2,
        'Green': 1,
        'One': 5,
        'Red': 0,
        'Zero': 4,
    }
    _member_names_ = [
        'Red',
        'Green',
        'Blue',
        'Alpha',
        'Zero',
        'One',
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


