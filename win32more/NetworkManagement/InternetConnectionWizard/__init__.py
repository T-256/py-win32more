from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.NetworkManagement.InternetConnectionWizard
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
ICW_REGPATHSETTINGS = 'Software\\Microsoft\\Internet Connection Wizard'
ICW_REGKEYCOMPLETED = 'Completed'
ICW_MAX_ACCTNAME = 256
ICW_MAX_PASSWORD = 256
ICW_MAX_LOGONNAME = 256
ICW_MAX_SERVERNAME = 64
ICW_MAX_RASNAME = 256
ICW_MAX_EMAILNAME = 64
ICW_MAX_EMAILADDR = 128
ICW_CHECKSTATUS = 1
ICW_LAUNCHFULL = 256
ICW_LAUNCHMANUAL = 512
ICW_USE_SHELLNEXT = 1024
ICW_FULL_SMARTSTART = 2048
ICW_FULLPRESENT = 1
ICW_MANUALPRESENT = 2
ICW_ALREADYRUN = 4
ICW_LAUNCHEDFULL = 256
ICW_LAUNCHEDMANUAL = 512
ICW_USEDEFAULTS = 1
def _define_PFNCHECKCONNECTIONWIZARD():
    return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32))
def _define_PFNSETSHELLNEXT():
    return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR)
__all__ = [
    "ICW_ALREADYRUN",
    "ICW_CHECKSTATUS",
    "ICW_FULLPRESENT",
    "ICW_FULL_SMARTSTART",
    "ICW_LAUNCHEDFULL",
    "ICW_LAUNCHEDMANUAL",
    "ICW_LAUNCHFULL",
    "ICW_LAUNCHMANUAL",
    "ICW_MANUALPRESENT",
    "ICW_MAX_ACCTNAME",
    "ICW_MAX_EMAILADDR",
    "ICW_MAX_EMAILNAME",
    "ICW_MAX_LOGONNAME",
    "ICW_MAX_PASSWORD",
    "ICW_MAX_RASNAME",
    "ICW_MAX_SERVERNAME",
    "ICW_REGKEYCOMPLETED",
    "ICW_REGPATHSETTINGS",
    "ICW_USEDEFAULTS",
    "ICW_USE_SHELLNEXT",
    "PFNCHECKCONNECTIONWIZARD",
    "PFNSETSHELLNEXT",
]