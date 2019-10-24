# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class DrawcallDescription(SwigPyObject):
    """ Describes the properties of a drawcall, dispatch, debug marker, or similar event. """
    def Reset(self): # real signature unknown; restored from __doc__
        """
        Reset()
        
        Resets the drawcall back to a default/empty state.
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

    baseVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For indexed drawcalls, the offset added to each index after fetching."""

    children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of :class:`DrawcallDescription` child drawcalls."""

    copyDestination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ResourceId` identifying the destination object in a copy, resolve or blit
operation.

"""

    copySource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The :class:`ResourceId` identifying the source object in a copy, resolve or blit
operation.

"""

    depthOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The resource used for depth output - see :data:`outputs`."""

    dispatchBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 3D base offset of the workgroup ID if the call allows an override, or 0 if not."""

    dispatchDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 3D number of workgroups to dispatch in a dispatch call."""

    dispatchThreadsDimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The 3D size of each workgroup in threads if the call allows an override, or 0 if not."""

    drawcallId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A 1-based index of this drawcall relative to other drawcalls."""

    drawIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The index of this draw in an call with multiple draws, e.g. an indirect draw.

0 if not part of a multi-draw.

"""

    eventId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :data:`eventId <APIEvent.eventId>` that actually produced the drawcall."""

    events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A list of the :class:`APIEvent` events that happened since the previous drawcall."""

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A set of :class:`DrawFlags` properties describing what kind of drawcall this is."""

    indexByteWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The width in bytes of each index.

Valid values are 1 (depending on API), 2 or 4, or 0 if the drawcall is not an indexed draw.

"""

    indexOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For indexed drawcalls, the first index to fetch from the index buffer."""

    instanceOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For instanced drawcalls, the offset applied before looking up instanced vertex inputs."""

    markerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A RGBA color specified by a debug marker call."""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The name of this drawcall. Typically a summarised/concise list of parameters.

.. note:: For drawcalls, the convention is to list primary parameters (vertex/index count, instance
  count) and omit secondary parameters (vertex offset, instance offset).

"""

    next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The next drawcall in the frame, or ``None`` if this is the last drawcall in the frame."""

    numIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of indices or vertices as appropriate for the drawcall. 0 if not used."""

    numInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of instances for the drawcall. 0 if not used."""

    outputs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
A simple list of the :class:`ResourceId` ids for the color outputs, which can be used
for very coarse bucketing of drawcalls into similar passes by their outputs.

"""

    parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The parent of this drawcall, or ``None`` if there is no parent for this drawcall.

"""

    previous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
The previous drawcall in the frame, or ``None`` if this is the first drawcall in the
frame.

"""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    topology = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`Topology` used in this drawcall."""

    vertexOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For non-indexed drawcalls, the offset applied before looking up each vertex input."""


    __dict__ = None # (!) real value is ''


