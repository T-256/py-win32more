from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.Cabinets
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
INCLUDED_FCI = 1
_A_NAME_IS_UTF = 128
_A_EXEC = 64
statusFile = 0
statusFolder = 1
statusCabinet = 2
INCLUDED_TYPES_FCI_FDI = 1
CB_MAX_DISK = 2147483647
CB_MAX_FILENAME = 256
CB_MAX_CABINET_NAME = 256
CB_MAX_CAB_PATH = 256
CB_MAX_DISK_NAME = 256
tcompMASK_TYPE = 15
tcompTYPE_NONE = 0
tcompTYPE_MSZIP = 1
tcompTYPE_QUANTUM = 2
tcompTYPE_LZX = 3
tcompBAD = 15
tcompMASK_LZX_WINDOW = 7936
tcompLZX_WINDOW_LO = 3840
tcompLZX_WINDOW_HI = 5376
tcompSHIFT_LZX_WINDOW = 8
tcompMASK_QUANTUM_LEVEL = 240
tcompQUANTUM_LEVEL_LO = 16
tcompQUANTUM_LEVEL_HI = 112
tcompSHIFT_QUANTUM_LEVEL = 4
tcompMASK_QUANTUM_MEM = 7936
tcompQUANTUM_MEM_LO = 2560
tcompQUANTUM_MEM_HI = 5376
tcompSHIFT_QUANTUM_MEM = 8
tcompMASK_RESERVED = 57344
INCLUDED_FDI = 1
def _define_FCICreate():
    try:
        return CFUNCTYPE(c_void_p,POINTER(win32more.Storage.Cabinets.ERF_head),win32more.Storage.Cabinets.PFNFCIFILEPLACED,win32more.Storage.Cabinets.PFNFCIALLOC,win32more.Storage.Cabinets.PFNFCIFREE,win32more.Storage.Cabinets.PFNFCIOPEN,win32more.Storage.Cabinets.PFNFCIREAD,win32more.Storage.Cabinets.PFNFCIWRITE,win32more.Storage.Cabinets.PFNFCICLOSE,win32more.Storage.Cabinets.PFNFCISEEK,win32more.Storage.Cabinets.PFNFCIDELETE,win32more.Storage.Cabinets.PFNFCIGETTEMPFILE,POINTER(win32more.Storage.Cabinets.CCAB_head),c_void_p)(('FCICreate', cdll['Cabinet.dll']), ((1, 'perf'),(1, 'pfnfcifp'),(1, 'pfna'),(1, 'pfnf'),(1, 'pfnopen'),(1, 'pfnread'),(1, 'pfnwrite'),(1, 'pfnclose'),(1, 'pfnseek'),(1, 'pfndelete'),(1, 'pfnfcigtf'),(1, 'pccab'),(1, 'pv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FCIAddFile():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.BOOL,win32more.Storage.Cabinets.PFNFCIGETNEXTCABINET,win32more.Storage.Cabinets.PFNFCISTATUS,win32more.Storage.Cabinets.PFNFCIGETOPENINFO,UInt16)(('FCIAddFile', cdll['Cabinet.dll']), ((1, 'hfci'),(1, 'pszSourceFile'),(1, 'pszFileName'),(1, 'fExecute'),(1, 'pfnfcignc'),(1, 'pfnfcis'),(1, 'pfnfcigoi'),(1, 'typeCompress'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FCIFlushCabinet():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.BOOL,win32more.Storage.Cabinets.PFNFCIGETNEXTCABINET,win32more.Storage.Cabinets.PFNFCISTATUS)(('FCIFlushCabinet', cdll['Cabinet.dll']), ((1, 'hfci'),(1, 'fGetNextCab'),(1, 'pfnfcignc'),(1, 'pfnfcis'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FCIFlushFolder():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Storage.Cabinets.PFNFCIGETNEXTCABINET,win32more.Storage.Cabinets.PFNFCISTATUS)(('FCIFlushFolder', cdll['Cabinet.dll']), ((1, 'hfci'),(1, 'pfnfcignc'),(1, 'pfnfcis'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FCIDestroy():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('FCIDestroy', cdll['Cabinet.dll']), ((1, 'hfci'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FDICreate():
    try:
        return CFUNCTYPE(c_void_p,win32more.Storage.Cabinets.PFNALLOC,win32more.Storage.Cabinets.PFNFREE,win32more.Storage.Cabinets.PFNOPEN,win32more.Storage.Cabinets.PFNREAD,win32more.Storage.Cabinets.PFNWRITE,win32more.Storage.Cabinets.PFNCLOSE,win32more.Storage.Cabinets.PFNSEEK,win32more.Storage.Cabinets.FDICREATE_CPU_TYPE,POINTER(win32more.Storage.Cabinets.ERF_head))(('FDICreate', cdll['Cabinet.dll']), ((1, 'pfnalloc'),(1, 'pfnfree'),(1, 'pfnopen'),(1, 'pfnread'),(1, 'pfnwrite'),(1, 'pfnclose'),(1, 'pfnseek'),(1, 'cpuType'),(1, 'perf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FDIIsCabinet():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,IntPtr,POINTER(win32more.Storage.Cabinets.FDICABINETINFO_head))(('FDIIsCabinet', cdll['Cabinet.dll']), ((1, 'hfdi'),(1, 'hf'),(1, 'pfdici'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FDICopy():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PSTR,win32more.Foundation.PSTR,Int32,win32more.Storage.Cabinets.PFNFDINOTIFY,win32more.Storage.Cabinets.PFNFDIDECRYPT,c_void_p)(('FDICopy', cdll['Cabinet.dll']), ((1, 'hfdi'),(1, 'pszCabinet'),(1, 'pszCabPath'),(1, 'flags'),(1, 'pfnfdin'),(1, 'pfnfdid'),(1, 'pvUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FDIDestroy():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('FDIDestroy', cdll['Cabinet.dll']), ((1, 'hfdi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FDITruncateCabinet():
    try:
        return CFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PSTR,UInt16)(('FDITruncateCabinet', cdll['Cabinet.dll']), ((1, 'hfdi'),(1, 'pszCabinetName'),(1, 'iFolderToDelete'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CCAB_head():
    class CCAB(Structure):
        pass
    return CCAB
def _define_CCAB():
    CCAB = win32more.Storage.Cabinets.CCAB_head
    CCAB._fields_ = [
        ('cb', UInt32),
        ('cbFolderThresh', UInt32),
        ('cbReserveCFHeader', UInt32),
        ('cbReserveCFFolder', UInt32),
        ('cbReserveCFData', UInt32),
        ('iCab', Int32),
        ('iDisk', Int32),
        ('fFailOnIncompressible', Int32),
        ('setID', UInt16),
        ('szDisk', win32more.Foundation.CHAR * 256),
        ('szCab', win32more.Foundation.CHAR * 256),
        ('szCabPath', win32more.Foundation.CHAR * 256),
    ]
    return CCAB
def _define_ERF_head():
    class ERF(Structure):
        pass
    return ERF
def _define_ERF():
    ERF = win32more.Storage.Cabinets.ERF_head
    ERF._fields_ = [
        ('erfOper', Int32),
        ('erfType', Int32),
        ('fError', win32more.Foundation.BOOL),
    ]
    return ERF
FCIERROR = Int32
FCIERR_NONE = 0
FCIERR_OPEN_SRC = 1
FCIERR_READ_SRC = 2
FCIERR_ALLOC_FAIL = 3
FCIERR_TEMP_FILE = 4
FCIERR_BAD_COMPR_TYPE = 5
FCIERR_CAB_FILE = 6
FCIERR_USER_ABORT = 7
FCIERR_MCI_FAIL = 8
FCIERR_CAB_FORMAT_LIMIT = 9
def _define_FDICABINETINFO_head():
    class FDICABINETINFO(Structure):
        pass
    return FDICABINETINFO
def _define_FDICABINETINFO():
    FDICABINETINFO = win32more.Storage.Cabinets.FDICABINETINFO_head
    FDICABINETINFO._fields_ = [
        ('cbCabinet', Int32),
        ('cFolders', UInt16),
        ('cFiles', UInt16),
        ('setID', UInt16),
        ('iCabinet', UInt16),
        ('fReserve', win32more.Foundation.BOOL),
        ('hasprev', win32more.Foundation.BOOL),
        ('hasnext', win32more.Foundation.BOOL),
    ]
    return FDICABINETINFO
FDICREATE_CPU_TYPE = Int32
FDICREATE_CPU_TYPE_cpuUNKNOWN = -1
FDICREATE_CPU_TYPE_cpu80286 = 0
FDICREATE_CPU_TYPE_cpu80386 = 1
def _define_FDIDECRYPT_head():
    class FDIDECRYPT(Structure):
        pass
    return FDIDECRYPT
def _define_FDIDECRYPT():
    FDIDECRYPT = win32more.Storage.Cabinets.FDIDECRYPT_head
    class FDIDECRYPT__Anonymous_e__Union(Union):
        pass
    class FDIDECRYPT__Anonymous_e__Union__cabinet_e__Struct(Structure):
        pass
    FDIDECRYPT__Anonymous_e__Union__cabinet_e__Struct._fields_ = [
        ('pHeaderReserve', c_void_p),
        ('cbHeaderReserve', UInt16),
        ('setID', UInt16),
        ('iCabinet', Int32),
    ]
    class FDIDECRYPT__Anonymous_e__Union__folder_e__Struct(Structure):
        pass
    FDIDECRYPT__Anonymous_e__Union__folder_e__Struct._fields_ = [
        ('pFolderReserve', c_void_p),
        ('cbFolderReserve', UInt16),
        ('iFolder', UInt16),
    ]
    class FDIDECRYPT__Anonymous_e__Union__decrypt_e__Struct(Structure):
        pass
    FDIDECRYPT__Anonymous_e__Union__decrypt_e__Struct._fields_ = [
        ('pDataReserve', c_void_p),
        ('cbDataReserve', UInt16),
        ('pbData', c_void_p),
        ('cbData', UInt16),
        ('fSplit', win32more.Foundation.BOOL),
        ('cbPartial', UInt16),
    ]
    FDIDECRYPT__Anonymous_e__Union._fields_ = [
        ('cabinet', FDIDECRYPT__Anonymous_e__Union__cabinet_e__Struct),
        ('folder', FDIDECRYPT__Anonymous_e__Union__folder_e__Struct),
        ('decrypt', FDIDECRYPT__Anonymous_e__Union__decrypt_e__Struct),
    ]
    FDIDECRYPT._anonymous_ = [
        'Anonymous',
    ]
    FDIDECRYPT._fields_ = [
        ('fdidt', win32more.Storage.Cabinets.FDIDECRYPTTYPE),
        ('pvUser', c_void_p),
        ('Anonymous', FDIDECRYPT__Anonymous_e__Union),
    ]
    return FDIDECRYPT
FDIDECRYPTTYPE = Int32
FDIDECRYPTTYPE_fdidtNEW_CABINET = 0
FDIDECRYPTTYPE_fdidtNEW_FOLDER = 1
FDIDECRYPTTYPE_fdidtDECRYPT = 2
FDIERROR = Int32
FDIERROR_NONE = 0
FDIERROR_CABINET_NOT_FOUND = 1
FDIERROR_NOT_A_CABINET = 2
FDIERROR_UNKNOWN_CABINET_VERSION = 3
FDIERROR_CORRUPT_CABINET = 4
FDIERROR_ALLOC_FAIL = 5
FDIERROR_BAD_COMPR_TYPE = 6
FDIERROR_MDI_FAIL = 7
FDIERROR_TARGET_FILE = 8
FDIERROR_RESERVE_MISMATCH = 9
FDIERROR_WRONG_CABINET = 10
FDIERROR_USER_ABORT = 11
FDIERROR_EOF = 12
def _define_FDINOTIFICATION_head():
    class FDINOTIFICATION(Structure):
        pass
    return FDINOTIFICATION
def _define_FDINOTIFICATION():
    FDINOTIFICATION = win32more.Storage.Cabinets.FDINOTIFICATION_head
    FDINOTIFICATION._fields_ = [
        ('cb', Int32),
        ('psz1', win32more.Foundation.PSTR),
        ('psz2', win32more.Foundation.PSTR),
        ('psz3', win32more.Foundation.PSTR),
        ('pv', c_void_p),
        ('hf', IntPtr),
        ('date', UInt16),
        ('time', UInt16),
        ('attribs', UInt16),
        ('setID', UInt16),
        ('iCabinet', UInt16),
        ('iFolder', UInt16),
        ('fdie', win32more.Storage.Cabinets.FDIERROR),
    ]
    return FDINOTIFICATION
FDINOTIFICATIONTYPE = Int32
FDINOTIFICATIONTYPE_fdintCABINET_INFO = 0
FDINOTIFICATIONTYPE_fdintPARTIAL_FILE = 1
FDINOTIFICATIONTYPE_fdintCOPY_FILE = 2
FDINOTIFICATIONTYPE_fdintCLOSE_FILE_INFO = 3
FDINOTIFICATIONTYPE_fdintNEXT_CABINET = 4
FDINOTIFICATIONTYPE_fdintENUMERATE = 5
def _define_FDISPILLFILE_head():
    class FDISPILLFILE(Structure):
        pass
    return FDISPILLFILE
def _define_FDISPILLFILE():
    FDISPILLFILE = win32more.Storage.Cabinets.FDISPILLFILE_head
    FDISPILLFILE._fields_ = [
        ('ach', win32more.Foundation.CHAR * 2),
        ('cbFile', Int32),
    ]
    return FDISPILLFILE
def _define_PFNALLOC():
    return CFUNCTYPE(c_void_p,UInt32)
def _define_PFNCLOSE():
    return CFUNCTYPE(Int32,IntPtr)
def _define_PFNFCIALLOC():
    return CFUNCTYPE(c_void_p,UInt32)
def _define_PFNFCICLOSE():
    return CFUNCTYPE(Int32,IntPtr,POINTER(Int32),c_void_p)
def _define_PFNFCIDELETE():
    return CFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(Int32),c_void_p)
def _define_PFNFCIFILEPLACED():
    return CFUNCTYPE(Int32,POINTER(win32more.Storage.Cabinets.CCAB_head),win32more.Foundation.PSTR,Int32,win32more.Foundation.BOOL,c_void_p)
def _define_PFNFCIFREE():
    return CFUNCTYPE(Void,c_void_p)
def _define_PFNFCIGETNEXTCABINET():
    return CFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.Cabinets.CCAB_head),UInt32,c_void_p)
def _define_PFNFCIGETOPENINFO():
    return CFUNCTYPE(IntPtr,win32more.Foundation.PSTR,POINTER(UInt16),POINTER(UInt16),POINTER(UInt16),POINTER(Int32),c_void_p)
def _define_PFNFCIGETTEMPFILE():
    return CFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,Int32,c_void_p)
def _define_PFNFCIOPEN():
    return CFUNCTYPE(IntPtr,win32more.Foundation.PSTR,Int32,Int32,POINTER(Int32),c_void_p)
def _define_PFNFCIREAD():
    return CFUNCTYPE(UInt32,IntPtr,c_void_p,UInt32,POINTER(Int32),c_void_p)
def _define_PFNFCISEEK():
    return CFUNCTYPE(Int32,IntPtr,Int32,Int32,POINTER(Int32),c_void_p)
def _define_PFNFCISTATUS():
    return CFUNCTYPE(Int32,UInt32,UInt32,UInt32,c_void_p)
def _define_PFNFCIWRITE():
    return CFUNCTYPE(UInt32,IntPtr,c_void_p,UInt32,POINTER(Int32),c_void_p)
def _define_PFNFDIDECRYPT():
    return CFUNCTYPE(Int32,POINTER(win32more.Storage.Cabinets.FDIDECRYPT_head))
def _define_PFNFDINOTIFY():
    return CFUNCTYPE(IntPtr,win32more.Storage.Cabinets.FDINOTIFICATIONTYPE,POINTER(win32more.Storage.Cabinets.FDINOTIFICATION_head))
def _define_PFNFREE():
    return CFUNCTYPE(Void,c_void_p)
def _define_PFNOPEN():
    return CFUNCTYPE(IntPtr,win32more.Foundation.PSTR,Int32,Int32)
def _define_PFNREAD():
    return CFUNCTYPE(UInt32,IntPtr,c_void_p,UInt32)
def _define_PFNSEEK():
    return CFUNCTYPE(Int32,IntPtr,Int32,Int32)
def _define_PFNWRITE():
    return CFUNCTYPE(UInt32,IntPtr,c_void_p,UInt32)
__all__ = [
    "CB_MAX_CABINET_NAME",
    "CB_MAX_CAB_PATH",
    "CB_MAX_DISK",
    "CB_MAX_DISK_NAME",
    "CB_MAX_FILENAME",
    "CCAB",
    "ERF",
    "FCIAddFile",
    "FCICreate",
    "FCIDestroy",
    "FCIERROR",
    "FCIERR_ALLOC_FAIL",
    "FCIERR_BAD_COMPR_TYPE",
    "FCIERR_CAB_FILE",
    "FCIERR_CAB_FORMAT_LIMIT",
    "FCIERR_MCI_FAIL",
    "FCIERR_NONE",
    "FCIERR_OPEN_SRC",
    "FCIERR_READ_SRC",
    "FCIERR_TEMP_FILE",
    "FCIERR_USER_ABORT",
    "FCIFlushCabinet",
    "FCIFlushFolder",
    "FDICABINETINFO",
    "FDICREATE_CPU_TYPE",
    "FDICREATE_CPU_TYPE_cpu80286",
    "FDICREATE_CPU_TYPE_cpu80386",
    "FDICREATE_CPU_TYPE_cpuUNKNOWN",
    "FDICopy",
    "FDICreate",
    "FDIDECRYPT",
    "FDIDECRYPTTYPE",
    "FDIDECRYPTTYPE_fdidtDECRYPT",
    "FDIDECRYPTTYPE_fdidtNEW_CABINET",
    "FDIDECRYPTTYPE_fdidtNEW_FOLDER",
    "FDIDestroy",
    "FDIERROR",
    "FDIERROR_ALLOC_FAIL",
    "FDIERROR_BAD_COMPR_TYPE",
    "FDIERROR_CABINET_NOT_FOUND",
    "FDIERROR_CORRUPT_CABINET",
    "FDIERROR_EOF",
    "FDIERROR_MDI_FAIL",
    "FDIERROR_NONE",
    "FDIERROR_NOT_A_CABINET",
    "FDIERROR_RESERVE_MISMATCH",
    "FDIERROR_TARGET_FILE",
    "FDIERROR_UNKNOWN_CABINET_VERSION",
    "FDIERROR_USER_ABORT",
    "FDIERROR_WRONG_CABINET",
    "FDIIsCabinet",
    "FDINOTIFICATION",
    "FDINOTIFICATIONTYPE",
    "FDINOTIFICATIONTYPE_fdintCABINET_INFO",
    "FDINOTIFICATIONTYPE_fdintCLOSE_FILE_INFO",
    "FDINOTIFICATIONTYPE_fdintCOPY_FILE",
    "FDINOTIFICATIONTYPE_fdintENUMERATE",
    "FDINOTIFICATIONTYPE_fdintNEXT_CABINET",
    "FDINOTIFICATIONTYPE_fdintPARTIAL_FILE",
    "FDISPILLFILE",
    "FDITruncateCabinet",
    "INCLUDED_FCI",
    "INCLUDED_FDI",
    "INCLUDED_TYPES_FCI_FDI",
    "PFNALLOC",
    "PFNCLOSE",
    "PFNFCIALLOC",
    "PFNFCICLOSE",
    "PFNFCIDELETE",
    "PFNFCIFILEPLACED",
    "PFNFCIFREE",
    "PFNFCIGETNEXTCABINET",
    "PFNFCIGETOPENINFO",
    "PFNFCIGETTEMPFILE",
    "PFNFCIOPEN",
    "PFNFCIREAD",
    "PFNFCISEEK",
    "PFNFCISTATUS",
    "PFNFCIWRITE",
    "PFNFDIDECRYPT",
    "PFNFDINOTIFY",
    "PFNFREE",
    "PFNOPEN",
    "PFNREAD",
    "PFNSEEK",
    "PFNWRITE",
    "_A_EXEC",
    "_A_NAME_IS_UTF",
    "statusCabinet",
    "statusFile",
    "statusFolder",
    "tcompBAD",
    "tcompLZX_WINDOW_HI",
    "tcompLZX_WINDOW_LO",
    "tcompMASK_LZX_WINDOW",
    "tcompMASK_QUANTUM_LEVEL",
    "tcompMASK_QUANTUM_MEM",
    "tcompMASK_RESERVED",
    "tcompMASK_TYPE",
    "tcompQUANTUM_LEVEL_HI",
    "tcompQUANTUM_LEVEL_LO",
    "tcompQUANTUM_MEM_HI",
    "tcompQUANTUM_MEM_LO",
    "tcompSHIFT_LZX_WINDOW",
    "tcompSHIFT_QUANTUM_LEVEL",
    "tcompSHIFT_QUANTUM_MEM",
    "tcompTYPE_LZX",
    "tcompTYPE_MSZIP",
    "tcompTYPE_NONE",
    "tcompTYPE_QUANTUM",
]
