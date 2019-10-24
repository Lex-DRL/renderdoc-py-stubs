# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class APIProperties(SwigPyObject):
    """ Gives some API-specific information about the capture. """
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

    degraded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the capture was loaded successfully but running in a degraded mode - e.g.
with software rendering, or with some functionality disabled due to lack of support.

"""

    localRenderer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`GraphicsAPI` used to render the log. For remote replay this could be
different to the above, and lets the UI make decisions e.g. to flip rendering of images.

"""

    pipelineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`GraphicsAPI` of the actual log/capture."""

    rgpCapture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the driver and system are configured to allow creating RGP captures."""

    shadersMutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
``True`` if the driver mutates shader reflection structures from event to event.
Currently this is only true for OpenGL where the superfluous indirect in the binding model must be
worked around by re-sorting bindings.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`GPUVendor` of the active GPU being used."""


    __dict__ = None # (!) real value is ''


