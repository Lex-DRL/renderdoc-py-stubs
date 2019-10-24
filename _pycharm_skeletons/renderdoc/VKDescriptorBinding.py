# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKDescriptorBinding(SwigPyObject):
    """ The contents of a single binding within a descriptor set, either arrayed or not. """
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

    binds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A list of :class:`VKBindingElement` with the binding elements.
If :data:`descriptorCount` is 1 then this isn't an array, and this list has only one element.

"""

    descriptorCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
How many descriptors are in this binding array.
If this binding is empty/non-existant this value will be ``0``.

"""

    dynamicallyUsedCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Lists how many bindings in :data:`binds` are dynamically used. Useful to avoid
redundant iteration to determine whether any bindings are present.

For more information see :data:`VKBindingElement.dynamicallyUsed`.

"""

    stageFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ShaderStageMask` where this binding is visible."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`BindType` of this binding."""


    __dict__ = None # (!) real value is ''


