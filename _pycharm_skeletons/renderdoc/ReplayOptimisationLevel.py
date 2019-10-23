# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class ReplayOptimisationLevel(__enum.IntEnum):
    """
    The level of optimisation used in
    
    .. data:: NoOptimisation
    
      Completely disabled, no optimisation will be used at all.
    
    .. data:: Conservative
    
      Optimisation is used when it doesn't interfere with replay correctness.
    
    .. data:: Balanced
    
      Optimisation is used when it has minimal impact on replay correctness. This could include e.g.
      resources appearing cleared instead of containing contents from prior frames where those resources
      are written to before being read.
    
    .. data:: Fastest
    
      All possible optimisations are enabled as long as they do not cause invalid/incorrect replay.
      This could result in side-effects like data from one replay being visible early in another replay,
      if it's known that the data will be overwritten before being used.
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

    Balanced = 2
    Conservative = 1
    Count = 4
    Fastest = 3
    First = 0
    NoOptimisation = 0
    _member_map_ = {
        'Balanced': 2,
        'Conservative': 1,
        'Count': 4,
        'Fastest': 3,
        'First': 0,
        'NoOptimisation': 0,
    }
    _member_names_ = [
        'NoOptimisation',
        'Conservative',
        'Balanced',
        'Fastest',
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


