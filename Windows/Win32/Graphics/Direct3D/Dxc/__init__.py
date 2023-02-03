from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.Graphics.Direct3D.Dxc
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
DXC_HASHFLAG_INCLUDES_SOURCE: UInt32 = 1
DXC_ARG_DEBUG: String = '-Zi'
DXC_ARG_SKIP_VALIDATION: String = '-Vd'
DXC_ARG_SKIP_OPTIMIZATIONS: String = '-Od'
DXC_ARG_PACK_MATRIX_ROW_MAJOR: String = '-Zpr'
DXC_ARG_PACK_MATRIX_COLUMN_MAJOR: String = '-Zpc'
DXC_ARG_AVOID_FLOW_CONTROL: String = '-Gfa'
DXC_ARG_PREFER_FLOW_CONTROL: String = '-Gfp'
DXC_ARG_ENABLE_STRICTNESS: String = '-Ges'
DXC_ARG_ENABLE_BACKWARDS_COMPATIBILITY: String = '-Gec'
DXC_ARG_IEEE_STRICTNESS: String = '-Gis'
DXC_ARG_OPTIMIZATION_LEVEL0: String = '-O0'
DXC_ARG_OPTIMIZATION_LEVEL1: String = '-O1'
DXC_ARG_OPTIMIZATION_LEVEL2: String = '-O2'
DXC_ARG_OPTIMIZATION_LEVEL3: String = '-O3'
DXC_ARG_WARNINGS_ARE_ERRORS: String = '-WX'
DXC_ARG_RESOURCES_MAY_ALIAS: String = '-res_may_alias'
DXC_ARG_ALL_RESOURCES_BOUND: String = '-all_resources_bound'
DXC_ARG_DEBUG_NAME_FOR_SOURCE: String = '-Zss'
DXC_ARG_DEBUG_NAME_FOR_BINARY: String = '-Zsb'
DXC_EXTRA_OUTPUT_NAME_STDOUT: String = '*stdout*'
DXC_EXTRA_OUTPUT_NAME_STDERR: String = '*stderr*'
DxcValidatorFlags_Default: UInt32 = 0
DxcValidatorFlags_InPlaceEdit: UInt32 = 1
DxcValidatorFlags_RootSignatureOnly: UInt32 = 2
DxcValidatorFlags_ModuleOnly: UInt32 = 4
DxcValidatorFlags_ValidMask: UInt32 = 7
DxcVersionInfoFlags_None: UInt32 = 0
DxcVersionInfoFlags_Debug: UInt32 = 1
DxcVersionInfoFlags_Internal: UInt32 = 2
CLSID_DxcCompiler: Guid = Guid('73e22d93-e6ce-47f3-b5-bf-f0-66-4f-39-c1-b0')
CLSID_DxcLinker: Guid = Guid('ef6a8087-b0ea-4d56-9e-45-d0-7e-1a-8b-78-06')
CLSID_DxcDiaDataSource: Guid = Guid('cd1f6b73-2ab0-484d-8e-dc-eb-e7-a4-3c-a0-9f')
CLSID_DxcCompilerArgs: Guid = Guid('3e56ae82-224d-470f-a1-a1-fe-30-16-ee-9f-9d')
CLSID_DxcLibrary: Guid = Guid('6245d6af-66e0-48fd-80-b4-4d-27-17-96-74-8c')
CLSID_DxcValidator: Guid = Guid('8ca3e215-f728-4cf3-8c-dd-88-af-91-75-87-a1')
CLSID_DxcAssembler: Guid = Guid('d728db68-f903-4f80-94-cd-dc-cf-76-ec-71-51')
CLSID_DxcContainerReflection: Guid = Guid('b9f54489-55b8-400c-ba-3a-16-75-e4-72-8b-91')
CLSID_DxcOptimizer: Guid = Guid('ae2cd79f-cc22-453f-9b-6b-b1-24-e7-a5-20-4c')
CLSID_DxcContainerBuilder: Guid = Guid('94134294-411f-4574-b4-d0-87-41-e2-52-40-d2')
CLSID_DxcPdbUtils: Guid = Guid('54621dfb-f2ce-457e-ae-8c-ec-35-5f-ae-ec-7c')
@winfunctype('dxcompiler.dll')
def DxcCreateInstance(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('dxcompiler.dll')
def DxcCreateInstance2(pMalloc: Windows.Win32.System.Com.IMalloc_head, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
DXC_CP = UInt32
DXC_CP_ACP: DXC_CP = 0
DXC_CP_UTF16: DXC_CP = 1200
DXC_CP_UTF8: DXC_CP = 65001
DXC_OUT_KIND = Int32
DXC_OUT_NONE: DXC_OUT_KIND = 0
DXC_OUT_OBJECT: DXC_OUT_KIND = 1
DXC_OUT_ERRORS: DXC_OUT_KIND = 2
DXC_OUT_PDB: DXC_OUT_KIND = 3
DXC_OUT_SHADER_HASH: DXC_OUT_KIND = 4
DXC_OUT_DISASSEMBLY: DXC_OUT_KIND = 5
DXC_OUT_HLSL: DXC_OUT_KIND = 6
DXC_OUT_TEXT: DXC_OUT_KIND = 7
DXC_OUT_REFLECTION: DXC_OUT_KIND = 8
DXC_OUT_ROOT_SIGNATURE: DXC_OUT_KIND = 9
DXC_OUT_EXTRA_OUTPUTS: DXC_OUT_KIND = 10
DXC_OUT_FORCE_DWORD: DXC_OUT_KIND = -1
class DxcArgPair(Structure):
    pName: Windows.Win32.Foundation.PWSTR
    pValue: Windows.Win32.Foundation.PWSTR
class DxcBuffer(Structure):
    Ptr: c_void_p
    Size: UIntPtr
    Encoding: UInt32
@winfunctype_pointer
def DxcCreateInstance2Proc(pMalloc: Windows.Win32.System.Com.IMalloc_head, rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype_pointer
def DxcCreateInstanceProc(rclsid: POINTER(Guid), riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class DxcDefine(Structure):
    Name: Windows.Win32.Foundation.PWSTR
    Value: Windows.Win32.Foundation.PWSTR
class DxcShaderHash(Structure):
    Flags: UInt32
    HashDigest: Byte * 16
class IDxcAssembler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('091f7a26-1c1f-4948-90-4b-e6-e3-a8-a7-71-d5')
    @commethod(3)
    def AssembleToContainer(pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcBlob(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8ba5fb08-5195-40e2-ac-58-0d-98-9c-3a-01-02')
    @commethod(3)
    def GetBufferPointer() -> c_void_p: ...
    @commethod(4)
    def GetBufferSize() -> UIntPtr: ...
class IDxcBlobEncoding(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob
    Guid = Guid('7241d424-2646-4191-97-c0-98-e9-6e-42-fc-68')
    @commethod(5)
    def GetEncoding(pKnown: POINTER(Windows.Win32.Foundation.BOOL), pCodePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcBlobUtf16(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    Guid = Guid('a3f84eab-0faa-497e-a3-9c-ee-6e-d6-0b-2d-84')
    @commethod(6)
    def GetStringPointer() -> Windows.Win32.Foundation.PWSTR: ...
    @commethod(7)
    def GetStringLength() -> UIntPtr: ...
class IDxcBlobUtf8(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding
    Guid = Guid('3da636c9-ba71-4024-a3-01-30-cb-f1-25-30-5b')
    @commethod(6)
    def GetStringPointer() -> Windows.Win32.Foundation.PSTR: ...
    @commethod(7)
    def GetStringLength() -> UIntPtr: ...
class IDxcCompiler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('8c210bf3-011f-4422-8d-70-6f-9a-cb-8d-b6-17')
    @commethod(3)
    def Compile(pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Preprocess(pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Disassemble(pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppDisassembly: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompiler2(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompiler
    Guid = Guid('a005a9d9-b8bb-4594-b5-c9-0e-63-3b-ec-4d-37')
    @commethod(6)
    def CompileWithDebug(pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head), ppDebugBlobName: POINTER(Windows.Win32.Foundation.PWSTR), ppDebugBlob: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompiler3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('228b4687-5a6a-4730-90-0c-97-02-b2-20-3f-54')
    @commethod(3)
    def Compile(pSource: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pIncludeHandler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head, riid: POINTER(Guid), ppResult: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Disassemble(pObject: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), riid: POINTER(Guid), ppResult: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcCompilerArgs(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('73effe2a-70dc-45f8-96-90-ef-f6-4c-02-42-9d')
    @commethod(3)
    def GetArguments() -> POINTER(Windows.Win32.Foundation.PWSTR): ...
    @commethod(4)
    def GetCount() -> UInt32: ...
    @commethod(5)
    def AddArguments(pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def AddArgumentsUTF8(pArguments: POINTER(Windows.Win32.Foundation.PSTR), argCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def AddDefines(pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcContainerBuilder(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('334b1f50-2292-4b35-99-a1-25-58-8d-8c-17-fe')
    @commethod(3)
    def Load(pDxilContainerHeader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AddPart(fourCC: UInt32, pSource: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RemovePart(fourCC: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SerializeContainer(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcContainerReflection(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d2c21b26-8350-4bdc-97-6a-33-1c-e6-f4-c5-4c')
    @commethod(3)
    def Load(pContainer: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPartCount(pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetPartKind(idx: UInt32, pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPartContent(idx: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindFirstPartKind(kind: UInt32, pResult: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPartReflection(idx: UInt32, iid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcExtraOutputs(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('319b37a2-a5c2-494a-a5-de-48-01-b2-fa-f9-89')
    @commethod(3)
    def GetOutputCount() -> UInt32: ...
    @commethod(4)
    def GetOutput(uIndex: UInt32, iid: POINTER(Guid), ppvObject: POINTER(c_void_p), ppOutputType: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head), ppOutputName: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcIncludeHandler(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7f61fc7d-950d-467f-b3-e3-3c-02-fb-49-18-7c')
    @commethod(3)
    def LoadSource(pFilename: Windows.Win32.Foundation.PWSTR, ppIncludeSource: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcLibrary(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e5204dc7-d18c-4c3c-bd-fb-85-16-73-98-0f-e7')
    @commethod(3)
    def SetMalloc(pMalloc: Windows.Win32.System.Com.IMalloc_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBlobFromBlob(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, offset: UInt32, length: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateBlobFromFile(pFileName: Windows.Win32.Foundation.PWSTR, codePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP), pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlobWithEncodingFromPinned(pText: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateBlobWithEncodingOnHeapCopy(pText: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateBlobWithEncodingOnMalloc(pText: c_void_p, pIMalloc: Windows.Win32.System.Com.IMalloc_head, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateIncludeHandler(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateStreamFromBlobReadOnly(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBlobAsUtf8(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetBlobAsUtf16(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcLinker(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f1b5be2a-62dd-4327-a1-c2-42-ac-1e-1e-78-e6')
    @commethod(3)
    def RegisterLibrary(pLibName: Windows.Win32.Foundation.PWSTR, pLib: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Link(pEntryName: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pLibNames: POINTER(Windows.Win32.Foundation.PWSTR), libCount: UInt32, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOperationResult(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('cedb484a-d4e9-445a-b9-91-ca-21-ca-15-7d-c2')
    @commethod(3)
    def GetStatus(pStatus: POINTER(Windows.Win32.Foundation.HRESULT)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetResult(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetErrorBuffer(ppErrors: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOptimizer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('25740e2e-9cba-401b-91-19-4f-b4-2f-39-f2-70')
    @commethod(3)
    def GetAvailablePassCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAvailablePass(index: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOptimizerPass_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def RunOptimizer(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppOptions: POINTER(Windows.Win32.Foundation.PWSTR), optionCount: UInt32, pOutputModule: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head), ppOutputText: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcOptimizerPass(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ae2cd79f-cc22-453f-9b-6b-b1-24-e7-a5-20-4c')
    @commethod(3)
    def GetOptionName(ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDescription(ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetOptionArgCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetOptionArgName(argIndex: UInt32, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetOptionArgDescription(argIndex: UInt32, ppResult: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcPdbUtils(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e6c9647e-9d6a-4c3b-b9-4c-52-4b-5a-6c-34-3d')
    @commethod(3)
    def Load(pPdbOrDxil: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSourceCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSource(uIndex: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSourceName(uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetFlagCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetFlag(uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetArgCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetArg(uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetArgPairCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetArgPair(uIndex: UInt32, pName: POINTER(Windows.Win32.Foundation.BSTR), pValue: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetDefineCount(pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetDefine(uIndex: UInt32, pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetTargetProfile(pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def GetEntryPoint(pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetMainFileName(pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def GetHash(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetName(pResult: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def IsFullPDB() -> Windows.Win32.Foundation.BOOL: ...
    @commethod(21)
    def GetFullPDB(ppFullPDB: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def GetVersionInfo(ppVersionInfo: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcVersionInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SetCompiler(pCompiler: Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompiler3_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def CompileForFullPDB(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def OverrideArgs(pArgPairs: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcArgPair_head), uNumArgPairs: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def OverrideRootSignature(pRootSignature: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcResult(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult
    Guid = Guid('58346cda-dde7-4497-94-61-6f-87-af-5e-06-59')
    @commethod(6)
    def HasOutput(dxcOutKind: Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND) -> Windows.Win32.Foundation.BOOL: ...
    @commethod(7)
    def GetOutput(dxcOutKind: Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND, iid: POINTER(Guid), ppvObject: POINTER(c_void_p), ppOutputName: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetNumOutputs() -> UInt32: ...
    @commethod(9)
    def GetOutputByIndex(Index: UInt32) -> Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND: ...
    @commethod(10)
    def PrimaryOutput() -> Windows.Win32.Graphics.Direct3D.Dxc.DXC_OUT_KIND: ...
class IDxcUtils(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('4605c4cb-2019-492a-ad-a4-65-f2-0b-b7-d6-7f')
    @commethod(3)
    def CreateBlobFromBlob(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, offset: UInt32, length: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateBlobFromPinned(pData: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def MoveToBlob(pData: c_void_p, pIMalloc: Windows.Win32.System.Com.IMalloc_head, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateBlob(pData: c_void_p, size: UInt32, codePage: Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def LoadFile(pFileName: Windows.Win32.Foundation.PWSTR, pCodePage: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DXC_CP), pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobEncoding_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateReadOnlyStreamFromBlob(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppStream: POINTER(Windows.Win32.System.Com.IStream_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateDefaultIncludeHandler(ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcIncludeHandler_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetBlobAsUtf8(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf8_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def GetBlobAsUtf16(pBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, pBlobEncoding: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlobUtf16_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetDxilContainerPart(pShader: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), DxcPart: UInt32, ppPartData: POINTER(c_void_p), pPartSizeInBytes: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def CreateReflection(pData: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), iid: POINTER(Guid), ppvReflection: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def BuildArguments(pSourceName: Windows.Win32.Foundation.PWSTR, pEntryPoint: Windows.Win32.Foundation.PWSTR, pTargetProfile: Windows.Win32.Foundation.PWSTR, pArguments: POINTER(Windows.Win32.Foundation.PWSTR), argCount: UInt32, pDefines: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcDefine_head), defineCount: UInt32, ppArgs: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcCompilerArgs_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def GetPDBContents(pPDBBlob: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, ppHash: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head), ppContainer: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcValidator(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a6e82bd2-1fd7-4826-98-11-28-57-e7-97-f4-9a')
    @commethod(3)
    def Validate(pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, Flags: UInt32, ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcValidator2(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcValidator
    Guid = Guid('458e1fd1-b1b2-4750-a6-e1-9c-10-f0-3b-ed-92')
    @commethod(4)
    def ValidateWithDebug(pShader: Windows.Win32.Graphics.Direct3D.Dxc.IDxcBlob_head, Flags: UInt32, pOptDebugBitcode: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.DxcBuffer_head), ppResult: POINTER(Windows.Win32.Graphics.Direct3D.Dxc.IDxcOperationResult_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('b04f5b50-2059-4f12-a8-ff-a1-e0-cd-e1-cc-7e')
    @commethod(3)
    def GetVersion(pMajor: POINTER(UInt32), pMinor: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFlags(pFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo2(c_void_p):
    extends: Windows.Win32.Graphics.Direct3D.Dxc.IDxcVersionInfo
    Guid = Guid('fb6904c4-42f0-4b62-9c-46-98-3a-f7-da-7c-83')
    @commethod(5)
    def GetCommitInfo(pCommitCount: POINTER(UInt32), pCommitHash: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
class IDxcVersionInfo3(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('5e13e843-9d25-473c-9a-d2-03-b2-d0-b4-4b-1e')
    @commethod(3)
    def GetCustomVersionString(pVersionString: POINTER(POINTER(SByte))) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'DxcArgPair')
make_head(_module, 'DxcBuffer')
make_head(_module, 'DxcCreateInstance2Proc')
make_head(_module, 'DxcCreateInstanceProc')
make_head(_module, 'DxcDefine')
make_head(_module, 'DxcShaderHash')
make_head(_module, 'IDxcAssembler')
make_head(_module, 'IDxcBlob')
make_head(_module, 'IDxcBlobEncoding')
make_head(_module, 'IDxcBlobUtf16')
make_head(_module, 'IDxcBlobUtf8')
make_head(_module, 'IDxcCompiler')
make_head(_module, 'IDxcCompiler2')
make_head(_module, 'IDxcCompiler3')
make_head(_module, 'IDxcCompilerArgs')
make_head(_module, 'IDxcContainerBuilder')
make_head(_module, 'IDxcContainerReflection')
make_head(_module, 'IDxcExtraOutputs')
make_head(_module, 'IDxcIncludeHandler')
make_head(_module, 'IDxcLibrary')
make_head(_module, 'IDxcLinker')
make_head(_module, 'IDxcOperationResult')
make_head(_module, 'IDxcOptimizer')
make_head(_module, 'IDxcOptimizerPass')
make_head(_module, 'IDxcPdbUtils')
make_head(_module, 'IDxcResult')
make_head(_module, 'IDxcUtils')
make_head(_module, 'IDxcValidator')
make_head(_module, 'IDxcValidator2')
make_head(_module, 'IDxcVersionInfo')
make_head(_module, 'IDxcVersionInfo2')
make_head(_module, 'IDxcVersionInfo3')
__all__ = [
    "CLSID_DxcAssembler",
    "CLSID_DxcCompiler",
    "CLSID_DxcCompilerArgs",
    "CLSID_DxcContainerBuilder",
    "CLSID_DxcContainerReflection",
    "CLSID_DxcDiaDataSource",
    "CLSID_DxcLibrary",
    "CLSID_DxcLinker",
    "CLSID_DxcOptimizer",
    "CLSID_DxcPdbUtils",
    "CLSID_DxcValidator",
    "DXC_ARG_ALL_RESOURCES_BOUND",
    "DXC_ARG_AVOID_FLOW_CONTROL",
    "DXC_ARG_DEBUG",
    "DXC_ARG_DEBUG_NAME_FOR_BINARY",
    "DXC_ARG_DEBUG_NAME_FOR_SOURCE",
    "DXC_ARG_ENABLE_BACKWARDS_COMPATIBILITY",
    "DXC_ARG_ENABLE_STRICTNESS",
    "DXC_ARG_IEEE_STRICTNESS",
    "DXC_ARG_OPTIMIZATION_LEVEL0",
    "DXC_ARG_OPTIMIZATION_LEVEL1",
    "DXC_ARG_OPTIMIZATION_LEVEL2",
    "DXC_ARG_OPTIMIZATION_LEVEL3",
    "DXC_ARG_PACK_MATRIX_COLUMN_MAJOR",
    "DXC_ARG_PACK_MATRIX_ROW_MAJOR",
    "DXC_ARG_PREFER_FLOW_CONTROL",
    "DXC_ARG_RESOURCES_MAY_ALIAS",
    "DXC_ARG_SKIP_OPTIMIZATIONS",
    "DXC_ARG_SKIP_VALIDATION",
    "DXC_ARG_WARNINGS_ARE_ERRORS",
    "DXC_CP",
    "DXC_CP_ACP",
    "DXC_CP_UTF16",
    "DXC_CP_UTF8",
    "DXC_EXTRA_OUTPUT_NAME_STDERR",
    "DXC_EXTRA_OUTPUT_NAME_STDOUT",
    "DXC_HASHFLAG_INCLUDES_SOURCE",
    "DXC_OUT_DISASSEMBLY",
    "DXC_OUT_ERRORS",
    "DXC_OUT_EXTRA_OUTPUTS",
    "DXC_OUT_FORCE_DWORD",
    "DXC_OUT_HLSL",
    "DXC_OUT_KIND",
    "DXC_OUT_NONE",
    "DXC_OUT_OBJECT",
    "DXC_OUT_PDB",
    "DXC_OUT_REFLECTION",
    "DXC_OUT_ROOT_SIGNATURE",
    "DXC_OUT_SHADER_HASH",
    "DXC_OUT_TEXT",
    "DxcArgPair",
    "DxcBuffer",
    "DxcCreateInstance",
    "DxcCreateInstance2",
    "DxcCreateInstance2Proc",
    "DxcCreateInstanceProc",
    "DxcDefine",
    "DxcShaderHash",
    "DxcValidatorFlags_Default",
    "DxcValidatorFlags_InPlaceEdit",
    "DxcValidatorFlags_ModuleOnly",
    "DxcValidatorFlags_RootSignatureOnly",
    "DxcValidatorFlags_ValidMask",
    "DxcVersionInfoFlags_Debug",
    "DxcVersionInfoFlags_Internal",
    "DxcVersionInfoFlags_None",
    "IDxcAssembler",
    "IDxcBlob",
    "IDxcBlobEncoding",
    "IDxcBlobUtf16",
    "IDxcBlobUtf8",
    "IDxcCompiler",
    "IDxcCompiler2",
    "IDxcCompiler3",
    "IDxcCompilerArgs",
    "IDxcContainerBuilder",
    "IDxcContainerReflection",
    "IDxcExtraOutputs",
    "IDxcIncludeHandler",
    "IDxcLibrary",
    "IDxcLinker",
    "IDxcOperationResult",
    "IDxcOptimizer",
    "IDxcOptimizerPass",
    "IDxcPdbUtils",
    "IDxcResult",
    "IDxcUtils",
    "IDxcValidator",
    "IDxcValidator2",
    "IDxcVersionInfo",
    "IDxcVersionInfo2",
    "IDxcVersionInfo3",
]
_arch_optional = [
]