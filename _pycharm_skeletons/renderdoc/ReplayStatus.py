# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ReplayStatus(__enum.IntEnum):
    """
    The status of a high-level replay operation such as opening a capture or connecting to
    a remote server.
    
    .. data:: Succeeded
    
      The operation succeeded.
    
    .. data:: UnknownError
    
      An unknown error occurred.
    
    .. data:: InternalError
    
      An internal error occurred indicating a bug or unexpected condition.
    
    .. data:: FileNotFound
    
      The specified file was not found.
    
    .. data:: InjectionFailed
    
      Injection or hooking into the target process failed.
    
    .. data:: IncompatibleProcess
    
      An incompatible process was found, e.g. a 32-bit process with 32-bit support not available.
    
    .. data:: NetworkIOFailed
    
      A network I/O operation failed.
    
    .. data:: NetworkRemoteBusy
    
      The remote side of the network connection was busy.
    
    .. data:: NetworkVersionMismatch
    
      The other side of the network connection was not at a compatible version.
    
    .. data:: FileIOFailed
    
      A filesystem I/O operation failed.
    
    .. data:: FileIncompatibleVersion
    
      The capture file had an incompatible version.
    
    .. data:: FileCorrupted
    
      The capture file is corrupted or otherwise unrecognisable.
    
    .. data:: ImageUnsupported
    
      The image file is recognised but the format is unsupported.
    
    .. data:: APIUnsupported
    
      The API used in the capture is not supported.
    
    .. data:: APIInitFailed
    
      The API used in the capture failed to initialise.
    
    .. data:: APIIncompatibleVersion
    
      The API data in the capture had an incompatible version.
    
    .. data:: APIHardwareUnsupported
    
      The API is not supported on the currently available hardware.
    
    .. data:: APIDataCorrupted
    
      While loading the capture for replay, the driver encountered corrupted or invalid serialised data.
    
    .. data:: APIReplayFailed
    
      The API failed to replay the capture, with some runtime error that couldn't be determined until
      the replay began.
    
    .. data:: AndroidGrantPermissionsFailed
    
      Failed to grant runtime permissions when installing Android remote server.
    
    .. data:: AndroidABINotFound
    
      Couldn't determine supported ABIs when installing Android remote server.
    
    .. data:: AndroidAPKFolderNotFound
    
      Couldn't find the folder which contains the Android remote server APK.
    
    .. data:: AndroidAPKInstallFailed
    
      Failed to install Android remote server for unknown reasons.
    
    .. data:: AndroidAPKVerifyFailed
    
      Failed to install Android remote server.
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

    AndroidABINotFound = 21
    AndroidAPKFolderNotFound = 22
    AndroidAPKInstallFailed = 23
    AndroidAPKVerifyFailed = 24
    AndroidGrantPermissionsFailed = 20
    APIDataCorrupted = 17
    APIHardwareUnsupported = 16
    APIIncompatibleVersion = 15
    APIInitFailed = 14
    APIReplayFailed = 18
    APIUnsupported = 13
    FileCorrupted = 11
    FileIncompatibleVersion = 10
    FileIOFailed = 9
    FileNotFound = 3
    ImageUnsupported = 12
    IncompatibleProcess = 5
    InjectionFailed = 4
    InternalError = 2
    JDWPFailure = 19
    NetworkIOFailed = 6
    NetworkRemoteBusy = 7
    NetworkVersionMismatch = 8
    Succeeded = 0
    UnknownError = 1
    _member_map_ = {
        'APIDataCorrupted': 17,
        'APIHardwareUnsupported': 16,
        'APIIncompatibleVersion': 15,
        'APIInitFailed': 14,
        'APIReplayFailed': 18,
        'APIUnsupported': 13,
        'AndroidABINotFound': 21,
        'AndroidAPKFolderNotFound': 22,
        'AndroidAPKInstallFailed': 23,
        'AndroidAPKVerifyFailed': 24,
        'AndroidGrantPermissionsFailed': 20,
        'FileCorrupted': 11,
        'FileIOFailed': 9,
        'FileIncompatibleVersion': 10,
        'FileNotFound': 3,
        'ImageUnsupported': 12,
        'IncompatibleProcess': 5,
        'InjectionFailed': 4,
        'InternalError': 2,
        'JDWPFailure': 19,
        'NetworkIOFailed': 6,
        'NetworkRemoteBusy': 7,
        'NetworkVersionMismatch': 8,
        'Succeeded': 0,
        'UnknownError': 1,
    }
    _member_names_ = [
        'Succeeded',
        'UnknownError',
        'InternalError',
        'FileNotFound',
        'InjectionFailed',
        'IncompatibleProcess',
        'NetworkIOFailed',
        'NetworkRemoteBusy',
        'NetworkVersionMismatch',
        'FileIOFailed',
        'FileIncompatibleVersion',
        'FileCorrupted',
        'ImageUnsupported',
        'APIUnsupported',
        'APIInitFailed',
        'APIIncompatibleVersion',
        'APIHardwareUnsupported',
        'APIDataCorrupted',
        'APIReplayFailed',
        'JDWPFailure',
        'AndroidGrantPermissionsFailed',
        'AndroidABINotFound',
        'AndroidAPKFolderNotFound',
        'AndroidAPKInstallFailed',
        'AndroidAPKVerifyFailed',
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
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
    }


