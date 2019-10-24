# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class TargetControl(SwigPyObject):
    """
    A connection to a running application with RenderDoc injected, which allows limited
    control over the capture process as well as querying the current status.
    """
    def Connected(self): # real signature unknown; restored from __doc__
        """
        Connected()
        
        Determines if the connection is still alive.
        
        :return: ``True`` if the connection still appears to be working, ``False`` if it has been closed.
        :rtype: ``bool``
        """
        pass

    def CopyCapture(self, captureId, localpath): # real signature unknown; restored from __doc__
        """
        CopyCapture(captureId, localpath)
        
        Begin copying a given capture stored on a remote machine to the local machine over the
        target control connection.
        
        :param int captureId: The identifier of the remote capture.
        :param str localpath: The absolute path on the local system where the file should be saved.
        """
        pass

    def CycleActiveWindow(self): # real signature unknown; restored from __doc__
        """
        CycleActiveWindow()
        
        Cycle the currently active window if there are more windows to capture.
        """
        pass

    def DeleteCapture(self, captureId): # real signature unknown; restored from __doc__
        """
        DeleteCapture(captureId)
        
        Delete a capture from the remote machine.
        
        :param int captureId: The identifier of the remote capture.
        """
        pass

    def GetAPI(self): # real signature unknown; restored from __doc__
        """
        GetAPI()
        
        Retrieves the API currently in use by the target.
        
        :return: The API name, or empty if no API is initialised yet.
        :rtype: ``str``
        """
        pass

    def GetBusyClient(self): # real signature unknown; restored from __doc__
        """
        GetBusyClient()
        
        If a busy message was received, determine the client keeping the target busy.
        
        :return: The name of the client currently connected to the target.
        :rtype: ``str``
        """
        pass

    def GetPID(self): # real signature unknown; restored from __doc__
        """
        GetPID()
        
        Retrieves the Process ID (PID) of the target on its local system.
        
        :return: The Process ID, or 0 if that's not applicable on the target platform.
        :rtype: ``int``
        """
        pass

    def GetTarget(self): # real signature unknown; restored from __doc__
        """
        GetTarget()
        
        Retrieves the target's name or identifier - typically the name of the executable.
        
        :return: The target name.
        :rtype: ``str``
        """
        pass

    def QueueCapture(self, frameNumber, numFrames): # real signature unknown; restored from __doc__
        """
        QueueCapture(frameNumber, numFrames)
        
        Queue up a capture to happen on a particular frame number. When this frame is about to
        begin a capture is begun, and it ends when this frame number ends.
        
        .. note:: Frame 0 is defined as starting when the device is created, up to the first swapchain
          present defined frame boundary.
        
        :param int frameNumber: The number of the frame to capture on.
        :param int numFrames: How many frames to capture. These will be captured sequentially and
          independently to separate files.
        """
        pass

    def ReceiveMessage(self, progress): # real signature unknown; restored from __doc__
        """
        ReceiveMessage(progress)
        
        Query to see if a message has been received from the remote system.
        
        The details of the types of messages that can be received are listed under
        :class:`TargetControlMessage`.
        
        .. note:: If no message has been received, this function will pump the connection. You are expected
          to continually call this function and process any messages to kee pthe connection alive.
        
          This function will block but only to a limited degree. If no message is waiting after a small time
          it will return with a No-op message to allow further processing.
        
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value when a long blocking message is coming through, e.g. a capture copy. Can be ``None`` if no
          progress is desired.
        :return: The message that was received.
        :rtype: TargetControlMessage
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Closes the connection without affecting the running application.
        """
        pass

    def TriggerCapture(self, numFrames): # real signature unknown; restored from __doc__
        """
        TriggerCapture(numFrames)
        
        Trigger a capture on the target, with the same semantics as if the capture key had
        been pressed - from the next presentation call after this message is processed on the target to the
        next after that.
        
        :param int numFrames: How many frames to capture. These will be captured sequentially and
          independently to separate files.
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


