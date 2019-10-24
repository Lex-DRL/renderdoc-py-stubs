# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ReplayOptions(SwigPyObject):
    """ The options controlling how replay of a capture should be performed """
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

    apiValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Replay with API validation enabled and use debug messages from there, ignoring any
that may be contained in the capture.

The default is not to do any validation.

.. note:: RenderDoc does not handle invalid API use in the general case so validation should still
  be performed at runtime in your program for ground truth results.

"""

    forceGPUDeviceID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Force the selection of a GPU by device ID. This allows overriding which GPU is used to
replay on.

When set to 0, specifies no particular device.

See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.

"""

    forceGPUDriverName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Force the selection of a GPU by driver name. This allows overriding which GPU is used
to replay on.

When set to an empty string, specifies no particular driver.

See :data:`forceGPUDeviceID` for a full explanation of GPU selection override.

"""

    forceGPUVendor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Force the selection of a GPU by vendor ID. This allows overriding which GPU is used to
replay on, even if a different GPU would be the best match for the capture.

When set to :data:`GPUVendor.Unknown`, specifies no particular vendor.

See also :data:`forceGPUDeviceID` and :data:`forceGPUDriverName`. Available GPUs can be enumerated
using :meth:`CaptureAccess.GetAvailableGPUs`.

The default is not to do any override. The capture contains information about what GPU was used, and
the closest matching GPU is used on replay.

.. note::
  If a GPU is forced that is not available or not supported for a given capture, such as when GPUs
  are only available for some APIs and not others, the default GPU selection will be used. If a GPU
  is available for a capture but fails to open however then there is no fallback to a default GPU.

  OpenGL does not support GPU selection so the default method (which effectively does nothing) will
  always be used.

"""

    optimisation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
How much optimisation should be done, potentially at the cost of correctness.

The default is :data:`ReplayOptimisationLevel.Balanced`.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is ''


