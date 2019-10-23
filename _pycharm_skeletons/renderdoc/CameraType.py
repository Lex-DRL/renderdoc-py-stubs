# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class CameraType(__enum.IntEnum):
    """
    The type of camera controls for an :class:`Camera`.
    
    .. data:: Arcball
    
      Arcball controls that rotate and zoom around the origin point.
    
    .. data:: FPSLook
    
      Traditional FPS style controls with movement in each axis relative to the current look direction.
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

    Arcball = 0
    FPSLook = 1
    _member_map_ = {
        'Arcball': 0,
        'FPSLook': 1,
    }
    _member_names_ = [
        'Arcball',
        'FPSLook',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
    }


