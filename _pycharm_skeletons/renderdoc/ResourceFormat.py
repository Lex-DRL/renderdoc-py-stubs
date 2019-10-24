# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ResourceFormat(SwigPyObject):
    """ Description of the format of a resource or element. """
    def BGRAOrder(self): # real signature unknown; restored from __doc__
        """
        BGRAOrder()
        
        :return: ``True`` if the components are to be read in ``BGRA`` order.
        :rtype: ``bool``
        """
        pass

    def Name(self): # real signature unknown; restored from __doc__
        """
        Name()
        
        :return: The name of the format.
        :rtype: ``str``
        """
        pass

    def SetBGRAOrder(self, flag): # real signature unknown; restored from __doc__
        """
        SetBGRAOrder(flag)
        
        Set BGRA order flag. See :meth:`BGRAOrder`.
        
        :param bool flag: The new flag value.
        """
        pass

    def SetYUVPlaneCount(self, planes): # real signature unknown; restored from __doc__
        """
        SetYUVPlaneCount(planes)
        
        Set number of YUV planes. See :meth:`YUVPlaneCount`.
        
        Invalid values will result in 1 being set.
        
        :param int planes: The new number of YUV planes.
        """
        pass

    def SetYUVSubsampling(self, subsampling): # real signature unknown; restored from __doc__
        """
        SetYUVSubsampling(subsampling)
        
        Set YUV subsampling rate. See :meth:`YUVSubsampling`.
        
        The value should be e.g. 444 for 4:4:4 or 422 for 4:2:2. Invalid values will result in 0 being set.
        
        :param int subsample: The new subsampling rate.
        """
        pass

    def Special(self): # real signature unknown; restored from __doc__
        """
        Special()
        
        :return: ``True`` if the ``ResourceFormat`` is a 'special' non-regular type.
        :rtype: ``bool``
        """
        pass

    def SRGBCorrected(self): # real signature unknown; restored from __doc__
        """
        SRGBCorrected()
        
        Equivalent to checking if :data:`compType` is :data:`CompType.UNormSRGB`
        
        :return: ``True`` if the components are SRGB corrected on read and write.
        :rtype: ``bool``
        """
        pass

    def YUVPlaneCount(self): # real signature unknown; restored from __doc__
        """
        YUVPlaneCount()
        
        Get the number of planes for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 1 is returned.
        
        :return: The number of planes
        :rtype: ``int``
        """
        pass

    def YUVSubsampling(self): # real signature unknown; restored from __doc__
        """
        YUVSubsampling()
        
        Get the subsampling rate for a YUV format. Only valid when :data:`type` is
        a YUV format like :attr:`ResourceFormatType.YUV8`.
        
        For other formats, 0 is returned.
        
        :return: The subsampling rate, e.g. 444 for 4:4:4 or 420 for 4:2:0
        :rtype: ``int``
        """
        pass

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

    compByteWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The width in bytes of each component."""

    compCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of components in each element."""

    compType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The :class:`type <CompType>` of each component."""

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
Set number of YUV planes. See :meth:`YUVPlaneCount`.

Invalid values will result in 1 being set.

:param int planes: The new number of YUV planes.

"""


    __dict__ = None # (!) real value is ''


