# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class Topology(__enum.IntEnum):
    """
    A primitive topology used for processing vertex data.
    
    .. data:: Unknown
    
      An unknown or undefined topology.
    
    .. data:: PointList
    
      A point list.
    
    .. data:: LineList
    
      A line list.
    
    .. data:: LineStrip
    
      A line strip.
    
    .. data:: LineLoop
    
      A line loop.
    
    .. data:: TriangleList
    
      A triangle list.
    
    .. data:: TriangleStrip
    
      A triangle strip.
    
    .. data:: TriangleFan
    
      A triangle fan.
    
    .. data:: LineList_Adj
    
      A line list with adjacency information.
    
    .. data:: LineStrip_Adj
    
      A line strip with adjacency information.
    
    .. data:: TriangleList_Adj
    
      A triangle list with adjacency information.
    
    .. data:: TriangleStrip_Adj
    
      A triangle strip with adjacency information.
    
    .. data:: PatchList
    
      An alias for :data:`PatchList_1CPs`.
    
    .. data:: PatchList_1CPs
    
      A patch list with 1 control points.
    
    .. data:: PatchList_2CPs
    
      A patch list with 2 control points.
    
    .. data:: PatchList_3CPs
    
      A patch list with 3 control points.
    
    .. data:: PatchList_4CPs
    
      A patch list with 4 control points.
    
    .. data:: PatchList_5CPs
    
      A patch list with 5 control points.
    
    .. data:: PatchList_6CPs
    
      A patch list with 6 control points.
    
    .. data:: PatchList_7CPs
    
      A patch list with 7 control points.
    
    .. data:: PatchList_8CPs
    
      A patch list with 8 control points.
    
    .. data:: PatchList_9CPs
    
      A patch list with 9 control points.
    
    .. data:: PatchList_10CPs
    
      A patch list with 10 control points.
    
    .. data:: PatchList_11CPs
    
      A patch list with 11 control points.
    
    .. data:: PatchList_12CPs
    
      A patch list with 12 control points.
    
    .. data:: PatchList_13CPs
    
      A patch list with 13 control points.
    
    .. data:: PatchList_14CPs
    
      A patch list with 14 control points.
    
    .. data:: PatchList_15CPs
    
      A patch list with 15 control points.
    
    .. data:: PatchList_16CPs
    
      A patch list with 16 control points.
    
    .. data:: PatchList_17CPs
    
      A patch list with 17 control points.
    
    .. data:: PatchList_18CPs
    
      A patch list with 18 control points.
    
    .. data:: PatchList_19CPs
    
      A patch list with 19 control points.
    
    .. data:: PatchList_20CPs
    
      A patch list with 20 control points.
    
    .. data:: PatchList_21CPs
    
      A patch list with 21 control points.
    
    .. data:: PatchList_22CPs
    
      A patch list with 22 control points.
    
    .. data:: PatchList_23CPs
    
      A patch list with 23 control points.
    
    .. data:: PatchList_24CPs
    
      A patch list with 24 control points.
    
    .. data:: PatchList_25CPs
    
      A patch list with 25 control points.
    
    .. data:: PatchList_26CPs
    
      A patch list with 26 control points.
    
    .. data:: PatchList_27CPs
    
      A patch list with 27 control points.
    
    .. data:: PatchList_28CPs
    
      A patch list with 28 control points.
    
    .. data:: PatchList_29CPs
    
      A patch list with 29 control points.
    
    .. data:: PatchList_30CPs
    
      A patch list with 30 control points.
    
    .. data:: PatchList_31CPs
    
      A patch list with 31 control points.
    
    .. data:: PatchList_32CPs
    
      A patch list with 32 control points.
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

    LineList = 2
    LineList_Adj = 8
    LineLoop = 4
    LineStrip = 3
    LineStrip_Adj = 9
    PatchList = 12
    PatchList_10CPs = 21
    PatchList_11CPs = 22
    PatchList_12CPs = 23
    PatchList_13CPs = 24
    PatchList_14CPs = 25
    PatchList_15CPs = 26
    PatchList_16CPs = 27
    PatchList_17CPs = 28
    PatchList_18CPs = 29
    PatchList_19CPs = 30
    PatchList_1CPs = 12
    PatchList_20CPs = 31
    PatchList_21CPs = 32
    PatchList_22CPs = 33
    PatchList_23CPs = 34
    PatchList_24CPs = 35
    PatchList_25CPs = 36
    PatchList_26CPs = 37
    PatchList_27CPs = 38
    PatchList_28CPs = 39
    PatchList_29CPs = 40
    PatchList_2CPs = 13
    PatchList_30CPs = 41
    PatchList_31CPs = 42
    PatchList_32CPs = 43
    PatchList_3CPs = 14
    PatchList_4CPs = 15
    PatchList_5CPs = 16
    PatchList_6CPs = 17
    PatchList_7CPs = 18
    PatchList_8CPs = 19
    PatchList_9CPs = 20
    PointList = 1
    TriangleFan = 7
    TriangleList = 5
    TriangleList_Adj = 10
    TriangleStrip = 6
    TriangleStrip_Adj = 11
    Unknown = 0
    _member_map_ = {
        'LineList': 2,
        'LineList_Adj': 8,
        'LineLoop': 4,
        'LineStrip': 3,
        'LineStrip_Adj': 9,
        'PatchList': 12,
        'PatchList_10CPs': 21,
        'PatchList_11CPs': 22,
        'PatchList_12CPs': 23,
        'PatchList_13CPs': 24,
        'PatchList_14CPs': 25,
        'PatchList_15CPs': 26,
        'PatchList_16CPs': 27,
        'PatchList_17CPs': 28,
        'PatchList_18CPs': 29,
        'PatchList_19CPs': 30,
        'PatchList_1CPs': 12,
        'PatchList_20CPs': 31,
        'PatchList_21CPs': 32,
        'PatchList_22CPs': 33,
        'PatchList_23CPs': 34,
        'PatchList_24CPs': 35,
        'PatchList_25CPs': 36,
        'PatchList_26CPs': 37,
        'PatchList_27CPs': 38,
        'PatchList_28CPs': 39,
        'PatchList_29CPs': 40,
        'PatchList_2CPs': 13,
        'PatchList_30CPs': 41,
        'PatchList_31CPs': 42,
        'PatchList_32CPs': 43,
        'PatchList_3CPs': 14,
        'PatchList_4CPs': 15,
        'PatchList_5CPs': 16,
        'PatchList_6CPs': 17,
        'PatchList_7CPs': 18,
        'PatchList_8CPs': 19,
        'PatchList_9CPs': 20,
        'PointList': 1,
        'TriangleFan': 7,
        'TriangleList': 5,
        'TriangleList_Adj': 10,
        'TriangleStrip': 6,
        'TriangleStrip_Adj': 11,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'PointList',
        'LineList',
        'LineStrip',
        'LineLoop',
        'TriangleList',
        'TriangleStrip',
        'TriangleFan',
        'LineList_Adj',
        'LineStrip_Adj',
        'TriangleList_Adj',
        'TriangleStrip_Adj',
        'PatchList',
        'PatchList_2CPs',
        'PatchList_3CPs',
        'PatchList_4CPs',
        'PatchList_5CPs',
        'PatchList_6CPs',
        'PatchList_7CPs',
        'PatchList_8CPs',
        'PatchList_9CPs',
        'PatchList_10CPs',
        'PatchList_11CPs',
        'PatchList_12CPs',
        'PatchList_13CPs',
        'PatchList_14CPs',
        'PatchList_15CPs',
        'PatchList_16CPs',
        'PatchList_17CPs',
        'PatchList_18CPs',
        'PatchList_19CPs',
        'PatchList_20CPs',
        'PatchList_21CPs',
        'PatchList_22CPs',
        'PatchList_23CPs',
        'PatchList_24CPs',
        'PatchList_25CPs',
        'PatchList_26CPs',
        'PatchList_27CPs',
        'PatchList_28CPs',
        'PatchList_29CPs',
        'PatchList_30CPs',
        'PatchList_31CPs',
        'PatchList_32CPs',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
        29: 29,
        30: 30,
        31: 31,
        32: 32,
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
    }


