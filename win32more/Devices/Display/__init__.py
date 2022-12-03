from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Devices.Display
import win32more.Devices.Properties
import win32more.Foundation
import win32more.Graphics.Direct3D9
import win32more.Graphics.DirectDraw
import win32more.Graphics.Gdi
import win32more.Graphics.OpenGL
import win32more.System.Com
import win32more.System.Console
import win32more.UI.ColorSystem
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        f = globals()[f'_define_{name}']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, f())
    return getattr(_module, name)
def __dir__():
    return __all__
def _define_Adapter_head():
    class Adapter(Structure):
        pass
    return Adapter
def _define_Adapter():
    Adapter = win32more.Devices.Display.Adapter_head
    Adapter._fields_ = [
        ('AdapterName', Char * 128),
        ('numSources', Int32),
        ('sources', win32more.Devices.Display.Sources * 1),
    ]
    return Adapter
def _define_Adapters_head():
    class Adapters(Structure):
        pass
    return Adapters
def _define_Adapters():
    Adapters = win32more.Devices.Display.Adapters_head
    Adapters._fields_ = [
        ('numAdapters', Int32),
        ('adapter', win32more.Devices.Display.Adapter * 1),
    ]
    return Adapters
def _define_GUID_DEVINTERFACE_DISPLAY_ADAPTER():
    return Guid('5b45201d-f2f2-4f3b-85-bb-30-ff-1f-95-35-99')
def _define_GUID_DEVINTERFACE_MONITOR():
    return Guid('e6f07b5f-ee97-4a90-b0-76-33-f5-7b-f4-ea-a7')
def _define_GUID_DISPLAY_DEVICE_ARRIVAL():
    return Guid('1ca05180-a699-450a-9a-0c-de-4f-be-3d-dd-89')
def _define_GUID_DEVINTERFACE_VIDEO_OUTPUT_ARRIVAL():
    return Guid('1ad9e4f0-f88d-4360-ba-b9-4c-2d-55-e5-64-cd')
def _define_DEVPKEY_IndirectDisplay():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('c50a3f10-aa5c-4247-b8-30-d6-a6-f8-ea-a3-10'), pid=1)
def _define_DEVPKEY_Device_TerminalLuid():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('c50a3f10-aa5c-4247-b8-30-d6-a6-f8-ea-a3-10'), pid=2)
def _define_DEVPKEY_Device_AdapterLuid():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('c50a3f10-aa5c-4247-b8-30-d6-a6-f8-ea-a3-10'), pid=3)
def _define_DEVPKEY_Device_ActivityId():
    return win32more.Devices.Properties.DEVPROPKEY(fmtid=Guid('c50a3f10-aa5c-4247-b8-30-d6-a6-f8-ea-a3-10'), pid=4)
INDIRECT_DISPLAY_INFO_FLAGS_CREATED_IDDCX_ADAPTER = 1
VIDEO_DEVICE_NAME = 'DISPLAY%d'
WVIDEO_DEVICE_NAME = 'DISPLAY%d'
IOCTL_VIDEO_DISABLE_VDM = 2293764
IOCTL_VIDEO_REGISTER_VDM = 2293768
IOCTL_VIDEO_SET_OUTPUT_DEVICE_POWER_STATE = 2293772
IOCTL_VIDEO_GET_OUTPUT_DEVICE_POWER_STATE = 2293776
IOCTL_VIDEO_MONITOR_DEVICE = 2293780
IOCTL_VIDEO_ENUM_MONITOR_PDO = 2293784
IOCTL_VIDEO_INIT_WIN32K_CALLBACKS = 2293788
IOCTL_VIDEO_IS_VGA_DEVICE = 2293796
IOCTL_VIDEO_USE_DEVICE_IN_SESSION = 2293800
IOCTL_VIDEO_PREPARE_FOR_EARECOVERY = 2293804
IOCTL_VIDEO_ENABLE_VDM = 2293760
IOCTL_VIDEO_SAVE_HARDWARE_STATE = 2294272
IOCTL_VIDEO_RESTORE_HARDWARE_STATE = 2294276
IOCTL_VIDEO_HANDLE_VIDEOPARAMETERS = 2293792
IOCTL_VIDEO_QUERY_AVAIL_MODES = 2294784
IOCTL_VIDEO_QUERY_NUM_AVAIL_MODES = 2294788
IOCTL_VIDEO_QUERY_CURRENT_MODE = 2294792
IOCTL_VIDEO_SET_CURRENT_MODE = 2294796
IOCTL_VIDEO_RESET_DEVICE = 2294800
IOCTL_VIDEO_LOAD_AND_SET_FONT = 2294804
IOCTL_VIDEO_SET_PALETTE_REGISTERS = 2294808
IOCTL_VIDEO_SET_COLOR_REGISTERS = 2294812
IOCTL_VIDEO_ENABLE_CURSOR = 2294816
IOCTL_VIDEO_DISABLE_CURSOR = 2294820
IOCTL_VIDEO_SET_CURSOR_ATTR = 2294824
IOCTL_VIDEO_QUERY_CURSOR_ATTR = 2294828
IOCTL_VIDEO_SET_CURSOR_POSITION = 2294832
IOCTL_VIDEO_QUERY_CURSOR_POSITION = 2294836
IOCTL_VIDEO_ENABLE_POINTER = 2294840
IOCTL_VIDEO_DISABLE_POINTER = 2294844
IOCTL_VIDEO_SET_POINTER_ATTR = 2294848
IOCTL_VIDEO_QUERY_POINTER_ATTR = 2294852
IOCTL_VIDEO_SET_POINTER_POSITION = 2294856
IOCTL_VIDEO_QUERY_POINTER_POSITION = 2294860
IOCTL_VIDEO_QUERY_POINTER_CAPABILITIES = 2294864
IOCTL_VIDEO_GET_BANK_SELECT_CODE = 2294868
IOCTL_VIDEO_MAP_VIDEO_MEMORY = 2294872
IOCTL_VIDEO_UNMAP_VIDEO_MEMORY = 2294876
IOCTL_VIDEO_QUERY_PUBLIC_ACCESS_RANGES = 2294880
IOCTL_VIDEO_FREE_PUBLIC_ACCESS_RANGES = 2294884
IOCTL_VIDEO_QUERY_COLOR_CAPABILITIES = 2294888
IOCTL_VIDEO_SET_POWER_MANAGEMENT = 2294892
IOCTL_VIDEO_GET_POWER_MANAGEMENT = 2294896
IOCTL_VIDEO_SHARE_VIDEO_MEMORY = 2294900
IOCTL_VIDEO_UNSHARE_VIDEO_MEMORY = 2294904
IOCTL_VIDEO_SET_COLOR_LUT_DATA = 2294908
IOCTL_VIDEO_GET_CHILD_STATE = 2294912
IOCTL_VIDEO_VALIDATE_CHILD_STATE_CONFIGURATION = 2294916
IOCTL_VIDEO_SET_CHILD_STATE_CONFIGURATION = 2294920
IOCTL_VIDEO_SWITCH_DUALVIEW = 2294924
IOCTL_VIDEO_SET_BANK_POSITION = 2294928
IOCTL_VIDEO_QUERY_SUPPORTED_BRIGHTNESS = 2294932
IOCTL_VIDEO_QUERY_DISPLAY_BRIGHTNESS = 2294936
IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS = 2294940
IOCTL_FSVIDEO_COPY_FRAME_BUFFER = 3409920
IOCTL_FSVIDEO_WRITE_TO_FRAME_BUFFER = 3409924
IOCTL_FSVIDEO_REVERSE_MOUSE_POINTER = 3409928
IOCTL_FSVIDEO_SET_CURRENT_MODE = 3409932
IOCTL_FSVIDEO_SET_SCREEN_INFORMATION = 3409936
IOCTL_FSVIDEO_SET_CURSOR_POSITION = 3409940
IOCTL_PANEL_QUERY_BRIGHTNESS_CAPS = 2296832
IOCTL_PANEL_QUERY_BRIGHTNESS_RANGES = 2296836
IOCTL_PANEL_GET_BRIGHTNESS = 2296840
IOCTL_PANEL_SET_BRIGHTNESS = 2296844
IOCTL_PANEL_SET_BRIGHTNESS_STATE = 2296848
IOCTL_PANEL_SET_BACKLIGHT_OPTIMIZATION = 2296852
IOCTL_PANEL_GET_BACKLIGHT_REDUCTION = 2296856
IOCTL_COLORSPACE_TRANSFORM_QUERY_TARGET_CAPS = 2297856
IOCTL_COLORSPACE_TRANSFORM_SET = 2297860
IOCTL_SET_ACTIVE_COLOR_PROFILE_NAME = 2297864
IOCTL_MIPI_DSI_QUERY_CAPS = 2298880
IOCTL_MIPI_DSI_TRANSMISSION = 2298884
IOCTL_MIPI_DSI_RESET = 2298888
DXGK_WIN32K_PARAM_FLAG_UPDATEREGISTRY = 1
DXGK_WIN32K_PARAM_FLAG_MODESWITCH = 2
DXGK_WIN32K_PARAM_FLAG_DISABLEVIEW = 4
VIDEO_DUALVIEW_REMOVABLE = 1
VIDEO_DUALVIEW_PRIMARY = 2147483648
VIDEO_DUALVIEW_SECONDARY = 1073741824
VIDEO_DUALVIEW_WDDM_VGA = 536870912
VIDEO_STATE_NON_STANDARD_VGA = 1
VIDEO_STATE_UNEMULATED_VGA_STATE = 2
VIDEO_STATE_PACKED_CHAIN4_MODE = 4
VIDEO_MODE_NO_ZERO_MEMORY = 2147483648
VIDEO_MODE_MAP_MEM_LINEAR = 1073741824
VIDEO_MODE_COLOR = 1
VIDEO_MODE_GRAPHICS = 2
VIDEO_MODE_PALETTE_DRIVEN = 4
VIDEO_MODE_MANAGED_PALETTE = 8
VIDEO_MODE_INTERLACED = 16
VIDEO_MODE_NO_OFF_SCREEN = 32
VIDEO_MODE_NO_64_BIT_ACCESS = 64
VIDEO_MODE_BANKED = 128
VIDEO_MODE_LINEAR = 256
VIDEO_MODE_ASYNC_POINTER = 1
VIDEO_MODE_MONO_POINTER = 2
VIDEO_MODE_COLOR_POINTER = 4
VIDEO_MODE_ANIMATE_START = 8
VIDEO_MODE_ANIMATE_UPDATE = 16
PLANAR_HC = 1
VIDEO_DEVICE_COLOR = 1
VIDEO_OPTIONAL_GAMMET_TABLE = 2
VIDEO_COLOR_LUT_DATA_FORMAT_RGB256WORDS = 1
VIDEO_COLOR_LUT_DATA_FORMAT_PRIVATEFORMAT = 2147483648
DISPLAYPOLICY_AC = 1
DISPLAYPOLICY_DC = 2
CHAR_TYPE_SBCS = 0
CHAR_TYPE_LEADING = 2
CHAR_TYPE_TRAILING = 3
BITMAP_BITS_BYTE_ALIGN = 8
BITMAP_BITS_WORD_ALIGN = 16
BITMAP_ARRAY_BYTE = 3
BITMAP_PLANES = 1
BITMAP_BITS_PIXEL = 1
DD_FULLSCREEN_VIDEO_DEVICE_NAME = '\\Device\\FSVideo'
VIDEO_REASON_NONE = 0
VIDEO_REASON_POLICY1 = 1
VIDEO_REASON_POLICY2 = 2
VIDEO_REASON_POLICY3 = 3
VIDEO_REASON_POLICY4 = 4
VIDEO_REASON_LOCK = 5
VIDEO_REASON_FAILED_ROTATION = 5
VIDEO_REASON_ALLOCATION = 6
VIDEO_REASON_SCRATCH = 8
VIDEO_REASON_CONFIGURATION = 9
VIDEO_MAX_REASON = 9
BRIGHTNESS_MAX_LEVEL_COUNT = 103
BRIGHTNESS_MAX_NIT_RANGE_COUNT = 16
DSI_PACKET_EMBEDDED_PAYLOAD_SIZE = 8
MAX_PACKET_COUNT = 128
DSI_INVALID_PACKET_INDEX = 255
DSI_SOT_ERROR = 1
DSI_SOT_SYNC_ERROR = 2
DSI_EOT_SYNC_ERROR = 4
DSI_ESCAPE_MODE_ENTRY_COMMAND_ERROR = 8
DSI_LOW_POWER_TRANSMIT_SYNC_ERROR = 16
DSI_PERIPHERAL_TIMEOUT_ERROR = 32
DSI_FALSE_CONTROL_ERROR = 64
DSI_CONTENTION_DETECTED = 128
DSI_CHECKSUM_ERROR_CORRECTED = 256
DSI_CHECKSUM_ERROR_NOT_CORRECTED = 512
DSI_LONG_PACKET_PAYLOAD_CHECKSUM_ERROR = 1024
DSI_DSI_DATA_TYPE_NOT_RECOGNIZED = 2048
DSI_DSI_VC_ID_INVALID = 4096
DSI_INVALID_TRANSMISSION_LENGTH = 8192
DSI_DSI_PROTOCOL_VIOLATION = 32768
HOST_DSI_DEVICE_NOT_READY = 1
HOST_DSI_INTERFACE_RESET = 2
HOST_DSI_DEVICE_RESET = 4
HOST_DSI_TRANSMISSION_CANCELLED = 16
HOST_DSI_TRANSMISSION_DROPPED = 32
HOST_DSI_TRANSMISSION_TIMEOUT = 64
HOST_DSI_INVALID_TRANSMISSION = 256
HOST_DSI_OS_REJECTED_PACKET = 512
HOST_DSI_DRIVER_REJECTED_PACKET = 1024
HOST_DSI_BAD_TRANSMISSION_MODE = 4096
def _define_GUID_MONITOR_OVERRIDE_PSEUDO_SPECIALIZED():
    return Guid('f196c02f-f86f-4f9a-aa-15-e9-ce-bd-fe-3b-96')
