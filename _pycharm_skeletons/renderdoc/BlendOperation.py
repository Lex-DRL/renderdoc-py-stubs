# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class BlendOperation(__enum.IntEnum):
    """
    A blending operation to apply in color blending.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "destination" value is the value in the target being blended to.
    
      These values are multiplied by a given blend factor, see :class:`BlendMultiplier`.
    
    .. data:: Add
    
      Add the two values being processed together.
    
    .. data:: Subtract
    
      Subtract the destination value from the source value.
    
    .. data:: ReversedSubtract
    
      Subtract the source value from the destination value.
    
    .. data:: Minimum
    
      The minimum of the source and destination value.
    
    .. data:: Maximum
    
      The maximum of the source and destination value.
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

    Add = 0
    Maximum = 4
    Minimum = 3
    ReversedSubtract = 2
    Subtract = 1
    _member_map_ = {
        'Add': 0,
        'Maximum': 4,
        'Minimum': 3,
        'ReversedSubtract': 2,
        'Subtract': 1,
    }
    _member_names_ = [
        'Add',
        'Subtract',
        'ReversedSubtract',
        'Minimum',
        'Maximum',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


