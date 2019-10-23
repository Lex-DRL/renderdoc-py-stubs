# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SDBasic(__enum.IntEnum):
    """
    The basic irreducible type of an object. Every other more complex type is built on these.
    
    .. data:: Chunk
    
      A 'special' type indicating that the object is a chunk. A chunk can be treated like a
      :data:`Struct` otherwise. See :class:`SDChunk`.
    
    .. data:: Struct
    
      A composite type with some number of children of different types, each child with its own name.
      May in some cases be empty, so the presence of children should not be assumed.
    
    .. data:: Array
    
      A composite type with some number of children with an identical type and referred to purely by
      their index in the array. May be empty.
    
    .. data:: Null
    
      An indicator that an object could be here, but is optional and is currently not present. See
      :data:`SDTypeFlags.Nullable`.
    
    .. data:: Buffer
    
      An opaque byte buffer.
    
    .. data:: String
    
      A string, encoded as UTF-8.
    
    .. data:: Enum
    
      An enum value - stored as an integer but with a distinct set of possible named values.
    
    .. data:: UnsignedInteger
    
      An unsigned integer.
    
    .. data:: SignedInteger
    
      An signed integer.
    
    .. data:: Float
    
      A floating point value.
    
    .. data:: Boolean
    
      A boolean true/false value.
    
    .. data:: Character
    
      A single byte character. Wide/multi-byte characters are not supported (these would be stored as a
      string with 1 character and multiple bytes in UTF-8).
    
    .. data:: Resource
    
      A ResourceId. Equivalent to (and stored as) an 8-byte unsigned integer, but specifically contains
      the unique Id of a resource in a capture.
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

    Array = 2
    Boolean = 10
    Buffer = 4
    Character = 11
    Chunk = 0
    Enum = 6
    Float = 9
    Null = 3
    Resource = 12
    SignedInteger = 8
    String = 5
    Struct = 1
    UnsignedInteger = 7
    _member_map_ = {
        'Array': 2,
        'Boolean': 10,
        'Buffer': 4,
        'Character': 11,
        'Chunk': 0,
        'Enum': 6,
        'Float': 9,
        'Null': 3,
        'Resource': 12,
        'SignedInteger': 8,
        'String': 5,
        'Struct': 1,
        'UnsignedInteger': 7,
    }
    _member_names_ = [
        'Chunk',
        'Struct',
        'Array',
        'Null',
        'Buffer',
        'String',
        'Enum',
        'UnsignedInteger',
        'SignedInteger',
        'Float',
        'Boolean',
        'Character',
        'Resource',
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
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
    }


