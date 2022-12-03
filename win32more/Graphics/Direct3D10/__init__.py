from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Direct3D
import win32more.Graphics.Direct3D10
import win32more.Graphics.Dxgi
import win32more.Graphics.Dxgi.Common
import win32more.System.Com
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
D3D10_16BIT_INDEX_STRIP_CUT_VALUE = 65535
D3D10_32BIT_INDEX_STRIP_CUT_VALUE = 4294967295
D3D10_8BIT_INDEX_STRIP_CUT_VALUE = 255
D3D10_ARRAY_AXIS_ADDRESS_RANGE_BIT_COUNT = 9
D3D10_CLIP_OR_CULL_DISTANCE_COUNT = 8
D3D10_CLIP_OR_CULL_DISTANCE_ELEMENT_COUNT = 2
D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT = 14
D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENTS = 4
D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_CONSTANT_BUFFER_HW_SLOT_COUNT = 15
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COUNT = 15
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_FLOWCONTROL_NESTING_LIMIT = 64
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COUNT = 1
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_IMMEDIATE_VALUE_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COMPONENTS = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COUNT = 128
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT = 128
D3D10_COMMONSHADER_SAMPLER_REGISTER_COMPONENTS = 1
D3D10_COMMONSHADER_SAMPLER_REGISTER_COUNT = 16
D3D10_COMMONSHADER_SAMPLER_REGISTER_READS_PER_INST = 1
D3D10_COMMONSHADER_SAMPLER_REGISTER_READ_PORTS = 1
D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT = 16
D3D10_COMMONSHADER_SUBROUTINE_NESTING_LIMIT = 32
D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENTS = 4
D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_COMMONSHADER_TEMP_REGISTER_COUNT = 4096
D3D10_COMMONSHADER_TEMP_REGISTER_READS_PER_INST = 3
D3D10_COMMONSHADER_TEMP_REGISTER_READ_PORTS = 3
D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MAX = 10
D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MIN = -10
D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_NEGATIVE = -8
D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_POSITIVE = 7
D3D10_DEFAULT_BLEND_FACTOR_ALPHA = 1
D3D10_DEFAULT_BLEND_FACTOR_BLUE = 1
D3D10_DEFAULT_BLEND_FACTOR_GREEN = 1
D3D10_DEFAULT_BLEND_FACTOR_RED = 1
D3D10_DEFAULT_BORDER_COLOR_COMPONENT = 0
D3D10_DEFAULT_DEPTH_BIAS = 0
D3D10_DEFAULT_DEPTH_BIAS_CLAMP = 0
D3D10_DEFAULT_MAX_ANISOTROPY = 16
D3D10_DEFAULT_MIP_LOD_BIAS = 0
D3D10_DEFAULT_RENDER_TARGET_ARRAY_INDEX = 0
D3D10_DEFAULT_SAMPLE_MASK = 4294967295
D3D10_DEFAULT_SCISSOR_ENDX = 0
D3D10_DEFAULT_SCISSOR_ENDY = 0
D3D10_DEFAULT_SCISSOR_STARTX = 0
D3D10_DEFAULT_SCISSOR_STARTY = 0
D3D10_DEFAULT_SLOPE_SCALED_DEPTH_BIAS = 0
D3D10_DEFAULT_STENCIL_READ_MASK = 255
D3D10_DEFAULT_STENCIL_REFERENCE = 0
D3D10_DEFAULT_STENCIL_WRITE_MASK = 255
D3D10_DEFAULT_VIEWPORT_AND_SCISSORRECT_INDEX = 0
D3D10_DEFAULT_VIEWPORT_HEIGHT = 0
D3D10_DEFAULT_VIEWPORT_MAX_DEPTH = 0
D3D10_DEFAULT_VIEWPORT_MIN_DEPTH = 0
D3D10_DEFAULT_VIEWPORT_TOPLEFTX = 0
D3D10_DEFAULT_VIEWPORT_TOPLEFTY = 0
D3D10_DEFAULT_VIEWPORT_WIDTH = 0
D3D10_FLOAT16_FUSED_TOLERANCE_IN_ULP = 0.6
D3D10_FLOAT32_MAX = 3.4028235e+38
D3D10_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP = 0.6
D3D10_FLOAT_TO_SRGB_EXPONENT_DENOMINATOR = 2.4
D3D10_FLOAT_TO_SRGB_EXPONENT_NUMERATOR = 1
D3D10_FLOAT_TO_SRGB_OFFSET = 0.055
D3D10_FLOAT_TO_SRGB_SCALE_1 = 12.92
D3D10_FLOAT_TO_SRGB_SCALE_2 = 1.055
D3D10_FLOAT_TO_SRGB_THRESHOLD = 0.0031308
D3D10_FTOI_INSTRUCTION_MAX_INPUT = 2147483600.0
D3D10_FTOI_INSTRUCTION_MIN_INPUT = -2147483600.0
D3D10_FTOU_INSTRUCTION_MAX_INPUT = 4294967300.0
D3D10_FTOU_INSTRUCTION_MIN_INPUT = 0
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENTS = 1
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_INPUT_PRIM_CONST_REGISTER_COUNT = 1
D3D10_GS_INPUT_PRIM_CONST_REGISTER_READS_PER_INST = 2
D3D10_GS_INPUT_PRIM_CONST_REGISTER_READ_PORTS = 1
D3D10_GS_INPUT_REGISTER_COMPONENTS = 4
D3D10_GS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_INPUT_REGISTER_COUNT = 16
D3D10_GS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_GS_INPUT_REGISTER_READ_PORTS = 1
D3D10_GS_INPUT_REGISTER_VERTICES = 6
D3D10_GS_OUTPUT_ELEMENTS = 32
D3D10_GS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_GS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_GS_OUTPUT_REGISTER_COUNT = 32
D3D10_IA_DEFAULT_INDEX_BUFFER_OFFSET_IN_BYTES = 0
D3D10_IA_DEFAULT_PRIMITIVE_TOPOLOGY = 0
D3D10_IA_DEFAULT_VERTEX_BUFFER_OFFSET_IN_BYTES = 0
D3D10_IA_INDEX_INPUT_RESOURCE_SLOT_COUNT = 1
D3D10_IA_INSTANCE_ID_BIT_COUNT = 32
D3D10_IA_INTEGER_ARITHMETIC_BIT_COUNT = 32
D3D10_IA_PRIMITIVE_ID_BIT_COUNT = 32
D3D10_IA_VERTEX_ID_BIT_COUNT = 32
D3D10_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT = 16
D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENTS_COMPONENTS = 64
D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENT_COUNT = 16
D3D10_INTEGER_DIVIDE_BY_ZERO_QUOTIENT = 4294967295
D3D10_INTEGER_DIVIDE_BY_ZERO_REMAINDER = 4294967295
D3D10_LINEAR_GAMMA = 1
D3D10_MAX_BORDER_COLOR_COMPONENT = 1
D3D10_MAX_DEPTH = 1
D3D10_MAX_MAXANISOTROPY = 16
D3D10_MAX_MULTISAMPLE_SAMPLE_COUNT = 32
D3D10_MAX_POSITION_VALUE = 3.4028236e+34
D3D10_MAX_TEXTURE_DIMENSION_2_TO_EXP = 17
D3D10_MIN_BORDER_COLOR_COMPONENT = 0
D3D10_MIN_DEPTH = 0
D3D10_MIN_MAXANISOTROPY = 0
D3D10_MIP_LOD_BIAS_MAX = 15.99
D3D10_MIP_LOD_BIAS_MIN = -16
D3D10_MIP_LOD_FRACTIONAL_BIT_COUNT = 6
D3D10_MIP_LOD_RANGE_BIT_COUNT = 8
D3D10_MULTISAMPLE_ANTIALIAS_LINE_WIDTH = 1.4
D3D10_NONSAMPLE_FETCH_OUT_OF_RANGE_ACCESS_RESULT = 0
D3D10_PIXEL_ADDRESS_RANGE_BIT_COUNT = 13
D3D10_PRE_SCISSOR_PIXEL_ADDRESS_RANGE_BIT_COUNT = 15
D3D10_PS_FRONTFACING_DEFAULT_VALUE = 4294967295
D3D10_PS_FRONTFACING_FALSE_VALUE = 0
D3D10_PS_FRONTFACING_TRUE_VALUE = 4294967295
D3D10_PS_INPUT_REGISTER_COMPONENTS = 4
D3D10_PS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_INPUT_REGISTER_COUNT = 32
D3D10_PS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_PS_INPUT_REGISTER_READ_PORTS = 1
D3D10_PS_LEGACY_PIXEL_CENTER_FRACTIONAL_COMPONENT = 0
D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENTS = 1
D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_OUTPUT_DEPTH_REGISTER_COUNT = 1
D3D10_PS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_PS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_PS_OUTPUT_REGISTER_COUNT = 8
D3D10_PS_PIXEL_CENTER_FRACTIONAL_COMPONENT = 0.5
D3D10_REQ_BLEND_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_BUFFER_RESOURCE_TEXEL_COUNT_2_TO_EXP = 27
D3D10_REQ_CONSTANT_BUFFER_ELEMENT_COUNT = 4096
D3D10_REQ_DEPTH_STENCIL_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_DRAWINDEXED_INDEX_COUNT_2_TO_EXP = 32
D3D10_REQ_DRAW_VERTEX_COUNT_2_TO_EXP = 32
D3D10_REQ_FILTERING_HW_ADDRESSABLE_RESOURCE_DIMENSION = 8192
D3D10_REQ_GS_INVOCATION_32BIT_OUTPUT_COMPONENT_LIMIT = 1024
D3D10_REQ_IMMEDIATE_CONSTANT_BUFFER_ELEMENT_COUNT = 4096
D3D10_REQ_MAXANISOTROPY = 16
D3D10_REQ_MIP_LEVELS = 14
D3D10_REQ_MULTI_ELEMENT_STRUCTURE_SIZE_IN_BYTES = 2048
D3D10_REQ_RASTERIZER_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_RENDER_TO_BUFFER_WINDOW_WIDTH = 8192
D3D10_REQ_RESOURCE_SIZE_IN_MEGABYTES = 128
D3D10_REQ_RESOURCE_VIEW_COUNT_PER_CONTEXT_2_TO_EXP = 20
D3D10_REQ_SAMPLER_OBJECT_COUNT_PER_CONTEXT = 4096
D3D10_REQ_TEXTURE1D_ARRAY_AXIS_DIMENSION = 512
D3D10_REQ_TEXTURE1D_U_DIMENSION = 8192
D3D10_REQ_TEXTURE2D_ARRAY_AXIS_DIMENSION = 512
D3D10_REQ_TEXTURE2D_U_OR_V_DIMENSION = 8192
D3D10_REQ_TEXTURE3D_U_V_OR_W_DIMENSION = 2048
D3D10_REQ_TEXTURECUBE_DIMENSION = 8192
D3D10_RESINFO_INSTRUCTION_MISSING_COMPONENT_RETVAL = 0
D3D10_SHADER_MAJOR_VERSION = 4
D3D10_SHADER_MINOR_VERSION = 0
D3D10_SHIFT_INSTRUCTION_PAD_VALUE = 0
D3D10_SHIFT_INSTRUCTION_SHIFT_VALUE_BIT_COUNT = 5
D3D10_SIMULTANEOUS_RENDER_TARGET_COUNT = 8
D3D10_SO_BUFFER_MAX_STRIDE_IN_BYTES = 2048
D3D10_SO_BUFFER_MAX_WRITE_WINDOW_IN_BYTES = 256
D3D10_SO_BUFFER_SLOT_COUNT = 4
D3D10_SO_DDI_REGISTER_INDEX_DENOTING_GAP = 4294967295
D3D10_SO_MULTIPLE_BUFFER_ELEMENTS_PER_BUFFER = 1
D3D10_SO_SINGLE_BUFFER_COMPONENT_LIMIT = 64
D3D10_SRGB_GAMMA = 2.2
D3D10_SRGB_TO_FLOAT_DENOMINATOR_1 = 12.92
D3D10_SRGB_TO_FLOAT_DENOMINATOR_2 = 1.055
D3D10_SRGB_TO_FLOAT_EXPONENT = 2.4
D3D10_SRGB_TO_FLOAT_OFFSET = 0.055
D3D10_SRGB_TO_FLOAT_THRESHOLD = 0.04045
D3D10_SRGB_TO_FLOAT_TOLERANCE_IN_ULP = 0.5
D3D10_STANDARD_COMPONENT_BIT_COUNT = 32
D3D10_STANDARD_COMPONENT_BIT_COUNT_DOUBLED = 64
D3D10_STANDARD_MAXIMUM_ELEMENT_ALIGNMENT_BYTE_MULTIPLE = 4
D3D10_STANDARD_PIXEL_COMPONENT_COUNT = 128
D3D10_STANDARD_PIXEL_ELEMENT_COUNT = 32
D3D10_STANDARD_VECTOR_SIZE = 4
D3D10_STANDARD_VERTEX_ELEMENT_COUNT = 16
D3D10_STANDARD_VERTEX_TOTAL_COMPONENT_COUNT = 64
D3D10_SUBPIXEL_FRACTIONAL_BIT_COUNT = 8
D3D10_SUBTEXEL_FRACTIONAL_BIT_COUNT = 6
D3D10_TEXEL_ADDRESS_RANGE_BIT_COUNT = 18
D3D10_UNBOUND_MEMORY_ACCESS_RESULT = 0
D3D10_VIEWPORT_AND_SCISSORRECT_MAX_INDEX = 15
D3D10_VIEWPORT_AND_SCISSORRECT_OBJECT_COUNT_PER_PIPELINE = 16
D3D10_VIEWPORT_BOUNDS_MAX = 16383
D3D10_VIEWPORT_BOUNDS_MIN = -16384
D3D10_VS_INPUT_REGISTER_COMPONENTS = 4
D3D10_VS_INPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_VS_INPUT_REGISTER_COUNT = 16
D3D10_VS_INPUT_REGISTER_READS_PER_INST = 2
D3D10_VS_INPUT_REGISTER_READ_PORTS = 1
D3D10_VS_OUTPUT_REGISTER_COMPONENTS = 4
D3D10_VS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_VS_OUTPUT_REGISTER_COUNT = 16
D3D10_WHQL_CONTEXT_COUNT_FOR_RESOURCE_LIMIT = 10
D3D10_WHQL_DRAWINDEXED_INDEX_COUNT_2_TO_EXP = 25
D3D10_WHQL_DRAW_VERTEX_COUNT_2_TO_EXP = 25
D3D_MAJOR_VERSION = 10
D3D_MINOR_VERSION = 0
D3D_SPEC_DATE_DAY = 8
D3D_SPEC_DATE_MONTH = 8
D3D_SPEC_DATE_YEAR = 2006
D3D_SPEC_VERSION = 1.050005
D3D10_1_IA_VERTEX_INPUT_STRUCTURE_ELEMENT_COUNT = 16
D3D10_1_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT = 16
_FACD3D10 = 2169
D3D10_APPEND_ALIGNED_ELEMENT = 4294967295
D3D10_FILTER_TYPE_MASK = 3
D3D10_MIN_FILTER_SHIFT = 4
D3D10_MAG_FILTER_SHIFT = 2
D3D10_MIP_FILTER_SHIFT = 0
D3D10_COMPARISON_FILTERING_BIT = 128
D3D10_ANISOTROPIC_FILTERING_BIT = 64
D3D10_TEXT_1BIT_BIT = 2147483648
D3D10_SDK_VERSION = 29
D3D10_1_DEFAULT_SAMPLE_MASK = 4294967295
D3D10_1_FLOAT16_FUSED_TOLERANCE_IN_ULP = 0.6
D3D10_1_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP = 0.6
D3D10_1_GS_INPUT_REGISTER_COUNT = 32
D3D10_1_IA_VERTEX_INPUT_STRUCTURE_ELEMENTS_COMPONENTS = 128
D3D10_1_PS_OUTPUT_MASK_REGISTER_COMPONENTS = 1
D3D10_1_PS_OUTPUT_MASK_REGISTER_COMPONENT_BIT_COUNT = 32
D3D10_1_PS_OUTPUT_MASK_REGISTER_COUNT = 1
D3D10_1_SHADER_MAJOR_VERSION = 4
D3D10_1_SHADER_MINOR_VERSION = 1
D3D10_1_SO_BUFFER_MAX_STRIDE_IN_BYTES = 2048
D3D10_1_SO_BUFFER_MAX_WRITE_WINDOW_IN_BYTES = 256
D3D10_1_SO_BUFFER_SLOT_COUNT = 4
D3D10_1_SO_MULTIPLE_BUFFER_ELEMENTS_PER_BUFFER = 1
D3D10_1_SO_SINGLE_BUFFER_COMPONENT_LIMIT = 64
D3D10_1_STANDARD_VERTEX_ELEMENT_COUNT = 32
D3D10_1_SUBPIXEL_FRACTIONAL_BIT_COUNT = 8
D3D10_1_VS_INPUT_REGISTER_COUNT = 32
D3D10_1_VS_OUTPUT_REGISTER_COUNT = 32
D3D10_SDK_LAYERS_VERSION = 11
D3D10_DEBUG_FEATURE_FLUSH_PER_RENDER_OP = 1
D3D10_DEBUG_FEATURE_FINISH_PER_RENDER_OP = 2
D3D10_DEBUG_FEATURE_PRESENT_PER_RENDER_OP = 4
def _define_DXGI_DEBUG_D3D10():
    return Guid('243b4c52-3606-4d3a-99-d7-a7-e7-b3-3e-d7-06')
D3D10_REGKEY_PATH = 'Software\\Microsoft\\Direct3D'
D3D10_MUTE_DEBUG_OUTPUT = 'MuteDebugOutput'
D3D10_ENABLE_BREAK_ON_MESSAGE = 'EnableBreakOnMessage'
D3D10_INFOQUEUE_STORAGE_FILTER_OVERRIDE = 'InfoQueueStorageFilterOverride'
D3D10_MUTE_CATEGORY = 'Mute_CATEGORY_%s'
D3D10_MUTE_SEVERITY = 'Mute_SEVERITY_%s'
D3D10_MUTE_ID_STRING = 'Mute_ID_%s'
D3D10_MUTE_ID_DECIMAL = 'Mute_ID_%d'
D3D10_UNMUTE_SEVERITY_INFO = 'Unmute_SEVERITY_INFO'
D3D10_BREAKON_CATEGORY = 'BreakOn_CATEGORY_%s'
D3D10_BREAKON_SEVERITY = 'BreakOn_SEVERITY_%s'
D3D10_BREAKON_ID_STRING = 'BreakOn_ID_%s'
D3D10_BREAKON_ID_DECIMAL = 'BreakOn_ID_%d'
D3D10_APPSIZE_STRING = 'Size'
D3D10_APPNAME_STRING = 'Name'
D3D10_INFO_QUEUE_DEFAULT_MESSAGE_COUNT_LIMIT = 1024
D3D10_SHADER_DEBUG = 1
D3D10_SHADER_SKIP_VALIDATION = 2
D3D10_SHADER_SKIP_OPTIMIZATION = 4
D3D10_SHADER_PACK_MATRIX_ROW_MAJOR = 8
D3D10_SHADER_PACK_MATRIX_COLUMN_MAJOR = 16
D3D10_SHADER_PARTIAL_PRECISION = 32
D3D10_SHADER_FORCE_VS_SOFTWARE_NO_OPT = 64
D3D10_SHADER_FORCE_PS_SOFTWARE_NO_OPT = 128
D3D10_SHADER_NO_PRESHADER = 256
D3D10_SHADER_AVOID_FLOW_CONTROL = 512
D3D10_SHADER_PREFER_FLOW_CONTROL = 1024
D3D10_SHADER_ENABLE_STRICTNESS = 2048
D3D10_SHADER_ENABLE_BACKWARDS_COMPATIBILITY = 4096
D3D10_SHADER_IEEE_STRICTNESS = 8192
D3D10_SHADER_WARNINGS_ARE_ERRORS = 262144
D3D10_SHADER_RESOURCES_MAY_ALIAS = 524288
D3D10_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES = 1048576
D3D10_ALL_RESOURCES_BOUND = 2097152
D3D10_SHADER_DEBUG_NAME_FOR_SOURCE = 4194304
D3D10_SHADER_DEBUG_NAME_FOR_BINARY = 8388608
D3D10_SHADER_OPTIMIZATION_LEVEL0 = 16384
D3D10_SHADER_OPTIMIZATION_LEVEL1 = 0
D3D10_SHADER_OPTIMIZATION_LEVEL3 = 32768
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST = 0
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_0 = 16
D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_1 = 32
D3D10_EFFECT_COMPILE_CHILD_EFFECT = 1
D3D10_EFFECT_COMPILE_ALLOW_SLOW_OPS = 2
D3D10_EFFECT_SINGLE_THREADED = 8
D3D10_EFFECT_VARIABLE_POOLED = 1
D3D10_EFFECT_VARIABLE_ANNOTATION = 2
D3D10_EFFECT_VARIABLE_EXPLICIT_BIND_POINT = 4
def _define_GUID_DeviceType():
    return Guid('d722fb4d-7a68-437a-b2-0c-58-04-ee-24-94-a6')
