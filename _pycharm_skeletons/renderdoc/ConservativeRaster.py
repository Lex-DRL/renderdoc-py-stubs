# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ConservativeRaster(__enum.IntEnum):
    """
    The conservative rasterization mode.
    
    .. data:: Disabled
    
      No conservative rasterization, the default rasterization coverage algorithm is used.
    
    .. data:: Underestimate
    
      Fragments will only be generated if the primitive full covers all parts of the pixel, including
      edges and corners.
    
    .. data:: Overestimate
    
      Fragments will be generated if the primitive covers any part of the pixel, including edges and
      corners.
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

    Disabled = 0
    Overestimate = 2
    Underestimate = 1
    _member_map_ = {
        'Disabled': 0,
        'Overestimate': 2,
        'Underestimate': 1,
    }
    _member_names_ = [
        'Disabled',
        'Underestimate',
        'Overestimate',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


