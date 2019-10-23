# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class CompType(__enum.IntEnum):
    """
    Represents the component type of a channel in a texture or element in a structure.
    
    .. data:: Typeless
    
      A component that has no concrete type.
    
    .. data:: Float
    
      A single-precision (32-bit) floating point value. This is an IEEE float with 1 sign bit,
      8 bits of exponent and 23 bits of mantissa.
    
    .. data:: UNorm
    
      An unsigned normalised floating point value. This is converted by dividing the input value by
      the maximum representable unsigned integer value, to produce a value in the range ``[0, 1]``
    
    .. data:: SNorm
    
      A signed normalised floating point value in range. This is converted by dividing the input value
      by the maximum representable *positive signed* integer value, to produce a value in the range
      ``[-1, 1]``. As a special case, the maximum negative signed integer is also mapped to ``-1`` so
      there are two representations of -1. This means there is only one ``0`` value and that there is
      the same range of available values for positive and negative values.
    
      For example, signed 16-bit integers range from ``-32768`` to ``+32767``. ``-32768`` is mapped to
      ``-1``, and then any other value is divided by ``32767`` giving an equal set of values in the
      range ``[-1, 0]`` as in the range ``[0, 1]``.
    
    .. data:: UInt
    
      An unsigned integer value.
    
    .. data:: SInt
    
      A signed integer value.
    
    .. data:: UScaled
    
      An unsigned scaled floating point value. This is converted from the input unsigned integer without
      any normalisation as with :data:`UNorm`, so the resulting values range from ``0`` to the maximum
      unsigned integer value ``2^N - 1``.
    
    .. data:: SScaled
    
      A signed scaled floating point value. This is converted from the input unsigned integer without
      any normalisation as with :data:`SNorm`, so the resulting values range from the minimum signed
      integer value ``-2^(N-1)`` to the maximum signed integer value ``2^(N-1) - 1``.
    
    .. data:: Depth
    
      An opaque value storing depth information, either :data:`unsigned normalised <UNorm>` or
      :data:`floating point <float>`.
    
    .. data:: Double
    
      A double-precision (64-bit) floating point value.
    
    .. data:: UNormSRGB
    
      Similar to :data:`UNorm` normalised between the minimum and maximum unsigned values to ``0.0`` -
      ``1.0``, but with an sRGB gamma curve applied.
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

    Depth = 8
    Double = 9
    Float = 1
    SInt = 5
    SNorm = 3
    SScaled = 7
    Typeless = 0
    UInt = 4
    UNorm = 2
    UNormSRGB = 10
    UScaled = 6
    _member_map_ = {
        'Depth': 8,
        'Double': 9,
        'Float': 1,
        'SInt': 5,
        'SNorm': 3,
        'SScaled': 7,
        'Typeless': 0,
        'UInt': 4,
        'UNorm': 2,
        'UNormSRGB': 10,
        'UScaled': 6,
    }
    _member_names_ = [
        'Typeless',
        'Float',
        'UNorm',
        'SNorm',
        'UInt',
        'SInt',
        'UScaled',
        'SScaled',
        'Depth',
        'Double',
        'UNormSRGB',
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
    }


