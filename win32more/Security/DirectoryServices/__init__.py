from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.Security.Authorization.UI
import win32more.Security.DirectoryServices
import win32more.UI.Controls
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
DSSI_READ_ONLY = 1
DSSI_NO_ACCESS_CHECK = 2
DSSI_NO_EDIT_SACL = 4
DSSI_NO_EDIT_OWNER = 8
DSSI_IS_ROOT = 16
DSSI_NO_FILTER = 32
DSSI_NO_READONLY_MESSAGE = 64
def _define_DSCreateISecurityInfoObject():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)(('DSCreateISecurityInfoObject', windll['DSSEC.dll']), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'ppSI'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSCreateISecurityInfoObjectEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)(('DSCreateISecurityInfoObjectEx', windll['DSSEC.dll']), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'pwszServer'),(1, 'pwszUserName'),(1, 'pwszPassword'),(1, 'dwFlags'),(1, 'ppSI'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSCreateSecurityPage():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.Controls.HPROPSHEETPAGE),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)(('DSCreateSecurityPage', windll['DSSEC.dll']), ((1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'phPage'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DSEditSecurity():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)(('DSEditSecurity', windll['DSSEC.dll']), ((1, 'hwndOwner'),(1, 'pwszObjectPath'),(1, 'pwszObjectClass'),(1, 'dwFlags'),(1, 'pwszCaption'),(1, 'pfnReadSD'),(1, 'pfnWriteSD'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PFNDSCREATEISECINFO():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)
def _define_PFNDSCREATEISECINFOEX():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.Authorization.UI.ISecurityInformation_head),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)
def _define_PFNDSCREATESECPAGE():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.UI.Controls.HPROPSHEETPAGE),win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)
def _define_PFNDSEDITSECURITY():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HWND,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,win32more.Security.DirectoryServices.PFNREADOBJECTSECURITY,win32more.Security.DirectoryServices.PFNWRITEOBJECTSECURITY,win32more.Foundation.LPARAM)
def _define_PFNREADOBJECTSECURITY():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Security.PSECURITY_DESCRIPTOR),win32more.Foundation.LPARAM)
def _define_PFNWRITEOBJECTSECURITY():
    return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Security.PSECURITY_DESCRIPTOR,win32more.Foundation.LPARAM)
__all__ = [
    "DSCreateISecurityInfoObject",
    "DSCreateISecurityInfoObjectEx",
    "DSCreateSecurityPage",
    "DSEditSecurity",
    "DSSI_IS_ROOT",
    "DSSI_NO_ACCESS_CHECK",
    "DSSI_NO_EDIT_OWNER",
    "DSSI_NO_EDIT_SACL",
    "DSSI_NO_FILTER",
    "DSSI_NO_READONLY_MESSAGE",
    "DSSI_READ_ONLY",
    "PFNDSCREATEISECINFO",
    "PFNDSCREATEISECINFOEX",
    "PFNDSCREATESECPAGE",
    "PFNDSEDITSECURITY",
    "PFNREADOBJECTSECURITY",
    "PFNWRITEOBJECTSECURITY",
]
