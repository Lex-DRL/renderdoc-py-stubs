# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class MessageSource(__enum.IntEnum):
    """
    Where a debug message was reported from
    
    .. data:: API
    
      This message comes from the API's debugging or validation layers.
    
    .. data:: RedundantAPIUse
    
      This message comes from detecting redundant API calls - calls with no side-effect or purpose, e.g.
      setting state that is already set.
    
    .. data:: IncorrectAPIUse
    
      This message comes from detecting incorrect use of the API.
    
    .. data:: GeneralPerformance
    
      This message comes from detecting general performance problems that are not hardware or platform
      specific.
    
    .. data:: GCNPerformance
    
      This message comes from detecting patterns that will cause performance problems on GCN-based
      hardware.
    
    .. data:: RuntimeWarning
    
      This message comes not from inspecting the log but something detected at runtime while in use,
      for example exceptions generated during shader debugging.
    
    .. data:: UnsupportedConfiguration
    
      This message comes from replaying a capture in an environment with insufficient capability to
      accurately reproduce the API work. Either this means the replay will be wrong, or it may be that
      depending on the exact API work some inaccuracies might happen.
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

    API = 0
    GCNPerformance = 4
    GeneralPerformance = 3
    IncorrectAPIUse = 2
    RedundantAPIUse = 1
    RuntimeWarning = 5
    UnsupportedConfiguration = 6
    _member_map_ = {
        'API': 0,
        'GCNPerformance': 4,
        'GeneralPerformance': 3,
        'IncorrectAPIUse': 2,
        'RedundantAPIUse': 1,
        'RuntimeWarning': 5,
        'UnsupportedConfiguration': 6,
    }
    _member_names_ = [
        'API',
        'RedundantAPIUse',
        'IncorrectAPIUse',
        'GeneralPerformance',
        'GCNPerformance',
        'RuntimeWarning',
        'UnsupportedConfiguration',
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
    }


