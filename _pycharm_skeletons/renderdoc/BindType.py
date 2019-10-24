# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class BindType(__enum.IntEnum):
    """
    The type of a shader resource bind.
    
    .. data:: Unknown
    
      An unknown type of binding.
    
    .. data:: ConstantBuffer
    
      A constant or uniform buffer.
    
    .. data:: Sampler
    
      A separate sampler object.
    
    .. data:: ImageSampler
    
      A combined image and sampler object.
    
    .. data:: ReadOnlyImage
    
      An image that can only be sampled from.
    
    .. data:: ReadWriteImage
    
      An image that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyTBuffer
    
      A texture buffer that can only be read from.
    
    .. data:: ReadWriteTBuffer
    
      A texture buffer that can be read from and written to arbitrarily.
    
    .. data:: ReadOnlyBuffer
    
      A buffer that can only be read from, distinct from :data:`ConstantBuffer`.
    
    .. data:: ReadWriteBuffer
    
      A buffer that can be read from and written to arbitrarily.
    
    .. data:: InputAttachment
    
      An input attachment for reading from the target currently being written.
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

    ConstantBuffer = 1
    ImageSampler = 3
    InputAttachment = 10
    ReadOnlyBuffer = 8
    ReadOnlyImage = 4
    ReadOnlyTBuffer = 6
    ReadWriteBuffer = 9
    ReadWriteImage = 5
    ReadWriteTBuffer = 7
    Sampler = 2
    Unknown = 0
    _member_map_ = {
        'ConstantBuffer': 1,
        'ImageSampler': 3,
        'InputAttachment': 10,
        'ReadOnlyBuffer': 8,
        'ReadOnlyImage': 4,
        'ReadOnlyTBuffer': 6,
        'ReadWriteBuffer': 9,
        'ReadWriteImage': 5,
        'ReadWriteTBuffer': 7,
        'Sampler': 2,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'ConstantBuffer',
        'Sampler',
        'ImageSampler',
        'ReadOnlyImage',
        'ReadWriteImage',
        'ReadOnlyTBuffer',
        'ReadWriteTBuffer',
        'ReadOnlyBuffer',
        'ReadWriteBuffer',
        'InputAttachment',
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
        9: 9,
        10: 10,
    }


