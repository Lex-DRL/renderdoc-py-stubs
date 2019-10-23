# encoding: utf-8
# module renderdoc
# from P:\1-Scripts\_Python\Py-Autocomplete\renderdoc.pyd
# by generator 1.146
# no doc

# imports
import enum as __enum


# Variables with simple values

BT2020 = 4
BT601 = 3
BT709 = 2

CositedEven = 0

ITUFull = 0
ITUNarrow = 1

Midpoint = 1

RangeOnly = 1
Raw = 0

# functions

def AllocArrayMem(sz): # real signature unknown; restored from __doc__
    """ AllocArrayMem(sz) """
    pass

def BecomeRemoteServer(listenhost, killReplay, previewWindow): # real signature unknown; restored from __doc__
    """
    BecomeRemoteServer(listenhost, killReplay, previewWindow)
    
    This launches a remote server which will continually run in a loop to server requests
    from external sources.
    
    This function will block until a remote connection tells the server to shut down, or the
    ``killReplay`` callback returns ``True``.
    
    :param str host: The name of the interface to listen on.
    :param KillCallback killReplay: A callback that returns a ``bool`` indicating if the server should
      be shut down or not.
    :param PreviewWindowCallback previewWindow: A callback that returns information for a preview window
      when the server wants to display some preview of the ongoing replay.
    """
    pass

def CanGlobalHook(): # real signature unknown; restored from __doc__
    """
    CanGlobalHook()
    
    Determines if the global hook is supported on the current platform and configuration.
    
    :return: ``True`` if global hooking can be used on the platform, ``False`` if not.
    :rtype: ``bool``
    """
    pass

def CBUsage(stage): # real signature unknown; restored from __doc__
    """
    CBUsage(stage)
    
    Calculate the ``ResourceUsage`` value for constant buffer use at a given shader stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for constant buffer usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def CheckAndroidPackage(URL, packageAndActivity, flags): # real signature unknown; restored from __doc__
    """
    CheckAndroidPackage(URL, packageAndActivity, flags)
    
    Internal function for checking remote Android package for requirements
    """
    pass

def CreateAndroidWindowingData(window): # real signature unknown; restored from __doc__
    """
    CreateAndroidWindowingData(window)
    
    Create a :class:`WindowingData` for an Android ``ANativeWindow`` handle.
    
    :param ANativeWindow window: The native ``ANativeWindow`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateBugReport(logfile, dumpfile, report): # real signature unknown; restored from __doc__
    """
    CreateBugReport(logfile, dumpfile, report)
    
    Internal function for creating a bug report zip.
    """
    pass

def CreateGgpWindowingData(): # real signature unknown; restored from __doc__
    """
    CreateGgpWindowingData()
    
    Create a :class:`WindowingData` for a GGP application.
    
    :return: A :class:`WindowingData` corresponding to the given system.
    :rtype: WindowingData
    """
    pass

def CreateHeadlessWindowingData(width, height): # real signature unknown; restored from __doc__
    """
    CreateHeadlessWindowingData(width, height)
    
    Create a :class:`WindowingData` for no backing window, it will be headless.
    
    :param int width: The initial width for this virtual window.
    :param int height: The initial height for this virtual window.
    
    :return: A :class:`WindowingData` corresponding to an 'empty' backing window.
    :rtype: WindowingData
    """
    pass

def CreateMacOSWindowingData(view, layer): # real signature unknown; restored from __doc__
    """
    CreateMacOSWindowingData(view, layer)
    
    Create a :class:`WindowingData` for an metal/opengl-compatible macOS ``CALayer`` handle
    and ``NSView`` handle (as void pointers).
    
    :param NSView view: The native ``NSView`` handle for this window.
    :param CALayer layer: The native ``CALayer`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateRemoteServerConnection(URL): # real signature unknown; restored from __doc__
    """
    CreateRemoteServerConnection(URL)
    
    Create a connection to a remote server running on given hostname and port.
    
    :param str URL: The hostname to connect to, if blank then localhost is used. If no protocol is
      specified then default TCP enumeration happens.
    :return: The status of opening the capture, whether success or failure, and a :class:`RemoteServer`
      instance if it were successful
    :rtype: ``pair`` of ReplayStatus and RemoteServer
    """
    pass

def CreateTargetControl(URL, ident, clientName, forceConnection): # real signature unknown; restored from __doc__
    """
    CreateTargetControl(URL, ident, clientName, forceConnection)
    
    Creates a :class:`TargetControl` connection to a given hostname and ident.
    
    This function will block until the control connection is ready, or an error occurs.
    
    :param str URL: The URL to connect to. If blank, the local machine is used. If no protocol is
      specified then default TCP enumeration happens.
    :param int ident: The ident for the particular target to connect to on that machine.
    :param str clientName: The client name to use when connecting. See
      :meth:`TargetControl.GetBusyClient`.
    :param bool forceConnection: Force the connection and kick off any existing client that is currently
      connected.
    :return: A handle to the target control connection, or ``None`` if something went wrong.
    :rtype: TargetControl
    """
    pass

def CreateWaylandWindowingData(display, window): # real signature unknown; restored from __doc__
    """
    CreateWaylandWindowingData(display, window)
    
    Create a :class:`WindowingData` for an Wayland ``wl_surface`` handle.
    
    :param wl_display display: The ``wl_display`` connection used for this window.
    :param wl_surface window: The native ``wl_surface`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateWin32WindowingData(window): # real signature unknown; restored from __doc__
    """
    CreateWin32WindowingData(window)
    
    Create a :class:`WindowingData` for a Win32 ``HWND`` handle.
    
    :param HWND window: The native ``HWND`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateXCBWindowingData(connection, window): # real signature unknown; restored from __doc__
    """
    CreateXCBWindowingData(connection, window)
    
    Create a :class:`WindowingData` for an XCB ``xcb_window_t`` handle.
    
    :param xcb_connection_t connection: The ``xcb_connection_t`` connection used for this window.
    :param xcb_window_t window: The native ``xcb_window_t`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def CreateXlibWindowingData(display, window): # real signature unknown; restored from __doc__
    """
    CreateXlibWindowingData(display, window)
    
    Create a :class:`WindowingData` for an Xlib ``Drawable`` handle.
    
    :param Display display: The ``Display`` connection used for this window.
    :param Drawable window: The native ``Drawable`` handle for this window.
    :return: A :class:`WindowingData` corresponding to the given window.
    :rtype: WindowingData
    """
    pass

