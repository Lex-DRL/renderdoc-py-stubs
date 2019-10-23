# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class CaptureOptions(SwigPyObject):
    """
    Sets up configuration and options for optional features either at capture time or at API
    initialisation time that the user can enable or disable at will.
    """
    def DecodeFromString(self, p_str): # real signature unknown; restored from __doc__
        """
        DecodeFromString(str)
        
        Decode the options from a string, as returned by :meth:`EncodeAsString`.
        """
        pass

    def EncodeAsString(self): # real signature unknown; restored from __doc__
        """
        EncodeAsString()
        
        Encode the current options to a string suitable for passing around between processes.
        
        :return: The encoded string, suitable for passing to :meth:`DecodeFromString`.
        :rtype: ``str``
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    allowFullscreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Allow the application to enable fullscreen.

Default - enabled

``True`` - The application can enable or disable fullscreen at will.

``False`` - fullscreen is force disabled.

"""

    allowVSync = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Allow the application to enable vsync.

Default - enabled

``True`` - The application can enable or disable vsync at will.

``False`` - vsync is force disabled.

"""

    apiValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Record API debugging events and messages

Default - disabled

``True`` - Enable built-in API debugging features and records the results into
the capture logfile, which is matched up with events on replay.

``False`` - no API debugging is forcibly enabled.

"""

    captureAllCmdLists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
In APIs that allow for the recording of command lists to be replayed later,
RenderDoc may choose to not capture command lists before a frame capture is
triggered, to reduce overheads. This means any command lists recorded once
and replayed many times will not be available and may cause a failure to
capture.

.. note:: This is only true for APIs where multithreading is difficult or
  discouraged. Newer APIs like Vulkan and D3D12 will ignore this option
  and always capture all command lists since the API is heavily oriented
  around it and the overheads have been reduced by API design.

``True`` - All command lists are captured from the start of the application.

``False`` - Command lists are only captured if their recording begins during
the period when a frame capture is in progress.

"""

    captureCallstacks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Capture CPU callstacks for API events

Default - disabled

``True`` - Enables capturing of callstacks.

``False`` - no callstacks are captured.

"""

    captureCallstacksOnlyDraws = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
When capturing CPU callstacks, only capture them from drawcalls.
This option does nothing if :data:`captureCallstacks` is not enabled.

Default - disabled

``True`` - Only captures callstacks for drawcall type API events.

``False`` - Callstacks, if enabled, are captured for every event.

"""

    debugOutputMute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Mute API debugging output when the API validation mode option is enabled.

Default - enabled

``True`` - Mute any API debug messages from being displayed or passed through.

``False`` - API debugging is displayed as normal.

"""

    delayForDebugger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Specify a delay in seconds to wait for a debugger to attach, after
creating or injecting into a process, before continuing to allow it to run.

``0`` indicates no delay, and the process will run immediately after injection.

Default - 0 seconds

"""

    hookIntoChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Hooks any system API calls that create child processes, and injects
RenderDoc into them recursively with the same options.

Default - disabled

``True`` - Hooks into spawned child processes.

``False`` - Child processes are not hooked by RenderDoc.

"""

    refAllResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
By default RenderDoc only includes resources in the final logfile necessary
for that frame, this allows you to override that behaviour.

Default - disabled

``True`` - all live resources at the time of capture are included in the log
and available for inspection.

``False`` - only the resources referenced by the captured frame are included.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    verifyBufferAccess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Verify buffer access. This includes checking the memory returned by a Map() call to
detect any out-of-bounds modification, as well as initialising buffers with undefined contents to
a marker value to catch use of uninitialised memory.

.. note::

  This option is only valid for OpenGL and D3D11. Explicit APIs such as D3D12 and Vulkan do not
  do the same kind of interception & checking and undefined contents are really undefined.

Default - disabled

``True`` - Verify buffer access.

``False`` - No verification is performed, and overwriting bounds may cause crashes or corruption in
RenderDoc.

"""


    __dict__ = None # (!) real value is ''


