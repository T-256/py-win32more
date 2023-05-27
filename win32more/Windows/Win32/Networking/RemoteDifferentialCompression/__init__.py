from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Networking.RemoteDifferentialCompression
import win32more.Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
RDCE_TABLE_FULL: UInt32 = 2147745793
RDCE_TABLE_CORRUPT: UInt32 = 2147745794
MSRDC_SIGNATURE_HASHSIZE: UInt32 = 16
SimilarityFileIdMinSize: UInt32 = 4
SimilarityFileIdMaxSize: UInt32 = 32
MSRDC_VERSION: UInt32 = 65536
MSRDC_MINIMUM_COMPATIBLE_APP_VERSION: UInt32 = 65536
MSRDC_MINIMUM_DEPTH: UInt32 = 1
MSRDC_MAXIMUM_DEPTH: UInt32 = 8
MSRDC_MINIMUM_COMPAREBUFFER: UInt32 = 100000
MSRDC_MAXIMUM_COMPAREBUFFER: UInt32 = 1073741824
MSRDC_DEFAULT_COMPAREBUFFER: UInt32 = 3200000
MSRDC_MINIMUM_INPUTBUFFERSIZE: UInt32 = 1024
MSRDC_MINIMUM_HORIZONSIZE: UInt32 = 128
MSRDC_MAXIMUM_HORIZONSIZE: UInt32 = 16384
MSRDC_MINIMUM_HASHWINDOWSIZE: UInt32 = 2
MSRDC_MAXIMUM_HASHWINDOWSIZE: UInt32 = 96
MSRDC_DEFAULT_HASHWINDOWSIZE_1: UInt32 = 48
MSRDC_DEFAULT_HORIZONSIZE_1: UInt32 = 1024
MSRDC_DEFAULT_HASHWINDOWSIZE_N: UInt32 = 2
MSRDC_DEFAULT_HORIZONSIZE_N: UInt32 = 128
MSRDC_MAXIMUM_TRAITVALUE: UInt32 = 63
MSRDC_MINIMUM_MATCHESREQUIRED: UInt32 = 1
MSRDC_MAXIMUM_MATCHESREQUIRED: UInt32 = 16
class FindSimilarFileIndexResults(EasyCastStructure):
    m_FileIndex: UInt32
    m_MatchCount: UInt32
