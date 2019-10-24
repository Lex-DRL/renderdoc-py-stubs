# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class D3D12ConstantBuffer(SwigPyObject):
    """ Describes the details of a constant buffer view descriptor. """
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

    byteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The byte offset where the buffer view starts in the underlying buffer."""

    byteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """How many bytes are in this constant buffer view."""

    immediate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this view is a root constant (i.e. not in a table)."""

    resourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the underlying buffer resource."""

    rootElement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index in the original root signature that this descriptor came from."""

    rootValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
If :data:`immediate` is ``True`` and this is a root constant, this contains a list of
``int`` values with the root values set.

"""

    tableIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index in the the parent descriptor table where this descriptor came from."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


