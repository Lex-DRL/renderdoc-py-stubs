# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ReplayOutputType(__enum.IntEnum):
    """
    The type of :class:`ReplayOutput` to create
    
    .. data:: Headless
    
      A headless output that does nothing to display to windows but can still be controlled and
      queried the same way
    
    .. data:: Texture
    
      An output that is used for displaying textures, thumbnails and pixel context
    
    .. data:: Mesh
    
      An output that will display mesh data previews
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

    Headless = 0
    Mesh = 2
    Texture = 1
    _member_map_ = {
        'Headless': 0,
        'Mesh': 2,
        'Texture': 1,
    }
    _member_names_ = [
        'Headless',
        'Texture',
        'Mesh',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


