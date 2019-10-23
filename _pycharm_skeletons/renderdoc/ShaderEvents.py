# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ShaderEvents(__enum.IntFlag):
    """
    A set of flags for events that may occur while debugging a shader
    
    .. data:: NoEvent
    
      No event has occurred.
    
    .. data:: SampleLoadGather
    
      A texture was sampled, loaded or gathered.
    
    .. data:: GeneratedNanOrInf
    
      A floating point operation generated a ``NaN`` or ``infinity`` result.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initital start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    GeneratedNanOrInf = 2
    NoEvent = 0
    SampleLoadGather = 1
    _member_map_ = {
        'GeneratedNanOrInf': 2,
        'NoEvent': 0,
        'SampleLoadGather': 1,
    }
    _member_names_ = [
        'NoEvent',
        'SampleLoadGather',
        'GeneratedNanOrInf',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


