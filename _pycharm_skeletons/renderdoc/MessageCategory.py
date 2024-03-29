# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class MessageCategory(__enum.IntEnum):
    """
    The type of issue that a debug message is about.
    
    .. data:: Application_Defined
    
      This message was generated by the application.
    
    .. data:: Miscellaneous
    
      This message doesn't fall into any other pre-defined category.
    
    .. data:: Initialization
    
      This message is about initialisation or creation of objects.
    
    .. data:: Cleanup
    
      This message is about cleanup, destruction or shutdown of objects.
    
    .. data:: Compilation
    
      This message is about compilation of shaders.
    
    .. data:: State_Creation
    
      This message is about creating unified state objects.
    
    .. data:: State_Setting
    
      This message is about changing current pipeline state.
    
    .. data:: State_Getting
    
      This message is about fetching or retrieving current pipeline state.
    
    .. data:: Resource_Manipulation
    
      This message is about updating or changing a resource's properties or contents.
    
    .. data:: Execution
    
      This message is about performing work.
    
    .. data:: Shaders
    
      This message is about the use, syntax, binding or linkage of shaders.
    
    .. data:: Deprecated
    
      This message is about the use of deprecated functionality.
    
    .. data:: Undefined
    
      This message is about the use of undefined behaviour.
    
    .. data:: Portability
    
      This message is about behaviour that could be or is not portable between different environments.
    
    .. data:: Performance
    
      This message is about performance problems or pitfalls.
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

    Application_Defined = 0
    Cleanup = 3
    Compilation = 4
    Deprecated = 11
    Execution = 9
    Initialization = 2
    Miscellaneous = 1
    Performance = 14
    Portability = 13
    Resource_Manipulation = 8
    Shaders = 10
    State_Creation = 5
    State_Getting = 7
    State_Setting = 6
    Undefined = 12
    _member_map_ = {
        'Application_Defined': 0,
        'Cleanup': 3,
        'Compilation': 4,
        'Deprecated': 11,
        'Execution': 9,
        'Initialization': 2,
        'Miscellaneous': 1,
        'Performance': 14,
        'Portability': 13,
        'Resource_Manipulation': 8,
        'Shaders': 10,
        'State_Creation': 5,
        'State_Getting': 7,
        'State_Setting': 6,
        'Undefined': 12,
    }
    _member_names_ = [
        'Application_Defined',
        'Miscellaneous',
        'Initialization',
        'Cleanup',
        'Compilation',
        'State_Creation',
        'State_Setting',
        'State_Getting',
        'Resource_Manipulation',
        'Execution',
        'Shaders',
        'Deprecated',
        'Undefined',
        'Portability',
        'Performance',
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
        11: 11,
        12: 12,
        13: 13,
        14: 14,
    }


