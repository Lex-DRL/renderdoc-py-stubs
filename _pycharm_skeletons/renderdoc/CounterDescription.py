# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class CounterDescription(SwigPyObject):
    """ Describes a GPU counter's purpose and result value. """
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

    category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The counter category. Can be empty for uncategorized counters."""

    counter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`GPUCounter` this counter represents.

.. note:: This is stored as an ``int`` not a :class:`GPUCounter` to allow for values that may not
  correspond to any of the predefined values if it's a hardware-specific counter value.

"""

    description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If available, a longer human-readable description of the value this counter measures."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A short human-readable name for the counter."""

    resultByteWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of bytes in the resulting value."""

    resultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`type of value <CompType>` returned by this counter."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`CounterUnit` for the result value."""

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`Uuid` of this counter, which uniquely identifies it."""


    __dict__ = None # (!) real value is ''


