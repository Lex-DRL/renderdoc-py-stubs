# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class CullMode(__enum.IntEnum):
    """
    The culling mode for polygons.
    
    .. data:: NoCull
    
      No polygon culling is performed.
    
    .. data:: Front
    
      Front-facing polygons are culled.
    
    .. data:: Back
    
      Back-facing polygons are culled.
    
    .. data:: FrontAndBack
    
      Both front-facing and back-facing polygons are culled.
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

    Back = 2
    Front = 1
    FrontAndBack = 3
    NoCull = 0
    _member_map_ = {
        'Back': 2,
        'Front': 1,
        'FrontAndBack': 3,
        'NoCull': 0,
    }
    _member_names_ = [
        'NoCull',
        'Front',
        'Back',
        'FrontAndBack',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