def _define_D3D10CreateDevice():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Device_head))(('D3D10CreateDevice', windll['d3d10.dll']), ((1, 'pAdapter'),(1, 'DriverType'),(1, 'Software'),(1, 'Flags'),(1, 'SDKVersion'),(1, 'ppDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateDeviceAndSwapChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head),POINTER(win32more.Graphics.Dxgi.IDXGISwapChain_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Device_head))(('D3D10CreateDeviceAndSwapChain', windll['d3d10.dll']), ((1, 'pAdapter'),(1, 'DriverType'),(1, 'Software'),(1, 'Flags'),(1, 'SDKVersion'),(1, 'pSwapChainDesc'),(1, 'ppSwapChain'),(1, 'ppDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10CreateBlob', windll['d3d10.dll']), ((1, 'NumBytes'),(1, 'ppBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CompileShader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10CompileShader', windll['d3d10.dll']), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pFileName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'pFunctionName'),(1, 'pProfile'),(1, 'Flags'),(1, 'ppShader'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10DisassembleShader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10DisassembleShader', windll['d3d10.dll']), ((1, 'pShader'),(1, 'BytecodeLength'),(1, 'EnableColorCode'),(1, 'pComments'),(1, 'ppDisassembly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetPixelShaderProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Graphics.Direct3D10.ID3D10Device_head)(('D3D10GetPixelShaderProfile', windll['d3d10.dll']), ((1, 'pDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetVertexShaderProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Graphics.Direct3D10.ID3D10Device_head)(('D3D10GetVertexShaderProfile', windll['d3d10.dll']), ((1, 'pDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetGeometryShaderProfile():
    try:
        return WINFUNCTYPE(win32more.Foundation.PSTR,win32more.Graphics.Direct3D10.ID3D10Device_head)(('D3D10GetGeometryShaderProfile', windll['d3d10.dll']), ((1, 'pDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10ReflectShader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderReflection_head))(('D3D10ReflectShader', windll['d3d10.dll']), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppReflector'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10PreprocessShader():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10PreprocessShader', windll['d3d10.dll']), ((1, 'pSrcData'),(1, 'SrcDataSize'),(1, 'pFileName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'ppShaderText'),(1, 'ppErrorMsgs'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetInputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10GetInputSignatureBlob', windll['d3d10.dll']), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetOutputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10GetOutputSignatureBlob', windll['d3d10.dll']), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetInputAndOutputSignatureBlob():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10GetInputAndOutputSignatureBlob', windll['d3d10.dll']), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppSignatureBlob'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10GetShaderDebugInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10GetShaderDebugInfo', windll['d3d10.dll']), ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppDebugInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskUnion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(('D3D10StateBlockMaskUnion', windll['d3d10.dll']), ((1, 'pA'),(1, 'pB'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskIntersect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(('D3D10StateBlockMaskIntersect', windll['d3d10.dll']), ((1, 'pA'),(1, 'pB'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskDifference():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(('D3D10StateBlockMaskDifference', windll['d3d10.dll']), ((1, 'pA'),(1, 'pB'),(1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskEnableCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),win32more.Graphics.Direct3D10.D3D10_DEVICE_STATE_TYPES,UInt32,UInt32)(('D3D10StateBlockMaskEnableCapture', windll['d3d10.dll']), ((1, 'pMask'),(1, 'StateType'),(1, 'RangeStart'),(1, 'RangeLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskDisableCapture():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),win32more.Graphics.Direct3D10.D3D10_DEVICE_STATE_TYPES,UInt32,UInt32)(('D3D10StateBlockMaskDisableCapture', windll['d3d10.dll']), ((1, 'pMask'),(1, 'StateType'),(1, 'RangeStart'),(1, 'RangeLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskEnableAll():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(('D3D10StateBlockMaskEnableAll', windll['d3d10.dll']), ((1, 'pMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskDisableAll():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(('D3D10StateBlockMaskDisableAll', windll['d3d10.dll']), ((1, 'pMask'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10StateBlockMaskGetSetting():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),win32more.Graphics.Direct3D10.D3D10_DEVICE_STATE_TYPES,UInt32)(('D3D10StateBlockMaskGetSetting', windll['d3d10.dll']), ((1, 'pMask'),(1, 'StateType'),(1, 'Entry'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateStateBlock():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Device_head,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head),POINTER(win32more.Graphics.Direct3D10.ID3D10StateBlock_head))(('D3D10CreateStateBlock', windll['d3d10.dll']), ((1, 'pDevice'),(1, 'pStateBlockMask'),(1, 'ppStateBlock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CompileEffectFromMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D.D3D_SHADER_MACRO_head),win32more.Graphics.Direct3D.ID3DInclude_head,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head),POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10CompileEffectFromMemory', windll['d3d10.dll']), ((1, 'pData'),(1, 'DataLength'),(1, 'pSrcFileName'),(1, 'pDefines'),(1, 'pInclude'),(1, 'HLSLFlags'),(1, 'FXFlags'),(1, 'ppCompiledEffect'),(1, 'ppErrors'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateEffectFromMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,win32more.Graphics.Direct3D10.ID3D10Device_head,win32more.Graphics.Direct3D10.ID3D10EffectPool_head,POINTER(win32more.Graphics.Direct3D10.ID3D10Effect_head))(('D3D10CreateEffectFromMemory', windll['d3d10.dll']), ((1, 'pData'),(1, 'DataLength'),(1, 'FXFlags'),(1, 'pDevice'),(1, 'pEffectPool'),(1, 'ppEffect'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateEffectPoolFromMemory():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,UInt32,win32more.Graphics.Direct3D10.ID3D10Device_head,POINTER(win32more.Graphics.Direct3D10.ID3D10EffectPool_head))(('D3D10CreateEffectPoolFromMemory', windll['d3d10.dll']), ((1, 'pData'),(1, 'DataLength'),(1, 'FXFlags'),(1, 'pDevice'),(1, 'ppEffectPool'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10DisassembleEffect():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Effect_head,win32more.Foundation.BOOL,POINTER(win32more.Graphics.Direct3D.ID3DBlob_head))(('D3D10DisassembleEffect', windll['d3d10.dll']), ((1, 'pEffect'),(1, 'EnableColorCode'),(1, 'ppDisassembly'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateDevice1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,win32more.Graphics.Direct3D10.D3D10_FEATURE_LEVEL1,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Device1_head))(('D3D10CreateDevice1', windll['d3d10_1.dll']), ((1, 'pAdapter'),(1, 'DriverType'),(1, 'Software'),(1, 'Flags'),(1, 'HardwareLevel'),(1, 'SDKVersion'),(1, 'ppDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_D3D10CreateDeviceAndSwapChain1():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,win32more.Graphics.Direct3D10.D3D10_FEATURE_LEVEL1,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head),POINTER(win32more.Graphics.Dxgi.IDXGISwapChain_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Device1_head))(('D3D10CreateDeviceAndSwapChain1', windll['d3d10_1.dll']), ((1, 'pAdapter'),(1, 'DriverType'),(1, 'Software'),(1, 'Flags'),(1, 'HardwareLevel'),(1, 'SDKVersion'),(1, 'pSwapChainDesc'),(1, 'ppSwapChain'),(1, 'ppDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
D3D10_ASYNC_GETDATA_FLAG = Int32
D3D10_ASYNC_GETDATA_DONOTFLUSH = 1
D3D10_BIND_FLAG = Int32
D3D10_BIND_VERTEX_BUFFER = 1
D3D10_BIND_INDEX_BUFFER = 2
D3D10_BIND_CONSTANT_BUFFER = 4
D3D10_BIND_SHADER_RESOURCE = 8
D3D10_BIND_STREAM_OUTPUT = 16
D3D10_BIND_RENDER_TARGET = 32
D3D10_BIND_DEPTH_STENCIL = 64
D3D10_BLEND = Int32
D3D10_BLEND_ZERO = 1
D3D10_BLEND_ONE = 2
D3D10_BLEND_SRC_COLOR = 3
D3D10_BLEND_INV_SRC_COLOR = 4
D3D10_BLEND_SRC_ALPHA = 5
D3D10_BLEND_INV_SRC_ALPHA = 6
D3D10_BLEND_DEST_ALPHA = 7
D3D10_BLEND_INV_DEST_ALPHA = 8
D3D10_BLEND_DEST_COLOR = 9
D3D10_BLEND_INV_DEST_COLOR = 10
D3D10_BLEND_SRC_ALPHA_SAT = 11
D3D10_BLEND_BLEND_FACTOR = 14
D3D10_BLEND_INV_BLEND_FACTOR = 15
D3D10_BLEND_SRC1_COLOR = 16
D3D10_BLEND_INV_SRC1_COLOR = 17
D3D10_BLEND_SRC1_ALPHA = 18
D3D10_BLEND_INV_SRC1_ALPHA = 19
def _define_D3D10_BLEND_DESC_head():
    class D3D10_BLEND_DESC(Structure):
        pass
    return D3D10_BLEND_DESC
def _define_D3D10_BLEND_DESC():
    D3D10_BLEND_DESC = win32more.Graphics.Direct3D10.D3D10_BLEND_DESC_head
    D3D10_BLEND_DESC._fields_ = [
        ('AlphaToCoverageEnable', win32more.Foundation.BOOL),
        ('BlendEnable', win32more.Foundation.BOOL * 8),
        ('SrcBlend', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('DestBlend', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('BlendOp', win32more.Graphics.Direct3D10.D3D10_BLEND_OP),
        ('SrcBlendAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('DestBlendAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('BlendOpAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND_OP),
        ('RenderTargetWriteMask', Byte * 8),
    ]
    return D3D10_BLEND_DESC
def _define_D3D10_BLEND_DESC1_head():
    class D3D10_BLEND_DESC1(Structure):
        pass
    return D3D10_BLEND_DESC1
def _define_D3D10_BLEND_DESC1():
    D3D10_BLEND_DESC1 = win32more.Graphics.Direct3D10.D3D10_BLEND_DESC1_head
    D3D10_BLEND_DESC1._fields_ = [
        ('AlphaToCoverageEnable', win32more.Foundation.BOOL),
        ('IndependentBlendEnable', win32more.Foundation.BOOL),
        ('RenderTarget', win32more.Graphics.Direct3D10.D3D10_RENDER_TARGET_BLEND_DESC1 * 8),
    ]
    return D3D10_BLEND_DESC1
D3D10_BLEND_OP = Int32
D3D10_BLEND_OP_ADD = 1
D3D10_BLEND_OP_SUBTRACT = 2
D3D10_BLEND_OP_REV_SUBTRACT = 3
D3D10_BLEND_OP_MIN = 4
D3D10_BLEND_OP_MAX = 5
def _define_D3D10_BOX_head():
    class D3D10_BOX(Structure):
        pass
    return D3D10_BOX
def _define_D3D10_BOX():
    D3D10_BOX = win32more.Graphics.Direct3D10.D3D10_BOX_head
    D3D10_BOX._fields_ = [
        ('left', UInt32),
        ('top', UInt32),
        ('front', UInt32),
        ('right', UInt32),
        ('bottom', UInt32),
        ('back', UInt32),
    ]
    return D3D10_BOX
def _define_D3D10_BUFFER_DESC_head():
    class D3D10_BUFFER_DESC(Structure):
        pass
    return D3D10_BUFFER_DESC
def _define_D3D10_BUFFER_DESC():
    D3D10_BUFFER_DESC = win32more.Graphics.Direct3D10.D3D10_BUFFER_DESC_head
    D3D10_BUFFER_DESC._fields_ = [
        ('ByteWidth', UInt32),
        ('Usage', win32more.Graphics.Direct3D10.D3D10_USAGE),
        ('BindFlags', UInt32),
        ('CPUAccessFlags', UInt32),
        ('MiscFlags', UInt32),
    ]
    return D3D10_BUFFER_DESC
def _define_D3D10_BUFFER_RTV_head():
    class D3D10_BUFFER_RTV(Structure):
        pass
    return D3D10_BUFFER_RTV
def _define_D3D10_BUFFER_RTV():
    D3D10_BUFFER_RTV = win32more.Graphics.Direct3D10.D3D10_BUFFER_RTV_head
    class D3D10_BUFFER_RTV__Anonymous1_e__Union(Union):
        pass
    D3D10_BUFFER_RTV__Anonymous1_e__Union._fields_ = [
        ('FirstElement', UInt32),
        ('ElementOffset', UInt32),
    ]
    class D3D10_BUFFER_RTV__Anonymous2_e__Union(Union):
        pass
    D3D10_BUFFER_RTV__Anonymous2_e__Union._fields_ = [
        ('NumElements', UInt32),
        ('ElementWidth', UInt32),
    ]
    D3D10_BUFFER_RTV._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    D3D10_BUFFER_RTV._fields_ = [
        ('Anonymous1', D3D10_BUFFER_RTV__Anonymous1_e__Union),
        ('Anonymous2', D3D10_BUFFER_RTV__Anonymous2_e__Union),
    ]
    return D3D10_BUFFER_RTV
def _define_D3D10_BUFFER_SRV_head():
    class D3D10_BUFFER_SRV(Structure):
        pass
    return D3D10_BUFFER_SRV
def _define_D3D10_BUFFER_SRV():
    D3D10_BUFFER_SRV = win32more.Graphics.Direct3D10.D3D10_BUFFER_SRV_head
    class D3D10_BUFFER_SRV__Anonymous1_e__Union(Union):
        pass
    D3D10_BUFFER_SRV__Anonymous1_e__Union._fields_ = [
        ('FirstElement', UInt32),
        ('ElementOffset', UInt32),
    ]
    class D3D10_BUFFER_SRV__Anonymous2_e__Union(Union):
        pass
    D3D10_BUFFER_SRV__Anonymous2_e__Union._fields_ = [
        ('NumElements', UInt32),
        ('ElementWidth', UInt32),
    ]
    D3D10_BUFFER_SRV._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    D3D10_BUFFER_SRV._fields_ = [
        ('Anonymous1', D3D10_BUFFER_SRV__Anonymous1_e__Union),
        ('Anonymous2', D3D10_BUFFER_SRV__Anonymous2_e__Union),
    ]
    return D3D10_BUFFER_SRV
D3D10_CLEAR_FLAG = Int32
D3D10_CLEAR_DEPTH = 1
D3D10_CLEAR_STENCIL = 2
D3D10_COLOR_WRITE_ENABLE = Int32
D3D10_COLOR_WRITE_ENABLE_RED = 1
D3D10_COLOR_WRITE_ENABLE_GREEN = 2
D3D10_COLOR_WRITE_ENABLE_BLUE = 4
D3D10_COLOR_WRITE_ENABLE_ALPHA = 8
D3D10_COLOR_WRITE_ENABLE_ALL = 15
D3D10_COMPARISON_FUNC = Int32
D3D10_COMPARISON_NEVER = 1
D3D10_COMPARISON_LESS = 2
D3D10_COMPARISON_EQUAL = 3
D3D10_COMPARISON_LESS_EQUAL = 4
D3D10_COMPARISON_GREATER = 5
D3D10_COMPARISON_NOT_EQUAL = 6
D3D10_COMPARISON_GREATER_EQUAL = 7
D3D10_COMPARISON_ALWAYS = 8
D3D10_COUNTER = Int32
D3D10_COUNTER_GPU_IDLE = 0
D3D10_COUNTER_VERTEX_PROCESSING = 1
D3D10_COUNTER_GEOMETRY_PROCESSING = 2
D3D10_COUNTER_PIXEL_PROCESSING = 3
D3D10_COUNTER_OTHER_GPU_PROCESSING = 4
D3D10_COUNTER_HOST_ADAPTER_BANDWIDTH_UTILIZATION = 5
D3D10_COUNTER_LOCAL_VIDMEM_BANDWIDTH_UTILIZATION = 6
D3D10_COUNTER_VERTEX_THROUGHPUT_UTILIZATION = 7
D3D10_COUNTER_TRIANGLE_SETUP_THROUGHPUT_UTILIZATION = 8
D3D10_COUNTER_FILLRATE_THROUGHPUT_UTILIZATION = 9
D3D10_COUNTER_VS_MEMORY_LIMITED = 10
D3D10_COUNTER_VS_COMPUTATION_LIMITED = 11
D3D10_COUNTER_GS_MEMORY_LIMITED = 12
D3D10_COUNTER_GS_COMPUTATION_LIMITED = 13
D3D10_COUNTER_PS_MEMORY_LIMITED = 14
D3D10_COUNTER_PS_COMPUTATION_LIMITED = 15
D3D10_COUNTER_POST_TRANSFORM_CACHE_HIT_RATE = 16
D3D10_COUNTER_TEXTURE_CACHE_HIT_RATE = 17
D3D10_COUNTER_DEVICE_DEPENDENT_0 = 1073741824
def _define_D3D10_COUNTER_DESC_head():
    class D3D10_COUNTER_DESC(Structure):
        pass
    return D3D10_COUNTER_DESC
def _define_D3D10_COUNTER_DESC():
    D3D10_COUNTER_DESC = win32more.Graphics.Direct3D10.D3D10_COUNTER_DESC_head
    D3D10_COUNTER_DESC._fields_ = [
        ('Counter', win32more.Graphics.Direct3D10.D3D10_COUNTER),
        ('MiscFlags', UInt32),
    ]
    return D3D10_COUNTER_DESC
def _define_D3D10_COUNTER_INFO_head():
    class D3D10_COUNTER_INFO(Structure):
        pass
    return D3D10_COUNTER_INFO
def _define_D3D10_COUNTER_INFO():
    D3D10_COUNTER_INFO = win32more.Graphics.Direct3D10.D3D10_COUNTER_INFO_head
    D3D10_COUNTER_INFO._fields_ = [
        ('LastDeviceDependentCounter', win32more.Graphics.Direct3D10.D3D10_COUNTER),
        ('NumSimultaneousCounters', UInt32),
        ('NumDetectableParallelUnits', Byte),
    ]
    return D3D10_COUNTER_INFO
D3D10_COUNTER_TYPE = Int32
D3D10_COUNTER_TYPE_FLOAT32 = 0
D3D10_COUNTER_TYPE_UINT16 = 1
D3D10_COUNTER_TYPE_UINT32 = 2
D3D10_COUNTER_TYPE_UINT64 = 3
D3D10_CPU_ACCESS_FLAG = Int32
D3D10_CPU_ACCESS_WRITE = 65536
D3D10_CPU_ACCESS_READ = 131072
D3D10_CREATE_DEVICE_FLAG = Int32
D3D10_CREATE_DEVICE_SINGLETHREADED = 1
D3D10_CREATE_DEVICE_DEBUG = 2
D3D10_CREATE_DEVICE_SWITCH_TO_REF = 4
D3D10_CREATE_DEVICE_PREVENT_INTERNAL_THREADING_OPTIMIZATIONS = 8
D3D10_CREATE_DEVICE_ALLOW_NULL_FROM_MAP = 16
D3D10_CREATE_DEVICE_BGRA_SUPPORT = 32
D3D10_CREATE_DEVICE_PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY = 128
D3D10_CREATE_DEVICE_STRICT_VALIDATION = 512
D3D10_CREATE_DEVICE_DEBUGGABLE = 1024
D3D10_CULL_MODE = Int32
D3D10_CULL_NONE = 1
D3D10_CULL_FRONT = 2
D3D10_CULL_BACK = 3
def _define_D3D10_DEPTH_STENCIL_DESC_head():
    class D3D10_DEPTH_STENCIL_DESC(Structure):
        pass
    return D3D10_DEPTH_STENCIL_DESC
def _define_D3D10_DEPTH_STENCIL_DESC():
    D3D10_DEPTH_STENCIL_DESC = win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_DESC_head
    D3D10_DEPTH_STENCIL_DESC._fields_ = [
        ('DepthEnable', win32more.Foundation.BOOL),
        ('DepthWriteMask', win32more.Graphics.Direct3D10.D3D10_DEPTH_WRITE_MASK),
        ('DepthFunc', win32more.Graphics.Direct3D10.D3D10_COMPARISON_FUNC),
        ('StencilEnable', win32more.Foundation.BOOL),
        ('StencilReadMask', Byte),
        ('StencilWriteMask', Byte),
        ('FrontFace', win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCILOP_DESC),
        ('BackFace', win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCILOP_DESC),
    ]
    return D3D10_DEPTH_STENCIL_DESC
def _define_D3D10_DEPTH_STENCIL_VIEW_DESC_head():
    class D3D10_DEPTH_STENCIL_VIEW_DESC(Structure):
        pass
    return D3D10_DEPTH_STENCIL_VIEW_DESC
def _define_D3D10_DEPTH_STENCIL_VIEW_DESC():
    D3D10_DEPTH_STENCIL_VIEW_DESC = win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_VIEW_DESC_head
    class D3D10_DEPTH_STENCIL_VIEW_DESC__Anonymous_e__Union(Union):
        pass
    D3D10_DEPTH_STENCIL_VIEW_DESC__Anonymous_e__Union._fields_ = [
        ('Texture1D', win32more.Graphics.Direct3D10.D3D10_TEX1D_DSV),
        ('Texture1DArray', win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_DSV),
        ('Texture2D', win32more.Graphics.Direct3D10.D3D10_TEX2D_DSV),
        ('Texture2DArray', win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_DSV),
        ('Texture2DMS', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_DSV),
        ('Texture2DMSArray', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_DSV),
    ]
    D3D10_DEPTH_STENCIL_VIEW_DESC._anonymous_ = [
        'Anonymous',
    ]
    D3D10_DEPTH_STENCIL_VIEW_DESC._fields_ = [
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('ViewDimension', win32more.Graphics.Direct3D10.D3D10_DSV_DIMENSION),
        ('Anonymous', D3D10_DEPTH_STENCIL_VIEW_DESC__Anonymous_e__Union),
    ]
    return D3D10_DEPTH_STENCIL_VIEW_DESC
def _define_D3D10_DEPTH_STENCILOP_DESC_head():
    class D3D10_DEPTH_STENCILOP_DESC(Structure):
        pass
    return D3D10_DEPTH_STENCILOP_DESC
def _define_D3D10_DEPTH_STENCILOP_DESC():
    D3D10_DEPTH_STENCILOP_DESC = win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCILOP_DESC_head
    D3D10_DEPTH_STENCILOP_DESC._fields_ = [
        ('StencilFailOp', win32more.Graphics.Direct3D10.D3D10_STENCIL_OP),
        ('StencilDepthFailOp', win32more.Graphics.Direct3D10.D3D10_STENCIL_OP),
        ('StencilPassOp', win32more.Graphics.Direct3D10.D3D10_STENCIL_OP),
        ('StencilFunc', win32more.Graphics.Direct3D10.D3D10_COMPARISON_FUNC),
    ]
    return D3D10_DEPTH_STENCILOP_DESC
D3D10_DEPTH_WRITE_MASK = Int32
D3D10_DEPTH_WRITE_MASK_ZERO = 0
D3D10_DEPTH_WRITE_MASK_ALL = 1
D3D10_DEVICE_STATE_TYPES = Int32
D3D10_DST_SO_BUFFERS = 1
D3D10_DST_OM_RENDER_TARGETS = 2
D3D10_DST_OM_DEPTH_STENCIL_STATE = 3
D3D10_DST_OM_BLEND_STATE = 4
D3D10_DST_VS = 5
D3D10_DST_VS_SAMPLERS = 6
D3D10_DST_VS_SHADER_RESOURCES = 7
D3D10_DST_VS_CONSTANT_BUFFERS = 8
D3D10_DST_GS = 9
D3D10_DST_GS_SAMPLERS = 10
D3D10_DST_GS_SHADER_RESOURCES = 11
D3D10_DST_GS_CONSTANT_BUFFERS = 12
D3D10_DST_PS = 13
D3D10_DST_PS_SAMPLERS = 14
D3D10_DST_PS_SHADER_RESOURCES = 15
D3D10_DST_PS_CONSTANT_BUFFERS = 16
D3D10_DST_IA_VERTEX_BUFFERS = 17
D3D10_DST_IA_INDEX_BUFFER = 18
D3D10_DST_IA_INPUT_LAYOUT = 19
D3D10_DST_IA_PRIMITIVE_TOPOLOGY = 20
D3D10_DST_RS_VIEWPORTS = 21
D3D10_DST_RS_SCISSOR_RECTS = 22
D3D10_DST_RS_RASTERIZER_STATE = 23
D3D10_DST_PREDICATION = 24
D3D10_DRIVER_TYPE = Int32
D3D10_DRIVER_TYPE_HARDWARE = 0
D3D10_DRIVER_TYPE_REFERENCE = 1
D3D10_DRIVER_TYPE_NULL = 2
D3D10_DRIVER_TYPE_SOFTWARE = 3
D3D10_DRIVER_TYPE_WARP = 5
D3D10_DSV_DIMENSION = Int32
D3D10_DSV_DIMENSION_UNKNOWN = 0
D3D10_DSV_DIMENSION_TEXTURE1D = 1
D3D10_DSV_DIMENSION_TEXTURE1DARRAY = 2
D3D10_DSV_DIMENSION_TEXTURE2D = 3
D3D10_DSV_DIMENSION_TEXTURE2DARRAY = 4
D3D10_DSV_DIMENSION_TEXTURE2DMS = 5
D3D10_DSV_DIMENSION_TEXTURE2DMSARRAY = 6
def _define_D3D10_EFFECT_DESC_head():
    class D3D10_EFFECT_DESC(Structure):
        pass
    return D3D10_EFFECT_DESC
def _define_D3D10_EFFECT_DESC():
    D3D10_EFFECT_DESC = win32more.Graphics.Direct3D10.D3D10_EFFECT_DESC_head
    D3D10_EFFECT_DESC._fields_ = [
        ('IsChildEffect', win32more.Foundation.BOOL),
        ('ConstantBuffers', UInt32),
        ('SharedConstantBuffers', UInt32),
        ('GlobalVariables', UInt32),
        ('SharedGlobalVariables', UInt32),
        ('Techniques', UInt32),
    ]
    return D3D10_EFFECT_DESC
def _define_D3D10_EFFECT_SHADER_DESC_head():
    class D3D10_EFFECT_SHADER_DESC(Structure):
        pass
    return D3D10_EFFECT_SHADER_DESC
def _define_D3D10_EFFECT_SHADER_DESC():
    D3D10_EFFECT_SHADER_DESC = win32more.Graphics.Direct3D10.D3D10_EFFECT_SHADER_DESC_head
    D3D10_EFFECT_SHADER_DESC._fields_ = [
        ('pInputSignature', c_char_p_no),
        ('IsInline', win32more.Foundation.BOOL),
        ('pBytecode', c_char_p_no),
        ('BytecodeLength', UInt32),
        ('SODecl', win32more.Foundation.PSTR),
        ('NumInputSignatureEntries', UInt32),
        ('NumOutputSignatureEntries', UInt32),
    ]
    return D3D10_EFFECT_SHADER_DESC
def _define_D3D10_EFFECT_TYPE_DESC_head():
    class D3D10_EFFECT_TYPE_DESC(Structure):
        pass
    return D3D10_EFFECT_TYPE_DESC
def _define_D3D10_EFFECT_TYPE_DESC():
    D3D10_EFFECT_TYPE_DESC = win32more.Graphics.Direct3D10.D3D10_EFFECT_TYPE_DESC_head
    D3D10_EFFECT_TYPE_DESC._fields_ = [
        ('TypeName', win32more.Foundation.PSTR),
        ('Class', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_CLASS),
        ('Type', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_TYPE),
        ('Elements', UInt32),
        ('Members', UInt32),
        ('Rows', UInt32),
        ('Columns', UInt32),
        ('PackedSize', UInt32),
        ('UnpackedSize', UInt32),
        ('Stride', UInt32),
    ]
    return D3D10_EFFECT_TYPE_DESC
def _define_D3D10_EFFECT_VARIABLE_DESC_head():
    class D3D10_EFFECT_VARIABLE_DESC(Structure):
        pass
    return D3D10_EFFECT_VARIABLE_DESC
def _define_D3D10_EFFECT_VARIABLE_DESC():
    D3D10_EFFECT_VARIABLE_DESC = win32more.Graphics.Direct3D10.D3D10_EFFECT_VARIABLE_DESC_head
    D3D10_EFFECT_VARIABLE_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Semantic', win32more.Foundation.PSTR),
        ('Flags', UInt32),
        ('Annotations', UInt32),
        ('BufferOffset', UInt32),
        ('ExplicitBindPoint', UInt32),
    ]
    return D3D10_EFFECT_VARIABLE_DESC
D3D10_FEATURE_LEVEL1 = Int32
D3D10_FEATURE_LEVEL_10_0 = 40960
D3D10_FEATURE_LEVEL_10_1 = 41216
D3D10_FEATURE_LEVEL_9_1 = 37120
D3D10_FEATURE_LEVEL_9_2 = 37376
D3D10_FEATURE_LEVEL_9_3 = 37632
D3D10_FILL_MODE = Int32
D3D10_FILL_WIREFRAME = 2
D3D10_FILL_SOLID = 3
D3D10_FILTER = Int32
D3D10_FILTER_MIN_MAG_MIP_POINT = 0
D3D10_FILTER_MIN_MAG_POINT_MIP_LINEAR = 1
D3D10_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT = 4
D3D10_FILTER_MIN_POINT_MAG_MIP_LINEAR = 5
D3D10_FILTER_MIN_LINEAR_MAG_MIP_POINT = 16
D3D10_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 17
D3D10_FILTER_MIN_MAG_LINEAR_MIP_POINT = 20
D3D10_FILTER_MIN_MAG_MIP_LINEAR = 21
D3D10_FILTER_ANISOTROPIC = 85
D3D10_FILTER_COMPARISON_MIN_MAG_MIP_POINT = 128
D3D10_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR = 129
D3D10_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT = 132
D3D10_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR = 133
D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT = 144
D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR = 145
D3D10_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT = 148
D3D10_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR = 149
D3D10_FILTER_COMPARISON_ANISOTROPIC = 213
D3D10_FILTER_TEXT_1BIT = -2147483648
D3D10_FILTER_TYPE = Int32
D3D10_FILTER_TYPE_POINT = 0
D3D10_FILTER_TYPE_LINEAR = 1
D3D10_FORMAT_SUPPORT = Int32
D3D10_FORMAT_SUPPORT_BUFFER = 1
D3D10_FORMAT_SUPPORT_IA_VERTEX_BUFFER = 2
D3D10_FORMAT_SUPPORT_IA_INDEX_BUFFER = 4
D3D10_FORMAT_SUPPORT_SO_BUFFER = 8
D3D10_FORMAT_SUPPORT_TEXTURE1D = 16
D3D10_FORMAT_SUPPORT_TEXTURE2D = 32
D3D10_FORMAT_SUPPORT_TEXTURE3D = 64
D3D10_FORMAT_SUPPORT_TEXTURECUBE = 128
D3D10_FORMAT_SUPPORT_SHADER_LOAD = 256
D3D10_FORMAT_SUPPORT_SHADER_SAMPLE = 512
D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_COMPARISON = 1024
D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_MONO_TEXT = 2048
D3D10_FORMAT_SUPPORT_MIP = 4096
D3D10_FORMAT_SUPPORT_MIP_AUTOGEN = 8192
D3D10_FORMAT_SUPPORT_RENDER_TARGET = 16384
D3D10_FORMAT_SUPPORT_BLENDABLE = 32768
D3D10_FORMAT_SUPPORT_DEPTH_STENCIL = 65536
D3D10_FORMAT_SUPPORT_CPU_LOCKABLE = 131072
D3D10_FORMAT_SUPPORT_MULTISAMPLE_RESOLVE = 262144
D3D10_FORMAT_SUPPORT_DISPLAY = 524288
D3D10_FORMAT_SUPPORT_CAST_WITHIN_BIT_LAYOUT = 1048576
D3D10_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET = 2097152
D3D10_FORMAT_SUPPORT_MULTISAMPLE_LOAD = 4194304
D3D10_FORMAT_SUPPORT_SHADER_GATHER = 8388608
D3D10_FORMAT_SUPPORT_BACK_BUFFER_CAST = 16777216
def _define_D3D10_INFO_QUEUE_FILTER_head():
    class D3D10_INFO_QUEUE_FILTER(Structure):
        pass
    return D3D10_INFO_QUEUE_FILTER
def _define_D3D10_INFO_QUEUE_FILTER():
    D3D10_INFO_QUEUE_FILTER = win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head
    D3D10_INFO_QUEUE_FILTER._fields_ = [
        ('AllowList', win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_DESC),
        ('DenyList', win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_DESC),
    ]
    return D3D10_INFO_QUEUE_FILTER
def _define_D3D10_INFO_QUEUE_FILTER_DESC_head():
    class D3D10_INFO_QUEUE_FILTER_DESC(Structure):
        pass
    return D3D10_INFO_QUEUE_FILTER_DESC
def _define_D3D10_INFO_QUEUE_FILTER_DESC():
    D3D10_INFO_QUEUE_FILTER_DESC = win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_DESC_head
    D3D10_INFO_QUEUE_FILTER_DESC._fields_ = [
        ('NumCategories', UInt32),
        ('pCategoryList', POINTER(win32more.Graphics.Direct3D10.D3D10_MESSAGE_CATEGORY)),
        ('NumSeverities', UInt32),
        ('pSeverityList', POINTER(win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY)),
        ('NumIDs', UInt32),
        ('pIDList', POINTER(win32more.Graphics.Direct3D10.D3D10_MESSAGE_ID)),
    ]
    return D3D10_INFO_QUEUE_FILTER_DESC
D3D10_INPUT_CLASSIFICATION = Int32
D3D10_INPUT_PER_VERTEX_DATA = 0
D3D10_INPUT_PER_INSTANCE_DATA = 1
def _define_D3D10_INPUT_ELEMENT_DESC_head():
    class D3D10_INPUT_ELEMENT_DESC(Structure):
        pass
    return D3D10_INPUT_ELEMENT_DESC
def _define_D3D10_INPUT_ELEMENT_DESC():
    D3D10_INPUT_ELEMENT_DESC = win32more.Graphics.Direct3D10.D3D10_INPUT_ELEMENT_DESC_head
    D3D10_INPUT_ELEMENT_DESC._fields_ = [
        ('SemanticName', win32more.Foundation.PSTR),
        ('SemanticIndex', UInt32),
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('InputSlot', UInt32),
        ('AlignedByteOffset', UInt32),
        ('InputSlotClass', win32more.Graphics.Direct3D10.D3D10_INPUT_CLASSIFICATION),
        ('InstanceDataStepRate', UInt32),
    ]
    return D3D10_INPUT_ELEMENT_DESC
D3D10_MAP = Int32
D3D10_MAP_READ = 1
D3D10_MAP_WRITE = 2
D3D10_MAP_READ_WRITE = 3
D3D10_MAP_WRITE_DISCARD = 4
D3D10_MAP_WRITE_NO_OVERWRITE = 5
D3D10_MAP_FLAG = Int32
D3D10_MAP_FLAG_DO_NOT_WAIT = 1048576
def _define_D3D10_MAPPED_TEXTURE2D_head():
    class D3D10_MAPPED_TEXTURE2D(Structure):
        pass
    return D3D10_MAPPED_TEXTURE2D
def _define_D3D10_MAPPED_TEXTURE2D():
    D3D10_MAPPED_TEXTURE2D = win32more.Graphics.Direct3D10.D3D10_MAPPED_TEXTURE2D_head
    D3D10_MAPPED_TEXTURE2D._fields_ = [
        ('pData', c_void_p),
        ('RowPitch', UInt32),
    ]
    return D3D10_MAPPED_TEXTURE2D
def _define_D3D10_MAPPED_TEXTURE3D_head():
    class D3D10_MAPPED_TEXTURE3D(Structure):
        pass
    return D3D10_MAPPED_TEXTURE3D
def _define_D3D10_MAPPED_TEXTURE3D():
    D3D10_MAPPED_TEXTURE3D = win32more.Graphics.Direct3D10.D3D10_MAPPED_TEXTURE3D_head
    D3D10_MAPPED_TEXTURE3D._fields_ = [
        ('pData', c_void_p),
        ('RowPitch', UInt32),
        ('DepthPitch', UInt32),
    ]
    return D3D10_MAPPED_TEXTURE3D
def _define_D3D10_MESSAGE_head():
    class D3D10_MESSAGE(Structure):
        pass
    return D3D10_MESSAGE
def _define_D3D10_MESSAGE():
    D3D10_MESSAGE = win32more.Graphics.Direct3D10.D3D10_MESSAGE_head
    D3D10_MESSAGE._fields_ = [
        ('Category', win32more.Graphics.Direct3D10.D3D10_MESSAGE_CATEGORY),
        ('Severity', win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY),
        ('ID', win32more.Graphics.Direct3D10.D3D10_MESSAGE_ID),
        ('pDescription', c_char_p_no),
        ('DescriptionByteLength', UIntPtr),
    ]
    return D3D10_MESSAGE
D3D10_MESSAGE_CATEGORY = Int32
D3D10_MESSAGE_CATEGORY_APPLICATION_DEFINED = 0
D3D10_MESSAGE_CATEGORY_MISCELLANEOUS = 1
D3D10_MESSAGE_CATEGORY_INITIALIZATION = 2
D3D10_MESSAGE_CATEGORY_CLEANUP = 3
D3D10_MESSAGE_CATEGORY_COMPILATION = 4
D3D10_MESSAGE_CATEGORY_STATE_CREATION = 5
D3D10_MESSAGE_CATEGORY_STATE_SETTING = 6
D3D10_MESSAGE_CATEGORY_STATE_GETTING = 7
D3D10_MESSAGE_CATEGORY_RESOURCE_MANIPULATION = 8
D3D10_MESSAGE_CATEGORY_EXECUTION = 9
D3D10_MESSAGE_CATEGORY_SHADER = 10
D3D10_MESSAGE_ID = Int32
D3D10_MESSAGE_ID_UNKNOWN = 0
D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_HAZARD = 1
D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_HAZARD = 2
D3D10_MESSAGE_ID_DEVICE_VSSETSHADERRESOURCES_HAZARD = 3
D3D10_MESSAGE_ID_DEVICE_VSSETCONSTANTBUFFERS_HAZARD = 4
D3D10_MESSAGE_ID_DEVICE_GSSETSHADERRESOURCES_HAZARD = 5
D3D10_MESSAGE_ID_DEVICE_GSSETCONSTANTBUFFERS_HAZARD = 6
D3D10_MESSAGE_ID_DEVICE_PSSETSHADERRESOURCES_HAZARD = 7
D3D10_MESSAGE_ID_DEVICE_PSSETCONSTANTBUFFERS_HAZARD = 8
D3D10_MESSAGE_ID_DEVICE_OMSETRENDERTARGETS_HAZARD = 9
D3D10_MESSAGE_ID_DEVICE_SOSETTARGETS_HAZARD = 10
D3D10_MESSAGE_ID_STRING_FROM_APPLICATION = 11
D3D10_MESSAGE_ID_CORRUPTED_THIS = 12
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER1 = 13
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER2 = 14
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER3 = 15
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER4 = 16
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER5 = 17
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER6 = 18
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER7 = 19
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER8 = 20
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER9 = 21
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER10 = 22
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER11 = 23
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER12 = 24
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER13 = 25
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER14 = 26
D3D10_MESSAGE_ID_CORRUPTED_PARAMETER15 = 27
D3D10_MESSAGE_ID_CORRUPTED_MULTITHREADING = 28
D3D10_MESSAGE_ID_MESSAGE_REPORTING_OUTOFMEMORY = 29
D3D10_MESSAGE_ID_IASETINPUTLAYOUT_UNBINDDELETINGOBJECT = 30
D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_UNBINDDELETINGOBJECT = 31
D3D10_MESSAGE_ID_IASETINDEXBUFFER_UNBINDDELETINGOBJECT = 32
D3D10_MESSAGE_ID_VSSETSHADER_UNBINDDELETINGOBJECT = 33
D3D10_MESSAGE_ID_VSSETSHADERRESOURCES_UNBINDDELETINGOBJECT = 34
D3D10_MESSAGE_ID_VSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT = 35
D3D10_MESSAGE_ID_VSSETSAMPLERS_UNBINDDELETINGOBJECT = 36
D3D10_MESSAGE_ID_GSSETSHADER_UNBINDDELETINGOBJECT = 37
D3D10_MESSAGE_ID_GSSETSHADERRESOURCES_UNBINDDELETINGOBJECT = 38
D3D10_MESSAGE_ID_GSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT = 39
D3D10_MESSAGE_ID_GSSETSAMPLERS_UNBINDDELETINGOBJECT = 40
D3D10_MESSAGE_ID_SOSETTARGETS_UNBINDDELETINGOBJECT = 41
D3D10_MESSAGE_ID_PSSETSHADER_UNBINDDELETINGOBJECT = 42
D3D10_MESSAGE_ID_PSSETSHADERRESOURCES_UNBINDDELETINGOBJECT = 43
D3D10_MESSAGE_ID_PSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT = 44
D3D10_MESSAGE_ID_PSSETSAMPLERS_UNBINDDELETINGOBJECT = 45
D3D10_MESSAGE_ID_RSSETSTATE_UNBINDDELETINGOBJECT = 46
D3D10_MESSAGE_ID_OMSETBLENDSTATE_UNBINDDELETINGOBJECT = 47
D3D10_MESSAGE_ID_OMSETDEPTHSTENCILSTATE_UNBINDDELETINGOBJECT = 48
D3D10_MESSAGE_ID_OMSETRENDERTARGETS_UNBINDDELETINGOBJECT = 49
D3D10_MESSAGE_ID_SETPREDICATION_UNBINDDELETINGOBJECT = 50
D3D10_MESSAGE_ID_GETPRIVATEDATA_MOREDATA = 51
D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDFREEDATA = 52
D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDIUNKNOWN = 53
D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDFLAGS = 54
D3D10_MESSAGE_ID_SETPRIVATEDATA_CHANGINGPARAMS = 55
D3D10_MESSAGE_ID_SETPRIVATEDATA_OUTOFMEMORY = 56
D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDFORMAT = 57
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDSAMPLES = 58
D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDUSAGE = 59
D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDBINDFLAGS = 60
D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDCPUACCESSFLAGS = 61
D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDMISCFLAGS = 62
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDCPUACCESSFLAGS = 63
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDBINDFLAGS = 64
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDINITIALDATA = 65
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDDIMENSIONS = 66
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDMIPLEVELS = 67
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDMISCFLAGS = 68
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDARG_RETURN = 69
D3D10_MESSAGE_ID_CREATEBUFFER_OUTOFMEMORY_RETURN = 70
D3D10_MESSAGE_ID_CREATEBUFFER_NULLDESC = 71
D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDCONSTANTBUFFERBINDINGS = 72
D3D10_MESSAGE_ID_CREATEBUFFER_LARGEALLOCATION = 73
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDFORMAT = 74
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNSUPPORTEDFORMAT = 75
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDSAMPLES = 76
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDUSAGE = 77
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDBINDFLAGS = 78
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDCPUACCESSFLAGS = 79
D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDMISCFLAGS = 80
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDCPUACCESSFLAGS = 81
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDBINDFLAGS = 82
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDINITIALDATA = 83
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDDIMENSIONS = 84
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDMIPLEVELS = 85
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDMISCFLAGS = 86
D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDARG_RETURN = 87
D3D10_MESSAGE_ID_CREATETEXTURE1D_OUTOFMEMORY_RETURN = 88
D3D10_MESSAGE_ID_CREATETEXTURE1D_NULLDESC = 89
D3D10_MESSAGE_ID_CREATETEXTURE1D_LARGEALLOCATION = 90
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDFORMAT = 91
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNSUPPORTEDFORMAT = 92
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDSAMPLES = 93
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDUSAGE = 94
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDBINDFLAGS = 95
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDCPUACCESSFLAGS = 96
D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDMISCFLAGS = 97
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDCPUACCESSFLAGS = 98
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDBINDFLAGS = 99
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDINITIALDATA = 100
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDDIMENSIONS = 101
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDMIPLEVELS = 102
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDMISCFLAGS = 103
D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDARG_RETURN = 104
D3D10_MESSAGE_ID_CREATETEXTURE2D_OUTOFMEMORY_RETURN = 105
D3D10_MESSAGE_ID_CREATETEXTURE2D_NULLDESC = 106
D3D10_MESSAGE_ID_CREATETEXTURE2D_LARGEALLOCATION = 107
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDFORMAT = 108
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNSUPPORTEDFORMAT = 109
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDSAMPLES = 110
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDUSAGE = 111
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDBINDFLAGS = 112
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDCPUACCESSFLAGS = 113
D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDMISCFLAGS = 114
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDCPUACCESSFLAGS = 115
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDBINDFLAGS = 116
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDINITIALDATA = 117
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDDIMENSIONS = 118
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDMIPLEVELS = 119
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDMISCFLAGS = 120
D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDARG_RETURN = 121
D3D10_MESSAGE_ID_CREATETEXTURE3D_OUTOFMEMORY_RETURN = 122
D3D10_MESSAGE_ID_CREATETEXTURE3D_NULLDESC = 123
D3D10_MESSAGE_ID_CREATETEXTURE3D_LARGEALLOCATION = 124
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_UNRECOGNIZEDFORMAT = 125
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDDESC = 126
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDFORMAT = 127
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDDIMENSIONS = 128
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDRESOURCE = 129
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_TOOMANYOBJECTS = 130
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDARG_RETURN = 131
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_OUTOFMEMORY_RETURN = 132
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_UNRECOGNIZEDFORMAT = 133
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_UNSUPPORTEDFORMAT = 134
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDDESC = 135
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDFORMAT = 136
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDDIMENSIONS = 137
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDRESOURCE = 138
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_TOOMANYOBJECTS = 139
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDARG_RETURN = 140
D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_OUTOFMEMORY_RETURN = 141
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_UNRECOGNIZEDFORMAT = 142
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDDESC = 143
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDFORMAT = 144
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDDIMENSIONS = 145
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDRESOURCE = 146
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_TOOMANYOBJECTS = 147
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDARG_RETURN = 148
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_OUTOFMEMORY_RETURN = 149
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_OUTOFMEMORY = 150
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TOOMANYELEMENTS = 151
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDFORMAT = 152
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INCOMPATIBLEFORMAT = 153
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSLOT = 154
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDINPUTSLOTCLASS = 155
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_STEPRATESLOTCLASSMISMATCH = 156
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSLOTCLASSCHANGE = 157
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSTEPRATECHANGE = 158
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDALIGNMENT = 159
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_DUPLICATESEMANTIC = 160
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_UNPARSEABLEINPUTSIGNATURE = 161
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_NULLSEMANTIC = 162
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_MISSINGELEMENT = 163
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_NULLDESC = 164
D3D10_MESSAGE_ID_CREATEVERTEXSHADER_OUTOFMEMORY = 165
D3D10_MESSAGE_ID_CREATEVERTEXSHADER_INVALIDSHADERBYTECODE = 166
D3D10_MESSAGE_ID_CREATEVERTEXSHADER_INVALIDSHADERTYPE = 167
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_OUTOFMEMORY = 168
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_INVALIDSHADERBYTECODE = 169
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_INVALIDSHADERTYPE = 170
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTOFMEMORY = 171
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSHADERBYTECODE = 172
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSHADERTYPE = 173
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDNUMENTRIES = 174
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTPUTSTREAMSTRIDEUNUSED = 175
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_UNEXPECTEDDECL = 176
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_EXPECTEDDECL = 177
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTPUTSLOT0EXPECTED = 178
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDOUTPUTSLOT = 179
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_ONLYONEELEMENTPERSLOT = 180
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDCOMPONENTCOUNT = 181
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSTARTCOMPONENTANDCOMPONENTCOUNT = 182
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDGAPDEFINITION = 183
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_REPEATEDOUTPUT = 184
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDOUTPUTSTREAMSTRIDE = 185
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MISSINGSEMANTIC = 186
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MASKMISMATCH = 187
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_CANTHAVEONLYGAPS = 188
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_DECLTOOCOMPLEX = 189
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MISSINGOUTPUTSIGNATURE = 190
D3D10_MESSAGE_ID_CREATEPIXELSHADER_OUTOFMEMORY = 191
D3D10_MESSAGE_ID_CREATEPIXELSHADER_INVALIDSHADERBYTECODE = 192
D3D10_MESSAGE_ID_CREATEPIXELSHADER_INVALIDSHADERTYPE = 193
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDFILLMODE = 194
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDCULLMODE = 195
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDDEPTHBIASCLAMP = 196
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDSLOPESCALEDDEPTHBIAS = 197
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_TOOMANYOBJECTS = 198
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_NULLDESC = 199
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDDEPTHWRITEMASK = 200
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDDEPTHFUNC = 201
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILFAILOP = 202
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILZFAILOP = 203
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILPASSOP = 204
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILFUNC = 205
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILFAILOP = 206
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILZFAILOP = 207
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILPASSOP = 208
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILFUNC = 209
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_TOOMANYOBJECTS = 210
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_NULLDESC = 211
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDSRCBLEND = 212
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDDESTBLEND = 213
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDBLENDOP = 214
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDSRCBLENDALPHA = 215
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDDESTBLENDALPHA = 216
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDBLENDOPALPHA = 217
D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDRENDERTARGETWRITEMASK = 218
D3D10_MESSAGE_ID_CREATEBLENDSTATE_TOOMANYOBJECTS = 219
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NULLDESC = 220
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDFILTER = 221
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSU = 222
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSV = 223
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSW = 224
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMIPLODBIAS = 225
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMAXANISOTROPY = 226
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDCOMPARISONFUNC = 227
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMINLOD = 228
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMAXLOD = 229
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_TOOMANYOBJECTS = 230
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NULLDESC = 231
D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_INVALIDQUERY = 232
D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_INVALIDMISCFLAGS = 233
D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_UNEXPECTEDMISCFLAG = 234
D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_NULLDESC = 235
D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_TOPOLOGY_UNRECOGNIZED = 236
D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_TOPOLOGY_UNDEFINED = 237
D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_INVALIDBUFFER = 238
D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_OFFSET_TOO_LARGE = 239
D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_BUFFERS_EMPTY = 240
D3D10_MESSAGE_ID_IASETINDEXBUFFER_INVALIDBUFFER = 241
D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_FORMAT_INVALID = 242
D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_OFFSET_TOO_LARGE = 243
D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_OFFSET_UNALIGNED = 244
D3D10_MESSAGE_ID_DEVICE_VSSETSHADERRESOURCES_VIEWS_EMPTY = 245
D3D10_MESSAGE_ID_VSSETCONSTANTBUFFERS_INVALIDBUFFER = 246
D3D10_MESSAGE_ID_DEVICE_VSSETCONSTANTBUFFERS_BUFFERS_EMPTY = 247
D3D10_MESSAGE_ID_DEVICE_VSSETSAMPLERS_SAMPLERS_EMPTY = 248
D3D10_MESSAGE_ID_DEVICE_GSSETSHADERRESOURCES_VIEWS_EMPTY = 249
D3D10_MESSAGE_ID_GSSETCONSTANTBUFFERS_INVALIDBUFFER = 250
D3D10_MESSAGE_ID_DEVICE_GSSETCONSTANTBUFFERS_BUFFERS_EMPTY = 251
D3D10_MESSAGE_ID_DEVICE_GSSETSAMPLERS_SAMPLERS_EMPTY = 252
D3D10_MESSAGE_ID_SOSETTARGETS_INVALIDBUFFER = 253
D3D10_MESSAGE_ID_DEVICE_SOSETTARGETS_OFFSET_UNALIGNED = 254
D3D10_MESSAGE_ID_DEVICE_PSSETSHADERRESOURCES_VIEWS_EMPTY = 255
D3D10_MESSAGE_ID_PSSETCONSTANTBUFFERS_INVALIDBUFFER = 256
D3D10_MESSAGE_ID_DEVICE_PSSETCONSTANTBUFFERS_BUFFERS_EMPTY = 257
D3D10_MESSAGE_ID_DEVICE_PSSETSAMPLERS_SAMPLERS_EMPTY = 258
D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_INVALIDVIEWPORT = 259
D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_INVALIDSCISSOR = 260
D3D10_MESSAGE_ID_CLEARRENDERTARGETVIEW_DENORMFLUSH = 261
D3D10_MESSAGE_ID_CLEARDEPTHSTENCILVIEW_DENORMFLUSH = 262
D3D10_MESSAGE_ID_CLEARDEPTHSTENCILVIEW_INVALID = 263
D3D10_MESSAGE_ID_DEVICE_IAGETVERTEXBUFFERS_BUFFERS_EMPTY = 264
D3D10_MESSAGE_ID_DEVICE_VSGETSHADERRESOURCES_VIEWS_EMPTY = 265
D3D10_MESSAGE_ID_DEVICE_VSGETCONSTANTBUFFERS_BUFFERS_EMPTY = 266
D3D10_MESSAGE_ID_DEVICE_VSGETSAMPLERS_SAMPLERS_EMPTY = 267
D3D10_MESSAGE_ID_DEVICE_GSGETSHADERRESOURCES_VIEWS_EMPTY = 268
D3D10_MESSAGE_ID_DEVICE_GSGETCONSTANTBUFFERS_BUFFERS_EMPTY = 269
D3D10_MESSAGE_ID_DEVICE_GSGETSAMPLERS_SAMPLERS_EMPTY = 270
D3D10_MESSAGE_ID_DEVICE_SOGETTARGETS_BUFFERS_EMPTY = 271
D3D10_MESSAGE_ID_DEVICE_PSGETSHADERRESOURCES_VIEWS_EMPTY = 272
D3D10_MESSAGE_ID_DEVICE_PSGETCONSTANTBUFFERS_BUFFERS_EMPTY = 273
D3D10_MESSAGE_ID_DEVICE_PSGETSAMPLERS_SAMPLERS_EMPTY = 274
D3D10_MESSAGE_ID_DEVICE_RSGETVIEWPORTS_VIEWPORTS_EMPTY = 275
D3D10_MESSAGE_ID_DEVICE_RSGETSCISSORRECTS_RECTS_EMPTY = 276
D3D10_MESSAGE_ID_DEVICE_GENERATEMIPS_RESOURCE_INVALID = 277
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDDESTINATIONSUBRESOURCE = 278
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCESUBRESOURCE = 279
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCEBOX = 280
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCE = 281
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDDESTINATIONSTATE = 282
D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCESTATE = 283
D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDSOURCE = 284
D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDDESTINATIONSTATE = 285
D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDSOURCESTATE = 286
D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONSUBRESOURCE = 287
D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONBOX = 288
D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONSTATE = 289
D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_DESTINATION_INVALID = 290
D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_DESTINATION_SUBRESOURCE_INVALID = 291
D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_SOURCE_INVALID = 292
D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_SOURCE_SUBRESOURCE_INVALID = 293
D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_FORMAT_INVALID = 294
D3D10_MESSAGE_ID_BUFFER_MAP_INVALIDMAPTYPE = 295
D3D10_MESSAGE_ID_BUFFER_MAP_INVALIDFLAGS = 296
D3D10_MESSAGE_ID_BUFFER_MAP_ALREADYMAPPED = 297
D3D10_MESSAGE_ID_BUFFER_MAP_DEVICEREMOVED_RETURN = 298
D3D10_MESSAGE_ID_BUFFER_UNMAP_NOTMAPPED = 299
D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDMAPTYPE = 300
D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDSUBRESOURCE = 301
D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDFLAGS = 302
D3D10_MESSAGE_ID_TEXTURE1D_MAP_ALREADYMAPPED = 303
D3D10_MESSAGE_ID_TEXTURE1D_MAP_DEVICEREMOVED_RETURN = 304
D3D10_MESSAGE_ID_TEXTURE1D_UNMAP_INVALIDSUBRESOURCE = 305
D3D10_MESSAGE_ID_TEXTURE1D_UNMAP_NOTMAPPED = 306
D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDMAPTYPE = 307
D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDSUBRESOURCE = 308
D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDFLAGS = 309
D3D10_MESSAGE_ID_TEXTURE2D_MAP_ALREADYMAPPED = 310
D3D10_MESSAGE_ID_TEXTURE2D_MAP_DEVICEREMOVED_RETURN = 311
D3D10_MESSAGE_ID_TEXTURE2D_UNMAP_INVALIDSUBRESOURCE = 312
D3D10_MESSAGE_ID_TEXTURE2D_UNMAP_NOTMAPPED = 313
D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDMAPTYPE = 314
D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDSUBRESOURCE = 315
D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDFLAGS = 316
D3D10_MESSAGE_ID_TEXTURE3D_MAP_ALREADYMAPPED = 317
D3D10_MESSAGE_ID_TEXTURE3D_MAP_DEVICEREMOVED_RETURN = 318
D3D10_MESSAGE_ID_TEXTURE3D_UNMAP_INVALIDSUBRESOURCE = 319
D3D10_MESSAGE_ID_TEXTURE3D_UNMAP_NOTMAPPED = 320
D3D10_MESSAGE_ID_CHECKFORMATSUPPORT_FORMAT_DEPRECATED = 321
D3D10_MESSAGE_ID_CHECKMULTISAMPLEQUALITYLEVELS_FORMAT_DEPRECATED = 322
D3D10_MESSAGE_ID_SETEXCEPTIONMODE_UNRECOGNIZEDFLAGS = 323
D3D10_MESSAGE_ID_SETEXCEPTIONMODE_INVALIDARG_RETURN = 324
D3D10_MESSAGE_ID_SETEXCEPTIONMODE_DEVICEREMOVED_RETURN = 325
D3D10_MESSAGE_ID_REF_SIMULATING_INFINITELY_FAST_HARDWARE = 326
D3D10_MESSAGE_ID_REF_THREADING_MODE = 327
D3D10_MESSAGE_ID_REF_UMDRIVER_EXCEPTION = 328
D3D10_MESSAGE_ID_REF_KMDRIVER_EXCEPTION = 329
D3D10_MESSAGE_ID_REF_HARDWARE_EXCEPTION = 330
D3D10_MESSAGE_ID_REF_ACCESSING_INDEXABLE_TEMP_OUT_OF_RANGE = 331
D3D10_MESSAGE_ID_REF_PROBLEM_PARSING_SHADER = 332
D3D10_MESSAGE_ID_REF_OUT_OF_MEMORY = 333
D3D10_MESSAGE_ID_REF_INFO = 334
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEXPOS_OVERFLOW = 335
D3D10_MESSAGE_ID_DEVICE_DRAWINDEXED_INDEXPOS_OVERFLOW = 336
D3D10_MESSAGE_ID_DEVICE_DRAWINSTANCED_VERTEXPOS_OVERFLOW = 337
D3D10_MESSAGE_ID_DEVICE_DRAWINSTANCED_INSTANCEPOS_OVERFLOW = 338
D3D10_MESSAGE_ID_DEVICE_DRAWINDEXEDINSTANCED_INSTANCEPOS_OVERFLOW = 339
D3D10_MESSAGE_ID_DEVICE_DRAWINDEXEDINSTANCED_INDEXPOS_OVERFLOW = 340
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_SHADER_NOT_SET = 341
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_SEMANTICNAME_NOT_FOUND = 342
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_REGISTERINDEX = 343
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_COMPONENTTYPE = 344
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_REGISTERMASK = 345
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_SYSTEMVALUE = 346
D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_NEVERWRITTEN_ALWAYSREADS = 347
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_NOT_SET = 348
D3D10_MESSAGE_ID_DEVICE_DRAW_INPUTLAYOUT_NOT_SET = 349
D3D10_MESSAGE_ID_DEVICE_DRAW_CONSTANT_BUFFER_NOT_SET = 350
D3D10_MESSAGE_ID_DEVICE_DRAW_CONSTANT_BUFFER_TOO_SMALL = 351
D3D10_MESSAGE_ID_DEVICE_DRAW_SAMPLER_NOT_SET = 352
D3D10_MESSAGE_ID_DEVICE_DRAW_SHADERRESOURCEVIEW_NOT_SET = 353
D3D10_MESSAGE_ID_DEVICE_DRAW_VIEW_DIMENSION_MISMATCH = 354
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_STRIDE_TOO_SMALL = 355
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_TOO_SMALL = 356
D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_NOT_SET = 357
D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_FORMAT_INVALID = 358
D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_TOO_SMALL = 359
D3D10_MESSAGE_ID_DEVICE_DRAW_GS_INPUT_PRIMITIVE_MISMATCH = 360
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_RETURN_TYPE_MISMATCH = 361
D3D10_MESSAGE_ID_DEVICE_DRAW_POSITION_NOT_PRESENT = 362
D3D10_MESSAGE_ID_DEVICE_DRAW_OUTPUT_STREAM_NOT_SET = 363
D3D10_MESSAGE_ID_DEVICE_DRAW_BOUND_RESOURCE_MAPPED = 364
D3D10_MESSAGE_ID_DEVICE_DRAW_INVALID_PRIMITIVETOPOLOGY = 365
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_OFFSET_UNALIGNED = 366
D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_STRIDE_UNALIGNED = 367
D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_OFFSET_UNALIGNED = 368
D3D10_MESSAGE_ID_DEVICE_DRAW_OUTPUT_STREAM_OFFSET_UNALIGNED = 369
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_LD_UNSUPPORTED = 370
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_SAMPLE_UNSUPPORTED = 371
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_SAMPLE_C_UNSUPPORTED = 372
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_MULTISAMPLE_UNSUPPORTED = 373
D3D10_MESSAGE_ID_DEVICE_DRAW_SO_TARGETS_BOUND_WITHOUT_SOURCE = 374
D3D10_MESSAGE_ID_DEVICE_DRAW_SO_STRIDE_LARGER_THAN_BUFFER = 375
D3D10_MESSAGE_ID_DEVICE_DRAW_OM_RENDER_TARGET_DOES_NOT_SUPPORT_BLENDING = 376
D3D10_MESSAGE_ID_DEVICE_DRAW_OM_DUAL_SOURCE_BLENDING_CAN_ONLY_HAVE_RENDER_TARGET_0 = 377
D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_AT_FAULT = 378
D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_POSSIBLY_AT_FAULT = 379
D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_NOT_AT_FAULT = 380
D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_INVALIDARG_RETURN = 381
D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_OUTOFMEMORY_RETURN = 382
D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_BADINTERFACE_RETURN = 383
D3D10_MESSAGE_ID_DEVICE_DRAW_VIEWPORT_NOT_SET = 384
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TRAILING_DIGIT_IN_SEMANTIC = 385
D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_TRAILING_DIGIT_IN_SEMANTIC = 386
D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_DENORMFLUSH = 387
D3D10_MESSAGE_ID_OMSETRENDERTARGETS_INVALIDVIEW = 388
D3D10_MESSAGE_ID_DEVICE_SETTEXTFILTERSIZE_INVALIDDIMENSIONS = 389
D3D10_MESSAGE_ID_DEVICE_DRAW_SAMPLER_MISMATCH = 390
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TYPE_MISMATCH = 391
D3D10_MESSAGE_ID_BLENDSTATE_GETDESC_LEGACY = 392
D3D10_MESSAGE_ID_SHADERRESOURCEVIEW_GETDESC_LEGACY = 393
D3D10_MESSAGE_ID_CREATEQUERY_OUTOFMEMORY_RETURN = 394
D3D10_MESSAGE_ID_CREATEPREDICATE_OUTOFMEMORY_RETURN = 395
D3D10_MESSAGE_ID_CREATECOUNTER_OUTOFRANGE_COUNTER = 396
D3D10_MESSAGE_ID_CREATECOUNTER_SIMULTANEOUS_ACTIVE_COUNTERS_EXHAUSTED = 397
D3D10_MESSAGE_ID_CREATECOUNTER_UNSUPPORTED_WELLKNOWN_COUNTER = 398
D3D10_MESSAGE_ID_CREATECOUNTER_OUTOFMEMORY_RETURN = 399
D3D10_MESSAGE_ID_CREATECOUNTER_NONEXCLUSIVE_RETURN = 400
D3D10_MESSAGE_ID_CREATECOUNTER_NULLDESC = 401
D3D10_MESSAGE_ID_CHECKCOUNTER_OUTOFRANGE_COUNTER = 402
D3D10_MESSAGE_ID_CHECKCOUNTER_UNSUPPORTED_WELLKNOWN_COUNTER = 403
D3D10_MESSAGE_ID_SETPREDICATION_INVALID_PREDICATE_STATE = 404
D3D10_MESSAGE_ID_QUERY_BEGIN_UNSUPPORTED = 405
D3D10_MESSAGE_ID_PREDICATE_BEGIN_DURING_PREDICATION = 406
D3D10_MESSAGE_ID_QUERY_BEGIN_DUPLICATE = 407
D3D10_MESSAGE_ID_QUERY_BEGIN_ABANDONING_PREVIOUS_RESULTS = 408
D3D10_MESSAGE_ID_PREDICATE_END_DURING_PREDICATION = 409
D3D10_MESSAGE_ID_QUERY_END_ABANDONING_PREVIOUS_RESULTS = 410
D3D10_MESSAGE_ID_QUERY_END_WITHOUT_BEGIN = 411
D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_DATASIZE = 412
D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_FLAGS = 413
D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_CALL = 414
D3D10_MESSAGE_ID_DEVICE_DRAW_PS_OUTPUT_TYPE_MISMATCH = 415
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_GATHER_UNSUPPORTED = 416
D3D10_MESSAGE_ID_DEVICE_DRAW_INVALID_USE_OF_CENTER_MULTISAMPLE_PATTERN = 417
D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_STRIDE_TOO_LARGE = 418
D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_INVALIDRANGE = 419
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_EMPTY_LAYOUT = 420
D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_SAMPLE_COUNT_MISMATCH = 421
D3D10_MESSAGE_ID_LIVE_OBJECT_SUMMARY = 422
D3D10_MESSAGE_ID_LIVE_BUFFER = 423
D3D10_MESSAGE_ID_LIVE_TEXTURE1D = 424
D3D10_MESSAGE_ID_LIVE_TEXTURE2D = 425
D3D10_MESSAGE_ID_LIVE_TEXTURE3D = 426
D3D10_MESSAGE_ID_LIVE_SHADERRESOURCEVIEW = 427
D3D10_MESSAGE_ID_LIVE_RENDERTARGETVIEW = 428
D3D10_MESSAGE_ID_LIVE_DEPTHSTENCILVIEW = 429
D3D10_MESSAGE_ID_LIVE_VERTEXSHADER = 430
D3D10_MESSAGE_ID_LIVE_GEOMETRYSHADER = 431
D3D10_MESSAGE_ID_LIVE_PIXELSHADER = 432
D3D10_MESSAGE_ID_LIVE_INPUTLAYOUT = 433
D3D10_MESSAGE_ID_LIVE_SAMPLER = 434
D3D10_MESSAGE_ID_LIVE_BLENDSTATE = 435
D3D10_MESSAGE_ID_LIVE_DEPTHSTENCILSTATE = 436
D3D10_MESSAGE_ID_LIVE_RASTERIZERSTATE = 437
D3D10_MESSAGE_ID_LIVE_QUERY = 438
D3D10_MESSAGE_ID_LIVE_PREDICATE = 439
D3D10_MESSAGE_ID_LIVE_COUNTER = 440
D3D10_MESSAGE_ID_LIVE_DEVICE = 441
D3D10_MESSAGE_ID_LIVE_SWAPCHAIN = 442
D3D10_MESSAGE_ID_D3D10_MESSAGES_END = 443
D3D10_MESSAGE_ID_D3D10L9_MESSAGES_START = 1048576
D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_STENCIL_NO_TWO_SIDED = 1048577
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_DepthBiasClamp_NOT_SUPPORTED = 1048578
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NO_COMPARISON_SUPPORT = 1048579
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_EXCESSIVE_ANISOTROPY = 1048580
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_BORDER_OUT_OF_RANGE = 1048581
D3D10_MESSAGE_ID_VSSETSAMPLERS_NOT_SUPPORTED = 1048582
D3D10_MESSAGE_ID_VSSETSAMPLERS_TOO_MANY_SAMPLERS = 1048583
D3D10_MESSAGE_ID_PSSETSAMPLERS_TOO_MANY_SAMPLERS = 1048584
D3D10_MESSAGE_ID_CREATERESOURCE_NO_ARRAYS = 1048585
D3D10_MESSAGE_ID_CREATERESOURCE_NO_VB_AND_IB_BIND = 1048586
D3D10_MESSAGE_ID_CREATERESOURCE_NO_TEXTURE_1D = 1048587
D3D10_MESSAGE_ID_CREATERESOURCE_DIMENSION_OUT_OF_RANGE = 1048588
D3D10_MESSAGE_ID_CREATERESOURCE_NOT_BINDABLE_AS_SHADER_RESOURCE = 1048589
D3D10_MESSAGE_ID_OMSETRENDERTARGETS_TOO_MANY_RENDER_TARGETS = 1048590
D3D10_MESSAGE_ID_OMSETRENDERTARGETS_NO_DIFFERING_BIT_DEPTHS = 1048591
D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_BAD_BUFFER_INDEX = 1048592
D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_TOO_MANY_VIEWPORTS = 1048593
D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_ADJACENCY_UNSUPPORTED = 1048594
D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_TOO_MANY_SCISSORS = 1048595
D3D10_MESSAGE_ID_COPYRESOURCE_ONLY_TEXTURE_2D_WITHIN_GPU_MEMORY = 1048596
D3D10_MESSAGE_ID_COPYRESOURCE_NO_TEXTURE_3D_READBACK = 1048597
D3D10_MESSAGE_ID_COPYRESOURCE_NO_TEXTURE_ONLY_READBACK = 1048598
D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_UNSUPPORTED_FORMAT = 1048599
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_ALPHA_TO_COVERAGE = 1048600
D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_DepthClipEnable_MUST_BE_TRUE = 1048601
D3D10_MESSAGE_ID_DRAWINDEXED_STARTINDEXLOCATION_MUST_BE_POSITIVE = 1048602
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_MUST_USE_LOWEST_LOD = 1048603
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_MINLOD_MUST_NOT_BE_FRACTIONAL = 1048604
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_MAXLOD_MUST_BE_FLT_MAX = 1048605
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_FIRSTARRAYSLICE_MUST_BE_ZERO = 1048606
D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_CUBES_MUST_HAVE_6_SIDES = 1048607
D3D10_MESSAGE_ID_CREATERESOURCE_NOT_BINDABLE_AS_RENDER_TARGET = 1048608
D3D10_MESSAGE_ID_CREATERESOURCE_NO_DWORD_INDEX_BUFFER = 1048609
D3D10_MESSAGE_ID_CREATERESOURCE_MSAA_PRECLUDES_SHADER_RESOURCE = 1048610
D3D10_MESSAGE_ID_CREATERESOURCE_PRESENTATION_PRECLUDES_SHADER_RESOURCE = 1048611
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_INDEPENDENT_BLEND_ENABLE = 1048612
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_INDEPENDENT_WRITE_MASKS = 1048613
D3D10_MESSAGE_ID_CREATERESOURCE_NO_STREAM_OUT = 1048614
D3D10_MESSAGE_ID_CREATERESOURCE_ONLY_VB_IB_FOR_BUFFERS = 1048615
D3D10_MESSAGE_ID_CREATERESOURCE_NO_AUTOGEN_FOR_VOLUMES = 1048616
D3D10_MESSAGE_ID_CREATERESOURCE_DXGI_FORMAT_R8G8B8A8_CANNOT_BE_SHARED = 1048617
D3D10_MESSAGE_ID_VSSHADERRESOURCES_NOT_SUPPORTED = 1048618
D3D10_MESSAGE_ID_GEOMETRY_SHADER_NOT_SUPPORTED = 1048619
D3D10_MESSAGE_ID_STREAM_OUT_NOT_SUPPORTED = 1048620
D3D10_MESSAGE_ID_TEXT_FILTER_NOT_SUPPORTED = 1048621
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_SEPARATE_ALPHA_BLEND = 1048622
D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_MRT_BLEND = 1048623
D3D10_MESSAGE_ID_CREATEBLENDSTATE_OPERATION_NOT_SUPPORTED = 1048624
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NO_MIRRORONCE = 1048625
D3D10_MESSAGE_ID_DRAWINSTANCED_NOT_SUPPORTED = 1048626
D3D10_MESSAGE_ID_DRAWINDEXEDINSTANCED_NOT_SUPPORTED_BELOW_9_3 = 1048627
D3D10_MESSAGE_ID_DRAWINDEXED_POINTLIST_UNSUPPORTED = 1048628
D3D10_MESSAGE_ID_SETBLENDSTATE_SAMPLE_MASK_CANNOT_BE_ZERO = 1048629
D3D10_MESSAGE_ID_CREATERESOURCE_DIMENSION_EXCEEDS_FEATURE_LEVEL_DEFINITION = 1048630
D3D10_MESSAGE_ID_CREATERESOURCE_ONLY_SINGLE_MIP_LEVEL_DEPTH_STENCIL_SUPPORTED = 1048631
D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_NEGATIVESCISSOR = 1048632
D3D10_MESSAGE_ID_SLOT_ZERO_MUST_BE_D3D10_INPUT_PER_VERTEX_DATA = 1048633
D3D10_MESSAGE_ID_CREATERESOURCE_NON_POW_2_MIPMAP = 1048634
D3D10_MESSAGE_ID_CREATESAMPLERSTATE_BORDER_NOT_SUPPORTED = 1048635
D3D10_MESSAGE_ID_OMSETRENDERTARGETS_NO_SRGB_MRT = 1048636
D3D10_MESSAGE_ID_COPYRESOURCE_NO_3D_MISMATCHED_UPDATES = 1048637
D3D10_MESSAGE_ID_D3D10L9_MESSAGES_END = 1048638
D3D10_MESSAGE_SEVERITY = Int32
D3D10_MESSAGE_SEVERITY_CORRUPTION = 0
D3D10_MESSAGE_SEVERITY_ERROR = 1
D3D10_MESSAGE_SEVERITY_WARNING = 2
D3D10_MESSAGE_SEVERITY_INFO = 3
D3D10_MESSAGE_SEVERITY_MESSAGE = 4
def _define_D3D10_PASS_DESC_head():
    class D3D10_PASS_DESC(Structure):
        pass
    return D3D10_PASS_DESC
def _define_D3D10_PASS_DESC():
    D3D10_PASS_DESC = win32more.Graphics.Direct3D10.D3D10_PASS_DESC_head
    D3D10_PASS_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Annotations', UInt32),
        ('pIAInputSignature', c_char_p_no),
        ('IAInputSignatureSize', UIntPtr),
        ('StencilRef', UInt32),
        ('SampleMask', UInt32),
        ('BlendFactor', Single * 4),
    ]
    return D3D10_PASS_DESC
def _define_D3D10_PASS_SHADER_DESC_head():
    class D3D10_PASS_SHADER_DESC(Structure):
        pass
    return D3D10_PASS_SHADER_DESC
def _define_D3D10_PASS_SHADER_DESC():
    D3D10_PASS_SHADER_DESC = win32more.Graphics.Direct3D10.D3D10_PASS_SHADER_DESC_head
    D3D10_PASS_SHADER_DESC._fields_ = [
        ('pShaderVariable', win32more.Graphics.Direct3D10.ID3D10EffectShaderVariable_head),
        ('ShaderIndex', UInt32),
    ]
    return D3D10_PASS_SHADER_DESC
D3D10_QUERY = Int32
D3D10_QUERY_EVENT = 0
D3D10_QUERY_OCCLUSION = 1
D3D10_QUERY_TIMESTAMP = 2
D3D10_QUERY_TIMESTAMP_DISJOINT = 3
D3D10_QUERY_PIPELINE_STATISTICS = 4
D3D10_QUERY_OCCLUSION_PREDICATE = 5
D3D10_QUERY_SO_STATISTICS = 6
D3D10_QUERY_SO_OVERFLOW_PREDICATE = 7
def _define_D3D10_QUERY_DATA_PIPELINE_STATISTICS_head():
    class D3D10_QUERY_DATA_PIPELINE_STATISTICS(Structure):
        pass
    return D3D10_QUERY_DATA_PIPELINE_STATISTICS
def _define_D3D10_QUERY_DATA_PIPELINE_STATISTICS():
    D3D10_QUERY_DATA_PIPELINE_STATISTICS = win32more.Graphics.Direct3D10.D3D10_QUERY_DATA_PIPELINE_STATISTICS_head
    D3D10_QUERY_DATA_PIPELINE_STATISTICS._fields_ = [
        ('IAVertices', UInt64),
        ('IAPrimitives', UInt64),
        ('VSInvocations', UInt64),
        ('GSInvocations', UInt64),
        ('GSPrimitives', UInt64),
        ('CInvocations', UInt64),
        ('CPrimitives', UInt64),
        ('PSInvocations', UInt64),
    ]
    return D3D10_QUERY_DATA_PIPELINE_STATISTICS
def _define_D3D10_QUERY_DATA_SO_STATISTICS_head():
    class D3D10_QUERY_DATA_SO_STATISTICS(Structure):
        pass
    return D3D10_QUERY_DATA_SO_STATISTICS
def _define_D3D10_QUERY_DATA_SO_STATISTICS():
    D3D10_QUERY_DATA_SO_STATISTICS = win32more.Graphics.Direct3D10.D3D10_QUERY_DATA_SO_STATISTICS_head
    D3D10_QUERY_DATA_SO_STATISTICS._fields_ = [
        ('NumPrimitivesWritten', UInt64),
        ('PrimitivesStorageNeeded', UInt64),
    ]
    return D3D10_QUERY_DATA_SO_STATISTICS
def _define_D3D10_QUERY_DATA_TIMESTAMP_DISJOINT_head():
    class D3D10_QUERY_DATA_TIMESTAMP_DISJOINT(Structure):
        pass
    return D3D10_QUERY_DATA_TIMESTAMP_DISJOINT
def _define_D3D10_QUERY_DATA_TIMESTAMP_DISJOINT():
    D3D10_QUERY_DATA_TIMESTAMP_DISJOINT = win32more.Graphics.Direct3D10.D3D10_QUERY_DATA_TIMESTAMP_DISJOINT_head
    D3D10_QUERY_DATA_TIMESTAMP_DISJOINT._fields_ = [
        ('Frequency', UInt64),
        ('Disjoint', win32more.Foundation.BOOL),
    ]
    return D3D10_QUERY_DATA_TIMESTAMP_DISJOINT
def _define_D3D10_QUERY_DESC_head():
    class D3D10_QUERY_DESC(Structure):
        pass
    return D3D10_QUERY_DESC
def _define_D3D10_QUERY_DESC():
    D3D10_QUERY_DESC = win32more.Graphics.Direct3D10.D3D10_QUERY_DESC_head
    D3D10_QUERY_DESC._fields_ = [
        ('Query', win32more.Graphics.Direct3D10.D3D10_QUERY),
        ('MiscFlags', UInt32),
    ]
    return D3D10_QUERY_DESC
D3D10_QUERY_MISC_FLAG = Int32
D3D10_QUERY_MISC_PREDICATEHINT = 1
D3D10_RAISE_FLAG = Int32
D3D10_RAISE_FLAG_DRIVER_INTERNAL_ERROR = 1
def _define_D3D10_RASTERIZER_DESC_head():
    class D3D10_RASTERIZER_DESC(Structure):
        pass
    return D3D10_RASTERIZER_DESC
def _define_D3D10_RASTERIZER_DESC():
    D3D10_RASTERIZER_DESC = win32more.Graphics.Direct3D10.D3D10_RASTERIZER_DESC_head
    D3D10_RASTERIZER_DESC._fields_ = [
        ('FillMode', win32more.Graphics.Direct3D10.D3D10_FILL_MODE),
        ('CullMode', win32more.Graphics.Direct3D10.D3D10_CULL_MODE),
        ('FrontCounterClockwise', win32more.Foundation.BOOL),
        ('DepthBias', Int32),
        ('DepthBiasClamp', Single),
        ('SlopeScaledDepthBias', Single),
        ('DepthClipEnable', win32more.Foundation.BOOL),
        ('ScissorEnable', win32more.Foundation.BOOL),
        ('MultisampleEnable', win32more.Foundation.BOOL),
        ('AntialiasedLineEnable', win32more.Foundation.BOOL),
    ]
    return D3D10_RASTERIZER_DESC
def _define_D3D10_RENDER_TARGET_BLEND_DESC1_head():
    class D3D10_RENDER_TARGET_BLEND_DESC1(Structure):
        pass
    return D3D10_RENDER_TARGET_BLEND_DESC1
def _define_D3D10_RENDER_TARGET_BLEND_DESC1():
    D3D10_RENDER_TARGET_BLEND_DESC1 = win32more.Graphics.Direct3D10.D3D10_RENDER_TARGET_BLEND_DESC1_head
    D3D10_RENDER_TARGET_BLEND_DESC1._fields_ = [
        ('BlendEnable', win32more.Foundation.BOOL),
        ('SrcBlend', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('DestBlend', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('BlendOp', win32more.Graphics.Direct3D10.D3D10_BLEND_OP),
        ('SrcBlendAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('DestBlendAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND),
        ('BlendOpAlpha', win32more.Graphics.Direct3D10.D3D10_BLEND_OP),
        ('RenderTargetWriteMask', Byte),
    ]
    return D3D10_RENDER_TARGET_BLEND_DESC1
def _define_D3D10_RENDER_TARGET_VIEW_DESC_head():
    class D3D10_RENDER_TARGET_VIEW_DESC(Structure):
        pass
    return D3D10_RENDER_TARGET_VIEW_DESC
def _define_D3D10_RENDER_TARGET_VIEW_DESC():
    D3D10_RENDER_TARGET_VIEW_DESC = win32more.Graphics.Direct3D10.D3D10_RENDER_TARGET_VIEW_DESC_head
    class D3D10_RENDER_TARGET_VIEW_DESC__Anonymous_e__Union(Union):
        pass
    D3D10_RENDER_TARGET_VIEW_DESC__Anonymous_e__Union._fields_ = [
        ('Buffer', win32more.Graphics.Direct3D10.D3D10_BUFFER_RTV),
        ('Texture1D', win32more.Graphics.Direct3D10.D3D10_TEX1D_RTV),
        ('Texture1DArray', win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_RTV),
        ('Texture2D', win32more.Graphics.Direct3D10.D3D10_TEX2D_RTV),
        ('Texture2DArray', win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_RTV),
        ('Texture2DMS', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_RTV),
        ('Texture2DMSArray', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_RTV),
        ('Texture3D', win32more.Graphics.Direct3D10.D3D10_TEX3D_RTV),
    ]
    D3D10_RENDER_TARGET_VIEW_DESC._anonymous_ = [
        'Anonymous',
    ]
    D3D10_RENDER_TARGET_VIEW_DESC._fields_ = [
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('ViewDimension', win32more.Graphics.Direct3D10.D3D10_RTV_DIMENSION),
        ('Anonymous', D3D10_RENDER_TARGET_VIEW_DESC__Anonymous_e__Union),
    ]
    return D3D10_RENDER_TARGET_VIEW_DESC
D3D10_RESOURCE_DIMENSION = Int32
D3D10_RESOURCE_DIMENSION_UNKNOWN = 0
D3D10_RESOURCE_DIMENSION_BUFFER = 1
D3D10_RESOURCE_DIMENSION_TEXTURE1D = 2
D3D10_RESOURCE_DIMENSION_TEXTURE2D = 3
D3D10_RESOURCE_DIMENSION_TEXTURE3D = 4
D3D10_RESOURCE_MISC_FLAG = Int32
D3D10_RESOURCE_MISC_GENERATE_MIPS = 1
D3D10_RESOURCE_MISC_SHARED = 2
D3D10_RESOURCE_MISC_TEXTURECUBE = 4
D3D10_RESOURCE_MISC_SHARED_KEYEDMUTEX = 16
D3D10_RESOURCE_MISC_GDI_COMPATIBLE = 32
D3D10_RTV_DIMENSION = Int32
D3D10_RTV_DIMENSION_UNKNOWN = 0
D3D10_RTV_DIMENSION_BUFFER = 1
D3D10_RTV_DIMENSION_TEXTURE1D = 2
D3D10_RTV_DIMENSION_TEXTURE1DARRAY = 3
D3D10_RTV_DIMENSION_TEXTURE2D = 4
D3D10_RTV_DIMENSION_TEXTURE2DARRAY = 5
D3D10_RTV_DIMENSION_TEXTURE2DMS = 6
D3D10_RTV_DIMENSION_TEXTURE2DMSARRAY = 7
D3D10_RTV_DIMENSION_TEXTURE3D = 8
def _define_D3D10_SAMPLER_DESC_head():
    class D3D10_SAMPLER_DESC(Structure):
        pass
    return D3D10_SAMPLER_DESC
def _define_D3D10_SAMPLER_DESC():
    D3D10_SAMPLER_DESC = win32more.Graphics.Direct3D10.D3D10_SAMPLER_DESC_head
    D3D10_SAMPLER_DESC._fields_ = [
        ('Filter', win32more.Graphics.Direct3D10.D3D10_FILTER),
        ('AddressU', win32more.Graphics.Direct3D10.D3D10_TEXTURE_ADDRESS_MODE),
        ('AddressV', win32more.Graphics.Direct3D10.D3D10_TEXTURE_ADDRESS_MODE),
        ('AddressW', win32more.Graphics.Direct3D10.D3D10_TEXTURE_ADDRESS_MODE),
        ('MipLODBias', Single),
        ('MaxAnisotropy', UInt32),
        ('ComparisonFunc', win32more.Graphics.Direct3D10.D3D10_COMPARISON_FUNC),
        ('BorderColor', Single * 4),
        ('MinLOD', Single),
        ('MaxLOD', Single),
    ]
    return D3D10_SAMPLER_DESC
def _define_D3D10_SHADER_BUFFER_DESC_head():
    class D3D10_SHADER_BUFFER_DESC(Structure):
        pass
    return D3D10_SHADER_BUFFER_DESC
def _define_D3D10_SHADER_BUFFER_DESC():
    D3D10_SHADER_BUFFER_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_BUFFER_DESC_head
    D3D10_SHADER_BUFFER_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Type', win32more.Graphics.Direct3D.D3D_CBUFFER_TYPE),
        ('Variables', UInt32),
        ('Size', UInt32),
        ('uFlags', UInt32),
    ]
    return D3D10_SHADER_BUFFER_DESC
def _define_D3D10_SHADER_DEBUG_FILE_INFO_head():
    class D3D10_SHADER_DEBUG_FILE_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_FILE_INFO
def _define_D3D10_SHADER_DEBUG_FILE_INFO():
    D3D10_SHADER_DEBUG_FILE_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_FILE_INFO_head
    D3D10_SHADER_DEBUG_FILE_INFO._fields_ = [
        ('FileName', UInt32),
        ('FileNameLen', UInt32),
        ('FileData', UInt32),
        ('FileLen', UInt32),
    ]
    return D3D10_SHADER_DEBUG_FILE_INFO
def _define_D3D10_SHADER_DEBUG_INFO_head():
    class D3D10_SHADER_DEBUG_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_INFO
def _define_D3D10_SHADER_DEBUG_INFO():
    D3D10_SHADER_DEBUG_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_INFO_head
    D3D10_SHADER_DEBUG_INFO._fields_ = [
        ('Size', UInt32),
        ('Creator', UInt32),
        ('EntrypointName', UInt32),
        ('ShaderTarget', UInt32),
        ('CompileFlags', UInt32),
        ('Files', UInt32),
        ('FileInfo', UInt32),
        ('Instructions', UInt32),
        ('InstructionInfo', UInt32),
        ('Variables', UInt32),
        ('VariableInfo', UInt32),
        ('InputVariables', UInt32),
        ('InputVariableInfo', UInt32),
        ('Tokens', UInt32),
        ('TokenInfo', UInt32),
        ('Scopes', UInt32),
        ('ScopeInfo', UInt32),
        ('ScopeVariables', UInt32),
        ('ScopeVariableInfo', UInt32),
        ('UintOffset', UInt32),
        ('StringOffset', UInt32),
    ]
    return D3D10_SHADER_DEBUG_INFO
def _define_D3D10_SHADER_DEBUG_INPUT_INFO_head():
    class D3D10_SHADER_DEBUG_INPUT_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_INPUT_INFO
def _define_D3D10_SHADER_DEBUG_INPUT_INFO():
    D3D10_SHADER_DEBUG_INPUT_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_INPUT_INFO_head
    D3D10_SHADER_DEBUG_INPUT_INFO._fields_ = [
        ('Var', UInt32),
        ('InitialRegisterSet', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_REGTYPE),
        ('InitialBank', UInt32),
        ('InitialRegister', UInt32),
        ('InitialComponent', UInt32),
        ('InitialValue', UInt32),
    ]
    return D3D10_SHADER_DEBUG_INPUT_INFO
def _define_D3D10_SHADER_DEBUG_INST_INFO_head():
    class D3D10_SHADER_DEBUG_INST_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_INST_INFO
def _define_D3D10_SHADER_DEBUG_INST_INFO():
    D3D10_SHADER_DEBUG_INST_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_INST_INFO_head
    D3D10_SHADER_DEBUG_INST_INFO._fields_ = [
        ('Id', UInt32),
        ('Opcode', UInt32),
        ('uOutputs', UInt32),
        ('pOutputs', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_OUTPUTREG_INFO * 2),
        ('TokenId', UInt32),
        ('NestingLevel', UInt32),
        ('Scopes', UInt32),
        ('ScopeInfo', UInt32),
        ('AccessedVars', UInt32),
        ('AccessedVarsInfo', UInt32),
    ]
    return D3D10_SHADER_DEBUG_INST_INFO
def _define_D3D10_SHADER_DEBUG_OUTPUTREG_INFO_head():
    class D3D10_SHADER_DEBUG_OUTPUTREG_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_OUTPUTREG_INFO
def _define_D3D10_SHADER_DEBUG_OUTPUTREG_INFO():
    D3D10_SHADER_DEBUG_OUTPUTREG_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_OUTPUTREG_INFO_head
    D3D10_SHADER_DEBUG_OUTPUTREG_INFO._fields_ = [
        ('OutputRegisterSet', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_REGTYPE),
        ('OutputReg', UInt32),
        ('TempArrayReg', UInt32),
        ('OutputComponents', UInt32 * 4),
        ('OutputVars', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_OUTPUTVAR * 4),
        ('IndexReg', UInt32),
        ('IndexComp', UInt32),
    ]
    return D3D10_SHADER_DEBUG_OUTPUTREG_INFO
def _define_D3D10_SHADER_DEBUG_OUTPUTVAR_head():
    class D3D10_SHADER_DEBUG_OUTPUTVAR(Structure):
        pass
    return D3D10_SHADER_DEBUG_OUTPUTVAR
def _define_D3D10_SHADER_DEBUG_OUTPUTVAR():
    D3D10_SHADER_DEBUG_OUTPUTVAR = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_OUTPUTVAR_head
    D3D10_SHADER_DEBUG_OUTPUTVAR._fields_ = [
        ('Var', UInt32),
        ('uValueMin', UInt32),
        ('uValueMax', UInt32),
        ('iValueMin', Int32),
        ('iValueMax', Int32),
        ('fValueMin', Single),
        ('fValueMax', Single),
        ('bNaNPossible', win32more.Foundation.BOOL),
        ('bInfPossible', win32more.Foundation.BOOL),
    ]
    return D3D10_SHADER_DEBUG_OUTPUTVAR
D3D10_SHADER_DEBUG_REGTYPE = Int32
D3D10_SHADER_DEBUG_REG_INPUT = 0
D3D10_SHADER_DEBUG_REG_OUTPUT = 1
D3D10_SHADER_DEBUG_REG_CBUFFER = 2
D3D10_SHADER_DEBUG_REG_TBUFFER = 3
D3D10_SHADER_DEBUG_REG_TEMP = 4
D3D10_SHADER_DEBUG_REG_TEMPARRAY = 5
D3D10_SHADER_DEBUG_REG_TEXTURE = 6
D3D10_SHADER_DEBUG_REG_SAMPLER = 7
D3D10_SHADER_DEBUG_REG_IMMEDIATECBUFFER = 8
D3D10_SHADER_DEBUG_REG_LITERAL = 9
D3D10_SHADER_DEBUG_REG_UNUSED = 10
D3D11_SHADER_DEBUG_REG_INTERFACE_POINTERS = 11
D3D11_SHADER_DEBUG_REG_UAV = 12
D3D10_SHADER_DEBUG_REG_FORCE_DWORD = 2147483647
def _define_D3D10_SHADER_DEBUG_SCOPE_INFO_head():
    class D3D10_SHADER_DEBUG_SCOPE_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_SCOPE_INFO
def _define_D3D10_SHADER_DEBUG_SCOPE_INFO():
    D3D10_SHADER_DEBUG_SCOPE_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_SCOPE_INFO_head
    D3D10_SHADER_DEBUG_SCOPE_INFO._fields_ = [
        ('ScopeType', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_SCOPETYPE),
        ('Name', UInt32),
        ('uNameLen', UInt32),
        ('uVariables', UInt32),
        ('VariableData', UInt32),
    ]
    return D3D10_SHADER_DEBUG_SCOPE_INFO
D3D10_SHADER_DEBUG_SCOPETYPE = Int32
D3D10_SHADER_DEBUG_SCOPE_GLOBAL = 0
D3D10_SHADER_DEBUG_SCOPE_BLOCK = 1
D3D10_SHADER_DEBUG_SCOPE_FORLOOP = 2
D3D10_SHADER_DEBUG_SCOPE_STRUCT = 3
D3D10_SHADER_DEBUG_SCOPE_FUNC_PARAMS = 4
D3D10_SHADER_DEBUG_SCOPE_STATEBLOCK = 5
D3D10_SHADER_DEBUG_SCOPE_NAMESPACE = 6
D3D10_SHADER_DEBUG_SCOPE_ANNOTATION = 7
D3D10_SHADER_DEBUG_SCOPE_FORCE_DWORD = 2147483647
def _define_D3D10_SHADER_DEBUG_SCOPEVAR_INFO_head():
    class D3D10_SHADER_DEBUG_SCOPEVAR_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_SCOPEVAR_INFO
def _define_D3D10_SHADER_DEBUG_SCOPEVAR_INFO():
    D3D10_SHADER_DEBUG_SCOPEVAR_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_SCOPEVAR_INFO_head
    D3D10_SHADER_DEBUG_SCOPEVAR_INFO._fields_ = [
        ('TokenId', UInt32),
        ('VarType', win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_VARTYPE),
        ('Class', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_CLASS),
        ('Rows', UInt32),
        ('Columns', UInt32),
        ('StructMemberScope', UInt32),
        ('uArrayIndices', UInt32),
        ('ArrayElements', UInt32),
        ('ArrayStrides', UInt32),
        ('uVariables', UInt32),
        ('uFirstVariable', UInt32),
    ]
    return D3D10_SHADER_DEBUG_SCOPEVAR_INFO
def _define_D3D10_SHADER_DEBUG_TOKEN_INFO_head():
    class D3D10_SHADER_DEBUG_TOKEN_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_TOKEN_INFO
def _define_D3D10_SHADER_DEBUG_TOKEN_INFO():
    D3D10_SHADER_DEBUG_TOKEN_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_TOKEN_INFO_head
    D3D10_SHADER_DEBUG_TOKEN_INFO._fields_ = [
        ('File', UInt32),
        ('Line', UInt32),
        ('Column', UInt32),
        ('TokenLength', UInt32),
        ('TokenId', UInt32),
    ]
    return D3D10_SHADER_DEBUG_TOKEN_INFO
def _define_D3D10_SHADER_DEBUG_VAR_INFO_head():
    class D3D10_SHADER_DEBUG_VAR_INFO(Structure):
        pass
    return D3D10_SHADER_DEBUG_VAR_INFO
def _define_D3D10_SHADER_DEBUG_VAR_INFO():
    D3D10_SHADER_DEBUG_VAR_INFO = win32more.Graphics.Direct3D10.D3D10_SHADER_DEBUG_VAR_INFO_head
    D3D10_SHADER_DEBUG_VAR_INFO._fields_ = [
        ('TokenId', UInt32),
        ('Type', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_TYPE),
        ('Register', UInt32),
        ('Component', UInt32),
        ('ScopeVar', UInt32),
        ('ScopeVarOffset', UInt32),
    ]
    return D3D10_SHADER_DEBUG_VAR_INFO
D3D10_SHADER_DEBUG_VARTYPE = Int32
D3D10_SHADER_DEBUG_VAR_VARIABLE = 0
D3D10_SHADER_DEBUG_VAR_FUNCTION = 1
D3D10_SHADER_DEBUG_VAR_FORCE_DWORD = 2147483647
def _define_D3D10_SHADER_DESC_head():
    class D3D10_SHADER_DESC(Structure):
        pass
    return D3D10_SHADER_DESC
def _define_D3D10_SHADER_DESC():
    D3D10_SHADER_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_DESC_head
    D3D10_SHADER_DESC._fields_ = [
        ('Version', UInt32),
        ('Creator', win32more.Foundation.PSTR),
        ('Flags', UInt32),
        ('ConstantBuffers', UInt32),
        ('BoundResources', UInt32),
        ('InputParameters', UInt32),
        ('OutputParameters', UInt32),
        ('InstructionCount', UInt32),
        ('TempRegisterCount', UInt32),
        ('TempArrayCount', UInt32),
        ('DefCount', UInt32),
        ('DclCount', UInt32),
        ('TextureNormalInstructions', UInt32),
        ('TextureLoadInstructions', UInt32),
        ('TextureCompInstructions', UInt32),
        ('TextureBiasInstructions', UInt32),
        ('TextureGradientInstructions', UInt32),
        ('FloatInstructionCount', UInt32),
        ('IntInstructionCount', UInt32),
        ('UintInstructionCount', UInt32),
        ('StaticFlowControlCount', UInt32),
        ('DynamicFlowControlCount', UInt32),
        ('MacroInstructionCount', UInt32),
        ('ArrayInstructionCount', UInt32),
        ('CutInstructionCount', UInt32),
        ('EmitInstructionCount', UInt32),
        ('GSOutputTopology', win32more.Graphics.Direct3D.D3D_PRIMITIVE_TOPOLOGY),
        ('GSMaxOutputVertexCount', UInt32),
    ]
    return D3D10_SHADER_DESC
def _define_D3D10_SHADER_INPUT_BIND_DESC_head():
    class D3D10_SHADER_INPUT_BIND_DESC(Structure):
        pass
    return D3D10_SHADER_INPUT_BIND_DESC
def _define_D3D10_SHADER_INPUT_BIND_DESC():
    D3D10_SHADER_INPUT_BIND_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_INPUT_BIND_DESC_head
    D3D10_SHADER_INPUT_BIND_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Type', win32more.Graphics.Direct3D.D3D_SHADER_INPUT_TYPE),
        ('BindPoint', UInt32),
        ('BindCount', UInt32),
        ('uFlags', UInt32),
        ('ReturnType', win32more.Graphics.Direct3D.D3D_RESOURCE_RETURN_TYPE),
        ('Dimension', win32more.Graphics.Direct3D.D3D_SRV_DIMENSION),
        ('NumSamples', UInt32),
    ]
    return D3D10_SHADER_INPUT_BIND_DESC
def _define_D3D10_SHADER_RESOURCE_VIEW_DESC_head():
    class D3D10_SHADER_RESOURCE_VIEW_DESC(Structure):
        pass
    return D3D10_SHADER_RESOURCE_VIEW_DESC
def _define_D3D10_SHADER_RESOURCE_VIEW_DESC():
    D3D10_SHADER_RESOURCE_VIEW_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC_head
    class D3D10_SHADER_RESOURCE_VIEW_DESC__Anonymous_e__Union(Union):
        pass
    D3D10_SHADER_RESOURCE_VIEW_DESC__Anonymous_e__Union._fields_ = [
        ('Buffer', win32more.Graphics.Direct3D10.D3D10_BUFFER_SRV),
        ('Texture1D', win32more.Graphics.Direct3D10.D3D10_TEX1D_SRV),
        ('Texture1DArray', win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_SRV),
        ('Texture2D', win32more.Graphics.Direct3D10.D3D10_TEX2D_SRV),
        ('Texture2DArray', win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_SRV),
        ('Texture2DMS', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_SRV),
        ('Texture2DMSArray', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_SRV),
        ('Texture3D', win32more.Graphics.Direct3D10.D3D10_TEX3D_SRV),
        ('TextureCube', win32more.Graphics.Direct3D10.D3D10_TEXCUBE_SRV),
    ]
    D3D10_SHADER_RESOURCE_VIEW_DESC._anonymous_ = [
        'Anonymous',
    ]
    D3D10_SHADER_RESOURCE_VIEW_DESC._fields_ = [
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('ViewDimension', win32more.Graphics.Direct3D.D3D_SRV_DIMENSION),
        ('Anonymous', D3D10_SHADER_RESOURCE_VIEW_DESC__Anonymous_e__Union),
    ]
    return D3D10_SHADER_RESOURCE_VIEW_DESC
def _define_D3D10_SHADER_RESOURCE_VIEW_DESC1_head():
    class D3D10_SHADER_RESOURCE_VIEW_DESC1(Structure):
        pass
    return D3D10_SHADER_RESOURCE_VIEW_DESC1
def _define_D3D10_SHADER_RESOURCE_VIEW_DESC1():
    D3D10_SHADER_RESOURCE_VIEW_DESC1 = win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC1_head
    class D3D10_SHADER_RESOURCE_VIEW_DESC1__Anonymous_e__Union(Union):
        pass
    D3D10_SHADER_RESOURCE_VIEW_DESC1__Anonymous_e__Union._fields_ = [
        ('Buffer', win32more.Graphics.Direct3D10.D3D10_BUFFER_SRV),
        ('Texture1D', win32more.Graphics.Direct3D10.D3D10_TEX1D_SRV),
        ('Texture1DArray', win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_SRV),
        ('Texture2D', win32more.Graphics.Direct3D10.D3D10_TEX2D_SRV),
        ('Texture2DArray', win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_SRV),
        ('Texture2DMS', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_SRV),
        ('Texture2DMSArray', win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_SRV),
        ('Texture3D', win32more.Graphics.Direct3D10.D3D10_TEX3D_SRV),
        ('TextureCube', win32more.Graphics.Direct3D10.D3D10_TEXCUBE_SRV),
        ('TextureCubeArray', win32more.Graphics.Direct3D10.D3D10_TEXCUBE_ARRAY_SRV1),
    ]
    D3D10_SHADER_RESOURCE_VIEW_DESC1._anonymous_ = [
        'Anonymous',
    ]
    D3D10_SHADER_RESOURCE_VIEW_DESC1._fields_ = [
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('ViewDimension', win32more.Graphics.Direct3D.D3D_SRV_DIMENSION),
        ('Anonymous', D3D10_SHADER_RESOURCE_VIEW_DESC1__Anonymous_e__Union),
    ]
    return D3D10_SHADER_RESOURCE_VIEW_DESC1
def _define_D3D10_SHADER_TYPE_DESC_head():
    class D3D10_SHADER_TYPE_DESC(Structure):
        pass
    return D3D10_SHADER_TYPE_DESC
def _define_D3D10_SHADER_TYPE_DESC():
    D3D10_SHADER_TYPE_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_TYPE_DESC_head
    D3D10_SHADER_TYPE_DESC._fields_ = [
        ('Class', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_CLASS),
        ('Type', win32more.Graphics.Direct3D.D3D_SHADER_VARIABLE_TYPE),
        ('Rows', UInt32),
        ('Columns', UInt32),
        ('Elements', UInt32),
        ('Members', UInt32),
        ('Offset', UInt32),
    ]
    return D3D10_SHADER_TYPE_DESC
def _define_D3D10_SHADER_VARIABLE_DESC_head():
    class D3D10_SHADER_VARIABLE_DESC(Structure):
        pass
    return D3D10_SHADER_VARIABLE_DESC
def _define_D3D10_SHADER_VARIABLE_DESC():
    D3D10_SHADER_VARIABLE_DESC = win32more.Graphics.Direct3D10.D3D10_SHADER_VARIABLE_DESC_head
    D3D10_SHADER_VARIABLE_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('StartOffset', UInt32),
        ('Size', UInt32),
        ('uFlags', UInt32),
        ('DefaultValue', c_void_p),
    ]
    return D3D10_SHADER_VARIABLE_DESC
def _define_D3D10_SIGNATURE_PARAMETER_DESC_head():
    class D3D10_SIGNATURE_PARAMETER_DESC(Structure):
        pass
    return D3D10_SIGNATURE_PARAMETER_DESC
def _define_D3D10_SIGNATURE_PARAMETER_DESC():
    D3D10_SIGNATURE_PARAMETER_DESC = win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head
    D3D10_SIGNATURE_PARAMETER_DESC._fields_ = [
        ('SemanticName', win32more.Foundation.PSTR),
        ('SemanticIndex', UInt32),
        ('Register', UInt32),
        ('SystemValueType', win32more.Graphics.Direct3D.D3D_NAME),
        ('ComponentType', win32more.Graphics.Direct3D.D3D_REGISTER_COMPONENT_TYPE),
        ('Mask', Byte),
        ('ReadWriteMask', Byte),
    ]
    return D3D10_SIGNATURE_PARAMETER_DESC
def _define_D3D10_SO_DECLARATION_ENTRY_head():
    class D3D10_SO_DECLARATION_ENTRY(Structure):
        pass
    return D3D10_SO_DECLARATION_ENTRY
def _define_D3D10_SO_DECLARATION_ENTRY():
    D3D10_SO_DECLARATION_ENTRY = win32more.Graphics.Direct3D10.D3D10_SO_DECLARATION_ENTRY_head
    D3D10_SO_DECLARATION_ENTRY._fields_ = [
        ('SemanticName', win32more.Foundation.PSTR),
        ('SemanticIndex', UInt32),
        ('StartComponent', Byte),
        ('ComponentCount', Byte),
        ('OutputSlot', Byte),
    ]
    return D3D10_SO_DECLARATION_ENTRY
D3D10_STANDARD_MULTISAMPLE_QUALITY_LEVELS = Int32
D3D10_STANDARD_MULTISAMPLE_PATTERN = -1
D3D10_CENTER_MULTISAMPLE_PATTERN = -2
def _define_D3D10_STATE_BLOCK_MASK_head():
    class D3D10_STATE_BLOCK_MASK(Structure):
        pass
    return D3D10_STATE_BLOCK_MASK
def _define_D3D10_STATE_BLOCK_MASK():
    D3D10_STATE_BLOCK_MASK = win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head
    D3D10_STATE_BLOCK_MASK._fields_ = [
        ('VS', Byte),
        ('VSSamplers', Byte * 2),
        ('VSShaderResources', Byte * 16),
        ('VSConstantBuffers', Byte * 2),
        ('GS', Byte),
        ('GSSamplers', Byte * 2),
        ('GSShaderResources', Byte * 16),
        ('GSConstantBuffers', Byte * 2),
        ('PS', Byte),
        ('PSSamplers', Byte * 2),
        ('PSShaderResources', Byte * 16),
        ('PSConstantBuffers', Byte * 2),
        ('IAVertexBuffers', Byte * 2),
        ('IAIndexBuffer', Byte),
        ('IAInputLayout', Byte),
        ('IAPrimitiveTopology', Byte),
        ('OMRenderTargets', Byte),
        ('OMDepthStencilState', Byte),
        ('OMBlendState', Byte),
        ('RSViewports', Byte),
        ('RSScissorRects', Byte),
        ('RSRasterizerState', Byte),
        ('SOBuffers', Byte),
        ('Predication', Byte),
    ]
    return D3D10_STATE_BLOCK_MASK
D3D10_STENCIL_OP = Int32
D3D10_STENCIL_OP_KEEP = 1
D3D10_STENCIL_OP_ZERO = 2
D3D10_STENCIL_OP_REPLACE = 3
D3D10_STENCIL_OP_INCR_SAT = 4
D3D10_STENCIL_OP_DECR_SAT = 5
D3D10_STENCIL_OP_INVERT = 6
D3D10_STENCIL_OP_INCR = 7
D3D10_STENCIL_OP_DECR = 8
def _define_D3D10_SUBRESOURCE_DATA_head():
    class D3D10_SUBRESOURCE_DATA(Structure):
        pass
    return D3D10_SUBRESOURCE_DATA
def _define_D3D10_SUBRESOURCE_DATA():
    D3D10_SUBRESOURCE_DATA = win32more.Graphics.Direct3D10.D3D10_SUBRESOURCE_DATA_head
    D3D10_SUBRESOURCE_DATA._fields_ = [
        ('pSysMem', c_void_p),
        ('SysMemPitch', UInt32),
        ('SysMemSlicePitch', UInt32),
    ]
    return D3D10_SUBRESOURCE_DATA
def _define_D3D10_TECHNIQUE_DESC_head():
    class D3D10_TECHNIQUE_DESC(Structure):
        pass
    return D3D10_TECHNIQUE_DESC
def _define_D3D10_TECHNIQUE_DESC():
    D3D10_TECHNIQUE_DESC = win32more.Graphics.Direct3D10.D3D10_TECHNIQUE_DESC_head
    D3D10_TECHNIQUE_DESC._fields_ = [
        ('Name', win32more.Foundation.PSTR),
        ('Passes', UInt32),
        ('Annotations', UInt32),
    ]
    return D3D10_TECHNIQUE_DESC
def _define_D3D10_TEX1D_ARRAY_DSV_head():
    class D3D10_TEX1D_ARRAY_DSV(Structure):
        pass
    return D3D10_TEX1D_ARRAY_DSV
def _define_D3D10_TEX1D_ARRAY_DSV():
    D3D10_TEX1D_ARRAY_DSV = win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_DSV_head
    D3D10_TEX1D_ARRAY_DSV._fields_ = [
        ('MipSlice', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX1D_ARRAY_DSV
def _define_D3D10_TEX1D_ARRAY_RTV_head():
    class D3D10_TEX1D_ARRAY_RTV(Structure):
        pass
    return D3D10_TEX1D_ARRAY_RTV
def _define_D3D10_TEX1D_ARRAY_RTV():
    D3D10_TEX1D_ARRAY_RTV = win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_RTV_head
    D3D10_TEX1D_ARRAY_RTV._fields_ = [
        ('MipSlice', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX1D_ARRAY_RTV
def _define_D3D10_TEX1D_ARRAY_SRV_head():
    class D3D10_TEX1D_ARRAY_SRV(Structure):
        pass
    return D3D10_TEX1D_ARRAY_SRV
def _define_D3D10_TEX1D_ARRAY_SRV():
    D3D10_TEX1D_ARRAY_SRV = win32more.Graphics.Direct3D10.D3D10_TEX1D_ARRAY_SRV_head
    D3D10_TEX1D_ARRAY_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX1D_ARRAY_SRV
def _define_D3D10_TEX1D_DSV_head():
    class D3D10_TEX1D_DSV(Structure):
        pass
    return D3D10_TEX1D_DSV
def _define_D3D10_TEX1D_DSV():
    D3D10_TEX1D_DSV = win32more.Graphics.Direct3D10.D3D10_TEX1D_DSV_head
    D3D10_TEX1D_DSV._fields_ = [
        ('MipSlice', UInt32),
    ]
    return D3D10_TEX1D_DSV
def _define_D3D10_TEX1D_RTV_head():
    class D3D10_TEX1D_RTV(Structure):
        pass
    return D3D10_TEX1D_RTV
def _define_D3D10_TEX1D_RTV():
    D3D10_TEX1D_RTV = win32more.Graphics.Direct3D10.D3D10_TEX1D_RTV_head
    D3D10_TEX1D_RTV._fields_ = [
        ('MipSlice', UInt32),
    ]
    return D3D10_TEX1D_RTV
def _define_D3D10_TEX1D_SRV_head():
    class D3D10_TEX1D_SRV(Structure):
        pass
    return D3D10_TEX1D_SRV
def _define_D3D10_TEX1D_SRV():
    D3D10_TEX1D_SRV = win32more.Graphics.Direct3D10.D3D10_TEX1D_SRV_head
    D3D10_TEX1D_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
    ]
    return D3D10_TEX1D_SRV
def _define_D3D10_TEX2D_ARRAY_DSV_head():
    class D3D10_TEX2D_ARRAY_DSV(Structure):
        pass
    return D3D10_TEX2D_ARRAY_DSV
def _define_D3D10_TEX2D_ARRAY_DSV():
    D3D10_TEX2D_ARRAY_DSV = win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_DSV_head
    D3D10_TEX2D_ARRAY_DSV._fields_ = [
        ('MipSlice', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2D_ARRAY_DSV
def _define_D3D10_TEX2D_ARRAY_RTV_head():
    class D3D10_TEX2D_ARRAY_RTV(Structure):
        pass
    return D3D10_TEX2D_ARRAY_RTV
def _define_D3D10_TEX2D_ARRAY_RTV():
    D3D10_TEX2D_ARRAY_RTV = win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_RTV_head
    D3D10_TEX2D_ARRAY_RTV._fields_ = [
        ('MipSlice', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2D_ARRAY_RTV
def _define_D3D10_TEX2D_ARRAY_SRV_head():
    class D3D10_TEX2D_ARRAY_SRV(Structure):
        pass
    return D3D10_TEX2D_ARRAY_SRV
def _define_D3D10_TEX2D_ARRAY_SRV():
    D3D10_TEX2D_ARRAY_SRV = win32more.Graphics.Direct3D10.D3D10_TEX2D_ARRAY_SRV_head
    D3D10_TEX2D_ARRAY_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2D_ARRAY_SRV
def _define_D3D10_TEX2D_DSV_head():
    class D3D10_TEX2D_DSV(Structure):
        pass
    return D3D10_TEX2D_DSV
def _define_D3D10_TEX2D_DSV():
    D3D10_TEX2D_DSV = win32more.Graphics.Direct3D10.D3D10_TEX2D_DSV_head
    D3D10_TEX2D_DSV._fields_ = [
        ('MipSlice', UInt32),
    ]
    return D3D10_TEX2D_DSV
def _define_D3D10_TEX2D_RTV_head():
    class D3D10_TEX2D_RTV(Structure):
        pass
    return D3D10_TEX2D_RTV
def _define_D3D10_TEX2D_RTV():
    D3D10_TEX2D_RTV = win32more.Graphics.Direct3D10.D3D10_TEX2D_RTV_head
    D3D10_TEX2D_RTV._fields_ = [
        ('MipSlice', UInt32),
    ]
    return D3D10_TEX2D_RTV
def _define_D3D10_TEX2D_SRV_head():
    class D3D10_TEX2D_SRV(Structure):
        pass
    return D3D10_TEX2D_SRV
def _define_D3D10_TEX2D_SRV():
    D3D10_TEX2D_SRV = win32more.Graphics.Direct3D10.D3D10_TEX2D_SRV_head
    D3D10_TEX2D_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
    ]
    return D3D10_TEX2D_SRV
def _define_D3D10_TEX2DMS_ARRAY_DSV_head():
    class D3D10_TEX2DMS_ARRAY_DSV(Structure):
        pass
    return D3D10_TEX2DMS_ARRAY_DSV
def _define_D3D10_TEX2DMS_ARRAY_DSV():
    D3D10_TEX2DMS_ARRAY_DSV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_DSV_head
    D3D10_TEX2DMS_ARRAY_DSV._fields_ = [
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2DMS_ARRAY_DSV
def _define_D3D10_TEX2DMS_ARRAY_RTV_head():
    class D3D10_TEX2DMS_ARRAY_RTV(Structure):
        pass
    return D3D10_TEX2DMS_ARRAY_RTV
def _define_D3D10_TEX2DMS_ARRAY_RTV():
    D3D10_TEX2DMS_ARRAY_RTV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_RTV_head
    D3D10_TEX2DMS_ARRAY_RTV._fields_ = [
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2DMS_ARRAY_RTV
def _define_D3D10_TEX2DMS_ARRAY_SRV_head():
    class D3D10_TEX2DMS_ARRAY_SRV(Structure):
        pass
    return D3D10_TEX2DMS_ARRAY_SRV
def _define_D3D10_TEX2DMS_ARRAY_SRV():
    D3D10_TEX2DMS_ARRAY_SRV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_ARRAY_SRV_head
    D3D10_TEX2DMS_ARRAY_SRV._fields_ = [
        ('FirstArraySlice', UInt32),
        ('ArraySize', UInt32),
    ]
    return D3D10_TEX2DMS_ARRAY_SRV
def _define_D3D10_TEX2DMS_DSV_head():
    class D3D10_TEX2DMS_DSV(Structure):
        pass
    return D3D10_TEX2DMS_DSV
def _define_D3D10_TEX2DMS_DSV():
    D3D10_TEX2DMS_DSV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_DSV_head
    D3D10_TEX2DMS_DSV._fields_ = [
        ('UnusedField_NothingToDefine', UInt32),
    ]
    return D3D10_TEX2DMS_DSV
def _define_D3D10_TEX2DMS_RTV_head():
    class D3D10_TEX2DMS_RTV(Structure):
        pass
    return D3D10_TEX2DMS_RTV
def _define_D3D10_TEX2DMS_RTV():
    D3D10_TEX2DMS_RTV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_RTV_head
    D3D10_TEX2DMS_RTV._fields_ = [
        ('UnusedField_NothingToDefine', UInt32),
    ]
    return D3D10_TEX2DMS_RTV
def _define_D3D10_TEX2DMS_SRV_head():
    class D3D10_TEX2DMS_SRV(Structure):
        pass
    return D3D10_TEX2DMS_SRV
def _define_D3D10_TEX2DMS_SRV():
    D3D10_TEX2DMS_SRV = win32more.Graphics.Direct3D10.D3D10_TEX2DMS_SRV_head
    D3D10_TEX2DMS_SRV._fields_ = [
        ('UnusedField_NothingToDefine', UInt32),
    ]
    return D3D10_TEX2DMS_SRV
def _define_D3D10_TEX3D_RTV_head():
    class D3D10_TEX3D_RTV(Structure):
        pass
    return D3D10_TEX3D_RTV
def _define_D3D10_TEX3D_RTV():
    D3D10_TEX3D_RTV = win32more.Graphics.Direct3D10.D3D10_TEX3D_RTV_head
    D3D10_TEX3D_RTV._fields_ = [
        ('MipSlice', UInt32),
        ('FirstWSlice', UInt32),
        ('WSize', UInt32),
    ]
    return D3D10_TEX3D_RTV
def _define_D3D10_TEX3D_SRV_head():
    class D3D10_TEX3D_SRV(Structure):
        pass
    return D3D10_TEX3D_SRV
def _define_D3D10_TEX3D_SRV():
    D3D10_TEX3D_SRV = win32more.Graphics.Direct3D10.D3D10_TEX3D_SRV_head
    D3D10_TEX3D_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
    ]
    return D3D10_TEX3D_SRV
def _define_D3D10_TEXCUBE_ARRAY_SRV1_head():
    class D3D10_TEXCUBE_ARRAY_SRV1(Structure):
        pass
    return D3D10_TEXCUBE_ARRAY_SRV1
def _define_D3D10_TEXCUBE_ARRAY_SRV1():
    D3D10_TEXCUBE_ARRAY_SRV1 = win32more.Graphics.Direct3D10.D3D10_TEXCUBE_ARRAY_SRV1_head
    D3D10_TEXCUBE_ARRAY_SRV1._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
        ('First2DArrayFace', UInt32),
        ('NumCubes', UInt32),
    ]
    return D3D10_TEXCUBE_ARRAY_SRV1
def _define_D3D10_TEXCUBE_SRV_head():
    class D3D10_TEXCUBE_SRV(Structure):
        pass
    return D3D10_TEXCUBE_SRV
def _define_D3D10_TEXCUBE_SRV():
    D3D10_TEXCUBE_SRV = win32more.Graphics.Direct3D10.D3D10_TEXCUBE_SRV_head
    D3D10_TEXCUBE_SRV._fields_ = [
        ('MostDetailedMip', UInt32),
        ('MipLevels', UInt32),
    ]
    return D3D10_TEXCUBE_SRV
D3D10_TEXTURE_ADDRESS_MODE = Int32
D3D10_TEXTURE_ADDRESS_WRAP = 1
D3D10_TEXTURE_ADDRESS_MIRROR = 2
D3D10_TEXTURE_ADDRESS_CLAMP = 3
D3D10_TEXTURE_ADDRESS_BORDER = 4
D3D10_TEXTURE_ADDRESS_MIRROR_ONCE = 5
def _define_D3D10_TEXTURE1D_DESC_head():
    class D3D10_TEXTURE1D_DESC(Structure):
        pass
    return D3D10_TEXTURE1D_DESC
def _define_D3D10_TEXTURE1D_DESC():
    D3D10_TEXTURE1D_DESC = win32more.Graphics.Direct3D10.D3D10_TEXTURE1D_DESC_head
    D3D10_TEXTURE1D_DESC._fields_ = [
        ('Width', UInt32),
        ('MipLevels', UInt32),
        ('ArraySize', UInt32),
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('Usage', win32more.Graphics.Direct3D10.D3D10_USAGE),
        ('BindFlags', UInt32),
        ('CPUAccessFlags', UInt32),
        ('MiscFlags', UInt32),
    ]
    return D3D10_TEXTURE1D_DESC
def _define_D3D10_TEXTURE2D_DESC_head():
    class D3D10_TEXTURE2D_DESC(Structure):
        pass
    return D3D10_TEXTURE2D_DESC
def _define_D3D10_TEXTURE2D_DESC():
    D3D10_TEXTURE2D_DESC = win32more.Graphics.Direct3D10.D3D10_TEXTURE2D_DESC_head
    D3D10_TEXTURE2D_DESC._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('MipLevels', UInt32),
        ('ArraySize', UInt32),
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('SampleDesc', win32more.Graphics.Dxgi.Common.DXGI_SAMPLE_DESC),
        ('Usage', win32more.Graphics.Direct3D10.D3D10_USAGE),
        ('BindFlags', UInt32),
        ('CPUAccessFlags', UInt32),
        ('MiscFlags', UInt32),
    ]
    return D3D10_TEXTURE2D_DESC
def _define_D3D10_TEXTURE3D_DESC_head():
    class D3D10_TEXTURE3D_DESC(Structure):
        pass
    return D3D10_TEXTURE3D_DESC
def _define_D3D10_TEXTURE3D_DESC():
    D3D10_TEXTURE3D_DESC = win32more.Graphics.Direct3D10.D3D10_TEXTURE3D_DESC_head
    D3D10_TEXTURE3D_DESC._fields_ = [
        ('Width', UInt32),
        ('Height', UInt32),
        ('Depth', UInt32),
        ('MipLevels', UInt32),
        ('Format', win32more.Graphics.Dxgi.Common.DXGI_FORMAT),
        ('Usage', win32more.Graphics.Direct3D10.D3D10_USAGE),
        ('BindFlags', UInt32),
        ('CPUAccessFlags', UInt32),
        ('MiscFlags', UInt32),
    ]
    return D3D10_TEXTURE3D_DESC
D3D10_TEXTURECUBE_FACE = Int32
D3D10_TEXTURECUBE_FACE_POSITIVE_X = 0
D3D10_TEXTURECUBE_FACE_NEGATIVE_X = 1
D3D10_TEXTURECUBE_FACE_POSITIVE_Y = 2
D3D10_TEXTURECUBE_FACE_NEGATIVE_Y = 3
D3D10_TEXTURECUBE_FACE_POSITIVE_Z = 4
D3D10_TEXTURECUBE_FACE_NEGATIVE_Z = 5
D3D10_USAGE = Int32
D3D10_USAGE_DEFAULT = 0
D3D10_USAGE_IMMUTABLE = 1
D3D10_USAGE_DYNAMIC = 2
D3D10_USAGE_STAGING = 3
def _define_D3D10_VIEWPORT_head():
    class D3D10_VIEWPORT(Structure):
        pass
    return D3D10_VIEWPORT
def _define_D3D10_VIEWPORT():
    D3D10_VIEWPORT = win32more.Graphics.Direct3D10.D3D10_VIEWPORT_head
    D3D10_VIEWPORT._fields_ = [
        ('TopLeftX', Int32),
        ('TopLeftY', Int32),
        ('Width', UInt32),
        ('Height', UInt32),
        ('MinDepth', Single),
        ('MaxDepth', Single),
    ]
    return D3D10_VIEWPORT
def _define_ID3D10Asynchronous_head():
    class ID3D10Asynchronous(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('9b7e4c0d-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Asynchronous
def _define_ID3D10Asynchronous():
    ID3D10Asynchronous = win32more.Graphics.Direct3D10.ID3D10Asynchronous_head
    ID3D10Asynchronous.Begin = COMMETHOD(WINFUNCTYPE(Void,)(7, 'Begin', ()))
    ID3D10Asynchronous.End = COMMETHOD(WINFUNCTYPE(Void,)(8, 'End', ()))
    ID3D10Asynchronous.GetData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32)(9, 'GetData', ((1, 'pData'),(1, 'DataSize'),(1, 'GetDataFlags'),)))
    ID3D10Asynchronous.GetDataSize = COMMETHOD(WINFUNCTYPE(UInt32,)(10, 'GetDataSize', ()))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10Asynchronous
def _define_ID3D10BlendState_head():
    class ID3D10BlendState(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('edad8d19-8a35-4d6d-85-66-2e-a2-76-cd-e1-61')
    return ID3D10BlendState
def _define_ID3D10BlendState():
    ID3D10BlendState = win32more.Graphics.Direct3D10.ID3D10BlendState_head
    ID3D10BlendState.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_BLEND_DESC_head))(7, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10BlendState
def _define_ID3D10BlendState1_head():
    class ID3D10BlendState1(win32more.Graphics.Direct3D10.ID3D10BlendState_head):
        Guid = Guid('edad8d99-8a35-4d6d-85-66-2e-a2-76-cd-e1-61')
    return ID3D10BlendState1
def _define_ID3D10BlendState1():
    ID3D10BlendState1 = win32more.Graphics.Direct3D10.ID3D10BlendState1_head
    ID3D10BlendState1.GetDesc1 = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_BLEND_DESC1_head))(8, 'GetDesc1', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10BlendState
    return ID3D10BlendState1
def _define_ID3D10Buffer_head():
    class ID3D10Buffer(win32more.Graphics.Direct3D10.ID3D10Resource_head):
        Guid = Guid('9b7e4c02-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Buffer
def _define_ID3D10Buffer():
    ID3D10Buffer = win32more.Graphics.Direct3D10.ID3D10Buffer_head
    ID3D10Buffer.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MAP,UInt32,POINTER(c_void_p))(10, 'Map', ((1, 'MapType'),(1, 'MapFlags'),(1, 'ppData'),)))
    ID3D10Buffer.Unmap = COMMETHOD(WINFUNCTYPE(Void,)(11, 'Unmap', ()))
    ID3D10Buffer.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_BUFFER_DESC_head))(12, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Resource
    return ID3D10Buffer
def _define_ID3D10Counter_head():
    class ID3D10Counter(win32more.Graphics.Direct3D10.ID3D10Asynchronous_head):
        Guid = Guid('9b7e4c11-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Counter
def _define_ID3D10Counter():
    ID3D10Counter = win32more.Graphics.Direct3D10.ID3D10Counter_head
    ID3D10Counter.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_COUNTER_DESC_head))(11, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Asynchronous
    return ID3D10Counter
def _define_ID3D10Debug_head():
    class ID3D10Debug(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b7e4e01-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Debug
def _define_ID3D10Debug():
    ID3D10Debug = win32more.Graphics.Direct3D10.ID3D10Debug_head
    ID3D10Debug.SetFeatureMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(3, 'SetFeatureMask', ((1, 'Mask'),)))
    ID3D10Debug.GetFeatureMask = COMMETHOD(WINFUNCTYPE(UInt32,)(4, 'GetFeatureMask', ()))
    ID3D10Debug.SetPresentPerRenderOpDelay = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'SetPresentPerRenderOpDelay', ((1, 'Milliseconds'),)))
    ID3D10Debug.GetPresentPerRenderOpDelay = COMMETHOD(WINFUNCTYPE(UInt32,)(6, 'GetPresentPerRenderOpDelay', ()))
    ID3D10Debug.SetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGISwapChain_head)(7, 'SetSwapChain', ((1, 'pSwapChain'),)))
    ID3D10Debug.GetSwapChain = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Dxgi.IDXGISwapChain_head))(8, 'GetSwapChain', ((1, 'ppSwapChain'),)))
    ID3D10Debug.Validate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Validate', ()))
    win32more.System.Com.IUnknown
    return ID3D10Debug
def _define_ID3D10DepthStencilState_head():
    class ID3D10DepthStencilState(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('2b4b1cc8-a4ad-41f8-83-22-ca-86-fc-3e-c6-75')
    return ID3D10DepthStencilState
def _define_ID3D10DepthStencilState():
    ID3D10DepthStencilState = win32more.Graphics.Direct3D10.ID3D10DepthStencilState_head
    ID3D10DepthStencilState.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_DESC_head))(7, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10DepthStencilState
def _define_ID3D10DepthStencilView_head():
    class ID3D10DepthStencilView(win32more.Graphics.Direct3D10.ID3D10View_head):
        Guid = Guid('9b7e4c09-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10DepthStencilView
def _define_ID3D10DepthStencilView():
    ID3D10DepthStencilView = win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head
    ID3D10DepthStencilView.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_VIEW_DESC_head))(8, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10View
    return ID3D10DepthStencilView
def _define_ID3D10Device_head():
    class ID3D10Device(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b7e4c0f-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Device
def _define_ID3D10Device():
    ID3D10Device = win32more.Graphics.Direct3D10.ID3D10Device_head
    ID3D10Device.VSSetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(3, 'VSSetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.PSSetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(4, 'PSSetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.PSSetShader = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10PixelShader_head)(5, 'PSSetShader', ((1, 'pPixelShader'),)))
    ID3D10Device.PSSetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(6, 'PSSetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.VSSetShader = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10VertexShader_head)(7, 'VSSetShader', ((1, 'pVertexShader'),)))
    ID3D10Device.DrawIndexed = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,Int32)(8, 'DrawIndexed', ((1, 'IndexCount'),(1, 'StartIndexLocation'),(1, 'BaseVertexLocation'),)))
    ID3D10Device.Draw = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32)(9, 'Draw', ((1, 'VertexCount'),(1, 'StartVertexLocation'),)))
    ID3D10Device.PSSetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(10, 'PSSetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.IASetInputLayout = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10InputLayout_head)(11, 'IASetInputLayout', ((1, 'pInputLayout'),)))
    ID3D10Device.IASetVertexBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head),POINTER(UInt32),POINTER(UInt32))(12, 'IASetVertexBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppVertexBuffers'),(1, 'pStrides'),(1, 'pOffsets'),)))
    ID3D10Device.IASetIndexBuffer = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Buffer_head,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32)(13, 'IASetIndexBuffer', ((1, 'pIndexBuffer'),(1, 'Format'),(1, 'Offset'),)))
    ID3D10Device.DrawIndexedInstanced = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,UInt32,Int32,UInt32)(14, 'DrawIndexedInstanced', ((1, 'IndexCountPerInstance'),(1, 'InstanceCount'),(1, 'StartIndexLocation'),(1, 'BaseVertexLocation'),(1, 'StartInstanceLocation'),)))
    ID3D10Device.DrawInstanced = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,UInt32,UInt32)(15, 'DrawInstanced', ((1, 'VertexCountPerInstance'),(1, 'InstanceCount'),(1, 'StartVertexLocation'),(1, 'StartInstanceLocation'),)))
    ID3D10Device.GSSetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(16, 'GSSetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.GSSetShader = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10GeometryShader_head)(17, 'GSSetShader', ((1, 'pShader'),)))
    ID3D10Device.IASetPrimitiveTopology = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D.D3D_PRIMITIVE_TOPOLOGY)(18, 'IASetPrimitiveTopology', ((1, 'Topology'),)))
    ID3D10Device.VSSetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(19, 'VSSetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.VSSetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(20, 'VSSetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.SetPredication = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Predicate_head,win32more.Foundation.BOOL)(21, 'SetPredication', ((1, 'pPredicate'),(1, 'PredicateValue'),)))
    ID3D10Device.GSSetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(22, 'GSSetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.GSSetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(23, 'GSSetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.OMSetRenderTargets = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head),win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head)(24, 'OMSetRenderTargets', ((1, 'NumViews'),(1, 'ppRenderTargetViews'),(1, 'pDepthStencilView'),)))
    ID3D10Device.OMSetBlendState = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10BlendState_head,POINTER(Single),UInt32)(25, 'OMSetBlendState', ((1, 'pBlendState'),(1, 'BlendFactor'),(1, 'SampleMask'),)))
    ID3D10Device.OMSetDepthStencilState = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10DepthStencilState_head,UInt32)(26, 'OMSetDepthStencilState', ((1, 'pDepthStencilState'),(1, 'StencilRef'),)))
    ID3D10Device.SOSetTargets = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head),POINTER(UInt32))(27, 'SOSetTargets', ((1, 'NumBuffers'),(1, 'ppSOTargets'),(1, 'pOffsets'),)))
    ID3D10Device.DrawAuto = COMMETHOD(WINFUNCTYPE(Void,)(28, 'DrawAuto', ()))
    ID3D10Device.RSSetState = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10RasterizerState_head)(29, 'RSSetState', ((1, 'pRasterizerState'),)))
    ID3D10Device.RSSetViewports = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_VIEWPORT_head))(30, 'RSSetViewports', ((1, 'NumViewports'),(1, 'pViewports'),)))
    ID3D10Device.RSSetScissorRects = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Foundation.RECT_head))(31, 'RSSetScissorRects', ((1, 'NumRects'),(1, 'pRects'),)))
    ID3D10Device.CopySubresourceRegion = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Resource_head,UInt32,UInt32,UInt32,UInt32,win32more.Graphics.Direct3D10.ID3D10Resource_head,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_BOX_head))(32, 'CopySubresourceRegion', ((1, 'pDstResource'),(1, 'DstSubresource'),(1, 'DstX'),(1, 'DstY'),(1, 'DstZ'),(1, 'pSrcResource'),(1, 'SrcSubresource'),(1, 'pSrcBox'),)))
    ID3D10Device.CopyResource = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Resource_head,win32more.Graphics.Direct3D10.ID3D10Resource_head)(33, 'CopyResource', ((1, 'pDstResource'),(1, 'pSrcResource'),)))
    ID3D10Device.UpdateSubresource = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Resource_head,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_BOX_head),c_void_p,UInt32,UInt32)(34, 'UpdateSubresource', ((1, 'pDstResource'),(1, 'DstSubresource'),(1, 'pDstBox'),(1, 'pSrcData'),(1, 'SrcRowPitch'),(1, 'SrcDepthPitch'),)))
    ID3D10Device.ClearRenderTargetView = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head,POINTER(Single))(35, 'ClearRenderTargetView', ((1, 'pRenderTargetView'),(1, 'ColorRGBA'),)))
    ID3D10Device.ClearDepthStencilView = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head,UInt32,Single,Byte)(36, 'ClearDepthStencilView', ((1, 'pDepthStencilView'),(1, 'ClearFlags'),(1, 'Depth'),(1, 'Stencil'),)))
    ID3D10Device.GenerateMips = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head)(37, 'GenerateMips', ((1, 'pShaderResourceView'),)))
    ID3D10Device.ResolveSubresource = COMMETHOD(WINFUNCTYPE(Void,win32more.Graphics.Direct3D10.ID3D10Resource_head,UInt32,win32more.Graphics.Direct3D10.ID3D10Resource_head,UInt32,win32more.Graphics.Dxgi.Common.DXGI_FORMAT)(38, 'ResolveSubresource', ((1, 'pDstResource'),(1, 'DstSubresource'),(1, 'pSrcResource'),(1, 'SrcSubresource'),(1, 'Format'),)))
    ID3D10Device.VSGetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(39, 'VSGetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.PSGetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(40, 'PSGetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.PSGetShader = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10PixelShader_head))(41, 'PSGetShader', ((1, 'ppPixelShader'),)))
    ID3D10Device.PSGetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(42, 'PSGetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.VSGetShader = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10VertexShader_head))(43, 'VSGetShader', ((1, 'ppVertexShader'),)))
    ID3D10Device.PSGetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(44, 'PSGetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.IAGetInputLayout = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10InputLayout_head))(45, 'IAGetInputLayout', ((1, 'ppInputLayout'),)))
    ID3D10Device.IAGetVertexBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head),POINTER(UInt32),POINTER(UInt32))(46, 'IAGetVertexBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppVertexBuffers'),(1, 'pStrides'),(1, 'pOffsets'),)))
    ID3D10Device.IAGetIndexBuffer = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head),POINTER(win32more.Graphics.Dxgi.Common.DXGI_FORMAT),POINTER(UInt32))(47, 'IAGetIndexBuffer', ((1, 'pIndexBuffer'),(1, 'Format'),(1, 'Offset'),)))
    ID3D10Device.GSGetConstantBuffers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(48, 'GSGetConstantBuffers', ((1, 'StartSlot'),(1, 'NumBuffers'),(1, 'ppConstantBuffers'),)))
    ID3D10Device.GSGetShader = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10GeometryShader_head))(49, 'GSGetShader', ((1, 'ppGeometryShader'),)))
    ID3D10Device.IAGetPrimitiveTopology = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D.D3D_PRIMITIVE_TOPOLOGY))(50, 'IAGetPrimitiveTopology', ((1, 'pTopology'),)))
    ID3D10Device.VSGetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(51, 'VSGetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.VSGetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(52, 'VSGetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.GetPredication = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10Predicate_head),POINTER(win32more.Foundation.BOOL))(53, 'GetPredication', ((1, 'ppPredicate'),(1, 'pPredicateValue'),)))
    ID3D10Device.GSGetShaderResources = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(54, 'GSGetShaderResources', ((1, 'StartSlot'),(1, 'NumViews'),(1, 'ppShaderResourceViews'),)))
    ID3D10Device.GSGetSamplers = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(55, 'GSGetSamplers', ((1, 'StartSlot'),(1, 'NumSamplers'),(1, 'ppSamplers'),)))
    ID3D10Device.OMGetRenderTargets = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head),POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head))(56, 'OMGetRenderTargets', ((1, 'NumViews'),(1, 'ppRenderTargetViews'),(1, 'ppDepthStencilView'),)))
    ID3D10Device.OMGetBlendState = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10BlendState_head),POINTER(Single),POINTER(UInt32))(57, 'OMGetBlendState', ((1, 'ppBlendState'),(1, 'BlendFactor'),(1, 'pSampleMask'),)))
    ID3D10Device.OMGetDepthStencilState = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilState_head),POINTER(UInt32))(58, 'OMGetDepthStencilState', ((1, 'ppDepthStencilState'),(1, 'pStencilRef'),)))
    ID3D10Device.SOGetTargets = COMMETHOD(WINFUNCTYPE(Void,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head),POINTER(UInt32))(59, 'SOGetTargets', ((1, 'NumBuffers'),(1, 'ppSOTargets'),(1, 'pOffsets'),)))
    ID3D10Device.RSGetState = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10RasterizerState_head))(60, 'RSGetState', ((1, 'ppRasterizerState'),)))
    ID3D10Device.RSGetViewports = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Graphics.Direct3D10.D3D10_VIEWPORT_head))(61, 'RSGetViewports', ((1, 'NumViewports'),(1, 'pViewports'),)))
    ID3D10Device.RSGetScissorRects = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32),POINTER(win32more.Foundation.RECT_head))(62, 'RSGetScissorRects', ((1, 'NumRects'),(1, 'pRects'),)))
    ID3D10Device.GetDeviceRemovedReason = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(63, 'GetDeviceRemovedReason', ()))
    ID3D10Device.SetExceptionMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(64, 'SetExceptionMode', ((1, 'RaiseFlags'),)))
    ID3D10Device.GetExceptionMode = COMMETHOD(WINFUNCTYPE(UInt32,)(65, 'GetExceptionMode', ()))
    ID3D10Device.GetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),c_void_p)(66, 'GetPrivateData', ((1, 'guid'),(1, 'pDataSize'),(1, 'pData'),)))
    ID3D10Device.SetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,c_void_p)(67, 'SetPrivateData', ((1, 'guid'),(1, 'DataSize'),(1, 'pData'),)))
    ID3D10Device.SetPrivateDataInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(68, 'SetPrivateDataInterface', ((1, 'guid'),(1, 'pData'),)))
    ID3D10Device.ClearState = COMMETHOD(WINFUNCTYPE(Void,)(69, 'ClearState', ()))
    ID3D10Device.Flush = COMMETHOD(WINFUNCTYPE(Void,)(70, 'Flush', ()))
    ID3D10Device.CreateBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_BUFFER_DESC_head),POINTER(win32more.Graphics.Direct3D10.D3D10_SUBRESOURCE_DATA_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(71, 'CreateBuffer', ((1, 'pDesc'),(1, 'pInitialData'),(1, 'ppBuffer'),)))
    ID3D10Device.CreateTexture1D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE1D_DESC_head),POINTER(win32more.Graphics.Direct3D10.D3D10_SUBRESOURCE_DATA_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Texture1D_head))(72, 'CreateTexture1D', ((1, 'pDesc'),(1, 'pInitialData'),(1, 'ppTexture1D'),)))
    ID3D10Device.CreateTexture2D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE2D_DESC_head),POINTER(win32more.Graphics.Direct3D10.D3D10_SUBRESOURCE_DATA_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Texture2D_head))(73, 'CreateTexture2D', ((1, 'pDesc'),(1, 'pInitialData'),(1, 'ppTexture2D'),)))
    ID3D10Device.CreateTexture3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE3D_DESC_head),POINTER(win32more.Graphics.Direct3D10.D3D10_SUBRESOURCE_DATA_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Texture3D_head))(74, 'CreateTexture3D', ((1, 'pDesc'),(1, 'pInitialData'),(1, 'ppTexture3D'),)))
    ID3D10Device.CreateShaderResourceView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Resource_head,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(75, 'CreateShaderResourceView', ((1, 'pResource'),(1, 'pDesc'),(1, 'ppSRView'),)))
    ID3D10Device.CreateRenderTargetView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Resource_head,POINTER(win32more.Graphics.Direct3D10.D3D10_RENDER_TARGET_VIEW_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head))(76, 'CreateRenderTargetView', ((1, 'pResource'),(1, 'pDesc'),(1, 'ppRTView'),)))
    ID3D10Device.CreateDepthStencilView = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Resource_head,POINTER(win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_VIEW_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head))(77, 'CreateDepthStencilView', ((1, 'pResource'),(1, 'pDesc'),(1, 'ppDepthStencilView'),)))
    ID3D10Device.CreateInputLayout = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INPUT_ELEMENT_DESC_head),UInt32,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.ID3D10InputLayout_head))(78, 'CreateInputLayout', ((1, 'pInputElementDescs'),(1, 'NumElements'),(1, 'pShaderBytecodeWithInputSignature'),(1, 'BytecodeLength'),(1, 'ppInputLayout'),)))
    ID3D10Device.CreateVertexShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.ID3D10VertexShader_head))(79, 'CreateVertexShader', ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppVertexShader'),)))
    ID3D10Device.CreateGeometryShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.ID3D10GeometryShader_head))(80, 'CreateGeometryShader', ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppGeometryShader'),)))
    ID3D10Device.CreateGeometryShaderWithStreamOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.D3D10_SO_DECLARATION_ENTRY_head),UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10GeometryShader_head))(81, 'CreateGeometryShaderWithStreamOutput', ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'pSODeclaration'),(1, 'NumEntries'),(1, 'OutputStreamStride'),(1, 'ppGeometryShader'),)))
    ID3D10Device.CreatePixelShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UIntPtr,POINTER(win32more.Graphics.Direct3D10.ID3D10PixelShader_head))(82, 'CreatePixelShader', ((1, 'pShaderBytecode'),(1, 'BytecodeLength'),(1, 'ppPixelShader'),)))
    ID3D10Device.CreateBlendState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_BLEND_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10BlendState_head))(83, 'CreateBlendState', ((1, 'pBlendStateDesc'),(1, 'ppBlendState'),)))
    ID3D10Device.CreateDepthStencilState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilState_head))(84, 'CreateDepthStencilState', ((1, 'pDepthStencilDesc'),(1, 'ppDepthStencilState'),)))
    ID3D10Device.CreateRasterizerState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_RASTERIZER_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10RasterizerState_head))(85, 'CreateRasterizerState', ((1, 'pRasterizerDesc'),(1, 'ppRasterizerState'),)))
    ID3D10Device.CreateSamplerState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SAMPLER_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(86, 'CreateSamplerState', ((1, 'pSamplerDesc'),(1, 'ppSamplerState'),)))
    ID3D10Device.CreateQuery = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_QUERY_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Query_head))(87, 'CreateQuery', ((1, 'pQueryDesc'),(1, 'ppQuery'),)))
    ID3D10Device.CreatePredicate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_QUERY_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Predicate_head))(88, 'CreatePredicate', ((1, 'pPredicateDesc'),(1, 'ppPredicate'),)))
    ID3D10Device.CreateCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_COUNTER_DESC_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Counter_head))(89, 'CreateCounter', ((1, 'pCounterDesc'),(1, 'ppCounter'),)))
    ID3D10Device.CheckFormatSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,POINTER(UInt32))(90, 'CheckFormatSupport', ((1, 'Format'),(1, 'pFormatSupport'),)))
    ID3D10Device.CheckMultisampleQualityLevels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.Common.DXGI_FORMAT,UInt32,POINTER(UInt32))(91, 'CheckMultisampleQualityLevels', ((1, 'Format'),(1, 'SampleCount'),(1, 'pNumQualityLevels'),)))
    ID3D10Device.CheckCounterInfo = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_COUNTER_INFO_head))(92, 'CheckCounterInfo', ((1, 'pCounterInfo'),)))
    ID3D10Device.CheckCounter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_COUNTER_DESC_head),POINTER(win32more.Graphics.Direct3D10.D3D10_COUNTER_TYPE),POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32))(93, 'CheckCounter', ((1, 'pDesc'),(1, 'pType'),(1, 'pActiveCounters'),(1, 'szName'),(1, 'pNameLength'),(1, 'szUnits'),(1, 'pUnitsLength'),(1, 'szDescription'),(1, 'pDescriptionLength'),)))
    ID3D10Device.GetCreationFlags = COMMETHOD(WINFUNCTYPE(UInt32,)(94, 'GetCreationFlags', ()))
    ID3D10Device.OpenSharedResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,POINTER(Guid),POINTER(c_void_p))(95, 'OpenSharedResource', ((1, 'hResource'),(1, 'ReturnedInterface'),(1, 'ppResource'),)))
    ID3D10Device.SetTextFilterSize = COMMETHOD(WINFUNCTYPE(Void,UInt32,UInt32)(96, 'SetTextFilterSize', ((1, 'Width'),(1, 'Height'),)))
    ID3D10Device.GetTextFilterSize = COMMETHOD(WINFUNCTYPE(Void,POINTER(UInt32),POINTER(UInt32))(97, 'GetTextFilterSize', ((1, 'pWidth'),(1, 'pHeight'),)))
    win32more.System.Com.IUnknown
    return ID3D10Device
