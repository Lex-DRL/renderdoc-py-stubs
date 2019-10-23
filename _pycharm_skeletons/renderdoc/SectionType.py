# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


class SectionType(__enum.IntEnum):
    """
    The types of several pre-defined and known sections. This allows consumers of the API
    to recognise and understand the contents of the section.
    
    Note that sections above the highest value here may be encountered if they were written in a new
    version of RenderDoc that addes a new section type. They should be considered equal to
    :data:`Unknown` by any processing.
    
    .. data:: Unknown
    
      An unknown section - any custom or non-predefined section will have this type.
    
    .. data:: FrameCapture
    
      This section contains the actual captured frame, in RenderDoc's internal chunked representation.
      The contents can be fetched as structured data with or without replaying the frame.
    
      The name for this section will be "renderdoc/internal/framecapture".
    
    .. data:: ResolveDatabase
    
      This section contains platform-specific data used to resolve callstacks.
    
      The name for this section will be "renderdoc/internal/resolvedb".
    
    .. data:: Bookmarks
    
      This section contains a JSON document with bookmarks added to the capture to highlight important
      events.
    
      The name for this section will be "renderdoc/ui/bookmarks".
    
    .. data:: Notes
    
      This section contains a JSON document with free-form information added for human consumption, e.g.
      details about how the capture was obtained with repro steps in the original program, or with
      driver and machine info.
    
      The name for this section will be "renderdoc/ui/notes".
    
    .. data:: ResourceRenames
    
      This section contains a JSON document with custom names applied to resources in the UI, over and
      above any friendly names specified in the capture itself.
    
      The name for this section will be "renderdoc/ui/resrenames".
    
    .. data:: AMDRGPProfile
    
      This section contains a .rgp profile from AMD's RGP tool, which can be extracted and loaded.
    
      The name for this section will be "amd/rgp/profile".
    
    .. data:: ExtendedThumbnail
    
      This section contains a thumbnail in format other than JPEG. For example, when it needs to be
      lossless.
    
      The name for this section will be "renderdoc/internal/exthumb".
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

    AMDRGPProfile = 6
    Bookmarks = 3
    Count = 8
    ExtendedThumbnail = 7
    First = 0
    FrameCapture = 1
    Notes = 4
    ResolveDatabase = 2
    ResourceRenames = 5
    Unknown = 0
    _member_map_ = {
        'AMDRGPProfile': 6,
        'Bookmarks': 3,
        'Count': 8,
        'ExtendedThumbnail': 7,
        'First': 0,
        'FrameCapture': 1,
        'Notes': 4,
        'ResolveDatabase': 2,
        'ResourceRenames': 5,
        'Unknown': 0,
    }
    _member_names_ = [
        'Unknown',
        'FrameCapture',
        'ResolveDatabase',
        'Bookmarks',
        'Notes',
        'ResourceRenames',
        'AMDRGPProfile',
        'ExtendedThumbnail',
        'Count',
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
    }