FD_ERROR = 4294967295
DDI_ERROR = 4294967295
FDM_TYPE_BM_SIDE_CONST = 1
FDM_TYPE_MAXEXT_EQUAL_BM_SIDE = 2
FDM_TYPE_CHAR_INC_EQUAL_BM_BASE = 4
FDM_TYPE_ZERO_BEARINGS = 8
FDM_TYPE_CONST_BEARINGS = 16
GS_UNICODE_HANDLES = 1
GS_8BIT_HANDLES = 2
GS_16BIT_HANDLES = 4
FM_VERSION_NUMBER = 0
FM_TYPE_LICENSED = 2
FM_READONLY_EMBED = 4
FM_EDITABLE_EMBED = 8
FM_NO_EMBEDDING = 2
FM_INFO_TECH_TRUETYPE = 1
FM_INFO_TECH_BITMAP = 2
FM_INFO_TECH_STROKE = 4
FM_INFO_TECH_OUTLINE_NOT_TRUETYPE = 8
FM_INFO_ARB_XFORMS = 16
FM_INFO_1BPP = 32
FM_INFO_4BPP = 64
FM_INFO_8BPP = 128
FM_INFO_16BPP = 256
FM_INFO_24BPP = 512
FM_INFO_32BPP = 1024
FM_INFO_INTEGER_WIDTH = 2048
FM_INFO_CONSTANT_WIDTH = 4096
FM_INFO_NOT_CONTIGUOUS = 8192
FM_INFO_TECH_MM = 16384
FM_INFO_RETURNS_OUTLINES = 32768
FM_INFO_RETURNS_STROKES = 65536
FM_INFO_RETURNS_BITMAPS = 131072
FM_INFO_DSIG = 262144
FM_INFO_RIGHT_HANDED = 524288
FM_INFO_INTEGRAL_SCALING = 1048576
FM_INFO_90DEGREE_ROTATIONS = 2097152
FM_INFO_OPTICALLY_FIXED_PITCH = 4194304
FM_INFO_DO_NOT_ENUMERATE = 8388608
FM_INFO_ISOTROPIC_SCALING_ONLY = 16777216
FM_INFO_ANISOTROPIC_SCALING_ONLY = 33554432
FM_INFO_TECH_CFF = 67108864
FM_INFO_FAMILY_EQUIV = 134217728
FM_INFO_DBCS_FIXED_PITCH = 268435456
FM_INFO_NONNEGATIVE_AC = 536870912
FM_INFO_IGNORE_TC_RA_ABLE = 1073741824
FM_INFO_TECH_TYPE1 = 2147483648
MAXCHARSETS = 16
FM_PANOSE_CULTURE_LATIN = 0
FM_SEL_ITALIC = 1
FM_SEL_UNDERSCORE = 2
FM_SEL_NEGATIVE = 4
FM_SEL_OUTLINED = 8
FM_SEL_STRIKEOUT = 16
FM_SEL_BOLD = 32
FM_SEL_REGULAR = 64
OPENGL_CMD = 4352
OPENGL_GETINFO = 4353
WNDOBJ_SETUP = 4354
DDI_DRIVER_VERSION_NT4 = 131072
DDI_DRIVER_VERSION_SP3 = 131075
DDI_DRIVER_VERSION_NT5 = 196608
DDI_DRIVER_VERSION_NT5_01 = 196864
DDI_DRIVER_VERSION_NT5_01_SP1 = 196865
GDI_DRIVER_VERSION = 16384
INDEX_DrvEnablePDEV = 0
INDEX_DrvCompletePDEV = 1
INDEX_DrvDisablePDEV = 2
INDEX_DrvEnableSurface = 3
INDEX_DrvDisableSurface = 4
INDEX_DrvAssertMode = 5
INDEX_DrvOffset = 6
INDEX_DrvResetPDEV = 7
INDEX_DrvDisableDriver = 8
INDEX_DrvCreateDeviceBitmap = 10
INDEX_DrvDeleteDeviceBitmap = 11
INDEX_DrvRealizeBrush = 12
INDEX_DrvDitherColor = 13
INDEX_DrvStrokePath = 14
INDEX_DrvFillPath = 15
INDEX_DrvStrokeAndFillPath = 16
INDEX_DrvPaint = 17
INDEX_DrvBitBlt = 18
INDEX_DrvCopyBits = 19
INDEX_DrvStretchBlt = 20
INDEX_DrvSetPalette = 22
INDEX_DrvTextOut = 23
INDEX_DrvEscape = 24
INDEX_DrvDrawEscape = 25
INDEX_DrvQueryFont = 26
INDEX_DrvQueryFontTree = 27
INDEX_DrvQueryFontData = 28
INDEX_DrvSetPointerShape = 29
INDEX_DrvMovePointer = 30
INDEX_DrvLineTo = 31
INDEX_DrvSendPage = 32
INDEX_DrvStartPage = 33
INDEX_DrvEndDoc = 34
INDEX_DrvStartDoc = 35
INDEX_DrvGetGlyphMode = 37
INDEX_DrvSynchronize = 38
INDEX_DrvSaveScreenBits = 40
INDEX_DrvGetModes = 41
INDEX_DrvFree = 42
INDEX_DrvDestroyFont = 43
INDEX_DrvQueryFontCaps = 44
INDEX_DrvLoadFontFile = 45
INDEX_DrvUnloadFontFile = 46
INDEX_DrvFontManagement = 47
INDEX_DrvQueryTrueTypeTable = 48
INDEX_DrvQueryTrueTypeOutline = 49
INDEX_DrvGetTrueTypeFile = 50
INDEX_DrvQueryFontFile = 51
INDEX_DrvMovePanning = 52
INDEX_DrvQueryAdvanceWidths = 53
INDEX_DrvSetPixelFormat = 54
INDEX_DrvDescribePixelFormat = 55
INDEX_DrvSwapBuffers = 56
INDEX_DrvStartBanding = 57
INDEX_DrvNextBand = 58
INDEX_DrvGetDirectDrawInfo = 59
INDEX_DrvEnableDirectDraw = 60
INDEX_DrvDisableDirectDraw = 61
INDEX_DrvQuerySpoolType = 62
INDEX_DrvIcmCreateColorTransform = 64
INDEX_DrvIcmDeleteColorTransform = 65
INDEX_DrvIcmCheckBitmapBits = 66
INDEX_DrvIcmSetDeviceGammaRamp = 67
INDEX_DrvGradientFill = 68
INDEX_DrvStretchBltROP = 69
INDEX_DrvPlgBlt = 70
INDEX_DrvAlphaBlend = 71
INDEX_DrvSynthesizeFont = 72
INDEX_DrvGetSynthesizedFontFiles = 73
INDEX_DrvTransparentBlt = 74
INDEX_DrvQueryPerBandInfo = 75
INDEX_DrvQueryDeviceSupport = 76
INDEX_DrvReserved1 = 77
INDEX_DrvReserved2 = 78
INDEX_DrvReserved3 = 79
INDEX_DrvReserved4 = 80
INDEX_DrvReserved5 = 81
INDEX_DrvReserved6 = 82
INDEX_DrvReserved7 = 83
INDEX_DrvReserved8 = 84
INDEX_DrvDeriveSurface = 85
INDEX_DrvQueryGlyphAttrs = 86
INDEX_DrvNotify = 87
INDEX_DrvSynchronizeSurface = 88
INDEX_DrvResetDevice = 89
INDEX_DrvReserved9 = 90
INDEX_DrvReserved10 = 91
INDEX_DrvReserved11 = 92
INDEX_DrvRenderHint = 93
INDEX_DrvCreateDeviceBitmapEx = 94
INDEX_DrvDeleteDeviceBitmapEx = 95
INDEX_DrvAssociateSharedSurface = 96
INDEX_DrvSynchronizeRedirectionBitmaps = 97
INDEX_DrvAccumulateD3DDirtyRect = 98
INDEX_DrvStartDxInterop = 99
INDEX_DrvEndDxInterop = 100
INDEX_DrvLockDisplayArea = 101
INDEX_DrvUnlockDisplayArea = 102
INDEX_DrvSurfaceComplete = 103
INDEX_LAST = 89
GCAPS_BEZIERS = 1
GCAPS_GEOMETRICWIDE = 2
GCAPS_ALTERNATEFILL = 4
GCAPS_WINDINGFILL = 8
GCAPS_HALFTONE = 16
GCAPS_COLOR_DITHER = 32
GCAPS_HORIZSTRIKE = 64
GCAPS_VERTSTRIKE = 128
GCAPS_OPAQUERECT = 256
GCAPS_VECTORFONT = 512
GCAPS_MONO_DITHER = 1024
GCAPS_ASYNCCHANGE = 2048
GCAPS_ASYNCMOVE = 4096
GCAPS_DONTJOURNAL = 8192
GCAPS_DIRECTDRAW = 16384
GCAPS_ARBRUSHOPAQUE = 32768
GCAPS_PANNING = 65536
GCAPS_HIGHRESTEXT = 262144
GCAPS_PALMANAGED = 524288
GCAPS_DITHERONREALIZE = 2097152
GCAPS_NO64BITMEMACCESS = 4194304
GCAPS_FORCEDITHER = 8388608
GCAPS_GRAY16 = 16777216
GCAPS_ICM = 33554432
GCAPS_CMYKCOLOR = 67108864
GCAPS_LAYERED = 134217728
GCAPS_ARBRUSHTEXT = 268435456
GCAPS_SCREENPRECISION = 536870912
GCAPS_FONT_RASTERIZER = 1073741824
GCAPS_NUP = 2147483648
GCAPS2_JPEGSRC = 1
GCAPS2_xxxx = 2
GCAPS2_PNGSRC = 8
GCAPS2_CHANGEGAMMARAMP = 16
GCAPS2_ALPHACURSOR = 32
GCAPS2_SYNCFLUSH = 64
GCAPS2_SYNCTIMER = 128
GCAPS2_ICD_MULTIMON = 256
GCAPS2_MOUSETRAILS = 512
GCAPS2_RESERVED1 = 1024
GCAPS2_REMOTEDRIVER = 1024
GCAPS2_EXCLUDELAYERED = 2048
GCAPS2_INCLUDEAPIBITMAPS = 4096
GCAPS2_SHOWHIDDENPOINTER = 8192
GCAPS2_CLEARTYPE = 16384
GCAPS2_ACC_DRIVER = 32768
GCAPS2_BITMAPEXREUSE = 65536
LA_GEOMETRIC = 1
LA_ALTERNATE = 2
LA_STARTGAP = 4
LA_STYLED = 8
JOIN_ROUND = 0
JOIN_BEVEL = 1
JOIN_MITER = 2
ENDCAP_ROUND = 0
ENDCAP_SQUARE = 1
ENDCAP_BUTT = 2
PRIMARY_ORDER_ABC = 0
PRIMARY_ORDER_ACB = 1
PRIMARY_ORDER_BAC = 2
PRIMARY_ORDER_BCA = 3
PRIMARY_ORDER_CBA = 4
PRIMARY_ORDER_CAB = 5
HT_PATSIZE_2x2 = 0
HT_PATSIZE_2x2_M = 1
HT_PATSIZE_4x4 = 2
HT_PATSIZE_4x4_M = 3
HT_PATSIZE_6x6 = 4
HT_PATSIZE_6x6_M = 5
HT_PATSIZE_8x8 = 6
HT_PATSIZE_8x8_M = 7
HT_PATSIZE_10x10 = 8
HT_PATSIZE_10x10_M = 9
HT_PATSIZE_12x12 = 10
HT_PATSIZE_12x12_M = 11
HT_PATSIZE_14x14 = 12
HT_PATSIZE_14x14_M = 13
HT_PATSIZE_16x16 = 14
HT_PATSIZE_16x16_M = 15
HT_PATSIZE_SUPERCELL = 16
HT_PATSIZE_SUPERCELL_M = 17
HT_PATSIZE_USER = 18
HT_PATSIZE_MAX_INDEX = 18
HT_PATSIZE_DEFAULT = 17
HT_USERPAT_CX_MIN = 4
HT_USERPAT_CX_MAX = 256
HT_USERPAT_CY_MIN = 4
HT_USERPAT_CY_MAX = 256
HT_FORMAT_1BPP = 0
HT_FORMAT_4BPP = 2
HT_FORMAT_4BPP_IRGB = 3
HT_FORMAT_8BPP = 4
HT_FORMAT_16BPP = 5
HT_FORMAT_24BPP = 6
HT_FORMAT_32BPP = 7
WINDDI_MAX_BROADCAST_CONTEXT = 64
HT_FLAG_SQUARE_DEVICE_PEL = 1
HT_FLAG_HAS_BLACK_DYE = 2
HT_FLAG_ADDITIVE_PRIMS = 4
HT_FLAG_USE_8BPP_BITMASK = 8
HT_FLAG_INK_HIGH_ABSORPTION = 16
HT_FLAG_INK_ABSORPTION_INDICES = 96
HT_FLAG_DO_DEVCLR_XFORM = 128
HT_FLAG_OUTPUT_CMY = 256
HT_FLAG_PRINT_DRAFT_MODE = 512
HT_FLAG_INVERT_8BPP_BITMASK_IDX = 1024
HT_FLAG_8BPP_CMY332_MASK = 4278190080
HT_FLAG_INK_ABSORPTION_IDX0 = 0
HT_FLAG_INK_ABSORPTION_IDX1 = 32
HT_FLAG_INK_ABSORPTION_IDX2 = 64
HT_FLAG_INK_ABSORPTION_IDX3 = 96
HT_FLAG_NORMAL_INK_ABSORPTION = 0
HT_FLAG_LOW_INK_ABSORPTION = 32
HT_FLAG_LOWER_INK_ABSORPTION = 64
HT_FLAG_LOWEST_INK_ABSORPTION = 96
PPC_DEFAULT = 0
PPC_UNDEFINED = 1
PPC_RGB_ORDER_VERTICAL_STRIPES = 2
PPC_BGR_ORDER_VERTICAL_STRIPES = 3
PPC_RGB_ORDER_HORIZONTAL_STRIPES = 4
PPC_BGR_ORDER_HORIZONTAL_STRIPES = 5
PPG_DEFAULT = 0
PPG_SRGB = 1
BR_DEVICE_ICM = 1
BR_HOST_ICM = 2
BR_CMYKCOLOR = 4
BR_ORIGCOLOR = 8
FO_SIM_BOLD = 8192
FO_SIM_ITALIC = 16384
FO_EM_HEIGHT = 32768
FO_GRAY16 = 65536
FO_NOGRAY16 = 131072
FO_NOHINTS = 262144
FO_NO_CHOICE = 524288
FO_CFF = 1048576
FO_POSTSCRIPT = 2097152
FO_MULTIPLEMASTER = 4194304
FO_VERT_FACE = 8388608
FO_DBCS_FONT = 16777216
FO_NOCLEARTYPE = 33554432
FO_CLEARTYPE_X = 268435456
FO_CLEARTYPE_Y = 536870912
FO_CLEARTYPENATURAL_X = 1073741824
DC_TRIVIAL = 0
DC_RECT = 1
DC_COMPLEX = 3
FC_RECT = 1
FC_RECT4 = 2
FC_COMPLEX = 3
TC_RECTANGLES = 0
TC_PATHOBJ = 2
OC_BANK_CLIP = 1
CT_RECTANGLES = 0
CD_RIGHTDOWN = 0
CD_LEFTDOWN = 1
CD_RIGHTUP = 2
CD_LEFTUP = 3
CD_ANY = 4
CD_LEFTWARDS = 1
CD_UPWARDS = 2
FO_HGLYPHS = 0
FO_GLYPHBITS = 1
FO_PATHOBJ = 2
FD_NEGATIVE_FONT = 1
FO_DEVICE_FONT = 1
FO_OUTLINE_CAPABLE = 2
SO_FLAG_DEFAULT_PLACEMENT = 1
SO_HORIZONTAL = 2
SO_VERTICAL = 4
SO_REVERSED = 8
SO_ZERO_BEARINGS = 16
SO_CHAR_INC_EQUAL_BM_BASE = 32
SO_MAXEXT_EQUAL_BM_SIDE = 64
SO_DO_NOT_SUBSTITUTE_DEVICE_FONT = 128
SO_GLYPHINDEX_TEXTOUT = 256
SO_ESC_NOT_ORIENT = 512
SO_DXDY = 1024
SO_CHARACTER_EXTRA = 2048
SO_BREAK_EXTRA = 4096
FO_ATTR_MODE_ROTATE = 1
PAL_INDEXED = 1
PAL_BITFIELDS = 2
PAL_RGB = 4
PAL_BGR = 8
PAL_CMYK = 16
PO_BEZIERS = 1
PO_ELLIPSE = 2
PO_ALL_INTEGERS = 4
PO_ENUM_AS_INTEGERS = 8
PO_WIDENED = 16
PD_BEGINSUBPATH = 1
PD_ENDSUBPATH = 2
PD_RESETSTYLE = 4
PD_CLOSEFIGURE = 8
PD_BEZIERS = 16
SGI_EXTRASPACE = 0
STYPE_BITMAP = 0
STYPE_DEVBITMAP = 3
BMF_1BPP = 1
BMF_4BPP = 2
BMF_8BPP = 3
BMF_16BPP = 4
BMF_24BPP = 5
BMF_32BPP = 6
BMF_4RLE = 7
BMF_8RLE = 8
BMF_JPEG = 9
BMF_PNG = 10
BMF_TOPDOWN = 1
BMF_NOZEROINIT = 2
BMF_DONTCACHE = 4
BMF_USERMEM = 8
BMF_KMSECTION = 16
BMF_NOTSYSMEM = 32
BMF_WINDOW_BLT = 64
BMF_UMPDMEM = 128
BMF_TEMP_ALPHA = 256
BMF_ACC_NOTIFY = 32768
BMF_RMT_ENTER = 16384
BMF_RESERVED = 15872
GX_IDENTITY = 0
GX_OFFSET = 1
GX_SCALE = 2
GX_GENERAL = 3
XF_LTOL = 0
XF_INV_LTOL = 1
XF_LTOFX = 2
XF_INV_FXTOL = 3
XO_TRIVIAL = 1
XO_TABLE = 2
XO_TO_MONO = 4
XO_FROM_CMYK = 8
XO_DEVICE_ICM = 16
XO_HOST_ICM = 32
XO_SRCPALETTE = 1
XO_DESTPALETTE = 2
XO_DESTDCPALETTE = 3
XO_SRCBITFIELDS = 4
XO_DESTBITFIELDS = 5
HOOK_BITBLT = 1
HOOK_STRETCHBLT = 2
HOOK_PLGBLT = 4
HOOK_TEXTOUT = 8
HOOK_PAINT = 16
HOOK_STROKEPATH = 32
HOOK_FILLPATH = 64
HOOK_STROKEANDFILLPATH = 128
HOOK_LINETO = 256
HOOK_COPYBITS = 1024
HOOK_MOVEPANNING = 2048
HOOK_SYNCHRONIZE = 4096
HOOK_STRETCHBLTROP = 8192
HOOK_SYNCHRONIZEACCESS = 16384
HOOK_TRANSPARENTBLT = 32768
HOOK_ALPHABLEND = 65536
HOOK_GRADIENTFILL = 131072
HOOK_FLAGS = 243199
MS_NOTSYSTEMMEMORY = 1
MS_SHAREDACCESS = 2
MS_CDDDEVICEBITMAP = 4
MS_REUSEDDEVICEBITMAP = 8
DRVQUERY_USERMODE = 1
HS_DDI_MAX = 6
DRD_SUCCESS = 0
DRD_ERROR = 1
SS_SAVE = 0
SS_RESTORE = 1
SS_FREE = 2
CDBEX_REDIRECTION = 1
CDBEX_DXINTEROP = 2
CDBEX_NTSHAREDSURFACEHANDLE = 4
CDBEX_CROSSADAPTER = 8
CDBEX_REUSE = 16
WINDDI_MAXSETPALETTECOLORS = 256
WINDDI_MAXSETPALETTECOLORINDEX = 255
DM_DEFAULT = 1
DM_MONOCHROME = 2
DCR_SOLID = 0
DCR_DRIVER = 1
DCR_HALFTONE = 2
RB_DITHERCOLOR = -2147483648
QFT_LIGATURES = 1
QFT_KERNPAIRS = 2
QFT_GLYPHSET = 3
QFD_GLYPHANDBITMAP = 1
QFD_GLYPHANDOUTLINE = 2
QFD_MAXEXTENTS = 3
QFD_TT_GLYPHANDBITMAP = 4
QFD_TT_GRAY1_BITMAP = 5
QFD_TT_GRAY2_BITMAP = 6
QFD_TT_GRAY4_BITMAP = 8
QFD_TT_GRAY8_BITMAP = 9
QFD_TT_MONO_BITMAP = 5
QC_OUTLINES = 1
QC_1BIT = 2
QC_4BIT = 4
FF_SIGNATURE_VERIFIED = 1
FF_IGNORED_SIGNATURE = 2
QAW_GETWIDTHS = 0
QAW_GETEASYWIDTHS = 1
TTO_METRICS_ONLY = 1
TTO_QUBICS = 2
TTO_UNHINTED = 4
QFF_DESCRIPTION = 1
QFF_NUMFACES = 2
FP_ALTERNATEMODE = 1
FP_WINDINGMODE = 2
SPS_ERROR = 0
SPS_DECLINE = 1
SPS_ACCEPT_NOEXCLUDE = 2
SPS_ACCEPT_EXCLUDE = 3
SPS_ACCEPT_SYNCHRONOUS = 4
SPS_CHANGE = 1
SPS_ASYNCCHANGE = 2
SPS_ANIMATESTART = 4
SPS_ANIMATEUPDATE = 8
SPS_ALPHA = 16
SPS_RESERVED = 32
SPS_RESERVED1 = 64
SPS_FLAGSMASK = 255
SPS_LENGTHMASK = 3840
SPS_FREQMASK = 1044480
ED_ABORTDOC = 1
IGRF_RGB_256BYTES = 0
IGRF_RGB_256WORDS = 1
QDS_CHECKJPEGFORMAT = 0
QDS_CHECKPNGFORMAT = 1
DSS_TIMER_EVENT = 1
DSS_FLUSH_EVENT = 2
DSS_RESERVED = 4
DSS_RESERVED1 = 8
DSS_RESERVED2 = 16
DN_ACCELERATION_LEVEL = 1
DN_DEVICE_ORIGIN = 2
DN_SLEEP_MODE = 3
DN_DRAWING_BEGIN = 4
DN_ASSOCIATE_WINDOW = 5
DN_COMPOSITION_CHANGED = 6
DN_DRAWING_BEGIN_APIBITMAP = 7
DN_SURFOBJ_DESTRUCTION = 8
WOC_RGN_CLIENT_DELTA = 1
WOC_RGN_CLIENT = 2
WOC_RGN_SURFACE_DELTA = 4
WOC_RGN_SURFACE = 8
WOC_CHANGED = 16
WOC_DELETE = 32
WOC_DRAWN = 64
WOC_SPRITE_OVERLAP = 128
WOC_SPRITE_NO_OVERLAP = 256
WOC_RGN_SPRITE = 512
WO_RGN_CLIENT_DELTA = 1
WO_RGN_CLIENT = 2
WO_RGN_SURFACE_DELTA = 4
WO_RGN_SURFACE = 8
WO_RGN_UPDATE_ALL = 16
WO_RGN_WINDOW = 32
WO_DRAW_NOTIFY = 64
WO_SPRITE_NOTIFY = 128
WO_RGN_DESKTOP_COORD = 256
WO_RGN_SPRITE = 512
EHN_RESTORED = 0
EHN_ERROR = 1
ECS_TEARDOWN = 1
ECS_REDRAW = 2
DEVHTADJF_COLOR_DEVICE = 1
DEVHTADJF_ADDITIVE_DEVICE = 2
FL_ZERO_MEMORY = 1
FL_NONPAGED_MEMORY = 2
FL_NON_SESSION = 4
QSA_MMX = 256
QSA_SSE = 8192
QSA_3DNOW = 16384
QSA_SSE1 = 8192
QSA_SSE2 = 65536
QSA_SSE3 = 524288
ENG_FNT_CACHE_READ_FAULT = 1
ENG_FNT_CACHE_WRITE_FAULT = 2
DRH_APIBITMAP = 1
MC_CAPS_NONE = 0
MC_CAPS_MONITOR_TECHNOLOGY_TYPE = 1
MC_CAPS_BRIGHTNESS = 2
MC_CAPS_CONTRAST = 4
MC_CAPS_COLOR_TEMPERATURE = 8
MC_CAPS_RED_GREEN_BLUE_GAIN = 16
MC_CAPS_RED_GREEN_BLUE_DRIVE = 32
MC_CAPS_DEGAUSS = 64
MC_CAPS_DISPLAY_AREA_POSITION = 128
MC_CAPS_DISPLAY_AREA_SIZE = 256
MC_CAPS_RESTORE_FACTORY_DEFAULTS = 1024
MC_CAPS_RESTORE_FACTORY_COLOR_DEFAULTS = 2048
MC_RESTORE_FACTORY_DEFAULTS_ENABLES_MONITOR_SETTINGS = 4096
MC_SUPPORTED_COLOR_TEMPERATURE_NONE = 0
MC_SUPPORTED_COLOR_TEMPERATURE_4000K = 1
MC_SUPPORTED_COLOR_TEMPERATURE_5000K = 2
MC_SUPPORTED_COLOR_TEMPERATURE_6500K = 4
MC_SUPPORTED_COLOR_TEMPERATURE_7500K = 8
MC_SUPPORTED_COLOR_TEMPERATURE_8200K = 16
MC_SUPPORTED_COLOR_TEMPERATURE_9300K = 32
MC_SUPPORTED_COLOR_TEMPERATURE_10000K = 64
MC_SUPPORTED_COLOR_TEMPERATURE_11500K = 128
PHYSICAL_MONITOR_DESCRIPTION_SIZE = 128
GETCONNECTEDIDS_TARGET = 0
GETCONNECTEDIDS_SOURCE = 1
S_INIT = 2
SETCONFIGURATION_STATUS_APPLIED = 0
SETCONFIGURATION_STATUS_ADDITIONAL = 1
SETCONFIGURATION_STATUS_OVERRIDDEN = 2
def _define_GetNumberOfPhysicalMonitorsFromHMONITOR():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMONITOR,POINTER(UInt32))(('GetNumberOfPhysicalMonitorsFromHMONITOR', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdwNumberOfPhysicalMonitors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNumberOfPhysicalMonitorsFromIDirect3DDevice9():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D9.IDirect3DDevice9_head,POINTER(UInt32))(('GetNumberOfPhysicalMonitorsFromIDirect3DDevice9', windll['dxva2.dll']), ((1, 'pDirect3DDevice9'),(1, 'pdwNumberOfPhysicalMonitors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPhysicalMonitorsFromHMONITOR():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HMONITOR,UInt32,POINTER(win32more.Devices.Display.PHYSICAL_MONITOR_head))(('GetPhysicalMonitorsFromHMONITOR', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'dwPhysicalMonitorArraySize'),(1, 'pPhysicalMonitorArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPhysicalMonitorsFromIDirect3DDevice9():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D9.IDirect3DDevice9_head,UInt32,POINTER(win32more.Devices.Display.PHYSICAL_MONITOR_head))(('GetPhysicalMonitorsFromIDirect3DDevice9', windll['dxva2.dll']), ((1, 'pDirect3DDevice9'),(1, 'dwPhysicalMonitorArraySize'),(1, 'pPhysicalMonitorArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyPhysicalMonitor():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('DestroyPhysicalMonitor', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DestroyPhysicalMonitors():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Devices.Display.PHYSICAL_MONITOR_head))(('DestroyPhysicalMonitors', windll['dxva2.dll']), ((1, 'dwPhysicalMonitorArraySize'),(1, 'pPhysicalMonitorArray'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVCPFeatureAndVCPFeatureReply():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,Byte,POINTER(win32more.Devices.Display.MC_VCP_CODE_TYPE),POINTER(UInt32),POINTER(UInt32))(('GetVCPFeatureAndVCPFeatureReply', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'bVCPCode'),(1, 'pvct'),(1, 'pdwCurrentValue'),(1, 'pdwMaximumValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVCPFeature():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,Byte,UInt32)(('SetVCPFeature', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'bVCPCode'),(1, 'dwNewValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaveCurrentSettings():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('SaveCurrentSettings', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCapabilitiesStringLength():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32))(('GetCapabilitiesStringLength', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdwCapabilitiesStringLengthInCharacters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CapabilitiesRequestAndCapabilitiesReply():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32)(('CapabilitiesRequestAndCapabilitiesReply', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pszASCIICapabilitiesString'),(1, 'dwCapabilitiesStringLengthInCharacters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTimingReport():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.MC_TIMING_REPORT_head))(('GetTimingReport', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pmtrMonitorTimingReport'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorCapabilities():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32))(('GetMonitorCapabilities', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdwMonitorCapabilities'),(1, 'pdwSupportedColorTemperatures'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SaveCurrentMonitorSettings():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('SaveCurrentMonitorSettings', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorTechnologyType():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.MC_DISPLAY_TECHNOLOGY_TYPE))(('GetMonitorTechnologyType', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdtyDisplayTechnologyType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorBrightness():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorBrightness', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdwMinimumBrightness'),(1, 'pdwCurrentBrightness'),(1, 'pdwMaximumBrightness'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorContrast():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorContrast', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pdwMinimumContrast'),(1, 'pdwCurrentContrast'),(1, 'pdwMaximumContrast'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorColorTemperature():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.MC_COLOR_TEMPERATURE))(('GetMonitorColorTemperature', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'pctCurrentColorTemperature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorRedGreenOrBlueDrive():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_DRIVE_TYPE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorRedGreenOrBlueDrive', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'dtDriveType'),(1, 'pdwMinimumDrive'),(1, 'pdwCurrentDrive'),(1, 'pdwMaximumDrive'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorRedGreenOrBlueGain():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_GAIN_TYPE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorRedGreenOrBlueGain', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'gtGainType'),(1, 'pdwMinimumGain'),(1, 'pdwCurrentGain'),(1, 'pdwMaximumGain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorBrightness():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,UInt32)(('SetMonitorBrightness', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'dwNewBrightness'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorContrast():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,UInt32)(('SetMonitorContrast', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'dwNewContrast'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorColorTemperature():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_COLOR_TEMPERATURE)(('SetMonitorColorTemperature', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'ctCurrentColorTemperature'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorRedGreenOrBlueDrive():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_DRIVE_TYPE,UInt32)(('SetMonitorRedGreenOrBlueDrive', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'dtDriveType'),(1, 'dwNewDrive'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorRedGreenOrBlueGain():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_GAIN_TYPE,UInt32)(('SetMonitorRedGreenOrBlueGain', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'gtGainType'),(1, 'dwNewGain'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DegaussMonitor():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('DegaussMonitor', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorDisplayAreaSize():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_SIZE_TYPE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorDisplayAreaSize', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'stSizeType'),(1, 'pdwMinimumWidthOrHeight'),(1, 'pdwCurrentWidthOrHeight'),(1, 'pdwMaximumWidthOrHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMonitorDisplayAreaPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_POSITION_TYPE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMonitorDisplayAreaPosition', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'ptPositionType'),(1, 'pdwMinimumPosition'),(1, 'pdwCurrentPosition'),(1, 'pdwMaximumPosition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorDisplayAreaSize():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_SIZE_TYPE,UInt32)(('SetMonitorDisplayAreaSize', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'stSizeType'),(1, 'dwNewDisplayAreaWidthOrHeight'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMonitorDisplayAreaPosition():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Devices.Display.MC_POSITION_TYPE,UInt32)(('SetMonitorDisplayAreaPosition', windll['dxva2.dll']), ((1, 'hMonitor'),(1, 'ptPositionType'),(1, 'dwNewPosition'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RestoreMonitorFactoryColorDefaults():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('RestoreMonitorFactoryColorDefaults', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RestoreMonitorFactoryDefaults():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE)(('RestoreMonitorFactoryDefaults', windll['dxva2.dll']), ((1, 'hMonitor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BRUSHOBJ_pvAllocRbrush():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.Devices.Display.BRUSHOBJ_head),UInt32)(('BRUSHOBJ_pvAllocRbrush', windll['GDI32.dll']), ((1, 'pbo'),(1, 'cj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BRUSHOBJ_pvGetRbrush():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.Devices.Display.BRUSHOBJ_head))(('BRUSHOBJ_pvGetRbrush', windll['GDI32.dll']), ((1, 'pbo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BRUSHOBJ_ulGetBrushColor():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.BRUSHOBJ_head))(('BRUSHOBJ_ulGetBrushColor', windll['GDI32.dll']), ((1, 'pbo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BRUSHOBJ_hGetColorTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.BRUSHOBJ_head))(('BRUSHOBJ_hGetColorTransform', windll['GDI32.dll']), ((1, 'pbo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPOBJ_cEnumStart():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.CLIPOBJ_head),win32more.Foundation.BOOL,UInt32,UInt32,UInt32)(('CLIPOBJ_cEnumStart', windll['GDI32.dll']), ((1, 'pco'),(1, 'bAll'),(1, 'iType'),(1, 'iDirection'),(1, 'cLimit'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPOBJ_bEnum():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.CLIPOBJ_head),UInt32,POINTER(UInt32))(('CLIPOBJ_bEnum', windll['GDI32.dll']), ((1, 'pco'),(1, 'cj'),(1, 'pul'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CLIPOBJ_ppoGetPath():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head))(('CLIPOBJ_ppoGetPath', windll['GDI32.dll']), ((1, 'pco'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_cGetAllGlyphHandles():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.FONTOBJ_head),POINTER(UInt32))(('FONTOBJ_cGetAllGlyphHandles', windll['GDI32.dll']), ((1, 'pfo'),(1, 'phg'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_vGetInfo():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,POINTER(win32more.Devices.Display.FONTINFO_head))(('FONTOBJ_vGetInfo', windll['GDI32.dll']), ((1, 'pfo'),(1, 'cjSize'),(1, 'pfi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_cGetGlyphs():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,UInt32,POINTER(UInt32),POINTER(c_void_p))(('FONTOBJ_cGetGlyphs', windll['GDI32.dll']), ((1, 'pfo'),(1, 'iMode'),(1, 'cGlyph'),(1, 'phg'),(1, 'ppvGlyph'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_pxoGetXform():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.FONTOBJ_head))(('FONTOBJ_pxoGetXform', windll['GDI32.dll']), ((1, 'pfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_pifi():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.IFIMETRICS_head),POINTER(win32more.Devices.Display.FONTOBJ_head))(('FONTOBJ_pifi', windll['GDI32.dll']), ((1, 'pfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_pfdg():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.FD_GLYPHSET_head),POINTER(win32more.Devices.Display.FONTOBJ_head))(('FONTOBJ_pfdg', windll['GDI32.dll']), ((1, 'pfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_pvTrueTypeFontFile():
    try:
        return WINFUNCTYPE(c_void_p,POINTER(win32more.Devices.Display.FONTOBJ_head),POINTER(UInt32))(('FONTOBJ_pvTrueTypeFontFile', windll['GDI32.dll']), ((1, 'pfo'),(1, 'pcjFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FONTOBJ_pQueryGlyphAttrs():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.FD_GLYPHATTR_head),POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32)(('FONTOBJ_pQueryGlyphAttrs', windll['GDI32.dll']), ((1, 'pfo'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PATHOBJ_vEnumStart():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.PATHOBJ_head))(('PATHOBJ_vEnumStart', windll['GDI32.dll']), ((1, 'ppo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PATHOBJ_bEnum():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.PATHDATA_head))(('PATHOBJ_bEnum', windll['GDI32.dll']), ((1, 'ppo'),(1, 'ppd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PATHOBJ_vEnumStartClipLines():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.LINEATTRS_head))(('PATHOBJ_vEnumStartClipLines', windll['GDI32.dll']), ((1, 'ppo'),(1, 'pco'),(1, 'pso'),(1, 'pla'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PATHOBJ_bEnumClipLines():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.PATHOBJ_head),UInt32,POINTER(win32more.Devices.Display.CLIPLINE_head))(('PATHOBJ_bEnumClipLines', windll['GDI32.dll']), ((1, 'ppo'),(1, 'cb'),(1, 'pcl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PATHOBJ_vGetBounds():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.RECTFX_head))(('PATHOBJ_vGetBounds', windll['GDI32.dll']), ((1, 'ppo'),(1, 'prectfx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STROBJ_vEnumStart():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.STROBJ_head))(('STROBJ_vEnumStart', windll['GDI32.dll']), ((1, 'pstro'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STROBJ_bEnum():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.STROBJ_head),POINTER(UInt32),POINTER(POINTER(win32more.Devices.Display.GLYPHPOS_head)))(('STROBJ_bEnum', windll['GDI32.dll']), ((1, 'pstro'),(1, 'pc'),(1, 'ppgpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STROBJ_bEnumPositionsOnly():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.STROBJ_head),POINTER(UInt32),POINTER(POINTER(win32more.Devices.Display.GLYPHPOS_head)))(('STROBJ_bEnumPositionsOnly', windll['GDI32.dll']), ((1, 'pstro'),(1, 'pc'),(1, 'ppgpos'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STROBJ_dwGetCodePage():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.STROBJ_head))(('STROBJ_dwGetCodePage', windll['GDI32.dll']), ((1, 'pstro'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_STROBJ_bGetAdvanceWidths():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.STROBJ_head),UInt32,UInt32,POINTER(win32more.Devices.Display.POINTQF_head))(('STROBJ_bGetAdvanceWidths', windll['GDI32.dll']), ((1, 'pso'),(1, 'iFirst'),(1, 'c'),(1, 'pptqD'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XFORMOBJ_iGetXform():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.XFORML_head))(('XFORMOBJ_iGetXform', windll['GDI32.dll']), ((1, 'pxo'),(1, 'pxform'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XFORMOBJ_bApplyXform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.XFORMOBJ_head),UInt32,UInt32,c_void_p,c_void_p)(('XFORMOBJ_bApplyXform', windll['GDI32.dll']), ((1, 'pxo'),(1, 'iMode'),(1, 'cPoints'),(1, 'pvIn'),(1, 'pvOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XLATEOBJ_iXlate():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.XLATEOBJ_head),UInt32)(('XLATEOBJ_iXlate', windll['GDI32.dll']), ((1, 'pxlo'),(1, 'iColor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XLATEOBJ_piVector():
    try:
        return WINFUNCTYPE(POINTER(UInt32),POINTER(win32more.Devices.Display.XLATEOBJ_head))(('XLATEOBJ_piVector', windll['GDI32.dll']), ((1, 'pxlo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XLATEOBJ_cGetPalette():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.XLATEOBJ_head),UInt32,UInt32,POINTER(UInt32))(('XLATEOBJ_cGetPalette', windll['GDI32.dll']), ((1, 'pxlo'),(1, 'iPal'),(1, 'cPal'),(1, 'pPal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_XLATEOBJ_hGetColorTransform():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.XLATEOBJ_head))(('XLATEOBJ_hGetColorTransform', windll['GDI32.dll']), ((1, 'pxlo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreateBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Foundation.SIZE,Int32,UInt32,UInt32,c_void_p)(('EngCreateBitmap', windll['GDI32.dll']), ((1, 'sizl'),(1, 'lWidth'),(1, 'iFormat'),(1, 'fl'),(1, 'pvBits'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreateDeviceSurface():
    try:
        return WINFUNCTYPE(win32more.Devices.Display.HSURF,win32more.Devices.Display.DHSURF,win32more.Foundation.SIZE,UInt32)(('EngCreateDeviceSurface', windll['GDI32.dll']), ((1, 'dhsurf'),(1, 'sizl'),(1, 'iFormatCompat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreateDeviceBitmap():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Devices.Display.DHSURF,win32more.Foundation.SIZE,UInt32)(('EngCreateDeviceBitmap', windll['GDI32.dll']), ((1, 'dhsurf'),(1, 'sizl'),(1, 'iFormatCompat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngDeleteSurface():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.HSURF)(('EngDeleteSurface', windll['GDI32.dll']), ((1, 'hsurf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngLockSurface():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.SURFOBJ_head),win32more.Devices.Display.HSURF)(('EngLockSurface', windll['GDI32.dll']), ((1, 'hsurf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngUnlockSurface():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.SURFOBJ_head))(('EngUnlockSurface', windll['GDI32.dll']), ((1, 'pso'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngEraseSurface():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Foundation.RECTL_head),UInt32)(('EngEraseSurface', windll['GDI32.dll']), ((1, 'pso'),(1, 'prcl'),(1, 'iColor'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngAssociateSurface():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.HSURF,win32more.Devices.Display.HDEV,UInt32)(('EngAssociateSurface', windll['GDI32.dll']), ((1, 'hsurf'),(1, 'hdev'),(1, 'flHooks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngMarkBandingSurface():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.HSURF)(('EngMarkBandingSurface', windll['GDI32.dll']), ((1, 'hsurf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCheckAbort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head))(('EngCheckAbort', windll['GDI32.dll']), ((1, 'pso'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngDeletePath():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.PATHOBJ_head))(('EngDeletePath', windll['GDI32.dll']), ((1, 'ppo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreatePalette():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HPALETTE,UInt32,UInt32,POINTER(UInt32),UInt32,UInt32,UInt32)(('EngCreatePalette', windll['GDI32.dll']), ((1, 'iMode'),(1, 'cColors'),(1, 'pulColors'),(1, 'flRed'),(1, 'flGreen'),(1, 'flBlue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngDeletePalette():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HPALETTE)(('EngDeletePalette', windll['GDI32.dll']), ((1, 'hpal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreateClip():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.CLIPOBJ_head),)(('EngCreateClip', windll['GDI32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngDeleteClip():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.CLIPOBJ_head))(('EngDeleteClip', windll['GDI32.dll']), ((1, 'pco'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngBitBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngBitBlt', windll['GDI32.dll']), ((1, 'psoTrg'),(1, 'psoSrc'),(1, 'psoMask'),(1, 'pco'),(1, 'pxlo'),(1, 'prclTrg'),(1, 'pptlSrc'),(1, 'pptlMask'),(1, 'pbo'),(1, 'pptlBrush'),(1, 'rop4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngLineTo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.RECTL_head),UInt32)(('EngLineTo', windll['GDI32.dll']), ((1, 'pso'),(1, 'pco'),(1, 'pbo'),(1, 'x1'),(1, 'y1'),(1, 'x2'),(1, 'y2'),(1, 'prclBounds'),(1, 'mix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngStretchBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngStretchBlt', windll['GDI32.dll']), ((1, 'psoDest'),(1, 'psoSrc'),(1, 'psoMask'),(1, 'pco'),(1, 'pxlo'),(1, 'pca'),(1, 'pptlHTOrg'),(1, 'prclDest'),(1, 'prclSrc'),(1, 'pptlMask'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngStretchBltROP():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32,POINTER(win32more.Devices.Display.BRUSHOBJ_head),UInt32)(('EngStretchBltROP', windll['GDI32.dll']), ((1, 'psoDest'),(1, 'psoSrc'),(1, 'psoMask'),(1, 'pco'),(1, 'pxlo'),(1, 'pca'),(1, 'pptlHTOrg'),(1, 'prclDest'),(1, 'prclSrc'),(1, 'pptlMask'),(1, 'iMode'),(1, 'pbo'),(1, 'rop4'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngAlphaBlend():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Devices.Display.BLENDOBJ_head))(('EngAlphaBlend', windll['GDI32.dll']), ((1, 'psoDest'),(1, 'psoSrc'),(1, 'pco'),(1, 'pxlo'),(1, 'prclDest'),(1, 'prclSrc'),(1, 'pBlendObj'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngGradientFill():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.TRIVERTEX_head),UInt32,c_void_p,UInt32,POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngGradientFill', windll['GDI32.dll']), ((1, 'psoDest'),(1, 'pco'),(1, 'pxlo'),(1, 'pVertex'),(1, 'nVertex'),(1, 'pMesh'),(1, 'nMesh'),(1, 'prclExtents'),(1, 'pptlDitherOrg'),(1, 'ulMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngTransparentBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),UInt32,UInt32)(('EngTransparentBlt', windll['GDI32.dll']), ((1, 'psoDst'),(1, 'psoSrc'),(1, 'pco'),(1, 'pxlo'),(1, 'prclDst'),(1, 'prclSrc'),(1, 'TransColor'),(1, 'bCalledFromBitBlt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngTextOut():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.STROBJ_head),POINTER(win32more.Devices.Display.FONTOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngTextOut', windll['GDI32.dll']), ((1, 'pso'),(1, 'pstro'),(1, 'pfo'),(1, 'pco'),(1, 'prclExtra'),(1, 'prclOpaque'),(1, 'pboFore'),(1, 'pboOpaque'),(1, 'pptlOrg'),(1, 'mix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngStrokePath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.LINEATTRS_head),UInt32)(('EngStrokePath', windll['GDI32.dll']), ((1, 'pso'),(1, 'ppo'),(1, 'pco'),(1, 'pxo'),(1, 'pbo'),(1, 'pptlBrushOrg'),(1, 'plineattrs'),(1, 'mix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngFillPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32,UInt32)(('EngFillPath', windll['GDI32.dll']), ((1, 'pso'),(1, 'ppo'),(1, 'pco'),(1, 'pbo'),(1, 'pptlBrushOrg'),(1, 'mix'),(1, 'flOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngStrokeAndFillPath():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Devices.Display.LINEATTRS_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32,UInt32)(('EngStrokeAndFillPath', windll['GDI32.dll']), ((1, 'pso'),(1, 'ppo'),(1, 'pco'),(1, 'pxo'),(1, 'pboStroke'),(1, 'plineattrs'),(1, 'pboFill'),(1, 'pptlBrushOrg'),(1, 'mixFill'),(1, 'flOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngPaint():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngPaint', windll['GDI32.dll']), ((1, 'pso'),(1, 'pco'),(1, 'pbo'),(1, 'pptlBrushOrg'),(1, 'mix'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCopyBits():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head))(('EngCopyBits', windll['GDI32.dll']), ((1, 'psoDest'),(1, 'psoSrc'),(1, 'pco'),(1, 'pxlo'),(1, 'prclDest'),(1, 'pptlSrc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngPlgBlt():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.POINTFIX_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)(('EngPlgBlt', windll['GDI32.dll']), ((1, 'psoTrg'),(1, 'psoSrc'),(1, 'psoMsk'),(1, 'pco'),(1, 'pxlo'),(1, 'pca'),(1, 'pptlBrushOrg'),(1, 'pptfx'),(1, 'prcl'),(1, 'pptl'),(1, 'iMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HT_Get8BPPFormatPalette():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head),UInt16,UInt16,UInt16)(('HT_Get8BPPFormatPalette', windll['GDI32.dll']), ((1, 'pPaletteEntry'),(1, 'RedGamma'),(1, 'GreenGamma'),(1, 'BlueGamma'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HT_Get8BPPMaskPalette():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Graphics.Gdi.PALETTEENTRY_head),win32more.Foundation.BOOL,Byte,UInt16,UInt16,UInt16)(('HT_Get8BPPMaskPalette', windll['GDI32.dll']), ((1, 'pPaletteEntry'),(1, 'Use8BPPMaskPal'),(1, 'CMYMask'),(1, 'RedGamma'),(1, 'GreenGamma'),(1, 'BlueGamma'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngGetPrinterDataFileName():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.Devices.Display.HDEV)(('EngGetPrinterDataFileName', windll['GDI32.dll']), ((1, 'hdev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngGetDriverName():
    try:
        return WINFUNCTYPE(win32more.Foundation.PWSTR,win32more.Devices.Display.HDEV)(('EngGetDriverName', windll['GDI32.dll']), ((1, 'hdev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngLoadModule():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('EngLoadModule', windll['GDI32.dll']), ((1, 'pwsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngFindResource():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.HANDLE,Int32,Int32,POINTER(UInt32))(('EngFindResource', windll['GDI32.dll']), ((1, 'h'),(1, 'iName'),(1, 'iType'),(1, 'pulSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngFreeModule():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.HANDLE)(('EngFreeModule', windll['GDI32.dll']), ((1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngCreateSemaphore():
    try:
        return WINFUNCTYPE(win32more.Devices.Display.HSEMAPHORE,)(('EngCreateSemaphore', windll['GDI32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngAcquireSemaphore():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.Display.HSEMAPHORE)(('EngAcquireSemaphore', windll['GDI32.dll']), ((1, 'hsem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngReleaseSemaphore():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.Display.HSEMAPHORE)(('EngReleaseSemaphore', windll['GDI32.dll']), ((1, 'hsem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngDeleteSemaphore():
    try:
        return WINFUNCTYPE(Void,win32more.Devices.Display.HSEMAPHORE)(('EngDeleteSemaphore', windll['GDI32.dll']), ((1, 'hsem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngMultiByteToUnicodeN():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.PSTR,UInt32)(('EngMultiByteToUnicodeN', windll['GDI32.dll']), ((1, 'UnicodeString'),(1, 'MaxBytesInUnicodeString'),(1, 'BytesInUnicodeString'),(1, 'MultiByteString'),(1, 'BytesInMultiByteString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngUnicodeToMultiByteN():
    try:
        return WINFUNCTYPE(Void,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,UInt32)(('EngUnicodeToMultiByteN', windll['GDI32.dll']), ((1, 'MultiByteString'),(1, 'MaxBytesInMultiByteString'),(1, 'BytesInMultiByteString'),(1, 'UnicodeString'),(1, 'BytesInUnicodeString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngQueryLocalTime():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.ENG_TIME_FIELDS_head))(('EngQueryLocalTime', windll['GDI32.dll']), ((1, 'param0'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngComputeGlyphSet():
    try:
        return WINFUNCTYPE(POINTER(win32more.Devices.Display.FD_GLYPHSET_head),Int32,Int32,Int32)(('EngComputeGlyphSet', windll['GDI32.dll']), ((1, 'nCodePage'),(1, 'nFirstChar'),(1, 'cChars'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngMultiByteToWideChar():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR,Int32,win32more.Foundation.PSTR,Int32)(('EngMultiByteToWideChar', windll['GDI32.dll']), ((1, 'CodePage'),(1, 'WideCharString'),(1, 'BytesInWideCharString'),(1, 'MultiByteString'),(1, 'BytesInMultiByteString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngWideCharToMultiByte():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR,Int32,win32more.Foundation.PSTR,Int32)(('EngWideCharToMultiByte', windll['GDI32.dll']), ((1, 'CodePage'),(1, 'WideCharString'),(1, 'BytesInWideCharString'),(1, 'MultiByteString'),(1, 'BytesInMultiByteString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngGetCurrentCodePage():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt16),POINTER(UInt16))(('EngGetCurrentCodePage', windll['GDI32.dll']), ((1, 'OemCodePage'),(1, 'AnsiCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EngQueryEMFInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.HDEV,POINTER(win32more.Devices.Display.EMFINFO_head))(('EngQueryEMFInfo', windll['GDI32.dll']), ((1, 'hdev'),(1, 'pEMFInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDisplayConfigBufferSizes():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32),POINTER(UInt32))(('GetDisplayConfigBufferSizes', windll['USER32.dll']), ((1, 'flags'),(1, 'numPathArrayElements'),(1, 'numModeInfoArrayElements'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDisplayConfig():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(win32more.Devices.Display.DISPLAYCONFIG_PATH_INFO_head),UInt32,POINTER(win32more.Devices.Display.DISPLAYCONFIG_MODE_INFO_head),UInt32)(('SetDisplayConfig', windll['USER32.dll']), ((1, 'numPathArrayElements'),(1, 'pathArray'),(1, 'numModeInfoArrayElements'),(1, 'modeInfoArray'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDisplayConfig():
    try:
        return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32),POINTER(win32more.Devices.Display.DISPLAYCONFIG_PATH_INFO_head),POINTER(UInt32),POINTER(win32more.Devices.Display.DISPLAYCONFIG_MODE_INFO_head),POINTER(win32more.Devices.Display.DISPLAYCONFIG_TOPOLOGY_ID))(('QueryDisplayConfig', windll['USER32.dll']), ((1, 'flags'),(1, 'numPathArrayElements'),(1, 'pathArray'),(1, 'numModeInfoArrayElements'),(1, 'modeInfoArray'),(1, 'currentTopologyId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisplayConfigGetDeviceInfo():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER_head))(('DisplayConfigGetDeviceInfo', windll['USER32.dll']), ((1, 'requestPacket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DisplayConfigSetDeviceInfo():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER_head))(('DisplayConfigSetDeviceInfo', windll['USER32.dll']), ((1, 'setPacket'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAutoRotationState():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.AR_STATE))(('GetAutoRotationState', windll['USER32.dll']), ((1, 'pState'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDisplayAutoRotationPreferences():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.ORIENTATION_PREFERENCE))(('GetDisplayAutoRotationPreferences', windll['USER32.dll']), ((1, 'pOrientation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetDisplayAutoRotationPreferences():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.ORIENTATION_PREFERENCE)(('SetDisplayAutoRotationPreferences', windll['USER32.dll']), ((1, 'orientation'),))
    except (FileNotFoundError, AttributeError):
        return None
AR_STATE = Int32
AR_ENABLED = 0
AR_DISABLED = 1
AR_SUPPRESSED = 2
AR_REMOTESESSION = 4
AR_MULTIMON = 8
AR_NOSENSOR = 16
AR_NOT_SUPPORTED = 32
AR_DOCKED = 64
AR_LAPTOP = 128
BACKLIGHT_OPTIMIZATION_LEVEL = Int32
BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDisable = 0
BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDesktop = 1
BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDynamic = 2
BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDimmed = 3
BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationEDR = 4
def _define_BACKLIGHT_REDUCTION_GAMMA_RAMP_head():
    class BACKLIGHT_REDUCTION_GAMMA_RAMP(Structure):
        pass
    return BACKLIGHT_REDUCTION_GAMMA_RAMP
def _define_BACKLIGHT_REDUCTION_GAMMA_RAMP():
    BACKLIGHT_REDUCTION_GAMMA_RAMP = win32more.Devices.Display.BACKLIGHT_REDUCTION_GAMMA_RAMP_head
    BACKLIGHT_REDUCTION_GAMMA_RAMP._fields_ = [
        ('R', UInt16 * 256),
        ('G', UInt16 * 256),
        ('B', UInt16 * 256),
    ]
    return BACKLIGHT_REDUCTION_GAMMA_RAMP
def _define_BANK_POSITION_head():
    class BANK_POSITION(Structure):
        pass
    return BANK_POSITION
def _define_BANK_POSITION():
    BANK_POSITION = win32more.Devices.Display.BANK_POSITION_head
    BANK_POSITION._fields_ = [
        ('ReadBankPosition', UInt32),
        ('WriteBankPosition', UInt32),
    ]
    return BANK_POSITION
BlackScreenDiagnosticsCalloutParam = Int32
BlackScreenDiagnosticsCalloutParam_BlackScreenDiagnosticsData = 1
BlackScreenDiagnosticsCalloutParam_BlackScreenDisplayRecovery = 2
def _define_BLENDOBJ_head():
    class BLENDOBJ(Structure):
        pass
    return BLENDOBJ
def _define_BLENDOBJ():
    BLENDOBJ = win32more.Devices.Display.BLENDOBJ_head
    BLENDOBJ._fields_ = [
        ('BlendFunction', win32more.Graphics.Gdi.BLENDFUNCTION),
    ]
    return BLENDOBJ
BRIGHTNESS_INTERFACE_VERSION = Int32
BRIGHTNESS_INTERFACE_VERSION_1 = 1
BRIGHTNESS_INTERFACE_VERSION_2 = 2
BRIGHTNESS_INTERFACE_VERSION_3 = 3
def _define_BRIGHTNESS_LEVEL_head():
    class BRIGHTNESS_LEVEL(Structure):
        pass
    return BRIGHTNESS_LEVEL
def _define_BRIGHTNESS_LEVEL():
    BRIGHTNESS_LEVEL = win32more.Devices.Display.BRIGHTNESS_LEVEL_head
    BRIGHTNESS_LEVEL._fields_ = [
        ('Count', Byte),
        ('Level', Byte * 103),
    ]
    return BRIGHTNESS_LEVEL
def _define_BRIGHTNESS_NIT_RANGE_head():
    class BRIGHTNESS_NIT_RANGE(Structure):
        pass
    return BRIGHTNESS_NIT_RANGE
def _define_BRIGHTNESS_NIT_RANGE():
    BRIGHTNESS_NIT_RANGE = win32more.Devices.Display.BRIGHTNESS_NIT_RANGE_head
    BRIGHTNESS_NIT_RANGE._fields_ = [
        ('MinLevelInMillinit', UInt32),
        ('MaxLevelInMillinit', UInt32),
        ('StepSizeInMillinit', UInt32),
    ]
    return BRIGHTNESS_NIT_RANGE
def _define_BRIGHTNESS_NIT_RANGES_head():
    class BRIGHTNESS_NIT_RANGES(Structure):
        pass
    return BRIGHTNESS_NIT_RANGES
def _define_BRIGHTNESS_NIT_RANGES():
    BRIGHTNESS_NIT_RANGES = win32more.Devices.Display.BRIGHTNESS_NIT_RANGES_head
    BRIGHTNESS_NIT_RANGES._fields_ = [
        ('NormalRangeCount', UInt32),
        ('RangeCount', UInt32),
        ('PreferredMaximumBrightness', UInt32),
        ('SupportedRanges', win32more.Devices.Display.BRIGHTNESS_NIT_RANGE * 16),
    ]
    return BRIGHTNESS_NIT_RANGES
def _define_BRUSHOBJ_head():
    class BRUSHOBJ(Structure):
        pass
    return BRUSHOBJ
def _define_BRUSHOBJ():
    BRUSHOBJ = win32more.Devices.Display.BRUSHOBJ_head
    BRUSHOBJ._fields_ = [
        ('iSolidColor', UInt32),
        ('pvRbrush', c_void_p),
        ('flColorType', UInt32),
    ]
    return BRUSHOBJ
def _define_CDDDXGK_REDIRBITMAPPRESENTINFO_head():
    class CDDDXGK_REDIRBITMAPPRESENTINFO(Structure):
        pass
    return CDDDXGK_REDIRBITMAPPRESENTINFO
def _define_CDDDXGK_REDIRBITMAPPRESENTINFO():
    CDDDXGK_REDIRBITMAPPRESENTINFO = win32more.Devices.Display.CDDDXGK_REDIRBITMAPPRESENTINFO_head
    CDDDXGK_REDIRBITMAPPRESENTINFO._fields_ = [
        ('NumDirtyRects', UInt32),
        ('DirtyRect', POINTER(win32more.Foundation.RECT_head)),
        ('NumContexts', UInt32),
        ('hContext', win32more.Foundation.HANDLE * 65),
        ('bDoNotSynchronizeWithDxContent', win32more.Foundation.BOOLEAN),
    ]
    return CDDDXGK_REDIRBITMAPPRESENTINFO
def _define_CHAR_IMAGE_INFO_head():
    class CHAR_IMAGE_INFO(Structure):
        pass
    return CHAR_IMAGE_INFO
def _define_CHAR_IMAGE_INFO():
    CHAR_IMAGE_INFO = win32more.Devices.Display.CHAR_IMAGE_INFO_head
    CHAR_IMAGE_INFO._fields_ = [
        ('CharInfo', win32more.System.Console.CHAR_INFO),
        ('FontImageInfo', win32more.Devices.Display.FONT_IMAGE_INFO),
    ]
    return CHAR_IMAGE_INFO
def _define_CHROMATICITY_COORDINATE_head():
    class CHROMATICITY_COORDINATE(Structure):
        pass
    return CHROMATICITY_COORDINATE
def _define_CHROMATICITY_COORDINATE():
    CHROMATICITY_COORDINATE = win32more.Devices.Display.CHROMATICITY_COORDINATE_head
    CHROMATICITY_COORDINATE._fields_ = [
        ('x', Single),
        ('y', Single),
    ]
    return CHROMATICITY_COORDINATE
def _define_CIECHROMA_head():
    class CIECHROMA(Structure):
        pass
    return CIECHROMA
def _define_CIECHROMA():
    CIECHROMA = win32more.Devices.Display.CIECHROMA_head
    CIECHROMA._fields_ = [
        ('x', Int32),
        ('y', Int32),
        ('Y', Int32),
    ]
    return CIECHROMA
def _define_CLIPLINE_head():
    class CLIPLINE(Structure):
        pass
    return CLIPLINE
def _define_CLIPLINE():
    CLIPLINE = win32more.Devices.Display.CLIPLINE_head
    CLIPLINE._fields_ = [
        ('ptfxA', win32more.Devices.Display.POINTFIX),
        ('ptfxB', win32more.Devices.Display.POINTFIX),
        ('lStyleState', Int32),
        ('c', UInt32),
        ('arun', win32more.Devices.Display.RUN * 1),
    ]
    return CLIPLINE
def _define_CLIPOBJ_head():
    class CLIPOBJ(Structure):
        pass
    return CLIPOBJ
def _define_CLIPOBJ():
    CLIPOBJ = win32more.Devices.Display.CLIPOBJ_head
    CLIPOBJ._fields_ = [
        ('iUniq', UInt32),
        ('rclBounds', win32more.Foundation.RECTL),
        ('iDComplexity', Byte),
        ('iFComplexity', Byte),
        ('iMode', Byte),
        ('fjOptions', Byte),
    ]
    return CLIPOBJ
def _define_COLORINFO_head():
    class COLORINFO(Structure):
        pass
    return COLORINFO
def _define_COLORINFO():
    COLORINFO = win32more.Devices.Display.COLORINFO_head
    COLORINFO._fields_ = [
        ('Red', win32more.Devices.Display.CIECHROMA),
        ('Green', win32more.Devices.Display.CIECHROMA),
        ('Blue', win32more.Devices.Display.CIECHROMA),
        ('Cyan', win32more.Devices.Display.CIECHROMA),
        ('Magenta', win32more.Devices.Display.CIECHROMA),
        ('Yellow', win32more.Devices.Display.CIECHROMA),
        ('AlignmentWhite', win32more.Devices.Display.CIECHROMA),
        ('RedGamma', Int32),
        ('GreenGamma', Int32),
        ('BlueGamma', Int32),
        ('MagentaInCyanDye', Int32),
        ('YellowInCyanDye', Int32),
        ('CyanInMagentaDye', Int32),
        ('YellowInMagentaDye', Int32),
        ('CyanInYellowDye', Int32),
        ('MagentaInYellowDye', Int32),
    ]
    return COLORINFO
def _define_COLORSPACE_TRANSFORM_head():
    class COLORSPACE_TRANSFORM(Structure):
        pass
    return COLORSPACE_TRANSFORM
def _define_COLORSPACE_TRANSFORM():
    COLORSPACE_TRANSFORM = win32more.Devices.Display.COLORSPACE_TRANSFORM_head
    class COLORSPACE_TRANSFORM__Data_e__Union(Union):
        pass
    COLORSPACE_TRANSFORM__Data_e__Union._fields_ = [
        ('Rgb256x3x16', win32more.Devices.Display.GAMMA_RAMP_RGB256x3x16),
        ('Dxgi1', win32more.Devices.Display.GAMMA_RAMP_DXGI_1),
        ('T3x4', win32more.Devices.Display.COLORSPACE_TRANSFORM_3x4),
        ('MatrixV2', win32more.Devices.Display.COLORSPACE_TRANSFORM_MATRIX_V2),
    ]
    COLORSPACE_TRANSFORM._fields_ = [
        ('Type', win32more.Devices.Display.COLORSPACE_TRANSFORM_TYPE),
        ('Data', COLORSPACE_TRANSFORM__Data_e__Union),
    ]
    return COLORSPACE_TRANSFORM
def _define_COLORSPACE_TRANSFORM_1DLUT_CAP_head():
    class COLORSPACE_TRANSFORM_1DLUT_CAP(Structure):
        pass
    return COLORSPACE_TRANSFORM_1DLUT_CAP
def _define_COLORSPACE_TRANSFORM_1DLUT_CAP():
    COLORSPACE_TRANSFORM_1DLUT_CAP = win32more.Devices.Display.COLORSPACE_TRANSFORM_1DLUT_CAP_head
    COLORSPACE_TRANSFORM_1DLUT_CAP._fields_ = [
        ('NumberOfLUTEntries', UInt32),
        ('DataCap', win32more.Devices.Display.COLORSPACE_TRANSFORM_DATA_CAP),
    ]
    return COLORSPACE_TRANSFORM_1DLUT_CAP
def _define_COLORSPACE_TRANSFORM_3x4_head():
    class COLORSPACE_TRANSFORM_3x4(Structure):
        pass
    return COLORSPACE_TRANSFORM_3x4
def _define_COLORSPACE_TRANSFORM_3x4():
    COLORSPACE_TRANSFORM_3x4 = win32more.Devices.Display.COLORSPACE_TRANSFORM_3x4_head
    COLORSPACE_TRANSFORM_3x4._fields_ = [
        ('ColorMatrix3x4', Single * 12),
        ('ScalarMultiplier', Single),
        ('LookupTable1D', win32more.Devices.Display.GAMMA_RAMP_RGB * 4096),
    ]
    return COLORSPACE_TRANSFORM_3x4
def _define_COLORSPACE_TRANSFORM_DATA_CAP_head():
    class COLORSPACE_TRANSFORM_DATA_CAP(Structure):
        pass
    return COLORSPACE_TRANSFORM_DATA_CAP
def _define_COLORSPACE_TRANSFORM_DATA_CAP():
    COLORSPACE_TRANSFORM_DATA_CAP = win32more.Devices.Display.COLORSPACE_TRANSFORM_DATA_CAP_head
    class COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union(Union):
        pass
    class COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous1_e__Struct(Structure):
        pass
    COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous1_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    class COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous2_e__Struct(Structure):
        pass
    COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous2_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union._fields_ = [
        ('Anonymous1', COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous1_e__Struct),
        ('Anonymous2', COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union__Anonymous2_e__Struct),
        ('Value', UInt32),
    ]
    COLORSPACE_TRANSFORM_DATA_CAP._anonymous_ = [
        'Anonymous',
    ]
    COLORSPACE_TRANSFORM_DATA_CAP._fields_ = [
        ('DataType', win32more.Devices.Display.COLORSPACE_TRANSFORM_DATA_TYPE),
        ('Anonymous', COLORSPACE_TRANSFORM_DATA_CAP__Anonymous_e__Union),
        ('NumericRangeMin', Single),
        ('NumericRangeMax', Single),
    ]
    return COLORSPACE_TRANSFORM_DATA_CAP
COLORSPACE_TRANSFORM_DATA_TYPE = Int32
COLORSPACE_TRANSFORM_DATA_TYPE_FIXED_POINT = 0
COLORSPACE_TRANSFORM_DATA_TYPE_FLOAT = 1
def _define_COLORSPACE_TRANSFORM_MATRIX_CAP_head():
    class COLORSPACE_TRANSFORM_MATRIX_CAP(Structure):
        pass
    return COLORSPACE_TRANSFORM_MATRIX_CAP
def _define_COLORSPACE_TRANSFORM_MATRIX_CAP():
    COLORSPACE_TRANSFORM_MATRIX_CAP = win32more.Devices.Display.COLORSPACE_TRANSFORM_MATRIX_CAP_head
    class COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union(Union):
        pass
    class COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union._fields_ = [
        ('Anonymous', COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union__Anonymous_e__Struct),
        ('Value', UInt32),
    ]
    COLORSPACE_TRANSFORM_MATRIX_CAP._anonymous_ = [
        'Anonymous',
    ]
    COLORSPACE_TRANSFORM_MATRIX_CAP._fields_ = [
        ('Anonymous', COLORSPACE_TRANSFORM_MATRIX_CAP__Anonymous_e__Union),
        ('DataCap', win32more.Devices.Display.COLORSPACE_TRANSFORM_DATA_CAP),
    ]
    return COLORSPACE_TRANSFORM_MATRIX_CAP
def _define_COLORSPACE_TRANSFORM_MATRIX_V2_head():
    class COLORSPACE_TRANSFORM_MATRIX_V2(Structure):
        pass
    return COLORSPACE_TRANSFORM_MATRIX_V2
def _define_COLORSPACE_TRANSFORM_MATRIX_V2():
    COLORSPACE_TRANSFORM_MATRIX_V2 = win32more.Devices.Display.COLORSPACE_TRANSFORM_MATRIX_V2_head
    COLORSPACE_TRANSFORM_MATRIX_V2._fields_ = [
        ('StageControlLookupTable1DDegamma', win32more.Devices.Display.COLORSPACE_TRANSFORM_STAGE_CONTROL),
        ('LookupTable1DDegamma', win32more.Devices.Display.GAMMA_RAMP_RGB * 4096),
        ('StageControlColorMatrix3x3', win32more.Devices.Display.COLORSPACE_TRANSFORM_STAGE_CONTROL),
        ('ColorMatrix3x3', Single * 9),
        ('StageControlLookupTable1DRegamma', win32more.Devices.Display.COLORSPACE_TRANSFORM_STAGE_CONTROL),
        ('LookupTable1DRegamma', win32more.Devices.Display.GAMMA_RAMP_RGB * 4096),
    ]
    return COLORSPACE_TRANSFORM_MATRIX_V2
def _define_COLORSPACE_TRANSFORM_SET_INPUT_head():
    class COLORSPACE_TRANSFORM_SET_INPUT(Structure):
        pass
    return COLORSPACE_TRANSFORM_SET_INPUT
def _define_COLORSPACE_TRANSFORM_SET_INPUT():
    COLORSPACE_TRANSFORM_SET_INPUT = win32more.Devices.Display.COLORSPACE_TRANSFORM_SET_INPUT_head
    COLORSPACE_TRANSFORM_SET_INPUT._fields_ = [
        ('OutputWireColorSpaceExpected', win32more.Devices.Display.OUTPUT_WIRE_COLOR_SPACE_TYPE),
        ('OutputWireFormatExpected', win32more.Devices.Display.OUTPUT_WIRE_FORMAT),
        ('ColorSpaceTransform', win32more.Devices.Display.COLORSPACE_TRANSFORM),
    ]
    return COLORSPACE_TRANSFORM_SET_INPUT
COLORSPACE_TRANSFORM_STAGE_CONTROL = Int32
ColorSpaceTransformStageControl_No_Change = 0
ColorSpaceTransformStageControl_Enable = 1
ColorSpaceTransformStageControl_Bypass = 2
def _define_COLORSPACE_TRANSFORM_TARGET_CAPS_head():
    class COLORSPACE_TRANSFORM_TARGET_CAPS(Structure):
        pass
    return COLORSPACE_TRANSFORM_TARGET_CAPS
def _define_COLORSPACE_TRANSFORM_TARGET_CAPS():
    COLORSPACE_TRANSFORM_TARGET_CAPS = win32more.Devices.Display.COLORSPACE_TRANSFORM_TARGET_CAPS_head
    COLORSPACE_TRANSFORM_TARGET_CAPS._fields_ = [
        ('Version', win32more.Devices.Display.COLORSPACE_TRANSFORM_TARGET_CAPS_VERSION),
        ('LookupTable1DDegammaCap', win32more.Devices.Display.COLORSPACE_TRANSFORM_1DLUT_CAP),
        ('ColorMatrix3x3Cap', win32more.Devices.Display.COLORSPACE_TRANSFORM_MATRIX_CAP),
        ('LookupTable1DRegammaCap', win32more.Devices.Display.COLORSPACE_TRANSFORM_1DLUT_CAP),
    ]
    return COLORSPACE_TRANSFORM_TARGET_CAPS
COLORSPACE_TRANSFORM_TARGET_CAPS_VERSION = Int32
COLORSPACE_TRANSFORM_VERSION_DEFAULT = 0
COLORSPACE_TRANSFORM_VERSION_1 = 1
COLORSPACE_TRANSFORM_VERSION_NOT_SUPPORTED = 0
COLORSPACE_TRANSFORM_TYPE = Int32
COLORSPACE_TRANSFORM_TYPE_UNINITIALIZED = 0
COLORSPACE_TRANSFORM_TYPE_DEFAULT = 1
COLORSPACE_TRANSFORM_TYPE_RGB256x3x16 = 2
COLORSPACE_TRANSFORM_TYPE_DXGI_1 = 3
COLORSPACE_TRANSFORM_TYPE_MATRIX_3x4 = 4
COLORSPACE_TRANSFORM_TYPE_MATRIX_V2 = 5
def _define_DEVHTADJDATA_head():
    class DEVHTADJDATA(Structure):
        pass
    return DEVHTADJDATA
def _define_DEVHTADJDATA():
    DEVHTADJDATA = win32more.Devices.Display.DEVHTADJDATA_head
    DEVHTADJDATA._fields_ = [
        ('DeviceFlags', UInt32),
        ('DeviceXDPI', UInt32),
        ('DeviceYDPI', UInt32),
        ('pDefHTInfo', POINTER(win32more.Devices.Display.DEVHTINFO_head)),
        ('pAdjHTInfo', POINTER(win32more.Devices.Display.DEVHTINFO_head)),
    ]
    return DEVHTADJDATA
def _define_DEVHTINFO_head():
    class DEVHTINFO(Structure):
        pass
    return DEVHTINFO
def _define_DEVHTINFO():
    DEVHTINFO = win32more.Devices.Display.DEVHTINFO_head
    DEVHTINFO._fields_ = [
        ('HTFlags', UInt32),
        ('HTPatternSize', UInt32),
        ('DevPelsDPI', UInt32),
        ('ColorInfo', win32more.Devices.Display.COLORINFO),
    ]
    return DEVHTINFO
def _define_DEVINFO_head():
    class DEVINFO(Structure):
        pass
    return DEVINFO
def _define_DEVINFO():
    DEVINFO = win32more.Devices.Display.DEVINFO_head
    DEVINFO._fields_ = [
        ('flGraphicsCaps', UInt32),
        ('lfDefaultFont', win32more.Graphics.Gdi.LOGFONTW),
        ('lfAnsiVarFont', win32more.Graphics.Gdi.LOGFONTW),
        ('lfAnsiFixFont', win32more.Graphics.Gdi.LOGFONTW),
        ('cFonts', UInt32),
        ('iDitherFormat', UInt32),
        ('cxDither', UInt16),
        ('cyDither', UInt16),
        ('hpalDefault', win32more.Graphics.Gdi.HPALETTE),
        ('flGraphicsCaps2', UInt32),
    ]
    return DEVINFO
DHPDEV = IntPtr
DHSURF = IntPtr
def _define_DISPLAY_BRIGHTNESS_head():
    class DISPLAY_BRIGHTNESS(Structure):
        pass
    return DISPLAY_BRIGHTNESS
def _define_DISPLAY_BRIGHTNESS():
    DISPLAY_BRIGHTNESS = win32more.Devices.Display.DISPLAY_BRIGHTNESS_head
    DISPLAY_BRIGHTNESS._fields_ = [
        ('ucDisplayPolicy', Byte),
        ('ucACBrightness', Byte),
        ('ucDCBrightness', Byte),
    ]
    return DISPLAY_BRIGHTNESS
def _define_DISPLAYCONFIG_2DREGION_head():
    class DISPLAYCONFIG_2DREGION(Structure):
        pass
    return DISPLAYCONFIG_2DREGION
def _define_DISPLAYCONFIG_2DREGION():
    DISPLAYCONFIG_2DREGION = win32more.Devices.Display.DISPLAYCONFIG_2DREGION_head
    DISPLAYCONFIG_2DREGION._fields_ = [
        ('cx', UInt32),
        ('cy', UInt32),
    ]
    return DISPLAYCONFIG_2DREGION
def _define_DISPLAYCONFIG_ADAPTER_NAME_head():
    class DISPLAYCONFIG_ADAPTER_NAME(Structure):
        pass
    return DISPLAYCONFIG_ADAPTER_NAME
def _define_DISPLAYCONFIG_ADAPTER_NAME():
    DISPLAYCONFIG_ADAPTER_NAME = win32more.Devices.Display.DISPLAYCONFIG_ADAPTER_NAME_head
    DISPLAYCONFIG_ADAPTER_NAME._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('adapterDevicePath', Char * 128),
    ]
    return DISPLAYCONFIG_ADAPTER_NAME
def _define_DISPLAYCONFIG_DESKTOP_IMAGE_INFO_head():
    class DISPLAYCONFIG_DESKTOP_IMAGE_INFO(Structure):
        pass
    return DISPLAYCONFIG_DESKTOP_IMAGE_INFO
def _define_DISPLAYCONFIG_DESKTOP_IMAGE_INFO():
    DISPLAYCONFIG_DESKTOP_IMAGE_INFO = win32more.Devices.Display.DISPLAYCONFIG_DESKTOP_IMAGE_INFO_head
    DISPLAYCONFIG_DESKTOP_IMAGE_INFO._fields_ = [
        ('PathSourceSize', win32more.Foundation.POINTL),
        ('DesktopImageRegion', win32more.Foundation.RECTL),
        ('DesktopImageClip', win32more.Foundation.RECTL),
    ]
    return DISPLAYCONFIG_DESKTOP_IMAGE_INFO
def _define_DISPLAYCONFIG_DEVICE_INFO_HEADER_head():
    class DISPLAYCONFIG_DEVICE_INFO_HEADER(Structure):
        pass
    return DISPLAYCONFIG_DEVICE_INFO_HEADER
def _define_DISPLAYCONFIG_DEVICE_INFO_HEADER():
    DISPLAYCONFIG_DEVICE_INFO_HEADER = win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER_head
    DISPLAYCONFIG_DEVICE_INFO_HEADER._fields_ = [
        ('type', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_TYPE),
        ('size', UInt32),
        ('adapterId', win32more.Foundation.LUID),
        ('id', UInt32),
    ]
    return DISPLAYCONFIG_DEVICE_INFO_HEADER
DISPLAYCONFIG_DEVICE_INFO_TYPE = Int32
DISPLAYCONFIG_DEVICE_INFO_GET_SOURCE_NAME = 1
DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME = 2
DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_PREFERRED_MODE = 3
DISPLAYCONFIG_DEVICE_INFO_GET_ADAPTER_NAME = 4
DISPLAYCONFIG_DEVICE_INFO_SET_TARGET_PERSISTENCE = 5
DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_BASE_TYPE = 6
DISPLAYCONFIG_DEVICE_INFO_GET_SUPPORT_VIRTUAL_RESOLUTION = 7
DISPLAYCONFIG_DEVICE_INFO_SET_SUPPORT_VIRTUAL_RESOLUTION = 8
DISPLAYCONFIG_DEVICE_INFO_GET_ADVANCED_COLOR_INFO = 9
DISPLAYCONFIG_DEVICE_INFO_SET_ADVANCED_COLOR_STATE = 10
DISPLAYCONFIG_DEVICE_INFO_GET_SDR_WHITE_LEVEL = 11
DISPLAYCONFIG_DEVICE_INFO_GET_MONITOR_SPECIALIZATION = 12
DISPLAYCONFIG_DEVICE_INFO_SET_MONITOR_SPECIALIZATION = 13
DISPLAYCONFIG_DEVICE_INFO_FORCE_UINT32 = -1
def _define_DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO_head():
    class DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO(Structure):
        pass
    return DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO
def _define_DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO():
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO = win32more.Devices.Display.DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO_head
    class DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO__Anonymous_e__Union),
        ('colorEncoding', win32more.Graphics.Gdi.DISPLAYCONFIG_COLOR_ENCODING),
        ('bitsPerColorChannel', UInt32),
    ]
    return DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO
def _define_DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION_head():
    class DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION(Structure):
        pass
    return DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION
def _define_DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION():
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION = win32more.Devices.Display.DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION_head
    class DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION
def _define_DISPLAYCONFIG_MODE_INFO_head():
    class DISPLAYCONFIG_MODE_INFO(Structure):
        pass
    return DISPLAYCONFIG_MODE_INFO
def _define_DISPLAYCONFIG_MODE_INFO():
    DISPLAYCONFIG_MODE_INFO = win32more.Devices.Display.DISPLAYCONFIG_MODE_INFO_head
    class DISPLAYCONFIG_MODE_INFO__Anonymous_e__Union(Union):
        pass
    DISPLAYCONFIG_MODE_INFO__Anonymous_e__Union._fields_ = [
        ('targetMode', win32more.Devices.Display.DISPLAYCONFIG_TARGET_MODE),
        ('sourceMode', win32more.Devices.Display.DISPLAYCONFIG_SOURCE_MODE),
        ('desktopImageInfo', win32more.Devices.Display.DISPLAYCONFIG_DESKTOP_IMAGE_INFO),
    ]
    DISPLAYCONFIG_MODE_INFO._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_MODE_INFO._fields_ = [
        ('infoType', win32more.Devices.Display.DISPLAYCONFIG_MODE_INFO_TYPE),
        ('id', UInt32),
        ('adapterId', win32more.Foundation.LUID),
        ('Anonymous', DISPLAYCONFIG_MODE_INFO__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_MODE_INFO
DISPLAYCONFIG_MODE_INFO_TYPE = Int32
DISPLAYCONFIG_MODE_INFO_TYPE_SOURCE = 1
DISPLAYCONFIG_MODE_INFO_TYPE_TARGET = 2
DISPLAYCONFIG_MODE_INFO_TYPE_DESKTOP_IMAGE = 3
DISPLAYCONFIG_MODE_INFO_TYPE_FORCE_UINT32 = -1
def _define_DISPLAYCONFIG_PATH_INFO_head():
    class DISPLAYCONFIG_PATH_INFO(Structure):
        pass
    return DISPLAYCONFIG_PATH_INFO
def _define_DISPLAYCONFIG_PATH_INFO():
    DISPLAYCONFIG_PATH_INFO = win32more.Devices.Display.DISPLAYCONFIG_PATH_INFO_head
    DISPLAYCONFIG_PATH_INFO._fields_ = [
        ('sourceInfo', win32more.Devices.Display.DISPLAYCONFIG_PATH_SOURCE_INFO),
        ('targetInfo', win32more.Devices.Display.DISPLAYCONFIG_PATH_TARGET_INFO),
        ('flags', UInt32),
    ]
    return DISPLAYCONFIG_PATH_INFO
def _define_DISPLAYCONFIG_PATH_SOURCE_INFO_head():
    class DISPLAYCONFIG_PATH_SOURCE_INFO(Structure):
        pass
    return DISPLAYCONFIG_PATH_SOURCE_INFO
def _define_DISPLAYCONFIG_PATH_SOURCE_INFO():
    DISPLAYCONFIG_PATH_SOURCE_INFO = win32more.Devices.Display.DISPLAYCONFIG_PATH_SOURCE_INFO_head
    class DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union._fields_ = [
        ('modeInfoIdx', UInt32),
        ('Anonymous', DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    DISPLAYCONFIG_PATH_SOURCE_INFO._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_PATH_SOURCE_INFO._fields_ = [
        ('adapterId', win32more.Foundation.LUID),
        ('id', UInt32),
        ('Anonymous', DISPLAYCONFIG_PATH_SOURCE_INFO__Anonymous_e__Union),
        ('statusFlags', UInt32),
    ]
    return DISPLAYCONFIG_PATH_SOURCE_INFO
def _define_DISPLAYCONFIG_PATH_TARGET_INFO_head():
    class DISPLAYCONFIG_PATH_TARGET_INFO(Structure):
        pass
    return DISPLAYCONFIG_PATH_TARGET_INFO
def _define_DISPLAYCONFIG_PATH_TARGET_INFO():
    DISPLAYCONFIG_PATH_TARGET_INFO = win32more.Devices.Display.DISPLAYCONFIG_PATH_TARGET_INFO_head
    class DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union._fields_ = [
        ('modeInfoIdx', UInt32),
        ('Anonymous', DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    DISPLAYCONFIG_PATH_TARGET_INFO._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_PATH_TARGET_INFO._fields_ = [
        ('adapterId', win32more.Foundation.LUID),
        ('id', UInt32),
        ('Anonymous', DISPLAYCONFIG_PATH_TARGET_INFO__Anonymous_e__Union),
        ('outputTechnology', win32more.Devices.Display.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY),
        ('rotation', win32more.Devices.Display.DISPLAYCONFIG_ROTATION),
        ('scaling', win32more.Devices.Display.DISPLAYCONFIG_SCALING),
        ('refreshRate', win32more.Devices.Display.DISPLAYCONFIG_RATIONAL),
        ('scanLineOrdering', win32more.Devices.Display.DISPLAYCONFIG_SCANLINE_ORDERING),
        ('targetAvailable', win32more.Foundation.BOOL),
        ('statusFlags', UInt32),
    ]
    return DISPLAYCONFIG_PATH_TARGET_INFO
DISPLAYCONFIG_PIXELFORMAT = Int32
DISPLAYCONFIG_PIXELFORMAT_8BPP = 1
DISPLAYCONFIG_PIXELFORMAT_16BPP = 2
DISPLAYCONFIG_PIXELFORMAT_24BPP = 3
DISPLAYCONFIG_PIXELFORMAT_32BPP = 4
DISPLAYCONFIG_PIXELFORMAT_NONGDI = 5
DISPLAYCONFIG_PIXELFORMAT_FORCE_UINT32 = -1
def _define_DISPLAYCONFIG_RATIONAL_head():
    class DISPLAYCONFIG_RATIONAL(Structure):
        pass
    return DISPLAYCONFIG_RATIONAL
def _define_DISPLAYCONFIG_RATIONAL():
    DISPLAYCONFIG_RATIONAL = win32more.Devices.Display.DISPLAYCONFIG_RATIONAL_head
    DISPLAYCONFIG_RATIONAL._fields_ = [
        ('Numerator', UInt32),
        ('Denominator', UInt32),
    ]
    return DISPLAYCONFIG_RATIONAL
DISPLAYCONFIG_ROTATION = Int32
DISPLAYCONFIG_ROTATION_IDENTITY = 1
DISPLAYCONFIG_ROTATION_ROTATE90 = 2
DISPLAYCONFIG_ROTATION_ROTATE180 = 3
DISPLAYCONFIG_ROTATION_ROTATE270 = 4
DISPLAYCONFIG_ROTATION_FORCE_UINT32 = -1
DISPLAYCONFIG_SCALING = Int32
DISPLAYCONFIG_SCALING_IDENTITY = 1
DISPLAYCONFIG_SCALING_CENTERED = 2
DISPLAYCONFIG_SCALING_STRETCHED = 3
DISPLAYCONFIG_SCALING_ASPECTRATIOCENTEREDMAX = 4
DISPLAYCONFIG_SCALING_CUSTOM = 5
DISPLAYCONFIG_SCALING_PREFERRED = 128
DISPLAYCONFIG_SCALING_FORCE_UINT32 = -1
DISPLAYCONFIG_SCANLINE_ORDERING = Int32
DISPLAYCONFIG_SCANLINE_ORDERING_UNSPECIFIED = 0
DISPLAYCONFIG_SCANLINE_ORDERING_PROGRESSIVE = 1
DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED = 2
DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_UPPERFIELDFIRST = 2
DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_LOWERFIELDFIRST = 3
DISPLAYCONFIG_SCANLINE_ORDERING_FORCE_UINT32 = -1
def _define_DISPLAYCONFIG_SDR_WHITE_LEVEL_head():
    class DISPLAYCONFIG_SDR_WHITE_LEVEL(Structure):
        pass
    return DISPLAYCONFIG_SDR_WHITE_LEVEL
def _define_DISPLAYCONFIG_SDR_WHITE_LEVEL():
    DISPLAYCONFIG_SDR_WHITE_LEVEL = win32more.Devices.Display.DISPLAYCONFIG_SDR_WHITE_LEVEL_head
    DISPLAYCONFIG_SDR_WHITE_LEVEL._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('SDRWhiteLevel', UInt32),
    ]
    return DISPLAYCONFIG_SDR_WHITE_LEVEL
def _define_DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE_head():
    class DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE(Structure):
        pass
    return DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE
def _define_DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE():
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE = win32more.Devices.Display.DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE_head
    class DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE
def _define_DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION_head():
    class DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION(Structure):
        pass
    return DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION
def _define_DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION():
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION = win32more.Devices.Display.DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION_head
    class DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION__Anonymous_e__Union),
        ('specializationType', Guid),
        ('specializationSubType', Guid),
        ('specializationApplicationName', Char * 128),
    ]
    return DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION
def _define_DISPLAYCONFIG_SET_TARGET_PERSISTENCE_head():
    class DISPLAYCONFIG_SET_TARGET_PERSISTENCE(Structure):
        pass
    return DISPLAYCONFIG_SET_TARGET_PERSISTENCE
def _define_DISPLAYCONFIG_SET_TARGET_PERSISTENCE():
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE = win32more.Devices.Display.DISPLAYCONFIG_SET_TARGET_PERSISTENCE_head
    class DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SET_TARGET_PERSISTENCE._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_SET_TARGET_PERSISTENCE__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_SET_TARGET_PERSISTENCE
def _define_DISPLAYCONFIG_SOURCE_DEVICE_NAME_head():
    class DISPLAYCONFIG_SOURCE_DEVICE_NAME(Structure):
        pass
    return DISPLAYCONFIG_SOURCE_DEVICE_NAME
def _define_DISPLAYCONFIG_SOURCE_DEVICE_NAME():
    DISPLAYCONFIG_SOURCE_DEVICE_NAME = win32more.Devices.Display.DISPLAYCONFIG_SOURCE_DEVICE_NAME_head
    DISPLAYCONFIG_SOURCE_DEVICE_NAME._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('viewGdiDeviceName', Char * 32),
    ]
    return DISPLAYCONFIG_SOURCE_DEVICE_NAME
def _define_DISPLAYCONFIG_SOURCE_MODE_head():
    class DISPLAYCONFIG_SOURCE_MODE(Structure):
        pass
    return DISPLAYCONFIG_SOURCE_MODE
def _define_DISPLAYCONFIG_SOURCE_MODE():
    DISPLAYCONFIG_SOURCE_MODE = win32more.Devices.Display.DISPLAYCONFIG_SOURCE_MODE_head
    DISPLAYCONFIG_SOURCE_MODE._fields_ = [
        ('width', UInt32),
        ('height', UInt32),
        ('pixelFormat', win32more.Devices.Display.DISPLAYCONFIG_PIXELFORMAT),
        ('position', win32more.Foundation.POINTL),
    ]
    return DISPLAYCONFIG_SOURCE_MODE
def _define_DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION_head():
    class DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION(Structure):
        pass
    return DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION
def _define_DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION():
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION = win32more.Devices.Display.DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION_head
    class DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('Anonymous', DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION
def _define_DISPLAYCONFIG_TARGET_BASE_TYPE_head():
    class DISPLAYCONFIG_TARGET_BASE_TYPE(Structure):
        pass
    return DISPLAYCONFIG_TARGET_BASE_TYPE
def _define_DISPLAYCONFIG_TARGET_BASE_TYPE():
    DISPLAYCONFIG_TARGET_BASE_TYPE = win32more.Devices.Display.DISPLAYCONFIG_TARGET_BASE_TYPE_head
    DISPLAYCONFIG_TARGET_BASE_TYPE._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('baseOutputTechnology', win32more.Devices.Display.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY),
    ]
    return DISPLAYCONFIG_TARGET_BASE_TYPE
def _define_DISPLAYCONFIG_TARGET_DEVICE_NAME_head():
    class DISPLAYCONFIG_TARGET_DEVICE_NAME(Structure):
        pass
    return DISPLAYCONFIG_TARGET_DEVICE_NAME
def _define_DISPLAYCONFIG_TARGET_DEVICE_NAME():
    DISPLAYCONFIG_TARGET_DEVICE_NAME = win32more.Devices.Display.DISPLAYCONFIG_TARGET_DEVICE_NAME_head
    DISPLAYCONFIG_TARGET_DEVICE_NAME._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('flags', win32more.Devices.Display.DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS),
        ('outputTechnology', win32more.Devices.Display.DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY),
        ('edidManufactureId', UInt16),
        ('edidProductCodeId', UInt16),
        ('connectorInstance', UInt32),
        ('monitorFriendlyDeviceName', Char * 64),
        ('monitorDevicePath', Char * 128),
    ]
    return DISPLAYCONFIG_TARGET_DEVICE_NAME
def _define_DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_head():
    class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS(Structure):
        pass
    return DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS
def _define_DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS():
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS = win32more.Devices.Display.DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS_head
    class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union._fields_ = [
        ('Anonymous', DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union__Anonymous_e__Struct),
        ('value', UInt32),
    ]
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS._fields_ = [
        ('Anonymous', DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS__Anonymous_e__Union),
    ]
    return DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS
def _define_DISPLAYCONFIG_TARGET_MODE_head():
    class DISPLAYCONFIG_TARGET_MODE(Structure):
        pass
    return DISPLAYCONFIG_TARGET_MODE
def _define_DISPLAYCONFIG_TARGET_MODE():
    DISPLAYCONFIG_TARGET_MODE = win32more.Devices.Display.DISPLAYCONFIG_TARGET_MODE_head
    DISPLAYCONFIG_TARGET_MODE._fields_ = [
        ('targetVideoSignalInfo', win32more.Devices.Display.DISPLAYCONFIG_VIDEO_SIGNAL_INFO),
    ]
    return DISPLAYCONFIG_TARGET_MODE
def _define_DISPLAYCONFIG_TARGET_PREFERRED_MODE_head():
    class DISPLAYCONFIG_TARGET_PREFERRED_MODE(Structure):
        pass
    return DISPLAYCONFIG_TARGET_PREFERRED_MODE
def _define_DISPLAYCONFIG_TARGET_PREFERRED_MODE():
    DISPLAYCONFIG_TARGET_PREFERRED_MODE = win32more.Devices.Display.DISPLAYCONFIG_TARGET_PREFERRED_MODE_head
    DISPLAYCONFIG_TARGET_PREFERRED_MODE._fields_ = [
        ('header', win32more.Devices.Display.DISPLAYCONFIG_DEVICE_INFO_HEADER),
        ('width', UInt32),
        ('height', UInt32),
        ('targetMode', win32more.Devices.Display.DISPLAYCONFIG_TARGET_MODE),
    ]
    return DISPLAYCONFIG_TARGET_PREFERRED_MODE
DISPLAYCONFIG_TOPOLOGY_ID = Int32
DISPLAYCONFIG_TOPOLOGY_INTERNAL = 1
DISPLAYCONFIG_TOPOLOGY_CLONE = 2
DISPLAYCONFIG_TOPOLOGY_EXTEND = 4
DISPLAYCONFIG_TOPOLOGY_EXTERNAL = 8
DISPLAYCONFIG_TOPOLOGY_FORCE_UINT32 = -1
DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY = Int32
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_OTHER = -1
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HD15 = 0
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SVIDEO = 1
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPOSITE_VIDEO = 2
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPONENT_VIDEO = 3
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DVI = 4
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HDMI = 5
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_LVDS = 6
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_D_JPN = 8
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDI = 9
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EXTERNAL = 10
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EMBEDDED = 11
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EXTERNAL = 12
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EMBEDDED = 13
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDTVDONGLE = 14
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST = 15
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_WIRED = 16
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_VIRTUAL = 17
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_USB_TUNNEL = 18
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INTERNAL = -2147483648
DISPLAYCONFIG_OUTPUT_TECHNOLOGY_FORCE_UINT32 = -1
def _define_DISPLAYCONFIG_VIDEO_SIGNAL_INFO_head():
    class DISPLAYCONFIG_VIDEO_SIGNAL_INFO(Structure):
        pass
    return DISPLAYCONFIG_VIDEO_SIGNAL_INFO
def _define_DISPLAYCONFIG_VIDEO_SIGNAL_INFO():
    DISPLAYCONFIG_VIDEO_SIGNAL_INFO = win32more.Devices.Display.DISPLAYCONFIG_VIDEO_SIGNAL_INFO_head
    class DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union(Union):
        pass
    class DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union__AdditionalSignalInfo_e__Struct(Structure):
        pass
    DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union__AdditionalSignalInfo_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union._fields_ = [
        ('AdditionalSignalInfo', DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union__AdditionalSignalInfo_e__Struct),
        ('videoStandard', UInt32),
    ]
    DISPLAYCONFIG_VIDEO_SIGNAL_INFO._anonymous_ = [
        'Anonymous',
    ]
    DISPLAYCONFIG_VIDEO_SIGNAL_INFO._fields_ = [
        ('pixelRate', UInt64),
        ('hSyncFreq', win32more.Devices.Display.DISPLAYCONFIG_RATIONAL),
        ('vSyncFreq', win32more.Devices.Display.DISPLAYCONFIG_RATIONAL),
        ('activeSize', win32more.Devices.Display.DISPLAYCONFIG_2DREGION),
        ('totalSize', win32more.Devices.Display.DISPLAYCONFIG_2DREGION),
        ('Anonymous', DISPLAYCONFIG_VIDEO_SIGNAL_INFO__Anonymous_e__Union),
        ('scanLineOrdering', win32more.Devices.Display.DISPLAYCONFIG_SCANLINE_ORDERING),
    ]
    return DISPLAYCONFIG_VIDEO_SIGNAL_INFO
def _define_DisplayMode_head():
    class DisplayMode(Structure):
        pass
    return DisplayMode
def _define_DisplayMode():
    DisplayMode = win32more.Devices.Display.DisplayMode_head
    DisplayMode._fields_ = [
        ('DeviceName', Char * 32),
        ('devMode', win32more.Graphics.Gdi.DEVMODEW),
    ]
    return DisplayMode
def _define_DisplayModes_head():
    class DisplayModes(Structure):
        pass
    return DisplayModes
def _define_DisplayModes():
    DisplayModes = win32more.Devices.Display.DisplayModes_head
    DisplayModes._fields_ = [
        ('numDisplayModes', Int32),
        ('displayMode', win32more.Devices.Display.DisplayMode * 1),
    ]
    return DisplayModes
def _define_DRH_APIBITMAPDATA_head():
    class DRH_APIBITMAPDATA(Structure):
        pass
    return DRH_APIBITMAPDATA
def _define_DRH_APIBITMAPDATA():
    DRH_APIBITMAPDATA = win32more.Devices.Display.DRH_APIBITMAPDATA_head
    DRH_APIBITMAPDATA._fields_ = [
        ('pso', POINTER(win32more.Devices.Display.SURFOBJ_head)),
        ('b', win32more.Foundation.BOOL),
    ]
    return DRH_APIBITMAPDATA
def _define_DRIVEROBJ_head():
    class DRIVEROBJ(Structure):
        pass
    return DRIVEROBJ
def _define_DRIVEROBJ():
    DRIVEROBJ = win32more.Devices.Display.DRIVEROBJ_head
    DRIVEROBJ._fields_ = [
        ('pvObj', c_void_p),
        ('pFreeProc', win32more.Devices.Display.FREEOBJPROC),
        ('hdev', win32more.Devices.Display.HDEV),
        ('dhpdev', win32more.Devices.Display.DHPDEV),
    ]
    return DRIVEROBJ
def _define_DRVENABLEDATA_head():
    class DRVENABLEDATA(Structure):
        pass
    return DRVENABLEDATA
def _define_DRVENABLEDATA():
    DRVENABLEDATA = win32more.Devices.Display.DRVENABLEDATA_head
    DRVENABLEDATA._fields_ = [
        ('iDriverVersion', UInt32),
        ('c', UInt32),
        ('pdrvfn', POINTER(win32more.Devices.Display.DRVFN_head)),
    ]
    return DRVENABLEDATA
def _define_DRVFN_head():
    class DRVFN(Structure):
        pass
    return DRVFN
def _define_DRVFN():
    DRVFN = win32more.Devices.Display.DRVFN_head
    DRVFN._fields_ = [
        ('iFunc', UInt32),
        ('pfn', win32more.Devices.Display.PFN),
    ]
    return DRVFN
DSI_CONTROL_TRANSMISSION_MODE = Int32
DCT_DEFAULT = 0
DCT_FORCE_LOW_POWER = 1
DCT_FORCE_HIGH_PERFORMANCE = 2
def _define_DXGK_WIN32K_PARAM_DATA_head():
    class DXGK_WIN32K_PARAM_DATA(Structure):
        pass
    return DXGK_WIN32K_PARAM_DATA
def _define_DXGK_WIN32K_PARAM_DATA():
    DXGK_WIN32K_PARAM_DATA = win32more.Devices.Display.DXGK_WIN32K_PARAM_DATA_head
    DXGK_WIN32K_PARAM_DATA._fields_ = [
        ('PathsArray', c_void_p),
        ('ModesArray', c_void_p),
        ('NumPathArrayElements', UInt32),
        ('NumModeArrayElements', UInt32),
        ('SDCFlags', UInt32),
    ]
    return DXGK_WIN32K_PARAM_DATA
def _define_EMFINFO_head():
    class EMFINFO(Structure):
        pass
    return EMFINFO
def _define_EMFINFO():
    EMFINFO = win32more.Devices.Display.EMFINFO_head
    EMFINFO._fields_ = [
        ('nSize', UInt32),
        ('hdc', win32more.Graphics.Gdi.HDC),
        ('pvEMF', c_char_p_no),
        ('pvCurrentRecord', c_char_p_no),
    ]
    return EMFINFO
ENG_DEVICE_ATTRIBUTE = Int32
QDA_RESERVED = 0
QDA_ACCELERATION_LEVEL = 1
def _define_ENG_EVENT_head():
    class ENG_EVENT(Structure):
        pass
    return ENG_EVENT
def _define_ENG_EVENT():
    ENG_EVENT = win32more.Devices.Display.ENG_EVENT_head
    ENG_EVENT._fields_ = [
        ('pKEvent', c_void_p),
        ('fFlags', UInt32),
    ]
    return ENG_EVENT
ENG_SYSTEM_ATTRIBUTE = Int32
ENG_SYSTEM_ATTRIBUTE_EngProcessorFeature = 1
ENG_SYSTEM_ATTRIBUTE_EngNumberOfProcessors = 2
ENG_SYSTEM_ATTRIBUTE_EngOptimumAvailableUserMemory = 3
ENG_SYSTEM_ATTRIBUTE_EngOptimumAvailableSystemMemory = 4
def _define_ENG_TIME_FIELDS_head():
    class ENG_TIME_FIELDS(Structure):
        pass
    return ENG_TIME_FIELDS
def _define_ENG_TIME_FIELDS():
    ENG_TIME_FIELDS = win32more.Devices.Display.ENG_TIME_FIELDS_head
    ENG_TIME_FIELDS._fields_ = [
        ('usYear', UInt16),
        ('usMonth', UInt16),
        ('usDay', UInt16),
        ('usHour', UInt16),
        ('usMinute', UInt16),
        ('usSecond', UInt16),
        ('usMilliseconds', UInt16),
        ('usWeekday', UInt16),
    ]
    return ENG_TIME_FIELDS
def _define_ENGSAFESEMAPHORE_head():
    class ENGSAFESEMAPHORE(Structure):
        pass
    return ENGSAFESEMAPHORE
def _define_ENGSAFESEMAPHORE():
    ENGSAFESEMAPHORE = win32more.Devices.Display.ENGSAFESEMAPHORE_head
    ENGSAFESEMAPHORE._fields_ = [
        ('hsem', win32more.Devices.Display.HSEMAPHORE),
        ('lCount', Int32),
    ]
    return ENGSAFESEMAPHORE
def _define_ENUMRECTS_head():
    class ENUMRECTS(Structure):
        pass
    return ENUMRECTS
def _define_ENUMRECTS():
    ENUMRECTS = win32more.Devices.Display.ENUMRECTS_head
    ENUMRECTS._fields_ = [
        ('c', UInt32),
        ('arcl', win32more.Foundation.RECTL * 1),
    ]
    return ENUMRECTS
def _define_FD_DEVICEMETRICS_head():
    class FD_DEVICEMETRICS(Structure):
        pass
    return FD_DEVICEMETRICS
def _define_FD_DEVICEMETRICS():
    FD_DEVICEMETRICS = win32more.Devices.Display.FD_DEVICEMETRICS_head
    FD_DEVICEMETRICS._fields_ = [
        ('flRealizedType', UInt32),
        ('pteBase', win32more.Devices.Display.POINTE),
        ('pteSide', win32more.Devices.Display.POINTE),
        ('lD', Int32),
        ('fxMaxAscender', Int32),
        ('fxMaxDescender', Int32),
        ('ptlUnderline1', win32more.Foundation.POINTL),
        ('ptlStrikeOut', win32more.Foundation.POINTL),
        ('ptlULThickness', win32more.Foundation.POINTL),
        ('ptlSOThickness', win32more.Foundation.POINTL),
        ('cxMax', UInt32),
        ('cyMax', UInt32),
        ('cjGlyphMax', UInt32),
        ('fdxQuantized', win32more.Devices.Display.FD_XFORM),
        ('lNonLinearExtLeading', Int32),
        ('lNonLinearIntLeading', Int32),
        ('lNonLinearMaxCharWidth', Int32),
        ('lNonLinearAvgCharWidth', Int32),
        ('lMinA', Int32),
        ('lMinC', Int32),
        ('lMinD', Int32),
        ('alReserved', Int32 * 1),
    ]
    return FD_DEVICEMETRICS
def _define_FD_GLYPHATTR_head():
    class FD_GLYPHATTR(Structure):
        pass
    return FD_GLYPHATTR
def _define_FD_GLYPHATTR():
    FD_GLYPHATTR = win32more.Devices.Display.FD_GLYPHATTR_head
    FD_GLYPHATTR._fields_ = [
        ('cjThis', UInt32),
        ('cGlyphs', UInt32),
        ('iMode', UInt32),
        ('aGlyphAttr', Byte * 1),
    ]
    return FD_GLYPHATTR
def _define_FD_GLYPHSET_head():
    class FD_GLYPHSET(Structure):
        pass
    return FD_GLYPHSET
def _define_FD_GLYPHSET():
    FD_GLYPHSET = win32more.Devices.Display.FD_GLYPHSET_head
    FD_GLYPHSET._fields_ = [
        ('cjThis', UInt32),
        ('flAccel', UInt32),
        ('cGlyphsSupported', UInt32),
        ('cRuns', UInt32),
        ('awcrun', win32more.Devices.Display.WCRUN * 1),
    ]
    return FD_GLYPHSET
def _define_FD_KERNINGPAIR_head():
    class FD_KERNINGPAIR(Structure):
        pass
    return FD_KERNINGPAIR
def _define_FD_KERNINGPAIR():
    FD_KERNINGPAIR = win32more.Devices.Display.FD_KERNINGPAIR_head
    FD_KERNINGPAIR._fields_ = [
        ('wcFirst', Char),
        ('wcSecond', Char),
        ('fwdKern', Int16),
    ]
    return FD_KERNINGPAIR
def _define_FD_LIGATURE_head():
    class FD_LIGATURE(Structure):
        pass
    return FD_LIGATURE
def _define_FD_LIGATURE():
    FD_LIGATURE = win32more.Devices.Display.FD_LIGATURE_head
    FD_LIGATURE._fields_ = [
        ('culThis', UInt32),
        ('ulType', UInt32),
        ('cLigatures', UInt32),
        ('alig', win32more.Devices.Display.LIGATURE * 1),
    ]
    return FD_LIGATURE
def _define_FD_XFORM_head():
    class FD_XFORM(Structure):
        pass
    return FD_XFORM
def _define_FD_XFORM():
    FD_XFORM = win32more.Devices.Display.FD_XFORM_head
    FD_XFORM._fields_ = [
        ('eXX', Single),
        ('eXY', Single),
        ('eYX', Single),
        ('eYY', Single),
    ]
    return FD_XFORM
def _define_FLOAT_LONG_head():
    class FLOAT_LONG(Union):
        pass
    return FLOAT_LONG
def _define_FLOAT_LONG():
    FLOAT_LONG = win32more.Devices.Display.FLOAT_LONG_head
    FLOAT_LONG._fields_ = [
        ('e', Single),
        ('l', Int32),
    ]
    return FLOAT_LONG
def _define_FLOATOBJ_XFORM_head():
    class FLOATOBJ_XFORM(Structure):
        pass
    return FLOATOBJ_XFORM
def _define_FLOATOBJ_XFORM():
    FLOATOBJ_XFORM = win32more.Devices.Display.FLOATOBJ_XFORM_head
    FLOATOBJ_XFORM._fields_ = [
        ('eM11', Single),
        ('eM12', Single),
        ('eM21', Single),
        ('eM22', Single),
        ('eDx', Single),
        ('eDy', Single),
    ]
    return FLOATOBJ_XFORM
def _define_FONT_IMAGE_INFO_head():
    class FONT_IMAGE_INFO(Structure):
        pass
    return FONT_IMAGE_INFO
def _define_FONT_IMAGE_INFO():
    FONT_IMAGE_INFO = win32more.Devices.Display.FONT_IMAGE_INFO_head
    FONT_IMAGE_INFO._fields_ = [
        ('FontSize', win32more.System.Console.COORD),
        ('ImageBits', c_char_p_no),
    ]
    return FONT_IMAGE_INFO
def _define_FONTDIFF_head():
    class FONTDIFF(Structure):
        pass
    return FONTDIFF
def _define_FONTDIFF():
    FONTDIFF = win32more.Devices.Display.FONTDIFF_head
    FONTDIFF._fields_ = [
        ('jReserved1', Byte),
        ('jReserved2', Byte),
        ('jReserved3', Byte),
        ('bWeight', Byte),
        ('usWinWeight', UInt16),
        ('fsSelection', UInt16),
        ('fwdAveCharWidth', Int16),
        ('fwdMaxCharInc', Int16),
        ('ptlCaret', win32more.Foundation.POINTL),
    ]
    return FONTDIFF
def _define_FONTINFO_head():
    class FONTINFO(Structure):
        pass
    return FONTINFO
def _define_FONTINFO():
    FONTINFO = win32more.Devices.Display.FONTINFO_head
    FONTINFO._fields_ = [
        ('cjThis', UInt32),
        ('flCaps', UInt32),
        ('cGlyphsSupported', UInt32),
        ('cjMaxGlyph1', UInt32),
        ('cjMaxGlyph4', UInt32),
        ('cjMaxGlyph8', UInt32),
        ('cjMaxGlyph32', UInt32),
    ]
    return FONTINFO
def _define_FONTOBJ_head():
    class FONTOBJ(Structure):
        pass
    return FONTOBJ
def _define_FONTOBJ():
    FONTOBJ = win32more.Devices.Display.FONTOBJ_head
    FONTOBJ._fields_ = [
        ('iUniq', UInt32),
        ('iFace', UInt32),
        ('cxMax', UInt32),
        ('flFontType', UInt32),
        ('iTTUniq', UIntPtr),
        ('iFile', UIntPtr),
        ('sizLogResPpi', win32more.Foundation.SIZE),
        ('ulStyleSize', UInt32),
        ('pvConsumer', c_void_p),
        ('pvProducer', c_void_p),
    ]
    return FONTOBJ
def _define_FONTSIM_head():
    class FONTSIM(Structure):
        pass
    return FONTSIM
def _define_FONTSIM():
    FONTSIM = win32more.Devices.Display.FONTSIM_head
    FONTSIM._fields_ = [
        ('dpBold', Int32),
        ('dpItalic', Int32),
        ('dpBoldItalic', Int32),
    ]
    return FONTSIM
def _define_FREEOBJPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.DRIVEROBJ_head))
def _define_FSCNTL_SCREEN_INFO_head():
    class FSCNTL_SCREEN_INFO(Structure):
        pass
    return FSCNTL_SCREEN_INFO
def _define_FSCNTL_SCREEN_INFO():
    FSCNTL_SCREEN_INFO = win32more.Devices.Display.FSCNTL_SCREEN_INFO_head
    FSCNTL_SCREEN_INFO._fields_ = [
        ('Position', win32more.System.Console.COORD),
        ('ScreenSize', win32more.System.Console.COORD),
        ('nNumberOfChars', UInt32),
    ]
    return FSCNTL_SCREEN_INFO
def _define_FSVIDEO_COPY_FRAME_BUFFER_head():
    class FSVIDEO_COPY_FRAME_BUFFER(Structure):
        pass
    return FSVIDEO_COPY_FRAME_BUFFER
def _define_FSVIDEO_COPY_FRAME_BUFFER():
    FSVIDEO_COPY_FRAME_BUFFER = win32more.Devices.Display.FSVIDEO_COPY_FRAME_BUFFER_head
    FSVIDEO_COPY_FRAME_BUFFER._fields_ = [
        ('SrcScreen', win32more.Devices.Display.FSCNTL_SCREEN_INFO),
        ('DestScreen', win32more.Devices.Display.FSCNTL_SCREEN_INFO),
    ]
    return FSVIDEO_COPY_FRAME_BUFFER
def _define_FSVIDEO_CURSOR_POSITION_head():
    class FSVIDEO_CURSOR_POSITION(Structure):
        pass
    return FSVIDEO_CURSOR_POSITION
def _define_FSVIDEO_CURSOR_POSITION():
    FSVIDEO_CURSOR_POSITION = win32more.Devices.Display.FSVIDEO_CURSOR_POSITION_head
    FSVIDEO_CURSOR_POSITION._fields_ = [
        ('Coord', win32more.Devices.Display.VIDEO_CURSOR_POSITION),
        ('dwType', UInt32),
    ]
    return FSVIDEO_CURSOR_POSITION
def _define_FSVIDEO_MODE_INFORMATION_head():
    class FSVIDEO_MODE_INFORMATION(Structure):
        pass
    return FSVIDEO_MODE_INFORMATION
def _define_FSVIDEO_MODE_INFORMATION():
    FSVIDEO_MODE_INFORMATION = win32more.Devices.Display.FSVIDEO_MODE_INFORMATION_head
    FSVIDEO_MODE_INFORMATION._fields_ = [
        ('VideoMode', win32more.Devices.Display.VIDEO_MODE_INFORMATION),
        ('VideoMemory', win32more.Devices.Display.VIDEO_MEMORY_INFORMATION),
    ]
    return FSVIDEO_MODE_INFORMATION
def _define_FSVIDEO_REVERSE_MOUSE_POINTER_head():
    class FSVIDEO_REVERSE_MOUSE_POINTER(Structure):
        pass
    return FSVIDEO_REVERSE_MOUSE_POINTER
def _define_FSVIDEO_REVERSE_MOUSE_POINTER():
    FSVIDEO_REVERSE_MOUSE_POINTER = win32more.Devices.Display.FSVIDEO_REVERSE_MOUSE_POINTER_head
    FSVIDEO_REVERSE_MOUSE_POINTER._fields_ = [
        ('Screen', win32more.Devices.Display.FSCNTL_SCREEN_INFO),
        ('dwType', UInt32),
    ]
    return FSVIDEO_REVERSE_MOUSE_POINTER
def _define_FSVIDEO_SCREEN_INFORMATION_head():
    class FSVIDEO_SCREEN_INFORMATION(Structure):
        pass
    return FSVIDEO_SCREEN_INFORMATION
def _define_FSVIDEO_SCREEN_INFORMATION():
    FSVIDEO_SCREEN_INFORMATION = win32more.Devices.Display.FSVIDEO_SCREEN_INFORMATION_head
    FSVIDEO_SCREEN_INFORMATION._fields_ = [
        ('ScreenSize', win32more.System.Console.COORD),
        ('FontSize', win32more.System.Console.COORD),
    ]
    return FSVIDEO_SCREEN_INFORMATION
def _define_FSVIDEO_WRITE_TO_FRAME_BUFFER_head():
    class FSVIDEO_WRITE_TO_FRAME_BUFFER(Structure):
        pass
    return FSVIDEO_WRITE_TO_FRAME_BUFFER
def _define_FSVIDEO_WRITE_TO_FRAME_BUFFER():
    FSVIDEO_WRITE_TO_FRAME_BUFFER = win32more.Devices.Display.FSVIDEO_WRITE_TO_FRAME_BUFFER_head
    FSVIDEO_WRITE_TO_FRAME_BUFFER._fields_ = [
        ('SrcBuffer', POINTER(win32more.Devices.Display.CHAR_IMAGE_INFO_head)),
        ('DestScreen', win32more.Devices.Display.FSCNTL_SCREEN_INFO),
    ]
    return FSVIDEO_WRITE_TO_FRAME_BUFFER
def _define_GAMMA_RAMP_DXGI_1_head():
    class GAMMA_RAMP_DXGI_1(Structure):
        pass
    return GAMMA_RAMP_DXGI_1
def _define_GAMMA_RAMP_DXGI_1():
    GAMMA_RAMP_DXGI_1 = win32more.Devices.Display.GAMMA_RAMP_DXGI_1_head
    GAMMA_RAMP_DXGI_1._fields_ = [
        ('Scale', win32more.Devices.Display.GAMMA_RAMP_RGB),
        ('Offset', win32more.Devices.Display.GAMMA_RAMP_RGB),
        ('GammaCurve', win32more.Devices.Display.GAMMA_RAMP_RGB * 1025),
    ]
    return GAMMA_RAMP_DXGI_1
def _define_GAMMA_RAMP_RGB_head():
    class GAMMA_RAMP_RGB(Structure):
        pass
    return GAMMA_RAMP_RGB
def _define_GAMMA_RAMP_RGB():
    GAMMA_RAMP_RGB = win32more.Devices.Display.GAMMA_RAMP_RGB_head
    GAMMA_RAMP_RGB._fields_ = [
        ('Red', Single),
        ('Green', Single),
        ('Blue', Single),
    ]
    return GAMMA_RAMP_RGB
def _define_GAMMA_RAMP_RGB256x3x16_head():
    class GAMMA_RAMP_RGB256x3x16(Structure):
        pass
    return GAMMA_RAMP_RGB256x3x16
def _define_GAMMA_RAMP_RGB256x3x16():
    GAMMA_RAMP_RGB256x3x16 = win32more.Devices.Display.GAMMA_RAMP_RGB256x3x16_head
    GAMMA_RAMP_RGB256x3x16._fields_ = [
        ('Red', UInt16 * 256),
        ('Green', UInt16 * 256),
        ('Blue', UInt16 * 256),
    ]
    return GAMMA_RAMP_RGB256x3x16
def _define_GAMMARAMP_head():
    class GAMMARAMP(Structure):
        pass
    return GAMMARAMP
def _define_GAMMARAMP():
    GAMMARAMP = win32more.Devices.Display.GAMMARAMP_head
    GAMMARAMP._fields_ = [
        ('Red', UInt16 * 256),
        ('Green', UInt16 * 256),
        ('Blue', UInt16 * 256),
    ]
    return GAMMARAMP
def _define_GDIINFO_head():
    class GDIINFO(Structure):
        pass
    return GDIINFO
def _define_GDIINFO():
    GDIINFO = win32more.Devices.Display.GDIINFO_head
    GDIINFO._fields_ = [
        ('ulVersion', UInt32),
        ('ulTechnology', UInt32),
        ('ulHorzSize', UInt32),
        ('ulVertSize', UInt32),
        ('ulHorzRes', UInt32),
        ('ulVertRes', UInt32),
        ('cBitsPixel', UInt32),
        ('cPlanes', UInt32),
        ('ulNumColors', UInt32),
        ('flRaster', UInt32),
        ('ulLogPixelsX', UInt32),
        ('ulLogPixelsY', UInt32),
        ('flTextCaps', UInt32),
        ('ulDACRed', UInt32),
        ('ulDACGreen', UInt32),
        ('ulDACBlue', UInt32),
        ('ulAspectX', UInt32),
        ('ulAspectY', UInt32),
        ('ulAspectXY', UInt32),
        ('xStyleStep', Int32),
        ('yStyleStep', Int32),
        ('denStyleStep', Int32),
        ('ptlPhysOffset', win32more.Foundation.POINTL),
        ('szlPhysSize', win32more.Foundation.SIZE),
        ('ulNumPalReg', UInt32),
        ('ciDevice', win32more.Devices.Display.COLORINFO),
        ('ulDevicePelsDPI', UInt32),
        ('ulPrimaryOrder', UInt32),
        ('ulHTPatternSize', UInt32),
        ('ulHTOutputFormat', UInt32),
        ('flHTFlags', UInt32),
        ('ulVRefresh', UInt32),
        ('ulBltAlignment', UInt32),
        ('ulPanningHorzRes', UInt32),
        ('ulPanningVertRes', UInt32),
        ('xPanningAlignment', UInt32),
        ('yPanningAlignment', UInt32),
        ('cxHTPat', UInt32),
        ('cyHTPat', UInt32),
        ('pHTPatA', c_char_p_no),
        ('pHTPatB', c_char_p_no),
        ('pHTPatC', c_char_p_no),
        ('flShadeBlend', UInt32),
        ('ulPhysicalPixelCharacteristics', UInt32),
        ('ulPhysicalPixelGamma', UInt32),
    ]
    return GDIINFO
def _define_GLYPHBITS_head():
    class GLYPHBITS(Structure):
        pass
    return GLYPHBITS
def _define_GLYPHBITS():
    GLYPHBITS = win32more.Devices.Display.GLYPHBITS_head
    GLYPHBITS._fields_ = [
        ('ptlOrigin', win32more.Foundation.POINTL),
        ('sizlBitmap', win32more.Foundation.SIZE),
        ('aj', Byte * 1),
    ]
    return GLYPHBITS
def _define_GLYPHDATA_head():
    class GLYPHDATA(Structure):
        pass
    return GLYPHDATA
def _define_GLYPHDATA():
    GLYPHDATA = win32more.Devices.Display.GLYPHDATA_head
    GLYPHDATA._fields_ = [
        ('gdf', win32more.Devices.Display.GLYPHDEF),
        ('hg', UInt32),
        ('fxD', Int32),
        ('fxA', Int32),
        ('fxAB', Int32),
        ('fxInkTop', Int32),
        ('fxInkBottom', Int32),
        ('rclInk', win32more.Foundation.RECTL),
        ('ptqD', win32more.Devices.Display.POINTQF),
    ]
    return GLYPHDATA
def _define_GLYPHDEF_head():
    class GLYPHDEF(Union):
        pass
    return GLYPHDEF
def _define_GLYPHDEF():
    GLYPHDEF = win32more.Devices.Display.GLYPHDEF_head
    GLYPHDEF._fields_ = [
        ('pgb', POINTER(win32more.Devices.Display.GLYPHBITS_head)),
        ('ppo', POINTER(win32more.Devices.Display.PATHOBJ_head)),
    ]
    return GLYPHDEF
def _define_GLYPHPOS_head():
    class GLYPHPOS(Structure):
        pass
    return GLYPHPOS
def _define_GLYPHPOS():
    GLYPHPOS = win32more.Devices.Display.GLYPHPOS_head
    GLYPHPOS._fields_ = [
        ('hg', UInt32),
        ('pgdf', POINTER(win32more.Devices.Display.GLYPHDEF_head)),
        ('ptl', win32more.Foundation.POINTL),
    ]
    return GLYPHPOS
HBM = IntPtr
HDEV = IntPtr
HDRVOBJ = IntPtr
HFASTMUTEX = IntPtr
HSEMAPHORE = IntPtr
HSURF = IntPtr
def _define_ICloneViewHelper_head():
    class ICloneViewHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('f6a3d4c4-5632-4d83-b0-a1-fb-88-71-2b-1e-b7')
    return ICloneViewHelper
def _define_ICloneViewHelper():
    ICloneViewHelper = win32more.Devices.Display.ICloneViewHelper_head
    ICloneViewHelper.GetConnectedIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),UInt32)(3, 'GetConnectedIDs', ((1, 'wszAdaptorName'),(1, 'pulCount'),(1, 'pulID'),(1, 'ulFlags'),)))
    ICloneViewHelper.GetActiveTopology = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(UInt32))(4, 'GetActiveTopology', ((1, 'wszAdaptorName'),(1, 'ulSourceID'),(1, 'pulCount'),(1, 'pulTargetID'),)))
    ICloneViewHelper.SetActiveTopology = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt32))(5, 'SetActiveTopology', ((1, 'wszAdaptorName'),(1, 'ulSourceID'),(1, 'ulCount'),(1, 'pulTargetID'),)))
    ICloneViewHelper.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(6, 'Commit', ((1, 'fFinalCall'),)))
    win32more.System.Com.IUnknown
    return ICloneViewHelper
def _define_IFIEXTRA_head():
    class IFIEXTRA(Structure):
        pass
    return IFIEXTRA
def _define_IFIEXTRA():
    IFIEXTRA = win32more.Devices.Display.IFIEXTRA_head
    IFIEXTRA._fields_ = [
        ('ulIdentifier', UInt32),
        ('dpFontSig', Int32),
        ('cig', UInt32),
        ('dpDesignVector', Int32),
        ('dpAxesInfoW', Int32),
        ('aulReserved', UInt32 * 1),
    ]
    return IFIEXTRA
def _define_IFIMETRICS_head():
    class IFIMETRICS(Structure):
        pass
    return IFIMETRICS
def _define_IFIMETRICS():
    IFIMETRICS = win32more.Devices.Display.IFIMETRICS_head
    IFIMETRICS._fields_ = [
        ('cjThis', UInt32),
        ('cjIfiExtra', UInt32),
        ('dpwszFamilyName', Int32),
        ('dpwszStyleName', Int32),
        ('dpwszFaceName', Int32),
        ('dpwszUniqueName', Int32),
        ('dpFontSim', Int32),
        ('lEmbedId', Int32),
        ('lItalicAngle', Int32),
        ('lCharBias', Int32),
        ('dpCharSets', Int32),
        ('jWinCharSet', Byte),
        ('jWinPitchAndFamily', Byte),
        ('usWinWeight', UInt16),
        ('flInfo', UInt32),
        ('fsSelection', UInt16),
        ('fsType', UInt16),
        ('fwdUnitsPerEm', Int16),
        ('fwdLowestPPEm', Int16),
        ('fwdWinAscender', Int16),
        ('fwdWinDescender', Int16),
        ('fwdMacAscender', Int16),
        ('fwdMacDescender', Int16),
        ('fwdMacLineGap', Int16),
        ('fwdTypoAscender', Int16),
        ('fwdTypoDescender', Int16),
        ('fwdTypoLineGap', Int16),
        ('fwdAveCharWidth', Int16),
        ('fwdMaxCharInc', Int16),
        ('fwdCapHeight', Int16),
        ('fwdXHeight', Int16),
        ('fwdSubscriptXSize', Int16),
        ('fwdSubscriptYSize', Int16),
        ('fwdSubscriptXOffset', Int16),
        ('fwdSubscriptYOffset', Int16),
        ('fwdSuperscriptXSize', Int16),
        ('fwdSuperscriptYSize', Int16),
        ('fwdSuperscriptXOffset', Int16),
        ('fwdSuperscriptYOffset', Int16),
        ('fwdUnderscoreSize', Int16),
        ('fwdUnderscorePosition', Int16),
        ('fwdStrikeoutSize', Int16),
        ('fwdStrikeoutPosition', Int16),
        ('chFirstChar', Byte),
        ('chLastChar', Byte),
        ('chDefaultChar', Byte),
        ('chBreakChar', Byte),
        ('wcFirstChar', Char),
        ('wcLastChar', Char),
        ('wcDefaultChar', Char),
        ('wcBreakChar', Char),
        ('ptlBaseline', win32more.Foundation.POINTL),
        ('ptlAspect', win32more.Foundation.POINTL),
        ('ptlCaret', win32more.Foundation.POINTL),
        ('rclFontBox', win32more.Foundation.RECTL),
        ('achVendId', Byte * 4),
        ('cKerningPairs', UInt32),
        ('ulPanoseCulture', UInt32),
        ('panose', win32more.Graphics.Gdi.PANOSE),
        ('Align', c_void_p),
    ]
    return IFIMETRICS
def _define_INDIRECT_DISPLAY_INFO_head():
    class INDIRECT_DISPLAY_INFO(Structure):
        pass
    return INDIRECT_DISPLAY_INFO
def _define_INDIRECT_DISPLAY_INFO():
    INDIRECT_DISPLAY_INFO = win32more.Devices.Display.INDIRECT_DISPLAY_INFO_head
    INDIRECT_DISPLAY_INFO._fields_ = [
        ('DisplayAdapterLuid', win32more.Foundation.LUID),
        ('Flags', UInt32),
        ('NumMonitors', UInt32),
        ('DisplayAdapterTargetBase', UInt32),
    ]
    return INDIRECT_DISPLAY_INFO
def _define_IViewHelper_head():
    class IViewHelper(win32more.System.Com.IUnknown_head):
        Guid = Guid('e85ccef5-aaaa-47f0-b5-e3-61-f7-ae-cd-c4-c1')
    return IViewHelper
def _define_IViewHelper():
    IViewHelper = win32more.Devices.Display.IViewHelper_head
    IViewHelper.GetConnectedIDs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),UInt32)(3, 'GetConnectedIDs', ((1, 'wszAdaptorName'),(1, 'pulCount'),(1, 'pulID'),(1, 'ulFlags'),)))
    IViewHelper.GetActiveTopology = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(UInt32))(4, 'GetActiveTopology', ((1, 'wszAdaptorName'),(1, 'ulSourceID'),(1, 'pulCount'),(1, 'pulTargetID'),)))
    IViewHelper.SetActiveTopology = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(UInt32))(5, 'SetActiveTopology', ((1, 'wszAdaptorName'),(1, 'ulSourceID'),(1, 'ulCount'),(1, 'pulTargetID'),)))
    IViewHelper.Commit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Commit', ()))
    IViewHelper.SetConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(UInt32))(7, 'SetConfiguration', ((1, 'pIStream'),(1, 'pulStatus'),)))
    IViewHelper.GetProceedOnNewConfiguration = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'GetProceedOnNewConfiguration', ()))
    win32more.System.Com.IUnknown
    return IViewHelper
def _define_LIGATURE_head():
    class LIGATURE(Structure):
        pass
    return LIGATURE
def _define_LIGATURE():
    LIGATURE = win32more.Devices.Display.LIGATURE_head
    LIGATURE._fields_ = [
        ('culSize', UInt32),
        ('pwsz', win32more.Foundation.PWSTR),
        ('chglyph', UInt32),
        ('ahglyph', UInt32 * 1),
    ]
    return LIGATURE
def _define_LINEATTRS_head():
    class LINEATTRS(Structure):
        pass
    return LINEATTRS
def _define_LINEATTRS():
    LINEATTRS = win32more.Devices.Display.LINEATTRS_head
    LINEATTRS._fields_ = [
        ('fl', UInt32),
        ('iJoin', UInt32),
        ('iEndCap', UInt32),
        ('elWidth', win32more.Devices.Display.FLOAT_LONG),
        ('eMiterLimit', Single),
        ('cstyle', UInt32),
        ('pstyle', POINTER(win32more.Devices.Display.FLOAT_LONG_head)),
        ('elStyleState', win32more.Devices.Display.FLOAT_LONG),
    ]
    return LINEATTRS
MC_COLOR_TEMPERATURE = Int32
MC_COLOR_TEMPERATURE_UNKNOWN = 0
MC_COLOR_TEMPERATURE_4000K = 1
MC_COLOR_TEMPERATURE_5000K = 2
MC_COLOR_TEMPERATURE_6500K = 3
MC_COLOR_TEMPERATURE_7500K = 4
MC_COLOR_TEMPERATURE_8200K = 5
MC_COLOR_TEMPERATURE_9300K = 6
MC_COLOR_TEMPERATURE_10000K = 7
MC_COLOR_TEMPERATURE_11500K = 8
MC_DISPLAY_TECHNOLOGY_TYPE = Int32
MC_SHADOW_MASK_CATHODE_RAY_TUBE = 0
MC_APERTURE_GRILL_CATHODE_RAY_TUBE = 1
MC_THIN_FILM_TRANSISTOR = 2
MC_LIQUID_CRYSTAL_ON_SILICON = 3
MC_PLASMA = 4
MC_ORGANIC_LIGHT_EMITTING_DIODE = 5
MC_ELECTROLUMINESCENT = 6
MC_MICROELECTROMECHANICAL = 7
MC_FIELD_EMISSION_DEVICE = 8
MC_DRIVE_TYPE = Int32
MC_RED_DRIVE = 0
MC_GREEN_DRIVE = 1
MC_BLUE_DRIVE = 2
MC_GAIN_TYPE = Int32
MC_RED_GAIN = 0
MC_GREEN_GAIN = 1
MC_BLUE_GAIN = 2
MC_POSITION_TYPE = Int32
MC_HORIZONTAL_POSITION = 0
MC_VERTICAL_POSITION = 1
MC_SIZE_TYPE = Int32
MC_WIDTH = 0
MC_HEIGHT = 1
def _define_MC_TIMING_REPORT_head():
    class MC_TIMING_REPORT(Structure):
        pass
    return MC_TIMING_REPORT
def _define_MC_TIMING_REPORT():
    MC_TIMING_REPORT = win32more.Devices.Display.MC_TIMING_REPORT_head
    MC_TIMING_REPORT._pack_ = 1
    MC_TIMING_REPORT._fields_ = [
        ('dwHorizontalFrequencyInHZ', UInt32),
        ('dwVerticalFrequencyInHZ', UInt32),
        ('bTimingStatusByte', Byte),
    ]
    return MC_TIMING_REPORT
MC_VCP_CODE_TYPE = Int32
MC_MOMENTARY = 0
MC_SET_PARAMETER = 1
def _define_MIPI_DSI_CAPS_head():
    class MIPI_DSI_CAPS(Structure):
        pass
    return MIPI_DSI_CAPS
def _define_MIPI_DSI_CAPS():
    MIPI_DSI_CAPS = win32more.Devices.Display.MIPI_DSI_CAPS_head
    MIPI_DSI_CAPS._fields_ = [
        ('DSITypeMajor', Byte),
        ('DSITypeMinor', Byte),
        ('SpecVersionMajor', Byte),
        ('SpecVersionMinor', Byte),
        ('SpecVersionPatch', Byte),
        ('TargetMaximumReturnPacketSize', UInt16),
        ('ResultCodeFlags', Byte),
        ('ResultCodeStatus', Byte),
        ('Revision', Byte),
        ('Level', Byte),
        ('DeviceClassHi', Byte),
        ('DeviceClassLo', Byte),
        ('ManufacturerHi', Byte),
        ('ManufacturerLo', Byte),
        ('ProductHi', Byte),
        ('ProductLo', Byte),
        ('LengthHi', Byte),
        ('LengthLo', Byte),
    ]
    return MIPI_DSI_CAPS
def _define_MIPI_DSI_PACKET_head():
    class MIPI_DSI_PACKET(Structure):
        pass
    return MIPI_DSI_PACKET
def _define_MIPI_DSI_PACKET():
    MIPI_DSI_PACKET = win32more.Devices.Display.MIPI_DSI_PACKET_head
    class MIPI_DSI_PACKET__Anonymous1_e__Union(Union):
        pass
    class MIPI_DSI_PACKET__Anonymous1_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIPI_DSI_PACKET__Anonymous1_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', Byte),
    ]
    MIPI_DSI_PACKET__Anonymous1_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIPI_DSI_PACKET__Anonymous1_e__Union._fields_ = [
        ('DataId', Byte),
        ('Anonymous', MIPI_DSI_PACKET__Anonymous1_e__Union__Anonymous_e__Struct),
    ]
    class MIPI_DSI_PACKET__Anonymous2_e__Union(Union):
        pass
    class MIPI_DSI_PACKET__Anonymous2_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIPI_DSI_PACKET__Anonymous2_e__Union__Anonymous_e__Struct._fields_ = [
        ('Data0', Byte),
        ('Data1', Byte),
    ]
    MIPI_DSI_PACKET__Anonymous2_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIPI_DSI_PACKET__Anonymous2_e__Union._fields_ = [
        ('Anonymous', MIPI_DSI_PACKET__Anonymous2_e__Union__Anonymous_e__Struct),
        ('LongWriteWordCount', UInt16),
    ]
    MIPI_DSI_PACKET._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    MIPI_DSI_PACKET._fields_ = [
        ('Anonymous1', MIPI_DSI_PACKET__Anonymous1_e__Union),
        ('Anonymous2', MIPI_DSI_PACKET__Anonymous2_e__Union),
        ('EccFiller', Byte),
        ('Payload', Byte * 8),
    ]
    return MIPI_DSI_PACKET
def _define_MIPI_DSI_RESET_head():
    class MIPI_DSI_RESET(Structure):
        pass
    return MIPI_DSI_RESET
def _define_MIPI_DSI_RESET():
    MIPI_DSI_RESET = win32more.Devices.Display.MIPI_DSI_RESET_head
    class MIPI_DSI_RESET__Anonymous_e__Union(Union):
        pass
    class MIPI_DSI_RESET__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    MIPI_DSI_RESET__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    MIPI_DSI_RESET__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    MIPI_DSI_RESET__Anonymous_e__Union._fields_ = [
        ('Anonymous', MIPI_DSI_RESET__Anonymous_e__Union__Anonymous_e__Struct),
        ('Results', UInt32),
    ]
    MIPI_DSI_RESET._anonymous_ = [
        'Anonymous',
    ]
    MIPI_DSI_RESET._fields_ = [
        ('Flags', UInt32),
        ('Anonymous', MIPI_DSI_RESET__Anonymous_e__Union),
    ]
    return MIPI_DSI_RESET
def _define_MIPI_DSI_TRANSMISSION_head():
    class MIPI_DSI_TRANSMISSION(Structure):
        pass
    return MIPI_DSI_TRANSMISSION
def _define_MIPI_DSI_TRANSMISSION():
    MIPI_DSI_TRANSMISSION = win32more.Devices.Display.MIPI_DSI_TRANSMISSION_head
    class MIPI_DSI_TRANSMISSION__Anonymous_e__Struct(Structure):
        pass
    MIPI_DSI_TRANSMISSION__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt16),
    ]
    MIPI_DSI_TRANSMISSION._anonymous_ = [
        'Anonymous',
    ]
    MIPI_DSI_TRANSMISSION._fields_ = [
        ('TotalBufferSize', UInt32),
        ('PacketCount', Byte),
        ('FailedPacket', Byte),
        ('Anonymous', MIPI_DSI_TRANSMISSION__Anonymous_e__Struct),
        ('ReadWordCount', UInt16),
        ('FinalCommandExtraPayload', UInt16),
        ('MipiErrors', UInt16),
        ('HostErrors', UInt16),
        ('Packets', win32more.Devices.Display.MIPI_DSI_PACKET * 1),
    ]
    return MIPI_DSI_TRANSMISSION
ORIENTATION_PREFERENCE = Int32
ORIENTATION_PREFERENCE_NONE = 0
ORIENTATION_PREFERENCE_LANDSCAPE = 1
ORIENTATION_PREFERENCE_PORTRAIT = 2
ORIENTATION_PREFERENCE_LANDSCAPE_FLIPPED = 4
ORIENTATION_PREFERENCE_PORTRAIT_FLIPPED = 8
OUTPUT_COLOR_ENCODING = Int32
OUTPUT_COLOR_ENCODING_RGB = 0
OUTPUT_COLOR_ENCODING_YCBCR444 = 1
OUTPUT_COLOR_ENCODING_YCBCR422 = 2
OUTPUT_COLOR_ENCODING_YCBCR420 = 3
OUTPUT_COLOR_ENCODING_INTENSITY = 4
OUTPUT_COLOR_ENCODING_FORCE_UINT32 = -1
OUTPUT_WIRE_COLOR_SPACE_TYPE = Int32
OUTPUT_WIRE_COLOR_SPACE_G22_P709 = 0
OUTPUT_WIRE_COLOR_SPACE_RESERVED = 4
OUTPUT_WIRE_COLOR_SPACE_G2084_P2020 = 12
OUTPUT_WIRE_COLOR_SPACE_G22_P709_WCG = 30
OUTPUT_WIRE_COLOR_SPACE_G22_P2020 = 31
OUTPUT_WIRE_COLOR_SPACE_G2084_P2020_HDR10PLUS = 32
OUTPUT_WIRE_COLOR_SPACE_G2084_P2020_DVLL = 33
def _define_OUTPUT_WIRE_FORMAT_head():
    class OUTPUT_WIRE_FORMAT(Structure):
        pass
    return OUTPUT_WIRE_FORMAT
def _define_OUTPUT_WIRE_FORMAT():
    OUTPUT_WIRE_FORMAT = win32more.Devices.Display.OUTPUT_WIRE_FORMAT_head
    OUTPUT_WIRE_FORMAT._fields_ = [
        ('ColorEncoding', win32more.Devices.Display.OUTPUT_COLOR_ENCODING),
        ('BitsPerPixel', UInt32),
    ]
    return OUTPUT_WIRE_FORMAT
def _define_PALOBJ_head():
    class PALOBJ(Structure):
        pass
    return PALOBJ
def _define_PALOBJ():
    PALOBJ = win32more.Devices.Display.PALOBJ_head
    PALOBJ._fields_ = [
        ('ulReserved', UInt32),
    ]
    return PALOBJ
def _define_PANEL_BRIGHTNESS_SENSOR_DATA_head():
    class PANEL_BRIGHTNESS_SENSOR_DATA(Structure):
        pass
    return PANEL_BRIGHTNESS_SENSOR_DATA
def _define_PANEL_BRIGHTNESS_SENSOR_DATA():
    PANEL_BRIGHTNESS_SENSOR_DATA = win32more.Devices.Display.PANEL_BRIGHTNESS_SENSOR_DATA_head
    class PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union(Union):
        pass
    class PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union._fields_ = [
        ('Anonymous', PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union__Anonymous_e__Struct),
        ('Value', UInt32),
    ]
    PANEL_BRIGHTNESS_SENSOR_DATA._anonymous_ = [
        'Anonymous',
    ]
    PANEL_BRIGHTNESS_SENSOR_DATA._fields_ = [
        ('Anonymous', PANEL_BRIGHTNESS_SENSOR_DATA__Anonymous_e__Union),
        ('AlsReading', Single),
        ('ChromaticityCoordinate', win32more.Devices.Display.CHROMATICITY_COORDINATE),
        ('ColorTemperature', Single),
    ]
    return PANEL_BRIGHTNESS_SENSOR_DATA
def _define_PANEL_GET_BACKLIGHT_REDUCTION_head():
    class PANEL_GET_BACKLIGHT_REDUCTION(Structure):
        pass
    return PANEL_GET_BACKLIGHT_REDUCTION
def _define_PANEL_GET_BACKLIGHT_REDUCTION():
    PANEL_GET_BACKLIGHT_REDUCTION = win32more.Devices.Display.PANEL_GET_BACKLIGHT_REDUCTION_head
    PANEL_GET_BACKLIGHT_REDUCTION._fields_ = [
        ('BacklightUsersetting', UInt16),
        ('BacklightEffective', UInt16),
        ('GammaRamp', win32more.Devices.Display.BACKLIGHT_REDUCTION_GAMMA_RAMP),
    ]
    return PANEL_GET_BACKLIGHT_REDUCTION
def _define_PANEL_GET_BRIGHTNESS_head():
    class PANEL_GET_BRIGHTNESS(Structure):
        pass
    return PANEL_GET_BRIGHTNESS
def _define_PANEL_GET_BRIGHTNESS():
    PANEL_GET_BRIGHTNESS = win32more.Devices.Display.PANEL_GET_BRIGHTNESS_head
    class PANEL_GET_BRIGHTNESS__Anonymous_e__Union(Union):
        pass
    class PANEL_GET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PANEL_GET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('CurrentInMillinits', UInt32),
        ('TargetInMillinits', UInt32),
    ]
    PANEL_GET_BRIGHTNESS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PANEL_GET_BRIGHTNESS__Anonymous_e__Union._fields_ = [
        ('Level', Byte),
        ('Anonymous', PANEL_GET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    PANEL_GET_BRIGHTNESS._anonymous_ = [
        'Anonymous',
    ]
    PANEL_GET_BRIGHTNESS._fields_ = [
        ('Version', win32more.Devices.Display.BRIGHTNESS_INTERFACE_VERSION),
        ('Anonymous', PANEL_GET_BRIGHTNESS__Anonymous_e__Union),
    ]
    return PANEL_GET_BRIGHTNESS
def _define_PANEL_QUERY_BRIGHTNESS_CAPS_head():
    class PANEL_QUERY_BRIGHTNESS_CAPS(Structure):
        pass
    return PANEL_QUERY_BRIGHTNESS_CAPS
def _define_PANEL_QUERY_BRIGHTNESS_CAPS():
    PANEL_QUERY_BRIGHTNESS_CAPS = win32more.Devices.Display.PANEL_QUERY_BRIGHTNESS_CAPS_head
    class PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union(Union):
        pass
    class PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union._fields_ = [
        ('Anonymous', PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union__Anonymous_e__Struct),
        ('Value', UInt32),
    ]
    PANEL_QUERY_BRIGHTNESS_CAPS._anonymous_ = [
        'Anonymous',
    ]
    PANEL_QUERY_BRIGHTNESS_CAPS._fields_ = [
        ('Version', win32more.Devices.Display.BRIGHTNESS_INTERFACE_VERSION),
        ('Anonymous', PANEL_QUERY_BRIGHTNESS_CAPS__Anonymous_e__Union),
    ]
    return PANEL_QUERY_BRIGHTNESS_CAPS
def _define_PANEL_QUERY_BRIGHTNESS_RANGES_head():
    class PANEL_QUERY_BRIGHTNESS_RANGES(Structure):
        pass
    return PANEL_QUERY_BRIGHTNESS_RANGES
def _define_PANEL_QUERY_BRIGHTNESS_RANGES():
    PANEL_QUERY_BRIGHTNESS_RANGES = win32more.Devices.Display.PANEL_QUERY_BRIGHTNESS_RANGES_head
    class PANEL_QUERY_BRIGHTNESS_RANGES__Anonymous_e__Union(Union):
        pass
    PANEL_QUERY_BRIGHTNESS_RANGES__Anonymous_e__Union._fields_ = [
        ('BrightnessLevel', win32more.Devices.Display.BRIGHTNESS_LEVEL),
        ('NitRanges', win32more.Devices.Display.BRIGHTNESS_NIT_RANGES),
    ]
    PANEL_QUERY_BRIGHTNESS_RANGES._anonymous_ = [
        'Anonymous',
    ]
    PANEL_QUERY_BRIGHTNESS_RANGES._fields_ = [
        ('Version', win32more.Devices.Display.BRIGHTNESS_INTERFACE_VERSION),
        ('Anonymous', PANEL_QUERY_BRIGHTNESS_RANGES__Anonymous_e__Union),
    ]
    return PANEL_QUERY_BRIGHTNESS_RANGES
def _define_PANEL_SET_BACKLIGHT_OPTIMIZATION_head():
    class PANEL_SET_BACKLIGHT_OPTIMIZATION(Structure):
        pass
    return PANEL_SET_BACKLIGHT_OPTIMIZATION
def _define_PANEL_SET_BACKLIGHT_OPTIMIZATION():
    PANEL_SET_BACKLIGHT_OPTIMIZATION = win32more.Devices.Display.PANEL_SET_BACKLIGHT_OPTIMIZATION_head
    PANEL_SET_BACKLIGHT_OPTIMIZATION._fields_ = [
        ('Level', win32more.Devices.Display.BACKLIGHT_OPTIMIZATION_LEVEL),
    ]
    return PANEL_SET_BACKLIGHT_OPTIMIZATION
def _define_PANEL_SET_BRIGHTNESS_head():
    class PANEL_SET_BRIGHTNESS(Structure):
        pass
    return PANEL_SET_BRIGHTNESS
def _define_PANEL_SET_BRIGHTNESS():
    PANEL_SET_BRIGHTNESS = win32more.Devices.Display.PANEL_SET_BRIGHTNESS_head
    class PANEL_SET_BRIGHTNESS__Anonymous_e__Union(Union):
        pass
    class PANEL_SET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PANEL_SET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('Millinits', UInt32),
        ('TransitionTimeInMs', UInt32),
        ('SensorData', win32more.Devices.Display.PANEL_BRIGHTNESS_SENSOR_DATA),
    ]
    PANEL_SET_BRIGHTNESS__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PANEL_SET_BRIGHTNESS__Anonymous_e__Union._fields_ = [
        ('Level', Byte),
        ('Anonymous', PANEL_SET_BRIGHTNESS__Anonymous_e__Union__Anonymous_e__Struct),
    ]
    PANEL_SET_BRIGHTNESS._anonymous_ = [
        'Anonymous',
    ]
    PANEL_SET_BRIGHTNESS._fields_ = [
        ('Version', win32more.Devices.Display.BRIGHTNESS_INTERFACE_VERSION),
        ('Anonymous', PANEL_SET_BRIGHTNESS__Anonymous_e__Union),
    ]
    return PANEL_SET_BRIGHTNESS
def _define_PANEL_SET_BRIGHTNESS_STATE_head():
    class PANEL_SET_BRIGHTNESS_STATE(Structure):
        pass
    return PANEL_SET_BRIGHTNESS_STATE
def _define_PANEL_SET_BRIGHTNESS_STATE():
    PANEL_SET_BRIGHTNESS_STATE = win32more.Devices.Display.PANEL_SET_BRIGHTNESS_STATE_head
    class PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union(Union):
        pass
    class PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union__Anonymous_e__Struct(Structure):
        pass
    PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union__Anonymous_e__Struct._fields_ = [
        ('_bitfield', UInt32),
    ]
    PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union._anonymous_ = [
        'Anonymous',
    ]
    PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union._fields_ = [
        ('Anonymous', PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union__Anonymous_e__Struct),
        ('Value', UInt32),
    ]
    PANEL_SET_BRIGHTNESS_STATE._anonymous_ = [
        'Anonymous',
    ]
    PANEL_SET_BRIGHTNESS_STATE._fields_ = [
        ('Anonymous', PANEL_SET_BRIGHTNESS_STATE__Anonymous_e__Union),
    ]
    return PANEL_SET_BRIGHTNESS_STATE
def _define_PATHDATA_head():
    class PATHDATA(Structure):
        pass
    return PATHDATA
def _define_PATHDATA():
    PATHDATA = win32more.Devices.Display.PATHDATA_head
    PATHDATA._fields_ = [
        ('flags', UInt32),
        ('count', UInt32),
        ('pptfx', POINTER(win32more.Devices.Display.POINTFIX_head)),
    ]
    return PATHDATA
def _define_PATHOBJ_head():
    class PATHOBJ(Structure):
        pass
    return PATHOBJ
def _define_PATHOBJ():
    PATHOBJ = win32more.Devices.Display.PATHOBJ_head
    PATHOBJ._fields_ = [
        ('fl', UInt32),
        ('cCurves', UInt32),
    ]
    return PATHOBJ
def _define_PERBANDINFO_head():
    class PERBANDINFO(Structure):
        pass
    return PERBANDINFO
def _define_PERBANDINFO():
    PERBANDINFO = win32more.Devices.Display.PERBANDINFO_head
    PERBANDINFO._fields_ = [
        ('bRepeatThisBand', win32more.Foundation.BOOL),
        ('szlBand', win32more.Foundation.SIZE),
        ('ulHorzRes', UInt32),
        ('ulVertRes', UInt32),
    ]
    return PERBANDINFO
def _define_PFN():
    return WINFUNCTYPE(IntPtr,)
def _define_PFN_DrvAccumulateD3DDirtyRect():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CDDDXGK_REDIRBITMAPPRESENTINFO_head))
def _define_PFN_DrvAlphaBlend():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Devices.Display.BLENDOBJ_head))
def _define_PFN_DrvAssertMode():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Foundation.BOOL)
def _define_PFN_DrvAssociateSharedSurface():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.SIZE)
def _define_PFN_DrvBitBlt():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvCompletePDEV():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV,win32more.Devices.Display.HDEV)
def _define_PFN_DrvCopyBits():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head))
def _define_PFN_DrvCreateDeviceBitmap():
    return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Devices.Display.DHPDEV,win32more.Foundation.SIZE,UInt32)
def _define_PFN_DrvCreateDeviceBitmapEx():
    return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,win32more.Devices.Display.DHPDEV,win32more.Foundation.SIZE,UInt32,UInt32,win32more.Devices.Display.DHSURF,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE))
def _define_PFN_DrvDeleteDeviceBitmap():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHSURF)
def _define_PFN_DrvDeleteDeviceBitmapEx():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHSURF)
def _define_PFN_DrvDeriveSurface():
    return WINFUNCTYPE(win32more.Graphics.Gdi.HBITMAP,POINTER(win32more.Graphics.DirectDraw.DD_DIRECTDRAW_GLOBAL_head),POINTER(win32more.Graphics.DirectDraw.DD_SURFACE_LOCAL_head))
def _define_PFN_DrvDescribePixelFormat():
    return WINFUNCTYPE(Int32,win32more.Devices.Display.DHPDEV,Int32,UInt32,POINTER(win32more.Graphics.OpenGL.PIXELFORMATDESCRIPTOR_head))
def _define_PFN_DrvDestroyFont():
    return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.FONTOBJ_head))
def _define_PFN_DrvDisableDirectDraw():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV)
def _define_PFN_DrvDisableDriver():
    return WINFUNCTYPE(Void,)
def _define_PFN_DrvDisablePDEV():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV)
def _define_PFN_DrvDisableSurface():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV)
def _define_PFN_DrvDitherColor():
    return WINFUNCTYPE(UInt32,win32more.Devices.Display.DHPDEV,UInt32,UInt32,POINTER(UInt32))
def _define_PFN_DrvDrawEscape():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.SURFOBJ_head),UInt32,POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Foundation.RECTL_head),UInt32,c_void_p)
def _define_PFN_DrvEnableDirectDraw():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,POINTER(win32more.Graphics.DirectDraw.DD_CALLBACKS_head),POINTER(win32more.Graphics.DirectDraw.DD_SURFACECALLBACKS_head),POINTER(win32more.Graphics.DirectDraw.DD_PALETTECALLBACKS_head))
def _define_PFN_DrvEnableDriver():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,UInt32,POINTER(win32more.Devices.Display.DRVENABLEDATA_head))
def _define_PFN_DrvEnablePDEV():
    return WINFUNCTYPE(win32more.Devices.Display.DHPDEV,POINTER(win32more.Graphics.Gdi.DEVMODEW_head),win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Devices.Display.HSURF),UInt32,POINTER(win32more.Devices.Display.GDIINFO_head),UInt32,POINTER(win32more.Devices.Display.DEVINFO_head),win32more.Devices.Display.HDEV,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE)
def _define_PFN_DrvEnableSurface():
    return WINFUNCTYPE(win32more.Devices.Display.HSURF,win32more.Devices.Display.DHPDEV)
def _define_PFN_DrvEndDoc():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),UInt32)
def _define_PFN_DrvEndDxInterop():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),win32more.Foundation.BOOL,POINTER(win32more.Foundation.BOOL),c_void_p)
def _define_PFN_DrvEscape():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.SURFOBJ_head),UInt32,UInt32,c_void_p,UInt32,c_void_p)
def _define_PFN_DrvFillPath():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32,UInt32)
def _define_PFN_DrvFontManagement():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,UInt32,c_void_p,UInt32,c_void_p)
def _define_PFN_DrvFree():
    return WINFUNCTYPE(Void,c_void_p,UIntPtr)
def _define_PFN_DrvGetDirectDrawInfo():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,POINTER(win32more.Graphics.DirectDraw.DD_HALINFO_head),POINTER(UInt32),POINTER(win32more.Graphics.DirectDraw.VIDEOMEMORY_head),POINTER(UInt32),POINTER(UInt32))
def _define_PFN_DrvGetGlyphMode():
    return WINFUNCTYPE(UInt32,win32more.Devices.Display.DHPDEV,POINTER(win32more.Devices.Display.FONTOBJ_head))
def _define_PFN_DrvGetModes():
    return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))
def _define_PFN_DrvGetTrueTypeFile():
    return WINFUNCTYPE(c_void_p,UIntPtr,POINTER(UInt32))
def _define_PFN_DrvGradientFill():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.TRIVERTEX_head),UInt32,c_void_p,UInt32,POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvIcmCheckBitmapBits():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Foundation.HANDLE,POINTER(win32more.Devices.Display.SURFOBJ_head),c_char_p_no)
def _define_PFN_DrvIcmCreateColorTransform():
    return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Devices.Display.DHPDEV,POINTER(win32more.UI.ColorSystem.LOGCOLORSPACEW_head),c_void_p,UInt32,c_void_p,UInt32,c_void_p,UInt32,UInt32)
def _define_PFN_DrvIcmDeleteColorTransform():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Foundation.HANDLE)
def _define_PFN_DrvIcmSetDeviceGammaRamp():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,UInt32,c_void_p)
def _define_PFN_DrvLineTo():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.RECTL_head),UInt32)
def _define_PFN_DrvLoadFontFile():
    return WINFUNCTYPE(UIntPtr,UInt32,POINTER(UIntPtr),POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Graphics.Gdi.DESIGNVECTOR_head),UInt32,UInt32)
def _define_PFN_DrvLockDisplayArea():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV,POINTER(win32more.Foundation.RECTL_head))
def _define_PFN_DrvMovePointer():
    return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.SURFOBJ_head),Int32,Int32,POINTER(win32more.Foundation.RECTL_head))
def _define_PFN_DrvNextBand():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Foundation.POINTL_head))
def _define_PFN_DrvNotify():
    return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.SURFOBJ_head),UInt32,c_void_p)
def _define_PFN_DrvPaint():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvPlgBlt():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.POINTFIX_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvQueryAdvanceWidths():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,POINTER(UInt32),c_void_p,UInt32)
def _define_PFN_DrvQueryDeviceSupport():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Devices.Display.XFORMOBJ_head),UInt32,UInt32,c_void_p,UInt32,c_void_p)
def _define_PFN_DrvQueryFont():
    return WINFUNCTYPE(POINTER(win32more.Devices.Display.IFIMETRICS_head),win32more.Devices.Display.DHPDEV,UIntPtr,UInt32,POINTER(UIntPtr))
def _define_PFN_DrvQueryFontCaps():
    return WINFUNCTYPE(Int32,UInt32,POINTER(UInt32))
def _define_PFN_DrvQueryFontData():
    return WINFUNCTYPE(Int32,win32more.Devices.Display.DHPDEV,POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,UInt32,POINTER(win32more.Devices.Display.GLYPHDATA_head),c_void_p,UInt32)
def _define_PFN_DrvQueryFontFile():
    return WINFUNCTYPE(Int32,UIntPtr,UInt32,UInt32,POINTER(UInt32))
def _define_PFN_DrvQueryFontTree():
    return WINFUNCTYPE(c_void_p,win32more.Devices.Display.DHPDEV,UIntPtr,UInt32,UInt32,POINTER(UIntPtr))
def _define_PFN_DrvQueryGlyphAttrs():
    return WINFUNCTYPE(POINTER(win32more.Devices.Display.FD_GLYPHATTR_head),POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32)
def _define_PFN_DrvQueryPerBandInfo():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PERBANDINFO_head))
def _define_PFN_DrvQuerySpoolType():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Foundation.PWSTR)
def _define_PFN_DrvQueryTrueTypeOutline():
    return WINFUNCTYPE(Int32,win32more.Devices.Display.DHPDEV,POINTER(win32more.Devices.Display.FONTOBJ_head),UInt32,win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.GLYPHDATA_head),UInt32,POINTER(win32more.Graphics.Gdi.TTPOLYGONHEADER_head))
