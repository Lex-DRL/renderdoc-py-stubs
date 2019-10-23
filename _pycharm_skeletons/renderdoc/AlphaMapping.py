# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class AlphaMapping(__enum.IntEnum):
    """
    What to do with the alpha channel from a texture while saving out to a file.
    
    .. data:: Discard
    
      Completely discard the alpha channel and only write RGB t othe file.
    
    .. data:: BlendToColor
    
      Blend to the primary background color using alpha.
    
    .. data:: BlendToCheckerboard
    
      Blend to a checkerboard pattern with the primary and secondary background colors.
    
    .. data:: Preserve
    
      Preserve the alpha channel and save it to the file by itself.
    
      This is only valid for file formats that support alpha channels.
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

    BlendToCheckerboard = 2
    BlendToColor = 1
    Count = 4
    Discard = 0
    First = 0
    Preserve = 3
    _member_map_ = {
        'BlendToCheckerboard': 2,
        'BlendToColor': 1,
        'Count': 4,
        'Discard': 0,
        'First': 0,
        'Preserve': 3,
    }
    _member_names_ = [
        'Discard',
        'BlendToColor',
        'BlendToCheckerboard',
        'Preserve',
        'Count',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


