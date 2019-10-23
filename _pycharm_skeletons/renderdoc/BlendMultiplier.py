# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class BlendMultiplier(__enum.IntEnum):
    """
    A multiplier on one component in the blend equation.
    
    .. note:: The "source" value is the value written out by the shader.
    
      The "second source" value is provided when dual source blending is used.
    
      The "destination" value is the value in the target being blended to.
    
      These values are combined using a given blend operation, see :class:`BlendOperation`.
    
      Where a color is referenced, the value depends on where the multiplier appears in the blend
      equation. If it is a multiplier on the color component then it refers to the color component. If
      it is a multiplier on the alpha component then it refers to the alpha component.
    
      If alpha is referenced explicitly it always refers to alpha, in both color and alpha equations.
    
    .. data:: Zero
    
      The literal value ``0.0``.
    
    .. data:: One
    
      The literal value ``1.0``.
    
    .. data:: SrcCol
    
      The source value's color.
    
    .. data:: InvSrcCol
    
      ``1.0`` minus the source value's color.
    
    .. data:: DstCol
    
      The destination value's color.
    
    .. data:: InvDstCol
    
      ``1.0`` minus the destination value's color.
    
    .. data:: SrcAlpha
    
      The source value's alpha.
    
    .. data:: InvSrcAlpha
    
      ``1.0`` minus the source value's alpha.
    
    .. data:: DstAlpha
    
      The destination value's alpha.
    
    .. data:: InvDstAlpha
    
      ``1.0`` minus the destination value's alpha.
    
    .. data:: SrcAlphaSat
    
      The lowest value of :data:`SrcAlpha` and :data:`InvDstAlpha`. If used in the alpha equation, it takes the value :data:`One`.
    
    .. data:: FactorRGB
    
      The color components of the fixed blend factor constant.
    
    .. data:: InvFactorRGB
    
      ``1.0`` minus the color components of the fixed blend factor constant.
    
    .. data:: FactorAlpha
    
      The alpha component of the fixed blend factor constant.
    
    .. data:: InvFactorAlpha
    
      ``1.0`` minus the alpha components of the fixed blend factor constant.
    
    .. data:: Src1Col
    
      The second source value's color.
    
    .. data:: InvSrc1Col
    
      ``1.0`` minus the second source value's color.
    
    .. data:: Src1Alpha
    
      The second source value's alpha.
    
    .. data:: InvSrc1Alpha
    
      ``1.0`` minus the second source value's alpha.
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

    DstAlpha = 8
    DstCol = 4
    FactorAlpha = 13
    FactorRGB = 11
    InvDstAlpha = 9
    InvDstCol = 5
    InvFactorAlpha = 14
    InvFactorRGB = 12
    InvSrc1Alpha = 18
    InvSrc1Col = 16
    InvSrcAlpha = 7
    InvSrcCol = 3
    One = 1
    Src1Alpha = 17
    Src1Col = 15
    SrcAlpha = 6
    SrcAlphaSat = 10
    SrcCol = 2
    Zero = 0
    _member_map_ = {
        'DstAlpha': 8,
        'DstCol': 4,
        'FactorAlpha': 13,
        'FactorRGB': 11,
        'InvDstAlpha': 9,
        'InvDstCol': 5,
        'InvFactorAlpha': 14,
        'InvFactorRGB': 12,
        'InvSrc1Alpha': 18,
        'InvSrc1Col': 16,
        'InvSrcAlpha': 7,
        'InvSrcCol': 3,
        'One': 1,
        'Src1Alpha': 17,
        'Src1Col': 15,
        'SrcAlpha': 6,
        'SrcAlphaSat': 10,
        'SrcCol': 2,
        'Zero': 0,
    }
    _member_names_ = [
        'Zero',
        'One',
        'SrcCol',
        'InvSrcCol',
        'DstCol',
        'InvDstCol',
        'SrcAlpha',
        'InvSrcAlpha',
        'DstAlpha',
        'InvDstAlpha',
        'SrcAlphaSat',
        'FactorRGB',
        'InvFactorRGB',
        'FactorAlpha',
        'InvFactorAlpha',
        'Src1Col',
        'InvSrc1Col',
        'Src1Alpha',
        'InvSrc1Alpha',
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
    }


