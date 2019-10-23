# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SectionFlags(__enum.IntFlag):
    """
    A set of flags describing the properties of a section in a renderdoc capture.
    
    .. data:: NoFlags
    
      No special section properties.
    
    .. data:: ASCIIStored
    
      This section was stored as pure ASCII. This can be useful since it is possible to generate
      an ASCII section in a text editor by hand or with any simple printf style script, and then
      concatenate it to a .rdc and have a valid section.
    
    .. data:: LZ4Compressed
    
      This section is compressed with LZ4 on disk.
    
    .. data:: ZstdCompressed
    
      This section is compressed with Zstd on disk.
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

    ASCIIStored = 1
    LZ4Compressed = 2
    NoFlags = 0
    ZstdCompressed = 4
    _member_map_ = {
        'ASCIIStored': 1,
        'LZ4Compressed': 2,
        'NoFlags': 0,
        'ZstdCompressed': 4,
    }
    _member_names_ = [
        'NoFlags',
        'ASCIIStored',
        'LZ4Compressed',
        'ZstdCompressed',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
    }