def _define_PFN_DrvQueryTrueTypeSection():
    return WINFUNCTYPE(Int32,UInt32,UInt32,UInt32,POINTER(win32more.Foundation.HANDLE),POINTER(Int32))
def _define_PFN_DrvQueryTrueTypeTable():
    return WINFUNCTYPE(Int32,UIntPtr,UInt32,UInt32,Int32,UInt32,c_char_p_no,POINTER(c_char_p_no),POINTER(UInt32))
def _define_PFN_DrvRealizeBrush():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),UInt32)
def _define_PFN_DrvRenderHint():
    return WINFUNCTYPE(Int32,win32more.Devices.Display.DHPDEV,UInt32,UIntPtr,c_void_p)
def _define_PFN_DrvResetDevice():
    return WINFUNCTYPE(UInt32,win32more.Devices.Display.DHPDEV,c_void_p)
def _define_PFN_DrvResetPDEV():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Devices.Display.DHPDEV)
def _define_PFN_DrvSaveScreenBits():
    return WINFUNCTYPE(UIntPtr,POINTER(win32more.Devices.Display.SURFOBJ_head),UInt32,UIntPtr,POINTER(win32more.Foundation.RECTL_head))
def _define_PFN_DrvSendPage():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head))
def _define_PFN_DrvSetPalette():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,POINTER(win32more.Devices.Display.PALOBJ_head),UInt32,UInt32,UInt32)
def _define_PFN_DrvSetPixelFormat():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),Int32,win32more.Foundation.HWND)
def _define_PFN_DrvSetPointerShape():
    return WINFUNCTYPE(UInt32,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),Int32,Int32,Int32,Int32,POINTER(win32more.Foundation.RECTL_head),UInt32)
