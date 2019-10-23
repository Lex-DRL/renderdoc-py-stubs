# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class GPUVendor(__enum.IntEnum):
    """
    Identifies a GPU vendor.
    
    .. data:: Unknown
    
      A GPU from an unknown vendor
    
    .. data:: ARM
    
      An ARM GPU
    
    .. data:: AMD
    
      An AMD GPU
    
    .. data:: Broadcom
    
      A Broadcom GPU
    
    .. data:: Imagination
    
      An Imagination GPU
    
    .. data:: Intel
    
      An Intel GPU
    
    .. data:: nVidia
    
      An nVidia GPU
    
    .. data:: Qualcomm
    
      A Qualcomm  GPU
    
    .. data:: Verisilicon
    
      A Verisilicon or Vivante GPU
    
    .. data:: Software
    
      A software-rendering emulated GPU
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

    AMD = 2
    ARM = 1
    Broadcom = 3
    Imagination = 4
    Intel = 5
    nVidia = 6
    Qualcomm = 7
    Software = 9
    Unknown = 0
    Verisilicon = 8
    _member_map_ = {
        'AMD': 2,
        'ARM': 1,
        'Broadcom': 3,
        'Imagination': 4,
        'Intel': 5,
        'Qualcomm': 7,
        'Software': 9,
        'Unknown': 0,
        'Verisilicon': 8,
        'nVidia': 6,
    }
    _member_names_ = [
        'Unknown',
        'ARM',
        'AMD',
        'Broadcom',
        'Imagination',
        'Intel',
        'nVidia',
        'Qualcomm',
        'Verisilicon',
        'Software',
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
    }


