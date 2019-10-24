# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ReplaySupport(__enum.IntEnum):
    """
    How supported a given API is on a particular replay instance.
    
    .. data:: Unsupported
    
      The API is not supported.
    
    .. data:: Supported
    
      The API is fully supported.
    
    .. data:: SuggestRemote
    
      The API is supported locally but the capture indicates it was made on a different type of machine
      so remote replay might be desired.
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

    SuggestRemote = 2
    Supported = 1
    Unsupported = 0
    _member_map_ = {
        'SuggestRemote': 2,
        'Supported': 1,
        'Unsupported': 0,
    }
    _member_names_ = [
        'Unsupported',
        'Supported',
        'SuggestRemote',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


