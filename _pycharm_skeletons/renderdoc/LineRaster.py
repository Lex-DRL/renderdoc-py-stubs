# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class LineRaster(__enum.IntEnum):
    """
    The line rasterization mode.
    
    .. data:: Default
    
      Default line rasterization mode as defined by the API specification.
    
    .. data:: Rectangular
    
      Lines are rasterized as rectangles extruded from the line.
    
    .. data:: Bresenham
    
      Lines are rasterized according to the bresenham line algorithm.
    
    .. data:: RectangularSmooth
    
      Lines are rasterized as rectangles extruded from the line with coverage falloff.
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

    Bresenham = 2
    Default = 0
    Rectangular = 1
    RectangularSmooth = 3
    _member_map_ = {
        'Bresenham': 2,
        'Default': 0,
        'Rectangular': 1,
        'RectangularSmooth': 3,
    }
    _member_names_ = [
        'Default',
        'Rectangular',
        'Bresenham',
        'RectangularSmooth',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


