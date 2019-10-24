# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class LogType(__enum.IntEnum):
    """
    The type of a log message
    
    .. data:: Debug
    
      The log message is a verbose debug-only message that can be discarded in release builds.
    
    .. data:: Comment
    
      The log message is informational.
    
    .. data:: Warning
    
      The log message describes a warning that could indicate a problem or be useful in diagnostics.
    
    .. data:: Error
    
      The log message indicates an error was encountered.
    
    .. data:: Fatal
    
      The log message indicates a fatal error occurred which is impossible to recover from.
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

    Comment = 1
    Count = 5
    Debug = 0
    Error = 3
    Fatal = 4
    First = 0
    Warning = 2
    _member_map_ = {
        'Comment': 1,
        'Count': 5,
        'Debug': 0,
        'Error': 3,
        'Fatal': 4,
        'First': 0,
        'Warning': 2,
    }
    _member_names_ = [
        'Debug',
        'Comment',
        'Warning',
        'Error',
        'Fatal',
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
    }