def EndSelfHostCapture(dllname): # real signature unknown; restored from __doc__
    """
    EndSelfHostCapture(dllname)
    
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to end a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass

def EnumerateRemoteTargets(URL, nextIdent): # real signature unknown; restored from __doc__
    """
    EnumerateRemoteTargets(URL, nextIdent)
    
    Repeatedly query to enumerate which targets are active on a given machine and their
    idents.
    
    Initially this should be called with ``nextIdent`` being 0, to retrieve the first target
    active. After that it can be called again and again with the previous return value to enumerate
    more targets.
    
    This function will block for a variable timeout depending on how many targets are scanned.
    
    :param str URL: The URL to connect to. If blank, the local machine is used. If no protocol is
      specified then default TCP enumeration happens.
    :param int nextIdent: The next ident to scan.
    :return: The ident of the next active target, or ``0`` if no other targets exist.
    :rtype: ``int``
    """
    pass

def ExecuteAndInject(app, workingDir, cmdLine, env, capturefile, opts, waitForExit): # real signature unknown; restored from __doc__
    """
    ExecuteAndInject(app, workingDir, cmdLine, env, capturefile, opts, waitForExit)
    
    Launch an application and inject into it to allow capturing.
    
    :param str app: The path to the application to run.
    :param str workingDir: The working directory to use when running the application. If blank, the
      directory containing the application is used.
    :param str cmdLine: The command line to use when running the application, it will be processed in a
      platform specific way to generate arguments.
    :param list env: Any :class:`EnvironmentModification` that should be made when running the program.
    :param str capturefile: The capture file path template, or blank to use a default location.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :param bool waitForExit: If ``True`` this function will block until the process exits.
    :return: The :class:`ExecuteResult` indicating both the status of the operation (success or failure)
      and any reason for failure, or else the ident where the new application is listening for target
      control if everything succeeded.
    :rtype: ExecuteResult
    """
    pass

def FloatToHalf(flt): # real signature unknown; restored from __doc__
    """
    FloatToHalf(flt)
    
    A utility function that converts a float to a half (stored in a 16-bit unsigned
    integer).
    
    :param float f: The floating point value.
    :return: The nearest half-float equivalent stored as an int.
    :rtype: ``int``
    """
    pass

def FreeArrayMem(mem): # real signature unknown; restored from __doc__
    """ FreeArrayMem(mem) """
    pass

def GetCommitHash(): # real signature unknown; restored from __doc__
    """
    GetCommitHash()
    
    Retrieves the commit hash used to build.
    
    This will be in the form "0123456789abcdef0123456789abcdef01234567"
    
    :return: The commit hash.
    :rtype: ``str``
    """
    pass

def GetConfigSetting(name): # real signature unknown; restored from __doc__
    """
    GetConfigSetting(name)
    
    Internal function for retrieving a config setting.
    """
    pass

def GetCurrentProcessMemoryUsage(): # real signature unknown; restored from __doc__
    """
    GetCurrentProcessMemoryUsage()
    
    Returns the current process's memory usage in bytes
    
    :return: The current memory usage in bytes.
    :rtype: ``int``
    """
    pass

def GetDefaultCaptureOptions(): # real signature unknown; restored from __doc__
    """
    GetDefaultCaptureOptions()
    
    Retrieve the default and recommended set of capture options.
    
    :return: The default capture options.
    :rtype: CaptureOptions
    """
    pass

def GetDeviceProtocolController(protocol): # real signature unknown; restored from __doc__
    """
    GetDeviceProtocolController(protocol)
    
    Creates a :class:`DeviceProtocolController` that provides device-specific controls.
    
    This interface is intended to allow closer integration with remote devices.
    
    .. note::
      Note that the use of scripting with Android is explicitly **not supported** due to the inherent
      fragility and unreliability of the Android platform. This interface is designed primarily for
      internal use and no support will be provided for Android-specific problems encountered using this.
    
    This function will not block, however the protocol may still be initialising when it is returned so
    immediate use of it may block.
    
    :param str protocol: The protocol to fetch a controller for.
    :return: A handle to the protocol controller, or ``None`` if something went wrong such as an
      unsupported protocol being specified.
    :rtype: DeviceProtocolController
    """
    pass

def GetDriverInformation(api): # real signature unknown; restored from __doc__
    """
    GetDriverInformation(api)
    
    Retrieves the driver information (if available) for a given graphics API.
    
    :param GraphicsAPI api: The API to get driver information for.
    :return: A :class:`DriverInformation` containing the driver information.
    :rtype: DriverInformation
    """
    pass

def GetLogFile(): # real signature unknown; restored from __doc__
    """
    GetLogFile()
    
    Gets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :return: The path to the current log file.
    :rtype: ``str``
    """
    pass

def GetLogFileContents(logfile): # real signature unknown; restored from __doc__
    """
    GetLogFileContents(logfile)
    
    Internal function for fetching the contents of a log
    """
    pass

def GetSupportedDeviceProtocols(): # real signature unknown; restored from __doc__
    """
    GetSupportedDeviceProtocols()
    
    Retrieve the set of device protocols supported (see :func:`GetDeviceProtocolController`).
    
    :return: The supported device protocols.
    :rtype: ``list`` of ``str``
    """
    pass

def GetVersionString(): # real signature unknown; restored from __doc__
    """
    GetVersionString()
    
    Retrieves the version string.
    
    This will be in the form "MAJOR.MINOR"
    
    :return: The version string.
    :rtype: ``str``
    """
    pass

def GPUVendorFromPCIVendor(vendorID): # real signature unknown; restored from __doc__
    """
    GPUVendorFromPCIVendor(vendorID)
    
    Get the GPUVendor for a given PCI Vendor ID.
    
    :param int vendorID: The PCI Vendor ID
    :return: The vendor identified
    :rtype: GPUVendor
    """
    pass

def HalfToFloat(half): # real signature unknown; restored from __doc__
    """
    HalfToFloat(half)
    
    A utility function that converts a half (stored in a 16-bit unsigned integer) to a
    float.
    
    :param int half: The half stored as an int.
    :return: The floating point equivalent.
    :rtype: ``float``
    """
    pass

def InitCamera(type): # real signature unknown; restored from __doc__
    """
    InitCamera(type)
    
    Create a new camera of a given type.
    
    :param CameraType type: The type of controls to use
    :return: The handle to the new camera.
    :rtype: Camera
    """
    pass

def InitGlobalEnv(env, args): # real signature unknown; restored from __doc__
    """
    InitGlobalEnv(env, args)
    
    Internal function for initialising global process environment in a replay program.
    """
    pass

def InjectIntoProcess(pid, env, capturefile, opts, waitForExit): # real signature unknown; restored from __doc__
    """
    InjectIntoProcess(pid, env, capturefile, opts, waitForExit)
    
    Where supported by operating system and permissions, inject into a running process.
    
    :param int pid: The Process ID (PID) to inject into.
    :param list env: Any :class:`EnvironmentModification` that should be made when running the program.
    :param str capturefile: The capture file path template, or blank to use a default location.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :param bool waitForExit: If ``True`` this function will block until the process exits.
    :return: The :class:`ExecuteResult` indicating both the status of the operation (success or failure)
      and any reason for failure, or else the ident where the new application is listening for target
      control if everything succeeded.
    :rtype: ExecuteResult
    """
    pass

def IsAMDCounter(c): # real signature unknown; restored from __doc__
    """
    IsAMDCounter(c)
    
    Check whether or not this is an AMD private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an AMD private counter, ``False`` if it's not.
    :rtype: ``bool``
    """
    pass

def IsD3D(api): # real signature unknown; restored from __doc__
    """
    IsD3D(api)
    
    Check if an API is D3D or not
    
    :param GraphicsAPI api: The graphics API in question
    :return: ``True`` if api is a D3D-based API, ``False`` otherwise
    """
    pass

def IsGenericCounter(c): # real signature unknown; restored from __doc__
    """
    IsGenericCounter(c)
    
    Check whether or not this is a Generic counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is a generic counter, ``False`` if it's not.
    :rtype: ``bool``
    """
    pass

def IsGlobalHookActive(): # real signature unknown; restored from __doc__
    """
    IsGlobalHookActive()
    
    Determines if the global hook is active or not.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`).
    
    :return: ``True`` if the hook is active, or ``False`` if the hook is inactive.
    :rtype: ``bool``
    """
    pass

def IsIntelCounter(c): # real signature unknown; restored from __doc__
    """
    IsIntelCounter(c)
    
    Check whether or not this is an Intel private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Intel private counter, ``False`` if it's not.
    :rtype: ``bool``
    """
    pass

def IsNvidiaCounter(c): # real signature unknown; restored from __doc__
    """
    IsNvidiaCounter(c)
    
    Check whether or not this is an Nvidia private counter.
    
    :param GPUCounter c: The counter.
    :return: ``True`` if it is an Nvidia private counter, ``False`` if it's not.
    :rtype: ``bool``
    """
    pass

def IsStrip(topology): # real signature unknown; restored from __doc__
    """
    IsStrip(topology)
    
    Check whether or not this is a strip-type topology.
    
    :param Topology t: The topology to check.
    :return: ``True`` if it describes a strip topology, ``False`` for a list.
    :rtype: ``bool``
    """
    pass

def IsTextRepresentation(encoding): # real signature unknown; restored from __doc__
    """
    IsTextRepresentation(encoding)
    
    Check whether or not this is a human readable text representation.
    
    :param ShaderEncoding e: The encoding to check.
    :return: ``True`` if it describes a text representation, ``False`` for a bytecode representation.
    :rtype: ``bool``
    """
    pass

def LogMessage(type, project, file, line, text): # real signature unknown; restored from __doc__
    """
    LogMessage(type, project, file, line, text)
    
    Internal function for logging messages in detail.
    """
    pass

def LogText(text): # real signature unknown; restored from __doc__
    """
    LogText(text)
    
    Internal function for logging text simply.
    """
    pass

def MakeDebuggablePackage(URL, packageAndActivity, progress): # real signature unknown; restored from __doc__
    """
    MakeDebuggablePackage(URL, packageAndActivity, progress)
    
    Internal function that attempts to modify APK contents, adding debuggable flag.
    """
    pass

def makeSDArray(name): # real signature unknown; restored from __doc__
    """
    makeSDArray(name)
    
    Make an array-type structured object
    """
    pass

def makeSDBool(name, val): # real signature unknown; restored from __doc__
    """
    makeSDBool(name, val)
    
    Make a structured object out of a boolean value
    """
    pass

def makeSDEnum(name, val): # real signature unknown; restored from __doc__
    """
    makeSDEnum(name, val)
    
    Make a structured object out of an enumeration value
    """
    pass

def makeSDFloat(name, val): # real signature unknown; restored from __doc__
    """
    makeSDFloat(name, val)
    
    Make a structured object out of a floating point value
    """
    pass

def makeSDInt32(name, val): # real signature unknown; restored from __doc__
    """
    makeSDInt32(name, val)
    
    Make a structured object out of a integer, stored as signed 32-bits
    """
    pass

def makeSDInt64(name, val): # real signature unknown; restored from __doc__
    """
    makeSDInt64(name, val)
    
    Make a structured object out of a signed integer
    """
    pass

def makeSDResourceId(name, val): # real signature unknown; restored from __doc__
    """
    makeSDResourceId(name, val)
    
    Make a structured object out of a ResourceId
    """
    pass

def makeSDString(name, val): # real signature unknown; restored from __doc__
    """
    makeSDString(name, val)
    
    Make a structured object out of a string
    """
    pass

def makeSDStruct(name, structtype): # real signature unknown; restored from __doc__
    """
    makeSDStruct(name, structtype)
    
    Make an struct-type structured object
    """
    pass

def makeSDUInt32(name, val): # real signature unknown; restored from __doc__
    """
    makeSDUInt32(name, val)
    
    Make a structured object out of a integer, stored as unsigned 32-bits
    """
    pass

def makeSDUInt64(name, val): # real signature unknown; restored from __doc__
    """
    makeSDUInt64(name, val)
    
    Make a structured object out of an unsigned integer
    """
    pass

def MaskForStage(stage): # real signature unknown; restored from __doc__
    """
    MaskForStage(stage)
    
    Calculate the corresponding flag for a shader stage
    
    :param ShaderStage stage: The shader stage
    :return: The flag that corresponds to the input shader stage
    :rtype: ShaderStageMask
    """
    pass

def NeedVulkanLayerRegistration(info): # real signature unknown; restored from __doc__
    """
    NeedVulkanLayerRegistration(info)
    
    Internal function for determining vulkan layer registration status.
    """
    pass

def NumVerticesPerPrimitive(topology): # real signature unknown; restored from __doc__
    """
    NumVerticesPerPrimitive(topology)
    
    A utility function that returns the number of vertices in a primitive of a given
    topology.
    
    .. note:: In strip topologies vertices are re-used.
    
    :param Topology topology: The topology to query about.
    :return: The number of vertices in a single primitive.
    :rtype: ``int``
    """
    pass

def OpenCaptureFile(): # real signature unknown; restored from __doc__
    """
    OpenCaptureFile()
    
    Create a handle for a capture file.
    
    This function returns a new handle to a capture file. Once initialised by opening a file the handle
    can only be shut-down, it is not re-usable.
    
    :return: A handle to the specified path.
    :rtype: CaptureFile
    """
    pass

def PatchList_Count(topology): # real signature unknown; restored from __doc__
    """
    PatchList_Count(topology)
    
    Return the number of control points in a patch list ``Topology``
    
    ``t`` must be a patch list topology, the return value will be between 1 and 32 inclusive
    
    :param Topology t: The patch list topology
    :return: The number of control points in the specified topology
    :rtype: ``int``
    """
    pass

def PatchList_Topology(N): # real signature unknown; restored from __doc__
    """
    PatchList_Topology(N)
    
    Return the patch list ``Topology`` with N control points
    
    ``N`` must be between 1 and 32 inclusive.
    
    :param int N: The number of control points in the patch list
    :return: The patchlist topology with that number of control points
    :rtype: Topology
    """
    pass

def RegisterMemoryRegion(base, size): # real signature unknown; restored from __doc__
    """
    RegisterMemoryRegion(base, size)
    
    Internal function for registering a memory region to be saved with crash dumps.
    """
    pass

def ResourceFormatName(fmt, name): # real signature unknown; restored from __doc__
    """
    ResourceFormatName(fmt, name)
    
    Internal function for getting the name for a resource format.
    """
    pass

def ResourceId_Null(): # real signature unknown; restored from __doc__
    """
    ResourceId_Null()
    
    A helper function that explicitly creates an empty/invalid/null :class:`ResourceId`.
    """
    pass

def ResUsage(stage): # real signature unknown; restored from __doc__
    """
    ResUsage(stage)
    
    Calculate the ``ResourceUsage`` value for read-only resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-only resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def RunFunctionalTests(pythonMinorVersion, args): # real signature unknown; restored from __doc__
    """
    RunFunctionalTests(pythonMinorVersion, args)
    
    Internal function that runs functional tests.
    """
    pass

def RunUnitTests(command, args): # real signature unknown; restored from __doc__
    """
    RunUnitTests(command, args)
    
    Internal function that runs unit tests.
    """
    pass

def RWResUsage(stage): # real signature unknown; restored from __doc__
    """
    RWResUsage(stage)
    
    Calculate the ``ResourceUsage`` value for read-write resource use at a given shader
    stage.
    
    :param ShaderStage stage: The shader stage.
    :return: The value for read-write resource usage at a given shader stage.
    :rtype: ResourceUsage
    """
    pass

def SetColors(darkChecker, lightChecker, darkTheme): # real signature unknown; restored from __doc__
    """
    SetColors(darkChecker, lightChecker, darkTheme)
    
    Internal function for setting UI theme colors.
    """
    pass

def SetConfigSetting(name, value): # real signature unknown; restored from __doc__
    """
    SetConfigSetting(name, value)
    
    Internal function for setting a config setting.
    """
    pass

def SetDebugLogFile(filename): # real signature unknown; restored from __doc__
    """
    SetDebugLogFile(filename)
    
    Sets the location for the diagnostic log output, shared by captured programs and the
    analysis program.
    
    :param str filename: The path to the new log file.
    """
    pass

def StartGlobalHook(pathmatch, logfile, opts): # real signature unknown; restored from __doc__
    """
    StartGlobalHook(pathmatch, logfile, opts)
    
    Begin injecting speculatively into all new processes started on the system. Where
    supported by platform, configuration, and setup begin injecting speculatively into all new processes
    started on the system.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is not active (see :func:`IsGlobalHookActive`).
    
    This function must be called when the process is running with administrator/superuser permissions.
    
    :param str pathmatch: A string to match against each new process's executable path to determine
      which corresponds to the program we actually want to capture.
    :param str logfile: Where to store any captures.
    :param CaptureOptions opts: The capture options to use when injecting into the program.
    :return: ``True`` if the hook is active, ``False`` if something went wrong. The hook must be closed
      with :func:`StopGlobalHook` before the application is closed.
    :rtype: ``bool``
    """
    pass

def StartSelfHostCapture(dllname): # real signature unknown; restored from __doc__
    """
    StartSelfHostCapture(dllname)
    
    When debugging RenderDoc it can be useful to capture itself by doing a side-build with a
    temporary name. This function wraps up the use of the in-application API to start a capture.
    
    :param str dllname: The name of the self-hosted capture module.
    """
    pass

def StopGlobalHook(): # real signature unknown; restored from __doc__
    """
    StopGlobalHook()
    
    Stop the global hook that was activated by :func:`StartGlobalHook`.
    
    This function can only be called if global hooking is supported (see :func:`CanGlobalHook`) and if
    global hooking is active (see :func:`IsGlobalHookActive`).
    """
    pass

def SupportsRestart(topology): # real signature unknown; restored from __doc__
    """
    SupportsRestart(topology)
    
    Check whether or not this topology supports primitive restart.
    
    .. note:: This is almost but not quite the same as being a line/triangle strip - triangle fans
      also support restart. See also :func:`IsStrip`.
    
    :param Topology t: The topology to check.
    :return: ``True`` if it describes a topology that allows restart, ``False`` for a list.
    :rtype: ``bool``
    """
    pass

def SWIG_PyInstanceMethod_New(*args, **kwargs): # real signature unknown
    pass

def UnregisterMemoryRegion(base): # real signature unknown; restored from __doc__
    """
    UnregisterMemoryRegion(base)
    
    Internal function for unregistering a memory region to be saved with crash dumps.
    """
    pass

def UpdateInstalledVersionNumber(): # real signature unknown; restored from __doc__
    """
    UpdateInstalledVersionNumber()
    
    Internal function for updating installed version number in windows registry.
    """
    pass

def UpdateVulkanLayerRegistration(systemLevel): # real signature unknown; restored from __doc__
    """
    UpdateVulkanLayerRegistration(systemLevel)
    
    Internal function for updating vulkan layer registration.
    """
    pass

def VertexOffset(topology, primitive): # real signature unknown; restored from __doc__
    """
    VertexOffset(topology, primitive)
    
    A utility function that returns the offset in the list of vertices of the first vertex
    in a particular primitive of a given topology. This calculation is simple but not trivial for the
    case of strip topologies.
    
    :param Topology topology: The topology to query about.
    :param int primitive: The primitive to query about.
    :return: The vertex offset where the primitive starts.
    :rtype: ``int``
    """
    pass

# classes

from .AddressMode import AddressMode
from .AlphaMapping import AlphaMapping
from .AndroidFlags import AndroidFlags
from .APIEvent import APIEvent
from .APIProperties import APIProperties
from .APIUseData import APIUseData
from .Bindpoint import Bindpoint
from .BindType import BindType
from .BlendEquation import BlendEquation
from .BlendMultiplier import BlendMultiplier
from .BlendOperation import BlendOperation
from .BlendStats import BlendStats
from .BoundCBuffer import BoundCBuffer
from .BoundResource import BoundResource
from .BoundResourceArray import BoundResourceArray
from .BoundVBuffer import BoundVBuffer
from .BucketRecordType import BucketRecordType
from .BufferCategory import BufferCategory
from .BufferDescription import BufferDescription
from .BusyData import BusyData
from .bytebuf import bytebuf
from .Camera import Camera
from .CameraType import CameraType
from .CaptureAccess import CaptureAccess
from .CaptureFile import CaptureFile
from .CaptureFileFormat import CaptureFileFormat
from .CaptureOptions import CaptureOptions
from .ColorBlend import ColorBlend
from .CompareFunction import CompareFunction
from .CompType import CompType
from .ConservativeRaster import ConservativeRaster
from .ConstantBindStats import ConstantBindStats
from .ConstantBlock import ConstantBlock
from .CounterDescription import CounterDescription
from .CounterResult import CounterResult
from .CounterUnit import CounterUnit
from .CounterValue import CounterValue
from .CullMode import CullMode
from .D3D11BlendState import D3D11BlendState
from .D3D11ConstantBuffer import D3D11ConstantBuffer
from .D3D11DepthStencilState import D3D11DepthStencilState
from .D3D11IndexBuffer import D3D11IndexBuffer
from .D3D11InputAssembly import D3D11InputAssembly
from .D3D11Layout import D3D11Layout
from .D3D11OutputMerger import D3D11OutputMerger
from .D3D11Predication import D3D11Predication
from .D3D11Rasterizer import D3D11Rasterizer
from .D3D11RasterizerState import D3D11RasterizerState
from .D3D11Sampler import D3D11Sampler
from .D3D11Shader import D3D11Shader
from .D3D11State import D3D11State
from .D3D11StreamOut import D3D11StreamOut
from .D3D11StreamOutBind import D3D11StreamOutBind
from .D3D11VertexBuffer import D3D11VertexBuffer
from .D3D11View import D3D11View
from .D3D12BlendState import D3D12BlendState
from .D3D12ConstantBuffer import D3D12ConstantBuffer
from .D3D12DepthStencilState import D3D12DepthStencilState
from .D3D12IndexBuffer import D3D12IndexBuffer
from .D3D12InputAssembly import D3D12InputAssembly
from .D3D12Layout import D3D12Layout
from .D3D12OM import D3D12OM
from .D3D12Rasterizer import D3D12Rasterizer
from .D3D12RasterizerState import D3D12RasterizerState
from .D3D12RegisterSpace import D3D12RegisterSpace
from .D3D12ResourceData import D3D12ResourceData
from .D3D12ResourceState import D3D12ResourceState
from .D3D12Sampler import D3D12Sampler
from .D3D12Shader import D3D12Shader
from .D3D12State import D3D12State
from .D3D12StreamOut import D3D12StreamOut
from .D3D12StreamOutBind import D3D12StreamOutBind
from .D3D12VertexBuffer import D3D12VertexBuffer
from .D3D12View import D3D12View
from .D3DBufferViewFlags import D3DBufferViewFlags
from .DebugMessage import DebugMessage
from .DebugOverlay import DebugOverlay
from .DepthStencilStats import DepthStencilStats
from .DeviceProtocolController import DeviceProtocolController
from .DispatchStats import DispatchStats
from .DoubleVecVal import DoubleVecVal
from .DrawcallDescription import DrawcallDescription
from .DrawcallStats import DrawcallStats
from .DrawFlags import DrawFlags
from .DriverInformation import DriverInformation
from .EnvironmentModification import EnvironmentModification
from .EnvMod import EnvMod
from .EnvSep import EnvSep
from .EventUsage import EventUsage
from .ExecuteResult import ExecuteResult
from .FileType import FileType
from .FillMode import FillMode
from .FilterFunction import FilterFunction
from .FilterMode import FilterMode
from .FloatVector import FloatVector
from .FloatVecVal import FloatVecVal
from .FrameDescription import FrameDescription
from .FrameStatistics import FrameStatistics
from .GLAttachment import GLAttachment
from .GLBlendState import GLBlendState
from .GLBuffer import GLBuffer
from .GLDepthState import GLDepthState
from .GLFBO import GLFBO
from .GLFeedback import GLFeedback
from .GLFixedVertexProcessing import GLFixedVertexProcessing
from .GLFrameBuffer import GLFrameBuffer
from .GLHints import GLHints
from .GLImageLoadStore import GLImageLoadStore
from .GlobalEnvironment import GlobalEnvironment
from .GLRasterizer import GLRasterizer
from .GLRasterizerState import GLRasterizerState
from .GLSampler import GLSampler
from .GLShader import GLShader
from .GLState import GLState
from .GLStencilState import GLStencilState
from .GLTexture import GLTexture
from .GLVertexAttribute import GLVertexAttribute
from .GLVertexBuffer import GLVertexBuffer
from .GLVertexInput import GLVertexInput
from .GPUCounter import GPUCounter
from .GPUDevice import GPUDevice
from .GPUVendor import GPUVendor
from .GraphicsAPI import GraphicsAPI
from .IndexBindStats import IndexBindStats
from .IntVecVal import IntVecVal
from .LayoutBindStats import LayoutBindStats
from .LineColumnInfo import LineColumnInfo
from .LineRaster import LineRaster
from .LocalVariableMapping import LocalVariableMapping
from .LogicOperation import LogicOperation
from .LogType import LogType
from .MeshDataStage import MeshDataStage
from .MeshDisplay import MeshDisplay
from .MeshFormat import MeshFormat
from .MessageCategory import MessageCategory
from .MessageSeverity import MessageSeverity
from .MessageSource import MessageSource
from .ModificationValue import ModificationValue
from .NewCaptureData import NewCaptureData
from .NewChildData import NewChildData
from .OutputTargetStats import OutputTargetStats
from .PathEntry import PathEntry
from .PathProperty import PathProperty
from .PipeState import PipeState
from .PixelModification import PixelModification
from .PixelValue import PixelValue
from .QualityHint import QualityHint
from .RasterizationStats import RasterizationStats
from .rdcarray_of_APIEvent import rdcarray_of_APIEvent
from .rdcarray_of_Bindpoint import rdcarray_of_Bindpoint
from .rdcarray_of_BoundResource import rdcarray_of_BoundResource
from .rdcarray_of_BoundResourceArray import rdcarray_of_BoundResourceArray
from .rdcarray_of_BoundVBuffer import rdcarray_of_BoundVBuffer
from .rdcarray_of_BufferDescription import rdcarray_of_BufferDescription
from .rdcarray_of_CaptureFileFormat import rdcarray_of_CaptureFileFormat
from .rdcarray_of_ColorBlend import rdcarray_of_ColorBlend
from .rdcarray_of_ConstantBlock import rdcarray_of_ConstantBlock
from .rdcarray_of_CounterResult import rdcarray_of_CounterResult
from .rdcarray_of_D3D11Pipe_ConstantBuffer import rdcarray_of_D3D11Pipe_ConstantBuffer
from .rdcarray_of_D3D11Pipe_Layout import rdcarray_of_D3D11Pipe_Layout
from .rdcarray_of_D3D11Pipe_Sampler import rdcarray_of_D3D11Pipe_Sampler
from .rdcarray_of_D3D11Pipe_StreamOutBind import rdcarray_of_D3D11Pipe_StreamOutBind
from .rdcarray_of_D3D11Pipe_VertexBuffer import rdcarray_of_D3D11Pipe_VertexBuffer
from .rdcarray_of_D3D11Pipe_View import rdcarray_of_D3D11Pipe_View
from .rdcarray_of_D3D12Pipe_ConstantBuffer import rdcarray_of_D3D12Pipe_ConstantBuffer
from .rdcarray_of_D3D12Pipe_Layout import rdcarray_of_D3D12Pipe_Layout
from .rdcarray_of_D3D12Pipe_RegisterSpace import rdcarray_of_D3D12Pipe_RegisterSpace
from .rdcarray_of_D3D12Pipe_ResourceData import rdcarray_of_D3D12Pipe_ResourceData
from .rdcarray_of_D3D12Pipe_ResourceState import rdcarray_of_D3D12Pipe_ResourceState
from .rdcarray_of_D3D12Pipe_Sampler import rdcarray_of_D3D12Pipe_Sampler
from .rdcarray_of_D3D12Pipe_StreamOutBind import rdcarray_of_D3D12Pipe_StreamOutBind
from .rdcarray_of_D3D12Pipe_VertexBuffer import rdcarray_of_D3D12Pipe_VertexBuffer
from .rdcarray_of_D3D12Pipe_View import rdcarray_of_D3D12Pipe_View
from .rdcarray_of_DebugMessage import rdcarray_of_DebugMessage
from .rdcarray_of_DrawcallDescription import rdcarray_of_DrawcallDescription
from .rdcarray_of_EnvironmentModification import rdcarray_of_EnvironmentModification
from .rdcarray_of_EventUsage import rdcarray_of_EventUsage
from .rdcarray_of_float import rdcarray_of_float
from .rdcarray_of_FloatVector import rdcarray_of_FloatVector
from .rdcarray_of_GLPipe_Attachment import rdcarray_of_GLPipe_Attachment
from .rdcarray_of_GLPipe_Buffer import rdcarray_of_GLPipe_Buffer
from .rdcarray_of_GLPipe_ImageLoadStore import rdcarray_of_GLPipe_ImageLoadStore
from .rdcarray_of_GLPipe_Sampler import rdcarray_of_GLPipe_Sampler
from .rdcarray_of_GLPipe_Texture import rdcarray_of_GLPipe_Texture
from .rdcarray_of_GLPipe_VertexAttribute import rdcarray_of_GLPipe_VertexAttribute
from .rdcarray_of_GLPipe_VertexBuffer import rdcarray_of_GLPipe_VertexBuffer
from .rdcarray_of_GPUCounter import rdcarray_of_GPUCounter
from .rdcarray_of_GPUDevice import rdcarray_of_GPUDevice
from .rdcarray_of_GraphicsAPI import rdcarray_of_GraphicsAPI
from .rdcarray_of_int import rdcarray_of_int
from .rdcarray_of_LineColumnInfo import rdcarray_of_LineColumnInfo
from .rdcarray_of_LocalVariableMapping import rdcarray_of_LocalVariableMapping
from .rdcarray_of_PathEntry import rdcarray_of_PathEntry
from .rdcarray_of_PixelModification import rdcarray_of_PixelModification
from .rdcarray_of_rdcstr import rdcarray_of_rdcstr
from .rdcarray_of_RegisterRange import rdcarray_of_RegisterRange
from .rdcarray_of_ResourceDescription import rdcarray_of_ResourceDescription
from .rdcarray_of_ResourceId import rdcarray_of_ResourceId
from .rdcarray_of_Scissor import rdcarray_of_Scissor
from .rdcarray_of_ShaderCompileFlag import rdcarray_of_ShaderCompileFlag
from .rdcarray_of_ShaderConstant import rdcarray_of_ShaderConstant
from .rdcarray_of_ShaderDebugState import rdcarray_of_ShaderDebugState
from .rdcarray_of_ShaderEncoding import rdcarray_of_ShaderEncoding
from .rdcarray_of_ShaderEntryPoint import rdcarray_of_ShaderEntryPoint
from .rdcarray_of_ShaderResource import rdcarray_of_ShaderResource
from .rdcarray_of_ShaderSampler import rdcarray_of_ShaderSampler
from .rdcarray_of_ShaderSourceFile import rdcarray_of_ShaderSourceFile
from .rdcarray_of_ShaderVariable import rdcarray_of_ShaderVariable
from .rdcarray_of_SigParameter import rdcarray_of_SigParameter
from .rdcarray_of_TextureDescription import rdcarray_of_TextureDescription
from .rdcarray_of_uint32_t import rdcarray_of_uint32_t
from .rdcarray_of_uint64_t import rdcarray_of_uint64_t
from .rdcarray_of_VertexInputAttribute import rdcarray_of_VertexInputAttribute
from .rdcarray_of_Viewport import rdcarray_of_Viewport
from .rdcarray_of_VKPipe_Attachment import rdcarray_of_VKPipe_Attachment
from .rdcarray_of_VKPipe_BindingElement import rdcarray_of_VKPipe_BindingElement
from .rdcarray_of_VKPipe_DescriptorBinding import rdcarray_of_VKPipe_DescriptorBinding
from .rdcarray_of_VKPipe_DescriptorSet import rdcarray_of_VKPipe_DescriptorSet
from .rdcarray_of_VKPipe_ImageData import rdcarray_of_VKPipe_ImageData
from .rdcarray_of_VKPipe_ImageLayout import rdcarray_of_VKPipe_ImageLayout
from .rdcarray_of_VKPipe_RenderArea import rdcarray_of_VKPipe_RenderArea
from .rdcarray_of_VKPipe_SpecializationConstant import rdcarray_of_VKPipe_SpecializationConstant
from .rdcarray_of_VKPipe_VertexAttribute import rdcarray_of_VKPipe_VertexAttribute
from .rdcarray_of_VKPipe_VertexBinding import rdcarray_of_VKPipe_VertexBinding
from .rdcarray_of_VKPipe_VertexBuffer import rdcarray_of_VKPipe_VertexBuffer
from .rdcarray_of_VKPipe_ViewportScissor import rdcarray_of_VKPipe_ViewportScissor
from .rdcarray_of_VKPipe_XFBBuffer import rdcarray_of_VKPipe_XFBBuffer
from .rdcarray_of_WindowingSystem import rdcarray_of_WindowingSystem
from .RegisterRange import RegisterRange
from .RegisterType import RegisterType
from .RemoteServer import RemoteServer
from .ReplayController import ReplayController
from .ReplayOptimisationLevel import ReplayOptimisationLevel
from .ReplayOptions import ReplayOptions
from .ReplayOutput import ReplayOutput
from .ReplayOutputType import ReplayOutputType
from .ReplayStatus import ReplayStatus
from .ReplaySupport import ReplaySupport
from .ResourceBindStats import ResourceBindStats
from .ResourceDescription import ResourceDescription
from .ResourceFormat import ResourceFormat
from .ResourceFormatType import ResourceFormatType
from .ResourceId import ResourceId
from .ResourceType import ResourceType
from .ResourceUpdateStats import ResourceUpdateStats
from .ResourceUsage import ResourceUsage
from .SamplerBindStats import SamplerBindStats
from .Scissor import Scissor
from .SDBasic import SDBasic
from .SDObject import SDObject
from .SDChunk import SDChunk
from .SDChunkFlags import SDChunkFlags
from .SDChunkMetaData import SDChunkMetaData
from .SDFile import SDFile
from .SDObjectData import SDObjectData
from .SDObjectPODData import SDObjectPODData
from .SDType import SDType
from .SDTypeFlags import SDTypeFlags
from .SectionFlags import SectionFlags
from .SectionProperties import SectionProperties
from .SectionType import SectionType
from .ShaderBindpointMapping import ShaderBindpointMapping
from .ShaderBuiltin import ShaderBuiltin
from .ShaderChangeStats import ShaderChangeStats
from .ShaderCompileFlag import ShaderCompileFlag
from .ShaderCompileFlags import ShaderCompileFlags
from .ShaderConstant import ShaderConstant
from .ShaderDebugInfo import ShaderDebugInfo
from .ShaderDebugState import ShaderDebugState
from .ShaderDebugTrace import ShaderDebugTrace
from .ShaderEncoding import ShaderEncoding
from .ShaderEntryPoint import ShaderEntryPoint
from .ShaderEvents import ShaderEvents
from .ShaderReflection import ShaderReflection
from .ShaderResource import ShaderResource
from .ShaderSampler import ShaderSampler
from .ShaderSourceFile import ShaderSourceFile
from .ShaderStage import ShaderStage
from .ShaderStageMask import ShaderStageMask
from .ShaderValue import ShaderValue
from .ShaderVariable import ShaderVariable
from .ShaderVariableDescriptor import ShaderVariableDescriptor
from .ShaderVariableType import ShaderVariableType
from .SigParameter import SigParameter
from .SolidShade import SolidShade
from .StencilFace import StencilFace
from .StencilOperation import StencilOperation
from .StructuredBufferList import StructuredBufferList
from .StructuredChunkList import StructuredChunkList
from .StructuredObjectList import StructuredObjectList
from .TargetControl import TargetControl
from .TargetControlMessage import TargetControlMessage
from .TargetControlMessageType import TargetControlMessageType
from .TextureCategory import TextureCategory
from .TextureComponentMapping import TextureComponentMapping
from .TextureDescription import TextureDescription
from .TextureDisplay import TextureDisplay
from .TextureFilter import TextureFilter
from .TextureSampleMapping import TextureSampleMapping
from .TextureSave import TextureSave
from .TextureSliceMapping import TextureSliceMapping
from .TextureSwizzle import TextureSwizzle
from .TextureType import TextureType
from .Thumbnail import Thumbnail
from .Topology import Topology
from .UIntVecVal import UIntVecVal
from .Uuid import Uuid
from .VarType import VarType
from .VertexBindStats import VertexBindStats
from .VertexInputAttribute import VertexInputAttribute
from .Viewport import Viewport
from .VKAttachment import VKAttachment
from .VKBindingElement import VKBindingElement
from .VKColorBlendState import VKColorBlendState
from .VKConditionalRendering import VKConditionalRendering
from .VKCurrentPass import VKCurrentPass
from .VKDepthStencil import VKDepthStencil
from .VKDescriptorBinding import VKDescriptorBinding
from .VKDescriptorSet import VKDescriptorSet
from .VKFramebuffer import VKFramebuffer
from .VKImageData import VKImageData
from .VKImageLayout import VKImageLayout
from .VKIndexBuffer import VKIndexBuffer
from .VKInputAssembly import VKInputAssembly
from .VKMultiSample import VKMultiSample
from .VKPipeline import VKPipeline
from .VKRasterizer import VKRasterizer
from .VKRenderArea import VKRenderArea
from .VKRenderPass import VKRenderPass
from .VKSampleLocations import VKSampleLocations
from .VKShader import VKShader
from .VKSpecializationConstant import VKSpecializationConstant
from .VKState import VKState
from .VKTessellation import VKTessellation
from .VKTransformFeedback import VKTransformFeedback
from .VKVertexAttribute import VKVertexAttribute
from .VKVertexBinding import VKVertexBinding
from .VKVertexBuffer import VKVertexBuffer
from .VKVertexInput import VKVertexInput
from .VKViewportScissor import VKViewportScissor
from .VKViewState import VKViewState
from .VKXFBBuffer import VKXFBBuffer
from .VulkanLayerFlags import VulkanLayerFlags
from .VulkanLayerRegistrationInfo import VulkanLayerRegistrationInfo
from .WindowingData import WindowingData
from .WindowingSystem import WindowingSystem
# variables with complex values

__all__ = [
    'SWIG_PyInstanceMethod_New',
    'FreeArrayMem',
    'AllocArrayMem',
    'ResourceId_Null',
    'CreateHeadlessWindowingData',
    'CreateWin32WindowingData',
    'CreateXlibWindowingData',
    'CreateXCBWindowingData',
    'CreateWaylandWindowingData',
    'CreateGgpWindowingData',
    'CreateAndroidWindowingData',
    'CreateMacOSWindowingData',
    'InitCamera',
    'HalfToFloat',
    'FloatToHalf',
    'NumVerticesPerPrimitive',
    'VertexOffset',
    'OpenCaptureFile',
    'CreateTargetControl',
    'EnumerateRemoteTargets',
    'CreateRemoteServerConnection',
    'BecomeRemoteServer',
    'GetDefaultCaptureOptions',
    'StartGlobalHook',
    'StopGlobalHook',
    'IsGlobalHookActive',
    'CanGlobalHook',
    'ExecuteAndInject',
    'InjectIntoProcess',
    'StartSelfHostCapture',
    'EndSelfHostCapture',
    'NeedVulkanLayerRegistration',
    'UpdateVulkanLayerRegistration',
    'UpdateInstalledVersionNumber',
    'InitGlobalEnv',
    'CreateBugReport',
    'RegisterMemoryRegion',
    'UnregisterMemoryRegion',
    'SetDebugLogFile',
    'GetLogFile',
    'GetLogFileContents',
    'LogText',
    'LogMessage',
    'GetVersionString',
    'GetCommitHash',
    'GetDriverInformation',
    'GetCurrentProcessMemoryUsage',
    'GetConfigSetting',
    'SetConfigSetting',
    'SetColors',
    'CheckAndroidPackage',
    'MakeDebuggablePackage',
    'GetSupportedDeviceProtocols',
    'GetDeviceProtocolController',
    'RunUnitTests',
    'RunFunctionalTests',
    'makeSDInt64',
    'makeSDUInt64',
    'makeSDInt32',
    'makeSDUInt32',
    'makeSDFloat',
    'makeSDBool',
    'makeSDString',
    'makeSDResourceId',
    'makeSDEnum',
    'makeSDArray',
    'makeSDStruct',
    'ResourceFormatName',
    'GPUVendorFromPCIVendor',
    'IsD3D',
    'IsTextRepresentation',
    'PatchList_Topology',
    'PatchList_Count',
    'SupportsRestart',
    'IsStrip',
    'CBUsage',
    'ResUsage',
    'RWResUsage',
    'IsGenericCounter',
    'IsAMDCounter',
    'IsIntelCounter',
    'IsNvidiaCounter',
    'MaskForStage',
    'ResourceId',
    'WindowingSystem',
    'WindowingData',
    'GlobalEnvironment',
    'ExecuteResult',
    'ReplayOutput',
    'ReplayController',
    'TargetControl',
    'CaptureAccess',
    'RemoteServer',
    'CaptureFile',
    'Camera',
    'VulkanLayerRegistrationInfo',
    'DeviceProtocolController',
    'bytebuf',
    'SDBasic',
    'SDTypeFlags',
    'SDType',
    'SDChunkFlags',
    'SDChunkMetaData',
    'SDObjectPODData',
    'StructuredObjectList',
    'SDObjectData',
    'SDObject',
    'SDChunk',
    'StructuredChunkList',
    'StructuredBufferList',
    'SDFile',
    'CaptureOptions',
    'MeshFormat',
    'MeshDisplay',
    'TextureDisplay',
    'TextureComponentMapping',
    'TextureSampleMapping',
    'TextureSliceMapping',
    'TextureSave',
    'NewCaptureData',
    'APIUseData',
    'BusyData',
    'NewChildData',
    'TargetControlMessage',
    'EnvironmentModification',
    'CaptureFileFormat',
    'GPUDevice',
    'ReplayOptions',
    'Viewport',
    'Scissor',
    'BlendEquation',
    'ColorBlend',
    'StencilFace',
    'BoundResource',
    'BoundResourceArray',
    'BoundVBuffer',
    'BoundCBuffer',
    'VertexInputAttribute',
    'D3D11Layout',
    'D3D11VertexBuffer',
    'D3D11IndexBuffer',
    'D3D11InputAssembly',
    'D3D11View',
    'D3D11Sampler',
    'D3D11ConstantBuffer',
    'D3D11Shader',
    'D3D11StreamOutBind',
    'D3D11StreamOut',
    'D3D11RasterizerState',
    'D3D11Rasterizer',
    'D3D11DepthStencilState',
    'D3D11BlendState',
    'D3D11OutputMerger',
    'D3D11Predication',
    'D3D11State',
    'D3D12Layout',
    'D3D12VertexBuffer',
    'D3D12IndexBuffer',
    'D3D12InputAssembly',
    'D3D12View',
    'D3D12Sampler',
    'D3D12ConstantBuffer',
    'D3D12RegisterSpace',
    'D3D12Shader',
    'D3D12StreamOutBind',
    'D3D12StreamOut',
    'D3D12RasterizerState',
    'D3D12Rasterizer',
    'D3D12DepthStencilState',
    'D3D12BlendState',
    'D3D12OM',
    'D3D12ResourceState',
    'D3D12ResourceData',
    'D3D12State',
    'FloatVector',
    'PathEntry',
    'SectionProperties',
    'ResourceFormat',
    'TextureFilter',
    'ResourceDescription',
    'BufferDescription',
    'TextureDescription',
    'APIEvent',
    'DebugMessage',
    'BucketRecordType',
    'ConstantBindStats',
    'SamplerBindStats',
    'ResourceBindStats',
    'ResourceUpdateStats',
    'DrawcallStats',
    'DispatchStats',
    'IndexBindStats',
    'VertexBindStats',
    'LayoutBindStats',
    'ShaderChangeStats',
    'BlendStats',
    'DepthStencilStats',
    'RasterizationStats',
    'OutputTargetStats',
    'FrameStatistics',
    'FrameDescription',
    'EventUsage',
    'DrawcallDescription',
    'APIProperties',
    'DriverInformation',
    'Uuid',
    'CounterDescription',
    'CounterValue',
    'CounterResult',
    'PixelValue',
    'ModificationValue',
    'PixelModification',
    'Thumbnail',
    'GLVertexAttribute',
    'GLVertexBuffer',
    'GLVertexInput',
    'GLShader',
    'GLFixedVertexProcessing',
    'GLTexture',
    'GLSampler',
    'GLBuffer',
    'GLImageLoadStore',
    'GLFeedback',
    'GLRasterizerState',
    'GLRasterizer',
    'GLDepthState',
    'GLStencilState',
    'GLAttachment',
    'GLFBO',
    'GLBlendState',
    'GLFrameBuffer',
    'GLHints',
    'GLState',
    'SectionType',
    'RegisterType',
    'VarType',
    'CompType',
    'TextureSwizzle',
    'AddressMode',
    'Raw',
    'RangeOnly',
    'BT709',
    'BT601',
    'BT2020',
    'ITUFull',
    'ITUNarrow',
    'CositedEven',
    'Midpoint',
    'ResourceType',
    'TextureType',
    'BindType',
    'ShaderBuiltin',
    'ReplayOutputType',
    'MeshDataStage',
    'DebugOverlay',
    'FileType',
    'AlphaMapping',
    'ResourceFormatType',
    'QualityHint',
    'GPUVendor',
    'GraphicsAPI',
    'ShaderEncoding',
    'Topology',
    'ShaderStage',
    'MessageCategory',
    'MessageSeverity',
    'MessageSource',
    'ResourceUsage',
    'SolidShade',
    'FillMode',
    'CullMode',
    'ConservativeRaster',
    'LineRaster',
    'FilterMode',
    'FilterFunction',
    'CompareFunction',
    'StencilOperation',
    'BlendMultiplier',
    'BlendOperation',
    'LogicOperation',
    'GPUCounter',
    'CounterUnit',
    'CameraType',
    'ReplaySupport',
    'ReplayStatus',
    'TargetControlMessageType',
    'EnvMod',
    'EnvSep',
    'LogType',
    'ReplayOptimisationLevel',
    'PathProperty',
    'SectionFlags',
    'BufferCategory',
    'D3DBufferViewFlags',
    'TextureCategory',
    'ShaderStageMask',
    'ShaderEvents',
    'DrawFlags',
    'VulkanLayerFlags',
    'AndroidFlags',
    'FloatVecVal',
    'DoubleVecVal',
    'IntVecVal',
    'UIntVecVal',
    'ShaderValue',
    'ShaderVariable',
    'RegisterRange',
    'LocalVariableMapping',
    'LineColumnInfo',
    'ShaderDebugState',
    'ShaderDebugTrace',
    'SigParameter',
    'ShaderVariableDescriptor',
    'ShaderVariableType',
    'ShaderConstant',
    'ConstantBlock',
    'ShaderSampler',
    'ShaderResource',
    'ShaderEntryPoint',
    'ShaderCompileFlag',
    'ShaderCompileFlags',
    'ShaderSourceFile',
    'ShaderDebugInfo',
    'ShaderReflection',
    'Bindpoint',
    'ShaderBindpointMapping',
    'VKBindingElement',
    'VKDescriptorBinding',
    'VKDescriptorSet',
    'VKPipeline',
    'VKIndexBuffer',
    'VKInputAssembly',
    'VKVertexAttribute',
    'VKVertexBinding',
    'VKVertexBuffer',
    'VKVertexInput',
    'VKSpecializationConstant',
    'VKShader',
    'VKTessellation',
    'VKXFBBuffer',
    'VKTransformFeedback',
    'VKRenderArea',
    'VKViewportScissor',
    'VKViewState',
    'VKRasterizer',
    'VKSampleLocations',
    'VKMultiSample',
    'VKColorBlendState',
    'VKDepthStencil',
    'VKRenderPass',
    'VKAttachment',
    'VKFramebuffer',
    'VKCurrentPass',
    'VKImageLayout',
    'VKImageData',
    'VKConditionalRendering',
    'VKState',
    'PipeState',
    'rdcarray_of_int',
    'rdcarray_of_float',
    'rdcarray_of_uint32_t',
    'rdcarray_of_uint64_t',
    'rdcarray_of_rdcstr',
    'rdcarray_of_WindowingSystem',
    'rdcarray_of_DrawcallDescription',
    'rdcarray_of_GPUCounter',
    'rdcarray_of_CounterResult',
    'rdcarray_of_APIEvent',
    'rdcarray_of_Bindpoint',
    'rdcarray_of_BufferDescription',
    'rdcarray_of_CaptureFileFormat',
    'rdcarray_of_ConstantBlock',
    'rdcarray_of_DebugMessage',
    'rdcarray_of_EnvironmentModification',
    'rdcarray_of_EventUsage',
    'rdcarray_of_PathEntry',
    'rdcarray_of_PixelModification',
    'rdcarray_of_ResourceDescription',
    'rdcarray_of_ResourceId',
    'rdcarray_of_LineColumnInfo',
    'rdcarray_of_ShaderCompileFlag',
    'rdcarray_of_ShaderConstant',
    'rdcarray_of_ShaderDebugState',
    'rdcarray_of_ShaderResource',
    'rdcarray_of_ShaderSampler',
    'rdcarray_of_ShaderSourceFile',
    'rdcarray_of_ShaderVariable',
    'rdcarray_of_ShaderEncoding',
    'rdcarray_of_RegisterRange',
    'rdcarray_of_LocalVariableMapping',
    'rdcarray_of_SigParameter',
    'rdcarray_of_TextureDescription',
    'rdcarray_of_ShaderEntryPoint',
    'rdcarray_of_Viewport',
    'rdcarray_of_Scissor',
    'rdcarray_of_ColorBlend',
    'rdcarray_of_BoundVBuffer',
    'rdcarray_of_VertexInputAttribute',
    'rdcarray_of_BoundResource',
    'rdcarray_of_BoundResourceArray',
    'rdcarray_of_FloatVector',
    'rdcarray_of_GraphicsAPI',
    'rdcarray_of_GPUDevice',
    'rdcarray_of_VKPipe_Attachment',
    'rdcarray_of_VKPipe_BindingElement',
    'rdcarray_of_VKPipe_DescriptorBinding',
    'rdcarray_of_VKPipe_DescriptorSet',
    'rdcarray_of_VKPipe_ImageData',
    'rdcarray_of_VKPipe_ImageLayout',
    'rdcarray_of_VKPipe_RenderArea',
    'rdcarray_of_VKPipe_SpecializationConstant',
    'rdcarray_of_VKPipe_XFBBuffer',
    'rdcarray_of_VKPipe_VertexBuffer',
    'rdcarray_of_VKPipe_VertexAttribute',
    'rdcarray_of_VKPipe_VertexBinding',
    'rdcarray_of_VKPipe_ViewportScissor',
    'rdcarray_of_D3D11Pipe_ConstantBuffer',
    'rdcarray_of_D3D11Pipe_Layout',
    'rdcarray_of_D3D11Pipe_Sampler',
    'rdcarray_of_D3D11Pipe_StreamOutBind',
    'rdcarray_of_D3D11Pipe_VertexBuffer',
    'rdcarray_of_D3D11Pipe_View',
    'rdcarray_of_D3D12Pipe_ConstantBuffer',
    'rdcarray_of_D3D12Pipe_Layout',
    'rdcarray_of_D3D12Pipe_RegisterSpace',
    'rdcarray_of_D3D12Pipe_ResourceData',
    'rdcarray_of_D3D12Pipe_ResourceState',
    'rdcarray_of_D3D12Pipe_Sampler',
    'rdcarray_of_D3D12Pipe_StreamOutBind',
    'rdcarray_of_D3D12Pipe_VertexBuffer',
    'rdcarray_of_D3D12Pipe_View',
    'rdcarray_of_GLPipe_Attachment',
    'rdcarray_of_GLPipe_Buffer',
    'rdcarray_of_GLPipe_ImageLoadStore',
    'rdcarray_of_GLPipe_Sampler',
    'rdcarray_of_GLPipe_Texture',
    'rdcarray_of_GLPipe_VertexBuffer',
    'rdcarray_of_GLPipe_VertexAttribute',
]

__loader__ = None # (!) real value is ''

__spec__ = None # (!) real value is ''

