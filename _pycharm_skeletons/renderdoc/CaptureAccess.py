# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class CaptureAccess(SwigPyObject):
    """
    An interface for accessing a capture, possibly over a network connection. This is a
    subset of the functionality provided in :class:`CaptureFile` which only supports import/export
    and construction of files.
    """
    def DriverName(self): # real signature unknown; restored from __doc__
        """
        DriverName()
        
        Retrieves the name of the driver that was used to create this capture.
        
        :return: A simple string identifying the driver used to make the capture.
        :rtype: ``str``
        """
        pass

    def FindSectionByName(self, name): # real signature unknown; restored from __doc__
        """
        FindSectionByName(name)
        
        Locate the index of a section by its name. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param str name: The name of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: ``int``.
        """
        pass

    def FindSectionByType(self, type): # real signature unknown; restored from __doc__
        """
        FindSectionByType(type)
        
        Locate the index of a section by its type. Returns ``-1`` if the section is not found.
        
        This index should not be cached, as writing sections could re-order the indices.
        
        :param SectionType type: The type of the section to search for.
        :return: The index of the section, or ``-1`` if not found.
        :rtype: ``int``.
        """
        pass

    def GetAvailableGPUs(self): # real signature unknown; restored from __doc__
        """
        GetAvailableGPUs()
        
        Returns the list of available GPUs, that can be used in combination with
        :class:`ReplayOptions` to force replay on a particular GPU.
        
        :return: The list of GPUs available.
        :rtype: ``list`` of :class:`GPUDevice`
        """
        pass

    def GetResolve(self, callstack): # real signature unknown; restored from __doc__
        """
        GetResolve(callstack)
        
        Retrieve the details of each stackframe in the provided callstack.
        
        Must only be called after :meth:`InitResolver` has returned ``True``.
        
        :param list callstack: The integer addresses in the original callstack.
        :return: The list of resolved callstack entries as strings.
        :rtype: ``list`` of ``str``
        """
        pass

    def GetSectionContents(self, index): # real signature unknown; restored from __doc__
        """
        GetSectionContents(index)
        
        Get the raw byte contents of the specified section.
        
        :param int index: The index of the section.
        :return: The raw contents of the section, if the index is valid.
        :rtype: ``bytes``.
        """
        pass

    def GetSectionCount(self): # real signature unknown; restored from __doc__
        """
        GetSectionCount()
        
        Retrieve the total number of available sections.
        
        :return: The number of sections in the capture
        :rtype: ``int``.
        """
        pass

    def GetSectionProperties(self, index): # real signature unknown; restored from __doc__
        """
        GetSectionProperties(index)
        
        Get the describing properties of the specified section.
        
        :param int index: The index of the section.
        :return: The properties of the section, if the index is valid.
        :rtype: SectionProperties
        """
        pass

    def HasCallstacks(self): # real signature unknown; restored from __doc__
        """
        HasCallstacks()
        
        Query if callstacks are available.
        
        :return: ``True`` if any callstacks are available, ``False`` otherwise.
        :rtype: ``bool``
        """
        pass

    def InitResolver(self, progress): # real signature unknown; restored from __doc__
        """
        InitResolver(progress)
        
        Begin initialising a callstack resolver, looking up symbol files and caching as
        necessary.
        
        This function blocks while trying to initialise callstack resolving, so it should be called on a
        separate thread.
        
        :param ProgressCallback progress: A callback that will be repeatedly called with an updated progress
          value for the resolver process. Can be ``None`` if no progress is desired.
        :return: ``True`` if the resolver successfully initialised, ``False`` if something went wrong.
        :rtype: ``bool``
        """
        pass

    def WriteSection(self, props, contents): # real signature unknown; restored from __doc__
        """
        WriteSection(props, contents)
        
        Writes a new section with specified properties and contents. If an existing section
        already has the same type or name, it will be overwritten (two sections cannot share the same type
        or name).
        
        :param SectionProperties props: The properties of the section to be written.
        :param bytes contents: The raw contents of the section.
        :return: ``True`` if the section was written successfully, ``False`` otherwise.
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