def _define_PFN_DrvStartBanding():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Foundation.POINTL_head))
def _define_PFN_DrvStartDoc():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),win32more.Foundation.PWSTR,UInt32)
def _define_PFN_DrvStartDxInterop():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),win32more.Foundation.BOOL,c_void_p)
def _define_PFN_DrvStartPage():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head))
def _define_PFN_DrvStretchBlt():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvStretchBltROP():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Graphics.Gdi.COLORADJUSTMENT_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.POINTL_head),UInt32,POINTER(win32more.Devices.Display.BRUSHOBJ_head),UInt32)
def _define_PFN_DrvStrokeAndFillPath():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Devices.Display.LINEATTRS_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32,UInt32)
def _define_PFN_DrvStrokePath():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.PATHOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XFORMOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),POINTER(win32more.Devices.Display.LINEATTRS_head),UInt32)
def _define_PFN_DrvSurfaceComplete():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Devices.Display.DHPDEV,win32more.Foundation.HANDLE)
def _define_PFN_DrvSwapBuffers():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.WNDOBJ_head))
def _define_PFN_DrvSynchronize():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV,POINTER(win32more.Foundation.RECTL_head))
def _define_PFN_DrvSynchronizeRedirectionBitmaps():
    return WINFUNCTYPE(win32more.Foundation.NTSTATUS,win32more.Devices.Display.DHPDEV,POINTER(UInt64))
