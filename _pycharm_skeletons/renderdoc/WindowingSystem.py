# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class WindowingSystem(__enum.IntEnum):
    """
    Specifies a windowing system to use for creating an output window.
    
    .. data:: Unknown
    
      Unknown window type, no windowing data is passed and no native window is described.
    
    .. data:: Headless
    
      The windowing data doesn't describe a real window but a virtual area, allowing all normal output
      rendering to happen off-screen.
      See :func:`CreateHeadlessWindowingData`.
    
    .. data:: Win32
    
      The windowing data refers to a Win32 window. See :func:`CreateWin32WindowingData`.
    
    .. data:: Xlib
    
      The windowing data refers to an Xlib window. See :func:`CreateXLibWindowingData`.
    
    .. data:: XCB
    
      The windowing data refers to an XCB window. See :func:`CreateXCBWindowingData`.
    
    .. data:: Wayland
    
      The windowing data refers to an Wayland window. See :func:`CreateWaylandWindowingData`.
    
    .. data:: Android
    
      The windowing data refers to an Android window. See :func:`CreateAndroidWindowingData`.
    
    .. data:: MacOS
    
      The windowing data refers to a MacOS / OS X NSView & CALayer that is Metal/GL compatible.
      See :func:`CreateMacOSWindowingData`.
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

    Android = 5
    GGP = 7
    Headless = 1
    MacOS = 6
    Unknown = 0
    Wayland = 8
    Win32 = 2
    XCB = 4
    Xlib = 3
    _member_map_ = {
        'Android': 5,
        'GGP': 7,
        'Headless': 1,
        'MacOS': 6,
        'Unknown': 0,
        'Wayland': 8,
        'Win32': 2,
        'XCB': 4,
        'Xlib': 3,
    }
    _member_names_ = [
        'Unknown',
        'Headless',
        'Win32',
        'Xlib',
        'XCB',
        'Android',
        'MacOS',
        'GGP',
        'Wayland',
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
    }


