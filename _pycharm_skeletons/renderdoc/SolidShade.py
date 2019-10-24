# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SolidShade(__enum.IntEnum):
    """
    What kind of solid shading to use when rendering a mesh.
    
    .. data:: NoSolid
    
      No solid shading should be done.
    
    .. data:: Solid
    
      The mesh should be rendered in a single flat unshaded color.
    
    .. data:: Lit
    
      The mesh should be rendered with face normals generated on the primitives and used for lighting.
    
    .. data:: Secondary
    
      The mesh should be rendered using the secondary element as color.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    Count = 4
    Lit = 2
    NoSolid = 0
    Secondary = 3
    Solid = 1
    _member_map_ = {
        'Count': 4,
        'Lit': 2,
        'NoSolid': 0,
        'Secondary': 3,
        'Solid': 1,
    }
    _member_names_ = [
        'NoSolid',
        'Solid',
        'Lit',
        'Secondary',
        'Count',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }


