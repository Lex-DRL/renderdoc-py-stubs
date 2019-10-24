# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class DeviceProtocolController(SwigPyObject):
    """ An interface for enumerating and controlling remote devices. """
    def GetDevices(self): # real signature unknown; restored from __doc__
        """
        GetDevices()
        
        Returns a list of devices currently available through the given protocol.
        
        Until a device is enumerated through this function it may not be available for connection through
        other methods such as target control or remote server access, even if the device is physically
        connected, due to initialisation happening only when enumerated.
        
        The returned string is the hostname of the device, which can be connected via
        ``protocol://hostname`` with interfaces that take a hostname.
        
        :return: A list of the devices currently available.
        :rtype: ``list`` of ``str``
        """
        pass

    def GetFriendlyName(self, URL): # real signature unknown; restored from __doc__
        """
        GetFriendlyName(URL)
        
        Retrieves the user friendly name of the given device. This may be easier for a user to
        correlate to a device than the hostname which may be only a programmatic identifier.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: A string identifying the device.
        :rtype: ``str``
        """
        pass

    def GetProtocolName(self): # real signature unknown; restored from __doc__
        """
        GetProtocolName()
        
        Retrieves the name of this protocol as passed to :func:`GetDeviceProtocolController`.
        
        :return: A string identifying the protocol.
        :rtype: ``str``
        """
        pass

    def IsSupported(self, URL): # real signature unknown; restored from __doc__
        """
        IsSupported(URL)
        
        Query if the device supports RenderDoc capture and replay.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: ``True`` if any the device is supported, ``False`` otherwise.
        :rtype: ``bool``
        """
        pass

    def StartRemoteServer(self, URL): # real signature unknown; restored from __doc__
        """
        StartRemoteServer(URL)
        
        Start the remote server running on the given device.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: The status of starting the server, whether success or failure.
        :rtype: ReplayStatus
        """
        pass

    def SupportsMultiplePrograms(self, URL): # real signature unknown; restored from __doc__
        """
        SupportsMultiplePrograms(URL)
        
        Query if the device supports multiple programs running and being captured. If not, the
        user can be prompted to close an existing program before a new one is launched.
        
        :param str URL: The URL of the device in the form ``protocol://host``, with protocol as returned by
          :func:`GetProtocolName` and host as returned by :func:`GetDevices`.
        :return: ``True`` if the device supports multiple programs, ``False`` otherwise.
        :rtype: ``bool``
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


