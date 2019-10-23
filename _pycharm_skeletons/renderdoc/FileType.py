# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class FileType(__enum.IntEnum):
    """
    The format of an image file
    
    .. data:: DDS
    
      A DDS file
    
    .. data:: PNG
    
      A PNG file
    
    .. data:: JPG
    
      A JPG file
    
    .. data:: BMP
    
      A BMP file
    
    .. data:: TGA
    
      A TGA file
    
    .. data:: HDR
    
      An HDR file
    
    .. data:: EXR
    
      An EXR file
    
    .. data:: RAW
    
      Raw data, just the bytes of the image tightly packed with no metadata or compression/encoding
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

    BMP = 3
    Count = 8
    DDS = 0
    EXR = 6
    First = 0
    HDR = 5
    JPG = 2
    PNG = 1
    Raw = 7
    TGA = 4
    _member_map_ = {
        'BMP': 3,
        'Count': 8,
        'DDS': 0,
        'EXR': 6,
        'First': 0,
        'HDR': 5,
        'JPG': 2,
        'PNG': 1,
        'Raw': 7,
        'TGA': 4,
    }
    _member_names_ = [
        'DDS',
        'PNG',
        'JPG',
        'BMP',
        'TGA',
        'HDR',
        'EXR',
        'Raw',
        'Count',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
    }


