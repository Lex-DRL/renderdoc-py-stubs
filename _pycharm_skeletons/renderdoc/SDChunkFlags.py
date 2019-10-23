# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SDChunkFlags(__enum.IntEnum):
    """
    Bitfield flags that could be applied to an :class:`SDChunk`.
    
    .. data:: NoFlags
    
      This chunk has no special properties.
    
    .. data:: OpaqueChunk
    
      This chunk wasn't supported for decoding or was skipped for another reason and was detailed as
      an opaque byte stream. It should be preserved as-is and will remain in native RDC format.
    
    .. data:: HasCallstack
    
      This chunk has a callstack. Used to indicate the presence of a callstack even if it's empty
      (perhaps due to failure to collect the stack frames).
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

    HasCallstack = 2
    NoFlags = 0
    OpaqueChunk = 1
    _member_map_ = {
        'HasCallstack': 2,
        'NoFlags': 0,
        'OpaqueChunk': 1,
    }
    _member_names_ = [
        'NoFlags',
        'OpaqueChunk',
        'HasCallstack',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
        2: 2,
    }


