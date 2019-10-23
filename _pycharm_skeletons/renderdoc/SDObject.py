# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class SDObject(SwigPyObject):
    """ Defines a single structured object. """
    def AddChild(self, child): # real signature unknown; restored from __doc__
        """
        AddChild(child)
        
        Add a new child object by duplicating it.
        """
        pass

    def AsBool(self): # real signature unknown; restored from __doc__
        """
        AsBool()
        
        Interprets the object as a ``bool`` and returns its value.
        Invalid if the object is not actually a ``bool``.
        """
        pass

    def AsFloat(self): # real signature unknown; restored from __doc__
        """
        AsFloat()
        
        Interprets the object as a floating point number and returns its value.
        Invalid if the object is not actually a floating point number.
        """
        pass

    def AsInt(self): # real signature unknown; restored from __doc__
        """
        AsInt()
        
        Interprets the object as an integer and returns its value.
        Invalid if the object is not actually an integer.
        """
        pass

    def AsResourceId(self): # real signature unknown; restored from __doc__
        """
        AsResourceId()
        
        Interprets the object as a :class:`ResourceId` and returns its value.
        Invalid if the object is not actually a :class:`ResourceId`.
        """
        pass

    def AsString(self): # real signature unknown; restored from __doc__
        """
        AsString()
        
        Interprets the object as a string and returns its value.
        Invalid if the object is not actually a string.
        """
        pass

    def Duplicate(self): # real signature unknown; restored from __doc__
        """
        Duplicate()
        
        Create a deep copy of this object.
        """
        pass

    def FindChild(self, childName): # real signature unknown; restored from __doc__
        """
        FindChild(childName)
        
        Find a child object by a given name.
        """
        pass

    def GetChild(self, index): # real signature unknown; restored from __doc__
        """
        GetChild(index)
        
        Get a child object at a given index.
        """
        pass

    def GetChildren(self): # real signature unknown; restored from __doc__
        """
        GetChildren()
        
        Get a ``list`` of :class:`SDObject` children.
        """
        pass

    def NumChildren(self): # real signature unknown; restored from __doc__
        """
        NumChildren()
        
        Get the number of child objects.
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

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`SDObjectData` with the contents of this object."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name of this object."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`SDType` of this object."""


    __dict__ = None # (!) real value is ''


