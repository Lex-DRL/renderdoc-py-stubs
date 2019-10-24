# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class LogicOperation(__enum.IntEnum):
    """
    A logical operation to apply when writing texture values to an output.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "destination" value is the value in the target being written to.
    
    .. data:: NoOp
    
      No operation is performed, the destination is unmodified.
    
    .. data:: Clear
    
      A ``0`` in every bit.
    
    .. data:: Set
    
      A ``1`` in every bit.
    
    .. data:: Copy
    
      The contents of the source value.
    
    .. data:: CopyInverted
    
      The contents of the source value are bitwise inverted.
    
    .. data:: Invert
    
      The contents of the destination value are bitwise inverted, then written.
    
    .. data:: And
    
      The source and destination values are combined with the bitwise ``AND`` operator.
    
    .. data:: Nand
    
      The source and destination values are combined with the bitwise ``NAND`` operator.
    
    .. data:: Or
    
      The source and destination values are combined with the bitwise ``OR`` operator.
    
    .. data:: Xor
    
      The source and destination values are combined with the bitwise ``XOR`` operator.
    
    .. data:: Nor
    
      The source and destination values are combined with the bitwise ``NOR`` operator.
    
    .. data:: Equivalent
    
      The source and destination values are combined with the logical equivalence operator, defined as
      ``NOT (s XOR d)``.
    
    .. data:: AndReverse
    
      The source and inverted destination values are combined with the bitwise ``AND`` operator - i.e.
      ``s AND (NOT d)``.
    
    .. data:: AndInverted
    
      The inverted source and destination values are combined with the bitwise ``AND`` operator - i.e.
      ``(NOT s) AND d``.
    
    .. data:: OrReverse
    
      The source and inverted destination values are combined with the bitwise ``OR`` operator - i.e.
      ``s OR (NOT d)``.
    
    .. data:: OrInverted
    
      The inverted source and destination values are combined with the bitwise ``OR`` operator - i.e.
      ``(NOT s) OR d``.
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

    And = 6
    AndInverted = 13
    AndReverse = 12
    Clear = 1
    Copy = 3
    CopyInverted = 4
    Equivalent = 11
    Invert = 5
    Nand = 7
    NoOp = 0
    Nor = 10
    Or = 8
    OrInverted = 15
    OrReverse = 14
    Set = 2
    Xor = 9
    _member_map_ = {
        'And': 6,
        'AndInverted': 13,
        'AndReverse': 12,
        'Clear': 1,
        'Copy': 3,
        'CopyInverted': 4,
        'Equivalent': 11,
        'Invert': 5,
        'Nand': 7,
        'NoOp': 0,
        'Nor': 10,
        'Or': 8,
        'OrInverted': 15,
        'OrReverse': 14,
        'Set': 2,
        'Xor': 9,
    }
    _member_names_ = [
        'NoOp',
        'Clear',
        'Set',
        'Copy',
        'CopyInverted',
        'Invert',
        'And',
        'Nand',
        'Or',
        'Xor',
        'Nor',
        'Equivalent',
        'AndReverse',
        'AndInverted',
        'OrReverse',
        'OrInverted',
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
        13: 13,
        14: 14,
        15: 15,
    }


