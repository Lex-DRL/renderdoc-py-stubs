# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class VKViewState(SwigPyObject):
    """ Describes the view state in the pipeline. """
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

    discardRectangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`VKRenderArea` defining discard rectangles."""

    discardRectanglesExclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if a fragment in any one of the discard rectangles fails the discard test,
and a fragment in none of them passes.

``False`` if a fragment in any one of the discard rectangles passes the discard test,
and a fragment in none of them is discarded.

.. note::
  A ``True`` value and an empty list of :data:`discardRectangles` means the test is effectively
  disabled, since with no rectangles no fragment can be inside one.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    viewportScissors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`VKViewportScissor`."""


    __dict__ = None # (!) real value is ''


