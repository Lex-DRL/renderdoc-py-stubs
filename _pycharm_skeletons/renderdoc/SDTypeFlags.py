# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SDTypeFlags(__enum.IntEnum):
    """
    Bitfield flags that could be applied to a type.
    
    .. data:: NoFlags
    
      This type has no special properties.
    
    .. data:: HasCustomString
    
      This type has a custom string. This could be used for example for enums, to display the string
      value of the enum as well as the integer storage, or perhaps for opaque types that should be
      displayed to the user as a string even if the underlying representation is not a string.
    
    .. data:: Hidden
    
      This type is considered an implementation detail and should not typically be displayed to the user.
    
    .. data:: Nullable
    
      This type is nullable and can sometimes be removed and replaced simply with a Null type. See
      :data:`SDBasic.Null`.
    
    .. data:: NullString
    
      Special flag to indicate that this is a C-string which was NULL, not just empty.
    
    .. data:: FixedArray
    
      Special flag to indicate that this is array was a fixed-size real array, rather than a complex
      container type or a pointer & length.
    
    .. data:: Union
    
      Special flag to indicate that this is structure is stored as a union, meaning all children share
      the same memory and some external flag indicates which element is valid.
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

    FixedArray = 16
    HasCustomString = 1
    Hidden = 2
    NoFlags = 0
    Nullable = 4
    NullString = 8
    Union = 32
    _member_map_ = {
        'FixedArray': 16,
        'HasCustomString': 1,
        'Hidden': 2,
        'NoFlags': 0,
        'NullString': 8,
        'Nullable': 4,
        'Union': 32,
    }
    _member_names_ = [
        'NoFlags',
        'HasCustomString',
        'Hidden',
        'Nullable',
        'NullString',
        'FixedArray',
        'Union',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
    }


