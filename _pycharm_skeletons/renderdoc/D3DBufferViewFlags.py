# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class D3DBufferViewFlags(__enum.IntFlag):
    """
    A set of flags for D3D buffer view properties.
    
    .. data:: NoFlags
    
      The buffer will not be used for any of the uses below.
    
    .. data:: Raw
    
      The buffer is used as a raw (byte-addressed) buffer.
    
    .. data:: Append
    
      The buffer is used as a append/consume view.
    
    .. data:: Counter
    
      The buffer is used with a structured buffer with associated hidden counter.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initital start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    Append = 2
    Counter = 4
    NoFlags = 0
    Raw = 1
    _member_map_ = {
        'Append': 2,
        'Counter': 4,
        'NoFlags': 0,
        'Raw': 1,
    }
    _member_names_ = [
        'NoFlags',
        'Raw',
        'Append',
        'Counter',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
    }


