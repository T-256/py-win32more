from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.System.DataExchange
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
WM_DDE_FIRST = 992
WM_DDE_INITIATE = 992
WM_DDE_TERMINATE = 993
WM_DDE_ADVISE = 994
WM_DDE_UNADVISE = 995
WM_DDE_ACK = 996
WM_DDE_DATA = 997
WM_DDE_REQUEST = 998
WM_DDE_POKE = 999
WM_DDE_EXECUTE = 1000
WM_DDE_LAST = 1000
CADV_LATEACK = 65535
DDE_FACK = 32768
DDE_FBUSY = 16384
DDE_FDEFERUPD = 16384
DDE_FACKREQ = 32768
DDE_FRELEASE = 8192
DDE_FREQUESTED = 4096
DDE_FAPPSTATUS = 255
DDE_FNOTPROCESSED = 0
MSGF_DDEMGR = 32769
CP_WINANSI = 1004
CP_WINUNICODE = 1200
CP_WINNEUTRAL = 1200
XTYPF_NOBLOCK = 2
XTYPF_NODATA = 4
XTYPF_ACKREQ = 8
XCLASS_MASK = 64512
XCLASS_BOOL = 4096
XCLASS_DATA = 8192
XCLASS_FLAGS = 16384
XCLASS_NOTIFICATION = 32768
XTYP_MASK = 240
XTYP_SHIFT = 4
TIMEOUT_ASYNC = 4294967295
QID_SYNC = 4294967295
SZDDESYS_TOPIC = 'System'
SZDDESYS_ITEM_TOPICS = 'Topics'
SZDDESYS_ITEM_SYSITEMS = 'SysItems'
SZDDESYS_ITEM_RTNMSG = 'ReturnMessage'
SZDDESYS_ITEM_STATUS = 'Status'
SZDDESYS_ITEM_FORMATS = 'Formats'
SZDDESYS_ITEM_HELP = 'Help'
SZDDE_ITEM_ITEMLIST = 'TopicItemList'
APPCMD_MASK = 4080
APPCLASS_MASK = 15
HDATA_APPOWNED = 1
DMLERR_NO_ERROR = 0
DMLERR_FIRST = 16384
DMLERR_ADVACKTIMEOUT = 16384
DMLERR_BUSY = 16385
DMLERR_DATAACKTIMEOUT = 16386
DMLERR_DLL_NOT_INITIALIZED = 16387
DMLERR_DLL_USAGE = 16388
DMLERR_EXECACKTIMEOUT = 16389
DMLERR_INVALIDPARAMETER = 16390
DMLERR_LOW_MEMORY = 16391
DMLERR_MEMORY_ERROR = 16392
DMLERR_NOTPROCESSED = 16393
DMLERR_NO_CONV_ESTABLISHED = 16394
DMLERR_POKEACKTIMEOUT = 16395
DMLERR_POSTMSG_FAILED = 16396
DMLERR_REENTRANCY = 16397
DMLERR_SERVER_DIED = 16398
DMLERR_SYS_ERROR = 16399
DMLERR_UNADVACKTIMEOUT = 16400
DMLERR_UNFOUND_QUEUE_ID = 16401
DMLERR_LAST = 16401
MH_CREATE = 1
MH_KEEP = 2
MH_DELETE = 3
MH_CLEANUP = 4
MAX_MONITORS = 4
MF_MASK = 4278190080
def _define_DdeSetQualityOfService():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,POINTER(win32more.Security.SECURITY_QUALITY_OF_SERVICE_head),POINTER(win32more.Security.SECURITY_QUALITY_OF_SERVICE_head))(('DdeSetQualityOfService', windll['USER32.dll']), ((1, 'hwndClient'),(1, 'pqosNew'),(1, 'pqosPrev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ImpersonateDdeClientWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND)(('ImpersonateDdeClientWindow', windll['USER32.dll']), ((1, 'hWndClient'),(1, 'hWndServer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PackDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.LPARAM,UInt32,UIntPtr,UIntPtr)(('PackDDElParam', windll['USER32.dll']), ((1, 'msg'),(1, 'uiLo'),(1, 'uiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnpackDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.LPARAM,POINTER(UIntPtr),POINTER(UIntPtr))(('UnpackDDElParam', windll['USER32.dll']), ((1, 'msg'),(1, 'lParam'),(1, 'puiLo'),(1, 'puiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.Foundation.LPARAM)(('FreeDDElParam', windll['USER32.dll']), ((1, 'msg'),(1, 'lParam'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReuseDDElParam():
    try:
        return WINFUNCTYPE(win32more.Foundation.LPARAM,win32more.Foundation.LPARAM,UInt32,UInt32,UIntPtr,UIntPtr)(('ReuseDDElParam', windll['USER32.dll']), ((1, 'lParam'),(1, 'msgIn'),(1, 'msgOut'),(1, 'uiLo'),(1, 'uiHi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeInitializeA():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.System.DataExchange.PFNCALLBACK,win32more.System.DataExchange.DDE_INITIALIZE_COMMAND,UInt32)(('DdeInitializeA', windll['USER32.dll']), ((1, 'pidInst'),(1, 'pfnCallback'),(1, 'afCmd'),(1, 'ulRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeInitializeW():
    try:
        return WINFUNCTYPE(UInt32,POINTER(UInt32),win32more.System.DataExchange.PFNCALLBACK,win32more.System.DataExchange.DDE_INITIALIZE_COMMAND,UInt32)(('DdeInitializeW', windll['USER32.dll']), ((1, 'pidInst'),(1, 'pfnCallback'),(1, 'afCmd'),(1, 'ulRes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeUninitialize():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('DdeUninitialize', windll['USER32.dll']), ((1, 'idInst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeConnectList():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONVLIST,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HCONVLIST,POINTER(win32more.System.DataExchange.CONVCONTEXT_head))(('DdeConnectList', windll['USER32.dll']), ((1, 'idInst'),(1, 'hszService'),(1, 'hszTopic'),(1, 'hConvList'),(1, 'pCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryNextServer():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HCONVLIST,win32more.System.DataExchange.HCONV)(('DdeQueryNextServer', windll['USER32.dll']), ((1, 'hConvList'),(1, 'hConvPrev'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeDisconnectList():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONVLIST)(('DdeDisconnectList', windll['USER32.dll']), ((1, 'hConvList'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeConnect():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,POINTER(win32more.System.DataExchange.CONVCONTEXT_head))(('DdeConnect', windll['USER32.dll']), ((1, 'idInst'),(1, 'hszService'),(1, 'hszTopic'),(1, 'pCC'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeDisconnect():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV)(('DdeDisconnect', windll['USER32.dll']), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeReconnect():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HCONV)(('DdeReconnect', windll['USER32.dll']), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryConvInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.DataExchange.HCONV,UInt32,POINTER(win32more.System.DataExchange.CONVINFO_head))(('DdeQueryConvInfo', windll['USER32.dll']), ((1, 'hConv'),(1, 'idTransaction'),(1, 'pConvInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeSetUserHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV,UInt32,UIntPtr)(('DdeSetUserHandle', windll['USER32.dll']), ((1, 'hConv'),(1, 'id'),(1, 'hUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAbandonTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HCONV,UInt32)(('DdeAbandonTransaction', windll['USER32.dll']), ((1, 'idInst'),(1, 'hConv'),(1, 'idTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdePostAdvise():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ)(('DdePostAdvise', windll['USER32.dll']), ((1, 'idInst'),(1, 'hszTopic'),(1, 'hszItem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeEnableCallback():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.DDE_ENABLE_CALLBACK_CMD)(('DdeEnableCallback', windll['USER32.dll']), ((1, 'idInst'),(1, 'hConv'),(1, 'wCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeImpersonateClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HCONV)(('DdeImpersonateClient', windll['USER32.dll']), ((1, 'hConv'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeNameService():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.DDE_NAME_SERVICE_CMD)(('DdeNameService', windll['USER32.dll']), ((1, 'idInst'),(1, 'hsz1'),(1, 'hsz2'),(1, 'afCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeClientTransaction():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HSZ,UInt32,win32more.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE,UInt32,POINTER(UInt32))(('DdeClientTransaction', windll['USER32.dll']), ((1, 'pData'),(1, 'cbData'),(1, 'hConv'),(1, 'hszItem'),(1, 'wFmt'),(1, 'wType'),(1, 'dwTimeout'),(1, 'pdwResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateDataHandle():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,c_char_p_no,UInt32,UInt32,win32more.System.DataExchange.HSZ,UInt32,UInt32)(('DdeCreateDataHandle', windll['USER32.dll']), ((1, 'idInst'),(1, 'pSrc'),(1, 'cb'),(1, 'cbOff'),(1, 'hszItem'),(1, 'wFmt'),(1, 'afCmd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAddData():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,UInt32)(('DdeAddData', windll['USER32.dll']), ((1, 'hData'),(1, 'pSrc'),(1, 'cb'),(1, 'cbOff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeGetData():
    try:
        return WINFUNCTYPE(UInt32,win32more.System.DataExchange.HDDEDATA,c_char_p_no,UInt32,UInt32)(('DdeGetData', windll['USER32.dll']), ((1, 'hData'),(1, 'pDst'),(1, 'cbMax'),(1, 'cbOff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeAccessData():
    try:
        return WINFUNCTYPE(c_char_p_no,win32more.System.DataExchange.HDDEDATA,POINTER(UInt32))(('DdeAccessData', windll['USER32.dll']), ((1, 'hData'),(1, 'pcbDataSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeUnaccessData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HDDEDATA)(('DdeUnaccessData', windll['USER32.dll']), ((1, 'hData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeFreeDataHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.DataExchange.HDDEDATA)(('DdeFreeDataHandle', windll['USER32.dll']), ((1, 'hData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeGetLastError():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('DdeGetLastError', windll['USER32.dll']), ((1, 'idInst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateStringHandleA():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HSZ,UInt32,win32more.Foundation.PSTR,Int32)(('DdeCreateStringHandleA', windll['USER32.dll']), ((1, 'idInst'),(1, 'psz'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCreateStringHandleW():
    try:
        return WINFUNCTYPE(win32more.System.DataExchange.HSZ,UInt32,win32more.Foundation.PWSTR,Int32)(('DdeCreateStringHandleW', windll['USER32.dll']), ((1, 'idInst'),(1, 'psz'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryStringA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.System.DataExchange.HSZ,win32more.Foundation.PSTR,UInt32,Int32)(('DdeQueryStringA', windll['USER32.dll']), ((1, 'idInst'),(1, 'hsz'),(1, 'psz'),(1, 'cchMax'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeQueryStringW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.System.DataExchange.HSZ,win32more.Foundation.PWSTR,UInt32,Int32)(('DdeQueryStringW', windll['USER32.dll']), ((1, 'idInst'),(1, 'hsz'),(1, 'psz'),(1, 'cchMax'),(1, 'iCodePage'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeFreeStringHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ)(('DdeFreeStringHandle', windll['USER32.dll']), ((1, 'idInst'),(1, 'hsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeKeepStringHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,win32more.System.DataExchange.HSZ)(('DdeKeepStringHandle', windll['USER32.dll']), ((1, 'idInst'),(1, 'hsz'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DdeCmpStringHandles():
    try:
        return WINFUNCTYPE(Int32,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ)(('DdeCmpStringHandles', windll['USER32.dll']), ((1, 'hsz1'),(1, 'hsz2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetWinMetaFileBits():
    try:
        return WINFUNCTYPE(win32more.Graphics.Gdi.HENHMETAFILE,UInt32,c_char_p_no,win32more.Graphics.Gdi.HDC,POINTER(win32more.System.DataExchange.METAFILEPICT_head))(('SetWinMetaFileBits', windll['GDI32.dll']), ((1, 'nSize'),(1, 'lpMeta16Data'),(1, 'hdcRef'),(1, 'lpMFP'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('OpenClipboard', windll['USER32.dll']), ((1, 'hWndNewOwner'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('CloseClipboard', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardSequenceNumber():
    try:
        return WINFUNCTYPE(UInt32,)(('GetClipboardSequenceNumber', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardOwner():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,)(('GetClipboardOwner', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetClipboardViewer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,win32more.Foundation.HWND)(('SetClipboardViewer', windll['USER32.dll']), ((1, 'hWndNewViewer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardViewer():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,)(('GetClipboardViewer', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ChangeClipboardChain():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.HWND)(('ChangeClipboardChain', windll['USER32.dll']), ((1, 'hWndRemove'),(1, 'hWndNewNext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetClipboardData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE)(('SetClipboardData', windll['USER32.dll']), ((1, 'uFormat'),(1, 'hMem'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardData():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32)(('GetClipboardData', windll['USER32.dll']), ((1, 'uFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterClipboardFormatA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR)(('RegisterClipboardFormatA', windll['USER32.dll']), ((1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterClipboardFormatW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR)(('RegisterClipboardFormatW', windll['USER32.dll']), ((1, 'lpszFormat'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CountClipboardFormats():
    try:
        return WINFUNCTYPE(Int32,)(('CountClipboardFormats', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EnumClipboardFormats():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('EnumClipboardFormats', windll['USER32.dll']), ((1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardFormatNameA():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PSTR,Int32)(('GetClipboardFormatNameA', windll['USER32.dll']), ((1, 'format'),(1, 'lpszFormatName'),(1, 'cchMaxCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetClipboardFormatNameW():
    try:
        return WINFUNCTYPE(Int32,UInt32,win32more.Foundation.PWSTR,Int32)(('GetClipboardFormatNameW', windll['USER32.dll']), ((1, 'format'),(1, 'lpszFormatName'),(1, 'cchMaxCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EmptyClipboard():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('EmptyClipboard', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsClipboardFormatAvailable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('IsClipboardFormatAvailable', windll['USER32.dll']), ((1, 'format'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetPriorityClipboardFormat():
    try:
        return WINFUNCTYPE(Int32,POINTER(UInt32),Int32)(('GetPriorityClipboardFormat', windll['USER32.dll']), ((1, 'paFormatPriorityList'),(1, 'cFormats'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetOpenClipboardWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.HWND,)(('GetOpenClipboardWindow', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddClipboardFormatListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('AddClipboardFormatListener', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveClipboardFormatListener():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('RemoveClipboardFormatListener', windll['USER32.dll']), ((1, 'hwnd'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetUpdatedClipboardFormats():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(UInt32),UInt32,POINTER(UInt32))(('GetUpdatedClipboardFormats', windll['USER32.dll']), ((1, 'lpuiFormats'),(1, 'cFormats'),(1, 'pcFormatsOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalDeleteAtom():
    try:
        return WINFUNCTYPE(UInt16,UInt16)(('GlobalDeleteAtom', windll['KERNEL32.dll']), ((1, 'nAtom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitAtomTable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('InitAtomTable', windll['KERNEL32.dll']), ((1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteAtom():
    try:
        return WINFUNCTYPE(UInt16,UInt16)(('DeleteAtom', windll['KERNEL32.dll']), ((1, 'nAtom'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR)(('GlobalAddAtomA', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR)(('GlobalAddAtomW', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomExA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR,UInt32)(('GlobalAddAtomExA', windll['KERNEL32.dll']), ((1, 'lpString'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalAddAtomExW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR,UInt32)(('GlobalAddAtomExW', windll['KERNEL32.dll']), ((1, 'lpString'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFindAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR)(('GlobalFindAtomA', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalFindAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR)(('GlobalFindAtomW', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalGetAtomNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt16,win32more.Foundation.PSTR,Int32)(('GlobalGetAtomNameA', windll['KERNEL32.dll']), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GlobalGetAtomNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt16,win32more.Foundation.PWSTR,Int32)(('GlobalGetAtomNameW', windll['KERNEL32.dll']), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR)(('AddAtomA', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR)(('AddAtomW', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindAtomA():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PSTR)(('FindAtomA', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindAtomW():
    try:
        return WINFUNCTYPE(UInt16,win32more.Foundation.PWSTR)(('FindAtomW', windll['KERNEL32.dll']), ((1, 'lpString'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAtomNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt16,win32more.Foundation.PSTR,Int32)(('GetAtomNameA', windll['KERNEL32.dll']), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetAtomNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt16,win32more.Foundation.PWSTR,Int32)(('GetAtomNameW', windll['KERNEL32.dll']), ((1, 'nAtom'),(1, 'lpBuffer'),(1, 'nSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CONVCONTEXT_head():
    class CONVCONTEXT(Structure):
        pass
    return CONVCONTEXT
def _define_CONVCONTEXT():
    CONVCONTEXT = win32more.System.DataExchange.CONVCONTEXT_head
    CONVCONTEXT._fields_ = [
        ('cb', UInt32),
        ('wFlags', UInt32),
        ('wCountryID', UInt32),
        ('iCodePage', Int32),
        ('dwLangID', UInt32),
        ('dwSecurity', UInt32),
        ('qos', win32more.Security.SECURITY_QUALITY_OF_SERVICE),
    ]
    return CONVCONTEXT
def _define_CONVINFO_head():
    class CONVINFO(Structure):
        pass
    return CONVINFO
def _define_CONVINFO():
    CONVINFO = win32more.System.DataExchange.CONVINFO_head
    CONVINFO._fields_ = [
        ('cb', UInt32),
        ('hUser', UIntPtr),
        ('hConvPartner', win32more.System.DataExchange.HCONV),
        ('hszSvcPartner', win32more.System.DataExchange.HSZ),
        ('hszServiceReq', win32more.System.DataExchange.HSZ),
        ('hszTopic', win32more.System.DataExchange.HSZ),
        ('hszItem', win32more.System.DataExchange.HSZ),
        ('wFmt', UInt32),
        ('wType', win32more.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE),
        ('wStatus', win32more.System.DataExchange.CONVINFO_STATUS),
        ('wConvst', win32more.System.DataExchange.CONVINFO_CONVERSATION_STATE),
        ('wLastError', UInt32),
        ('hConvList', win32more.System.DataExchange.HCONVLIST),
        ('ConvCtxt', win32more.System.DataExchange.CONVCONTEXT),
        ('hwnd', win32more.Foundation.HWND),
        ('hwndPartner', win32more.Foundation.HWND),
    ]
    return CONVINFO
CONVINFO_CONVERSATION_STATE = UInt32
XST_ADVACKRCVD = 13
XST_ADVDATAACKRCVD = 16
XST_ADVDATASENT = 15
XST_ADVSENT = 11
XST_CONNECTED = 2
XST_DATARCVD = 6
XST_EXECACKRCVD = 10
XST_EXECSENT = 9
XST_INCOMPLETE = 1
XST_INIT1 = 3
XST_INIT2 = 4
XST_NULL = 0
XST_POKEACKRCVD = 8
XST_POKESENT = 7
XST_REQSENT = 5
XST_UNADVACKRCVD = 14
XST_UNADVSENT = 12
CONVINFO_STATUS = UInt32
ST_ADVISE = 2
ST_BLOCKED = 8
ST_BLOCKNEXT = 128
ST_CLIENT = 16
ST_CONNECTED = 1
ST_INLIST = 64
ST_ISLOCAL = 4
ST_ISSELF = 256
ST_TERMINATED = 32
def _define_COPYDATASTRUCT_head():
    class COPYDATASTRUCT(Structure):
        pass
    return COPYDATASTRUCT
def _define_COPYDATASTRUCT():
    COPYDATASTRUCT = win32more.System.DataExchange.COPYDATASTRUCT_head
    COPYDATASTRUCT._fields_ = [
        ('dwData', UIntPtr),
        ('cbData', UInt32),
        ('lpData', c_void_p),
    ]
    return COPYDATASTRUCT
DDE_CLIENT_TRANSACTION_TYPE = UInt32
XTYP_ADVSTART = 4144
XTYP_ADVSTOP = 32832
XTYP_EXECUTE = 16464
XTYP_POKE = 16528
XTYP_REQUEST = 8368
XTYP_ADVDATA = 16400
XTYP_ADVREQ = 8226
XTYP_CONNECT = 4194
XTYP_CONNECT_CONFIRM = 32882
XTYP_DISCONNECT = 32962
XTYP_MONITOR = 33010
XTYP_REGISTER = 32930
XTYP_UNREGISTER = 32978
XTYP_WILDCONNECT = 8418
XTYP_XACT_COMPLETE = 32896
DDE_ENABLE_CALLBACK_CMD = UInt32
EC_ENABLEALL = 0
EC_ENABLEONE = 128
EC_DISABLE = 8
EC_QUERYWAITING = 2
DDE_INITIALIZE_COMMAND = UInt32
APPCLASS_MONITOR = 1
APPCLASS_STANDARD = 0
APPCMD_CLIENTONLY = 16
APPCMD_FILTERINITS = 32
CBF_FAIL_ALLSVRXACTIONS = 258048
CBF_FAIL_ADVISES = 16384
CBF_FAIL_CONNECTIONS = 8192
CBF_FAIL_EXECUTES = 32768
CBF_FAIL_POKES = 65536
CBF_FAIL_REQUESTS = 131072
CBF_FAIL_SELFCONNECTIONS = 4096
CBF_SKIP_ALLNOTIFICATIONS = 3932160
CBF_SKIP_CONNECT_CONFIRMS = 262144
CBF_SKIP_DISCONNECTS = 2097152
CBF_SKIP_REGISTRATIONS = 524288
CBF_SKIP_UNREGISTRATIONS = 1048576
MF_CALLBACKS = 134217728
MF_CONV = 1073741824
MF_ERRORS = 268435456
MF_HSZ_INFO = 16777216
MF_LINKS = 536870912
MF_POSTMSGS = 67108864
MF_SENDMSGS = 33554432
DDE_NAME_SERVICE_CMD = UInt32
DNS_REGISTER = 1
DNS_UNREGISTER = 2
DNS_FILTERON = 4
DNS_FILTEROFF = 8
def _define_DDEACK_head():
    class DDEACK(Structure):
        pass
    return DDEACK
def _define_DDEACK():
    DDEACK = win32more.System.DataExchange.DDEACK_head
    DDEACK._fields_ = [
        ('_bitfield', UInt16),
    ]
    return DDEACK
def _define_DDEADVISE_head():
    class DDEADVISE(Structure):
        pass
    return DDEADVISE
def _define_DDEADVISE():
    DDEADVISE = win32more.System.DataExchange.DDEADVISE_head
    DDEADVISE._fields_ = [
        ('_bitfield', UInt16),
        ('cfFormat', Int16),
    ]
    return DDEADVISE
def _define_DDEDATA_head():
    class DDEDATA(Structure):
        pass
    return DDEDATA
def _define_DDEDATA():
    DDEDATA = win32more.System.DataExchange.DDEDATA_head
    DDEDATA._fields_ = [
        ('_bitfield', UInt16),
        ('cfFormat', Int16),
        ('Value', Byte * 1),
    ]
    return DDEDATA
def _define_DDELN_head():
    class DDELN(Structure):
        pass
    return DDELN
def _define_DDELN():
    DDELN = win32more.System.DataExchange.DDELN_head
    DDELN._fields_ = [
        ('_bitfield', UInt16),
        ('cfFormat', Int16),
    ]
    return DDELN
def _define_DDEML_MSG_HOOK_DATA_head():
    class DDEML_MSG_HOOK_DATA(Structure):
        pass
    return DDEML_MSG_HOOK_DATA
def _define_DDEML_MSG_HOOK_DATA():
    DDEML_MSG_HOOK_DATA = win32more.System.DataExchange.DDEML_MSG_HOOK_DATA_head
    DDEML_MSG_HOOK_DATA._fields_ = [
        ('uiLo', UIntPtr),
        ('uiHi', UIntPtr),
        ('cbData', UInt32),
        ('Data', UInt32 * 8),
    ]
    return DDEML_MSG_HOOK_DATA
def _define_DDEPOKE_head():
    class DDEPOKE(Structure):
        pass
    return DDEPOKE
def _define_DDEPOKE():
    DDEPOKE = win32more.System.DataExchange.DDEPOKE_head
    DDEPOKE._fields_ = [
        ('_bitfield', UInt16),
        ('cfFormat', Int16),
        ('Value', Byte * 1),
    ]
    return DDEPOKE
def _define_DDEUP_head():
    class DDEUP(Structure):
        pass
    return DDEUP
def _define_DDEUP():
    DDEUP = win32more.System.DataExchange.DDEUP_head
    DDEUP._fields_ = [
        ('_bitfield', UInt16),
        ('cfFormat', Int16),
        ('rgb', Byte * 1),
    ]
    return DDEUP
HCONV = IntPtr
HCONVLIST = IntPtr
HDDEDATA = IntPtr
HSZ = IntPtr
def _define_HSZPAIR_head():
    class HSZPAIR(Structure):
        pass
    return HSZPAIR
def _define_HSZPAIR():
    HSZPAIR = win32more.System.DataExchange.HSZPAIR_head
    HSZPAIR._fields_ = [
        ('hszSvc', win32more.System.DataExchange.HSZ),
        ('hszTopic', win32more.System.DataExchange.HSZ),
    ]
    return HSZPAIR
def _define_METAFILEPICT_head():
    class METAFILEPICT(Structure):
        pass
    return METAFILEPICT
def _define_METAFILEPICT():
    METAFILEPICT = win32more.System.DataExchange.METAFILEPICT_head
    METAFILEPICT._fields_ = [
        ('mm', Int32),
        ('xExt', Int32),
        ('yExt', Int32),
        ('hMF', win32more.Graphics.Gdi.HMETAFILE),
    ]
    return METAFILEPICT
def _define_MONCBSTRUCT_head():
    class MONCBSTRUCT(Structure):
        pass
    return MONCBSTRUCT
def _define_MONCBSTRUCT():
    MONCBSTRUCT = win32more.System.DataExchange.MONCBSTRUCT_head
    MONCBSTRUCT._fields_ = [
        ('cb', UInt32),
        ('dwTime', UInt32),
        ('hTask', win32more.Foundation.HANDLE),
        ('dwRet', UInt32),
        ('wType', UInt32),
        ('wFmt', UInt32),
        ('hConv', win32more.System.DataExchange.HCONV),
        ('hsz1', win32more.System.DataExchange.HSZ),
        ('hsz2', win32more.System.DataExchange.HSZ),
        ('hData', win32more.System.DataExchange.HDDEDATA),
        ('dwData1', UIntPtr),
        ('dwData2', UIntPtr),
        ('cc', win32more.System.DataExchange.CONVCONTEXT),
        ('cbData', UInt32),
        ('Data', UInt32 * 8),
    ]
    return MONCBSTRUCT
def _define_MONCONVSTRUCT_head():
    class MONCONVSTRUCT(Structure):
        pass
    return MONCONVSTRUCT
def _define_MONCONVSTRUCT():
    MONCONVSTRUCT = win32more.System.DataExchange.MONCONVSTRUCT_head
    MONCONVSTRUCT._fields_ = [
        ('cb', UInt32),
        ('fConnect', win32more.Foundation.BOOL),
        ('dwTime', UInt32),
        ('hTask', win32more.Foundation.HANDLE),
        ('hszSvc', win32more.System.DataExchange.HSZ),
        ('hszTopic', win32more.System.DataExchange.HSZ),
        ('hConvClient', win32more.System.DataExchange.HCONV),
        ('hConvServer', win32more.System.DataExchange.HCONV),
    ]
    return MONCONVSTRUCT
def _define_MONERRSTRUCT_head():
    class MONERRSTRUCT(Structure):
        pass
    return MONERRSTRUCT
def _define_MONERRSTRUCT():
    MONERRSTRUCT = win32more.System.DataExchange.MONERRSTRUCT_head
    MONERRSTRUCT._fields_ = [
        ('cb', UInt32),
        ('wLastError', UInt32),
        ('dwTime', UInt32),
        ('hTask', win32more.Foundation.HANDLE),
    ]
    return MONERRSTRUCT
def _define_MONHSZSTRUCTA_head():
    class MONHSZSTRUCTA(Structure):
        pass
    return MONHSZSTRUCTA
def _define_MONHSZSTRUCTA():
    MONHSZSTRUCTA = win32more.System.DataExchange.MONHSZSTRUCTA_head
    MONHSZSTRUCTA._fields_ = [
        ('cb', UInt32),
        ('fsAction', win32more.Foundation.BOOL),
        ('dwTime', UInt32),
        ('hsz', win32more.System.DataExchange.HSZ),
        ('hTask', win32more.Foundation.HANDLE),
        ('str', win32more.Foundation.CHAR * 1),
    ]
    return MONHSZSTRUCTA
def _define_MONHSZSTRUCTW_head():
    class MONHSZSTRUCTW(Structure):
        pass
    return MONHSZSTRUCTW
def _define_MONHSZSTRUCTW():
    MONHSZSTRUCTW = win32more.System.DataExchange.MONHSZSTRUCTW_head
    MONHSZSTRUCTW._fields_ = [
        ('cb', UInt32),
        ('fsAction', win32more.Foundation.BOOL),
        ('dwTime', UInt32),
        ('hsz', win32more.System.DataExchange.HSZ),
        ('hTask', win32more.Foundation.HANDLE),
        ('str', Char * 1),
    ]
    return MONHSZSTRUCTW
def _define_MONLINKSTRUCT_head():
    class MONLINKSTRUCT(Structure):
        pass
    return MONLINKSTRUCT
def _define_MONLINKSTRUCT():
    MONLINKSTRUCT = win32more.System.DataExchange.MONLINKSTRUCT_head
    MONLINKSTRUCT._fields_ = [
        ('cb', UInt32),
        ('dwTime', UInt32),
        ('hTask', win32more.Foundation.HANDLE),
        ('fEstablished', win32more.Foundation.BOOL),
        ('fNoData', win32more.Foundation.BOOL),
        ('hszSvc', win32more.System.DataExchange.HSZ),
        ('hszTopic', win32more.System.DataExchange.HSZ),
        ('hszItem', win32more.System.DataExchange.HSZ),
        ('wFmt', UInt32),
        ('fServer', win32more.Foundation.BOOL),
        ('hConvServer', win32more.System.DataExchange.HCONV),
        ('hConvClient', win32more.System.DataExchange.HCONV),
    ]
    return MONLINKSTRUCT
def _define_MONMSGSTRUCT_head():
    class MONMSGSTRUCT(Structure):
        pass
    return MONMSGSTRUCT
def _define_MONMSGSTRUCT():
    MONMSGSTRUCT = win32more.System.DataExchange.MONMSGSTRUCT_head
    MONMSGSTRUCT._fields_ = [
        ('cb', UInt32),
        ('hwndTo', win32more.Foundation.HWND),
        ('dwTime', UInt32),
        ('hTask', win32more.Foundation.HANDLE),
        ('wMsg', UInt32),
        ('wParam', win32more.Foundation.WPARAM),
        ('lParam', win32more.Foundation.LPARAM),
        ('dmhd', win32more.System.DataExchange.DDEML_MSG_HOOK_DATA),
    ]
    return MONMSGSTRUCT
def _define_PFNCALLBACK():
    return WINFUNCTYPE(win32more.System.DataExchange.HDDEDATA,UInt32,UInt32,win32more.System.DataExchange.HCONV,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HSZ,win32more.System.DataExchange.HDDEDATA,UIntPtr,UIntPtr)
__all__ = [
    "APPCLASS_MASK",
    "APPCLASS_MONITOR",
    "APPCLASS_STANDARD",
    "APPCMD_CLIENTONLY",
    "APPCMD_FILTERINITS",
    "APPCMD_MASK",
    "AddAtomA",
    "AddAtomW",
    "AddClipboardFormatListener",
    "CADV_LATEACK",
    "CBF_FAIL_ADVISES",
    "CBF_FAIL_ALLSVRXACTIONS",
    "CBF_FAIL_CONNECTIONS",
    "CBF_FAIL_EXECUTES",
    "CBF_FAIL_POKES",
    "CBF_FAIL_REQUESTS",
    "CBF_FAIL_SELFCONNECTIONS",
    "CBF_SKIP_ALLNOTIFICATIONS",
    "CBF_SKIP_CONNECT_CONFIRMS",
    "CBF_SKIP_DISCONNECTS",
    "CBF_SKIP_REGISTRATIONS",
    "CBF_SKIP_UNREGISTRATIONS",
    "CONVCONTEXT",
    "CONVINFO",
    "CONVINFO_CONVERSATION_STATE",
    "CONVINFO_STATUS",
    "COPYDATASTRUCT",
    "CP_WINANSI",
    "CP_WINNEUTRAL",
    "CP_WINUNICODE",
    "ChangeClipboardChain",
    "CloseClipboard",
    "CountClipboardFormats",
    "DDEACK",
    "DDEADVISE",
    "DDEDATA",
    "DDELN",
    "DDEML_MSG_HOOK_DATA",
    "DDEPOKE",
    "DDEUP",
    "DDE_CLIENT_TRANSACTION_TYPE",
    "DDE_ENABLE_CALLBACK_CMD",
    "DDE_FACK",
    "DDE_FACKREQ",
    "DDE_FAPPSTATUS",
    "DDE_FBUSY",
    "DDE_FDEFERUPD",
    "DDE_FNOTPROCESSED",
    "DDE_FRELEASE",
    "DDE_FREQUESTED",
    "DDE_INITIALIZE_COMMAND",
    "DDE_NAME_SERVICE_CMD",
    "DMLERR_ADVACKTIMEOUT",
    "DMLERR_BUSY",
    "DMLERR_DATAACKTIMEOUT",
    "DMLERR_DLL_NOT_INITIALIZED",
    "DMLERR_DLL_USAGE",
    "DMLERR_EXECACKTIMEOUT",
    "DMLERR_FIRST",
    "DMLERR_INVALIDPARAMETER",
    "DMLERR_LAST",
    "DMLERR_LOW_MEMORY",
    "DMLERR_MEMORY_ERROR",
    "DMLERR_NOTPROCESSED",
    "DMLERR_NO_CONV_ESTABLISHED",
    "DMLERR_NO_ERROR",
    "DMLERR_POKEACKTIMEOUT",
    "DMLERR_POSTMSG_FAILED",
    "DMLERR_REENTRANCY",
    "DMLERR_SERVER_DIED",
    "DMLERR_SYS_ERROR",
    "DMLERR_UNADVACKTIMEOUT",
    "DMLERR_UNFOUND_QUEUE_ID",
    "DNS_FILTEROFF",
    "DNS_FILTERON",
    "DNS_REGISTER",
    "DNS_UNREGISTER",
    "DdeAbandonTransaction",
    "DdeAccessData",
    "DdeAddData",
    "DdeClientTransaction",
    "DdeCmpStringHandles",
    "DdeConnect",
    "DdeConnectList",
    "DdeCreateDataHandle",
    "DdeCreateStringHandleA",
    "DdeCreateStringHandleW",
    "DdeDisconnect",
    "DdeDisconnectList",
    "DdeEnableCallback",
    "DdeFreeDataHandle",
    "DdeFreeStringHandle",
    "DdeGetData",
    "DdeGetLastError",
    "DdeImpersonateClient",
    "DdeInitializeA",
    "DdeInitializeW",
    "DdeKeepStringHandle",
    "DdeNameService",
    "DdePostAdvise",
    "DdeQueryConvInfo",
    "DdeQueryNextServer",
    "DdeQueryStringA",
    "DdeQueryStringW",
    "DdeReconnect",
    "DdeSetQualityOfService",
    "DdeSetUserHandle",
    "DdeUnaccessData",
    "DdeUninitialize",
    "DeleteAtom",
    "EC_DISABLE",
    "EC_ENABLEALL",
    "EC_ENABLEONE",
    "EC_QUERYWAITING",
    "EmptyClipboard",
    "EnumClipboardFormats",
    "FindAtomA",
    "FindAtomW",
    "FreeDDElParam",
    "GetAtomNameA",
    "GetAtomNameW",
    "GetClipboardData",
    "GetClipboardFormatNameA",
    "GetClipboardFormatNameW",
    "GetClipboardOwner",
    "GetClipboardSequenceNumber",
    "GetClipboardViewer",
    "GetOpenClipboardWindow",
    "GetPriorityClipboardFormat",
    "GetUpdatedClipboardFormats",
    "GlobalAddAtomA",
    "GlobalAddAtomExA",
    "GlobalAddAtomExW",
    "GlobalAddAtomW",
    "GlobalDeleteAtom",
    "GlobalFindAtomA",
    "GlobalFindAtomW",
    "GlobalGetAtomNameA",
    "GlobalGetAtomNameW",
    "HCONV",
    "HCONVLIST",
    "HDATA_APPOWNED",
    "HDDEDATA",
    "HSZ",
    "HSZPAIR",
    "ImpersonateDdeClientWindow",
    "InitAtomTable",
    "IsClipboardFormatAvailable",
    "MAX_MONITORS",
    "METAFILEPICT",
    "MF_CALLBACKS",
    "MF_CONV",
    "MF_ERRORS",
    "MF_HSZ_INFO",
    "MF_LINKS",
    "MF_MASK",
    "MF_POSTMSGS",
    "MF_SENDMSGS",
    "MH_CLEANUP",
    "MH_CREATE",
    "MH_DELETE",
    "MH_KEEP",
    "MONCBSTRUCT",
    "MONCONVSTRUCT",
    "MONERRSTRUCT",
    "MONHSZSTRUCTA",
    "MONHSZSTRUCTW",
    "MONLINKSTRUCT",
    "MONMSGSTRUCT",
    "MSGF_DDEMGR",
    "OpenClipboard",
    "PFNCALLBACK",
    "PackDDElParam",
    "QID_SYNC",
    "RegisterClipboardFormatA",
    "RegisterClipboardFormatW",
    "RemoveClipboardFormatListener",
    "ReuseDDElParam",
    "ST_ADVISE",
    "ST_BLOCKED",
    "ST_BLOCKNEXT",
    "ST_CLIENT",
    "ST_CONNECTED",
    "ST_INLIST",
    "ST_ISLOCAL",
    "ST_ISSELF",
    "ST_TERMINATED",
    "SZDDESYS_ITEM_FORMATS",
    "SZDDESYS_ITEM_HELP",
    "SZDDESYS_ITEM_RTNMSG",
    "SZDDESYS_ITEM_STATUS",
    "SZDDESYS_ITEM_SYSITEMS",
    "SZDDESYS_ITEM_TOPICS",
    "SZDDESYS_TOPIC",
    "SZDDE_ITEM_ITEMLIST",
    "SetClipboardData",
    "SetClipboardViewer",
    "SetWinMetaFileBits",
    "TIMEOUT_ASYNC",
    "UnpackDDElParam",
    "WM_DDE_ACK",
    "WM_DDE_ADVISE",
    "WM_DDE_DATA",
    "WM_DDE_EXECUTE",
    "WM_DDE_FIRST",
    "WM_DDE_INITIATE",
    "WM_DDE_LAST",
    "WM_DDE_POKE",
    "WM_DDE_REQUEST",
    "WM_DDE_TERMINATE",
    "WM_DDE_UNADVISE",
    "XCLASS_BOOL",
    "XCLASS_DATA",
    "XCLASS_FLAGS",
    "XCLASS_MASK",
    "XCLASS_NOTIFICATION",
    "XST_ADVACKRCVD",
    "XST_ADVDATAACKRCVD",
    "XST_ADVDATASENT",
    "XST_ADVSENT",
    "XST_CONNECTED",
    "XST_DATARCVD",
    "XST_EXECACKRCVD",
    "XST_EXECSENT",
    "XST_INCOMPLETE",
    "XST_INIT1",
    "XST_INIT2",
    "XST_NULL",
    "XST_POKEACKRCVD",
    "XST_POKESENT",
    "XST_REQSENT",
    "XST_UNADVACKRCVD",
    "XST_UNADVSENT",
    "XTYPF_ACKREQ",
    "XTYPF_NOBLOCK",
    "XTYPF_NODATA",
    "XTYP_ADVDATA",
    "XTYP_ADVREQ",
    "XTYP_ADVSTART",
    "XTYP_ADVSTOP",
    "XTYP_CONNECT",
    "XTYP_CONNECT_CONFIRM",
    "XTYP_DISCONNECT",
    "XTYP_EXECUTE",
    "XTYP_MASK",
    "XTYP_MONITOR",
    "XTYP_POKE",
    "XTYP_REGISTER",
    "XTYP_REQUEST",
    "XTYP_SHIFT",
    "XTYP_UNREGISTER",
    "XTYP_WILDCONNECT",
    "XTYP_XACT_COMPLETE",
]