def _define_ID3D10Device1_head():
    class ID3D10Device1(win32more.Graphics.Direct3D10.ID3D10Device_head):
        Guid = Guid('9b7e4c8f-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Device1
def _define_ID3D10Device1():
    ID3D10Device1 = win32more.Graphics.Direct3D10.ID3D10Device1_head
    ID3D10Device1.CreateShaderResourceView1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Resource_head,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC1_head),POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView1_head))(98, 'CreateShaderResourceView1', ((1, 'pResource'),(1, 'pDesc'),(1, 'ppSRView'),)))
    ID3D10Device1.CreateBlendState1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_BLEND_DESC1_head),POINTER(win32more.Graphics.Direct3D10.ID3D10BlendState1_head))(99, 'CreateBlendState1', ((1, 'pBlendStateDesc'),(1, 'ppBlendState'),)))
    ID3D10Device1.GetFeatureLevel = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.D3D10_FEATURE_LEVEL1,)(100, 'GetFeatureLevel', ()))
    win32more.Graphics.Direct3D10.ID3D10Device
    return ID3D10Device1
def _define_ID3D10DeviceChild_head():
    class ID3D10DeviceChild(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b7e4c00-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10DeviceChild
def _define_ID3D10DeviceChild():
    ID3D10DeviceChild = win32more.Graphics.Direct3D10.ID3D10DeviceChild_head
    ID3D10DeviceChild.GetDevice = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10Device_head))(3, 'GetDevice', ((1, 'ppDevice'),)))
    ID3D10DeviceChild.GetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),POINTER(UInt32),c_void_p)(4, 'GetPrivateData', ((1, 'guid'),(1, 'pDataSize'),(1, 'pData'),)))
    ID3D10DeviceChild.SetPrivateData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),UInt32,c_void_p)(5, 'SetPrivateData', ((1, 'guid'),(1, 'DataSize'),(1, 'pData'),)))
    ID3D10DeviceChild.SetPrivateDataInterface = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),win32more.System.Com.IUnknown_head)(6, 'SetPrivateDataInterface', ((1, 'guid'),(1, 'pData'),)))
    win32more.System.Com.IUnknown
    return ID3D10DeviceChild
