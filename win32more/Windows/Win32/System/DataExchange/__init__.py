from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.Graphics.Gdi
import win32more.Windows.Win32.Security
import win32more.Windows.Win32.System.DataExchange
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WM_DDE_FIRST: UInt32 = 992
WM_DDE_INITIATE: UInt32 = 992
WM_DDE_TERMINATE: UInt32 = 993
WM_DDE_ADVISE: UInt32 = 994
WM_DDE_UNADVISE: UInt32 = 995
WM_DDE_ACK: UInt32 = 996
WM_DDE_DATA: UInt32 = 997
WM_DDE_REQUEST: UInt32 = 998
WM_DDE_POKE: UInt32 = 999
WM_DDE_EXECUTE: UInt32 = 1000
WM_DDE_LAST: UInt32 = 1000
CADV_LATEACK: UInt32 = 65535
DDE_FACK: UInt32 = 32768
DDE_FBUSY: UInt32 = 16384
DDE_FDEFERUPD: UInt32 = 16384
DDE_FACKREQ: UInt32 = 32768
DDE_FRELEASE: UInt32 = 8192
DDE_FREQUESTED: UInt32 = 4096
DDE_FAPPSTATUS: UInt32 = 255
DDE_FNOTPROCESSED: UInt32 = 0
MSGF_DDEMGR: UInt32 = 32769
CP_WINANSI: Int32 = 1004
CP_WINUNICODE: Int32 = 1200
CP_WINNEUTRAL: Int32 = 1200
XTYPF_NOBLOCK: UInt32 = 2
XTYPF_NODATA: UInt32 = 4
XTYPF_ACKREQ: UInt32 = 8
XCLASS_MASK: UInt32 = 64512
XCLASS_BOOL: UInt32 = 4096
XCLASS_DATA: UInt32 = 8192
XCLASS_FLAGS: UInt32 = 16384
XCLASS_NOTIFICATION: UInt32 = 32768
XTYP_MASK: UInt32 = 240
XTYP_SHIFT: UInt32 = 4
TIMEOUT_ASYNC: UInt32 = 4294967295
QID_SYNC: UInt32 = 4294967295
SZDDESYS_TOPIC: String = 'System'
SZDDESYS_ITEM_TOPICS: String = 'Topics'
SZDDESYS_ITEM_SYSITEMS: String = 'SysItems'
SZDDESYS_ITEM_RTNMSG: String = 'ReturnMessage'
SZDDESYS_ITEM_STATUS: String = 'Status'
SZDDESYS_ITEM_FORMATS: String = 'Formats'
SZDDESYS_ITEM_HELP: String = 'Help'
SZDDE_ITEM_ITEMLIST: String = 'TopicItemList'
APPCMD_MASK: Int32 = 4080
APPCLASS_MASK: Int32 = 15
HDATA_APPOWNED: UInt32 = 1
DMLERR_NO_ERROR: UInt32 = 0
DMLERR_FIRST: UInt32 = 16384
DMLERR_ADVACKTIMEOUT: UInt32 = 16384
DMLERR_BUSY: UInt32 = 16385
DMLERR_DATAACKTIMEOUT: UInt32 = 16386
DMLERR_DLL_NOT_INITIALIZED: UInt32 = 16387
DMLERR_DLL_USAGE: UInt32 = 16388
DMLERR_EXECACKTIMEOUT: UInt32 = 16389
DMLERR_INVALIDPARAMETER: UInt32 = 16390
DMLERR_LOW_MEMORY: UInt32 = 16391
DMLERR_MEMORY_ERROR: UInt32 = 16392
DMLERR_NOTPROCESSED: UInt32 = 16393
DMLERR_NO_CONV_ESTABLISHED: UInt32 = 16394
DMLERR_POKEACKTIMEOUT: UInt32 = 16395
DMLERR_POSTMSG_FAILED: UInt32 = 16396
DMLERR_REENTRANCY: UInt32 = 16397
DMLERR_SERVER_DIED: UInt32 = 16398
DMLERR_SYS_ERROR: UInt32 = 16399
DMLERR_UNADVACKTIMEOUT: UInt32 = 16400
DMLERR_UNFOUND_QUEUE_ID: UInt32 = 16401
DMLERR_LAST: UInt32 = 16401
MH_CREATE: UInt32 = 1
MH_KEEP: UInt32 = 2
MH_DELETE: UInt32 = 3
MH_CLEANUP: UInt32 = 4
MAX_MONITORS: UInt32 = 4
MF_MASK: UInt32 = 4278190080
@winfunctype('USER32.dll')
def DdeSetQualityOfService(hwndClient: win32more.Windows.Win32.Foundation.HWND, pqosNew: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE_head), pqosPrev: POINTER(win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE_head)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ImpersonateDdeClientWindow(hWndClient: win32more.Windows.Win32.Foundation.HWND, hWndServer: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def PackDDElParam(msg: UInt32, uiLo: UIntPtr, uiHi: UIntPtr) -> win32more.Windows.Win32.Foundation.LPARAM: ...
@winfunctype('USER32.dll')
def UnpackDDElParam(msg: UInt32, lParam: win32more.Windows.Win32.Foundation.LPARAM, puiLo: POINTER(UIntPtr), puiHi: POINTER(UIntPtr)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def FreeDDElParam(msg: UInt32, lParam: win32more.Windows.Win32.Foundation.LPARAM) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ReuseDDElParam(lParam: win32more.Windows.Win32.Foundation.LPARAM, msgIn: UInt32, msgOut: UInt32, uiLo: UIntPtr, uiHi: UIntPtr) -> win32more.Windows.Win32.Foundation.LPARAM: ...
@winfunctype('USER32.dll')
def DdeInitializeA(pidInst: POINTER(UInt32), pfnCallback: win32more.Windows.Win32.System.DataExchange.PFNCALLBACK, afCmd: win32more.Windows.Win32.System.DataExchange.DDE_INITIALIZE_COMMAND, ulRes: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeInitializeW(pidInst: POINTER(UInt32), pfnCallback: win32more.Windows.Win32.System.DataExchange.PFNCALLBACK, afCmd: win32more.Windows.Win32.System.DataExchange.DDE_INITIALIZE_COMMAND, ulRes: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeUninitialize(idInst: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeConnectList(idInst: UInt32, hszService: win32more.Windows.Win32.System.DataExchange.HSZ, hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ, hConvList: win32more.Windows.Win32.System.DataExchange.HCONVLIST, pCC: POINTER(win32more.Windows.Win32.System.DataExchange.CONVCONTEXT_head)) -> win32more.Windows.Win32.System.DataExchange.HCONVLIST: ...
@winfunctype('USER32.dll')
def DdeQueryNextServer(hConvList: win32more.Windows.Win32.System.DataExchange.HCONVLIST, hConvPrev: win32more.Windows.Win32.System.DataExchange.HCONV) -> win32more.Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeDisconnectList(hConvList: win32more.Windows.Win32.System.DataExchange.HCONVLIST) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeConnect(idInst: UInt32, hszService: win32more.Windows.Win32.System.DataExchange.HSZ, hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ, pCC: POINTER(win32more.Windows.Win32.System.DataExchange.CONVCONTEXT_head)) -> win32more.Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeDisconnect(hConv: win32more.Windows.Win32.System.DataExchange.HCONV) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeReconnect(hConv: win32more.Windows.Win32.System.DataExchange.HCONV) -> win32more.Windows.Win32.System.DataExchange.HCONV: ...
@winfunctype('USER32.dll')
def DdeQueryConvInfo(hConv: win32more.Windows.Win32.System.DataExchange.HCONV, idTransaction: UInt32, pConvInfo: POINTER(win32more.Windows.Win32.System.DataExchange.CONVINFO_head)) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeSetUserHandle(hConv: win32more.Windows.Win32.System.DataExchange.HCONV, id: UInt32, hUser: UIntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeAbandonTransaction(idInst: UInt32, hConv: win32more.Windows.Win32.System.DataExchange.HCONV, idTransaction: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdePostAdvise(idInst: UInt32, hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ, hszItem: win32more.Windows.Win32.System.DataExchange.HSZ) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeEnableCallback(idInst: UInt32, hConv: win32more.Windows.Win32.System.DataExchange.HCONV, wCmd: win32more.Windows.Win32.System.DataExchange.DDE_ENABLE_CALLBACK_CMD) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeImpersonateClient(hConv: win32more.Windows.Win32.System.DataExchange.HCONV) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeNameService(idInst: UInt32, hsz1: win32more.Windows.Win32.System.DataExchange.HSZ, hsz2: win32more.Windows.Win32.System.DataExchange.HSZ, afCmd: win32more.Windows.Win32.System.DataExchange.DDE_NAME_SERVICE_CMD) -> win32more.Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeClientTransaction(pData: POINTER(Byte), cbData: UInt32, hConv: win32more.Windows.Win32.System.DataExchange.HCONV, hszItem: win32more.Windows.Win32.System.DataExchange.HSZ, wFmt: UInt32, wType: win32more.Windows.Win32.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE, dwTimeout: UInt32, pdwResult: POINTER(UInt32)) -> win32more.Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeCreateDataHandle(idInst: UInt32, pSrc: POINTER(Byte), cb: UInt32, cbOff: UInt32, hszItem: win32more.Windows.Win32.System.DataExchange.HSZ, wFmt: UInt32, afCmd: UInt32) -> win32more.Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeAddData(hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA, pSrc: POINTER(Byte), cb: UInt32, cbOff: UInt32) -> win32more.Windows.Win32.System.DataExchange.HDDEDATA: ...
@winfunctype('USER32.dll')
def DdeGetData(hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA, pDst: POINTER(Byte), cbMax: UInt32, cbOff: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeAccessData(hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA, pcbDataSize: POINTER(UInt32)) -> POINTER(Byte): ...
@winfunctype('USER32.dll')
def DdeUnaccessData(hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeFreeDataHandle(hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeGetLastError(idInst: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeCreateStringHandleA(idInst: UInt32, psz: win32more.Windows.Win32.Foundation.PSTR, iCodePage: Int32) -> win32more.Windows.Win32.System.DataExchange.HSZ: ...
@winfunctype('USER32.dll')
def DdeCreateStringHandleW(idInst: UInt32, psz: win32more.Windows.Win32.Foundation.PWSTR, iCodePage: Int32) -> win32more.Windows.Win32.System.DataExchange.HSZ: ...
@winfunctype('USER32.dll')
def DdeQueryStringA(idInst: UInt32, hsz: win32more.Windows.Win32.System.DataExchange.HSZ, psz: win32more.Windows.Win32.Foundation.PSTR, cchMax: UInt32, iCodePage: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeQueryStringW(idInst: UInt32, hsz: win32more.Windows.Win32.System.DataExchange.HSZ, psz: win32more.Windows.Win32.Foundation.PWSTR, cchMax: UInt32, iCodePage: Int32) -> UInt32: ...
@winfunctype('USER32.dll')
def DdeFreeStringHandle(idInst: UInt32, hsz: win32more.Windows.Win32.System.DataExchange.HSZ) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeKeepStringHandle(idInst: UInt32, hsz: win32more.Windows.Win32.System.DataExchange.HSZ) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def DdeCmpStringHandles(hsz1: win32more.Windows.Win32.System.DataExchange.HSZ, hsz2: win32more.Windows.Win32.System.DataExchange.HSZ) -> Int32: ...
@winfunctype('GDI32.dll')
def SetWinMetaFileBits(nSize: UInt32, lpMeta16Data: POINTER(Byte), hdcRef: win32more.Windows.Win32.Graphics.Gdi.HDC, lpMFP: POINTER(win32more.Windows.Win32.System.DataExchange.METAFILEPICT_head)) -> win32more.Windows.Win32.Graphics.Gdi.HENHMETAFILE: ...
@winfunctype('USER32.dll')
def OpenClipboard(hWndNewOwner: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def CloseClipboard() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetClipboardSequenceNumber() -> UInt32: ...
@winfunctype('USER32.dll')
def GetClipboardOwner() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def SetClipboardViewer(hWndNewViewer: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def GetClipboardViewer() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def ChangeClipboardChain(hWndRemove: win32more.Windows.Win32.Foundation.HWND, hWndNewNext: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def SetClipboardData(uFormat: UInt32, hMem: win32more.Windows.Win32.Foundation.HANDLE) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USER32.dll')
def GetClipboardData(uFormat: UInt32) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('USER32.dll')
def RegisterClipboardFormatA(lpszFormat: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('USER32.dll')
def RegisterClipboardFormatW(lpszFormat: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('USER32.dll')
def CountClipboardFormats() -> Int32: ...
@winfunctype('USER32.dll')
def EnumClipboardFormats(format: UInt32) -> UInt32: ...
@winfunctype('USER32.dll')
def GetClipboardFormatNameA(format: UInt32, lpszFormatName: win32more.Windows.Win32.Foundation.PSTR, cchMaxCount: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetClipboardFormatNameW(format: UInt32, lpszFormatName: win32more.Windows.Win32.Foundation.PWSTR, cchMaxCount: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def EmptyClipboard() -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def IsClipboardFormatAvailable(format: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetPriorityClipboardFormat(paFormatPriorityList: POINTER(UInt32), cFormats: Int32) -> Int32: ...
@winfunctype('USER32.dll')
def GetOpenClipboardWindow() -> win32more.Windows.Win32.Foundation.HWND: ...
@winfunctype('USER32.dll')
def AddClipboardFormatListener(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def RemoveClipboardFormatListener(hwnd: win32more.Windows.Win32.Foundation.HWND) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def GetUpdatedClipboardFormats(lpuiFormats: POINTER(UInt32), cFormats: UInt32, pcFormatsOut: POINTER(UInt32)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GlobalDeleteAtom(nAtom: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def InitAtomTable(nSize: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def DeleteAtom(nAtom: UInt16) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomA(lpString: win32more.Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomW(lpString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomExA(lpString: win32more.Windows.Win32.Foundation.PSTR, Flags: UInt32) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalAddAtomExW(lpString: win32more.Windows.Win32.Foundation.PWSTR, Flags: UInt32) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalFindAtomA(lpString: win32more.Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalFindAtomW(lpString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GlobalGetAtomNameA(nAtom: UInt16, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GlobalGetAtomNameW(nAtom: UInt16, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddAtomA(lpString: win32more.Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def AddAtomW(lpString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def FindAtomA(lpString: win32more.Windows.Win32.Foundation.PSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def FindAtomW(lpString: win32more.Windows.Win32.Foundation.PWSTR) -> UInt16: ...
@winfunctype('KERNEL32.dll')
def GetAtomNameA(nAtom: UInt16, lpBuffer: win32more.Windows.Win32.Foundation.PSTR, nSize: Int32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetAtomNameW(nAtom: UInt16, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR, nSize: Int32) -> UInt32: ...
class CONVCONTEXT(EasyCastStructure):
    cb: UInt32
    wFlags: UInt32
    wCountryID: UInt32
    iCodePage: Int32
    dwLangID: UInt32
    dwSecurity: UInt32
    qos: win32more.Windows.Win32.Security.SECURITY_QUALITY_OF_SERVICE
class CONVINFO(EasyCastStructure):
    cb: UInt32
    hUser: UIntPtr
    hConvPartner: win32more.Windows.Win32.System.DataExchange.HCONV
    hszSvcPartner: win32more.Windows.Win32.System.DataExchange.HSZ
    hszServiceReq: win32more.Windows.Win32.System.DataExchange.HSZ
    hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ
    hszItem: win32more.Windows.Win32.System.DataExchange.HSZ
    wFmt: UInt32
    wType: win32more.Windows.Win32.System.DataExchange.DDE_CLIENT_TRANSACTION_TYPE
    wStatus: win32more.Windows.Win32.System.DataExchange.CONVINFO_STATUS
    wConvst: win32more.Windows.Win32.System.DataExchange.CONVINFO_CONVERSATION_STATE
    wLastError: UInt32
    hConvList: win32more.Windows.Win32.System.DataExchange.HCONVLIST
    ConvCtxt: win32more.Windows.Win32.System.DataExchange.CONVCONTEXT
    hwnd: win32more.Windows.Win32.Foundation.HWND
    hwndPartner: win32more.Windows.Win32.Foundation.HWND
CONVINFO_CONVERSATION_STATE = UInt32
XST_ADVACKRCVD: CONVINFO_CONVERSATION_STATE = 13
XST_ADVDATAACKRCVD: CONVINFO_CONVERSATION_STATE = 16
XST_ADVDATASENT: CONVINFO_CONVERSATION_STATE = 15
XST_ADVSENT: CONVINFO_CONVERSATION_STATE = 11
XST_CONNECTED: CONVINFO_CONVERSATION_STATE = 2
XST_DATARCVD: CONVINFO_CONVERSATION_STATE = 6
XST_EXECACKRCVD: CONVINFO_CONVERSATION_STATE = 10
XST_EXECSENT: CONVINFO_CONVERSATION_STATE = 9
XST_INCOMPLETE: CONVINFO_CONVERSATION_STATE = 1
XST_INIT1: CONVINFO_CONVERSATION_STATE = 3
XST_INIT2: CONVINFO_CONVERSATION_STATE = 4
XST_NULL: CONVINFO_CONVERSATION_STATE = 0
XST_POKEACKRCVD: CONVINFO_CONVERSATION_STATE = 8
XST_POKESENT: CONVINFO_CONVERSATION_STATE = 7
XST_REQSENT: CONVINFO_CONVERSATION_STATE = 5
XST_UNADVACKRCVD: CONVINFO_CONVERSATION_STATE = 14
XST_UNADVSENT: CONVINFO_CONVERSATION_STATE = 12
CONVINFO_STATUS = UInt32
ST_ADVISE: CONVINFO_STATUS = 2
ST_BLOCKED: CONVINFO_STATUS = 8
ST_BLOCKNEXT: CONVINFO_STATUS = 128
ST_CLIENT: CONVINFO_STATUS = 16
ST_CONNECTED: CONVINFO_STATUS = 1
ST_INLIST: CONVINFO_STATUS = 64
ST_ISLOCAL: CONVINFO_STATUS = 4
ST_ISSELF: CONVINFO_STATUS = 256
ST_TERMINATED: CONVINFO_STATUS = 32
class COPYDATASTRUCT(EasyCastStructure):
    dwData: UIntPtr
    cbData: UInt32
    lpData: VoidPtr
class DDEACK(EasyCastStructure):
    _bitfield: UInt16
class DDEADVISE(EasyCastStructure):
    _bitfield: UInt16
    cfFormat: Int16
class DDEDATA(EasyCastStructure):
    _bitfield: UInt16
    cfFormat: Int16
    Value: Byte * 1
class DDELN(EasyCastStructure):
    _bitfield: UInt16
    cfFormat: Int16
class DDEML_MSG_HOOK_DATA(EasyCastStructure):
    uiLo: UIntPtr
    uiHi: UIntPtr
    cbData: UInt32
    Data: UInt32 * 8
class DDEPOKE(EasyCastStructure):
    _bitfield: UInt16
    cfFormat: Int16
    Value: Byte * 1
class DDEUP(EasyCastStructure):
    _bitfield: UInt16
    cfFormat: Int16
    rgb: Byte * 1
DDE_CLIENT_TRANSACTION_TYPE = UInt32
XTYP_ADVSTART: DDE_CLIENT_TRANSACTION_TYPE = 4144
XTYP_ADVSTOP: DDE_CLIENT_TRANSACTION_TYPE = 32832
XTYP_EXECUTE: DDE_CLIENT_TRANSACTION_TYPE = 16464
XTYP_POKE: DDE_CLIENT_TRANSACTION_TYPE = 16528
XTYP_REQUEST: DDE_CLIENT_TRANSACTION_TYPE = 8368
XTYP_ADVDATA: DDE_CLIENT_TRANSACTION_TYPE = 16400
XTYP_ADVREQ: DDE_CLIENT_TRANSACTION_TYPE = 8226
XTYP_CONNECT: DDE_CLIENT_TRANSACTION_TYPE = 4194
XTYP_CONNECT_CONFIRM: DDE_CLIENT_TRANSACTION_TYPE = 32882
XTYP_DISCONNECT: DDE_CLIENT_TRANSACTION_TYPE = 32962
XTYP_MONITOR: DDE_CLIENT_TRANSACTION_TYPE = 33010
XTYP_REGISTER: DDE_CLIENT_TRANSACTION_TYPE = 32930
XTYP_UNREGISTER: DDE_CLIENT_TRANSACTION_TYPE = 32978
XTYP_WILDCONNECT: DDE_CLIENT_TRANSACTION_TYPE = 8418
XTYP_XACT_COMPLETE: DDE_CLIENT_TRANSACTION_TYPE = 32896
DDE_ENABLE_CALLBACK_CMD = UInt32
EC_ENABLEALL: DDE_ENABLE_CALLBACK_CMD = 0
EC_ENABLEONE: DDE_ENABLE_CALLBACK_CMD = 128
EC_DISABLE: DDE_ENABLE_CALLBACK_CMD = 8
EC_QUERYWAITING: DDE_ENABLE_CALLBACK_CMD = 2
DDE_INITIALIZE_COMMAND = UInt32
APPCLASS_MONITOR: DDE_INITIALIZE_COMMAND = 1
APPCLASS_STANDARD: DDE_INITIALIZE_COMMAND = 0
APPCMD_CLIENTONLY: DDE_INITIALIZE_COMMAND = 16
APPCMD_FILTERINITS: DDE_INITIALIZE_COMMAND = 32
CBF_FAIL_ALLSVRXACTIONS: DDE_INITIALIZE_COMMAND = 258048
CBF_FAIL_ADVISES: DDE_INITIALIZE_COMMAND = 16384
CBF_FAIL_CONNECTIONS: DDE_INITIALIZE_COMMAND = 8192
CBF_FAIL_EXECUTES: DDE_INITIALIZE_COMMAND = 32768
CBF_FAIL_POKES: DDE_INITIALIZE_COMMAND = 65536
CBF_FAIL_REQUESTS: DDE_INITIALIZE_COMMAND = 131072
CBF_FAIL_SELFCONNECTIONS: DDE_INITIALIZE_COMMAND = 4096
CBF_SKIP_ALLNOTIFICATIONS: DDE_INITIALIZE_COMMAND = 3932160
CBF_SKIP_CONNECT_CONFIRMS: DDE_INITIALIZE_COMMAND = 262144
CBF_SKIP_DISCONNECTS: DDE_INITIALIZE_COMMAND = 2097152
CBF_SKIP_REGISTRATIONS: DDE_INITIALIZE_COMMAND = 524288
CBF_SKIP_UNREGISTRATIONS: DDE_INITIALIZE_COMMAND = 1048576
MF_CALLBACKS: DDE_INITIALIZE_COMMAND = 134217728
MF_CONV: DDE_INITIALIZE_COMMAND = 1073741824
MF_ERRORS: DDE_INITIALIZE_COMMAND = 268435456
MF_HSZ_INFO: DDE_INITIALIZE_COMMAND = 16777216
MF_LINKS: DDE_INITIALIZE_COMMAND = 536870912
MF_POSTMSGS: DDE_INITIALIZE_COMMAND = 67108864
MF_SENDMSGS: DDE_INITIALIZE_COMMAND = 33554432
DDE_NAME_SERVICE_CMD = UInt32
DNS_REGISTER: DDE_NAME_SERVICE_CMD = 1
DNS_UNREGISTER: DDE_NAME_SERVICE_CMD = 2
DNS_FILTERON: DDE_NAME_SERVICE_CMD = 4
DNS_FILTEROFF: DDE_NAME_SERVICE_CMD = 8
HCONV = IntPtr
HCONVLIST = IntPtr
HDDEDATA = IntPtr
HSZ = IntPtr
class HSZPAIR(EasyCastStructure):
    hszSvc: win32more.Windows.Win32.System.DataExchange.HSZ
    hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ
class METAFILEPICT(EasyCastStructure):
    mm: Int32
    xExt: Int32
    yExt: Int32
    hMF: win32more.Windows.Win32.Graphics.Gdi.HMETAFILE
class MONCBSTRUCT(EasyCastStructure):
    cb: UInt32
    dwTime: UInt32
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    dwRet: UInt32
    wType: UInt32
    wFmt: UInt32
    hConv: win32more.Windows.Win32.System.DataExchange.HCONV
    hsz1: win32more.Windows.Win32.System.DataExchange.HSZ
    hsz2: win32more.Windows.Win32.System.DataExchange.HSZ
    hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA
    dwData1: UIntPtr
    dwData2: UIntPtr
    cc: win32more.Windows.Win32.System.DataExchange.CONVCONTEXT
    cbData: UInt32
    Data: UInt32 * 8
class MONCONVSTRUCT(EasyCastStructure):
    cb: UInt32
    fConnect: win32more.Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    hszSvc: win32more.Windows.Win32.System.DataExchange.HSZ
    hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ
    hConvClient: win32more.Windows.Win32.System.DataExchange.HCONV
    hConvServer: win32more.Windows.Win32.System.DataExchange.HCONV
class MONERRSTRUCT(EasyCastStructure):
    cb: UInt32
    wLastError: UInt32
    dwTime: UInt32
    hTask: win32more.Windows.Win32.Foundation.HANDLE
class MONHSZSTRUCTA(EasyCastStructure):
    cb: UInt32
    fsAction: win32more.Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hsz: win32more.Windows.Win32.System.DataExchange.HSZ
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    str: win32more.Windows.Win32.Foundation.CHAR * 1
class MONHSZSTRUCTW(EasyCastStructure):
    cb: UInt32
    fsAction: win32more.Windows.Win32.Foundation.BOOL
    dwTime: UInt32
    hsz: win32more.Windows.Win32.System.DataExchange.HSZ
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    str: Char * 1
class MONLINKSTRUCT(EasyCastStructure):
    cb: UInt32
    dwTime: UInt32
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    fEstablished: win32more.Windows.Win32.Foundation.BOOL
    fNoData: win32more.Windows.Win32.Foundation.BOOL
    hszSvc: win32more.Windows.Win32.System.DataExchange.HSZ
    hszTopic: win32more.Windows.Win32.System.DataExchange.HSZ
    hszItem: win32more.Windows.Win32.System.DataExchange.HSZ
    wFmt: UInt32
    fServer: win32more.Windows.Win32.Foundation.BOOL
    hConvServer: win32more.Windows.Win32.System.DataExchange.HCONV
    hConvClient: win32more.Windows.Win32.System.DataExchange.HCONV
class MONMSGSTRUCT(EasyCastStructure):
    cb: UInt32
    hwndTo: win32more.Windows.Win32.Foundation.HWND
    dwTime: UInt32
    hTask: win32more.Windows.Win32.Foundation.HANDLE
    wMsg: UInt32
    wParam: win32more.Windows.Win32.Foundation.WPARAM
    lParam: win32more.Windows.Win32.Foundation.LPARAM
    dmhd: win32more.Windows.Win32.System.DataExchange.DDEML_MSG_HOOK_DATA
@winfunctype_pointer
def PFNCALLBACK(wType: UInt32, wFmt: UInt32, hConv: win32more.Windows.Win32.System.DataExchange.HCONV, hsz1: win32more.Windows.Win32.System.DataExchange.HSZ, hsz2: win32more.Windows.Win32.System.DataExchange.HSZ, hData: win32more.Windows.Win32.System.DataExchange.HDDEDATA, dwData1: UIntPtr, dwData2: UIntPtr) -> win32more.Windows.Win32.System.DataExchange.HDDEDATA: ...
make_head(_module, 'CONVCONTEXT')
make_head(_module, 'CONVINFO')
make_head(_module, 'COPYDATASTRUCT')
make_head(_module, 'DDEACK')
make_head(_module, 'DDEADVISE')
make_head(_module, 'DDEDATA')
make_head(_module, 'DDELN')
make_head(_module, 'DDEML_MSG_HOOK_DATA')
make_head(_module, 'DDEPOKE')
make_head(_module, 'DDEUP')
make_head(_module, 'HSZPAIR')
make_head(_module, 'METAFILEPICT')
make_head(_module, 'MONCBSTRUCT')
make_head(_module, 'MONCONVSTRUCT')
make_head(_module, 'MONERRSTRUCT')
make_head(_module, 'MONHSZSTRUCTA')
make_head(_module, 'MONHSZSTRUCTW')
make_head(_module, 'MONLINKSTRUCT')
make_head(_module, 'MONMSGSTRUCT')
make_head(_module, 'PFNCALLBACK')