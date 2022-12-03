from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.System.Shutdown
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
MAX_REASON_NAME_LEN = 64
MAX_REASON_DESC_LEN = 256
MAX_REASON_BUGID_LEN = 32
MAX_REASON_COMMENT_LEN = 512
SHUTDOWN_TYPE_LEN = 32
POLICY_SHOWREASONUI_NEVER = 0
POLICY_SHOWREASONUI_ALWAYS = 1
POLICY_SHOWREASONUI_WORKSTATIONONLY = 2
POLICY_SHOWREASONUI_SERVERONLY = 3
SNAPSHOT_POLICY_NEVER = 0
SNAPSHOT_POLICY_ALWAYS = 1
SNAPSHOT_POLICY_UNPLANNED = 2
MAX_NUM_REASONS = 256
def _define_InitiateSystemShutdownA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('InitiateSystemShutdownA', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwTimeout'),(1, 'bForceAppsClosed'),(1, 'bRebootAfterShutdown'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitiateSystemShutdownW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL)(('InitiateSystemShutdownW', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwTimeout'),(1, 'bForceAppsClosed'),(1, 'bRebootAfterShutdown'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AbortSystemShutdownA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('AbortSystemShutdownA', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AbortSystemShutdownW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('AbortSystemShutdownW', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitiateSystemShutdownExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.System.Shutdown.SHUTDOWN_REASON)(('InitiateSystemShutdownExA', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwTimeout'),(1, 'bForceAppsClosed'),(1, 'bRebootAfterShutdown'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitiateSystemShutdownExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.BOOL,win32more.Foundation.BOOL,win32more.System.Shutdown.SHUTDOWN_REASON)(('InitiateSystemShutdownExW', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwTimeout'),(1, 'bForceAppsClosed'),(1, 'bRebootAfterShutdown'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitiateShutdownA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.System.Shutdown.SHUTDOWN_FLAGS,win32more.System.Shutdown.SHUTDOWN_REASON)(('InitiateShutdownA', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwGracePeriod'),(1, 'dwShutdownFlags'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InitiateShutdownW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.System.Shutdown.SHUTDOWN_FLAGS,win32more.System.Shutdown.SHUTDOWN_REASON)(('InitiateShutdownW', windll['ADVAPI32.dll']), ((1, 'lpMachineName'),(1, 'lpMessage'),(1, 'dwGracePeriod'),(1, 'dwShutdownFlags'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckForHiberboot():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Foundation.BOOLEAN),win32more.Foundation.BOOLEAN)(('CheckForHiberboot', windll['ADVAPI32.dll']), ((1, 'pHiberboot'),(1, 'bClearFlag'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExitWindowsEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.System.Shutdown.EXIT_WINDOWS_FLAGS,win32more.System.Shutdown.SHUTDOWN_REASON)(('ExitWindowsEx', windll['USER32.dll']), ((1, 'uFlags'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockWorkStation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('LockWorkStation', windll['USER32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShutdownBlockReasonCreate():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.PWSTR)(('ShutdownBlockReasonCreate', windll['USER32.dll']), ((1, 'hWnd'),(1, 'pwszReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShutdownBlockReasonQuery():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Foundation.PWSTR,POINTER(UInt32))(('ShutdownBlockReasonQuery', windll['USER32.dll']), ((1, 'hWnd'),(1, 'pwszBuff'),(1, 'pcchBuff'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ShutdownBlockReasonDestroy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND)(('ShutdownBlockReasonDestroy', windll['USER32.dll']), ((1, 'hWnd'),))
    except (FileNotFoundError, AttributeError):
        return None
EXIT_WINDOWS_FLAGS = UInt32
EWX_HYBRID_SHUTDOWN = 4194304
EWX_LOGOFF = 0
EWX_POWEROFF = 8
EWX_REBOOT = 2
EWX_RESTARTAPPS = 64
EWX_SHUTDOWN = 1
SHUTDOWN_FLAGS = UInt32
SHUTDOWN_FORCE_OTHERS = 1
SHUTDOWN_FORCE_SELF = 2
SHUTDOWN_RESTART = 4
SHUTDOWN_POWEROFF = 8
SHUTDOWN_NOREBOOT = 16
SHUTDOWN_GRACE_OVERRIDE = 32
SHUTDOWN_INSTALL_UPDATES = 64
SHUTDOWN_RESTARTAPPS = 128
SHUTDOWN_SKIP_SVC_PRESHUTDOWN = 256
SHUTDOWN_HYBRID = 512
SHUTDOWN_RESTART_BOOTOPTIONS = 1024
SHUTDOWN_SOFT_REBOOT = 2048
SHUTDOWN_MOBILE_UI = 4096
SHUTDOWN_ARSO = 8192
SHUTDOWN_CHECK_SAFE_FOR_SERVER = 16384
SHUTDOWN_VAIL_CONTAINER = 32768
SHUTDOWN_SYSTEM_INITIATED = 65536
SHUTDOWN_REASON = UInt32
SHTDN_REASON_NONE = 0
SHTDN_REASON_FLAG_COMMENT_REQUIRED = 16777216
SHTDN_REASON_FLAG_DIRTY_PROBLEM_ID_REQUIRED = 33554432
SHTDN_REASON_FLAG_CLEAN_UI = 67108864
SHTDN_REASON_FLAG_DIRTY_UI = 134217728
SHTDN_REASON_FLAG_MOBILE_UI_RESERVED = 268435456
SHTDN_REASON_FLAG_USER_DEFINED = 1073741824
SHTDN_REASON_FLAG_PLANNED = 2147483648
SHTDN_REASON_MAJOR_OTHER = 0
SHTDN_REASON_MAJOR_NONE = 0
SHTDN_REASON_MAJOR_HARDWARE = 65536
SHTDN_REASON_MAJOR_OPERATINGSYSTEM = 131072
SHTDN_REASON_MAJOR_SOFTWARE = 196608
SHTDN_REASON_MAJOR_APPLICATION = 262144
SHTDN_REASON_MAJOR_SYSTEM = 327680
SHTDN_REASON_MAJOR_POWER = 393216
SHTDN_REASON_MAJOR_LEGACY_API = 458752
SHTDN_REASON_MINOR_OTHER = 0
SHTDN_REASON_MINOR_NONE = 255
SHTDN_REASON_MINOR_MAINTENANCE = 1
SHTDN_REASON_MINOR_INSTALLATION = 2
SHTDN_REASON_MINOR_UPGRADE = 3
SHTDN_REASON_MINOR_RECONFIG = 4
SHTDN_REASON_MINOR_HUNG = 5
SHTDN_REASON_MINOR_UNSTABLE = 6
SHTDN_REASON_MINOR_DISK = 7
SHTDN_REASON_MINOR_PROCESSOR = 8
SHTDN_REASON_MINOR_NETWORKCARD = 9
SHTDN_REASON_MINOR_POWER_SUPPLY = 10
SHTDN_REASON_MINOR_CORDUNPLUGGED = 11
SHTDN_REASON_MINOR_ENVIRONMENT = 12
SHTDN_REASON_MINOR_HARDWARE_DRIVER = 13
SHTDN_REASON_MINOR_OTHERDRIVER = 14
SHTDN_REASON_MINOR_BLUESCREEN = 15
SHTDN_REASON_MINOR_SERVICEPACK = 16
SHTDN_REASON_MINOR_HOTFIX = 17
SHTDN_REASON_MINOR_SECURITYFIX = 18
SHTDN_REASON_MINOR_SECURITY = 19
SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY = 20
SHTDN_REASON_MINOR_WMI = 21
SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL = 22
SHTDN_REASON_MINOR_HOTFIX_UNINSTALL = 23
SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL = 24
SHTDN_REASON_MINOR_MMC = 25
SHTDN_REASON_MINOR_SYSTEMRESTORE = 26
SHTDN_REASON_MINOR_TERMSRV = 32
SHTDN_REASON_MINOR_DC_PROMOTION = 33
SHTDN_REASON_MINOR_DC_DEMOTION = 34
SHTDN_REASON_UNKNOWN = 255
SHTDN_REASON_LEGACY_API = 2147942400
SHTDN_REASON_VALID_BIT_MASK = 3238002687
__all__ = [
    "AbortSystemShutdownA",
    "AbortSystemShutdownW",
    "CheckForHiberboot",
    "EWX_HYBRID_SHUTDOWN",
    "EWX_LOGOFF",
    "EWX_POWEROFF",
    "EWX_REBOOT",
    "EWX_RESTARTAPPS",
    "EWX_SHUTDOWN",
    "EXIT_WINDOWS_FLAGS",
    "ExitWindowsEx",
    "InitiateShutdownA",
    "InitiateShutdownW",
    "InitiateSystemShutdownA",
    "InitiateSystemShutdownExA",
    "InitiateSystemShutdownExW",
    "InitiateSystemShutdownW",
    "LockWorkStation",
    "MAX_NUM_REASONS",
    "MAX_REASON_BUGID_LEN",
    "MAX_REASON_COMMENT_LEN",
    "MAX_REASON_DESC_LEN",
    "MAX_REASON_NAME_LEN",
    "POLICY_SHOWREASONUI_ALWAYS",
    "POLICY_SHOWREASONUI_NEVER",
    "POLICY_SHOWREASONUI_SERVERONLY",
    "POLICY_SHOWREASONUI_WORKSTATIONONLY",
    "SHTDN_REASON_FLAG_CLEAN_UI",
    "SHTDN_REASON_FLAG_COMMENT_REQUIRED",
    "SHTDN_REASON_FLAG_DIRTY_PROBLEM_ID_REQUIRED",
    "SHTDN_REASON_FLAG_DIRTY_UI",
    "SHTDN_REASON_FLAG_MOBILE_UI_RESERVED",
    "SHTDN_REASON_FLAG_PLANNED",
    "SHTDN_REASON_FLAG_USER_DEFINED",
    "SHTDN_REASON_LEGACY_API",
    "SHTDN_REASON_MAJOR_APPLICATION",
    "SHTDN_REASON_MAJOR_HARDWARE",
    "SHTDN_REASON_MAJOR_LEGACY_API",
    "SHTDN_REASON_MAJOR_NONE",
    "SHTDN_REASON_MAJOR_OPERATINGSYSTEM",
    "SHTDN_REASON_MAJOR_OTHER",
    "SHTDN_REASON_MAJOR_POWER",
    "SHTDN_REASON_MAJOR_SOFTWARE",
    "SHTDN_REASON_MAJOR_SYSTEM",
    "SHTDN_REASON_MINOR_BLUESCREEN",
    "SHTDN_REASON_MINOR_CORDUNPLUGGED",
    "SHTDN_REASON_MINOR_DC_DEMOTION",
    "SHTDN_REASON_MINOR_DC_PROMOTION",
    "SHTDN_REASON_MINOR_DISK",
    "SHTDN_REASON_MINOR_ENVIRONMENT",
    "SHTDN_REASON_MINOR_HARDWARE_DRIVER",
    "SHTDN_REASON_MINOR_HOTFIX",
    "SHTDN_REASON_MINOR_HOTFIX_UNINSTALL",
    "SHTDN_REASON_MINOR_HUNG",
    "SHTDN_REASON_MINOR_INSTALLATION",
    "SHTDN_REASON_MINOR_MAINTENANCE",
    "SHTDN_REASON_MINOR_MMC",
    "SHTDN_REASON_MINOR_NETWORKCARD",
    "SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY",
    "SHTDN_REASON_MINOR_NONE",
    "SHTDN_REASON_MINOR_OTHER",
    "SHTDN_REASON_MINOR_OTHERDRIVER",
    "SHTDN_REASON_MINOR_POWER_SUPPLY",
    "SHTDN_REASON_MINOR_PROCESSOR",
    "SHTDN_REASON_MINOR_RECONFIG",
    "SHTDN_REASON_MINOR_SECURITY",
    "SHTDN_REASON_MINOR_SECURITYFIX",
    "SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL",
    "SHTDN_REASON_MINOR_SERVICEPACK",
    "SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL",
    "SHTDN_REASON_MINOR_SYSTEMRESTORE",
    "SHTDN_REASON_MINOR_TERMSRV",
    "SHTDN_REASON_MINOR_UNSTABLE",
    "SHTDN_REASON_MINOR_UPGRADE",
    "SHTDN_REASON_MINOR_WMI",
    "SHTDN_REASON_NONE",
    "SHTDN_REASON_UNKNOWN",
    "SHTDN_REASON_VALID_BIT_MASK",
    "SHUTDOWN_ARSO",
    "SHUTDOWN_CHECK_SAFE_FOR_SERVER",
    "SHUTDOWN_FLAGS",
    "SHUTDOWN_FORCE_OTHERS",
    "SHUTDOWN_FORCE_SELF",
    "SHUTDOWN_GRACE_OVERRIDE",
    "SHUTDOWN_HYBRID",
    "SHUTDOWN_INSTALL_UPDATES",
    "SHUTDOWN_MOBILE_UI",
    "SHUTDOWN_NOREBOOT",
    "SHUTDOWN_POWEROFF",
    "SHUTDOWN_REASON",
    "SHUTDOWN_RESTART",
    "SHUTDOWN_RESTARTAPPS",
    "SHUTDOWN_RESTART_BOOTOPTIONS",
    "SHUTDOWN_SKIP_SVC_PRESHUTDOWN",
    "SHUTDOWN_SOFT_REBOOT",
    "SHUTDOWN_SYSTEM_INITIATED",
    "SHUTDOWN_TYPE_LEN",
    "SHUTDOWN_VAIL_CONTAINER",
    "SNAPSHOT_POLICY_ALWAYS",
    "SNAPSHOT_POLICY_NEVER",
    "SNAPSHOT_POLICY_UNPLANNED",
    "ShutdownBlockReasonCreate",
    "ShutdownBlockReasonDestroy",
    "ShutdownBlockReasonQuery",
]