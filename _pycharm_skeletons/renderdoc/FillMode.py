# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class FillMode(__enum.IntEnum):
    """
    The fill mode for polygons.
    
    .. data:: Solid
    
      Polygons are filled in and rasterized solidly.
    
    .. data:: Wireframe
    
      Polygons are rendered only with lines along their edges, forming a wireframe.
    
    .. data:: Point
    
      Only the points at the polygons vertices are rendered.
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

    Point = 2
    Solid = 0
    Wireframe = 1
    _member_map_ = {
        'Point': 2,
        'Solid': 0,
        'Wireframe': 1,
    }
    _member_names_ = [
        'Solid',
        'Wireframe',
        'Point',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


