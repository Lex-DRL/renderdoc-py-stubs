# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class PathProperty(__enum.IntFlag):
    """
    A set of flags describing the properties of a path on a remote filesystem.
    
    .. data:: NoFlags
    
      No special file properties.
    
    .. data:: Directory
    
      This file is a directory or folder.
    
    .. data:: Hidden
    
      This file is considered hidden by the filesystem.
    
    .. data:: Executable
    
      This file has been identified as an executable program or script.
    
    .. data:: ErrorUnknown
    
      A special flag indicating that a query for this file failed, but for unknown reasons.
    
    .. data:: ErrorAccessDenied
    
      A special flag indicating that a query for this file failed because access to the path was
      denied.
    
    .. data:: ErrorInvalidPath
    
      A special flag indicating that a query for this file failed because the path was invalid.
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

    Directory = 1
    ErrorAccessDenied = 16384
    ErrorInvalidPath = 32768
    ErrorUnknown = 8192
    Executable = 4
    Hidden = 2
    NoFlags = 0
    _member_map_ = {
        'Directory': 1,
        'ErrorAccessDenied': 16384,
        'ErrorInvalidPath': 32768,
        'ErrorUnknown': 8192,
        'Executable': 4,
        'Hidden': 2,
        'NoFlags': 0,
    }
    _member_names_ = [
        'NoFlags',
        'Directory',
        'Hidden',
        'Executable',
        'ErrorUnknown',
        'ErrorAccessDenied',
        'ErrorInvalidPath',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8192: 8192,
        16384: 16384,
        32768: 32768,
    }


