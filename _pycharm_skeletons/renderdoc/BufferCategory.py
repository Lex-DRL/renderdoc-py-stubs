# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class BufferCategory(__enum.IntFlag):
    """
    A set of flags describing how this buffer may be used
    
    .. data:: NoFlags
    
      The buffer will not be used for any of the uses below.
    
    .. data:: Vertex
    
      The buffer will be used for sourcing vertex input data.
    
    .. data:: Index
    
      The buffer will be used for sourcing primitive index data.
    
    .. data:: Constants
    
      The buffer will be used for sourcing shader constant data.
    
    .. data:: ReadWrite
    
      The buffer will be used for read and write access from shaders.
    
    .. data:: Indirect
    
      The buffer will be used to provide indirect parameters for launching GPU-based drawcalls.
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

    Constants = 4
    Index = 2
    Indirect = 16
    NoFlags = 0
    ReadWrite = 8
    Vertex = 1
    _member_map_ = {
        'Constants': 4,
        'Index': 2,
        'Indirect': 16,
        'NoFlags': 0,
        'ReadWrite': 8,
        'Vertex': 1,
    }
    _member_names_ = [
        'NoFlags',
        'Vertex',
        'Index',
        'Constants',
        'ReadWrite',
        'Indirect',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
    }


