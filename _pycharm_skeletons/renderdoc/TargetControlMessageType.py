# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class TargetControlMessageType(__enum.IntEnum):
    """
    The type of message received from or sent to an application target control connection.
    
    .. data:: Unknown
    
      No message or an unknown message type.
    
    .. data:: Disconnected
    
      The other end of the connection disconnected.
    
    .. data:: Busy
    
      The other end of the connection was busy.
    
    .. data:: Noop
    
      Nothing happened, the connection is being kept alive.
    
    .. data:: NewCapture
    
      A new capture was made.
    
    .. data:: CaptureCopied
    
      A capture was successfully copied across the connection.
    
    .. data:: RegisterAPI
    
      The target has initialised a graphics API.
    
    .. data:: NewChild
    
      The target has created a child process.
    
    .. data:: CaptureProgress
    
      Progress update on an on-going frame capture.
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

    Busy = 2
    CapturableWindowCount = 9
    CaptureCopied = 5
    CaptureProgress = 8
    Disconnected = 1
    NewCapture = 4
    NewChild = 7
    Noop = 3
    RegisterAPI = 6
    Unknown = 0
    _member_map_ = {
        'Busy': 2,
        'CapturableWindowCount': 9,
        'CaptureCopied': 5,
        'CaptureProgress': 8,
        'Disconnected': 1,
        'NewCapture': 4,
        'NewChild': 7,
        'Noop': 3,
        'RegisterAPI': 6,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'Disconnected',
        'Busy',
        'Noop',
        'NewCapture',
        'CaptureCopied',
        'RegisterAPI',
        'NewChild',
        'CaptureProgress',
        'CapturableWindowCount',
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
    }