def _define_ID3D10Effect_head():
    class ID3D10Effect(win32more.System.Com.IUnknown_head):
        Guid = Guid('51b0ca8b-ec0b-4519-87-0d-8e-e1-cb-50-17-c7')
    return ID3D10Effect
def _define_ID3D10Effect():
    ID3D10Effect = win32more.Graphics.Direct3D10.ID3D10Effect_head
    ID3D10Effect.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(3, 'IsValid', ()))
    ID3D10Effect.IsPool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(4, 'IsPool', ()))
    ID3D10Effect.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10Device_head))(5, 'GetDevice', ((1, 'ppDevice'),)))
    ID3D10Effect.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_EFFECT_DESC_head))(6, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10Effect.GetConstantBufferByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectConstantBuffer_head,UInt32)(7, 'GetConstantBufferByIndex', ((1, 'Index'),)))
    ID3D10Effect.GetConstantBufferByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectConstantBuffer_head,win32more.Foundation.PSTR)(8, 'GetConstantBufferByName', ((1, 'Name'),)))
    ID3D10Effect.GetVariableByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(9, 'GetVariableByIndex', ((1, 'Index'),)))
    ID3D10Effect.GetVariableByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(10, 'GetVariableByName', ((1, 'Name'),)))
    ID3D10Effect.GetVariableBySemantic = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(11, 'GetVariableBySemantic', ((1, 'Semantic'),)))
    ID3D10Effect.GetTechniqueByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectTechnique_head,UInt32)(12, 'GetTechniqueByIndex', ((1, 'Index'),)))
    ID3D10Effect.GetTechniqueByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectTechnique_head,win32more.Foundation.PSTR)(13, 'GetTechniqueByName', ((1, 'Name'),)))
    ID3D10Effect.Optimize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Optimize', ()))
    ID3D10Effect.IsOptimized = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(15, 'IsOptimized', ()))
    win32more.System.Com.IUnknown
    return ID3D10Effect
