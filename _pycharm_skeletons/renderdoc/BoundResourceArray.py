# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class BoundResourceArray(SwigPyObject):
    """
    Contains all of the bound resources at a particular bindpoint. In APIs that don't
    support resource arrays, there will only be one bound resource.
    """
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

    bindPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The bind point for this array of bound resources."""

    dynamicallyUsedCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Lists how many bindings in :data:`resources` are dynamically used.

Some APIs provide fine-grained usage based on dynamic shader feedback, to support 'bindless'
scenarios where only a small sparse subset of bound resources are actually used.

"""

    resources = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The resources at this bind point"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