def _define_PFN_DrvSynchronizeSurface():
    return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Foundation.RECTL_head),UInt32)
def _define_PFN_DrvTextOut():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.STROBJ_head),POINTER(win32more.Devices.Display.FONTOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Devices.Display.BRUSHOBJ_head),POINTER(win32more.Foundation.POINTL_head),UInt32)
def _define_PFN_DrvTransparentBlt():
    return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.SURFOBJ_head),POINTER(win32more.Devices.Display.CLIPOBJ_head),POINTER(win32more.Devices.Display.XLATEOBJ_head),POINTER(win32more.Foundation.RECTL_head),POINTER(win32more.Foundation.RECTL_head),UInt32,UInt32)
def _define_PFN_DrvUnloadFontFile():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UIntPtr)
def _define_PFN_DrvUnlockDisplayArea():
    return WINFUNCTYPE(Void,win32more.Devices.Display.DHPDEV,POINTER(win32more.Foundation.RECTL_head))
def _define_PFN_EngCombineRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,Int32)
def _define_PFN_EngCopyRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)
def _define_PFN_EngCreateRectRgn():
    return WINFUNCTYPE(win32more.Foundation.HANDLE,Int32,Int32,Int32,Int32)
def _define_PFN_EngDeleteRgn():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE)
def _define_PFN_EngIntersectRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)
def _define_PFN_EngSubtractRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)
def _define_PFN_EngUnionRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)
def _define_PFN_EngXorRgn():
    return WINFUNCTYPE(Int32,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE)
