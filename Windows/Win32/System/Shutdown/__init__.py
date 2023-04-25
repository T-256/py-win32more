from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Shutdown
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
MAX_REASON_NAME_LEN: UInt32 = 64
MAX_REASON_DESC_LEN: UInt32 = 256
MAX_REASON_BUGID_LEN: UInt32 = 32
MAX_REASON_COMMENT_LEN: UInt32 = 512
SHUTDOWN_TYPE_LEN: UInt32 = 32
POLICY_SHOWREASONUI_NEVER: UInt32 = 0
POLICY_SHOWREASONUI_ALWAYS: UInt32 = 1
POLICY_SHOWREASONUI_WORKSTATIONONLY: UInt32 = 2
POLICY_SHOWREASONUI_SERVERONLY: UInt32 = 3
SNAPSHOT_POLICY_NEVER: UInt32 = 0
SNAPSHOT_POLICY_ALWAYS: UInt32 = 1
SNAPSHOT_POLICY_UNPLANNED: UInt32 = 2
MAX_NUM_REASONS: UInt32 = 256
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownA(lpMachineName: Windows.Win32.Foundation.PSTR, lpMessage: Windows.Win32.Foundation.PSTR, dwTimeout: UInt32, bForceAppsClosed: Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownW(lpMachineName: Windows.Win32.Foundation.PWSTR, lpMessage: Windows.Win32.Foundation.PWSTR, dwTimeout: UInt32, bForceAppsClosed: Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AbortSystemShutdownA(lpMachineName: Windows.Win32.Foundation.PSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def AbortSystemShutdownW(lpMachineName: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownExA(lpMachineName: Windows.Win32.Foundation.PSTR, lpMessage: Windows.Win32.Foundation.PSTR, dwTimeout: UInt32, bForceAppsClosed: Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: Windows.Win32.Foundation.BOOL, dwReason: Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateSystemShutdownExW(lpMachineName: Windows.Win32.Foundation.PWSTR, lpMessage: Windows.Win32.Foundation.PWSTR, dwTimeout: UInt32, bForceAppsClosed: Windows.Win32.Foundation.BOOL, bRebootAfterShutdown: Windows.Win32.Foundation.BOOL, dwReason: Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('ADVAPI32.dll')
def InitiateShutdownA(lpMachineName: Windows.Win32.Foundation.PSTR, lpMessage: Windows.Win32.Foundation.PSTR, dwGracePeriod: UInt32, dwShutdownFlags: Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS, dwReason: Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def InitiateShutdownW(lpMachineName: Windows.Win32.Foundation.PWSTR, lpMessage: Windows.Win32.Foundation.PWSTR, dwGracePeriod: UInt32, dwShutdownFlags: Windows.Win32.System.Shutdown.SHUTDOWN_FLAGS, dwReason: Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> UInt32: ...
@winfunctype('ADVAPI32.dll')
def CheckForHiberboot(pHiberboot: POINTER(Windows.Win32.Foundation.BOOLEAN), bClearFlag: Windows.Win32.Foundation.BOOLEAN) -> UInt32: ...
@winfunctype('USER32.dll')
def ExitWindowsEx(uFlags: Windows.Win32.System.Shutdown.EXIT_WINDOWS_FLAGS, dwReason: Windows.Win32.System.Shutdown.SHUTDOWN_REASON) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def LockWorkStation() -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonCreate(hWnd: Windows.Win32.Foundation.HWND, pwszReason: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonQuery(hWnd: Windows.Win32.Foundation.HWND, pwszBuff: Windows.Win32.Foundation.PWSTR, pcchBuff: POINTER(UInt32)) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('USER32.dll')
def ShutdownBlockReasonDestroy(hWnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.BOOL: ...
EXIT_WINDOWS_FLAGS = UInt32
EWX_HYBRID_SHUTDOWN: EXIT_WINDOWS_FLAGS = 4194304
EWX_LOGOFF: EXIT_WINDOWS_FLAGS = 0
EWX_POWEROFF: EXIT_WINDOWS_FLAGS = 8
EWX_REBOOT: EXIT_WINDOWS_FLAGS = 2
EWX_RESTARTAPPS: EXIT_WINDOWS_FLAGS = 64
EWX_SHUTDOWN: EXIT_WINDOWS_FLAGS = 1
SHUTDOWN_FLAGS = UInt32
SHUTDOWN_FORCE_OTHERS: SHUTDOWN_FLAGS = 1
SHUTDOWN_FORCE_SELF: SHUTDOWN_FLAGS = 2
SHUTDOWN_RESTART: SHUTDOWN_FLAGS = 4
SHUTDOWN_POWEROFF: SHUTDOWN_FLAGS = 8
SHUTDOWN_NOREBOOT: SHUTDOWN_FLAGS = 16
SHUTDOWN_GRACE_OVERRIDE: SHUTDOWN_FLAGS = 32
SHUTDOWN_INSTALL_UPDATES: SHUTDOWN_FLAGS = 64
SHUTDOWN_RESTARTAPPS: SHUTDOWN_FLAGS = 128
SHUTDOWN_SKIP_SVC_PRESHUTDOWN: SHUTDOWN_FLAGS = 256
SHUTDOWN_HYBRID: SHUTDOWN_FLAGS = 512
SHUTDOWN_RESTART_BOOTOPTIONS: SHUTDOWN_FLAGS = 1024
SHUTDOWN_SOFT_REBOOT: SHUTDOWN_FLAGS = 2048
SHUTDOWN_MOBILE_UI: SHUTDOWN_FLAGS = 4096
SHUTDOWN_ARSO: SHUTDOWN_FLAGS = 8192
SHUTDOWN_CHECK_SAFE_FOR_SERVER: SHUTDOWN_FLAGS = 16384
SHUTDOWN_VAIL_CONTAINER: SHUTDOWN_FLAGS = 32768
SHUTDOWN_SYSTEM_INITIATED: SHUTDOWN_FLAGS = 65536
SHUTDOWN_REASON = UInt32
SHTDN_REASON_NONE: SHUTDOWN_REASON = 0
SHTDN_REASON_FLAG_COMMENT_REQUIRED: SHUTDOWN_REASON = 16777216
SHTDN_REASON_FLAG_DIRTY_PROBLEM_ID_REQUIRED: SHUTDOWN_REASON = 33554432
SHTDN_REASON_FLAG_CLEAN_UI: SHUTDOWN_REASON = 67108864
SHTDN_REASON_FLAG_DIRTY_UI: SHUTDOWN_REASON = 134217728
SHTDN_REASON_FLAG_MOBILE_UI_RESERVED: SHUTDOWN_REASON = 268435456
SHTDN_REASON_FLAG_USER_DEFINED: SHUTDOWN_REASON = 1073741824
SHTDN_REASON_FLAG_PLANNED: SHUTDOWN_REASON = 2147483648
SHTDN_REASON_MAJOR_OTHER: SHUTDOWN_REASON = 0
SHTDN_REASON_MAJOR_NONE: SHUTDOWN_REASON = 0
SHTDN_REASON_MAJOR_HARDWARE: SHUTDOWN_REASON = 65536
SHTDN_REASON_MAJOR_OPERATINGSYSTEM: SHUTDOWN_REASON = 131072
SHTDN_REASON_MAJOR_SOFTWARE: SHUTDOWN_REASON = 196608
SHTDN_REASON_MAJOR_APPLICATION: SHUTDOWN_REASON = 262144
SHTDN_REASON_MAJOR_SYSTEM: SHUTDOWN_REASON = 327680
SHTDN_REASON_MAJOR_POWER: SHUTDOWN_REASON = 393216
SHTDN_REASON_MAJOR_LEGACY_API: SHUTDOWN_REASON = 458752
SHTDN_REASON_MINOR_OTHER: SHUTDOWN_REASON = 0
SHTDN_REASON_MINOR_NONE: SHUTDOWN_REASON = 255
SHTDN_REASON_MINOR_MAINTENANCE: SHUTDOWN_REASON = 1
SHTDN_REASON_MINOR_INSTALLATION: SHUTDOWN_REASON = 2
SHTDN_REASON_MINOR_UPGRADE: SHUTDOWN_REASON = 3
SHTDN_REASON_MINOR_RECONFIG: SHUTDOWN_REASON = 4
SHTDN_REASON_MINOR_HUNG: SHUTDOWN_REASON = 5
SHTDN_REASON_MINOR_UNSTABLE: SHUTDOWN_REASON = 6
SHTDN_REASON_MINOR_DISK: SHUTDOWN_REASON = 7
SHTDN_REASON_MINOR_PROCESSOR: SHUTDOWN_REASON = 8
SHTDN_REASON_MINOR_NETWORKCARD: SHUTDOWN_REASON = 9
SHTDN_REASON_MINOR_POWER_SUPPLY: SHUTDOWN_REASON = 10
SHTDN_REASON_MINOR_CORDUNPLUGGED: SHUTDOWN_REASON = 11
SHTDN_REASON_MINOR_ENVIRONMENT: SHUTDOWN_REASON = 12
SHTDN_REASON_MINOR_HARDWARE_DRIVER: SHUTDOWN_REASON = 13
SHTDN_REASON_MINOR_OTHERDRIVER: SHUTDOWN_REASON = 14
SHTDN_REASON_MINOR_BLUESCREEN: SHUTDOWN_REASON = 15
SHTDN_REASON_MINOR_SERVICEPACK: SHUTDOWN_REASON = 16
SHTDN_REASON_MINOR_HOTFIX: SHUTDOWN_REASON = 17
SHTDN_REASON_MINOR_SECURITYFIX: SHUTDOWN_REASON = 18
SHTDN_REASON_MINOR_SECURITY: SHUTDOWN_REASON = 19
SHTDN_REASON_MINOR_NETWORK_CONNECTIVITY: SHUTDOWN_REASON = 20
SHTDN_REASON_MINOR_WMI: SHUTDOWN_REASON = 21
SHTDN_REASON_MINOR_SERVICEPACK_UNINSTALL: SHUTDOWN_REASON = 22
SHTDN_REASON_MINOR_HOTFIX_UNINSTALL: SHUTDOWN_REASON = 23
SHTDN_REASON_MINOR_SECURITYFIX_UNINSTALL: SHUTDOWN_REASON = 24
SHTDN_REASON_MINOR_MMC: SHUTDOWN_REASON = 25
SHTDN_REASON_MINOR_SYSTEMRESTORE: SHUTDOWN_REASON = 26
SHTDN_REASON_MINOR_TERMSRV: SHUTDOWN_REASON = 32
SHTDN_REASON_MINOR_DC_PROMOTION: SHUTDOWN_REASON = 33
SHTDN_REASON_MINOR_DC_DEMOTION: SHUTDOWN_REASON = 34
SHTDN_REASON_UNKNOWN: SHUTDOWN_REASON = 255
SHTDN_REASON_LEGACY_API: SHUTDOWN_REASON = 2147942400
SHTDN_REASON_VALID_BIT_MASK: SHUTDOWN_REASON = 3238002687
