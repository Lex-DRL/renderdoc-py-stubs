# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class AndroidFlags(__enum.IntFlag):
    """
    A set of flags giving details of the current status of Android tracability.
    
    .. data:: NoFlags
    
      There are no problems with the Android application setup.
    
    .. data:: Debuggable
    
      The application is debuggable.
    
    .. data:: RootAccess
    
       The device being targeted has root access.
    
    .. data:: MissingTools
    
       When patching, some necessary tools were not found.
    
    .. data:: ManifestPatchFailure
    
       When patching, modifying the manifest file to include the debuggable flag failed.
    
    .. data:: RepackagingAPKFailure
    
       When patching, repackaging, signing and installing the new package failed.
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

    Debuggable = 1
    ManifestPatchFailure = 8192
    MissingTools = 4096
    NoFlags = 0
    RepackagingAPKFailure = 16384
    RootAccess = 2
    _member_map_ = {
        'Debuggable': 1,
        'ManifestPatchFailure': 8192,
        'MissingTools': 4096,
        'NoFlags': 0,
        'RepackagingAPKFailure': 16384,
        'RootAccess': 2,
    }
    _member_names_ = [
        'NoFlags',
        'Debuggable',
        'RootAccess',
        'MissingTools',
        'ManifestPatchFailure',
        'RepackagingAPKFailure',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4096: 4096,
        8192: 8192,
        16384: 16384,
    }


