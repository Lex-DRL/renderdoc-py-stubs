# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class TextureCategory(__enum.IntFlag):
    """
    A set of flags describing how this texture may be used
    
    .. data:: NoFlags
    
      The texture will not be used for any of the uses below.
    
    .. data:: ShaderRead
    
      The texture will be read by a shader.
    
    .. data:: ColorTarget
    
      The texture will be written to as a color target.
    
    .. data:: DepthTarget
    
      The texture will be written to and tested against as a depth target.
    
    .. data:: ShaderReadWrite
    
      The texture will be read and written to by a shader.
    
    .. data:: SwapBuffer
    
      The texture is part of a window swapchain.
    """
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
                name: the name of the member
                start: the initital start value or None
                count: the number of existing members
                last_value: the last value assigned or None
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    ColorTarget = 2
    DepthTarget = 4
    NoFlags = 0
    ShaderRead = 1
    ShaderReadWrite = 8
    SwapBuffer = 16
    _member_map_ = {
        'ColorTarget': 2,
        'DepthTarget': 4,
        'NoFlags': 0,
        'ShaderRead': 1,
        'ShaderReadWrite': 8,
        'SwapBuffer': 16,
    }
    _member_names_ = [
        'NoFlags',
        'ShaderRead',
        'ColorTarget',
        'DepthTarget',
        'ShaderReadWrite',
        'SwapBuffer',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
        4: 4,
        8: 8,
        16: 16,
    }


