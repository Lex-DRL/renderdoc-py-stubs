# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class VulkanLayerFlags(__enum.IntFlag):
    """
    A set of flags giving details of the current status of vulkan layer registration.
    
    .. data:: NoFlags
    
      There are no problems with the vulkan layer registration.
    
    .. data:: OtherInstallsRegistered
    
      Other conflicting installs of the same layer in other locations are registered.
    
    .. data:: ThisInstallRegistered
    
      This current install of the layer is registered.
    
    .. data:: NeedElevation
    
      Fixing any issues will require elevation to system administrator privileges.
    
    .. data:: CouldElevate
    
      Fixing issues could be done purely as a user, but can optionally be done at system level with
      system administrator privileges.
    
    .. data:: RegisterAll
    
      All listed locations for the current layer must be registered for correct functioning.
    
      If this flag is not set, then the listed locations are an 'or' list of alternatives.
    
    .. data:: UpdateAllowed
    
      If the current registrations can be updated or re-pointed to fix the issues.
    
    .. data:: Unfixable
    
      The current situation is not fixable automatically and requires user intervention/disambiguation.
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

    CouldElevate = 8
    NeedElevation = 4
    NoFlags = 0
    OtherInstallsRegistered = 1
    RegisterAll = 16
    ThisInstallRegistered = 2
    Unfixable = 64
    UpdateAllowed = 32
    _member_map_ = {
        'CouldElevate': 8,
        'NeedElevation': 4,
        'NoFlags': 0,
        'OtherInstallsRegistered': 1,
        'RegisterAll': 16,
        'ThisInstallRegistered': 2,
        'Unfixable': 64,
        'UpdateAllowed': 32,
    }
    _member_names_ = [
        'NoFlags',
        'OtherInstallsRegistered',
        'ThisInstallRegistered',
        'NeedElevation',
        'CouldElevate',
        'RegisterAll',
        'UpdateAllowed',
        'Unfixable',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
        32: 32,
        64: 64,
    }