def _define_PHYSICAL_MONITOR_head():
    class PHYSICAL_MONITOR(Structure):
        pass
    return PHYSICAL_MONITOR
def _define_PHYSICAL_MONITOR():
    PHYSICAL_MONITOR = win32more.Devices.Display.PHYSICAL_MONITOR_head
    PHYSICAL_MONITOR._pack_ = 1
    PHYSICAL_MONITOR._fields_ = [
        ('hPhysicalMonitor', win32more.Foundation.HANDLE),
        ('szPhysicalMonitorDescription', Char * 128),
    ]
    return PHYSICAL_MONITOR
def _define_POINTE_head():
    class POINTE(Structure):
        pass
    return POINTE
def _define_POINTE():
    POINTE = win32more.Devices.Display.POINTE_head
    POINTE._fields_ = [
        ('x', Single),
        ('y', Single),
    ]
    return POINTE
def _define_POINTFIX_head():
    class POINTFIX(Structure):
        pass
    return POINTFIX
def _define_POINTFIX():
    POINTFIX = win32more.Devices.Display.POINTFIX_head
    POINTFIX._fields_ = [
        ('x', Int32),
        ('y', Int32),
    ]
    return POINTFIX
def _define_POINTQF_head():
    class POINTQF(Structure):
        pass
    return POINTQF
def _define_POINTQF():
    POINTQF = win32more.Devices.Display.POINTQF_head
    POINTQF._fields_ = [
        ('x', win32more.Foundation.LARGE_INTEGER),
        ('y', win32more.Foundation.LARGE_INTEGER),
    ]
    return POINTQF
def _define_PVIDEO_WIN32K_CALLOUT():
    return WINFUNCTYPE(Void,c_void_p)
def _define_RECTFX_head():
    class RECTFX(Structure):
        pass
    return RECTFX
def _define_RECTFX():
    RECTFX = win32more.Devices.Display.RECTFX_head
    RECTFX._fields_ = [
        ('xLeft', Int32),
        ('yTop', Int32),
        ('xRight', Int32),
        ('yBottom', Int32),
    ]
    return RECTFX
def _define_RUN_head():
    class RUN(Structure):
        pass
    return RUN
def _define_RUN():
    RUN = win32more.Devices.Display.RUN_head
    RUN._fields_ = [
        ('iStart', Int32),
        ('iStop', Int32),
    ]
    return RUN
def _define_SET_ACTIVE_COLOR_PROFILE_NAME_head():
    class SET_ACTIVE_COLOR_PROFILE_NAME(Structure):
        pass
    return SET_ACTIVE_COLOR_PROFILE_NAME
def _define_SET_ACTIVE_COLOR_PROFILE_NAME():
    SET_ACTIVE_COLOR_PROFILE_NAME = win32more.Devices.Display.SET_ACTIVE_COLOR_PROFILE_NAME_head
    SET_ACTIVE_COLOR_PROFILE_NAME._fields_ = [
        ('ColorProfileName', Char * 1),
    ]
    return SET_ACTIVE_COLOR_PROFILE_NAME
def _define_SORTCOMP():
    return CFUNCTYPE(Int32,c_void_p,c_void_p)
def _define_Sources_head():
    class Sources(Structure):
        pass
    return Sources
def _define_Sources():
    Sources = win32more.Devices.Display.Sources_head
    Sources._fields_ = [
        ('sourceId', UInt32),
        ('numTargets', Int32),
        ('aTargets', UInt32 * 1),
    ]
    return Sources
def _define_STROBJ_head():
    class STROBJ(Structure):
        pass
    return STROBJ
def _define_STROBJ():
    STROBJ = win32more.Devices.Display.STROBJ_head
    STROBJ._fields_ = [
        ('cGlyphs', UInt32),
        ('flAccel', UInt32),
        ('ulCharInc', UInt32),
        ('rclBkGround', win32more.Foundation.RECTL),
        ('pgp', POINTER(win32more.Devices.Display.GLYPHPOS_head)),
        ('pwszOrg', win32more.Foundation.PWSTR),
    ]
    return STROBJ
def _define_SURFOBJ_head():
    class SURFOBJ(Structure):
        pass
    return SURFOBJ
def _define_SURFOBJ():
    SURFOBJ = win32more.Devices.Display.SURFOBJ_head
    SURFOBJ._fields_ = [
        ('dhsurf', win32more.Devices.Display.DHSURF),
        ('hsurf', win32more.Devices.Display.HSURF),
        ('dhpdev', win32more.Devices.Display.DHPDEV),
        ('hdev', win32more.Devices.Display.HDEV),
        ('sizlBitmap', win32more.Foundation.SIZE),
        ('cjBits', UInt32),
        ('pvBits', c_void_p),
        ('pvScan0', c_void_p),
        ('lDelta', Int32),
        ('iUniq', UInt32),
        ('iBitmapFormat', UInt32),
        ('iType', UInt16),
        ('fjBitmap', UInt16),
    ]
    return SURFOBJ
def _define_TYPE1_FONT_head():
    class TYPE1_FONT(Structure):
        pass
    return TYPE1_FONT
def _define_TYPE1_FONT():
    TYPE1_FONT = win32more.Devices.Display.TYPE1_FONT_head
    TYPE1_FONT._fields_ = [
        ('hPFM', win32more.Foundation.HANDLE),
        ('hPFB', win32more.Foundation.HANDLE),
        ('ulIdentifier', UInt32),
    ]
    return TYPE1_FONT
def _define_VGA_CHAR_head():
    class VGA_CHAR(Structure):
        pass
    return VGA_CHAR
def _define_VGA_CHAR():
    VGA_CHAR = win32more.Devices.Display.VGA_CHAR_head
    VGA_CHAR._fields_ = [
        ('Char', win32more.Foundation.CHAR),
        ('Attributes', win32more.Foundation.CHAR),
    ]
    return VGA_CHAR
def _define_VIDEO_BANK_SELECT_head():
    class VIDEO_BANK_SELECT(Structure):
        pass
    return VIDEO_BANK_SELECT
def _define_VIDEO_BANK_SELECT():
    VIDEO_BANK_SELECT = win32more.Devices.Display.VIDEO_BANK_SELECT_head
    VIDEO_BANK_SELECT._fields_ = [
        ('Length', UInt32),
        ('Size', UInt32),
        ('BankingFlags', UInt32),
        ('BankingType', UInt32),
        ('PlanarHCBankingType', UInt32),
        ('BitmapWidthInBytes', UInt32),
        ('BitmapSize', UInt32),
        ('Granularity', UInt32),
        ('PlanarHCGranularity', UInt32),
        ('CodeOffset', UInt32),
        ('PlanarHCBankCodeOffset', UInt32),
        ('PlanarHCEnableCodeOffset', UInt32),
        ('PlanarHCDisableCodeOffset', UInt32),
    ]
    return VIDEO_BANK_SELECT
VIDEO_BANK_TYPE = Int32
VIDEO_BANK_TYPE_VideoNotBanked = 0
VIDEO_BANK_TYPE_VideoBanked1RW = 1
VIDEO_BANK_TYPE_VideoBanked1R1W = 2
VIDEO_BANK_TYPE_VideoBanked2RW = 3
VIDEO_BANK_TYPE_NumVideoBankTypes = 4
def _define_VIDEO_BRIGHTNESS_POLICY_head():
    class VIDEO_BRIGHTNESS_POLICY(Structure):
        pass
    return VIDEO_BRIGHTNESS_POLICY
def _define_VIDEO_BRIGHTNESS_POLICY():
    VIDEO_BRIGHTNESS_POLICY = win32more.Devices.Display.VIDEO_BRIGHTNESS_POLICY_head
    class VIDEO_BRIGHTNESS_POLICY__Anonymous_e__Struct(Structure):
        pass
    VIDEO_BRIGHTNESS_POLICY__Anonymous_e__Struct._fields_ = [
        ('BatteryLevel', Byte),
        ('Brightness', Byte),
    ]
    VIDEO_BRIGHTNESS_POLICY._fields_ = [
        ('DefaultToBiosPolicy', win32more.Foundation.BOOLEAN),
        ('LevelCount', Byte),
        ('Level', VIDEO_BRIGHTNESS_POLICY__Anonymous_e__Struct * 1),
    ]
    return VIDEO_BRIGHTNESS_POLICY
def _define_VIDEO_CLUT_head():
    class VIDEO_CLUT(Structure):
        pass
    return VIDEO_CLUT
def _define_VIDEO_CLUT():
    VIDEO_CLUT = win32more.Devices.Display.VIDEO_CLUT_head
    class VIDEO_CLUT__Anonymous_e__Union(Union):
        pass
    VIDEO_CLUT__Anonymous_e__Union._fields_ = [
        ('RgbArray', win32more.Devices.Display.VIDEO_CLUTDATA),
        ('RgbLong', UInt32),
    ]
    VIDEO_CLUT._fields_ = [
        ('NumEntries', UInt16),
        ('FirstEntry', UInt16),
        ('LookupTable', VIDEO_CLUT__Anonymous_e__Union * 1),
    ]
    return VIDEO_CLUT
def _define_VIDEO_CLUTDATA_head():
    class VIDEO_CLUTDATA(Structure):
        pass
    return VIDEO_CLUTDATA
def _define_VIDEO_CLUTDATA():
    VIDEO_CLUTDATA = win32more.Devices.Display.VIDEO_CLUTDATA_head
    VIDEO_CLUTDATA._fields_ = [
        ('Red', Byte),
        ('Green', Byte),
        ('Blue', Byte),
        ('Unused', Byte),
    ]
    return VIDEO_CLUTDATA
def _define_VIDEO_COLOR_CAPABILITIES_head():
    class VIDEO_COLOR_CAPABILITIES(Structure):
        pass
    return VIDEO_COLOR_CAPABILITIES
def _define_VIDEO_COLOR_CAPABILITIES():
    VIDEO_COLOR_CAPABILITIES = win32more.Devices.Display.VIDEO_COLOR_CAPABILITIES_head
    VIDEO_COLOR_CAPABILITIES._fields_ = [
        ('Length', UInt32),
        ('AttributeFlags', UInt32),
        ('RedPhosphoreDecay', Int32),
        ('GreenPhosphoreDecay', Int32),
        ('BluePhosphoreDecay', Int32),
        ('WhiteChromaticity_x', Int32),
        ('WhiteChromaticity_y', Int32),
        ('WhiteChromaticity_Y', Int32),
        ('RedChromaticity_x', Int32),
        ('RedChromaticity_y', Int32),
        ('GreenChromaticity_x', Int32),
        ('GreenChromaticity_y', Int32),
        ('BlueChromaticity_x', Int32),
        ('BlueChromaticity_y', Int32),
        ('WhiteGamma', Int32),
        ('RedGamma', Int32),
        ('GreenGamma', Int32),
        ('BlueGamma', Int32),
    ]
    return VIDEO_COLOR_CAPABILITIES
def _define_VIDEO_COLOR_LUT_DATA_head():
    class VIDEO_COLOR_LUT_DATA(Structure):
        pass
    return VIDEO_COLOR_LUT_DATA
def _define_VIDEO_COLOR_LUT_DATA():
    VIDEO_COLOR_LUT_DATA = win32more.Devices.Display.VIDEO_COLOR_LUT_DATA_head
    VIDEO_COLOR_LUT_DATA._fields_ = [
        ('Length', UInt32),
        ('LutDataFormat', UInt32),
        ('LutData', Byte * 1),
    ]
    return VIDEO_COLOR_LUT_DATA
def _define_VIDEO_CURSOR_ATTRIBUTES_head():
    class VIDEO_CURSOR_ATTRIBUTES(Structure):
        pass
    return VIDEO_CURSOR_ATTRIBUTES
def _define_VIDEO_CURSOR_ATTRIBUTES():
    VIDEO_CURSOR_ATTRIBUTES = win32more.Devices.Display.VIDEO_CURSOR_ATTRIBUTES_head
    VIDEO_CURSOR_ATTRIBUTES._fields_ = [
        ('Width', UInt16),
        ('Height', UInt16),
        ('Column', Int16),
        ('Row', Int16),
        ('Rate', Byte),
        ('Enable', Byte),
    ]
    return VIDEO_CURSOR_ATTRIBUTES
def _define_VIDEO_CURSOR_POSITION_head():
    class VIDEO_CURSOR_POSITION(Structure):
        pass
    return VIDEO_CURSOR_POSITION
def _define_VIDEO_CURSOR_POSITION():
    VIDEO_CURSOR_POSITION = win32more.Devices.Display.VIDEO_CURSOR_POSITION_head
    VIDEO_CURSOR_POSITION._fields_ = [
        ('Column', Int16),
        ('Row', Int16),
    ]
    return VIDEO_CURSOR_POSITION
def _define_VIDEO_DEVICE_SESSION_STATUS_head():
    class VIDEO_DEVICE_SESSION_STATUS(Structure):
        pass
    return VIDEO_DEVICE_SESSION_STATUS
def _define_VIDEO_DEVICE_SESSION_STATUS():
    VIDEO_DEVICE_SESSION_STATUS = win32more.Devices.Display.VIDEO_DEVICE_SESSION_STATUS_head
    VIDEO_DEVICE_SESSION_STATUS._fields_ = [
        ('bEnable', UInt32),
        ('bSuccess', UInt32),
    ]
    return VIDEO_DEVICE_SESSION_STATUS
def _define_VIDEO_HARDWARE_STATE_head():
    class VIDEO_HARDWARE_STATE(Structure):
        pass
    return VIDEO_HARDWARE_STATE
def _define_VIDEO_HARDWARE_STATE():
    VIDEO_HARDWARE_STATE = win32more.Devices.Display.VIDEO_HARDWARE_STATE_head
    VIDEO_HARDWARE_STATE._fields_ = [
        ('StateHeader', POINTER(win32more.Devices.Display.VIDEO_HARDWARE_STATE_HEADER_head)),
        ('StateLength', UInt32),
    ]
    return VIDEO_HARDWARE_STATE
def _define_VIDEO_HARDWARE_STATE_HEADER_head():
    class VIDEO_HARDWARE_STATE_HEADER(Structure):
        pass
    return VIDEO_HARDWARE_STATE_HEADER
def _define_VIDEO_HARDWARE_STATE_HEADER():
    VIDEO_HARDWARE_STATE_HEADER = win32more.Devices.Display.VIDEO_HARDWARE_STATE_HEADER_head
    VIDEO_HARDWARE_STATE_HEADER._fields_ = [
        ('Length', UInt32),
        ('PortValue', Byte * 48),
        ('AttribIndexDataState', UInt32),
        ('BasicSequencerOffset', UInt32),
        ('BasicCrtContOffset', UInt32),
        ('BasicGraphContOffset', UInt32),
        ('BasicAttribContOffset', UInt32),
        ('BasicDacOffset', UInt32),
        ('BasicLatchesOffset', UInt32),
        ('ExtendedSequencerOffset', UInt32),
        ('ExtendedCrtContOffset', UInt32),
        ('ExtendedGraphContOffset', UInt32),
        ('ExtendedAttribContOffset', UInt32),
        ('ExtendedDacOffset', UInt32),
        ('ExtendedValidatorStateOffset', UInt32),
        ('ExtendedMiscDataOffset', UInt32),
        ('PlaneLength', UInt32),
        ('Plane1Offset', UInt32),
        ('Plane2Offset', UInt32),
        ('Plane3Offset', UInt32),
        ('Plane4Offset', UInt32),
        ('VGAStateFlags', UInt32),
        ('DIBOffset', UInt32),
        ('DIBBitsPerPixel', UInt32),
        ('DIBXResolution', UInt32),
        ('DIBYResolution', UInt32),
        ('DIBXlatOffset', UInt32),
        ('DIBXlatLength', UInt32),
        ('VesaInfoOffset', UInt32),
        ('FrameBufferData', c_void_p),
    ]
    return VIDEO_HARDWARE_STATE_HEADER
def _define_VIDEO_LOAD_FONT_INFORMATION_head():
    class VIDEO_LOAD_FONT_INFORMATION(Structure):
        pass
    return VIDEO_LOAD_FONT_INFORMATION
def _define_VIDEO_LOAD_FONT_INFORMATION():
    VIDEO_LOAD_FONT_INFORMATION = win32more.Devices.Display.VIDEO_LOAD_FONT_INFORMATION_head
    VIDEO_LOAD_FONT_INFORMATION._fields_ = [
        ('WidthInPixels', UInt16),
        ('HeightInPixels', UInt16),
        ('FontSize', UInt32),
        ('Font', Byte * 1),
    ]
    return VIDEO_LOAD_FONT_INFORMATION
def _define_VIDEO_LUT_RGB256WORDS_head():
    class VIDEO_LUT_RGB256WORDS(Structure):
        pass
    return VIDEO_LUT_RGB256WORDS
def _define_VIDEO_LUT_RGB256WORDS():
    VIDEO_LUT_RGB256WORDS = win32more.Devices.Display.VIDEO_LUT_RGB256WORDS_head
    VIDEO_LUT_RGB256WORDS._fields_ = [
        ('Red', UInt16 * 256),
        ('Green', UInt16 * 256),
        ('Blue', UInt16 * 256),
    ]
    return VIDEO_LUT_RGB256WORDS
def _define_VIDEO_MEMORY_head():
    class VIDEO_MEMORY(Structure):
        pass
    return VIDEO_MEMORY
def _define_VIDEO_MEMORY():
    VIDEO_MEMORY = win32more.Devices.Display.VIDEO_MEMORY_head
    VIDEO_MEMORY._fields_ = [
        ('RequestedVirtualAddress', c_void_p),
    ]
    return VIDEO_MEMORY
def _define_VIDEO_MEMORY_INFORMATION_head():
    class VIDEO_MEMORY_INFORMATION(Structure):
        pass
    return VIDEO_MEMORY_INFORMATION
def _define_VIDEO_MEMORY_INFORMATION():
    VIDEO_MEMORY_INFORMATION = win32more.Devices.Display.VIDEO_MEMORY_INFORMATION_head
    VIDEO_MEMORY_INFORMATION._fields_ = [
        ('VideoRamBase', c_void_p),
        ('VideoRamLength', UInt32),
        ('FrameBufferBase', c_void_p),
        ('FrameBufferLength', UInt32),
    ]
    return VIDEO_MEMORY_INFORMATION
def _define_VIDEO_MODE_head():
    class VIDEO_MODE(Structure):
        pass
    return VIDEO_MODE
def _define_VIDEO_MODE():
    VIDEO_MODE = win32more.Devices.Display.VIDEO_MODE_head
    VIDEO_MODE._fields_ = [
        ('RequestedMode', UInt32),
    ]
    return VIDEO_MODE
def _define_VIDEO_MODE_INFORMATION_head():
    class VIDEO_MODE_INFORMATION(Structure):
        pass
    return VIDEO_MODE_INFORMATION
def _define_VIDEO_MODE_INFORMATION():
    VIDEO_MODE_INFORMATION = win32more.Devices.Display.VIDEO_MODE_INFORMATION_head
    VIDEO_MODE_INFORMATION._fields_ = [
        ('Length', UInt32),
        ('ModeIndex', UInt32),
        ('VisScreenWidth', UInt32),
        ('VisScreenHeight', UInt32),
        ('ScreenStride', UInt32),
        ('NumberOfPlanes', UInt32),
        ('BitsPerPlane', UInt32),
        ('Frequency', UInt32),
        ('XMillimeter', UInt32),
        ('YMillimeter', UInt32),
        ('NumberRedBits', UInt32),
        ('NumberGreenBits', UInt32),
        ('NumberBlueBits', UInt32),
        ('RedMask', UInt32),
        ('GreenMask', UInt32),
        ('BlueMask', UInt32),
        ('AttributeFlags', UInt32),
        ('VideoMemoryBitmapWidth', UInt32),
        ('VideoMemoryBitmapHeight', UInt32),
        ('DriverSpecificAttributeFlags', UInt32),
    ]
    return VIDEO_MODE_INFORMATION
def _define_VIDEO_MONITOR_DESCRIPTOR_head():
    class VIDEO_MONITOR_DESCRIPTOR(Structure):
        pass
    return VIDEO_MONITOR_DESCRIPTOR
def _define_VIDEO_MONITOR_DESCRIPTOR():
    VIDEO_MONITOR_DESCRIPTOR = win32more.Devices.Display.VIDEO_MONITOR_DESCRIPTOR_head
    VIDEO_MONITOR_DESCRIPTOR._fields_ = [
        ('DescriptorSize', UInt32),
        ('Descriptor', Byte * 1),
    ]
    return VIDEO_MONITOR_DESCRIPTOR
def _define_VIDEO_NUM_MODES_head():
    class VIDEO_NUM_MODES(Structure):
        pass
    return VIDEO_NUM_MODES
def _define_VIDEO_NUM_MODES():
    VIDEO_NUM_MODES = win32more.Devices.Display.VIDEO_NUM_MODES_head
    VIDEO_NUM_MODES._fields_ = [
        ('NumModes', UInt32),
        ('ModeInformationLength', UInt32),
    ]
    return VIDEO_NUM_MODES
def _define_VIDEO_PALETTE_DATA_head():
    class VIDEO_PALETTE_DATA(Structure):
        pass
    return VIDEO_PALETTE_DATA
def _define_VIDEO_PALETTE_DATA():
    VIDEO_PALETTE_DATA = win32more.Devices.Display.VIDEO_PALETTE_DATA_head
    VIDEO_PALETTE_DATA._fields_ = [
        ('NumEntries', UInt16),
        ('FirstEntry', UInt16),
        ('Colors', UInt16 * 1),
    ]
    return VIDEO_PALETTE_DATA
def _define_VIDEO_PERFORMANCE_COUNTER_head():
    class VIDEO_PERFORMANCE_COUNTER(Structure):
        pass
    return VIDEO_PERFORMANCE_COUNTER
def _define_VIDEO_PERFORMANCE_COUNTER():
    VIDEO_PERFORMANCE_COUNTER = win32more.Devices.Display.VIDEO_PERFORMANCE_COUNTER_head
    VIDEO_PERFORMANCE_COUNTER._fields_ = [
        ('NbOfAllocationEvicted', UInt64 * 10),
        ('NbOfAllocationMarked', UInt64 * 10),
        ('NbOfAllocationRestored', UInt64 * 10),
        ('KBytesEvicted', UInt64 * 10),
        ('KBytesMarked', UInt64 * 10),
        ('KBytesRestored', UInt64 * 10),
        ('NbProcessCommited', UInt64),
        ('NbAllocationCommited', UInt64),
        ('NbAllocationMarked', UInt64),
        ('KBytesAllocated', UInt64),
        ('KBytesAvailable', UInt64),
        ('KBytesCurMarked', UInt64),
        ('Reference', UInt64),
        ('Unreference', UInt64),
        ('TrueReference', UInt64),
        ('NbOfPageIn', UInt64),
        ('KBytesPageIn', UInt64),
        ('NbOfPageOut', UInt64),
        ('KBytesPageOut', UInt64),
        ('NbOfRotateOut', UInt64),
        ('KBytesRotateOut', UInt64),
    ]
    return VIDEO_PERFORMANCE_COUNTER
def _define_VIDEO_POINTER_ATTRIBUTES_head():
    class VIDEO_POINTER_ATTRIBUTES(Structure):
        pass
    return VIDEO_POINTER_ATTRIBUTES
def _define_VIDEO_POINTER_ATTRIBUTES():
    VIDEO_POINTER_ATTRIBUTES = win32more.Devices.Display.VIDEO_POINTER_ATTRIBUTES_head
    VIDEO_POINTER_ATTRIBUTES._fields_ = [
        ('Flags', UInt32),
        ('Width', UInt32),
        ('Height', UInt32),
        ('WidthInBytes', UInt32),
        ('Enable', UInt32),
        ('Column', Int16),
        ('Row', Int16),
        ('Pixels', Byte * 1),
    ]
    return VIDEO_POINTER_ATTRIBUTES
def _define_VIDEO_POINTER_CAPABILITIES_head():
    class VIDEO_POINTER_CAPABILITIES(Structure):
        pass
    return VIDEO_POINTER_CAPABILITIES
def _define_VIDEO_POINTER_CAPABILITIES():
    VIDEO_POINTER_CAPABILITIES = win32more.Devices.Display.VIDEO_POINTER_CAPABILITIES_head
    VIDEO_POINTER_CAPABILITIES._fields_ = [
        ('Flags', UInt32),
        ('MaxWidth', UInt32),
        ('MaxHeight', UInt32),
        ('HWPtrBitmapStart', UInt32),
        ('HWPtrBitmapEnd', UInt32),
    ]
    return VIDEO_POINTER_CAPABILITIES
def _define_VIDEO_POINTER_POSITION_head():
    class VIDEO_POINTER_POSITION(Structure):
        pass
    return VIDEO_POINTER_POSITION
def _define_VIDEO_POINTER_POSITION():
    VIDEO_POINTER_POSITION = win32more.Devices.Display.VIDEO_POINTER_POSITION_head
    VIDEO_POINTER_POSITION._fields_ = [
        ('Column', Int16),
        ('Row', Int16),
    ]
    return VIDEO_POINTER_POSITION
def _define_VIDEO_POWER_MANAGEMENT_head():
    class VIDEO_POWER_MANAGEMENT(Structure):
        pass
    return VIDEO_POWER_MANAGEMENT
def _define_VIDEO_POWER_MANAGEMENT():
    VIDEO_POWER_MANAGEMENT = win32more.Devices.Display.VIDEO_POWER_MANAGEMENT_head
    VIDEO_POWER_MANAGEMENT._fields_ = [
        ('Length', UInt32),
        ('DPMSVersion', UInt32),
        ('PowerState', UInt32),
    ]
    return VIDEO_POWER_MANAGEMENT
VIDEO_POWER_STATE = Int32
VIDEO_POWER_STATE_VideoPowerUnspecified = 0
VIDEO_POWER_STATE_VideoPowerOn = 1
VIDEO_POWER_STATE_VideoPowerStandBy = 2
VIDEO_POWER_STATE_VideoPowerSuspend = 3
VIDEO_POWER_STATE_VideoPowerOff = 4
VIDEO_POWER_STATE_VideoPowerHibernate = 5
VIDEO_POWER_STATE_VideoPowerShutdown = 6
VIDEO_POWER_STATE_VideoPowerMaximum = 7
def _define_VIDEO_PUBLIC_ACCESS_RANGES_head():
    class VIDEO_PUBLIC_ACCESS_RANGES(Structure):
        pass
    return VIDEO_PUBLIC_ACCESS_RANGES
def _define_VIDEO_PUBLIC_ACCESS_RANGES():
    VIDEO_PUBLIC_ACCESS_RANGES = win32more.Devices.Display.VIDEO_PUBLIC_ACCESS_RANGES_head
    VIDEO_PUBLIC_ACCESS_RANGES._fields_ = [
        ('InIoSpace', UInt32),
        ('MappedInIoSpace', UInt32),
        ('VirtualAddress', c_void_p),
    ]
    return VIDEO_PUBLIC_ACCESS_RANGES
def _define_VIDEO_QUERY_PERFORMANCE_COUNTER_head():
    class VIDEO_QUERY_PERFORMANCE_COUNTER(Structure):
        pass
    return VIDEO_QUERY_PERFORMANCE_COUNTER
def _define_VIDEO_QUERY_PERFORMANCE_COUNTER():
    VIDEO_QUERY_PERFORMANCE_COUNTER = win32more.Devices.Display.VIDEO_QUERY_PERFORMANCE_COUNTER_head
    VIDEO_QUERY_PERFORMANCE_COUNTER._fields_ = [
        ('BufferSize', UInt32),
        ('Buffer', POINTER(win32more.Devices.Display.VIDEO_PERFORMANCE_COUNTER_head)),
    ]
    return VIDEO_QUERY_PERFORMANCE_COUNTER
def _define_VIDEO_REGISTER_VDM_head():
    class VIDEO_REGISTER_VDM(Structure):
        pass
    return VIDEO_REGISTER_VDM
def _define_VIDEO_REGISTER_VDM():
    VIDEO_REGISTER_VDM = win32more.Devices.Display.VIDEO_REGISTER_VDM_head
    VIDEO_REGISTER_VDM._fields_ = [
        ('MinimumStateSize', UInt32),
    ]
    return VIDEO_REGISTER_VDM
def _define_VIDEO_SHARE_MEMORY_head():
    class VIDEO_SHARE_MEMORY(Structure):
        pass
    return VIDEO_SHARE_MEMORY
def _define_VIDEO_SHARE_MEMORY():
    VIDEO_SHARE_MEMORY = win32more.Devices.Display.VIDEO_SHARE_MEMORY_head
    VIDEO_SHARE_MEMORY._fields_ = [
        ('ProcessHandle', win32more.Foundation.HANDLE),
        ('ViewOffset', UInt32),
        ('ViewSize', UInt32),
        ('RequestedVirtualAddress', c_void_p),
    ]
    return VIDEO_SHARE_MEMORY
def _define_VIDEO_SHARE_MEMORY_INFORMATION_head():
    class VIDEO_SHARE_MEMORY_INFORMATION(Structure):
        pass
    return VIDEO_SHARE_MEMORY_INFORMATION
def _define_VIDEO_SHARE_MEMORY_INFORMATION():
    VIDEO_SHARE_MEMORY_INFORMATION = win32more.Devices.Display.VIDEO_SHARE_MEMORY_INFORMATION_head
    VIDEO_SHARE_MEMORY_INFORMATION._fields_ = [
        ('SharedViewOffset', UInt32),
        ('SharedViewSize', UInt32),
        ('VirtualAddress', c_void_p),
    ]
    return VIDEO_SHARE_MEMORY_INFORMATION
def _define_VIDEO_VDM_head():
    class VIDEO_VDM(Structure):
        pass
    return VIDEO_VDM
def _define_VIDEO_VDM():
    VIDEO_VDM = win32more.Devices.Display.VIDEO_VDM_head
    VIDEO_VDM._fields_ = [
        ('ProcessHandle', win32more.Foundation.HANDLE),
    ]
    return VIDEO_VDM
def _define_VIDEO_WIN32K_CALLBACKS_head():
    class VIDEO_WIN32K_CALLBACKS(Structure):
        pass
    return VIDEO_WIN32K_CALLBACKS
def _define_VIDEO_WIN32K_CALLBACKS():
    VIDEO_WIN32K_CALLBACKS = win32more.Devices.Display.VIDEO_WIN32K_CALLBACKS_head
    VIDEO_WIN32K_CALLBACKS._fields_ = [
        ('PhysDisp', c_void_p),
        ('Callout', win32more.Devices.Display.PVIDEO_WIN32K_CALLOUT),
        ('bACPI', UInt32),
        ('pPhysDeviceObject', win32more.Foundation.HANDLE),
        ('DualviewFlags', UInt32),
    ]
    return VIDEO_WIN32K_CALLBACKS
def _define_VIDEO_WIN32K_CALLBACKS_PARAMS_head():
    class VIDEO_WIN32K_CALLBACKS_PARAMS(Structure):
        pass
    return VIDEO_WIN32K_CALLBACKS_PARAMS
def _define_VIDEO_WIN32K_CALLBACKS_PARAMS():
    VIDEO_WIN32K_CALLBACKS_PARAMS = win32more.Devices.Display.VIDEO_WIN32K_CALLBACKS_PARAMS_head
    VIDEO_WIN32K_CALLBACKS_PARAMS._fields_ = [
        ('CalloutType', win32more.Devices.Display.VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE),
        ('PhysDisp', c_void_p),
        ('Param', UIntPtr),
        ('Status', Int32),
        ('LockUserSession', win32more.Foundation.BOOLEAN),
        ('IsPostDevice', win32more.Foundation.BOOLEAN),
        ('SurpriseRemoval', win32more.Foundation.BOOLEAN),
        ('WaitForQueueReady', win32more.Foundation.BOOLEAN),
    ]
    return VIDEO_WIN32K_CALLBACKS_PARAMS
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE = Int32
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoPowerNotifyCallout = 1
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoEnumChildPdoNotifyCallout = 3
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoFindAdapterCallout = 4
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoPnpNotifyCallout = 7
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkDisplaySwitchCallout = 8
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkFindAdapterTdrCallout = 10
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkHardwareProtectionTeardown = 11
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoRepaintDesktop = 12
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoUpdateCursor = 13
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDisableMultiPlaneOverlay = 14
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDesktopDuplicationChange = 15
VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoBlackScreenDiagnostics = 16
def _define_VIDEOPARAMETERS_head():
    class VIDEOPARAMETERS(Structure):
        pass
    return VIDEOPARAMETERS