def _define_ID3D10EffectBlendVariable_head():
    class ID3D10EffectBlendVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('1fcd2294-df6d-4eae-86-b3-0e-91-60-cf-b0-7b')
    return ID3D10EffectBlendVariable
def _define_ID3D10EffectBlendVariable():
    ID3D10EffectBlendVariable = win32more.Graphics.Direct3D10.ID3D10EffectBlendVariable_head
    ID3D10EffectBlendVariable.GetBlendState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10BlendState_head))(25, 'GetBlendState', ((1, 'Index'),(1, 'ppBlendState'),)))
    ID3D10EffectBlendVariable.GetBackingStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_BLEND_DESC_head))(26, 'GetBackingStore', ((1, 'Index'),(1, 'pBlendDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectBlendVariable
def _define_ID3D10EffectConstantBuffer_head():
    class ID3D10EffectConstantBuffer(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('56648f4d-cc8b-4444-a5-ad-b5-a3-d7-6e-91-b3')
    return ID3D10EffectConstantBuffer
def _define_ID3D10EffectConstantBuffer():
    ID3D10EffectConstantBuffer = win32more.Graphics.Direct3D10.ID3D10EffectConstantBuffer_head
    ID3D10EffectConstantBuffer.SetConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10Buffer_head)(25, 'SetConstantBuffer', ((1, 'pConstantBuffer'),)))
    ID3D10EffectConstantBuffer.GetConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10Buffer_head))(26, 'GetConstantBuffer', ((1, 'ppConstantBuffer'),)))
    ID3D10EffectConstantBuffer.SetTextureBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head)(27, 'SetTextureBuffer', ((1, 'pTextureBuffer'),)))
    ID3D10EffectConstantBuffer.GetTextureBuffer = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(28, 'GetTextureBuffer', ((1, 'ppTextureBuffer'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectConstantBuffer
def _define_ID3D10EffectDepthStencilVariable_head():
    class ID3D10EffectDepthStencilVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('af482368-330a-46a5-9a-5c-01-c7-1a-f2-4c-8d')
    return ID3D10EffectDepthStencilVariable
def _define_ID3D10EffectDepthStencilVariable():
    ID3D10EffectDepthStencilVariable = win32more.Graphics.Direct3D10.ID3D10EffectDepthStencilVariable_head
    ID3D10EffectDepthStencilVariable.GetDepthStencilState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilState_head))(25, 'GetDepthStencilState', ((1, 'Index'),(1, 'ppDepthStencilState'),)))
    ID3D10EffectDepthStencilVariable.GetBackingStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_DEPTH_STENCIL_DESC_head))(26, 'GetBackingStore', ((1, 'Index'),(1, 'pDepthStencilDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectDepthStencilVariable
def _define_ID3D10EffectDepthStencilViewVariable_head():
    class ID3D10EffectDepthStencilViewVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('3e02c918-cc79-4985-b6-22-2d-92-ad-70-16-23')
    return ID3D10EffectDepthStencilViewVariable
def _define_ID3D10EffectDepthStencilViewVariable():
    ID3D10EffectDepthStencilViewVariable = win32more.Graphics.Direct3D10.ID3D10EffectDepthStencilViewVariable_head
    ID3D10EffectDepthStencilViewVariable.SetDepthStencil = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head)(25, 'SetDepthStencil', ((1, 'pResource'),)))
    ID3D10EffectDepthStencilViewVariable.GetDepthStencil = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head))(26, 'GetDepthStencil', ((1, 'ppResource'),)))
    ID3D10EffectDepthStencilViewVariable.SetDepthStencilArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head),UInt32,UInt32)(27, 'SetDepthStencilArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectDepthStencilViewVariable.GetDepthStencilArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10DepthStencilView_head),UInt32,UInt32)(28, 'GetDepthStencilArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectDepthStencilViewVariable
def _define_ID3D10EffectMatrixVariable_head():
    class ID3D10EffectMatrixVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('50666c24-b82f-4eed-a1-72-5b-6e-7e-85-22-e0')
    return ID3D10EffectMatrixVariable
def _define_ID3D10EffectMatrixVariable():
    ID3D10EffectMatrixVariable = win32more.Graphics.Direct3D10.ID3D10EffectMatrixVariable_head
    ID3D10EffectMatrixVariable.SetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(25, 'SetMatrix', ((1, 'pData'),)))
    ID3D10EffectMatrixVariable.GetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(26, 'GetMatrix', ((1, 'pData'),)))
    ID3D10EffectMatrixVariable.SetMatrixArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(27, 'SetMatrixArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectMatrixVariable.GetMatrixArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(28, 'GetMatrixArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectMatrixVariable.SetMatrixTranspose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(29, 'SetMatrixTranspose', ((1, 'pData'),)))
    ID3D10EffectMatrixVariable.GetMatrixTranspose = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(30, 'GetMatrixTranspose', ((1, 'pData'),)))
    ID3D10EffectMatrixVariable.SetMatrixTransposeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(31, 'SetMatrixTransposeArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectMatrixVariable.GetMatrixTransposeArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(32, 'GetMatrixTransposeArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectMatrixVariable
def _define_ID3D10EffectPass_head():
    class ID3D10EffectPass(c_void_p):
        Guid = Guid('5cfbeb89-1a06-46e0-b2-82-e3-f9-bf-a3-6a-54')
    return ID3D10EffectPass
def _define_ID3D10EffectPass():
    ID3D10EffectPass = win32more.Graphics.Direct3D10.ID3D10EffectPass_head
    ID3D10EffectPass.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(0, 'IsValid', ()))
    ID3D10EffectPass.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_PASS_DESC_head))(1, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10EffectPass.GetVertexShaderDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_PASS_SHADER_DESC_head))(2, 'GetVertexShaderDesc', ((1, 'pDesc'),)))
    ID3D10EffectPass.GetGeometryShaderDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_PASS_SHADER_DESC_head))(3, 'GetGeometryShaderDesc', ((1, 'pDesc'),)))
    ID3D10EffectPass.GetPixelShaderDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_PASS_SHADER_DESC_head))(4, 'GetPixelShaderDesc', ((1, 'pDesc'),)))
    ID3D10EffectPass.GetAnnotationByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(5, 'GetAnnotationByIndex', ((1, 'Index'),)))
    ID3D10EffectPass.GetAnnotationByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(6, 'GetAnnotationByName', ((1, 'Name'),)))
    ID3D10EffectPass.Apply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'Apply', ((1, 'Flags'),)))
    ID3D10EffectPass.ComputeStateBlockMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(8, 'ComputeStateBlockMask', ((1, 'pStateBlockMask'),)))
    return ID3D10EffectPass
def _define_ID3D10EffectPool_head():
    class ID3D10EffectPool(win32more.System.Com.IUnknown_head):
        Guid = Guid('9537ab04-3250-412e-82-13-fc-d2-f8-67-79-33')
    return ID3D10EffectPool
def _define_ID3D10EffectPool():
    ID3D10EffectPool = win32more.Graphics.Direct3D10.ID3D10EffectPool_head
    ID3D10EffectPool.AsEffect = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10Effect_head,)(3, 'AsEffect', ()))
    win32more.System.Com.IUnknown
    return ID3D10EffectPool
def _define_ID3D10EffectRasterizerVariable_head():
    class ID3D10EffectRasterizerVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('21af9f0e-4d94-4ea9-97-85-2c-b7-6b-8c-0b-34')
    return ID3D10EffectRasterizerVariable
def _define_ID3D10EffectRasterizerVariable():
    ID3D10EffectRasterizerVariable = win32more.Graphics.Direct3D10.ID3D10EffectRasterizerVariable_head
    ID3D10EffectRasterizerVariable.GetRasterizerState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10RasterizerState_head))(25, 'GetRasterizerState', ((1, 'Index'),(1, 'ppRasterizerState'),)))
    ID3D10EffectRasterizerVariable.GetBackingStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_RASTERIZER_DESC_head))(26, 'GetBackingStore', ((1, 'Index'),(1, 'pRasterizerDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectRasterizerVariable
def _define_ID3D10EffectRenderTargetViewVariable_head():
    class ID3D10EffectRenderTargetViewVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('28ca0cc3-c2c9-40bb-b5-7f-67-b7-37-12-2b-17')
    return ID3D10EffectRenderTargetViewVariable
def _define_ID3D10EffectRenderTargetViewVariable():
    ID3D10EffectRenderTargetViewVariable = win32more.Graphics.Direct3D10.ID3D10EffectRenderTargetViewVariable_head
    ID3D10EffectRenderTargetViewVariable.SetRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head)(25, 'SetRenderTarget', ((1, 'pResource'),)))
    ID3D10EffectRenderTargetViewVariable.GetRenderTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head))(26, 'GetRenderTarget', ((1, 'ppResource'),)))
    ID3D10EffectRenderTargetViewVariable.SetRenderTargetArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head),UInt32,UInt32)(27, 'SetRenderTargetArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectRenderTargetViewVariable.GetRenderTargetArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head),UInt32,UInt32)(28, 'GetRenderTargetArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectRenderTargetViewVariable
def _define_ID3D10EffectSamplerVariable_head():
    class ID3D10EffectSamplerVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('6530d5c7-07e9-4271-a4-18-e7-ce-4b-d1-e4-80')
    return ID3D10EffectSamplerVariable
def _define_ID3D10EffectSamplerVariable():
    ID3D10EffectSamplerVariable = win32more.Graphics.Direct3D10.ID3D10EffectSamplerVariable_head
    ID3D10EffectSamplerVariable.GetSampler = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10SamplerState_head))(25, 'GetSampler', ((1, 'Index'),(1, 'ppSampler'),)))
    ID3D10EffectSamplerVariable.GetBackingStore = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SAMPLER_DESC_head))(26, 'GetBackingStore', ((1, 'Index'),(1, 'pSamplerDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectSamplerVariable
def _define_ID3D10EffectScalarVariable_head():
    class ID3D10EffectScalarVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('00e48f7b-d2c8-49e8-a8-6c-02-2d-ee-53-43-1f')
    return ID3D10EffectScalarVariable
def _define_ID3D10EffectScalarVariable():
    ID3D10EffectScalarVariable = win32more.Graphics.Direct3D10.ID3D10EffectScalarVariable_head
    ID3D10EffectScalarVariable.SetFloat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(25, 'SetFloat', ((1, 'Value'),)))
    ID3D10EffectScalarVariable.GetFloat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(26, 'GetFloat', ((1, 'pValue'),)))
    ID3D10EffectScalarVariable.SetFloatArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(27, 'SetFloatArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectScalarVariable.GetFloatArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(28, 'GetFloatArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectScalarVariable.SetInt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32)(29, 'SetInt', ((1, 'Value'),)))
    ID3D10EffectScalarVariable.GetInt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(30, 'GetInt', ((1, 'pValue'),)))
    ID3D10EffectScalarVariable.SetIntArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,UInt32)(31, 'SetIntArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectScalarVariable.GetIntArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,UInt32)(32, 'GetIntArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectScalarVariable.SetBool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(33, 'SetBool', ((1, 'Value'),)))
    ID3D10EffectScalarVariable.GetBool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(34, 'GetBool', ((1, 'pValue'),)))
    ID3D10EffectScalarVariable.SetBoolArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,UInt32)(35, 'SetBoolArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectScalarVariable.GetBoolArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,UInt32)(36, 'GetBoolArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectScalarVariable
def _define_ID3D10EffectShaderResourceVariable_head():
    class ID3D10EffectShaderResourceVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('c0a7157b-d872-4b1d-80-73-ef-c2-ac-d4-b1-fc')
    return ID3D10EffectShaderResourceVariable
def _define_ID3D10EffectShaderResourceVariable():
    ID3D10EffectShaderResourceVariable = win32more.Graphics.Direct3D10.ID3D10EffectShaderResourceVariable_head
    ID3D10EffectShaderResourceVariable.SetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head)(25, 'SetResource', ((1, 'pResource'),)))
    ID3D10EffectShaderResourceVariable.GetResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head))(26, 'GetResource', ((1, 'ppResource'),)))
    ID3D10EffectShaderResourceVariable.SetResourceArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head),UInt32,UInt32)(27, 'SetResourceArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectShaderResourceVariable.GetResourceArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head),UInt32,UInt32)(28, 'GetResourceArray', ((1, 'ppResources'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectShaderResourceVariable
def _define_ID3D10EffectShaderVariable_head():
    class ID3D10EffectShaderVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('80849279-c799-4797-8c-33-04-07-a0-7d-9e-06')
    return ID3D10EffectShaderVariable
def _define_ID3D10EffectShaderVariable():
    ID3D10EffectShaderVariable = win32more.Graphics.Direct3D10.ID3D10EffectShaderVariable_head
    ID3D10EffectShaderVariable.GetShaderDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_EFFECT_SHADER_DESC_head))(25, 'GetShaderDesc', ((1, 'ShaderIndex'),(1, 'pDesc'),)))
    ID3D10EffectShaderVariable.GetVertexShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10VertexShader_head))(26, 'GetVertexShader', ((1, 'ShaderIndex'),(1, 'ppVS'),)))
    ID3D10EffectShaderVariable.GetGeometryShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10GeometryShader_head))(27, 'GetGeometryShader', ((1, 'ShaderIndex'),(1, 'ppGS'),)))
    ID3D10EffectShaderVariable.GetPixelShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10PixelShader_head))(28, 'GetPixelShader', ((1, 'ShaderIndex'),(1, 'ppPS'),)))
    ID3D10EffectShaderVariable.GetInputSignatureElementDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(29, 'GetInputSignatureElementDesc', ((1, 'ShaderIndex'),(1, 'Element'),(1, 'pDesc'),)))
    ID3D10EffectShaderVariable.GetOutputSignatureElementDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(30, 'GetOutputSignatureElementDesc', ((1, 'ShaderIndex'),(1, 'Element'),(1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectShaderVariable
def _define_ID3D10EffectStringVariable_head():
    class ID3D10EffectStringVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('71417501-8df9-4e0a-a7-8a-25-5f-97-56-ba-ff')
    return ID3D10EffectStringVariable
def _define_ID3D10EffectStringVariable():
    ID3D10EffectStringVariable = win32more.Graphics.Direct3D10.ID3D10EffectStringVariable_head
    ID3D10EffectStringVariable.GetString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSTR))(25, 'GetString', ((1, 'ppString'),)))
    ID3D10EffectStringVariable.GetStringArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSTR),UInt32,UInt32)(26, 'GetStringArray', ((1, 'ppStrings'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectStringVariable
def _define_ID3D10EffectTechnique_head():
    class ID3D10EffectTechnique(c_void_p):
        Guid = Guid('db122ce8-d1c9-4292-b2-37-24-ed-3d-e8-b1-75')
    return ID3D10EffectTechnique
def _define_ID3D10EffectTechnique():
    ID3D10EffectTechnique = win32more.Graphics.Direct3D10.ID3D10EffectTechnique_head
    ID3D10EffectTechnique.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(0, 'IsValid', ()))
    ID3D10EffectTechnique.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_TECHNIQUE_DESC_head))(1, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10EffectTechnique.GetAnnotationByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(2, 'GetAnnotationByIndex', ((1, 'Index'),)))
    ID3D10EffectTechnique.GetAnnotationByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(3, 'GetAnnotationByName', ((1, 'Name'),)))
    ID3D10EffectTechnique.GetPassByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectPass_head,UInt32)(4, 'GetPassByIndex', ((1, 'Index'),)))
    ID3D10EffectTechnique.GetPassByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectPass_head,win32more.Foundation.PSTR)(5, 'GetPassByName', ((1, 'Name'),)))
    ID3D10EffectTechnique.ComputeStateBlockMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_STATE_BLOCK_MASK_head))(6, 'ComputeStateBlockMask', ((1, 'pStateBlockMask'),)))
    return ID3D10EffectTechnique
