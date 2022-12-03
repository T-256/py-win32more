from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.System.Mailslots
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
def _define_CreateMailslotA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateMailslotA', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'nMaxMessageSize'),(1, 'lReadTimeout'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateMailslotW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateMailslotW', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'nMaxMessageSize'),(1, 'lReadTimeout'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetMailslotInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetMailslotInfo', windll['KERNEL32.dll']), ((1, 'hMailslot'),(1, 'lpMaxMessageSize'),(1, 'lpNextSize'),(1, 'lpMessageCount'),(1, 'lpReadTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetMailslotInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('SetMailslotInfo', windll['KERNEL32.dll']), ((1, 'hMailslot'),(1, 'lReadTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
__all__ = [
    "CreateMailslotA",
    "CreateMailslotW",
    "GetMailslotInfo",
    "SetMailslotInfo",
]
