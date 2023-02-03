from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Devices.SerialCommunication
import Windows.Win32.Foundation
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
COMDB_MIN_PORTS_ARBITRATED: UInt32 = 256
COMDB_MAX_PORTS_ARBITRATED: UInt32 = 4096
CDB_REPORT_BITS: UInt32 = 0
CDB_REPORT_BYTES: UInt32 = 1
@winfunctype('MSPORTS.dll')
def ComDBOpen(PHComDB: POINTER(IntPtr)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClose(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBGetCurrentPortUsage(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB, Buffer: c_char_p_no, BufferSize: UInt32, ReportType: UInt32, MaxPortsReported: POINTER(UInt32)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClaimNextFreePort(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: POINTER(UInt32)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBClaimPort(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: UInt32, ForceClaim: Windows.Win32.Foundation.BOOL, Forced: POINTER(Windows.Win32.Foundation.BOOL)) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBReleasePort(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB, ComNumber: UInt32) -> Int32: ...
@winfunctype('MSPORTS.dll')
def ComDBResizeDatabase(HComDB: Windows.Win32.Devices.SerialCommunication.HCOMDB, NewSize: UInt32) -> Int32: ...
HCOMDB = IntPtr
__all__ = [
    "CDB_REPORT_BITS",
    "CDB_REPORT_BYTES",
    "COMDB_MAX_PORTS_ARBITRATED",
    "COMDB_MIN_PORTS_ARBITRATED",
    "ComDBClaimNextFreePort",
    "ComDBClaimPort",
    "ComDBClose",
    "ComDBGetCurrentPortUsage",
    "ComDBOpen",
    "ComDBReleasePort",
    "ComDBResizeDatabase",
    "HCOMDB",
]
_arch_optional = [
]