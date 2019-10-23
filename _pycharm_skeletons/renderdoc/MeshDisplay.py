# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class MeshDisplay(SwigPyObject):
    """
    Describes how to render a mesh preview of one or more meshes. Describes the camera configuration as
    well as what options to use when rendering both the current mesh, and any other auxilliary meshes.
    
    .. data:: NoHighlight
    
      Value for :data:`highlightVert` if no vertex should be highlighted.
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

    aspect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The aspect ratio to use when calculating a perspective projection matrix."""

    cam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`Camera` to use when rendering all of the meshes."""

    curInstance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the currently selected instance in the drawcall."""

    curView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the currently selected multiview view in the drawcall."""

    fov = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The field of view to use when calculating a perspective projection matrix."""

    highlightVert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The index of the vertex to highlight, or :data:`NoHighlight` to select no vertex."""

    maxBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The maximum co-ordinates in each axis of the mesh bounding box."""

    minBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The minimum co-ordinates in each axis of the mesh bounding box."""

    ortho = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the projection matrix to use when unprojecting vertex positions is orthographic."""

    position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`MeshFormat` of the position data for the mesh."""

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`MeshFormat` of the secondary data for the mesh, if used for solid shading."""

    showAllInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if all instances in the drawcall should be drawn as secondary meshes."""

    showBBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the bounding box around the mesh should be rendered."""

    showPrevInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if all previous instances in the drawcall should be drawn as secondary meshes."""

    showWholePass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if all draws in the current pass up to the current draw should be drawn as secondary meshes."""

    solidShadeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`solid shading mode <SolidShade>` to use when rendering the current mesh."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`MeshDataStage` where this mesh data comes from."""

    wireframeDraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """``True`` if the wireframe of the mesh should be rendered as well as solid shading."""


    NoHighlight = 4294967295
    __dict__ = None # (!) real value is ''


