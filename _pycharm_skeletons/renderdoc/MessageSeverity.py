# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class MessageSeverity(__enum.IntEnum):
    """
    How serious a debug message is
    
    .. data:: High
    
      This message is very serious, indicating a guaranteed problem or major flaw.
    
    .. data:: Medium
    
      This message is somewhat serious, indicating a problem that should be addressed or investigated.
    
    .. data:: Low
    
      This message is not very serious. This indicates something that might indicate a problem.
    
    .. data:: Info
    
      This message is not about a problem but is purely informational.
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

    High = 0
    Info = 3
    Low = 2
    Medium = 1
    _member_map_ = {
        'High': 0,
        'Info': 3,
        'Low': 2,
        'Medium': 1,
    }
    _member_names_ = [
        'High',
        'Medium',
        'Low',
        'Info',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


