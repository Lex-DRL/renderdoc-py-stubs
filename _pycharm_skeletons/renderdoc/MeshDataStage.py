# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class MeshDataStage(__enum.IntEnum):
    """
    Describes a particular stage in the geometry transformation pipeline.
    
    .. data:: Unknown
    
      Unknown or invalid stage.
    
    .. data:: VSIn
    
      The inputs to the vertex shader described by the explicit API vertex input bindings.
    
    .. data:: VSOut
    
      The outputs from the vertex shader corresponding one-to-one to the input elements.
    
    .. data:: GSOut
    
      The final output from the last stage in the pipeline, be that tessellation or geometry shader.
    
      This has possibly been expanded/multiplied from the inputs
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

    GSOut = 3
    Unknown = 0
    VSIn = 1
    VSOut = 2
    _member_map_ = {
        'GSOut': 3,
        'Unknown': 0,
        'VSIn': 1,
        'VSOut': 2,
    }
    _member_names_ = [
        'Unknown',
        'VSIn',
        'VSOut',
        'GSOut',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
    }


