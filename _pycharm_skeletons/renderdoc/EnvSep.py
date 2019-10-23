# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class EnvSep(__enum.IntEnum):
    """
    The separator to use if needed when modifying an environment variable.
    
    .. data:: Platform
    
      Use the character appropriate for separating items on the platform.
    
      On Windows this means the semi-colon ``;`` character will be used, on posix systems the colon
      ``:`` character will be used.
    
    .. data:: SemiColon
    
      Use a semi-colon ``;`` character.
    
    .. data:: Colon
    
      Use a colon ``:`` character.
    
    .. data:: NoSep
    
      No separator will be used.
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

    Colon = 2
    NoSep = 3
    Platform = 0
    SemiColon = 1
    _member_map_ = {
        'Colon': 2,
        'NoSep': 3,
        'Platform': 0,
        'SemiColon': 1,
    }
    _member_names_ = [
        'Platform',
        'SemiColon',
        'Colon',
        'NoSep',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