def _define_ID3D10EffectType_head():
    class ID3D10EffectType(c_void_p):
        Guid = Guid('4e9e1ddc-cd9d-4772-a8-37-00-18-0b-9b-88-fd')
    return ID3D10EffectType
def _define_ID3D10EffectType():
    ID3D10EffectType = win32more.Graphics.Direct3D10.ID3D10EffectType_head
    ID3D10EffectType.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(0, 'IsValid', ()))
    ID3D10EffectType.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_EFFECT_TYPE_DESC_head))(1, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10EffectType.GetMemberTypeByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectType_head,UInt32)(2, 'GetMemberTypeByIndex', ((1, 'Index'),)))
    ID3D10EffectType.GetMemberTypeByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectType_head,win32more.Foundation.PSTR)(3, 'GetMemberTypeByName', ((1, 'Name'),)))
    ID3D10EffectType.GetMemberTypeBySemantic = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectType_head,win32more.Foundation.PSTR)(4, 'GetMemberTypeBySemantic', ((1, 'Semantic'),)))
    ID3D10EffectType.GetMemberName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.PSTR,UInt32)(5, 'GetMemberName', ((1, 'Index'),)))
    ID3D10EffectType.GetMemberSemantic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.PSTR,UInt32)(6, 'GetMemberSemantic', ((1, 'Index'),)))
    return ID3D10EffectType
def _define_ID3D10EffectVariable_head():
    class ID3D10EffectVariable(c_void_p):
        Guid = Guid('ae897105-00e6-45bf-bb-8e-28-1d-d6-db-8e-1b')
    return ID3D10EffectVariable
def _define_ID3D10EffectVariable():
    ID3D10EffectVariable = win32more.Graphics.Direct3D10.ID3D10EffectVariable_head
    ID3D10EffectVariable.IsValid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(0, 'IsValid', ()))
    ID3D10EffectVariable.GetType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectType_head,)(1, 'GetType', ()))
    ID3D10EffectVariable.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_EFFECT_VARIABLE_DESC_head))(2, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10EffectVariable.GetAnnotationByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(3, 'GetAnnotationByIndex', ((1, 'Index'),)))
    ID3D10EffectVariable.GetAnnotationByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(4, 'GetAnnotationByName', ((1, 'Name'),)))
    ID3D10EffectVariable.GetMemberByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(5, 'GetMemberByIndex', ((1, 'Index'),)))
    ID3D10EffectVariable.GetMemberByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(6, 'GetMemberByName', ((1, 'Name'),)))
    ID3D10EffectVariable.GetMemberBySemantic = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,win32more.Foundation.PSTR)(7, 'GetMemberBySemantic', ((1, 'Semantic'),)))
    ID3D10EffectVariable.GetElement = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head,UInt32)(8, 'GetElement', ((1, 'Index'),)))
    ID3D10EffectVariable.GetParentConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectConstantBuffer_head,)(9, 'GetParentConstantBuffer', ()))
    ID3D10EffectVariable.AsScalar = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectScalarVariable_head,)(10, 'AsScalar', ()))
    ID3D10EffectVariable.AsVector = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectVectorVariable_head,)(11, 'AsVector', ()))
    ID3D10EffectVariable.AsMatrix = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectMatrixVariable_head,)(12, 'AsMatrix', ()))
    ID3D10EffectVariable.AsString = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectStringVariable_head,)(13, 'AsString', ()))
    ID3D10EffectVariable.AsShaderResource = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectShaderResourceVariable_head,)(14, 'AsShaderResource', ()))
    ID3D10EffectVariable.AsRenderTargetView = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectRenderTargetViewVariable_head,)(15, 'AsRenderTargetView', ()))
    ID3D10EffectVariable.AsDepthStencilView = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectDepthStencilViewVariable_head,)(16, 'AsDepthStencilView', ()))
    ID3D10EffectVariable.AsConstantBuffer = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectConstantBuffer_head,)(17, 'AsConstantBuffer', ()))
    ID3D10EffectVariable.AsShader = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectShaderVariable_head,)(18, 'AsShader', ()))
    ID3D10EffectVariable.AsBlend = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectBlendVariable_head,)(19, 'AsBlend', ()))
    ID3D10EffectVariable.AsDepthStencil = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectDepthStencilVariable_head,)(20, 'AsDepthStencil', ()))
    ID3D10EffectVariable.AsRasterizer = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectRasterizerVariable_head,)(21, 'AsRasterizer', ()))
    ID3D10EffectVariable.AsSampler = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10EffectSamplerVariable_head,)(22, 'AsSampler', ()))
    ID3D10EffectVariable.SetRawValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32)(23, 'SetRawValue', ((1, 'pData'),(1, 'Offset'),(1, 'ByteCount'),)))
    ID3D10EffectVariable.GetRawValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32,UInt32)(24, 'GetRawValue', ((1, 'pData'),(1, 'Offset'),(1, 'ByteCount'),)))
    return ID3D10EffectVariable
def _define_ID3D10EffectVectorVariable_head():
    class ID3D10EffectVectorVariable(win32more.Graphics.Direct3D10.ID3D10EffectVariable_head):
        Guid = Guid('62b98c44-1f82-4c67-bc-d0-72-cf-8f-21-7e-81')
    return ID3D10EffectVectorVariable
def _define_ID3D10EffectVectorVariable():
    ID3D10EffectVectorVariable = win32more.Graphics.Direct3D10.ID3D10EffectVectorVariable_head
    ID3D10EffectVectorVariable.SetBoolVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(25, 'SetBoolVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.SetIntVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(26, 'SetIntVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.SetFloatVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(27, 'SetFloatVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.GetBoolVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(28, 'GetBoolVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.GetIntVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32))(29, 'GetIntVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.GetFloatVector = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(30, 'GetFloatVector', ((1, 'pData'),)))
    ID3D10EffectVectorVariable.SetBoolVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,UInt32)(31, 'SetBoolVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectVectorVariable.SetIntVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,UInt32)(32, 'SetIntVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectVectorVariable.SetFloatVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(33, 'SetFloatVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectVectorVariable.GetBoolVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL),UInt32,UInt32)(34, 'GetBoolVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectVectorVariable.GetIntVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),UInt32,UInt32)(35, 'GetIntVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    ID3D10EffectVectorVariable.GetFloatVectorArray = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single),UInt32,UInt32)(36, 'GetFloatVectorArray', ((1, 'pData'),(1, 'Offset'),(1, 'Count'),)))
    win32more.Graphics.Direct3D10.ID3D10EffectVariable
    return ID3D10EffectVectorVariable
def _define_ID3D10GeometryShader_head():
    class ID3D10GeometryShader(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('6316be88-54cd-4040-ab-44-20-46-1b-c8-1f-68')
    return ID3D10GeometryShader
def _define_ID3D10GeometryShader():
    ID3D10GeometryShader = win32more.Graphics.Direct3D10.ID3D10GeometryShader_head
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10GeometryShader
def _define_ID3D10InfoQueue_head():
    class ID3D10InfoQueue(win32more.System.Com.IUnknown_head):
        Guid = Guid('1b940b17-2642-4d1f-ab-1f-b9-9b-ad-0c-39-5f')
    return ID3D10InfoQueue
def _define_ID3D10InfoQueue():
    ID3D10InfoQueue = win32more.Graphics.Direct3D10.ID3D10InfoQueue_head
    ID3D10InfoQueue.SetMessageCountLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64)(3, 'SetMessageCountLimit', ((1, 'MessageCountLimit'),)))
    ID3D10InfoQueue.ClearStoredMessages = COMMETHOD(WINFUNCTYPE(Void,)(4, 'ClearStoredMessages', ()))
    ID3D10InfoQueue.GetMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Graphics.Direct3D10.D3D10_MESSAGE_head),POINTER(UIntPtr))(5, 'GetMessage', ((1, 'MessageIndex'),(1, 'pMessage'),(1, 'pMessageByteLength'),)))
    ID3D10InfoQueue.GetNumMessagesAllowedByStorageFilter = COMMETHOD(WINFUNCTYPE(UInt64,)(6, 'GetNumMessagesAllowedByStorageFilter', ()))
    ID3D10InfoQueue.GetNumMessagesDeniedByStorageFilter = COMMETHOD(WINFUNCTYPE(UInt64,)(7, 'GetNumMessagesDeniedByStorageFilter', ()))
    ID3D10InfoQueue.GetNumStoredMessages = COMMETHOD(WINFUNCTYPE(UInt64,)(8, 'GetNumStoredMessages', ()))
    ID3D10InfoQueue.GetNumStoredMessagesAllowedByRetrievalFilter = COMMETHOD(WINFUNCTYPE(UInt64,)(9, 'GetNumStoredMessagesAllowedByRetrievalFilter', ()))
    ID3D10InfoQueue.GetNumMessagesDiscardedByMessageCountLimit = COMMETHOD(WINFUNCTYPE(UInt64,)(10, 'GetNumMessagesDiscardedByMessageCountLimit', ()))
    ID3D10InfoQueue.GetMessageCountLimit = COMMETHOD(WINFUNCTYPE(UInt64,)(11, 'GetMessageCountLimit', ()))
    ID3D10InfoQueue.AddStorageFilterEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head))(12, 'AddStorageFilterEntries', ((1, 'pFilter'),)))
    ID3D10InfoQueue.GetStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head),POINTER(UIntPtr))(13, 'GetStorageFilter', ((1, 'pFilter'),(1, 'pFilterByteLength'),)))
    ID3D10InfoQueue.ClearStorageFilter = COMMETHOD(WINFUNCTYPE(Void,)(14, 'ClearStorageFilter', ()))
    ID3D10InfoQueue.PushEmptyStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(15, 'PushEmptyStorageFilter', ()))
    ID3D10InfoQueue.PushCopyOfStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'PushCopyOfStorageFilter', ()))
    ID3D10InfoQueue.PushStorageFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head))(17, 'PushStorageFilter', ((1, 'pFilter'),)))
    ID3D10InfoQueue.PopStorageFilter = COMMETHOD(WINFUNCTYPE(Void,)(18, 'PopStorageFilter', ()))
    ID3D10InfoQueue.GetStorageFilterStackSize = COMMETHOD(WINFUNCTYPE(UInt32,)(19, 'GetStorageFilterStackSize', ()))
    ID3D10InfoQueue.AddRetrievalFilterEntries = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head))(20, 'AddRetrievalFilterEntries', ((1, 'pFilter'),)))
    ID3D10InfoQueue.GetRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head),POINTER(UIntPtr))(21, 'GetRetrievalFilter', ((1, 'pFilter'),(1, 'pFilterByteLength'),)))
    ID3D10InfoQueue.ClearRetrievalFilter = COMMETHOD(WINFUNCTYPE(Void,)(22, 'ClearRetrievalFilter', ()))
    ID3D10InfoQueue.PushEmptyRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'PushEmptyRetrievalFilter', ()))
    ID3D10InfoQueue.PushCopyOfRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(24, 'PushCopyOfRetrievalFilter', ()))
    ID3D10InfoQueue.PushRetrievalFilter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_INFO_QUEUE_FILTER_head))(25, 'PushRetrievalFilter', ((1, 'pFilter'),)))
    ID3D10InfoQueue.PopRetrievalFilter = COMMETHOD(WINFUNCTYPE(Void,)(26, 'PopRetrievalFilter', ()))
    ID3D10InfoQueue.GetRetrievalFilterStackSize = COMMETHOD(WINFUNCTYPE(UInt32,)(27, 'GetRetrievalFilterStackSize', ()))
    ID3D10InfoQueue.AddMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MESSAGE_CATEGORY,win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY,win32more.Graphics.Direct3D10.D3D10_MESSAGE_ID,win32more.Foundation.PSTR)(28, 'AddMessage', ((1, 'Category'),(1, 'Severity'),(1, 'ID'),(1, 'pDescription'),)))
    ID3D10InfoQueue.AddApplicationMessage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY,win32more.Foundation.PSTR)(29, 'AddApplicationMessage', ((1, 'Severity'),(1, 'pDescription'),)))
    ID3D10InfoQueue.SetBreakOnCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MESSAGE_CATEGORY,win32more.Foundation.BOOL)(30, 'SetBreakOnCategory', ((1, 'Category'),(1, 'bEnable'),)))
    ID3D10InfoQueue.SetBreakOnSeverity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY,win32more.Foundation.BOOL)(31, 'SetBreakOnSeverity', ((1, 'Severity'),(1, 'bEnable'),)))
    ID3D10InfoQueue.SetBreakOnID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Direct3D10.D3D10_MESSAGE_ID,win32more.Foundation.BOOL)(32, 'SetBreakOnID', ((1, 'ID'),(1, 'bEnable'),)))
    ID3D10InfoQueue.GetBreakOnCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct3D10.D3D10_MESSAGE_CATEGORY)(33, 'GetBreakOnCategory', ((1, 'Category'),)))
    ID3D10InfoQueue.GetBreakOnSeverity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct3D10.D3D10_MESSAGE_SEVERITY)(34, 'GetBreakOnSeverity', ((1, 'Severity'),)))
    ID3D10InfoQueue.GetBreakOnID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Direct3D10.D3D10_MESSAGE_ID)(35, 'GetBreakOnID', ((1, 'ID'),)))
    ID3D10InfoQueue.SetMuteDebugOutput = COMMETHOD(WINFUNCTYPE(Void,win32more.Foundation.BOOL)(36, 'SetMuteDebugOutput', ((1, 'bMute'),)))
    ID3D10InfoQueue.GetMuteDebugOutput = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(37, 'GetMuteDebugOutput', ()))
    win32more.System.Com.IUnknown
    return ID3D10InfoQueue
def _define_ID3D10InputLayout_head():
    class ID3D10InputLayout(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('9b7e4c0b-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10InputLayout
def _define_ID3D10InputLayout():
    ID3D10InputLayout = win32more.Graphics.Direct3D10.ID3D10InputLayout_head
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10InputLayout
def _define_ID3D10Multithread_head():
    class ID3D10Multithread(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b7e4e00-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Multithread
def _define_ID3D10Multithread():
    ID3D10Multithread = win32more.Graphics.Direct3D10.ID3D10Multithread_head
    ID3D10Multithread.Enter = COMMETHOD(WINFUNCTYPE(Void,)(3, 'Enter', ()))
    ID3D10Multithread.Leave = COMMETHOD(WINFUNCTYPE(Void,)(4, 'Leave', ()))
    ID3D10Multithread.SetMultithreadProtected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(5, 'SetMultithreadProtected', ((1, 'bMTProtect'),)))
    ID3D10Multithread.GetMultithreadProtected = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(6, 'GetMultithreadProtected', ()))
    win32more.System.Com.IUnknown
    return ID3D10Multithread
def _define_ID3D10PixelShader_head():
    class ID3D10PixelShader(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('4968b601-9d00-4cde-83-46-8e-7f-67-58-19-b6')
    return ID3D10PixelShader
def _define_ID3D10PixelShader():
    ID3D10PixelShader = win32more.Graphics.Direct3D10.ID3D10PixelShader_head
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10PixelShader
def _define_ID3D10Predicate_head():
    class ID3D10Predicate(win32more.Graphics.Direct3D10.ID3D10Query_head):
        Guid = Guid('9b7e4c10-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Predicate
def _define_ID3D10Predicate():
    ID3D10Predicate = win32more.Graphics.Direct3D10.ID3D10Predicate_head
    win32more.Graphics.Direct3D10.ID3D10Query
    return ID3D10Predicate
def _define_ID3D10Query_head():
    class ID3D10Query(win32more.Graphics.Direct3D10.ID3D10Asynchronous_head):
        Guid = Guid('9b7e4c0e-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Query
def _define_ID3D10Query():
    ID3D10Query = win32more.Graphics.Direct3D10.ID3D10Query_head
    ID3D10Query.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_QUERY_DESC_head))(11, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Asynchronous
    return ID3D10Query
def _define_ID3D10RasterizerState_head():
    class ID3D10RasterizerState(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('a2a07292-89af-4345-be-2e-c5-3d-9f-bb-6e-9f')
    return ID3D10RasterizerState
def _define_ID3D10RasterizerState():
    ID3D10RasterizerState = win32more.Graphics.Direct3D10.ID3D10RasterizerState_head
    ID3D10RasterizerState.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_RASTERIZER_DESC_head))(7, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10RasterizerState
def _define_ID3D10RenderTargetView_head():
    class ID3D10RenderTargetView(win32more.Graphics.Direct3D10.ID3D10View_head):
        Guid = Guid('9b7e4c08-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10RenderTargetView
def _define_ID3D10RenderTargetView():
    ID3D10RenderTargetView = win32more.Graphics.Direct3D10.ID3D10RenderTargetView_head
    ID3D10RenderTargetView.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_RENDER_TARGET_VIEW_DESC_head))(8, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10View
    return ID3D10RenderTargetView
def _define_ID3D10Resource_head():
    class ID3D10Resource(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('9b7e4c01-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Resource
def _define_ID3D10Resource():
    ID3D10Resource = win32more.Graphics.Direct3D10.ID3D10Resource_head
    ID3D10Resource.GetType = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_RESOURCE_DIMENSION))(7, 'GetType', ((1, 'rType'),)))
    ID3D10Resource.SetEvictionPriority = COMMETHOD(WINFUNCTYPE(Void,UInt32)(8, 'SetEvictionPriority', ((1, 'EvictionPriority'),)))
    ID3D10Resource.GetEvictionPriority = COMMETHOD(WINFUNCTYPE(UInt32,)(9, 'GetEvictionPriority', ()))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10Resource
def _define_ID3D10SamplerState_head():
    class ID3D10SamplerState(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('9b7e4c0c-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10SamplerState
def _define_ID3D10SamplerState():
    ID3D10SamplerState = win32more.Graphics.Direct3D10.ID3D10SamplerState_head
    ID3D10SamplerState.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_SAMPLER_DESC_head))(7, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10SamplerState
def _define_ID3D10ShaderReflection_head():
    class ID3D10ShaderReflection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d40e20b6-f8f7-42ad-ab-20-4b-af-8f-15-df-aa')
    return ID3D10ShaderReflection
def _define_ID3D10ShaderReflection():
    ID3D10ShaderReflection = win32more.Graphics.Direct3D10.ID3D10ShaderReflection_head
    ID3D10ShaderReflection.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_DESC_head))(3, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10ShaderReflection.GetConstantBufferByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionConstantBuffer_head,UInt32)(4, 'GetConstantBufferByIndex', ((1, 'Index'),)))
    ID3D10ShaderReflection.GetConstantBufferByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionConstantBuffer_head,win32more.Foundation.PSTR)(5, 'GetConstantBufferByName', ((1, 'Name'),)))
    ID3D10ShaderReflection.GetResourceBindingDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_INPUT_BIND_DESC_head))(6, 'GetResourceBindingDesc', ((1, 'ResourceIndex'),(1, 'pDesc'),)))
    ID3D10ShaderReflection.GetInputParameterDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(7, 'GetInputParameterDesc', ((1, 'ParameterIndex'),(1, 'pDesc'),)))
    ID3D10ShaderReflection.GetOutputParameterDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(8, 'GetOutputParameterDesc', ((1, 'ParameterIndex'),(1, 'pDesc'),)))
    win32more.System.Com.IUnknown
    return ID3D10ShaderReflection
def _define_ID3D10ShaderReflection1_head():
    class ID3D10ShaderReflection1(win32more.System.Com.IUnknown_head):
        Guid = Guid('c3457783-a846-47ce-95-20-ce-a6-f6-6e-74-47')
    return ID3D10ShaderReflection1
def _define_ID3D10ShaderReflection1():
    ID3D10ShaderReflection1 = win32more.Graphics.Direct3D10.ID3D10ShaderReflection1_head
    ID3D10ShaderReflection1.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_DESC_head))(3, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10ShaderReflection1.GetConstantBufferByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionConstantBuffer_head,UInt32)(4, 'GetConstantBufferByIndex', ((1, 'Index'),)))
    ID3D10ShaderReflection1.GetConstantBufferByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionConstantBuffer_head,win32more.Foundation.PSTR)(5, 'GetConstantBufferByName', ((1, 'Name'),)))
    ID3D10ShaderReflection1.GetResourceBindingDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_INPUT_BIND_DESC_head))(6, 'GetResourceBindingDesc', ((1, 'ResourceIndex'),(1, 'pDesc'),)))
    ID3D10ShaderReflection1.GetInputParameterDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(7, 'GetInputParameterDesc', ((1, 'ParameterIndex'),(1, 'pDesc'),)))
    ID3D10ShaderReflection1.GetOutputParameterDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_SIGNATURE_PARAMETER_DESC_head))(8, 'GetOutputParameterDesc', ((1, 'ParameterIndex'),(1, 'pDesc'),)))
    ID3D10ShaderReflection1.GetVariableByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionVariable_head,win32more.Foundation.PSTR)(9, 'GetVariableByName', ((1, 'Name'),)))
    ID3D10ShaderReflection1.GetResourceBindingDescByName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_INPUT_BIND_DESC_head))(10, 'GetResourceBindingDescByName', ((1, 'Name'),(1, 'pDesc'),)))
    ID3D10ShaderReflection1.GetMovInstructionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(11, 'GetMovInstructionCount', ((1, 'pCount'),)))
    ID3D10ShaderReflection1.GetMovcInstructionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetMovcInstructionCount', ((1, 'pCount'),)))
    ID3D10ShaderReflection1.GetConversionInstructionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(13, 'GetConversionInstructionCount', ((1, 'pCount'),)))
    ID3D10ShaderReflection1.GetBitwiseInstructionCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetBitwiseInstructionCount', ((1, 'pCount'),)))
    ID3D10ShaderReflection1.GetGSInputPrimitive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D.D3D_PRIMITIVE))(15, 'GetGSInputPrimitive', ((1, 'pPrim'),)))
    ID3D10ShaderReflection1.IsLevel9Shader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(16, 'IsLevel9Shader', ((1, 'pbLevel9Shader'),)))
    ID3D10ShaderReflection1.IsSampleFrequencyShader = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(17, 'IsSampleFrequencyShader', ((1, 'pbSampleFrequency'),)))
    win32more.System.Com.IUnknown
    return ID3D10ShaderReflection1
def _define_ID3D10ShaderReflectionConstantBuffer_head():
    class ID3D10ShaderReflectionConstantBuffer(c_void_p):
        Guid = Guid('66c66a94-dddd-4b62-a6-6a-f0-da-33-c2-b4-d0')
    return ID3D10ShaderReflectionConstantBuffer
def _define_ID3D10ShaderReflectionConstantBuffer():
    ID3D10ShaderReflectionConstantBuffer = win32more.Graphics.Direct3D10.ID3D10ShaderReflectionConstantBuffer_head
    ID3D10ShaderReflectionConstantBuffer.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_BUFFER_DESC_head))(0, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10ShaderReflectionConstantBuffer.GetVariableByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionVariable_head,UInt32)(1, 'GetVariableByIndex', ((1, 'Index'),)))
    ID3D10ShaderReflectionConstantBuffer.GetVariableByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionVariable_head,win32more.Foundation.PSTR)(2, 'GetVariableByName', ((1, 'Name'),)))
    return ID3D10ShaderReflectionConstantBuffer
def _define_ID3D10ShaderReflectionType_head():
    class ID3D10ShaderReflectionType(c_void_p):
        Guid = Guid('c530ad7d-9b16-4395-a9-79-ba-2e-cf-f8-3a-dd')
    return ID3D10ShaderReflectionType
def _define_ID3D10ShaderReflectionType():
    ID3D10ShaderReflectionType = win32more.Graphics.Direct3D10.ID3D10ShaderReflectionType_head
    ID3D10ShaderReflectionType.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_TYPE_DESC_head))(0, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10ShaderReflectionType.GetMemberTypeByIndex = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionType_head,UInt32)(1, 'GetMemberTypeByIndex', ((1, 'Index'),)))
    ID3D10ShaderReflectionType.GetMemberTypeByName = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionType_head,win32more.Foundation.PSTR)(2, 'GetMemberTypeByName', ((1, 'Name'),)))
    ID3D10ShaderReflectionType.GetMemberTypeName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.PSTR,UInt32)(3, 'GetMemberTypeName', ((1, 'Index'),)))
    return ID3D10ShaderReflectionType
def _define_ID3D10ShaderReflectionVariable_head():
    class ID3D10ShaderReflectionVariable(c_void_p):
        Guid = Guid('1bf63c95-2650-405d-99-c1-36-36-bd-1d-a0-a1')
    return ID3D10ShaderReflectionVariable
def _define_ID3D10ShaderReflectionVariable():
    ID3D10ShaderReflectionVariable = win32more.Graphics.Direct3D10.ID3D10ShaderReflectionVariable_head
    ID3D10ShaderReflectionVariable.GetDesc = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_VARIABLE_DESC_head))(0, 'GetDesc', ((1, 'pDesc'),)))
    ID3D10ShaderReflectionVariable.GetType = COMMETHOD(WINFUNCTYPE(win32more.Graphics.Direct3D10.ID3D10ShaderReflectionType_head,)(1, 'GetType', ()))
    return ID3D10ShaderReflectionVariable
def _define_ID3D10ShaderResourceView_head():
    class ID3D10ShaderResourceView(win32more.Graphics.Direct3D10.ID3D10View_head):
        Guid = Guid('9b7e4c07-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10ShaderResourceView
def _define_ID3D10ShaderResourceView():
    ID3D10ShaderResourceView = win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head
    ID3D10ShaderResourceView.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC_head))(8, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10View
    return ID3D10ShaderResourceView
def _define_ID3D10ShaderResourceView1_head():
    class ID3D10ShaderResourceView1(win32more.Graphics.Direct3D10.ID3D10ShaderResourceView_head):
        Guid = Guid('9b7e4c87-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10ShaderResourceView1
def _define_ID3D10ShaderResourceView1():
    ID3D10ShaderResourceView1 = win32more.Graphics.Direct3D10.ID3D10ShaderResourceView1_head
    ID3D10ShaderResourceView1.GetDesc1 = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_SHADER_RESOURCE_VIEW_DESC1_head))(9, 'GetDesc1', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10ShaderResourceView
    return ID3D10ShaderResourceView1
def _define_ID3D10StateBlock_head():
    class ID3D10StateBlock(win32more.System.Com.IUnknown_head):
        Guid = Guid('0803425a-57f5-4dd6-94-65-a8-75-70-83-4a-08')
    return ID3D10StateBlock
def _define_ID3D10StateBlock():
    ID3D10StateBlock = win32more.Graphics.Direct3D10.ID3D10StateBlock_head
    ID3D10StateBlock.Capture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Capture', ()))
    ID3D10StateBlock.Apply = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Apply', ()))
    ID3D10StateBlock.ReleaseAllDeviceObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'ReleaseAllDeviceObjects', ()))
    ID3D10StateBlock.GetDevice = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Graphics.Direct3D10.ID3D10Device_head))(6, 'GetDevice', ((1, 'ppDevice'),)))
    win32more.System.Com.IUnknown
    return ID3D10StateBlock
def _define_ID3D10SwitchToRef_head():
    class ID3D10SwitchToRef(win32more.System.Com.IUnknown_head):
        Guid = Guid('9b7e4e02-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10SwitchToRef
def _define_ID3D10SwitchToRef():
    ID3D10SwitchToRef = win32more.Graphics.Direct3D10.ID3D10SwitchToRef_head
    ID3D10SwitchToRef.SetUseRef = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.BOOL)(3, 'SetUseRef', ((1, 'UseRef'),)))
    ID3D10SwitchToRef.GetUseRef = COMMETHOD(WINFUNCTYPE(win32more.Foundation.BOOL,)(4, 'GetUseRef', ()))
    win32more.System.Com.IUnknown
    return ID3D10SwitchToRef
def _define_ID3D10Texture1D_head():
    class ID3D10Texture1D(win32more.Graphics.Direct3D10.ID3D10Resource_head):
        Guid = Guid('9b7e4c03-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Texture1D
def _define_ID3D10Texture1D():
    ID3D10Texture1D = win32more.Graphics.Direct3D10.ID3D10Texture1D_head
    ID3D10Texture1D.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct3D10.D3D10_MAP,UInt32,POINTER(c_void_p))(10, 'Map', ((1, 'Subresource'),(1, 'MapType'),(1, 'MapFlags'),(1, 'ppData'),)))
    ID3D10Texture1D.Unmap = COMMETHOD(WINFUNCTYPE(Void,UInt32)(11, 'Unmap', ((1, 'Subresource'),)))
    ID3D10Texture1D.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE1D_DESC_head))(12, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Resource
    return ID3D10Texture1D
def _define_ID3D10Texture2D_head():
    class ID3D10Texture2D(win32more.Graphics.Direct3D10.ID3D10Resource_head):
        Guid = Guid('9b7e4c04-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Texture2D
def _define_ID3D10Texture2D():
    ID3D10Texture2D = win32more.Graphics.Direct3D10.ID3D10Texture2D_head
    ID3D10Texture2D.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct3D10.D3D10_MAP,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_MAPPED_TEXTURE2D_head))(10, 'Map', ((1, 'Subresource'),(1, 'MapType'),(1, 'MapFlags'),(1, 'pMappedTex2D'),)))
    ID3D10Texture2D.Unmap = COMMETHOD(WINFUNCTYPE(Void,UInt32)(11, 'Unmap', ((1, 'Subresource'),)))
    ID3D10Texture2D.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE2D_DESC_head))(12, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Resource
    return ID3D10Texture2D
def _define_ID3D10Texture3D_head():
    class ID3D10Texture3D(win32more.Graphics.Direct3D10.ID3D10Resource_head):
        Guid = Guid('9b7e4c05-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10Texture3D
def _define_ID3D10Texture3D():
    ID3D10Texture3D = win32more.Graphics.Direct3D10.ID3D10Texture3D_head
    ID3D10Texture3D.Map = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Graphics.Direct3D10.D3D10_MAP,UInt32,POINTER(win32more.Graphics.Direct3D10.D3D10_MAPPED_TEXTURE3D_head))(10, 'Map', ((1, 'Subresource'),(1, 'MapType'),(1, 'MapFlags'),(1, 'pMappedTex3D'),)))
    ID3D10Texture3D.Unmap = COMMETHOD(WINFUNCTYPE(Void,UInt32)(11, 'Unmap', ((1, 'Subresource'),)))
    ID3D10Texture3D.GetDesc = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.D3D10_TEXTURE3D_DESC_head))(12, 'GetDesc', ((1, 'pDesc'),)))
    win32more.Graphics.Direct3D10.ID3D10Resource
    return ID3D10Texture3D