def _define_VIDEOPARAMETERS():
    VIDEOPARAMETERS = win32more.Devices.Display.VIDEOPARAMETERS_head
    VIDEOPARAMETERS._fields_ = [
        ('Guid', Guid),
        ('dwOffset', UInt32),
        ('dwCommand', UInt32),
        ('dwFlags', UInt32),
        ('dwMode', UInt32),
        ('dwTVStandard', UInt32),
        ('dwAvailableModes', UInt32),
        ('dwAvailableTVStandard', UInt32),
        ('dwFlickerFilter', UInt32),
        ('dwOverScanX', UInt32),
        ('dwOverScanY', UInt32),
        ('dwMaxUnscaledX', UInt32),
        ('dwMaxUnscaledY', UInt32),
        ('dwPositionX', UInt32),
        ('dwPositionY', UInt32),
        ('dwBrightness', UInt32),
        ('dwContrast', UInt32),
        ('dwCPType', UInt32),
        ('dwCPCommand', UInt32),
        ('dwCPStandard', UInt32),
        ('dwCPKey', UInt32),
        ('bCP_APSTriggerBits', UInt32),
        ('bOEMCopyProtection', Byte * 256),
    ]
    return VIDEOPARAMETERS
def _define_WCRUN_head():
    class WCRUN(Structure):
        pass
    return WCRUN
def _define_WCRUN():
    WCRUN = win32more.Devices.Display.WCRUN_head
    WCRUN._fields_ = [
        ('wcLow', Char),
        ('cGlyphs', UInt16),
        ('phg', POINTER(UInt32)),
    ]
    return WCRUN
def _define_WNDOBJ_head():
    class WNDOBJ(Structure):
        pass
    return WNDOBJ
def _define_WNDOBJ():
    WNDOBJ = win32more.Devices.Display.WNDOBJ_head
    WNDOBJ._fields_ = [
        ('coClient', win32more.Devices.Display.CLIPOBJ),
        ('pvConsumer', c_void_p),
        ('rclClient', win32more.Foundation.RECTL),
        ('psoOwner', POINTER(win32more.Devices.Display.SURFOBJ_head)),
    ]
    return WNDOBJ
def _define_WNDOBJCHANGEPROC():
    return WINFUNCTYPE(Void,POINTER(win32more.Devices.Display.WNDOBJ_head),UInt32)
def _define_XFORML_head():
    class XFORML(Structure):
        pass
    return XFORML
def _define_XFORML():
    XFORML = win32more.Devices.Display.XFORML_head
    XFORML._fields_ = [
        ('eM11', Single),
        ('eM12', Single),
        ('eM21', Single),
        ('eM22', Single),
        ('eDx', Single),
        ('eDy', Single),
    ]
    return XFORML
def _define_XFORMOBJ_head():
    class XFORMOBJ(Structure):
        pass
    return XFORMOBJ
def _define_XFORMOBJ():
    XFORMOBJ = win32more.Devices.Display.XFORMOBJ_head
    XFORMOBJ._fields_ = [
        ('ulReserved', UInt32),
    ]
    return XFORMOBJ
def _define_XLATEOBJ_head():
    class XLATEOBJ(Structure):
        pass
    return XLATEOBJ
def _define_XLATEOBJ():
    XLATEOBJ = win32more.Devices.Display.XLATEOBJ_head
    XLATEOBJ._fields_ = [
        ('iUniq', UInt32),
        ('flXlate', UInt32),
        ('iSrcType', UInt16),
        ('iDstType', UInt16),
        ('cEntries', UInt32),
        ('pulXlate', POINTER(UInt32)),
    ]
    return XLATEOBJ
