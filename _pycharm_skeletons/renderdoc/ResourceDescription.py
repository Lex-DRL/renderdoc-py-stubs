# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ResourceDescription(SwigPyObject):
    """ A description of any type of resource. """
    def SetCustomName(self, givenName): # real signature unknown; restored from __doc__
        """
        SetCustomName(givenName)
        
        Utility function for setting up a custom name to overwrite the auto-generated one.
        
        :param str givenName: The custom name to use.
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

    autogeneratedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if :data:`name` was just autogenerated based on the ID, not assigned a
human-readable name by the application.

"""

    derivedResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ResourceId` of any derived resources, such as resource views or aliases.

Can be empty if there are no derived resources.

This is the inverse of :data:`parentResources` in a potentially many:many relationship, but
typically it is one parent to many derived.

"""

    initialisationChunks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The chunk indices in the structured file that initialised this resource.

This will at least contain the first call that created it, but may contain other auxilliary calls.

"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The name given to this resource."""

    parentResources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ResourceId` of parent resources, of which this is derived.

Can be empty if there are no parent resources.

This is the inverse of :data:`derivedResources` in a potentially many:many relationship, but
typically it is one parent to many derived.

"""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The unique :class:`ResourceId` that identifies this resource."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceType` of the resource."""


    __dict__ = None # (!) real value is ''

