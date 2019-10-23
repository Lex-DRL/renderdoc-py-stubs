# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class QualityHint(__enum.IntEnum):
    """
    An API specific hint for a certain behaviour. A legacy concept in OpenGL that controls
    hints to the implementation where there is room for interpretation within the range of valid
    behaviour.
    
    .. data:: DontCare
    
      The hinted behaviour can follow any valid path as the implementation decides.
    
    .. data:: Nicest
    
      The hinted behaviour should follow the most correct or highest quality path.
    
    .. data:: Fastest
    
      The hinted behaviour should follow the most efficient path.
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

    DontCare = 0
    Fastest = 2
    Nicest = 1
    _member_map_ = {
        'DontCare': 0,
        'Fastest': 2,
        'Nicest': 1,
    }
    _member_names_ = [
        'DontCare',
        'Nicest',
        'Fastest',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


