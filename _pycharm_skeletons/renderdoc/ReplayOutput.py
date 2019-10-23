# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


from .SwigPyObject import SwigPyObject

class ReplayOutput(SwigPyObject):
    """
    A stateful output handle that contains the current configuration for one particular view
    of the capture. This allows multiple outputs to run independently without interfering with each
    other.
    
    The different types are enumerated in :class:`ReplayOutputType`.
    
    .. function:: KillCallback()
    
      Not an actual member function - the signature for any ``KillCallback`` callbacks.
    
      Called whenever some on-going blocking process needs to determine if it should close.
    
      :return: Whether or not the process should be killed.
      :rtype: ``bool``
    
    .. function:: ProgressCallback()
    
      Not an actual member function - the signature for any ``ProgressCallback`` callbacks.
    
      Called by an on-going blocking process to update a progress bar or similar user feedback.
    
      The progress value will go from 0.0 to 1.0 as the process completes. Any other value will indicate
      that the process has completed
    
      :param float progress: The latest progress amount.
    
    .. function:: PreviewWindowCallback()
    
      Not an actual member function - the signature for any ``PreviewWindowCallback`` callbacks.
    
      Called when a preview window could optionally be opened to display some information. It will be
      called repeatedly with :paramref:`active` set to ``True`` to allow any platform-specific message
      pumping.
    
      :param bool active: ``True`` if a preview window is active/opened, ``False`` if it has closed.
      :return: The windowing data for a preview window, or empty/default values if no window should be
        created.
      :rtype: WindowingData
    
    .. data:: NoResult
    
      No result was found in e.g. :meth:`PickVertex`.
    """
    def AddThumbnail(self, window, textureId, typeHint, mip, slice): # real signature unknown; restored from __doc__
        """
        AddThumbnail(window, textureId, typeHint, mip, slice)
        
        Sets up a thumbnail for displaying a particular texture with sensible defaults.
        
        The window handle specified will be filled (in an aspect-ratio preserving way) with the texture.
        
        If the window specified has been used for a thumbnail before, then the texture will be updated but
        otherwise nothing will be created and the existing internal data will be reused. This means that
        you can call this function multiple times to just change the texture.
        
        Should only be called for texture outputs.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :param ResourceId textureId: The texture ID to display in the thumbnail preview.
        :param int slice: The slice of the texture to display.
        :param int mip: The mip of the texture to display.
        :return: A boolean indicating if the thumbnail was successfully created.
        :rtype: ``bool``
        """
        pass

    def ClearThumbnails(self): # real signature unknown; restored from __doc__
        """
        ClearThumbnails()
        
        Clear and release all thumbnails associated with this output. See :meth:`AddThumbnail`.
        """
        pass

    def DisablePixelContext(self): # real signature unknown; restored from __doc__
        """
        DisablePixelContext()
        
        Disable the pixel context view from rendering.
        """
        pass

    def Display(self): # real signature unknown; restored from __doc__
        """
        Display()
        
        Render to the window handle specified when the output was created.
        
        This will also render any thumbnails and the pixel context, if enabled.
        """
        pass

    def GetCustomShaderTexID(self): # real signature unknown; restored from __doc__
        """
        GetCustomShaderTexID()
        
        Retrieves the :class:`ResourceId` containing the contents of the texture after being
        passed through a custom shader pass.
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the results of the custom shader.
        :rtype: ResourceId
        """
        pass

    def GetDebugOverlayTexID(self): # real signature unknown; restored from __doc__
        """
        GetDebugOverlayTexID()
        
        Retrieves the :class:`ResourceId` containing the contents of the debug overlay
        rendering (if enabled).
        
        Should only be called for texture outputs.
        
        :return: The :class:`ResourceId` assigned to the texture with the debug overlay.
        :rtype: ResourceId
        """
        pass

    def GetDimensions(self): # real signature unknown; restored from __doc__
        """
        GetDimensions()
        
        Retrieve the current dimensions of the output.
        
        :return: The current width and height of the output.
        :rtype: ``pair`` of two ``int``
        """
        pass

    def GetHistogram(self, minval, maxval, channels): # real signature unknown; restored from __doc__
        """
        GetHistogram(minval, maxval, channels)
        
        Retrieve a list of values that can be used to show a histogram of values for the
        current texture.
        
        The output list contains N buckets, and each bucket has the number of pixels that falls in each
        bucket when the pixel values are divided between ``minval`` and ``maxval``.
        
        Should only be called for texture outputs.
        
        :param float minval: The lower end of the smallest bucket. If any values are below this, they are
          not added to any bucket.
        :param float maxval: The upper end of the largest bucket. If any values are above this, they are
          not added to any bucket.
        :param list channels: A list of four ``bool`` values indicating whether each of RGBA should be
          included in the count.
        :return: A list of the unnormalised bucket values.
        :rtype: ``list`` of ``int``
        """
        pass

    def GetMinMax(self): # real signature unknown; restored from __doc__
        """
        GetMinMax()
        
        Retrieves the minimum and maximum values in the current texture.
        
        Should only be called for texture outputs.
        
        :return: A tuple with the minimum and maximum pixel values respectively.
        :rtype: ``tuple`` of PixelValue and PixelValue
        """
        pass

    def PickPixel(self, textureId, customShader, x, y, sliceFace, mip, sample): # real signature unknown; restored from __doc__
        """
        PickPixel(textureId, customShader, x, y, sliceFace, mip, sample)
        
        Retrieve the contents of a particular pixel in a texture.
        
        Should only be called for texture outputs.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        :param ResourceId textureId: The texture to pick the pixel from.
        :param bool customShader: Whether to apply the configured custom shader.
        :param int x: The x co-ordinate to pick from.
        :param int y: The y co-ordinate to pick from.
        :param int sliceFace: The slice of an array or 3D texture, or face of a cubemap texture.
        :param int mip: The mip level to pick from.
        :param int sample: The multisample sample to pick from.
        :return: The contents of the pixel.
        :rtype: PixelValue
        """
        pass

    def PickVertex(self, eventId, x, y): # real signature unknown; restored from __doc__
        """
        PickVertex(eventId, x, y)
        
        Retrieves the vertex and instance that is under the cursor location, when viewed
        relative to the current window with the current mesh display configuration.
        
        .. note::
          X and Y co-ordinates are always considered to be top-left, even on GL, for consistency between
          APIs and preventing the need for API-specific code in most cases. This means if co-ordinates are
          fetched from e.g. viewport or scissor data or other GL pipeline state which is perhaps in
          bottom-left co-ordinates, care must be taken to translate them.
        
        Should only be called for mesh outputs.
        
        :param int eventId: The event ID to pick at.
        :param int x: The x co-ordinate to pick from.
        :param int y: The y co-ordinate to pick from.
        :return: A tuple with the first value being the vertex index in the mesh, and the second value being
          the instance index. The values are set to :data:`NoResult` if no vertex was found, 
        :rtype: ``tuple`` of ``int`` and ``int``
        """
        pass

    def ReadbackOutputTexture(self): # real signature unknown; restored from __doc__
        """
        ReadbackOutputTexture()
        
        Read the output texture back as byte data. Primarily useful for headless outputs where
        the output data is not displayed anywhere natively.
        
        :return: The output texture data as tightly packed RGB 3-byte data.
        :rtype: ``bytes``
        """
        pass

    def SetDimensions(self, width, height): # real signature unknown; restored from __doc__
        """
        SetDimensions(width, height)
        
        Sets the dimensions of the output, useful only for headless outputs that don't have a
        backing window which don't have any implicit dimensions. This allows configuring a virtual viewport
        which is useful for operations like picking vertices that depends on the output dimensions.
        
        .. note:: For outputs with backing windows, this will be ignored.
        
        :param int width: The width to use.
        :param int height: The height to use.
        """
        pass

    def SetMeshDisplay(self, o): # real signature unknown; restored from __doc__
        """
        SetMeshDisplay(o)
        
        Sets the :class:`MeshDisplay` configuration for a mesh output.
        """
        pass

    def SetPixelContext(self, window): # real signature unknown; restored from __doc__
        """
        SetPixelContext(window)
        
        Sets up a zoomed in pixel context view around a particular pixel selection.
        
        The texture rendering uses the configuration specified in :meth:`SetTextureDisplay` except with a
        fixed high zoom value and a fixed position, see :meth:`SetPixelContextLocation`.
        
        Should only be called for texture outputs.
        
        :param WindowingData window: A :class:`WindowingData` describing the native window.
        :return: A boolean indicating if the pixel context was successfully configured.
        :rtype: ``bool``
        """
        pass

    def SetPixelContextLocation(self, x, y): # real signature unknown; restored from __doc__
        """
        SetPixelContextLocation(x, y)
        
        Sets the pixel that the pixel context should be centred on.
        
        Should only be called for texture outputs.
        """
        pass

    def SetTextureDisplay(self, o): # real signature unknown; restored from __doc__
        """
        SetTextureDisplay(o)
        
        Sets the :class:`TextureDisplay` configuration for a texture output.
        """
        pass

    def Shutdown(self): # real signature unknown; restored from __doc__
        """
        Shutdown()
        
        Shutdown this output.
        
        It's optional to call this, as calling :meth:`ReplayController.Shutdown` will shut down all of its
        outputs.
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

    this = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    thisown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    NoResult = 4294967295
    __dict__ = None # (!) real value is ''