__all__ = [
    "AR_DISABLED",
    "AR_DOCKED",
    "AR_ENABLED",
    "AR_LAPTOP",
    "AR_MULTIMON",
    "AR_NOSENSOR",
    "AR_NOT_SUPPORTED",
    "AR_REMOTESESSION",
    "AR_STATE",
    "AR_SUPPRESSED",
    "Adapter",
    "Adapters",
    "BACKLIGHT_OPTIMIZATION_LEVEL",
    "BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDesktop",
    "BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDimmed",
    "BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDisable",
    "BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationDynamic",
    "BACKLIGHT_OPTIMIZATION_LEVEL_BacklightOptimizationEDR",
    "BACKLIGHT_REDUCTION_GAMMA_RAMP",
    "BANK_POSITION",
    "BITMAP_ARRAY_BYTE",
    "BITMAP_BITS_BYTE_ALIGN",
    "BITMAP_BITS_PIXEL",
    "BITMAP_BITS_WORD_ALIGN",
    "BITMAP_PLANES",
    "BLENDOBJ",
    "BMF_16BPP",
    "BMF_1BPP",
    "BMF_24BPP",
    "BMF_32BPP",
    "BMF_4BPP",
    "BMF_4RLE",
    "BMF_8BPP",
    "BMF_8RLE",
    "BMF_ACC_NOTIFY",
    "BMF_DONTCACHE",
    "BMF_JPEG",
    "BMF_KMSECTION",
    "BMF_NOTSYSMEM",
    "BMF_NOZEROINIT",
    "BMF_PNG",
    "BMF_RESERVED",
    "BMF_RMT_ENTER",
    "BMF_TEMP_ALPHA",
    "BMF_TOPDOWN",
    "BMF_UMPDMEM",
    "BMF_USERMEM",
    "BMF_WINDOW_BLT",
    "BRIGHTNESS_INTERFACE_VERSION",
    "BRIGHTNESS_INTERFACE_VERSION_1",
    "BRIGHTNESS_INTERFACE_VERSION_2",
    "BRIGHTNESS_INTERFACE_VERSION_3",
    "BRIGHTNESS_LEVEL",
    "BRIGHTNESS_MAX_LEVEL_COUNT",
    "BRIGHTNESS_MAX_NIT_RANGE_COUNT",
    "BRIGHTNESS_NIT_RANGE",
    "BRIGHTNESS_NIT_RANGES",
    "BRUSHOBJ",
    "BRUSHOBJ_hGetColorTransform",
    "BRUSHOBJ_pvAllocRbrush",
    "BRUSHOBJ_pvGetRbrush",
    "BRUSHOBJ_ulGetBrushColor",
    "BR_CMYKCOLOR",
    "BR_DEVICE_ICM",
    "BR_HOST_ICM",
    "BR_ORIGCOLOR",
    "BlackScreenDiagnosticsCalloutParam",
    "BlackScreenDiagnosticsCalloutParam_BlackScreenDiagnosticsData",
    "BlackScreenDiagnosticsCalloutParam_BlackScreenDisplayRecovery",
    "CDBEX_CROSSADAPTER",
    "CDBEX_DXINTEROP",
    "CDBEX_NTSHAREDSURFACEHANDLE",
    "CDBEX_REDIRECTION",
    "CDBEX_REUSE",
    "CDDDXGK_REDIRBITMAPPRESENTINFO",
    "CD_ANY",
    "CD_LEFTDOWN",
    "CD_LEFTUP",
    "CD_LEFTWARDS",
    "CD_RIGHTDOWN",
    "CD_RIGHTUP",
    "CD_UPWARDS",
    "CHAR_IMAGE_INFO",
    "CHAR_TYPE_LEADING",
    "CHAR_TYPE_SBCS",
    "CHAR_TYPE_TRAILING",
    "CHROMATICITY_COORDINATE",
    "CIECHROMA",
    "CLIPLINE",
    "CLIPOBJ",
    "CLIPOBJ_bEnum",
    "CLIPOBJ_cEnumStart",
    "CLIPOBJ_ppoGetPath",
    "COLORINFO",
    "COLORSPACE_TRANSFORM",
    "COLORSPACE_TRANSFORM_1DLUT_CAP",
    "COLORSPACE_TRANSFORM_3x4",
    "COLORSPACE_TRANSFORM_DATA_CAP",
    "COLORSPACE_TRANSFORM_DATA_TYPE",
    "COLORSPACE_TRANSFORM_DATA_TYPE_FIXED_POINT",
    "COLORSPACE_TRANSFORM_DATA_TYPE_FLOAT",
    "COLORSPACE_TRANSFORM_MATRIX_CAP",
    "COLORSPACE_TRANSFORM_MATRIX_V2",
    "COLORSPACE_TRANSFORM_SET_INPUT",
    "COLORSPACE_TRANSFORM_STAGE_CONTROL",
    "COLORSPACE_TRANSFORM_TARGET_CAPS",
    "COLORSPACE_TRANSFORM_TARGET_CAPS_VERSION",
    "COLORSPACE_TRANSFORM_TYPE",
    "COLORSPACE_TRANSFORM_TYPE_DEFAULT",
    "COLORSPACE_TRANSFORM_TYPE_DXGI_1",
    "COLORSPACE_TRANSFORM_TYPE_MATRIX_3x4",
    "COLORSPACE_TRANSFORM_TYPE_MATRIX_V2",
    "COLORSPACE_TRANSFORM_TYPE_RGB256x3x16",
    "COLORSPACE_TRANSFORM_TYPE_UNINITIALIZED",
    "COLORSPACE_TRANSFORM_VERSION_1",
    "COLORSPACE_TRANSFORM_VERSION_DEFAULT",
    "COLORSPACE_TRANSFORM_VERSION_NOT_SUPPORTED",
    "CT_RECTANGLES",
    "CapabilitiesRequestAndCapabilitiesReply",
    "ColorSpaceTransformStageControl_Bypass",
    "ColorSpaceTransformStageControl_Enable",
    "ColorSpaceTransformStageControl_No_Change",
    "DCR_DRIVER",
    "DCR_HALFTONE",
    "DCR_SOLID",
    "DCT_DEFAULT",
    "DCT_FORCE_HIGH_PERFORMANCE",
    "DCT_FORCE_LOW_POWER",
    "DC_COMPLEX",
    "DC_RECT",
    "DC_TRIVIAL",
    "DDI_DRIVER_VERSION_NT4",
    "DDI_DRIVER_VERSION_NT5",
    "DDI_DRIVER_VERSION_NT5_01",
    "DDI_DRIVER_VERSION_NT5_01_SP1",
    "DDI_DRIVER_VERSION_SP3",
    "DDI_ERROR",
    "DD_FULLSCREEN_VIDEO_DEVICE_NAME",
    "DEVHTADJDATA",
    "DEVHTADJF_ADDITIVE_DEVICE",
    "DEVHTADJF_COLOR_DEVICE",
    "DEVHTINFO",
    "DEVINFO",
    "DEVPKEY_Device_ActivityId",
    "DEVPKEY_Device_AdapterLuid",
    "DEVPKEY_Device_TerminalLuid",
    "DEVPKEY_IndirectDisplay",
    "DHPDEV",
    "DHSURF",
    "DISPLAYCONFIG_2DREGION",
    "DISPLAYCONFIG_ADAPTER_NAME",
    "DISPLAYCONFIG_DESKTOP_IMAGE_INFO",
    "DISPLAYCONFIG_DEVICE_INFO_FORCE_UINT32",
    "DISPLAYCONFIG_DEVICE_INFO_GET_ADAPTER_NAME",
    "DISPLAYCONFIG_DEVICE_INFO_GET_ADVANCED_COLOR_INFO",
    "DISPLAYCONFIG_DEVICE_INFO_GET_MONITOR_SPECIALIZATION",
    "DISPLAYCONFIG_DEVICE_INFO_GET_SDR_WHITE_LEVEL",
    "DISPLAYCONFIG_DEVICE_INFO_GET_SOURCE_NAME",
    "DISPLAYCONFIG_DEVICE_INFO_GET_SUPPORT_VIRTUAL_RESOLUTION",
    "DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_BASE_TYPE",
    "DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_NAME",
    "DISPLAYCONFIG_DEVICE_INFO_GET_TARGET_PREFERRED_MODE",
    "DISPLAYCONFIG_DEVICE_INFO_HEADER",
    "DISPLAYCONFIG_DEVICE_INFO_SET_ADVANCED_COLOR_STATE",
    "DISPLAYCONFIG_DEVICE_INFO_SET_MONITOR_SPECIALIZATION",
    "DISPLAYCONFIG_DEVICE_INFO_SET_SUPPORT_VIRTUAL_RESOLUTION",
    "DISPLAYCONFIG_DEVICE_INFO_SET_TARGET_PERSISTENCE",
    "DISPLAYCONFIG_DEVICE_INFO_TYPE",
    "DISPLAYCONFIG_GET_ADVANCED_COLOR_INFO",
    "DISPLAYCONFIG_GET_MONITOR_SPECIALIZATION",
    "DISPLAYCONFIG_MODE_INFO",
    "DISPLAYCONFIG_MODE_INFO_TYPE",
    "DISPLAYCONFIG_MODE_INFO_TYPE_DESKTOP_IMAGE",
    "DISPLAYCONFIG_MODE_INFO_TYPE_FORCE_UINT32",
    "DISPLAYCONFIG_MODE_INFO_TYPE_SOURCE",
    "DISPLAYCONFIG_MODE_INFO_TYPE_TARGET",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPONENT_VIDEO",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_COMPOSITE_VIDEO",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EMBEDDED",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_EXTERNAL",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DISPLAYPORT_USB_TUNNEL",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_DVI",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_D_JPN",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_FORCE_UINT32",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HD15",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HDMI",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_VIRTUAL",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INDIRECT_WIRED",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_INTERNAL",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_LVDS",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_OTHER",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDI",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SDTVDONGLE",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_SVIDEO",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EMBEDDED",
    "DISPLAYCONFIG_OUTPUT_TECHNOLOGY_UDI_EXTERNAL",
    "DISPLAYCONFIG_PATH_INFO",
    "DISPLAYCONFIG_PATH_SOURCE_INFO",
    "DISPLAYCONFIG_PATH_TARGET_INFO",
    "DISPLAYCONFIG_PIXELFORMAT",
    "DISPLAYCONFIG_PIXELFORMAT_16BPP",
    "DISPLAYCONFIG_PIXELFORMAT_24BPP",
    "DISPLAYCONFIG_PIXELFORMAT_32BPP",
    "DISPLAYCONFIG_PIXELFORMAT_8BPP",
    "DISPLAYCONFIG_PIXELFORMAT_FORCE_UINT32",
    "DISPLAYCONFIG_PIXELFORMAT_NONGDI",
    "DISPLAYCONFIG_RATIONAL",
    "DISPLAYCONFIG_ROTATION",
    "DISPLAYCONFIG_ROTATION_FORCE_UINT32",
    "DISPLAYCONFIG_ROTATION_IDENTITY",
    "DISPLAYCONFIG_ROTATION_ROTATE180",
    "DISPLAYCONFIG_ROTATION_ROTATE270",
    "DISPLAYCONFIG_ROTATION_ROTATE90",
    "DISPLAYCONFIG_SCALING",
    "DISPLAYCONFIG_SCALING_ASPECTRATIOCENTEREDMAX",
    "DISPLAYCONFIG_SCALING_CENTERED",
    "DISPLAYCONFIG_SCALING_CUSTOM",
    "DISPLAYCONFIG_SCALING_FORCE_UINT32",
    "DISPLAYCONFIG_SCALING_IDENTITY",
    "DISPLAYCONFIG_SCALING_PREFERRED",
    "DISPLAYCONFIG_SCALING_STRETCHED",
    "DISPLAYCONFIG_SCANLINE_ORDERING",
    "DISPLAYCONFIG_SCANLINE_ORDERING_FORCE_UINT32",
    "DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED",
    "DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_LOWERFIELDFIRST",
    "DISPLAYCONFIG_SCANLINE_ORDERING_INTERLACED_UPPERFIELDFIRST",
    "DISPLAYCONFIG_SCANLINE_ORDERING_PROGRESSIVE",
    "DISPLAYCONFIG_SCANLINE_ORDERING_UNSPECIFIED",
    "DISPLAYCONFIG_SDR_WHITE_LEVEL",
    "DISPLAYCONFIG_SET_ADVANCED_COLOR_STATE",
    "DISPLAYCONFIG_SET_MONITOR_SPECIALIZATION",
    "DISPLAYCONFIG_SET_TARGET_PERSISTENCE",
    "DISPLAYCONFIG_SOURCE_DEVICE_NAME",
    "DISPLAYCONFIG_SOURCE_MODE",
    "DISPLAYCONFIG_SUPPORT_VIRTUAL_RESOLUTION",
    "DISPLAYCONFIG_TARGET_BASE_TYPE",
    "DISPLAYCONFIG_TARGET_DEVICE_NAME",
    "DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS",
    "DISPLAYCONFIG_TARGET_MODE",
    "DISPLAYCONFIG_TARGET_PREFERRED_MODE",
    "DISPLAYCONFIG_TOPOLOGY_CLONE",
    "DISPLAYCONFIG_TOPOLOGY_EXTEND",
    "DISPLAYCONFIG_TOPOLOGY_EXTERNAL",
    "DISPLAYCONFIG_TOPOLOGY_FORCE_UINT32",
    "DISPLAYCONFIG_TOPOLOGY_ID",
    "DISPLAYCONFIG_TOPOLOGY_INTERNAL",
    "DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY",
    "DISPLAYCONFIG_VIDEO_SIGNAL_INFO",
    "DISPLAYPOLICY_AC",
    "DISPLAYPOLICY_DC",
    "DISPLAY_BRIGHTNESS",
    "DM_DEFAULT",
    "DM_MONOCHROME",
    "DN_ACCELERATION_LEVEL",
    "DN_ASSOCIATE_WINDOW",
    "DN_COMPOSITION_CHANGED",
    "DN_DEVICE_ORIGIN",
    "DN_DRAWING_BEGIN",
    "DN_DRAWING_BEGIN_APIBITMAP",
    "DN_SLEEP_MODE",
    "DN_SURFOBJ_DESTRUCTION",
    "DRD_ERROR",
    "DRD_SUCCESS",
    "DRH_APIBITMAP",
    "DRH_APIBITMAPDATA",
    "DRIVEROBJ",
    "DRVENABLEDATA",
    "DRVFN",
    "DRVQUERY_USERMODE",
    "DSI_CHECKSUM_ERROR_CORRECTED",
    "DSI_CHECKSUM_ERROR_NOT_CORRECTED",
    "DSI_CONTENTION_DETECTED",
    "DSI_CONTROL_TRANSMISSION_MODE",
    "DSI_DSI_DATA_TYPE_NOT_RECOGNIZED",
    "DSI_DSI_PROTOCOL_VIOLATION",
    "DSI_DSI_VC_ID_INVALID",
    "DSI_EOT_SYNC_ERROR",
    "DSI_ESCAPE_MODE_ENTRY_COMMAND_ERROR",
    "DSI_FALSE_CONTROL_ERROR",
    "DSI_INVALID_PACKET_INDEX",
    "DSI_INVALID_TRANSMISSION_LENGTH",
    "DSI_LONG_PACKET_PAYLOAD_CHECKSUM_ERROR",
    "DSI_LOW_POWER_TRANSMIT_SYNC_ERROR",
    "DSI_PACKET_EMBEDDED_PAYLOAD_SIZE",
    "DSI_PERIPHERAL_TIMEOUT_ERROR",
    "DSI_SOT_ERROR",
    "DSI_SOT_SYNC_ERROR",
    "DSS_FLUSH_EVENT",
    "DSS_RESERVED",
    "DSS_RESERVED1",
    "DSS_RESERVED2",
    "DSS_TIMER_EVENT",
    "DXGK_WIN32K_PARAM_DATA",
    "DXGK_WIN32K_PARAM_FLAG_DISABLEVIEW",
    "DXGK_WIN32K_PARAM_FLAG_MODESWITCH",
    "DXGK_WIN32K_PARAM_FLAG_UPDATEREGISTRY",
    "DegaussMonitor",
    "DestroyPhysicalMonitor",
    "DestroyPhysicalMonitors",
    "DisplayConfigGetDeviceInfo",
    "DisplayConfigSetDeviceInfo",
    "DisplayMode",
    "DisplayModes",
    "ECS_REDRAW",
    "ECS_TEARDOWN",
    "ED_ABORTDOC",
    "EHN_ERROR",
    "EHN_RESTORED",
    "EMFINFO",
    "ENDCAP_BUTT",
    "ENDCAP_ROUND",
    "ENDCAP_SQUARE",
    "ENGSAFESEMAPHORE",
    "ENG_DEVICE_ATTRIBUTE",
    "ENG_EVENT",
    "ENG_FNT_CACHE_READ_FAULT",
    "ENG_FNT_CACHE_WRITE_FAULT",
    "ENG_SYSTEM_ATTRIBUTE",
    "ENG_SYSTEM_ATTRIBUTE_EngNumberOfProcessors",
    "ENG_SYSTEM_ATTRIBUTE_EngOptimumAvailableSystemMemory",
    "ENG_SYSTEM_ATTRIBUTE_EngOptimumAvailableUserMemory",
    "ENG_SYSTEM_ATTRIBUTE_EngProcessorFeature",
    "ENG_TIME_FIELDS",
    "ENUMRECTS",
    "EngAcquireSemaphore",
    "EngAlphaBlend",
    "EngAssociateSurface",
    "EngBitBlt",
    "EngCheckAbort",
    "EngComputeGlyphSet",
    "EngCopyBits",
    "EngCreateBitmap",
    "EngCreateClip",
    "EngCreateDeviceBitmap",
    "EngCreateDeviceSurface",
    "EngCreatePalette",
    "EngCreateSemaphore",
    "EngDeleteClip",
    "EngDeletePalette",
    "EngDeletePath",
    "EngDeleteSemaphore",
    "EngDeleteSurface",
    "EngEraseSurface",
    "EngFillPath",
    "EngFindResource",
    "EngFreeModule",
    "EngGetCurrentCodePage",
    "EngGetDriverName",
    "EngGetPrinterDataFileName",
    "EngGradientFill",
    "EngLineTo",
    "EngLoadModule",
    "EngLockSurface",
    "EngMarkBandingSurface",
    "EngMultiByteToUnicodeN",
    "EngMultiByteToWideChar",
    "EngPaint",
    "EngPlgBlt",
    "EngQueryEMFInfo",
    "EngQueryLocalTime",
    "EngReleaseSemaphore",
    "EngStretchBlt",
    "EngStretchBltROP",
    "EngStrokeAndFillPath",
    "EngStrokePath",
    "EngTextOut",
    "EngTransparentBlt",
    "EngUnicodeToMultiByteN",
    "EngUnlockSurface",
    "EngWideCharToMultiByte",
    "FC_COMPLEX",
    "FC_RECT",
    "FC_RECT4",
    "FDM_TYPE_BM_SIDE_CONST",
    "FDM_TYPE_CHAR_INC_EQUAL_BM_BASE",
    "FDM_TYPE_CONST_BEARINGS",
    "FDM_TYPE_MAXEXT_EQUAL_BM_SIDE",
    "FDM_TYPE_ZERO_BEARINGS",
    "FD_DEVICEMETRICS",
    "FD_ERROR",
    "FD_GLYPHATTR",
    "FD_GLYPHSET",
    "FD_KERNINGPAIR",
    "FD_LIGATURE",
    "FD_NEGATIVE_FONT",
    "FD_XFORM",
    "FF_IGNORED_SIGNATURE",
    "FF_SIGNATURE_VERIFIED",
    "FLOATOBJ_XFORM",
    "FLOAT_LONG",
    "FL_NONPAGED_MEMORY",
    "FL_NON_SESSION",
    "FL_ZERO_MEMORY",
    "FM_EDITABLE_EMBED",
    "FM_INFO_16BPP",
    "FM_INFO_1BPP",
    "FM_INFO_24BPP",
    "FM_INFO_32BPP",
    "FM_INFO_4BPP",
    "FM_INFO_8BPP",
    "FM_INFO_90DEGREE_ROTATIONS",
    "FM_INFO_ANISOTROPIC_SCALING_ONLY",
    "FM_INFO_ARB_XFORMS",
    "FM_INFO_CONSTANT_WIDTH",
    "FM_INFO_DBCS_FIXED_PITCH",
    "FM_INFO_DO_NOT_ENUMERATE",
    "FM_INFO_DSIG",
    "FM_INFO_FAMILY_EQUIV",
    "FM_INFO_IGNORE_TC_RA_ABLE",
    "FM_INFO_INTEGER_WIDTH",
    "FM_INFO_INTEGRAL_SCALING",
    "FM_INFO_ISOTROPIC_SCALING_ONLY",
    "FM_INFO_NONNEGATIVE_AC",
    "FM_INFO_NOT_CONTIGUOUS",
    "FM_INFO_OPTICALLY_FIXED_PITCH",
    "FM_INFO_RETURNS_BITMAPS",
    "FM_INFO_RETURNS_OUTLINES",
    "FM_INFO_RETURNS_STROKES",
    "FM_INFO_RIGHT_HANDED",
    "FM_INFO_TECH_BITMAP",
    "FM_INFO_TECH_CFF",
    "FM_INFO_TECH_MM",
    "FM_INFO_TECH_OUTLINE_NOT_TRUETYPE",
    "FM_INFO_TECH_STROKE",
    "FM_INFO_TECH_TRUETYPE",
    "FM_INFO_TECH_TYPE1",
    "FM_NO_EMBEDDING",
    "FM_PANOSE_CULTURE_LATIN",
    "FM_READONLY_EMBED",
    "FM_SEL_BOLD",
    "FM_SEL_ITALIC",
    "FM_SEL_NEGATIVE",
    "FM_SEL_OUTLINED",
    "FM_SEL_REGULAR",
    "FM_SEL_STRIKEOUT",
    "FM_SEL_UNDERSCORE",
    "FM_TYPE_LICENSED",
    "FM_VERSION_NUMBER",
    "FONTDIFF",
    "FONTINFO",
    "FONTOBJ",
    "FONTOBJ_cGetAllGlyphHandles",
    "FONTOBJ_cGetGlyphs",
    "FONTOBJ_pQueryGlyphAttrs",
    "FONTOBJ_pfdg",
    "FONTOBJ_pifi",
    "FONTOBJ_pvTrueTypeFontFile",
    "FONTOBJ_pxoGetXform",
    "FONTOBJ_vGetInfo",
    "FONTSIM",
    "FONT_IMAGE_INFO",
    "FO_ATTR_MODE_ROTATE",
    "FO_CFF",
    "FO_CLEARTYPENATURAL_X",
    "FO_CLEARTYPE_X",
    "FO_CLEARTYPE_Y",
    "FO_DBCS_FONT",
    "FO_DEVICE_FONT",
    "FO_EM_HEIGHT",
    "FO_GLYPHBITS",
    "FO_GRAY16",
    "FO_HGLYPHS",
    "FO_MULTIPLEMASTER",
    "FO_NOCLEARTYPE",
    "FO_NOGRAY16",
    "FO_NOHINTS",
    "FO_NO_CHOICE",
    "FO_OUTLINE_CAPABLE",
    "FO_PATHOBJ",
    "FO_POSTSCRIPT",
    "FO_SIM_BOLD",
    "FO_SIM_ITALIC",
    "FO_VERT_FACE",
    "FP_ALTERNATEMODE",
    "FP_WINDINGMODE",
    "FREEOBJPROC",
    "FSCNTL_SCREEN_INFO",
    "FSVIDEO_COPY_FRAME_BUFFER",
    "FSVIDEO_CURSOR_POSITION",
    "FSVIDEO_MODE_INFORMATION",
    "FSVIDEO_REVERSE_MOUSE_POINTER",
    "FSVIDEO_SCREEN_INFORMATION",
    "FSVIDEO_WRITE_TO_FRAME_BUFFER",
    "GAMMARAMP",
    "GAMMA_RAMP_DXGI_1",
    "GAMMA_RAMP_RGB",
    "GAMMA_RAMP_RGB256x3x16",
    "GCAPS2_ACC_DRIVER",
    "GCAPS2_ALPHACURSOR",
    "GCAPS2_BITMAPEXREUSE",
    "GCAPS2_CHANGEGAMMARAMP",
    "GCAPS2_CLEARTYPE",
    "GCAPS2_EXCLUDELAYERED",
    "GCAPS2_ICD_MULTIMON",
    "GCAPS2_INCLUDEAPIBITMAPS",
    "GCAPS2_JPEGSRC",
    "GCAPS2_MOUSETRAILS",
    "GCAPS2_PNGSRC",
    "GCAPS2_REMOTEDRIVER",
    "GCAPS2_RESERVED1",
    "GCAPS2_SHOWHIDDENPOINTER",
    "GCAPS2_SYNCFLUSH",
    "GCAPS2_SYNCTIMER",
    "GCAPS2_xxxx",
    "GCAPS_ALTERNATEFILL",
    "GCAPS_ARBRUSHOPAQUE",
    "GCAPS_ARBRUSHTEXT",
    "GCAPS_ASYNCCHANGE",
    "GCAPS_ASYNCMOVE",
    "GCAPS_BEZIERS",
    "GCAPS_CMYKCOLOR",
    "GCAPS_COLOR_DITHER",
    "GCAPS_DIRECTDRAW",
    "GCAPS_DITHERONREALIZE",
    "GCAPS_DONTJOURNAL",
    "GCAPS_FONT_RASTERIZER",
    "GCAPS_FORCEDITHER",
    "GCAPS_GEOMETRICWIDE",
    "GCAPS_GRAY16",
    "GCAPS_HALFTONE",
    "GCAPS_HIGHRESTEXT",
    "GCAPS_HORIZSTRIKE",
    "GCAPS_ICM",
    "GCAPS_LAYERED",
    "GCAPS_MONO_DITHER",
    "GCAPS_NO64BITMEMACCESS",
    "GCAPS_NUP",
    "GCAPS_OPAQUERECT",
    "GCAPS_PALMANAGED",
    "GCAPS_PANNING",
    "GCAPS_SCREENPRECISION",
    "GCAPS_VECTORFONT",
    "GCAPS_VERTSTRIKE",
    "GCAPS_WINDINGFILL",
    "GDIINFO",
    "GDI_DRIVER_VERSION",
    "GETCONNECTEDIDS_SOURCE",
    "GETCONNECTEDIDS_TARGET",
    "GLYPHBITS",
    "GLYPHDATA",
    "GLYPHDEF",
    "GLYPHPOS",
    "GS_16BIT_HANDLES",
    "GS_8BIT_HANDLES",
    "GS_UNICODE_HANDLES",
    "GUID_DEVINTERFACE_DISPLAY_ADAPTER",
    "GUID_DEVINTERFACE_MONITOR",
    "GUID_DEVINTERFACE_VIDEO_OUTPUT_ARRIVAL",
    "GUID_DISPLAY_DEVICE_ARRIVAL",
    "GUID_MONITOR_OVERRIDE_PSEUDO_SPECIALIZED",
    "GX_GENERAL",
    "GX_IDENTITY",
    "GX_OFFSET",
    "GX_SCALE",
    "GetAutoRotationState",
    "GetCapabilitiesStringLength",
    "GetDisplayAutoRotationPreferences",
    "GetDisplayConfigBufferSizes",
    "GetMonitorBrightness",
    "GetMonitorCapabilities",
    "GetMonitorColorTemperature",
    "GetMonitorContrast",
    "GetMonitorDisplayAreaPosition",
    "GetMonitorDisplayAreaSize",
    "GetMonitorRedGreenOrBlueDrive",
    "GetMonitorRedGreenOrBlueGain",
    "GetMonitorTechnologyType",
    "GetNumberOfPhysicalMonitorsFromHMONITOR",
    "GetNumberOfPhysicalMonitorsFromIDirect3DDevice9",
    "GetPhysicalMonitorsFromHMONITOR",
    "GetPhysicalMonitorsFromIDirect3DDevice9",
    "GetTimingReport",
    "GetVCPFeatureAndVCPFeatureReply",
    "HBM",
    "HDEV",
    "HDRVOBJ",
    "HFASTMUTEX",
    "HOOK_ALPHABLEND",
    "HOOK_BITBLT",
    "HOOK_COPYBITS",
    "HOOK_FILLPATH",
    "HOOK_FLAGS",
    "HOOK_GRADIENTFILL",
    "HOOK_LINETO",
    "HOOK_MOVEPANNING",
    "HOOK_PAINT",
    "HOOK_PLGBLT",
    "HOOK_STRETCHBLT",
    "HOOK_STRETCHBLTROP",
    "HOOK_STROKEANDFILLPATH",
    "HOOK_STROKEPATH",
    "HOOK_SYNCHRONIZE",
    "HOOK_SYNCHRONIZEACCESS",
    "HOOK_TEXTOUT",
    "HOOK_TRANSPARENTBLT",
    "HOST_DSI_BAD_TRANSMISSION_MODE",
    "HOST_DSI_DEVICE_NOT_READY",
    "HOST_DSI_DEVICE_RESET",
    "HOST_DSI_DRIVER_REJECTED_PACKET",
    "HOST_DSI_INTERFACE_RESET",
    "HOST_DSI_INVALID_TRANSMISSION",
    "HOST_DSI_OS_REJECTED_PACKET",
    "HOST_DSI_TRANSMISSION_CANCELLED",
    "HOST_DSI_TRANSMISSION_DROPPED",
    "HOST_DSI_TRANSMISSION_TIMEOUT",
    "HSEMAPHORE",
    "HSURF",
    "HS_DDI_MAX",
    "HT_FLAG_8BPP_CMY332_MASK",
    "HT_FLAG_ADDITIVE_PRIMS",
    "HT_FLAG_DO_DEVCLR_XFORM",
    "HT_FLAG_HAS_BLACK_DYE",
    "HT_FLAG_INK_ABSORPTION_IDX0",
    "HT_FLAG_INK_ABSORPTION_IDX1",
    "HT_FLAG_INK_ABSORPTION_IDX2",
    "HT_FLAG_INK_ABSORPTION_IDX3",
    "HT_FLAG_INK_ABSORPTION_INDICES",
    "HT_FLAG_INK_HIGH_ABSORPTION",
    "HT_FLAG_INVERT_8BPP_BITMASK_IDX",
    "HT_FLAG_LOWER_INK_ABSORPTION",
    "HT_FLAG_LOWEST_INK_ABSORPTION",
    "HT_FLAG_LOW_INK_ABSORPTION",
    "HT_FLAG_NORMAL_INK_ABSORPTION",
    "HT_FLAG_OUTPUT_CMY",
    "HT_FLAG_PRINT_DRAFT_MODE",
    "HT_FLAG_SQUARE_DEVICE_PEL",
    "HT_FLAG_USE_8BPP_BITMASK",
    "HT_FORMAT_16BPP",
    "HT_FORMAT_1BPP",
    "HT_FORMAT_24BPP",
    "HT_FORMAT_32BPP",
    "HT_FORMAT_4BPP",
    "HT_FORMAT_4BPP_IRGB",
    "HT_FORMAT_8BPP",
    "HT_Get8BPPFormatPalette",
    "HT_Get8BPPMaskPalette",
    "HT_PATSIZE_10x10",
    "HT_PATSIZE_10x10_M",
    "HT_PATSIZE_12x12",
    "HT_PATSIZE_12x12_M",
    "HT_PATSIZE_14x14",
    "HT_PATSIZE_14x14_M",
    "HT_PATSIZE_16x16",
    "HT_PATSIZE_16x16_M",
    "HT_PATSIZE_2x2",
    "HT_PATSIZE_2x2_M",
    "HT_PATSIZE_4x4",
    "HT_PATSIZE_4x4_M",
    "HT_PATSIZE_6x6",
    "HT_PATSIZE_6x6_M",
    "HT_PATSIZE_8x8",
    "HT_PATSIZE_8x8_M",
    "HT_PATSIZE_DEFAULT",
    "HT_PATSIZE_MAX_INDEX",
    "HT_PATSIZE_SUPERCELL",
    "HT_PATSIZE_SUPERCELL_M",
    "HT_PATSIZE_USER",
    "HT_USERPAT_CX_MAX",
    "HT_USERPAT_CX_MIN",
    "HT_USERPAT_CY_MAX",
    "HT_USERPAT_CY_MIN",
    "ICloneViewHelper",
    "IFIEXTRA",
    "IFIMETRICS",
    "IGRF_RGB_256BYTES",
    "IGRF_RGB_256WORDS",
    "INDEX_DrvAccumulateD3DDirtyRect",
    "INDEX_DrvAlphaBlend",
    "INDEX_DrvAssertMode",
    "INDEX_DrvAssociateSharedSurface",
    "INDEX_DrvBitBlt",
    "INDEX_DrvCompletePDEV",
    "INDEX_DrvCopyBits",
    "INDEX_DrvCreateDeviceBitmap",
    "INDEX_DrvCreateDeviceBitmapEx",
    "INDEX_DrvDeleteDeviceBitmap",
    "INDEX_DrvDeleteDeviceBitmapEx",
    "INDEX_DrvDeriveSurface",
    "INDEX_DrvDescribePixelFormat",
    "INDEX_DrvDestroyFont",
    "INDEX_DrvDisableDirectDraw",
    "INDEX_DrvDisableDriver",
    "INDEX_DrvDisablePDEV",
    "INDEX_DrvDisableSurface",
    "INDEX_DrvDitherColor",
    "INDEX_DrvDrawEscape",
    "INDEX_DrvEnableDirectDraw",
    "INDEX_DrvEnablePDEV",
    "INDEX_DrvEnableSurface",
    "INDEX_DrvEndDoc",
    "INDEX_DrvEndDxInterop",
    "INDEX_DrvEscape",
    "INDEX_DrvFillPath",
    "INDEX_DrvFontManagement",
    "INDEX_DrvFree",
    "INDEX_DrvGetDirectDrawInfo",
    "INDEX_DrvGetGlyphMode",
    "INDEX_DrvGetModes",
    "INDEX_DrvGetSynthesizedFontFiles",
    "INDEX_DrvGetTrueTypeFile",
    "INDEX_DrvGradientFill",
    "INDEX_DrvIcmCheckBitmapBits",
    "INDEX_DrvIcmCreateColorTransform",
    "INDEX_DrvIcmDeleteColorTransform",
    "INDEX_DrvIcmSetDeviceGammaRamp",
    "INDEX_DrvLineTo",
    "INDEX_DrvLoadFontFile",
    "INDEX_DrvLockDisplayArea",
    "INDEX_DrvMovePanning",
    "INDEX_DrvMovePointer",
    "INDEX_DrvNextBand",
    "INDEX_DrvNotify",
    "INDEX_DrvOffset",
    "INDEX_DrvPaint",
    "INDEX_DrvPlgBlt",
    "INDEX_DrvQueryAdvanceWidths",
    "INDEX_DrvQueryDeviceSupport",
    "INDEX_DrvQueryFont",
    "INDEX_DrvQueryFontCaps",
    "INDEX_DrvQueryFontData",
    "INDEX_DrvQueryFontFile",
    "INDEX_DrvQueryFontTree",
    "INDEX_DrvQueryGlyphAttrs",
    "INDEX_DrvQueryPerBandInfo",
    "INDEX_DrvQuerySpoolType",
    "INDEX_DrvQueryTrueTypeOutline",
    "INDEX_DrvQueryTrueTypeTable",
    "INDEX_DrvRealizeBrush",
    "INDEX_DrvRenderHint",
    "INDEX_DrvReserved1",
    "INDEX_DrvReserved10",
    "INDEX_DrvReserved11",
    "INDEX_DrvReserved2",
    "INDEX_DrvReserved3",
    "INDEX_DrvReserved4",
    "INDEX_DrvReserved5",
    "INDEX_DrvReserved6",
    "INDEX_DrvReserved7",
    "INDEX_DrvReserved8",
    "INDEX_DrvReserved9",
    "INDEX_DrvResetDevice",
    "INDEX_DrvResetPDEV",
    "INDEX_DrvSaveScreenBits",
    "INDEX_DrvSendPage",
    "INDEX_DrvSetPalette",
    "INDEX_DrvSetPixelFormat",
    "INDEX_DrvSetPointerShape",
    "INDEX_DrvStartBanding",
    "INDEX_DrvStartDoc",
    "INDEX_DrvStartDxInterop",
    "INDEX_DrvStartPage",
    "INDEX_DrvStretchBlt",
    "INDEX_DrvStretchBltROP",
    "INDEX_DrvStrokeAndFillPath",
    "INDEX_DrvStrokePath",
    "INDEX_DrvSurfaceComplete",
    "INDEX_DrvSwapBuffers",
    "INDEX_DrvSynchronize",
    "INDEX_DrvSynchronizeRedirectionBitmaps",
    "INDEX_DrvSynchronizeSurface",
    "INDEX_DrvSynthesizeFont",
    "INDEX_DrvTextOut",
    "INDEX_DrvTransparentBlt",
    "INDEX_DrvUnloadFontFile",
    "INDEX_DrvUnlockDisplayArea",
    "INDEX_LAST",
    "INDIRECT_DISPLAY_INFO",
    "INDIRECT_DISPLAY_INFO_FLAGS_CREATED_IDDCX_ADAPTER",
    "IOCTL_COLORSPACE_TRANSFORM_QUERY_TARGET_CAPS",
    "IOCTL_COLORSPACE_TRANSFORM_SET",
    "IOCTL_FSVIDEO_COPY_FRAME_BUFFER",
    "IOCTL_FSVIDEO_REVERSE_MOUSE_POINTER",
    "IOCTL_FSVIDEO_SET_CURRENT_MODE",
    "IOCTL_FSVIDEO_SET_CURSOR_POSITION",
    "IOCTL_FSVIDEO_SET_SCREEN_INFORMATION",
    "IOCTL_FSVIDEO_WRITE_TO_FRAME_BUFFER",
    "IOCTL_MIPI_DSI_QUERY_CAPS",
    "IOCTL_MIPI_DSI_RESET",
    "IOCTL_MIPI_DSI_TRANSMISSION",
    "IOCTL_PANEL_GET_BACKLIGHT_REDUCTION",
    "IOCTL_PANEL_GET_BRIGHTNESS",
    "IOCTL_PANEL_QUERY_BRIGHTNESS_CAPS",
    "IOCTL_PANEL_QUERY_BRIGHTNESS_RANGES",
    "IOCTL_PANEL_SET_BACKLIGHT_OPTIMIZATION",
    "IOCTL_PANEL_SET_BRIGHTNESS",
    "IOCTL_PANEL_SET_BRIGHTNESS_STATE",
    "IOCTL_SET_ACTIVE_COLOR_PROFILE_NAME",
    "IOCTL_VIDEO_DISABLE_CURSOR",
    "IOCTL_VIDEO_DISABLE_POINTER",
    "IOCTL_VIDEO_DISABLE_VDM",
    "IOCTL_VIDEO_ENABLE_CURSOR",
    "IOCTL_VIDEO_ENABLE_POINTER",
    "IOCTL_VIDEO_ENABLE_VDM",
    "IOCTL_VIDEO_ENUM_MONITOR_PDO",
    "IOCTL_VIDEO_FREE_PUBLIC_ACCESS_RANGES",
    "IOCTL_VIDEO_GET_BANK_SELECT_CODE",
    "IOCTL_VIDEO_GET_CHILD_STATE",
    "IOCTL_VIDEO_GET_OUTPUT_DEVICE_POWER_STATE",
    "IOCTL_VIDEO_GET_POWER_MANAGEMENT",
    "IOCTL_VIDEO_HANDLE_VIDEOPARAMETERS",
    "IOCTL_VIDEO_INIT_WIN32K_CALLBACKS",
    "IOCTL_VIDEO_IS_VGA_DEVICE",
    "IOCTL_VIDEO_LOAD_AND_SET_FONT",
    "IOCTL_VIDEO_MAP_VIDEO_MEMORY",
    "IOCTL_VIDEO_MONITOR_DEVICE",
    "IOCTL_VIDEO_PREPARE_FOR_EARECOVERY",
    "IOCTL_VIDEO_QUERY_AVAIL_MODES",
    "IOCTL_VIDEO_QUERY_COLOR_CAPABILITIES",
    "IOCTL_VIDEO_QUERY_CURRENT_MODE",
    "IOCTL_VIDEO_QUERY_CURSOR_ATTR",
    "IOCTL_VIDEO_QUERY_CURSOR_POSITION",
    "IOCTL_VIDEO_QUERY_DISPLAY_BRIGHTNESS",
    "IOCTL_VIDEO_QUERY_NUM_AVAIL_MODES",
    "IOCTL_VIDEO_QUERY_POINTER_ATTR",
    "IOCTL_VIDEO_QUERY_POINTER_CAPABILITIES",
    "IOCTL_VIDEO_QUERY_POINTER_POSITION",
    "IOCTL_VIDEO_QUERY_PUBLIC_ACCESS_RANGES",
    "IOCTL_VIDEO_QUERY_SUPPORTED_BRIGHTNESS",
    "IOCTL_VIDEO_REGISTER_VDM",
    "IOCTL_VIDEO_RESET_DEVICE",
    "IOCTL_VIDEO_RESTORE_HARDWARE_STATE",
    "IOCTL_VIDEO_SAVE_HARDWARE_STATE",
    "IOCTL_VIDEO_SET_BANK_POSITION",
    "IOCTL_VIDEO_SET_CHILD_STATE_CONFIGURATION",
    "IOCTL_VIDEO_SET_COLOR_LUT_DATA",
    "IOCTL_VIDEO_SET_COLOR_REGISTERS",
    "IOCTL_VIDEO_SET_CURRENT_MODE",
    "IOCTL_VIDEO_SET_CURSOR_ATTR",
    "IOCTL_VIDEO_SET_CURSOR_POSITION",
    "IOCTL_VIDEO_SET_DISPLAY_BRIGHTNESS",
    "IOCTL_VIDEO_SET_OUTPUT_DEVICE_POWER_STATE",
    "IOCTL_VIDEO_SET_PALETTE_REGISTERS",
    "IOCTL_VIDEO_SET_POINTER_ATTR",
    "IOCTL_VIDEO_SET_POINTER_POSITION",
    "IOCTL_VIDEO_SET_POWER_MANAGEMENT",
    "IOCTL_VIDEO_SHARE_VIDEO_MEMORY",
    "IOCTL_VIDEO_SWITCH_DUALVIEW",
    "IOCTL_VIDEO_UNMAP_VIDEO_MEMORY",
    "IOCTL_VIDEO_UNSHARE_VIDEO_MEMORY",
    "IOCTL_VIDEO_USE_DEVICE_IN_SESSION",
    "IOCTL_VIDEO_VALIDATE_CHILD_STATE_CONFIGURATION",
    "IViewHelper",
    "JOIN_BEVEL",
    "JOIN_MITER",
    "JOIN_ROUND",
    "LA_ALTERNATE",
    "LA_GEOMETRIC",
    "LA_STARTGAP",
    "LA_STYLED",
    "LIGATURE",
    "LINEATTRS",
    "MAXCHARSETS",
    "MAX_PACKET_COUNT",
    "MC_APERTURE_GRILL_CATHODE_RAY_TUBE",
    "MC_BLUE_DRIVE",
    "MC_BLUE_GAIN",
    "MC_CAPS_BRIGHTNESS",
    "MC_CAPS_COLOR_TEMPERATURE",
    "MC_CAPS_CONTRAST",
    "MC_CAPS_DEGAUSS",
    "MC_CAPS_DISPLAY_AREA_POSITION",
    "MC_CAPS_DISPLAY_AREA_SIZE",
    "MC_CAPS_MONITOR_TECHNOLOGY_TYPE",
    "MC_CAPS_NONE",
    "MC_CAPS_RED_GREEN_BLUE_DRIVE",
    "MC_CAPS_RED_GREEN_BLUE_GAIN",
    "MC_CAPS_RESTORE_FACTORY_COLOR_DEFAULTS",
    "MC_CAPS_RESTORE_FACTORY_DEFAULTS",
    "MC_COLOR_TEMPERATURE",
    "MC_COLOR_TEMPERATURE_10000K",
    "MC_COLOR_TEMPERATURE_11500K",
    "MC_COLOR_TEMPERATURE_4000K",
    "MC_COLOR_TEMPERATURE_5000K",
    "MC_COLOR_TEMPERATURE_6500K",
    "MC_COLOR_TEMPERATURE_7500K",
    "MC_COLOR_TEMPERATURE_8200K",
    "MC_COLOR_TEMPERATURE_9300K",
    "MC_COLOR_TEMPERATURE_UNKNOWN",
    "MC_DISPLAY_TECHNOLOGY_TYPE",
    "MC_DRIVE_TYPE",
    "MC_ELECTROLUMINESCENT",
    "MC_FIELD_EMISSION_DEVICE",
    "MC_GAIN_TYPE",
    "MC_GREEN_DRIVE",
    "MC_GREEN_GAIN",
    "MC_HEIGHT",
    "MC_HORIZONTAL_POSITION",
    "MC_LIQUID_CRYSTAL_ON_SILICON",
    "MC_MICROELECTROMECHANICAL",
    "MC_MOMENTARY",
    "MC_ORGANIC_LIGHT_EMITTING_DIODE",
    "MC_PLASMA",
    "MC_POSITION_TYPE",
    "MC_RED_DRIVE",
    "MC_RED_GAIN",
    "MC_RESTORE_FACTORY_DEFAULTS_ENABLES_MONITOR_SETTINGS",
    "MC_SET_PARAMETER",
    "MC_SHADOW_MASK_CATHODE_RAY_TUBE",
    "MC_SIZE_TYPE",
    "MC_SUPPORTED_COLOR_TEMPERATURE_10000K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_11500K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_4000K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_5000K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_6500K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_7500K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_8200K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_9300K",
    "MC_SUPPORTED_COLOR_TEMPERATURE_NONE",
    "MC_THIN_FILM_TRANSISTOR",
    "MC_TIMING_REPORT",
    "MC_VCP_CODE_TYPE",
    "MC_VERTICAL_POSITION",
    "MC_WIDTH",
    "MIPI_DSI_CAPS",
    "MIPI_DSI_PACKET",
    "MIPI_DSI_RESET",
    "MIPI_DSI_TRANSMISSION",
    "MS_CDDDEVICEBITMAP",
    "MS_NOTSYSTEMMEMORY",
    "MS_REUSEDDEVICEBITMAP",
    "MS_SHAREDACCESS",
    "OC_BANK_CLIP",
    "OPENGL_CMD",
    "OPENGL_GETINFO",
    "ORIENTATION_PREFERENCE",
    "ORIENTATION_PREFERENCE_LANDSCAPE",
    "ORIENTATION_PREFERENCE_LANDSCAPE_FLIPPED",
    "ORIENTATION_PREFERENCE_NONE",
    "ORIENTATION_PREFERENCE_PORTRAIT",
    "ORIENTATION_PREFERENCE_PORTRAIT_FLIPPED",
    "OUTPUT_COLOR_ENCODING",
    "OUTPUT_COLOR_ENCODING_FORCE_UINT32",
    "OUTPUT_COLOR_ENCODING_INTENSITY",
    "OUTPUT_COLOR_ENCODING_RGB",
    "OUTPUT_COLOR_ENCODING_YCBCR420",
    "OUTPUT_COLOR_ENCODING_YCBCR422",
    "OUTPUT_COLOR_ENCODING_YCBCR444",
    "OUTPUT_WIRE_COLOR_SPACE_G2084_P2020",
    "OUTPUT_WIRE_COLOR_SPACE_G2084_P2020_DVLL",
    "OUTPUT_WIRE_COLOR_SPACE_G2084_P2020_HDR10PLUS",
    "OUTPUT_WIRE_COLOR_SPACE_G22_P2020",
    "OUTPUT_WIRE_COLOR_SPACE_G22_P709",
    "OUTPUT_WIRE_COLOR_SPACE_G22_P709_WCG",
    "OUTPUT_WIRE_COLOR_SPACE_RESERVED",
    "OUTPUT_WIRE_COLOR_SPACE_TYPE",
    "OUTPUT_WIRE_FORMAT",
    "PALOBJ",
    "PAL_BGR",
    "PAL_BITFIELDS",
    "PAL_CMYK",
    "PAL_INDEXED",
    "PAL_RGB",
    "PANEL_BRIGHTNESS_SENSOR_DATA",
    "PANEL_GET_BACKLIGHT_REDUCTION",
    "PANEL_GET_BRIGHTNESS",
    "PANEL_QUERY_BRIGHTNESS_CAPS",
    "PANEL_QUERY_BRIGHTNESS_RANGES",
    "PANEL_SET_BACKLIGHT_OPTIMIZATION",
    "PANEL_SET_BRIGHTNESS",
    "PANEL_SET_BRIGHTNESS_STATE",
    "PATHDATA",
    "PATHOBJ",
    "PATHOBJ_bEnum",
    "PATHOBJ_bEnumClipLines",
    "PATHOBJ_vEnumStart",
    "PATHOBJ_vEnumStartClipLines",
    "PATHOBJ_vGetBounds",
    "PD_BEGINSUBPATH",
    "PD_BEZIERS",
    "PD_CLOSEFIGURE",
    "PD_ENDSUBPATH",
    "PD_RESETSTYLE",
    "PERBANDINFO",
    "PFN",
    "PFN_DrvAccumulateD3DDirtyRect",
    "PFN_DrvAlphaBlend",
    "PFN_DrvAssertMode",
    "PFN_DrvAssociateSharedSurface",
    "PFN_DrvBitBlt",
    "PFN_DrvCompletePDEV",
    "PFN_DrvCopyBits",
    "PFN_DrvCreateDeviceBitmap",
    "PFN_DrvCreateDeviceBitmapEx",
    "PFN_DrvDeleteDeviceBitmap",
    "PFN_DrvDeleteDeviceBitmapEx",
    "PFN_DrvDeriveSurface",
    "PFN_DrvDescribePixelFormat",
    "PFN_DrvDestroyFont",
    "PFN_DrvDisableDirectDraw",
    "PFN_DrvDisableDriver",
    "PFN_DrvDisablePDEV",
    "PFN_DrvDisableSurface",
    "PFN_DrvDitherColor",
    "PFN_DrvDrawEscape",
    "PFN_DrvEnableDirectDraw",
    "PFN_DrvEnableDriver",
    "PFN_DrvEnablePDEV",
    "PFN_DrvEnableSurface",
    "PFN_DrvEndDoc",
    "PFN_DrvEndDxInterop",
    "PFN_DrvEscape",
    "PFN_DrvFillPath",
    "PFN_DrvFontManagement",
    "PFN_DrvFree",
    "PFN_DrvGetDirectDrawInfo",
    "PFN_DrvGetGlyphMode",
    "PFN_DrvGetModes",
    "PFN_DrvGetTrueTypeFile",
    "PFN_DrvGradientFill",
    "PFN_DrvIcmCheckBitmapBits",
    "PFN_DrvIcmCreateColorTransform",
    "PFN_DrvIcmDeleteColorTransform",
    "PFN_DrvIcmSetDeviceGammaRamp",
    "PFN_DrvLineTo",
    "PFN_DrvLoadFontFile",
    "PFN_DrvLockDisplayArea",
    "PFN_DrvMovePointer",
    "PFN_DrvNextBand",
    "PFN_DrvNotify",
    "PFN_DrvPaint",
    "PFN_DrvPlgBlt",
    "PFN_DrvQueryAdvanceWidths",
    "PFN_DrvQueryDeviceSupport",
    "PFN_DrvQueryFont",
    "PFN_DrvQueryFontCaps",
    "PFN_DrvQueryFontData",
    "PFN_DrvQueryFontFile",
    "PFN_DrvQueryFontTree",
    "PFN_DrvQueryGlyphAttrs",
    "PFN_DrvQueryPerBandInfo",
    "PFN_DrvQuerySpoolType",
    "PFN_DrvQueryTrueTypeOutline",
    "PFN_DrvQueryTrueTypeSection",
    "PFN_DrvQueryTrueTypeTable",
    "PFN_DrvRealizeBrush",
    "PFN_DrvRenderHint",
    "PFN_DrvResetDevice",
    "PFN_DrvResetPDEV",
    "PFN_DrvSaveScreenBits",
    "PFN_DrvSendPage",
    "PFN_DrvSetPalette",
    "PFN_DrvSetPixelFormat",
    "PFN_DrvSetPointerShape",
    "PFN_DrvStartBanding",
    "PFN_DrvStartDoc",
    "PFN_DrvStartDxInterop",
    "PFN_DrvStartPage",
    "PFN_DrvStretchBlt",
    "PFN_DrvStretchBltROP",
    "PFN_DrvStrokeAndFillPath",
    "PFN_DrvStrokePath",
    "PFN_DrvSurfaceComplete",
    "PFN_DrvSwapBuffers",
    "PFN_DrvSynchronize",
    "PFN_DrvSynchronizeRedirectionBitmaps",
    "PFN_DrvSynchronizeSurface",
    "PFN_DrvTextOut",
    "PFN_DrvTransparentBlt",
    "PFN_DrvUnloadFontFile",
    "PFN_DrvUnlockDisplayArea",
    "PFN_EngCombineRgn",
    "PFN_EngCopyRgn",
    "PFN_EngCreateRectRgn",
    "PFN_EngDeleteRgn",
    "PFN_EngIntersectRgn",
    "PFN_EngSubtractRgn",
    "PFN_EngUnionRgn",
    "PFN_EngXorRgn",
    "PHYSICAL_MONITOR",
    "PHYSICAL_MONITOR_DESCRIPTION_SIZE",
    "PLANAR_HC",
    "POINTE",
    "POINTFIX",
    "POINTQF",
    "PO_ALL_INTEGERS",
    "PO_BEZIERS",
    "PO_ELLIPSE",
    "PO_ENUM_AS_INTEGERS",
    "PO_WIDENED",
    "PPC_BGR_ORDER_HORIZONTAL_STRIPES",
    "PPC_BGR_ORDER_VERTICAL_STRIPES",
    "PPC_DEFAULT",
    "PPC_RGB_ORDER_HORIZONTAL_STRIPES",
    "PPC_RGB_ORDER_VERTICAL_STRIPES",
    "PPC_UNDEFINED",
    "PPG_DEFAULT",
    "PPG_SRGB",
    "PRIMARY_ORDER_ABC",
    "PRIMARY_ORDER_ACB",
    "PRIMARY_ORDER_BAC",
    "PRIMARY_ORDER_BCA",
    "PRIMARY_ORDER_CAB",
    "PRIMARY_ORDER_CBA",
    "PVIDEO_WIN32K_CALLOUT",
    "QAW_GETEASYWIDTHS",
    "QAW_GETWIDTHS",
    "QC_1BIT",
    "QC_4BIT",
    "QC_OUTLINES",
    "QDA_ACCELERATION_LEVEL",
    "QDA_RESERVED",
    "QDS_CHECKJPEGFORMAT",
    "QDS_CHECKPNGFORMAT",
    "QFD_GLYPHANDBITMAP",
    "QFD_GLYPHANDOUTLINE",
    "QFD_MAXEXTENTS",
    "QFD_TT_GLYPHANDBITMAP",
    "QFD_TT_GRAY1_BITMAP",
    "QFD_TT_GRAY2_BITMAP",
    "QFD_TT_GRAY4_BITMAP",
    "QFD_TT_GRAY8_BITMAP",
    "QFD_TT_MONO_BITMAP",
    "QFF_DESCRIPTION",
    "QFF_NUMFACES",
    "QFT_GLYPHSET",
    "QFT_KERNPAIRS",
    "QFT_LIGATURES",
    "QSA_3DNOW",
    "QSA_MMX",
    "QSA_SSE",
    "QSA_SSE1",
    "QSA_SSE2",
    "QSA_SSE3",
    "QueryDisplayConfig",
    "RB_DITHERCOLOR",
    "RECTFX",
    "RUN",
    "RestoreMonitorFactoryColorDefaults",
    "RestoreMonitorFactoryDefaults",
    "SETCONFIGURATION_STATUS_ADDITIONAL",
    "SETCONFIGURATION_STATUS_APPLIED",
    "SETCONFIGURATION_STATUS_OVERRIDDEN",
    "SET_ACTIVE_COLOR_PROFILE_NAME",
    "SGI_EXTRASPACE",
    "SORTCOMP",
    "SO_BREAK_EXTRA",
    "SO_CHARACTER_EXTRA",
    "SO_CHAR_INC_EQUAL_BM_BASE",
    "SO_DO_NOT_SUBSTITUTE_DEVICE_FONT",
    "SO_DXDY",
    "SO_ESC_NOT_ORIENT",
    "SO_FLAG_DEFAULT_PLACEMENT",
    "SO_GLYPHINDEX_TEXTOUT",
    "SO_HORIZONTAL",
    "SO_MAXEXT_EQUAL_BM_SIDE",
    "SO_REVERSED",
    "SO_VERTICAL",
    "SO_ZERO_BEARINGS",
    "SPS_ACCEPT_EXCLUDE",
    "SPS_ACCEPT_NOEXCLUDE",
    "SPS_ACCEPT_SYNCHRONOUS",
    "SPS_ALPHA",
    "SPS_ANIMATESTART",
    "SPS_ANIMATEUPDATE",
    "SPS_ASYNCCHANGE",
    "SPS_CHANGE",
    "SPS_DECLINE",
    "SPS_ERROR",
    "SPS_FLAGSMASK",
    "SPS_FREQMASK",
    "SPS_LENGTHMASK",
    "SPS_RESERVED",
    "SPS_RESERVED1",
    "SS_FREE",
    "SS_RESTORE",
    "SS_SAVE",
    "STROBJ",
    "STROBJ_bEnum",
    "STROBJ_bEnumPositionsOnly",
    "STROBJ_bGetAdvanceWidths",
    "STROBJ_dwGetCodePage",
    "STROBJ_vEnumStart",
    "STYPE_BITMAP",
    "STYPE_DEVBITMAP",
    "SURFOBJ",
    "S_INIT",
    "SaveCurrentMonitorSettings",
    "SaveCurrentSettings",
    "SetDisplayAutoRotationPreferences",
    "SetDisplayConfig",
    "SetMonitorBrightness",
    "SetMonitorColorTemperature",
    "SetMonitorContrast",
    "SetMonitorDisplayAreaPosition",
    "SetMonitorDisplayAreaSize",
    "SetMonitorRedGreenOrBlueDrive",
    "SetMonitorRedGreenOrBlueGain",
    "SetVCPFeature",
    "Sources",
    "TC_PATHOBJ",
    "TC_RECTANGLES",
    "TTO_METRICS_ONLY",
    "TTO_QUBICS",
    "TTO_UNHINTED",
    "TYPE1_FONT",
    "VGA_CHAR",
    "VIDEOPARAMETERS",
    "VIDEO_BANK_SELECT",
    "VIDEO_BANK_TYPE",
    "VIDEO_BANK_TYPE_NumVideoBankTypes",
    "VIDEO_BANK_TYPE_VideoBanked1R1W",
    "VIDEO_BANK_TYPE_VideoBanked1RW",
    "VIDEO_BANK_TYPE_VideoBanked2RW",
    "VIDEO_BANK_TYPE_VideoNotBanked",
    "VIDEO_BRIGHTNESS_POLICY",
    "VIDEO_CLUT",
    "VIDEO_CLUTDATA",
    "VIDEO_COLOR_CAPABILITIES",
    "VIDEO_COLOR_LUT_DATA",
    "VIDEO_COLOR_LUT_DATA_FORMAT_PRIVATEFORMAT",
    "VIDEO_COLOR_LUT_DATA_FORMAT_RGB256WORDS",
    "VIDEO_CURSOR_ATTRIBUTES",
    "VIDEO_CURSOR_POSITION",
    "VIDEO_DEVICE_COLOR",
    "VIDEO_DEVICE_NAME",
    "VIDEO_DEVICE_SESSION_STATUS",
    "VIDEO_DUALVIEW_PRIMARY",
    "VIDEO_DUALVIEW_REMOVABLE",
    "VIDEO_DUALVIEW_SECONDARY",
    "VIDEO_DUALVIEW_WDDM_VGA",
    "VIDEO_HARDWARE_STATE",
    "VIDEO_HARDWARE_STATE_HEADER",
    "VIDEO_LOAD_FONT_INFORMATION",
    "VIDEO_LUT_RGB256WORDS",
    "VIDEO_MAX_REASON",
    "VIDEO_MEMORY",
    "VIDEO_MEMORY_INFORMATION",
    "VIDEO_MODE",
    "VIDEO_MODE_ANIMATE_START",
    "VIDEO_MODE_ANIMATE_UPDATE",
    "VIDEO_MODE_ASYNC_POINTER",
    "VIDEO_MODE_BANKED",
    "VIDEO_MODE_COLOR",
    "VIDEO_MODE_COLOR_POINTER",
    "VIDEO_MODE_GRAPHICS",
    "VIDEO_MODE_INFORMATION",
    "VIDEO_MODE_INTERLACED",
    "VIDEO_MODE_LINEAR",
    "VIDEO_MODE_MANAGED_PALETTE",
    "VIDEO_MODE_MAP_MEM_LINEAR",
    "VIDEO_MODE_MONO_POINTER",
    "VIDEO_MODE_NO_64_BIT_ACCESS",
    "VIDEO_MODE_NO_OFF_SCREEN",
    "VIDEO_MODE_NO_ZERO_MEMORY",
    "VIDEO_MODE_PALETTE_DRIVEN",
    "VIDEO_MONITOR_DESCRIPTOR",
    "VIDEO_NUM_MODES",
    "VIDEO_OPTIONAL_GAMMET_TABLE",
    "VIDEO_PALETTE_DATA",
    "VIDEO_PERFORMANCE_COUNTER",
    "VIDEO_POINTER_ATTRIBUTES",
    "VIDEO_POINTER_CAPABILITIES",
    "VIDEO_POINTER_POSITION",
    "VIDEO_POWER_MANAGEMENT",
    "VIDEO_POWER_STATE",
    "VIDEO_POWER_STATE_VideoPowerHibernate",
    "VIDEO_POWER_STATE_VideoPowerMaximum",
    "VIDEO_POWER_STATE_VideoPowerOff",
    "VIDEO_POWER_STATE_VideoPowerOn",
    "VIDEO_POWER_STATE_VideoPowerShutdown",
    "VIDEO_POWER_STATE_VideoPowerStandBy",
    "VIDEO_POWER_STATE_VideoPowerSuspend",
    "VIDEO_POWER_STATE_VideoPowerUnspecified",
    "VIDEO_PUBLIC_ACCESS_RANGES",
    "VIDEO_QUERY_PERFORMANCE_COUNTER",
    "VIDEO_REASON_ALLOCATION",
    "VIDEO_REASON_CONFIGURATION",
    "VIDEO_REASON_FAILED_ROTATION",
    "VIDEO_REASON_LOCK",
    "VIDEO_REASON_NONE",
    "VIDEO_REASON_POLICY1",
    "VIDEO_REASON_POLICY2",
    "VIDEO_REASON_POLICY3",
    "VIDEO_REASON_POLICY4",
    "VIDEO_REASON_SCRATCH",
    "VIDEO_REGISTER_VDM",
    "VIDEO_SHARE_MEMORY",
    "VIDEO_SHARE_MEMORY_INFORMATION",
    "VIDEO_STATE_NON_STANDARD_VGA",
    "VIDEO_STATE_PACKED_CHAIN4_MODE",
    "VIDEO_STATE_UNEMULATED_VGA_STATE",
    "VIDEO_VDM",
    "VIDEO_WIN32K_CALLBACKS",
    "VIDEO_WIN32K_CALLBACKS_PARAMS",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoBlackScreenDiagnostics",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDesktopDuplicationChange",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDisableMultiPlaneOverlay",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkDisplaySwitchCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkFindAdapterTdrCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoDxgkHardwareProtectionTeardown",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoEnumChildPdoNotifyCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoFindAdapterCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoPnpNotifyCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoPowerNotifyCallout",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoRepaintDesktop",
    "VIDEO_WIN32K_CALLBACKS_PARAMS_TYPE_VideoUpdateCursor",
    "WCRUN",
    "WINDDI_MAXSETPALETTECOLORINDEX",
    "WINDDI_MAXSETPALETTECOLORS",
    "WINDDI_MAX_BROADCAST_CONTEXT",
    "WNDOBJ",
    "WNDOBJCHANGEPROC",
    "WNDOBJ_SETUP",
    "WOC_CHANGED",
    "WOC_DELETE",
    "WOC_DRAWN",
    "WOC_RGN_CLIENT",
    "WOC_RGN_CLIENT_DELTA",
    "WOC_RGN_SPRITE",
    "WOC_RGN_SURFACE",
    "WOC_RGN_SURFACE_DELTA",
    "WOC_SPRITE_NO_OVERLAP",
    "WOC_SPRITE_OVERLAP",
    "WO_DRAW_NOTIFY",
    "WO_RGN_CLIENT",
    "WO_RGN_CLIENT_DELTA",
    "WO_RGN_DESKTOP_COORD",
    "WO_RGN_SPRITE",
    "WO_RGN_SURFACE",
    "WO_RGN_SURFACE_DELTA",
    "WO_RGN_UPDATE_ALL",
    "WO_RGN_WINDOW",
    "WO_SPRITE_NOTIFY",
    "WVIDEO_DEVICE_NAME",
    "XFORML",
    "XFORMOBJ",
    "XFORMOBJ_bApplyXform",
    "XFORMOBJ_iGetXform",
    "XF_INV_FXTOL",
    "XF_INV_LTOL",
    "XF_LTOFX",
    "XF_LTOL",
    "XLATEOBJ",
    "XLATEOBJ_cGetPalette",
    "XLATEOBJ_hGetColorTransform",
    "XLATEOBJ_iXlate",
    "XLATEOBJ_piVector",
    "XO_DESTBITFIELDS",
    "XO_DESTDCPALETTE",
    "XO_DESTPALETTE",
    "XO_DEVICE_ICM",
    "XO_FROM_CMYK",
    "XO_HOST_ICM",
    "XO_SRCBITFIELDS",
    "XO_SRCPALETTE",
    "XO_TABLE",
    "XO_TO_MONO",
    "XO_TRIVIAL",
]