FindSimilarResults = Guid('{96236a93-9dbc-11da-9e3f-0011114ae311}')
GeneratorParametersType = Int32
RDCGENTYPE_Unused: GeneratorParametersType = 0
RDCGENTYPE_FilterMax: GeneratorParametersType = 1
class IFindSimilarResults(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a81-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNextFileId(self, numTraitsMatched: POINTER(UInt32), similarityFileId: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityFileId_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcComparator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a77-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def Process(self, endOfInput: win32more.Windows.Win32.Foundation.BOOL, endOfOutput: POINTER(win32more.Windows.Win32.Foundation.BOOL), inputBuffer: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcBufferPointer_head), outputBuffer: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcNeedPointer_head), rdc_ErrorCode: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcFileReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a74-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetFileSize(self, fileSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Read(self, offsetFileStart: UInt64, bytesToRead: UInt32, bytesActuallyRead: POINTER(UInt32), buffer: POINTER(Byte), eof: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFilePosition(self, offsetFromStart: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcFileWriter(ComPtr):
    extends: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcFileReader
    _iid_ = Guid('{96236a75-9dbc-11da-9e3f-0011114ae311}')
    @commethod(6)
    def Write(self, offsetFileStart: UInt64, bytesToWrite: UInt32, buffer: POINTER(Byte)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Truncate(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def DeleteOnClose(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a73-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetGeneratorParameters(self, level: UInt32, iGeneratorParameters: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Process(self, endOfInput: win32more.Windows.Win32.Foundation.BOOL, endOfOutput: POINTER(win32more.Windows.Win32.Foundation.BOOL), inputBuffer: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcBufferPointer_head), depth: UInt32, outputBuffers: POINTER(POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcBufferPointer_head)), rdc_ErrorCode: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcGeneratorFilterMaxParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a72-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetHorizonSize(self, horizonSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetHorizonSize(self, horizonSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHashWindowSize(self, hashWindowSize: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetHashWindowSize(self, hashWindowSize: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcGeneratorParameters(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a71-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetGeneratorParametersType(self, parametersType: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.GeneratorParametersType)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetParametersVersion(self, currentVersion: POINTER(UInt32), minimumCompatibleAppVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSerializeSize(self, size: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Serialize(self, size: UInt32, parametersBlob: POINTER(Byte), bytesWritten: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcLibrary(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a78-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def ComputeDefaultRecursionDepth(self, fileSize: UInt64, depth: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateGeneratorParameters(self, parametersType: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.GeneratorParametersType, level: UInt32, iGeneratorParameters: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenGeneratorParameters(self, size: UInt32, parametersBlob: POINTER(Byte), iGeneratorParameters: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def CreateGenerator(self, depth: UInt32, iGeneratorParametersArray: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcGeneratorParameters_head), iGenerator: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcGenerator_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def CreateComparator(self, iSeedSignaturesFile: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcFileReader_head, comparatorBufferSize: UInt32, iComparator: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcComparator_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CreateSignatureReader(self, iFileReader: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcFileReader_head, iSignatureReader: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcSignatureReader_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRDCVersion(self, currentVersion: POINTER(UInt32), minimumCompatibleAppVersion: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcSignatureReader(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a76-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def ReadHeader(self, rdc_ErrorCode: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RDC_ErrorCode)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReadSignatures(self, rdcSignaturePointer: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcSignaturePointer_head), endOfOutput: POINTER(win32more.Windows.Win32.Foundation.BOOL)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRdcSimilarityGenerator(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a80-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def EnableSimilarity(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Results(self, similarityData: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarity(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a83-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def CreateTable(self, path: win32more.Windows.Win32.Foundation.PWSTR, truncate: win32more.Windows.Win32.Foundation.BOOL, securityDescriptor: POINTER(Byte), recordSize: UInt32, isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(self, mapping: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head, fileIdFile: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcFileWriter_head, truncate: win32more.Windows.Win32.Foundation.BOOL, recordSize: UInt32, isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(self, isValid: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Append(self, similarityFileId: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityFileId_head), similarityData: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindSimilarFileId(self, similarityData: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData_head), numberOfMatchesRequired: UInt16, resultsSize: UInt32, findSimilarResults: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IFindSimilarResults_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def CopyAndSwap(self, newSimilarityTables: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarity_head, reportProgress: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarityReportProgress_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCount(self, recordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarityFileIdTable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7f-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def CreateTable(self, path: win32more.Windows.Win32.Foundation.PWSTR, truncate: win32more.Windows.Win32.Foundation.BOOL, securityDescriptor: POINTER(Byte), recordSize: UInt32, isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(self, fileIdFile: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.IRdcFileWriter_head, truncate: win32more.Windows.Win32.Foundation.BOOL, recordSize: UInt32, isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(self, isValid: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Append(self, similarityFileId: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityFileId_head), similarityFileIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Lookup(self, similarityFileIndex: UInt32, similarityFileId: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityFileId_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Invalidate(self, similarityFileIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetRecordCount(self, recordCount: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarityReportProgress(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7a-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def ReportProgress(self, percentCompleted: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarityTableDumpState(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7b-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def GetNextData(self, resultsSize: UInt32, resultsUsed: POINTER(UInt32), eof: POINTER(win32more.Windows.Win32.Foundation.BOOL), results: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityDumpData_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarityTraitsMappedView(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7c-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def Flush(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Unmap(self) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Get(self, index: UInt64, dirty: win32more.Windows.Win32.Foundation.BOOL, numElements: UInt32, viewInfo: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityMappedViewInfo_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetView(self, mappedPageBegin: POINTER(POINTER(Byte)), mappedPageEnd: POINTER(POINTER(Byte))) -> Void: ...
class ISimilarityTraitsMapping(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7d-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def CloseMapping(self) -> Void: ...
    @commethod(4)
    def SetFileSize(self, fileSize: UInt64) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetFileSize(self, fileSize: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OpenMapping(self, accessMode: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, begin: UInt64, end: UInt64, actualEnd: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResizeMapping(self, accessMode: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, begin: UInt64, end: UInt64, actualEnd: POINTER(UInt64)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetPageSize(self, pageSize: POINTER(UInt32)) -> Void: ...
    @commethod(9)
    def CreateView(self, minimumMappedPages: UInt32, accessMode: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcMappingAccessMode, mappedView: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarityTraitsMappedView_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class ISimilarityTraitsTable(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{96236a7e-9dbc-11da-9e3f-0011114ae311}')
    @commethod(3)
    def CreateTable(self, path: win32more.Windows.Win32.Foundation.PWSTR, truncate: win32more.Windows.Win32.Foundation.BOOL, securityDescriptor: POINTER(Byte), isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateTableIndirect(self, mapping: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarityTraitsMapping_head, truncate: win32more.Windows.Win32.Foundation.BOOL, isNew: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcCreatedTables)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CloseTable(self, isValid: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Append(self, data: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData_head), fileIndex: UInt32) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FindSimilarFileIndex(self, similarityData: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData_head), numberOfMatchesRequired: UInt16, findSimilarFileIndexResults: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.FindSimilarFileIndexResults_head), resultsSize: UInt32, resultsUsed: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginDump(self, similarityTableDumpState: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.ISimilarityTableDumpState_head)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetLastIndex(self, fileIndex: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RDC_ErrorCode = Int32
RDC_NoError: RDC_ErrorCode = 0
RDC_HeaderVersionNewer: RDC_ErrorCode = 1
RDC_HeaderVersionOlder: RDC_ErrorCode = 2
RDC_HeaderMissingOrCorrupt: RDC_ErrorCode = 3
RDC_HeaderWrongType: RDC_ErrorCode = 4
RDC_DataMissingOrCorrupt: RDC_ErrorCode = 5
RDC_DataTooManyRecords: RDC_ErrorCode = 6
RDC_FileChecksumMismatch: RDC_ErrorCode = 7
RDC_ApplicationError: RDC_ErrorCode = 8
RDC_Aborted: RDC_ErrorCode = 9
RDC_Win32Error: RDC_ErrorCode = 10
class RdcBufferPointer(EasyCastStructure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: POINTER(Byte)
RdcComparator = Guid('{96236a8b-9dbc-11da-9e3f-0011114ae311}')
RdcCreatedTables = Int32
RDCTABLE_InvalidOrUnknown: RdcCreatedTables = 0
RDCTABLE_Existing: RdcCreatedTables = 1
RDCTABLE_New: RdcCreatedTables = 2
RdcFileReader = Guid('{96236a89-9dbc-11da-9e3f-0011114ae311}')
RdcGenerator = Guid('{96236a88-9dbc-11da-9e3f-0011114ae311}')
RdcGeneratorFilterMaxParameters = Guid('{96236a87-9dbc-11da-9e3f-0011114ae311}')
RdcGeneratorParameters = Guid('{96236a86-9dbc-11da-9e3f-0011114ae311}')
RdcLibrary = Guid('{96236a85-9dbc-11da-9e3f-0011114ae311}')
RdcMappingAccessMode = Int32
RDCMAPPING_Undefined: RdcMappingAccessMode = 0
RDCMAPPING_ReadOnly: RdcMappingAccessMode = 1
RDCMAPPING_ReadWrite: RdcMappingAccessMode = 2
class RdcNeed(EasyCastStructure):
    m_BlockType: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcNeedType
    m_FileOffset: UInt64
    m_BlockLength: UInt64
class RdcNeedPointer(EasyCastStructure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcNeed_head)
RdcNeedType = Int32
RDCNEED_SOURCE: RdcNeedType = 0
RDCNEED_TARGET: RdcNeedType = 1
RDCNEED_SEED: RdcNeedType = 2
RDCNEED_SEED_MAX: RdcNeedType = 255
class RdcSignature(EasyCastStructure):
    m_Signature: Byte * 16
    m_BlockLength: UInt16
class RdcSignaturePointer(EasyCastStructure):
    m_Size: UInt32
    m_Used: UInt32
    m_Data: POINTER(win32more.Windows.Win32.Networking.RemoteDifferentialCompression.RdcSignature_head)
RdcSignatureReader = Guid('{96236a8a-9dbc-11da-9e3f-0011114ae311}')
RdcSimilarityGenerator = Guid('{96236a92-9dbc-11da-9e3f-0011114ae311}')
Similarity = Guid('{96236a91-9dbc-11da-9e3f-0011114ae311}')
class SimilarityData(EasyCastStructure):
    m_Data: Byte * 16
class SimilarityDumpData(EasyCastStructure):
    m_FileIndex: UInt32
    m_Data: win32more.Windows.Win32.Networking.RemoteDifferentialCompression.SimilarityData
class SimilarityFileId(EasyCastStructure):
    m_FileId: Byte * 32
SimilarityFileIdTable = Guid('{96236a90-9dbc-11da-9e3f-0011114ae311}')
class SimilarityMappedViewInfo(EasyCastStructure):
    m_Data: POINTER(Byte)
    m_Length: UInt32
SimilarityReportProgress = Guid('{96236a8d-9dbc-11da-9e3f-0011114ae311}')
SimilarityTableDumpState = Guid('{96236a8e-9dbc-11da-9e3f-0011114ae311}')
SimilarityTraitsMappedView = Guid('{96236a95-9dbc-11da-9e3f-0011114ae311}')
SimilarityTraitsMapping = Guid('{96236a94-9dbc-11da-9e3f-0011114ae311}')
SimilarityTraitsTable = Guid('{96236a8f-9dbc-11da-9e3f-0011114ae311}')
make_head(_module, 'FindSimilarFileIndexResults')
make_head(_module, 'IFindSimilarResults')
make_head(_module, 'IRdcComparator')
make_head(_module, 'IRdcFileReader')
make_head(_module, 'IRdcFileWriter')
make_head(_module, 'IRdcGenerator')
make_head(_module, 'IRdcGeneratorFilterMaxParameters')
make_head(_module, 'IRdcGeneratorParameters')
make_head(_module, 'IRdcLibrary')
make_head(_module, 'IRdcSignatureReader')
make_head(_module, 'IRdcSimilarityGenerator')
make_head(_module, 'ISimilarity')
make_head(_module, 'ISimilarityFileIdTable')
make_head(_module, 'ISimilarityReportProgress')
make_head(_module, 'ISimilarityTableDumpState')
make_head(_module, 'ISimilarityTraitsMappedView')
make_head(_module, 'ISimilarityTraitsMapping')
make_head(_module, 'ISimilarityTraitsTable')
make_head(_module, 'RdcBufferPointer')
make_head(_module, 'RdcNeed')
make_head(_module, 'RdcNeedPointer')
make_head(_module, 'RdcSignature')
make_head(_module, 'RdcSignaturePointer')
make_head(_module, 'SimilarityData')
make_head(_module, 'SimilarityDumpData')
make_head(_module, 'SimilarityFileId')
make_head(_module, 'SimilarityMappedViewInfo')