def _define_ID3D10VertexShader_head():
    class ID3D10VertexShader(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('9b7e4c0a-342c-4106-a1-9f-4f-27-04-f6-89-f0')
    return ID3D10VertexShader
def _define_ID3D10VertexShader():
    ID3D10VertexShader = win32more.Graphics.Direct3D10.ID3D10VertexShader_head
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10VertexShader
def _define_ID3D10View_head():
    class ID3D10View(win32more.Graphics.Direct3D10.ID3D10DeviceChild_head):
        Guid = Guid('c902b03f-60a7-49ba-99-36-2a-3a-b3-7a-7e-33')
    return ID3D10View
def _define_ID3D10View():
    ID3D10View = win32more.Graphics.Direct3D10.ID3D10View_head
    ID3D10View.GetResource = COMMETHOD(WINFUNCTYPE(Void,POINTER(win32more.Graphics.Direct3D10.ID3D10Resource_head))(7, 'GetResource', ((1, 'ppResource'),)))
    win32more.Graphics.Direct3D10.ID3D10DeviceChild
    return ID3D10View
def _define_PFN_D3D10_CREATE_DEVICE_AND_SWAP_CHAIN1():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,win32more.Graphics.Direct3D10.D3D10_FEATURE_LEVEL1,UInt32,POINTER(win32more.Graphics.Dxgi.DXGI_SWAP_CHAIN_DESC_head),POINTER(win32more.Graphics.Dxgi.IDXGISwapChain_head),POINTER(win32more.Graphics.Direct3D10.ID3D10Device1_head))
def _define_PFN_D3D10_CREATE_DEVICE1():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Graphics.Dxgi.IDXGIAdapter_head,win32more.Graphics.Direct3D10.D3D10_DRIVER_TYPE,win32more.Foundation.HINSTANCE,UInt32,win32more.Graphics.Direct3D10.D3D10_FEATURE_LEVEL1,UInt32,POINTER(win32more.Graphics.Direct3D10.ID3D10Device1_head))
__all__ = [
    "D3D10CompileEffectFromMemory",
    "D3D10CompileShader",
    "D3D10CreateBlob",
    "D3D10CreateDevice",
    "D3D10CreateDevice1",
    "D3D10CreateDeviceAndSwapChain",
    "D3D10CreateDeviceAndSwapChain1",
    "D3D10CreateEffectFromMemory",
    "D3D10CreateEffectPoolFromMemory",
    "D3D10CreateStateBlock",
    "D3D10DisassembleEffect",
    "D3D10DisassembleShader",
    "D3D10GetGeometryShaderProfile",
    "D3D10GetInputAndOutputSignatureBlob",
    "D3D10GetInputSignatureBlob",
    "D3D10GetOutputSignatureBlob",
    "D3D10GetPixelShaderProfile",
    "D3D10GetShaderDebugInfo",
    "D3D10GetVertexShaderProfile",
    "D3D10PreprocessShader",
    "D3D10ReflectShader",
    "D3D10StateBlockMaskDifference",
    "D3D10StateBlockMaskDisableAll",
    "D3D10StateBlockMaskDisableCapture",
    "D3D10StateBlockMaskEnableAll",
    "D3D10StateBlockMaskEnableCapture",
    "D3D10StateBlockMaskGetSetting",
    "D3D10StateBlockMaskIntersect",
    "D3D10StateBlockMaskUnion",
    "D3D10_16BIT_INDEX_STRIP_CUT_VALUE",
    "D3D10_1_DEFAULT_SAMPLE_MASK",
    "D3D10_1_FLOAT16_FUSED_TOLERANCE_IN_ULP",
    "D3D10_1_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP",
    "D3D10_1_GS_INPUT_REGISTER_COUNT",
    "D3D10_1_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT",
    "D3D10_1_IA_VERTEX_INPUT_STRUCTURE_ELEMENTS_COMPONENTS",
    "D3D10_1_IA_VERTEX_INPUT_STRUCTURE_ELEMENT_COUNT",
    "D3D10_1_PS_OUTPUT_MASK_REGISTER_COMPONENTS",
    "D3D10_1_PS_OUTPUT_MASK_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_1_PS_OUTPUT_MASK_REGISTER_COUNT",
    "D3D10_1_SHADER_MAJOR_VERSION",
    "D3D10_1_SHADER_MINOR_VERSION",
    "D3D10_1_SO_BUFFER_MAX_STRIDE_IN_BYTES",
    "D3D10_1_SO_BUFFER_MAX_WRITE_WINDOW_IN_BYTES",
    "D3D10_1_SO_BUFFER_SLOT_COUNT",
    "D3D10_1_SO_MULTIPLE_BUFFER_ELEMENTS_PER_BUFFER",
    "D3D10_1_SO_SINGLE_BUFFER_COMPONENT_LIMIT",
    "D3D10_1_STANDARD_VERTEX_ELEMENT_COUNT",
    "D3D10_1_SUBPIXEL_FRACTIONAL_BIT_COUNT",
    "D3D10_1_VS_INPUT_REGISTER_COUNT",
    "D3D10_1_VS_OUTPUT_REGISTER_COUNT",
    "D3D10_32BIT_INDEX_STRIP_CUT_VALUE",
    "D3D10_8BIT_INDEX_STRIP_CUT_VALUE",
    "D3D10_ALL_RESOURCES_BOUND",
    "D3D10_ANISOTROPIC_FILTERING_BIT",
    "D3D10_APPEND_ALIGNED_ELEMENT",
    "D3D10_APPNAME_STRING",
    "D3D10_APPSIZE_STRING",
    "D3D10_ARRAY_AXIS_ADDRESS_RANGE_BIT_COUNT",
    "D3D10_ASYNC_GETDATA_DONOTFLUSH",
    "D3D10_ASYNC_GETDATA_FLAG",
    "D3D10_BIND_CONSTANT_BUFFER",
    "D3D10_BIND_DEPTH_STENCIL",
    "D3D10_BIND_FLAG",
    "D3D10_BIND_INDEX_BUFFER",
    "D3D10_BIND_RENDER_TARGET",
    "D3D10_BIND_SHADER_RESOURCE",
    "D3D10_BIND_STREAM_OUTPUT",
    "D3D10_BIND_VERTEX_BUFFER",
    "D3D10_BLEND",
    "D3D10_BLEND_BLEND_FACTOR",
    "D3D10_BLEND_DESC",
    "D3D10_BLEND_DESC1",
    "D3D10_BLEND_DEST_ALPHA",
    "D3D10_BLEND_DEST_COLOR",
    "D3D10_BLEND_INV_BLEND_FACTOR",
    "D3D10_BLEND_INV_DEST_ALPHA",
    "D3D10_BLEND_INV_DEST_COLOR",
    "D3D10_BLEND_INV_SRC1_ALPHA",
    "D3D10_BLEND_INV_SRC1_COLOR",
    "D3D10_BLEND_INV_SRC_ALPHA",
    "D3D10_BLEND_INV_SRC_COLOR",
    "D3D10_BLEND_ONE",
    "D3D10_BLEND_OP",
    "D3D10_BLEND_OP_ADD",
    "D3D10_BLEND_OP_MAX",
    "D3D10_BLEND_OP_MIN",
    "D3D10_BLEND_OP_REV_SUBTRACT",
    "D3D10_BLEND_OP_SUBTRACT",
    "D3D10_BLEND_SRC1_ALPHA",
    "D3D10_BLEND_SRC1_COLOR",
    "D3D10_BLEND_SRC_ALPHA",
    "D3D10_BLEND_SRC_ALPHA_SAT",
    "D3D10_BLEND_SRC_COLOR",
    "D3D10_BLEND_ZERO",
    "D3D10_BOX",
    "D3D10_BREAKON_CATEGORY",
    "D3D10_BREAKON_ID_DECIMAL",
    "D3D10_BREAKON_ID_STRING",
    "D3D10_BREAKON_SEVERITY",
    "D3D10_BUFFER_DESC",
    "D3D10_BUFFER_RTV",
    "D3D10_BUFFER_SRV",
    "D3D10_CENTER_MULTISAMPLE_PATTERN",
    "D3D10_CLEAR_DEPTH",
    "D3D10_CLEAR_FLAG",
    "D3D10_CLEAR_STENCIL",
    "D3D10_CLIP_OR_CULL_DISTANCE_COUNT",
    "D3D10_CLIP_OR_CULL_DISTANCE_ELEMENT_COUNT",
    "D3D10_COLOR_WRITE_ENABLE",
    "D3D10_COLOR_WRITE_ENABLE_ALL",
    "D3D10_COLOR_WRITE_ENABLE_ALPHA",
    "D3D10_COLOR_WRITE_ENABLE_BLUE",
    "D3D10_COLOR_WRITE_ENABLE_GREEN",
    "D3D10_COLOR_WRITE_ENABLE_RED",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_API_SLOT_COUNT",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENTS",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_COMPONENT_BIT_COUNT",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_HW_SLOT_COUNT",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COMPONENTS",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_COUNT",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READS_PER_INST",
    "D3D10_COMMONSHADER_CONSTANT_BUFFER_REGISTER_READ_PORTS",
    "D3D10_COMMONSHADER_FLOWCONTROL_NESTING_LIMIT",
    "D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COMPONENTS",
    "D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_COUNT",
    "D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READS_PER_INST",
    "D3D10_COMMONSHADER_IMMEDIATE_CONSTANT_BUFFER_REGISTER_READ_PORTS",
    "D3D10_COMMONSHADER_IMMEDIATE_VALUE_COMPONENT_BIT_COUNT",
    "D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COMPONENTS",
    "D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_COUNT",
    "D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READS_PER_INST",
    "D3D10_COMMONSHADER_INPUT_RESOURCE_REGISTER_READ_PORTS",
    "D3D10_COMMONSHADER_INPUT_RESOURCE_SLOT_COUNT",
    "D3D10_COMMONSHADER_SAMPLER_REGISTER_COMPONENTS",
    "D3D10_COMMONSHADER_SAMPLER_REGISTER_COUNT",
    "D3D10_COMMONSHADER_SAMPLER_REGISTER_READS_PER_INST",
    "D3D10_COMMONSHADER_SAMPLER_REGISTER_READ_PORTS",
    "D3D10_COMMONSHADER_SAMPLER_SLOT_COUNT",
    "D3D10_COMMONSHADER_SUBROUTINE_NESTING_LIMIT",
    "D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENTS",
    "D3D10_COMMONSHADER_TEMP_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_COMMONSHADER_TEMP_REGISTER_COUNT",
    "D3D10_COMMONSHADER_TEMP_REGISTER_READS_PER_INST",
    "D3D10_COMMONSHADER_TEMP_REGISTER_READ_PORTS",
    "D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MAX",
    "D3D10_COMMONSHADER_TEXCOORD_RANGE_REDUCTION_MIN",
    "D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_NEGATIVE",
    "D3D10_COMMONSHADER_TEXEL_OFFSET_MAX_POSITIVE",
    "D3D10_COMPARISON_ALWAYS",
    "D3D10_COMPARISON_EQUAL",
    "D3D10_COMPARISON_FILTERING_BIT",
    "D3D10_COMPARISON_FUNC",
    "D3D10_COMPARISON_GREATER",
    "D3D10_COMPARISON_GREATER_EQUAL",
    "D3D10_COMPARISON_LESS",
    "D3D10_COMPARISON_LESS_EQUAL",
    "D3D10_COMPARISON_NEVER",
    "D3D10_COMPARISON_NOT_EQUAL",
    "D3D10_COUNTER",
    "D3D10_COUNTER_DESC",
    "D3D10_COUNTER_DEVICE_DEPENDENT_0",
    "D3D10_COUNTER_FILLRATE_THROUGHPUT_UTILIZATION",
    "D3D10_COUNTER_GEOMETRY_PROCESSING",
    "D3D10_COUNTER_GPU_IDLE",
    "D3D10_COUNTER_GS_COMPUTATION_LIMITED",
    "D3D10_COUNTER_GS_MEMORY_LIMITED",
    "D3D10_COUNTER_HOST_ADAPTER_BANDWIDTH_UTILIZATION",
    "D3D10_COUNTER_INFO",
    "D3D10_COUNTER_LOCAL_VIDMEM_BANDWIDTH_UTILIZATION",
    "D3D10_COUNTER_OTHER_GPU_PROCESSING",
    "D3D10_COUNTER_PIXEL_PROCESSING",
    "D3D10_COUNTER_POST_TRANSFORM_CACHE_HIT_RATE",
    "D3D10_COUNTER_PS_COMPUTATION_LIMITED",
    "D3D10_COUNTER_PS_MEMORY_LIMITED",
    "D3D10_COUNTER_TEXTURE_CACHE_HIT_RATE",
    "D3D10_COUNTER_TRIANGLE_SETUP_THROUGHPUT_UTILIZATION",
    "D3D10_COUNTER_TYPE",
    "D3D10_COUNTER_TYPE_FLOAT32",
    "D3D10_COUNTER_TYPE_UINT16",
    "D3D10_COUNTER_TYPE_UINT32",
    "D3D10_COUNTER_TYPE_UINT64",
    "D3D10_COUNTER_VERTEX_PROCESSING",
    "D3D10_COUNTER_VERTEX_THROUGHPUT_UTILIZATION",
    "D3D10_COUNTER_VS_COMPUTATION_LIMITED",
    "D3D10_COUNTER_VS_MEMORY_LIMITED",
    "D3D10_CPU_ACCESS_FLAG",
    "D3D10_CPU_ACCESS_READ",
    "D3D10_CPU_ACCESS_WRITE",
    "D3D10_CREATE_DEVICE_ALLOW_NULL_FROM_MAP",
    "D3D10_CREATE_DEVICE_BGRA_SUPPORT",
    "D3D10_CREATE_DEVICE_DEBUG",
    "D3D10_CREATE_DEVICE_DEBUGGABLE",
    "D3D10_CREATE_DEVICE_FLAG",
    "D3D10_CREATE_DEVICE_PREVENT_ALTERING_LAYER_SETTINGS_FROM_REGISTRY",
    "D3D10_CREATE_DEVICE_PREVENT_INTERNAL_THREADING_OPTIMIZATIONS",
    "D3D10_CREATE_DEVICE_SINGLETHREADED",
    "D3D10_CREATE_DEVICE_STRICT_VALIDATION",
    "D3D10_CREATE_DEVICE_SWITCH_TO_REF",
    "D3D10_CULL_BACK",
    "D3D10_CULL_FRONT",
    "D3D10_CULL_MODE",
    "D3D10_CULL_NONE",
    "D3D10_DEBUG_FEATURE_FINISH_PER_RENDER_OP",
    "D3D10_DEBUG_FEATURE_FLUSH_PER_RENDER_OP",
    "D3D10_DEBUG_FEATURE_PRESENT_PER_RENDER_OP",
    "D3D10_DEFAULT_BLEND_FACTOR_ALPHA",
    "D3D10_DEFAULT_BLEND_FACTOR_BLUE",
    "D3D10_DEFAULT_BLEND_FACTOR_GREEN",
    "D3D10_DEFAULT_BLEND_FACTOR_RED",
    "D3D10_DEFAULT_BORDER_COLOR_COMPONENT",
    "D3D10_DEFAULT_DEPTH_BIAS",
    "D3D10_DEFAULT_DEPTH_BIAS_CLAMP",
    "D3D10_DEFAULT_MAX_ANISOTROPY",
    "D3D10_DEFAULT_MIP_LOD_BIAS",
    "D3D10_DEFAULT_RENDER_TARGET_ARRAY_INDEX",
    "D3D10_DEFAULT_SAMPLE_MASK",
    "D3D10_DEFAULT_SCISSOR_ENDX",
    "D3D10_DEFAULT_SCISSOR_ENDY",
    "D3D10_DEFAULT_SCISSOR_STARTX",
    "D3D10_DEFAULT_SCISSOR_STARTY",
    "D3D10_DEFAULT_SLOPE_SCALED_DEPTH_BIAS",
    "D3D10_DEFAULT_STENCIL_READ_MASK",
    "D3D10_DEFAULT_STENCIL_REFERENCE",
    "D3D10_DEFAULT_STENCIL_WRITE_MASK",
    "D3D10_DEFAULT_VIEWPORT_AND_SCISSORRECT_INDEX",
    "D3D10_DEFAULT_VIEWPORT_HEIGHT",
    "D3D10_DEFAULT_VIEWPORT_MAX_DEPTH",
    "D3D10_DEFAULT_VIEWPORT_MIN_DEPTH",
    "D3D10_DEFAULT_VIEWPORT_TOPLEFTX",
    "D3D10_DEFAULT_VIEWPORT_TOPLEFTY",
    "D3D10_DEFAULT_VIEWPORT_WIDTH",
    "D3D10_DEPTH_STENCILOP_DESC",
    "D3D10_DEPTH_STENCIL_DESC",
    "D3D10_DEPTH_STENCIL_VIEW_DESC",
    "D3D10_DEPTH_WRITE_MASK",
    "D3D10_DEPTH_WRITE_MASK_ALL",
    "D3D10_DEPTH_WRITE_MASK_ZERO",
    "D3D10_DEVICE_STATE_TYPES",
    "D3D10_DRIVER_TYPE",
    "D3D10_DRIVER_TYPE_HARDWARE",
    "D3D10_DRIVER_TYPE_NULL",
    "D3D10_DRIVER_TYPE_REFERENCE",
    "D3D10_DRIVER_TYPE_SOFTWARE",
    "D3D10_DRIVER_TYPE_WARP",
    "D3D10_DST_GS",
    "D3D10_DST_GS_CONSTANT_BUFFERS",
    "D3D10_DST_GS_SAMPLERS",
    "D3D10_DST_GS_SHADER_RESOURCES",
    "D3D10_DST_IA_INDEX_BUFFER",
    "D3D10_DST_IA_INPUT_LAYOUT",
    "D3D10_DST_IA_PRIMITIVE_TOPOLOGY",
    "D3D10_DST_IA_VERTEX_BUFFERS",
    "D3D10_DST_OM_BLEND_STATE",
    "D3D10_DST_OM_DEPTH_STENCIL_STATE",
    "D3D10_DST_OM_RENDER_TARGETS",
    "D3D10_DST_PREDICATION",
    "D3D10_DST_PS",
    "D3D10_DST_PS_CONSTANT_BUFFERS",
    "D3D10_DST_PS_SAMPLERS",
    "D3D10_DST_PS_SHADER_RESOURCES",
    "D3D10_DST_RS_RASTERIZER_STATE",
    "D3D10_DST_RS_SCISSOR_RECTS",
    "D3D10_DST_RS_VIEWPORTS",
    "D3D10_DST_SO_BUFFERS",
    "D3D10_DST_VS",
    "D3D10_DST_VS_CONSTANT_BUFFERS",
    "D3D10_DST_VS_SAMPLERS",
    "D3D10_DST_VS_SHADER_RESOURCES",
    "D3D10_DSV_DIMENSION",
    "D3D10_DSV_DIMENSION_TEXTURE1D",
    "D3D10_DSV_DIMENSION_TEXTURE1DARRAY",
    "D3D10_DSV_DIMENSION_TEXTURE2D",
    "D3D10_DSV_DIMENSION_TEXTURE2DARRAY",
    "D3D10_DSV_DIMENSION_TEXTURE2DMS",
    "D3D10_DSV_DIMENSION_TEXTURE2DMSARRAY",
    "D3D10_DSV_DIMENSION_UNKNOWN",
    "D3D10_EFFECT_COMPILE_ALLOW_SLOW_OPS",
    "D3D10_EFFECT_COMPILE_CHILD_EFFECT",
    "D3D10_EFFECT_DESC",
    "D3D10_EFFECT_SHADER_DESC",
    "D3D10_EFFECT_SINGLE_THREADED",
    "D3D10_EFFECT_TYPE_DESC",
    "D3D10_EFFECT_VARIABLE_ANNOTATION",
    "D3D10_EFFECT_VARIABLE_DESC",
    "D3D10_EFFECT_VARIABLE_EXPLICIT_BIND_POINT",
    "D3D10_EFFECT_VARIABLE_POOLED",
    "D3D10_ENABLE_BREAK_ON_MESSAGE",
    "D3D10_ENABLE_UNBOUNDED_DESCRIPTOR_TABLES",
    "D3D10_FEATURE_LEVEL1",
    "D3D10_FEATURE_LEVEL_10_0",
    "D3D10_FEATURE_LEVEL_10_1",
    "D3D10_FEATURE_LEVEL_9_1",
    "D3D10_FEATURE_LEVEL_9_2",
    "D3D10_FEATURE_LEVEL_9_3",
    "D3D10_FILL_MODE",
    "D3D10_FILL_SOLID",
    "D3D10_FILL_WIREFRAME",
    "D3D10_FILTER",
    "D3D10_FILTER_ANISOTROPIC",
    "D3D10_FILTER_COMPARISON_ANISOTROPIC",
    "D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_MIP_POINT",
    "D3D10_FILTER_COMPARISON_MIN_LINEAR_MAG_POINT_MIP_LINEAR",
    "D3D10_FILTER_COMPARISON_MIN_MAG_LINEAR_MIP_POINT",
    "D3D10_FILTER_COMPARISON_MIN_MAG_MIP_LINEAR",
    "D3D10_FILTER_COMPARISON_MIN_MAG_MIP_POINT",
    "D3D10_FILTER_COMPARISON_MIN_MAG_POINT_MIP_LINEAR",
    "D3D10_FILTER_COMPARISON_MIN_POINT_MAG_LINEAR_MIP_POINT",
    "D3D10_FILTER_COMPARISON_MIN_POINT_MAG_MIP_LINEAR",
    "D3D10_FILTER_MIN_LINEAR_MAG_MIP_POINT",
    "D3D10_FILTER_MIN_LINEAR_MAG_POINT_MIP_LINEAR",
    "D3D10_FILTER_MIN_MAG_LINEAR_MIP_POINT",
    "D3D10_FILTER_MIN_MAG_MIP_LINEAR",
    "D3D10_FILTER_MIN_MAG_MIP_POINT",
    "D3D10_FILTER_MIN_MAG_POINT_MIP_LINEAR",
    "D3D10_FILTER_MIN_POINT_MAG_LINEAR_MIP_POINT",
    "D3D10_FILTER_MIN_POINT_MAG_MIP_LINEAR",
    "D3D10_FILTER_TEXT_1BIT",
    "D3D10_FILTER_TYPE",
    "D3D10_FILTER_TYPE_LINEAR",
    "D3D10_FILTER_TYPE_MASK",
    "D3D10_FILTER_TYPE_POINT",
    "D3D10_FLOAT16_FUSED_TOLERANCE_IN_ULP",
    "D3D10_FLOAT32_MAX",
    "D3D10_FLOAT32_TO_INTEGER_TOLERANCE_IN_ULP",
    "D3D10_FLOAT_TO_SRGB_EXPONENT_DENOMINATOR",
    "D3D10_FLOAT_TO_SRGB_EXPONENT_NUMERATOR",
    "D3D10_FLOAT_TO_SRGB_OFFSET",
    "D3D10_FLOAT_TO_SRGB_SCALE_1",
    "D3D10_FLOAT_TO_SRGB_SCALE_2",
    "D3D10_FLOAT_TO_SRGB_THRESHOLD",
    "D3D10_FORMAT_SUPPORT",
    "D3D10_FORMAT_SUPPORT_BACK_BUFFER_CAST",
    "D3D10_FORMAT_SUPPORT_BLENDABLE",
    "D3D10_FORMAT_SUPPORT_BUFFER",
    "D3D10_FORMAT_SUPPORT_CAST_WITHIN_BIT_LAYOUT",
    "D3D10_FORMAT_SUPPORT_CPU_LOCKABLE",
    "D3D10_FORMAT_SUPPORT_DEPTH_STENCIL",
    "D3D10_FORMAT_SUPPORT_DISPLAY",
    "D3D10_FORMAT_SUPPORT_IA_INDEX_BUFFER",
    "D3D10_FORMAT_SUPPORT_IA_VERTEX_BUFFER",
    "D3D10_FORMAT_SUPPORT_MIP",
    "D3D10_FORMAT_SUPPORT_MIP_AUTOGEN",
    "D3D10_FORMAT_SUPPORT_MULTISAMPLE_LOAD",
    "D3D10_FORMAT_SUPPORT_MULTISAMPLE_RENDERTARGET",
    "D3D10_FORMAT_SUPPORT_MULTISAMPLE_RESOLVE",
    "D3D10_FORMAT_SUPPORT_RENDER_TARGET",
    "D3D10_FORMAT_SUPPORT_SHADER_GATHER",
    "D3D10_FORMAT_SUPPORT_SHADER_LOAD",
    "D3D10_FORMAT_SUPPORT_SHADER_SAMPLE",
    "D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_COMPARISON",
    "D3D10_FORMAT_SUPPORT_SHADER_SAMPLE_MONO_TEXT",
    "D3D10_FORMAT_SUPPORT_SO_BUFFER",
    "D3D10_FORMAT_SUPPORT_TEXTURE1D",
    "D3D10_FORMAT_SUPPORT_TEXTURE2D",
    "D3D10_FORMAT_SUPPORT_TEXTURE3D",
    "D3D10_FORMAT_SUPPORT_TEXTURECUBE",
    "D3D10_FTOI_INSTRUCTION_MAX_INPUT",
    "D3D10_FTOI_INSTRUCTION_MIN_INPUT",
    "D3D10_FTOU_INSTRUCTION_MAX_INPUT",
    "D3D10_FTOU_INSTRUCTION_MIN_INPUT",
    "D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENTS",
    "D3D10_GS_INPUT_PRIM_CONST_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_GS_INPUT_PRIM_CONST_REGISTER_COUNT",
    "D3D10_GS_INPUT_PRIM_CONST_REGISTER_READS_PER_INST",
    "D3D10_GS_INPUT_PRIM_CONST_REGISTER_READ_PORTS",
    "D3D10_GS_INPUT_REGISTER_COMPONENTS",
    "D3D10_GS_INPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_GS_INPUT_REGISTER_COUNT",
    "D3D10_GS_INPUT_REGISTER_READS_PER_INST",
    "D3D10_GS_INPUT_REGISTER_READ_PORTS",
    "D3D10_GS_INPUT_REGISTER_VERTICES",
    "D3D10_GS_OUTPUT_ELEMENTS",
    "D3D10_GS_OUTPUT_REGISTER_COMPONENTS",
    "D3D10_GS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_GS_OUTPUT_REGISTER_COUNT",
    "D3D10_IA_DEFAULT_INDEX_BUFFER_OFFSET_IN_BYTES",
    "D3D10_IA_DEFAULT_PRIMITIVE_TOPOLOGY",
    "D3D10_IA_DEFAULT_VERTEX_BUFFER_OFFSET_IN_BYTES",
    "D3D10_IA_INDEX_INPUT_RESOURCE_SLOT_COUNT",
    "D3D10_IA_INSTANCE_ID_BIT_COUNT",
    "D3D10_IA_INTEGER_ARITHMETIC_BIT_COUNT",
    "D3D10_IA_PRIMITIVE_ID_BIT_COUNT",
    "D3D10_IA_VERTEX_ID_BIT_COUNT",
    "D3D10_IA_VERTEX_INPUT_RESOURCE_SLOT_COUNT",
    "D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENTS_COMPONENTS",
    "D3D10_IA_VERTEX_INPUT_STRUCTURE_ELEMENT_COUNT",
    "D3D10_INFOQUEUE_STORAGE_FILTER_OVERRIDE",
    "D3D10_INFO_QUEUE_DEFAULT_MESSAGE_COUNT_LIMIT",
    "D3D10_INFO_QUEUE_FILTER",
    "D3D10_INFO_QUEUE_FILTER_DESC",
    "D3D10_INPUT_CLASSIFICATION",
    "D3D10_INPUT_ELEMENT_DESC",
    "D3D10_INPUT_PER_INSTANCE_DATA",
    "D3D10_INPUT_PER_VERTEX_DATA",
    "D3D10_INTEGER_DIVIDE_BY_ZERO_QUOTIENT",
    "D3D10_INTEGER_DIVIDE_BY_ZERO_REMAINDER",
    "D3D10_LINEAR_GAMMA",
    "D3D10_MAG_FILTER_SHIFT",
    "D3D10_MAP",
    "D3D10_MAPPED_TEXTURE2D",
    "D3D10_MAPPED_TEXTURE3D",
    "D3D10_MAP_FLAG",
    "D3D10_MAP_FLAG_DO_NOT_WAIT",
    "D3D10_MAP_READ",
    "D3D10_MAP_READ_WRITE",
    "D3D10_MAP_WRITE",
    "D3D10_MAP_WRITE_DISCARD",
    "D3D10_MAP_WRITE_NO_OVERWRITE",
    "D3D10_MAX_BORDER_COLOR_COMPONENT",
    "D3D10_MAX_DEPTH",
    "D3D10_MAX_MAXANISOTROPY",
    "D3D10_MAX_MULTISAMPLE_SAMPLE_COUNT",
    "D3D10_MAX_POSITION_VALUE",
    "D3D10_MAX_TEXTURE_DIMENSION_2_TO_EXP",
    "D3D10_MESSAGE",
    "D3D10_MESSAGE_CATEGORY",
    "D3D10_MESSAGE_CATEGORY_APPLICATION_DEFINED",
    "D3D10_MESSAGE_CATEGORY_CLEANUP",
    "D3D10_MESSAGE_CATEGORY_COMPILATION",
    "D3D10_MESSAGE_CATEGORY_EXECUTION",
    "D3D10_MESSAGE_CATEGORY_INITIALIZATION",
    "D3D10_MESSAGE_CATEGORY_MISCELLANEOUS",
    "D3D10_MESSAGE_CATEGORY_RESOURCE_MANIPULATION",
    "D3D10_MESSAGE_CATEGORY_SHADER",
    "D3D10_MESSAGE_CATEGORY_STATE_CREATION",
    "D3D10_MESSAGE_CATEGORY_STATE_GETTING",
    "D3D10_MESSAGE_CATEGORY_STATE_SETTING",
    "D3D10_MESSAGE_ID",
    "D3D10_MESSAGE_ID_BLENDSTATE_GETDESC_LEGACY",
    "D3D10_MESSAGE_ID_BUFFER_MAP_ALREADYMAPPED",
    "D3D10_MESSAGE_ID_BUFFER_MAP_DEVICEREMOVED_RETURN",
    "D3D10_MESSAGE_ID_BUFFER_MAP_INVALIDFLAGS",
    "D3D10_MESSAGE_ID_BUFFER_MAP_INVALIDMAPTYPE",
    "D3D10_MESSAGE_ID_BUFFER_UNMAP_NOTMAPPED",
    "D3D10_MESSAGE_ID_CHECKCOUNTER_OUTOFRANGE_COUNTER",
    "D3D10_MESSAGE_ID_CHECKCOUNTER_UNSUPPORTED_WELLKNOWN_COUNTER",
    "D3D10_MESSAGE_ID_CHECKFORMATSUPPORT_FORMAT_DEPRECATED",
    "D3D10_MESSAGE_ID_CHECKMULTISAMPLEQUALITYLEVELS_FORMAT_DEPRECATED",
    "D3D10_MESSAGE_ID_CLEARDEPTHSTENCILVIEW_DENORMFLUSH",
    "D3D10_MESSAGE_ID_CLEARDEPTHSTENCILVIEW_INVALID",
    "D3D10_MESSAGE_ID_CLEARRENDERTARGETVIEW_DENORMFLUSH",
    "D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDDESTINATIONSTATE",
    "D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDSOURCE",
    "D3D10_MESSAGE_ID_COPYRESOURCE_INVALIDSOURCESTATE",
    "D3D10_MESSAGE_ID_COPYRESOURCE_NO_3D_MISMATCHED_UPDATES",
    "D3D10_MESSAGE_ID_COPYRESOURCE_NO_TEXTURE_3D_READBACK",
    "D3D10_MESSAGE_ID_COPYRESOURCE_NO_TEXTURE_ONLY_READBACK",
    "D3D10_MESSAGE_ID_COPYRESOURCE_ONLY_TEXTURE_2D_WITHIN_GPU_MEMORY",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDDESTINATIONSTATE",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDDESTINATIONSUBRESOURCE",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCE",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCEBOX",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCESTATE",
    "D3D10_MESSAGE_ID_COPYSUBRESOURCEREGION_INVALIDSOURCESUBRESOURCE",
    "D3D10_MESSAGE_ID_CORRUPTED_MULTITHREADING",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER1",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER10",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER11",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER12",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER13",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER14",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER15",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER2",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER3",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER4",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER5",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER6",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER7",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER8",
    "D3D10_MESSAGE_ID_CORRUPTED_PARAMETER9",
    "D3D10_MESSAGE_ID_CORRUPTED_THIS",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDBLENDOP",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDBLENDOPALPHA",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDDESTBLEND",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDDESTBLENDALPHA",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDRENDERTARGETWRITEMASK",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDSRCBLEND",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_INVALIDSRCBLENDALPHA",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_ALPHA_TO_COVERAGE",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_INDEPENDENT_BLEND_ENABLE",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_INDEPENDENT_WRITE_MASKS",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_MRT_BLEND",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NO_SEPARATE_ALPHA_BLEND",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_NULLDESC",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_OPERATION_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_CREATEBLENDSTATE_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDCONSTANTBUFFERBINDINGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDINITIALDATA",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDMIPLEVELS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_INVALIDSAMPLES",
    "D3D10_MESSAGE_ID_CREATEBUFFER_LARGEALLOCATION",
    "D3D10_MESSAGE_ID_CREATEBUFFER_NULLDESC",
    "D3D10_MESSAGE_ID_CREATEBUFFER_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATEBUFFER_UNRECOGNIZEDUSAGE",
    "D3D10_MESSAGE_ID_CREATECOUNTER_NONEXCLUSIVE_RETURN",
    "D3D10_MESSAGE_ID_CREATECOUNTER_NULLDESC",
    "D3D10_MESSAGE_ID_CREATECOUNTER_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATECOUNTER_OUTOFRANGE_COUNTER",
    "D3D10_MESSAGE_ID_CREATECOUNTER_SIMULTANEOUS_ACTIVE_COUNTERS_EXHAUSTED",
    "D3D10_MESSAGE_ID_CREATECOUNTER_UNSUPPORTED_WELLKNOWN_COUNTER",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILFAILOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILFUNC",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILPASSOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDBACKFACESTENCILZFAILOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDDEPTHFUNC",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDDEPTHWRITEMASK",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILFAILOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILFUNC",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILPASSOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_INVALIDFRONTFACESTENCILZFAILOP",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_NULLDESC",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_STENCIL_NO_TWO_SIDED",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILSTATE_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDDESC",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDFORMAT",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_INVALIDRESOURCE",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATEDEPTHSTENCILVIEW_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_CANTHAVEONLYGAPS",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_DECLTOOCOMPLEX",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_EXPECTEDDECL",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDCOMPONENTCOUNT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDGAPDEFINITION",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDNUMENTRIES",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDOUTPUTSLOT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDOUTPUTSTREAMSTRIDE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSHADERBYTECODE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSHADERTYPE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_INVALIDSTARTCOMPONENTANDCOMPONENTCOUNT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MASKMISMATCH",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MISSINGOUTPUTSIGNATURE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_MISSINGSEMANTIC",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_ONLYONEELEMENTPERSLOT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTPUTSLOT0EXPECTED",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_OUTPUTSTREAMSTRIDEUNUSED",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_REPEATEDOUTPUT",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_TRAILING_DIGIT_IN_SEMANTIC",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADERWITHSTREAMOUTPUT_UNEXPECTEDDECL",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_INVALIDSHADERBYTECODE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_INVALIDSHADERTYPE",
    "D3D10_MESSAGE_ID_CREATEGEOMETRYSHADER_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_DUPLICATESEMANTIC",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_EMPTY_LAYOUT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INCOMPATIBLEFORMAT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDALIGNMENT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDFORMAT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDINPUTSLOTCLASS",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSLOT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSLOTCLASSCHANGE",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_INVALIDSTEPRATECHANGE",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_MISSINGELEMENT",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_NULLDESC",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_NULLSEMANTIC",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_STEPRATESLOTCLASSMISMATCH",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TOOMANYELEMENTS",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TRAILING_DIGIT_IN_SEMANTIC",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_TYPE_MISMATCH",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_UNPARSEABLEINPUTSIGNATURE",
    "D3D10_MESSAGE_ID_CREATEINPUTLAYOUT_UNSUPPORTED_FORMAT",
    "D3D10_MESSAGE_ID_CREATEPIXELSHADER_INVALIDSHADERBYTECODE",
    "D3D10_MESSAGE_ID_CREATEPIXELSHADER_INVALIDSHADERTYPE",
    "D3D10_MESSAGE_ID_CREATEPIXELSHADER_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_CREATEPREDICATE_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_INVALIDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_INVALIDQUERY",
    "D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_NULLDESC",
    "D3D10_MESSAGE_ID_CREATEQUERYORPREDICATE_UNEXPECTEDMISCFLAG",
    "D3D10_MESSAGE_ID_CREATEQUERY_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_DepthBiasClamp_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_DepthClipEnable_MUST_BE_TRUE",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDCULLMODE",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDDEPTHBIASCLAMP",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDFILLMODE",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_INVALIDSLOPESCALEDDEPTHBIAS",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_NULLDESC",
    "D3D10_MESSAGE_ID_CREATERASTERIZERSTATE_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDDESC",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDFORMAT",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_INVALIDRESOURCE",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATERENDERTARGETVIEW_UNSUPPORTEDFORMAT",
    "D3D10_MESSAGE_ID_CREATERESOURCE_DIMENSION_EXCEEDS_FEATURE_LEVEL_DEFINITION",
    "D3D10_MESSAGE_ID_CREATERESOURCE_DIMENSION_OUT_OF_RANGE",
    "D3D10_MESSAGE_ID_CREATERESOURCE_DXGI_FORMAT_R8G8B8A8_CANNOT_BE_SHARED",
    "D3D10_MESSAGE_ID_CREATERESOURCE_MSAA_PRECLUDES_SHADER_RESOURCE",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NON_POW_2_MIPMAP",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NOT_BINDABLE_AS_RENDER_TARGET",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NOT_BINDABLE_AS_SHADER_RESOURCE",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_ARRAYS",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_AUTOGEN_FOR_VOLUMES",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_DWORD_INDEX_BUFFER",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_STREAM_OUT",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_TEXTURE_1D",
    "D3D10_MESSAGE_ID_CREATERESOURCE_NO_VB_AND_IB_BIND",
    "D3D10_MESSAGE_ID_CREATERESOURCE_ONLY_SINGLE_MIP_LEVEL_DEPTH_STENCIL_SUPPORTED",
    "D3D10_MESSAGE_ID_CREATERESOURCE_ONLY_VB_IB_FOR_BUFFERS",
    "D3D10_MESSAGE_ID_CREATERESOURCE_PRESENTATION_PRECLUDES_SHADER_RESOURCE",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_BORDER_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_BORDER_OUT_OF_RANGE",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_EXCESSIVE_ANISOTROPY",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSU",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSV",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDADDRESSW",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDCOMPARISONFUNC",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDFILTER",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMAXANISOTROPY",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMAXLOD",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMINLOD",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_INVALIDMIPLODBIAS",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_MAXLOD_MUST_BE_FLT_MAX",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_MINLOD_MUST_NOT_BE_FRACTIONAL",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NO_COMPARISON_SUPPORT",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NO_MIRRORONCE",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_NULLDESC",
    "D3D10_MESSAGE_ID_CREATESAMPLERSTATE_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_CUBES_MUST_HAVE_6_SIDES",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_FIRSTARRAYSLICE_MUST_BE_ZERO",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDDESC",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDFORMAT",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_INVALIDRESOURCE",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_MUST_USE_LOWEST_LOD",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_TOOMANYOBJECTS",
    "D3D10_MESSAGE_ID_CREATESHADERRESOURCEVIEW_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDINITIALDATA",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDMIPLEVELS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_INVALIDSAMPLES",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_LARGEALLOCATION",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_NULLDESC",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNRECOGNIZEDUSAGE",
    "D3D10_MESSAGE_ID_CREATETEXTURE1D_UNSUPPORTEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDINITIALDATA",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDMIPLEVELS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_INVALIDSAMPLES",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_LARGEALLOCATION",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_NULLDESC",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNRECOGNIZEDUSAGE",
    "D3D10_MESSAGE_ID_CREATETEXTURE2D_UNSUPPORTEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDINITIALDATA",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDMIPLEVELS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_INVALIDSAMPLES",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_LARGEALLOCATION",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_NULLDESC",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDBINDFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDCPUACCESSFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDFORMAT",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDMISCFLAGS",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNRECOGNIZEDUSAGE",
    "D3D10_MESSAGE_ID_CREATETEXTURE3D_UNSUPPORTEDFORMAT",
    "D3D10_MESSAGE_ID_CREATEVERTEXSHADER_INVALIDSHADERBYTECODE",
    "D3D10_MESSAGE_ID_CREATEVERTEXSHADER_INVALIDSHADERTYPE",
    "D3D10_MESSAGE_ID_CREATEVERTEXSHADER_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_D3D10L9_MESSAGES_END",
    "D3D10_MESSAGE_ID_D3D10L9_MESSAGES_START",
    "D3D10_MESSAGE_ID_D3D10_MESSAGES_END",
    "D3D10_MESSAGE_ID_DEVICE_DRAWINDEXEDINSTANCED_INDEXPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAWINDEXEDINSTANCED_INSTANCEPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAWINDEXED_INDEXPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAWINSTANCED_INSTANCEPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAWINSTANCED_VERTEXPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_BOUND_RESOURCE_MAPPED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_CONSTANT_BUFFER_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_CONSTANT_BUFFER_TOO_SMALL",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_GS_INPUT_PRIMITIVE_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_FORMAT_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_TOO_SMALL",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_OFFSET_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INPUTLAYOUT_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INVALID_PRIMITIVETOPOLOGY",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_INVALID_USE_OF_CENTER_MULTISAMPLE_PATTERN",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_OM_DUAL_SOURCE_BLENDING_CAN_ONLY_HAVE_RENDER_TARGET_0",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_OM_RENDER_TARGET_DOES_NOT_SUPPORT_BLENDING",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_OUTPUT_STREAM_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_OUTPUT_STREAM_OFFSET_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_POSITION_NOT_PRESENT",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_PS_OUTPUT_TYPE_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_GATHER_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_LD_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_SAMPLE_C_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_FORMAT_SAMPLE_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_MULTISAMPLE_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_RETURN_TYPE_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_RESOURCE_SAMPLE_COUNT_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_SAMPLER_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_SAMPLER_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_SHADERRESOURCEVIEW_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_SO_STRIDE_LARGER_THAN_BUFFER",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_SO_TARGETS_BOUND_WITHOUT_SOURCE",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEXPOS_OVERFLOW",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_STRIDE_TOO_SMALL",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_BUFFER_TOO_SMALL",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_OFFSET_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_SHADER_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VERTEX_STRIDE_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VIEWPORT_NOT_SET",
    "D3D10_MESSAGE_ID_DEVICE_DRAW_VIEW_DIMENSION_MISMATCH",
    "D3D10_MESSAGE_ID_DEVICE_GENERATEMIPS_RESOURCE_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_GSGETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_GSGETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_GSGETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_GSSETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_GSSETCONSTANTBUFFERS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_GSSETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_GSSETSHADERRESOURCES_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_GSSETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_IAGETVERTEXBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_FORMAT_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_OFFSET_TOO_LARGE",
    "D3D10_MESSAGE_ID_DEVICE_IASETINDEXBUFFER_OFFSET_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_ADJACENCY_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_TOPOLOGY_UNDEFINED",
    "D3D10_MESSAGE_ID_DEVICE_IASETPRIMITIVETOPOLOGY_TOPOLOGY_UNRECOGNIZED",
    "D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_INVALIDRANGE",
    "D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_OFFSET_TOO_LARGE",
    "D3D10_MESSAGE_ID_DEVICE_IASETVERTEXBUFFERS_STRIDE_TOO_LARGE",
    "D3D10_MESSAGE_ID_DEVICE_OMSETRENDERTARGETS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_BADINTERFACE_RETURN",
    "D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_DEVICE_OPEN_SHARED_RESOURCE_OUTOFMEMORY_RETURN",
    "D3D10_MESSAGE_ID_DEVICE_PSGETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_PSGETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_PSGETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_PSSETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_PSSETCONSTANTBUFFERS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_PSSETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_PSSETSHADERRESOURCES_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_PSSETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_AT_FAULT",
    "D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_NOT_AT_FAULT",
    "D3D10_MESSAGE_ID_DEVICE_REMOVAL_PROCESS_POSSIBLY_AT_FAULT",
    "D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_DESTINATION_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_DESTINATION_SUBRESOURCE_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_FORMAT_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_SOURCE_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_RESOLVESUBRESOURCE_SOURCE_SUBRESOURCE_INVALID",
    "D3D10_MESSAGE_ID_DEVICE_RSGETSCISSORRECTS_RECTS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_RSGETVIEWPORTS_VIEWPORTS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_INVALIDSCISSOR",
    "D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_NEGATIVESCISSOR",
    "D3D10_MESSAGE_ID_DEVICE_RSSETSCISSORRECTS_TOO_MANY_SCISSORS",
    "D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_DENORMFLUSH",
    "D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_INVALIDVIEWPORT",
    "D3D10_MESSAGE_ID_DEVICE_RSSETVIEWPORTS_TOO_MANY_VIEWPORTS",
    "D3D10_MESSAGE_ID_DEVICE_SETTEXTFILTERSIZE_INVALIDDIMENSIONS",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_COMPONENTTYPE",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_NEVERWRITTEN_ALWAYSREADS",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_REGISTERINDEX",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_REGISTERMASK",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_SEMANTICNAME_NOT_FOUND",
    "D3D10_MESSAGE_ID_DEVICE_SHADER_LINKAGE_SYSTEMVALUE",
    "D3D10_MESSAGE_ID_DEVICE_SOGETTARGETS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_SOSETTARGETS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_SOSETTARGETS_OFFSET_UNALIGNED",
    "D3D10_MESSAGE_ID_DEVICE_VSGETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_VSGETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_VSGETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_VSSETCONSTANTBUFFERS_BUFFERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_VSSETCONSTANTBUFFERS_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_VSSETSAMPLERS_SAMPLERS_EMPTY",
    "D3D10_MESSAGE_ID_DEVICE_VSSETSHADERRESOURCES_HAZARD",
    "D3D10_MESSAGE_ID_DEVICE_VSSETSHADERRESOURCES_VIEWS_EMPTY",
    "D3D10_MESSAGE_ID_DRAWINDEXEDINSTANCED_NOT_SUPPORTED_BELOW_9_3",
    "D3D10_MESSAGE_ID_DRAWINDEXED_POINTLIST_UNSUPPORTED",
    "D3D10_MESSAGE_ID_DRAWINDEXED_STARTINDEXLOCATION_MUST_BE_POSITIVE",
    "D3D10_MESSAGE_ID_DRAWINSTANCED_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_GEOMETRY_SHADER_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_GETPRIVATEDATA_MOREDATA",
    "D3D10_MESSAGE_ID_GSSETCONSTANTBUFFERS_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_GSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_GSSETSAMPLERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_GSSETSHADERRESOURCES_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_GSSETSHADER_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_IASETINDEXBUFFER_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_IASETINDEXBUFFER_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_IASETINPUTLAYOUT_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_BAD_BUFFER_INDEX",
    "D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_IASETVERTEXBUFFERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_LIVE_BLENDSTATE",
    "D3D10_MESSAGE_ID_LIVE_BUFFER",
    "D3D10_MESSAGE_ID_LIVE_COUNTER",
    "D3D10_MESSAGE_ID_LIVE_DEPTHSTENCILSTATE",
    "D3D10_MESSAGE_ID_LIVE_DEPTHSTENCILVIEW",
    "D3D10_MESSAGE_ID_LIVE_DEVICE",
    "D3D10_MESSAGE_ID_LIVE_GEOMETRYSHADER",
    "D3D10_MESSAGE_ID_LIVE_INPUTLAYOUT",
    "D3D10_MESSAGE_ID_LIVE_OBJECT_SUMMARY",
    "D3D10_MESSAGE_ID_LIVE_PIXELSHADER",
    "D3D10_MESSAGE_ID_LIVE_PREDICATE",
    "D3D10_MESSAGE_ID_LIVE_QUERY",
    "D3D10_MESSAGE_ID_LIVE_RASTERIZERSTATE",
    "D3D10_MESSAGE_ID_LIVE_RENDERTARGETVIEW",
    "D3D10_MESSAGE_ID_LIVE_SAMPLER",
    "D3D10_MESSAGE_ID_LIVE_SHADERRESOURCEVIEW",
    "D3D10_MESSAGE_ID_LIVE_SWAPCHAIN",
    "D3D10_MESSAGE_ID_LIVE_TEXTURE1D",
    "D3D10_MESSAGE_ID_LIVE_TEXTURE2D",
    "D3D10_MESSAGE_ID_LIVE_TEXTURE3D",
    "D3D10_MESSAGE_ID_LIVE_VERTEXSHADER",
    "D3D10_MESSAGE_ID_MESSAGE_REPORTING_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_OMSETBLENDSTATE_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_OMSETDEPTHSTENCILSTATE_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_OMSETRENDERTARGETS_INVALIDVIEW",
    "D3D10_MESSAGE_ID_OMSETRENDERTARGETS_NO_DIFFERING_BIT_DEPTHS",
    "D3D10_MESSAGE_ID_OMSETRENDERTARGETS_NO_SRGB_MRT",
    "D3D10_MESSAGE_ID_OMSETRENDERTARGETS_TOO_MANY_RENDER_TARGETS",
    "D3D10_MESSAGE_ID_OMSETRENDERTARGETS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_PREDICATE_BEGIN_DURING_PREDICATION",
    "D3D10_MESSAGE_ID_PREDICATE_END_DURING_PREDICATION",
    "D3D10_MESSAGE_ID_PSSETCONSTANTBUFFERS_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_PSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_PSSETSAMPLERS_TOO_MANY_SAMPLERS",
    "D3D10_MESSAGE_ID_PSSETSAMPLERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_PSSETSHADERRESOURCES_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_PSSETSHADER_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_QUERY_BEGIN_ABANDONING_PREVIOUS_RESULTS",
    "D3D10_MESSAGE_ID_QUERY_BEGIN_DUPLICATE",
    "D3D10_MESSAGE_ID_QUERY_BEGIN_UNSUPPORTED",
    "D3D10_MESSAGE_ID_QUERY_END_ABANDONING_PREVIOUS_RESULTS",
    "D3D10_MESSAGE_ID_QUERY_END_WITHOUT_BEGIN",
    "D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_CALL",
    "D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_DATASIZE",
    "D3D10_MESSAGE_ID_QUERY_GETDATA_INVALID_FLAGS",
    "D3D10_MESSAGE_ID_REF_ACCESSING_INDEXABLE_TEMP_OUT_OF_RANGE",
    "D3D10_MESSAGE_ID_REF_HARDWARE_EXCEPTION",
    "D3D10_MESSAGE_ID_REF_INFO",
    "D3D10_MESSAGE_ID_REF_KMDRIVER_EXCEPTION",
    "D3D10_MESSAGE_ID_REF_OUT_OF_MEMORY",
    "D3D10_MESSAGE_ID_REF_PROBLEM_PARSING_SHADER",
    "D3D10_MESSAGE_ID_REF_SIMULATING_INFINITELY_FAST_HARDWARE",
    "D3D10_MESSAGE_ID_REF_THREADING_MODE",
    "D3D10_MESSAGE_ID_REF_UMDRIVER_EXCEPTION",
    "D3D10_MESSAGE_ID_RSSETSTATE_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_SETBLENDSTATE_SAMPLE_MASK_CANNOT_BE_ZERO",
    "D3D10_MESSAGE_ID_SETEXCEPTIONMODE_DEVICEREMOVED_RETURN",
    "D3D10_MESSAGE_ID_SETEXCEPTIONMODE_INVALIDARG_RETURN",
    "D3D10_MESSAGE_ID_SETEXCEPTIONMODE_UNRECOGNIZEDFLAGS",
    "D3D10_MESSAGE_ID_SETPREDICATION_INVALID_PREDICATE_STATE",
    "D3D10_MESSAGE_ID_SETPREDICATION_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_SETPRIVATEDATA_CHANGINGPARAMS",
    "D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDFLAGS",
    "D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDFREEDATA",
    "D3D10_MESSAGE_ID_SETPRIVATEDATA_INVALIDIUNKNOWN",
    "D3D10_MESSAGE_ID_SETPRIVATEDATA_OUTOFMEMORY",
    "D3D10_MESSAGE_ID_SHADERRESOURCEVIEW_GETDESC_LEGACY",
    "D3D10_MESSAGE_ID_SLOT_ZERO_MUST_BE_D3D10_INPUT_PER_VERTEX_DATA",
    "D3D10_MESSAGE_ID_SOSETTARGETS_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_SOSETTARGETS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_STREAM_OUT_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_STRING_FROM_APPLICATION",
    "D3D10_MESSAGE_ID_TEXTURE1D_MAP_ALREADYMAPPED",
    "D3D10_MESSAGE_ID_TEXTURE1D_MAP_DEVICEREMOVED_RETURN",
    "D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDFLAGS",
    "D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDMAPTYPE",
    "D3D10_MESSAGE_ID_TEXTURE1D_MAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE1D_UNMAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE1D_UNMAP_NOTMAPPED",
    "D3D10_MESSAGE_ID_TEXTURE2D_MAP_ALREADYMAPPED",
    "D3D10_MESSAGE_ID_TEXTURE2D_MAP_DEVICEREMOVED_RETURN",
    "D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDFLAGS",
    "D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDMAPTYPE",
    "D3D10_MESSAGE_ID_TEXTURE2D_MAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE2D_UNMAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE2D_UNMAP_NOTMAPPED",
    "D3D10_MESSAGE_ID_TEXTURE3D_MAP_ALREADYMAPPED",
    "D3D10_MESSAGE_ID_TEXTURE3D_MAP_DEVICEREMOVED_RETURN",
    "D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDFLAGS",
    "D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDMAPTYPE",
    "D3D10_MESSAGE_ID_TEXTURE3D_MAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE3D_UNMAP_INVALIDSUBRESOURCE",
    "D3D10_MESSAGE_ID_TEXTURE3D_UNMAP_NOTMAPPED",
    "D3D10_MESSAGE_ID_TEXT_FILTER_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_UNKNOWN",
    "D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONBOX",
    "D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONSTATE",
    "D3D10_MESSAGE_ID_UPDATESUBRESOURCE_INVALIDDESTINATIONSUBRESOURCE",
    "D3D10_MESSAGE_ID_VSSETCONSTANTBUFFERS_INVALIDBUFFER",
    "D3D10_MESSAGE_ID_VSSETCONSTANTBUFFERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_VSSETSAMPLERS_NOT_SUPPORTED",
    "D3D10_MESSAGE_ID_VSSETSAMPLERS_TOO_MANY_SAMPLERS",
    "D3D10_MESSAGE_ID_VSSETSAMPLERS_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_VSSETSHADERRESOURCES_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_VSSETSHADER_UNBINDDELETINGOBJECT",
    "D3D10_MESSAGE_ID_VSSHADERRESOURCES_NOT_SUPPORTED",
    "D3D10_MESSAGE_SEVERITY",
    "D3D10_MESSAGE_SEVERITY_CORRUPTION",
    "D3D10_MESSAGE_SEVERITY_ERROR",
    "D3D10_MESSAGE_SEVERITY_INFO",
    "D3D10_MESSAGE_SEVERITY_MESSAGE",
    "D3D10_MESSAGE_SEVERITY_WARNING",
    "D3D10_MIN_BORDER_COLOR_COMPONENT",
    "D3D10_MIN_DEPTH",
    "D3D10_MIN_FILTER_SHIFT",
    "D3D10_MIN_MAXANISOTROPY",
    "D3D10_MIP_FILTER_SHIFT",
    "D3D10_MIP_LOD_BIAS_MAX",
    "D3D10_MIP_LOD_BIAS_MIN",
    "D3D10_MIP_LOD_FRACTIONAL_BIT_COUNT",
    "D3D10_MIP_LOD_RANGE_BIT_COUNT",
    "D3D10_MULTISAMPLE_ANTIALIAS_LINE_WIDTH",
    "D3D10_MUTE_CATEGORY",
    "D3D10_MUTE_DEBUG_OUTPUT",
    "D3D10_MUTE_ID_DECIMAL",
    "D3D10_MUTE_ID_STRING",
    "D3D10_MUTE_SEVERITY",
    "D3D10_NONSAMPLE_FETCH_OUT_OF_RANGE_ACCESS_RESULT",
    "D3D10_PASS_DESC",
    "D3D10_PASS_SHADER_DESC",
    "D3D10_PIXEL_ADDRESS_RANGE_BIT_COUNT",
    "D3D10_PRE_SCISSOR_PIXEL_ADDRESS_RANGE_BIT_COUNT",
    "D3D10_PS_FRONTFACING_DEFAULT_VALUE",
    "D3D10_PS_FRONTFACING_FALSE_VALUE",
    "D3D10_PS_FRONTFACING_TRUE_VALUE",
    "D3D10_PS_INPUT_REGISTER_COMPONENTS",
    "D3D10_PS_INPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_PS_INPUT_REGISTER_COUNT",
    "D3D10_PS_INPUT_REGISTER_READS_PER_INST",
    "D3D10_PS_INPUT_REGISTER_READ_PORTS",
    "D3D10_PS_LEGACY_PIXEL_CENTER_FRACTIONAL_COMPONENT",
    "D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENTS",
    "D3D10_PS_OUTPUT_DEPTH_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_PS_OUTPUT_DEPTH_REGISTER_COUNT",
    "D3D10_PS_OUTPUT_REGISTER_COMPONENTS",
    "D3D10_PS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_PS_OUTPUT_REGISTER_COUNT",
    "D3D10_PS_PIXEL_CENTER_FRACTIONAL_COMPONENT",
    "D3D10_QUERY",
    "D3D10_QUERY_DATA_PIPELINE_STATISTICS",
    "D3D10_QUERY_DATA_SO_STATISTICS",
    "D3D10_QUERY_DATA_TIMESTAMP_DISJOINT",
    "D3D10_QUERY_DESC",
    "D3D10_QUERY_EVENT",
    "D3D10_QUERY_MISC_FLAG",
    "D3D10_QUERY_MISC_PREDICATEHINT",
    "D3D10_QUERY_OCCLUSION",
    "D3D10_QUERY_OCCLUSION_PREDICATE",
    "D3D10_QUERY_PIPELINE_STATISTICS",
    "D3D10_QUERY_SO_OVERFLOW_PREDICATE",
    "D3D10_QUERY_SO_STATISTICS",
    "D3D10_QUERY_TIMESTAMP",
    "D3D10_QUERY_TIMESTAMP_DISJOINT",
    "D3D10_RAISE_FLAG",
    "D3D10_RAISE_FLAG_DRIVER_INTERNAL_ERROR",
    "D3D10_RASTERIZER_DESC",
    "D3D10_REGKEY_PATH",
    "D3D10_RENDER_TARGET_BLEND_DESC1",
    "D3D10_RENDER_TARGET_VIEW_DESC",
    "D3D10_REQ_BLEND_OBJECT_COUNT_PER_CONTEXT",
    "D3D10_REQ_BUFFER_RESOURCE_TEXEL_COUNT_2_TO_EXP",
    "D3D10_REQ_CONSTANT_BUFFER_ELEMENT_COUNT",
    "D3D10_REQ_DEPTH_STENCIL_OBJECT_COUNT_PER_CONTEXT",
    "D3D10_REQ_DRAWINDEXED_INDEX_COUNT_2_TO_EXP",
    "D3D10_REQ_DRAW_VERTEX_COUNT_2_TO_EXP",
    "D3D10_REQ_FILTERING_HW_ADDRESSABLE_RESOURCE_DIMENSION",
    "D3D10_REQ_GS_INVOCATION_32BIT_OUTPUT_COMPONENT_LIMIT",
    "D3D10_REQ_IMMEDIATE_CONSTANT_BUFFER_ELEMENT_COUNT",
    "D3D10_REQ_MAXANISOTROPY",
    "D3D10_REQ_MIP_LEVELS",
    "D3D10_REQ_MULTI_ELEMENT_STRUCTURE_SIZE_IN_BYTES",
    "D3D10_REQ_RASTERIZER_OBJECT_COUNT_PER_CONTEXT",
    "D3D10_REQ_RENDER_TO_BUFFER_WINDOW_WIDTH",
    "D3D10_REQ_RESOURCE_SIZE_IN_MEGABYTES",
    "D3D10_REQ_RESOURCE_VIEW_COUNT_PER_CONTEXT_2_TO_EXP",
    "D3D10_REQ_SAMPLER_OBJECT_COUNT_PER_CONTEXT",
    "D3D10_REQ_TEXTURE1D_ARRAY_AXIS_DIMENSION",
    "D3D10_REQ_TEXTURE1D_U_DIMENSION",
    "D3D10_REQ_TEXTURE2D_ARRAY_AXIS_DIMENSION",
    "D3D10_REQ_TEXTURE2D_U_OR_V_DIMENSION",
    "D3D10_REQ_TEXTURE3D_U_V_OR_W_DIMENSION",
    "D3D10_REQ_TEXTURECUBE_DIMENSION",
    "D3D10_RESINFO_INSTRUCTION_MISSING_COMPONENT_RETVAL",
    "D3D10_RESOURCE_DIMENSION",
    "D3D10_RESOURCE_DIMENSION_BUFFER",
    "D3D10_RESOURCE_DIMENSION_TEXTURE1D",
    "D3D10_RESOURCE_DIMENSION_TEXTURE2D",
    "D3D10_RESOURCE_DIMENSION_TEXTURE3D",
    "D3D10_RESOURCE_DIMENSION_UNKNOWN",
    "D3D10_RESOURCE_MISC_FLAG",
    "D3D10_RESOURCE_MISC_GDI_COMPATIBLE",
    "D3D10_RESOURCE_MISC_GENERATE_MIPS",
    "D3D10_RESOURCE_MISC_SHARED",
    "D3D10_RESOURCE_MISC_SHARED_KEYEDMUTEX",
    "D3D10_RESOURCE_MISC_TEXTURECUBE",
    "D3D10_RTV_DIMENSION",
    "D3D10_RTV_DIMENSION_BUFFER",
    "D3D10_RTV_DIMENSION_TEXTURE1D",
    "D3D10_RTV_DIMENSION_TEXTURE1DARRAY",
    "D3D10_RTV_DIMENSION_TEXTURE2D",
    "D3D10_RTV_DIMENSION_TEXTURE2DARRAY",
    "D3D10_RTV_DIMENSION_TEXTURE2DMS",
    "D3D10_RTV_DIMENSION_TEXTURE2DMSARRAY",
    "D3D10_RTV_DIMENSION_TEXTURE3D",
    "D3D10_RTV_DIMENSION_UNKNOWN",
    "D3D10_SAMPLER_DESC",
    "D3D10_SDK_LAYERS_VERSION",
    "D3D10_SDK_VERSION",
    "D3D10_SHADER_AVOID_FLOW_CONTROL",
    "D3D10_SHADER_BUFFER_DESC",
    "D3D10_SHADER_DEBUG",
    "D3D10_SHADER_DEBUG_FILE_INFO",
    "D3D10_SHADER_DEBUG_INFO",
    "D3D10_SHADER_DEBUG_INPUT_INFO",
    "D3D10_SHADER_DEBUG_INST_INFO",
    "D3D10_SHADER_DEBUG_NAME_FOR_BINARY",
    "D3D10_SHADER_DEBUG_NAME_FOR_SOURCE",
    "D3D10_SHADER_DEBUG_OUTPUTREG_INFO",
    "D3D10_SHADER_DEBUG_OUTPUTVAR",
    "D3D10_SHADER_DEBUG_REGTYPE",
    "D3D10_SHADER_DEBUG_REG_CBUFFER",
    "D3D10_SHADER_DEBUG_REG_FORCE_DWORD",
    "D3D10_SHADER_DEBUG_REG_IMMEDIATECBUFFER",
    "D3D10_SHADER_DEBUG_REG_INPUT",
    "D3D10_SHADER_DEBUG_REG_LITERAL",
    "D3D10_SHADER_DEBUG_REG_OUTPUT",
    "D3D10_SHADER_DEBUG_REG_SAMPLER",
    "D3D10_SHADER_DEBUG_REG_TBUFFER",
    "D3D10_SHADER_DEBUG_REG_TEMP",
    "D3D10_SHADER_DEBUG_REG_TEMPARRAY",
    "D3D10_SHADER_DEBUG_REG_TEXTURE",
    "D3D10_SHADER_DEBUG_REG_UNUSED",
    "D3D10_SHADER_DEBUG_SCOPETYPE",
    "D3D10_SHADER_DEBUG_SCOPEVAR_INFO",
    "D3D10_SHADER_DEBUG_SCOPE_ANNOTATION",
    "D3D10_SHADER_DEBUG_SCOPE_BLOCK",
    "D3D10_SHADER_DEBUG_SCOPE_FORCE_DWORD",
    "D3D10_SHADER_DEBUG_SCOPE_FORLOOP",
    "D3D10_SHADER_DEBUG_SCOPE_FUNC_PARAMS",
    "D3D10_SHADER_DEBUG_SCOPE_GLOBAL",
    "D3D10_SHADER_DEBUG_SCOPE_INFO",
    "D3D10_SHADER_DEBUG_SCOPE_NAMESPACE",
    "D3D10_SHADER_DEBUG_SCOPE_STATEBLOCK",
    "D3D10_SHADER_DEBUG_SCOPE_STRUCT",
    "D3D10_SHADER_DEBUG_TOKEN_INFO",
    "D3D10_SHADER_DEBUG_VARTYPE",
    "D3D10_SHADER_DEBUG_VAR_FORCE_DWORD",
    "D3D10_SHADER_DEBUG_VAR_FUNCTION",
    "D3D10_SHADER_DEBUG_VAR_INFO",
    "D3D10_SHADER_DEBUG_VAR_VARIABLE",
    "D3D10_SHADER_DESC",
    "D3D10_SHADER_ENABLE_BACKWARDS_COMPATIBILITY",
    "D3D10_SHADER_ENABLE_STRICTNESS",
    "D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_0",
    "D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_1_1",
    "D3D10_SHADER_FLAGS2_FORCE_ROOT_SIGNATURE_LATEST",
    "D3D10_SHADER_FORCE_PS_SOFTWARE_NO_OPT",
    "D3D10_SHADER_FORCE_VS_SOFTWARE_NO_OPT",
    "D3D10_SHADER_IEEE_STRICTNESS",
    "D3D10_SHADER_INPUT_BIND_DESC",
    "D3D10_SHADER_MAJOR_VERSION",
    "D3D10_SHADER_MINOR_VERSION",
    "D3D10_SHADER_NO_PRESHADER",
    "D3D10_SHADER_OPTIMIZATION_LEVEL0",
    "D3D10_SHADER_OPTIMIZATION_LEVEL1",
    "D3D10_SHADER_OPTIMIZATION_LEVEL3",
    "D3D10_SHADER_PACK_MATRIX_COLUMN_MAJOR",
    "D3D10_SHADER_PACK_MATRIX_ROW_MAJOR",
    "D3D10_SHADER_PARTIAL_PRECISION",
    "D3D10_SHADER_PREFER_FLOW_CONTROL",
    "D3D10_SHADER_RESOURCES_MAY_ALIAS",
    "D3D10_SHADER_RESOURCE_VIEW_DESC",
    "D3D10_SHADER_RESOURCE_VIEW_DESC1",
    "D3D10_SHADER_SKIP_OPTIMIZATION",
    "D3D10_SHADER_SKIP_VALIDATION",
    "D3D10_SHADER_TYPE_DESC",
    "D3D10_SHADER_VARIABLE_DESC",
    "D3D10_SHADER_WARNINGS_ARE_ERRORS",
    "D3D10_SHIFT_INSTRUCTION_PAD_VALUE",
    "D3D10_SHIFT_INSTRUCTION_SHIFT_VALUE_BIT_COUNT",
    "D3D10_SIGNATURE_PARAMETER_DESC",
    "D3D10_SIMULTANEOUS_RENDER_TARGET_COUNT",
    "D3D10_SO_BUFFER_MAX_STRIDE_IN_BYTES",
    "D3D10_SO_BUFFER_MAX_WRITE_WINDOW_IN_BYTES",
    "D3D10_SO_BUFFER_SLOT_COUNT",
    "D3D10_SO_DDI_REGISTER_INDEX_DENOTING_GAP",
    "D3D10_SO_DECLARATION_ENTRY",
    "D3D10_SO_MULTIPLE_BUFFER_ELEMENTS_PER_BUFFER",
    "D3D10_SO_SINGLE_BUFFER_COMPONENT_LIMIT",
    "D3D10_SRGB_GAMMA",
    "D3D10_SRGB_TO_FLOAT_DENOMINATOR_1",
    "D3D10_SRGB_TO_FLOAT_DENOMINATOR_2",
    "D3D10_SRGB_TO_FLOAT_EXPONENT",
    "D3D10_SRGB_TO_FLOAT_OFFSET",
    "D3D10_SRGB_TO_FLOAT_THRESHOLD",
    "D3D10_SRGB_TO_FLOAT_TOLERANCE_IN_ULP",
    "D3D10_STANDARD_COMPONENT_BIT_COUNT",
    "D3D10_STANDARD_COMPONENT_BIT_COUNT_DOUBLED",
    "D3D10_STANDARD_MAXIMUM_ELEMENT_ALIGNMENT_BYTE_MULTIPLE",
    "D3D10_STANDARD_MULTISAMPLE_PATTERN",
    "D3D10_STANDARD_MULTISAMPLE_QUALITY_LEVELS",
    "D3D10_STANDARD_PIXEL_COMPONENT_COUNT",
    "D3D10_STANDARD_PIXEL_ELEMENT_COUNT",
    "D3D10_STANDARD_VECTOR_SIZE",
    "D3D10_STANDARD_VERTEX_ELEMENT_COUNT",
    "D3D10_STANDARD_VERTEX_TOTAL_COMPONENT_COUNT",
    "D3D10_STATE_BLOCK_MASK",
    "D3D10_STENCIL_OP",
    "D3D10_STENCIL_OP_DECR",
    "D3D10_STENCIL_OP_DECR_SAT",
    "D3D10_STENCIL_OP_INCR",
    "D3D10_STENCIL_OP_INCR_SAT",
    "D3D10_STENCIL_OP_INVERT",
    "D3D10_STENCIL_OP_KEEP",
    "D3D10_STENCIL_OP_REPLACE",
    "D3D10_STENCIL_OP_ZERO",
    "D3D10_SUBPIXEL_FRACTIONAL_BIT_COUNT",
    "D3D10_SUBRESOURCE_DATA",
    "D3D10_SUBTEXEL_FRACTIONAL_BIT_COUNT",
    "D3D10_TECHNIQUE_DESC",
    "D3D10_TEX1D_ARRAY_DSV",
    "D3D10_TEX1D_ARRAY_RTV",
    "D3D10_TEX1D_ARRAY_SRV",
    "D3D10_TEX1D_DSV",
    "D3D10_TEX1D_RTV",
    "D3D10_TEX1D_SRV",
    "D3D10_TEX2DMS_ARRAY_DSV",
    "D3D10_TEX2DMS_ARRAY_RTV",
    "D3D10_TEX2DMS_ARRAY_SRV",
    "D3D10_TEX2DMS_DSV",
    "D3D10_TEX2DMS_RTV",
    "D3D10_TEX2DMS_SRV",
    "D3D10_TEX2D_ARRAY_DSV",
    "D3D10_TEX2D_ARRAY_RTV",
    "D3D10_TEX2D_ARRAY_SRV",
    "D3D10_TEX2D_DSV",
    "D3D10_TEX2D_RTV",
    "D3D10_TEX2D_SRV",
    "D3D10_TEX3D_RTV",
    "D3D10_TEX3D_SRV",
    "D3D10_TEXCUBE_ARRAY_SRV1",
    "D3D10_TEXCUBE_SRV",
    "D3D10_TEXEL_ADDRESS_RANGE_BIT_COUNT",
    "D3D10_TEXTURE1D_DESC",
    "D3D10_TEXTURE2D_DESC",
    "D3D10_TEXTURE3D_DESC",
    "D3D10_TEXTURECUBE_FACE",
    "D3D10_TEXTURECUBE_FACE_NEGATIVE_X",
    "D3D10_TEXTURECUBE_FACE_NEGATIVE_Y",
    "D3D10_TEXTURECUBE_FACE_NEGATIVE_Z",
    "D3D10_TEXTURECUBE_FACE_POSITIVE_X",
    "D3D10_TEXTURECUBE_FACE_POSITIVE_Y",
    "D3D10_TEXTURECUBE_FACE_POSITIVE_Z",
    "D3D10_TEXTURE_ADDRESS_BORDER",
    "D3D10_TEXTURE_ADDRESS_CLAMP",
    "D3D10_TEXTURE_ADDRESS_MIRROR",
    "D3D10_TEXTURE_ADDRESS_MIRROR_ONCE",
    "D3D10_TEXTURE_ADDRESS_MODE",
    "D3D10_TEXTURE_ADDRESS_WRAP",
    "D3D10_TEXT_1BIT_BIT",
    "D3D10_UNBOUND_MEMORY_ACCESS_RESULT",
    "D3D10_UNMUTE_SEVERITY_INFO",
    "D3D10_USAGE",
    "D3D10_USAGE_DEFAULT",
    "D3D10_USAGE_DYNAMIC",
    "D3D10_USAGE_IMMUTABLE",
    "D3D10_USAGE_STAGING",
    "D3D10_VIEWPORT",
    "D3D10_VIEWPORT_AND_SCISSORRECT_MAX_INDEX",
    "D3D10_VIEWPORT_AND_SCISSORRECT_OBJECT_COUNT_PER_PIPELINE",
    "D3D10_VIEWPORT_BOUNDS_MAX",
    "D3D10_VIEWPORT_BOUNDS_MIN",
    "D3D10_VS_INPUT_REGISTER_COMPONENTS",
    "D3D10_VS_INPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_VS_INPUT_REGISTER_COUNT",
    "D3D10_VS_INPUT_REGISTER_READS_PER_INST",
    "D3D10_VS_INPUT_REGISTER_READ_PORTS",
    "D3D10_VS_OUTPUT_REGISTER_COMPONENTS",
    "D3D10_VS_OUTPUT_REGISTER_COMPONENT_BIT_COUNT",
    "D3D10_VS_OUTPUT_REGISTER_COUNT",
    "D3D10_WHQL_CONTEXT_COUNT_FOR_RESOURCE_LIMIT",
    "D3D10_WHQL_DRAWINDEXED_INDEX_COUNT_2_TO_EXP",
    "D3D10_WHQL_DRAW_VERTEX_COUNT_2_TO_EXP",
    "D3D11_SHADER_DEBUG_REG_INTERFACE_POINTERS",
    "D3D11_SHADER_DEBUG_REG_UAV",
    "D3D_MAJOR_VERSION",
    "D3D_MINOR_VERSION",
    "D3D_SPEC_DATE_DAY",
    "D3D_SPEC_DATE_MONTH",
    "D3D_SPEC_DATE_YEAR",
    "D3D_SPEC_VERSION",
    "DXGI_DEBUG_D3D10",
    "GUID_DeviceType",
    "ID3D10Asynchronous",
    "ID3D10BlendState",
    "ID3D10BlendState1",
    "ID3D10Buffer",
    "ID3D10Counter",
    "ID3D10Debug",
    "ID3D10DepthStencilState",
    "ID3D10DepthStencilView",
    "ID3D10Device",
    "ID3D10Device1",
    "ID3D10DeviceChild",
    "ID3D10Effect",
    "ID3D10EffectBlendVariable",
    "ID3D10EffectConstantBuffer",
    "ID3D10EffectDepthStencilVariable",
    "ID3D10EffectDepthStencilViewVariable",
    "ID3D10EffectMatrixVariable",
    "ID3D10EffectPass",
    "ID3D10EffectPool",
    "ID3D10EffectRasterizerVariable",
    "ID3D10EffectRenderTargetViewVariable",
    "ID3D10EffectSamplerVariable",
    "ID3D10EffectScalarVariable",
    "ID3D10EffectShaderResourceVariable",
    "ID3D10EffectShaderVariable",
    "ID3D10EffectStringVariable",
    "ID3D10EffectTechnique",
    "ID3D10EffectType",
    "ID3D10EffectVariable",
    "ID3D10EffectVectorVariable",
    "ID3D10GeometryShader",
    "ID3D10InfoQueue",
    "ID3D10InputLayout",
    "ID3D10Multithread",
    "ID3D10PixelShader",
    "ID3D10Predicate",
    "ID3D10Query",
    "ID3D10RasterizerState",
    "ID3D10RenderTargetView",
    "ID3D10Resource",
    "ID3D10SamplerState",
    "ID3D10ShaderReflection",
    "ID3D10ShaderReflection1",
    "ID3D10ShaderReflectionConstantBuffer",
    "ID3D10ShaderReflectionType",
    "ID3D10ShaderReflectionVariable",
    "ID3D10ShaderResourceView",
    "ID3D10ShaderResourceView1",
    "ID3D10StateBlock",
    "ID3D10SwitchToRef",
    "ID3D10Texture1D",
    "ID3D10Texture2D",
    "ID3D10Texture3D",
    "ID3D10VertexShader",
    "ID3D10View",
    "PFN_D3D10_CREATE_DEVICE1",
    "PFN_D3D10_CREATE_DEVICE_AND_SWAP_CHAIN1",
    "_FACD3D10",
]
