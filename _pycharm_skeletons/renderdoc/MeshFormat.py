# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class MeshFormat(SwigPyObject):
    """
    Contains the details of a single element of data (such as position or texture
    co-ordinates) within a mesh.
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

    allowRestart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the primitive restart index feature should be used."""

    baseVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """For indexed meshes, a value added to each index before using it to read the vertex."""

    farPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The far plane for the projection matrix."""

    format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceFormat` describing this mesh component."""

    indexByteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset in bytes where the indices start in idxbuf."""

    indexByteStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width in bytes of each index. Valid values are 1 (depending on API), 2 or 4."""

    indexResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the index buffer that goes with this mesh element."""

    instanced = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this mesh element comes from instanced data. See :data:`instStepRate`."""

    instStepRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of instances to render with the same value. See :data:`instanced`."""

    meshColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The color to use for rendering the wireframe of this mesh element, as a :class:`FloatVector`."""

    nearPlane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The near plane for the projection matrix."""

    numIndices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of vertices in the mesh."""

    restartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The primitive restart index to use, if possible. See :data:`allowRestart`."""

    showAlpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the alpha component of this element should be used."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    topology = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`Topology` that describes the primitives in this mesh."""

    unproject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if this mesh element contains post-projection positional data."""

    vertexByteOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The offset in bytes to the start of the vertex data."""

    vertexByteStride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The stride in bytes between the start of one vertex and the start of another."""

    vertexResourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`ResourceId` of the vertex buffer containing this mesh element."""


    __dict__ = None # (!) real value is ''


