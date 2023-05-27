from __future__ import annotations
from ctypes import POINTER
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, SByte, SUCCEEDED, Single, String, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_head, press, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Com
import win32more.Windows.Win32.System.RemoteAssistance
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
DISPID_EVENT_ON_STATE_CHANGED: UInt32 = 5
DISPID_EVENT_ON_TERMINATION: UInt32 = 6
DISPID_EVENT_ON_CONTEXT_DATA: UInt32 = 7
DISPID_EVENT_ON_SEND_ERROR: UInt32 = 8
class DRendezvousSessionEvents(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IDispatch
    _iid_ = Guid('{3fa19cf8-64c4-4f53-ae60-635b3806eca6}')
class IRendezvousApplication(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{4f4d070b-a275-49fb-b10d-8ec26387b50d}')
    @commethod(3)
    def SetRendezvousSession(self, pRendezvousSession: win32more.Windows.Win32.System.Com.IUnknown_head) -> win32more.Windows.Win32.Foundation.HRESULT: ...
class IRendezvousSession(ComPtr):
    extends: win32more.Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('{9ba4b1dd-8b0c-48b7-9e7c-2f25857c8df5}')
    @commethod(3)
    def get_State(self, pSessionState: POINTER(win32more.Windows.Win32.System.RemoteAssistance.RENDEZVOUS_SESSION_STATE)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_RemoteUser(self, bstrUserName: POINTER(win32more.Windows.Win32.Foundation.BSTR)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_Flags(self, pFlags: POINTER(Int32)) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendContextData(self, bstrData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Terminate(self, hr: win32more.Windows.Win32.Foundation.HRESULT, bstrAppData: win32more.Windows.Win32.Foundation.BSTR) -> win32more.Windows.Win32.Foundation.HRESULT: ...
RENDEZVOUS_SESSION_FLAGS = Int32
RSF_NONE: RENDEZVOUS_SESSION_FLAGS = 0
RSF_INVITER: RENDEZVOUS_SESSION_FLAGS = 1
RSF_INVITEE: RENDEZVOUS_SESSION_FLAGS = 2
RSF_ORIGINAL_INVITER: RENDEZVOUS_SESSION_FLAGS = 4
RSF_REMOTE_LEGACYSESSION: RENDEZVOUS_SESSION_FLAGS = 8
RSF_REMOTE_WIN7SESSION: RENDEZVOUS_SESSION_FLAGS = 16
RENDEZVOUS_SESSION_STATE = Int32
RSS_UNKNOWN: RENDEZVOUS_SESSION_STATE = 0
RSS_READY: RENDEZVOUS_SESSION_STATE = 1
RSS_INVITATION: RENDEZVOUS_SESSION_STATE = 2
RSS_ACCEPTED: RENDEZVOUS_SESSION_STATE = 3
RSS_CONNECTED: RENDEZVOUS_SESSION_STATE = 4
RSS_CANCELLED: RENDEZVOUS_SESSION_STATE = 5
RSS_DECLINED: RENDEZVOUS_SESSION_STATE = 6
RSS_TERMINATED: RENDEZVOUS_SESSION_STATE = 7
RendezvousApplication = Guid('{0b7e019a-b5de-47fa-8966-9082f82fb192}')
make_head(_module, 'DRendezvousSessionEvents')
make_head(_module, 'IRendezvousApplication')
make_head(_module, 'IRendezvousSession')