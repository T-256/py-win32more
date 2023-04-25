from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.DesktopSharing
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
ATTENDEE_DISCONNECT_REASON = Int32
ATTENDEE_DISCONNECT_REASON_MIN: ATTENDEE_DISCONNECT_REASON = 0
ATTENDEE_DISCONNECT_REASON_APP: ATTENDEE_DISCONNECT_REASON = 0
ATTENDEE_DISCONNECT_REASON_ERR: ATTENDEE_DISCONNECT_REASON = 1
ATTENDEE_DISCONNECT_REASON_CLI: ATTENDEE_DISCONNECT_REASON = 2
ATTENDEE_DISCONNECT_REASON_MAX: ATTENDEE_DISCONNECT_REASON = 2
DISPID_RDPSRAPI_METHOD_OPEN: UInt32 = 100
DISPID_RDPSRAPI_METHOD_CLOSE: UInt32 = 101
DISPID_RDPSRAPI_METHOD_SETSHAREDRECT: UInt32 = 102
DISPID_RDPSRAPI_METHOD_GETSHAREDRECT: UInt32 = 103
DISPID_RDPSRAPI_METHOD_VIEWERCONNECT: UInt32 = 104
DISPID_RDPSRAPI_METHOD_VIEWERDISCONNECT: UInt32 = 105
DISPID_RDPSRAPI_METHOD_TERMINATE_CONNECTION: UInt32 = 106
DISPID_RDPSRAPI_METHOD_CREATE_INVITATION: UInt32 = 107
DISPID_RDPSRAPI_METHOD_REQUEST_CONTROL: UInt32 = 108
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_CREATE: UInt32 = 109
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SEND_DATA: UInt32 = 110
DISPID_RDPSRAPI_METHOD_VIRTUAL_CHANNEL_SET_ACCESS: UInt32 = 111
DISPID_RDPSRAPI_METHOD_PAUSE: UInt32 = 112
DISPID_RDPSRAPI_METHOD_RESUME: UInt32 = 113
DISPID_RDPSRAPI_METHOD_SHOW_WINDOW: UInt32 = 114
DISPID_RDPSRAPI_METHOD_REQUEST_COLOR_DEPTH_CHANGE: UInt32 = 115
DISPID_RDPSRAPI_METHOD_STARTREVCONNECTLISTENER: UInt32 = 116
DISPID_RDPSRAPI_METHOD_CONNECTTOCLIENT: UInt32 = 117
DISPID_RDPSRAPI_METHOD_SET_RENDERING_SURFACE: UInt32 = 118
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_BUTTON_EVENT: UInt32 = 119
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_MOVE_EVENT: UInt32 = 120
DISPID_RDPSRAPI_METHOD_SEND_MOUSE_WHEEL_EVENT: UInt32 = 121
DISPID_RDPSRAPI_METHOD_SEND_KEYBOARD_EVENT: UInt32 = 122
DISPID_RDPSRAPI_METHOD_SEND_SYNC_EVENT: UInt32 = 123
DISPID_RDPSRAPI_METHOD_BEGIN_TOUCH_FRAME: UInt32 = 124
DISPID_RDPSRAPI_METHOD_ADD_TOUCH_INPUT: UInt32 = 125
DISPID_RDPSRAPI_METHOD_END_TOUCH_FRAME: UInt32 = 126
DISPID_RDPSRAPI_METHOD_CONNECTUSINGTRANSPORTSTREAM: UInt32 = 127
DISPID_RDPSRAPI_METHOD_SENDCONTROLLEVELCHANGERESPONSE: UInt32 = 148
DISPID_RDPSRAPI_METHOD_GETFRAMEBUFFERBITS: UInt32 = 149
DISPID_RDPSRAPI_PROP_DISPIDVALUE: UInt32 = 200
DISPID_RDPSRAPI_PROP_ID: UInt32 = 201
DISPID_RDPSRAPI_PROP_SESSION_PROPERTIES: UInt32 = 202
DISPID_RDPSRAPI_PROP_ATTENDEES: UInt32 = 203
DISPID_RDPSRAPI_PROP_INVITATIONS: UInt32 = 204
DISPID_RDPSRAPI_PROP_INVITATION: UInt32 = 205
DISPID_RDPSRAPI_PROP_CHANNELMANAGER: UInt32 = 206
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETNAME: UInt32 = 207
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETFLAGS: UInt32 = 208
DISPID_RDPSRAPI_PROP_VIRTUAL_CHANNEL_GETPRIORITY: UInt32 = 209
DISPID_RDPSRAPI_PROP_WINDOWID: UInt32 = 210
DISPID_RDPSRAPI_PROP_APPLICATION: UInt32 = 211
DISPID_RDPSRAPI_PROP_WINDOWSHARED: UInt32 = 212
DISPID_RDPSRAPI_PROP_WINDOWNAME: UInt32 = 213
DISPID_RDPSRAPI_PROP_APPNAME: UInt32 = 214
DISPID_RDPSRAPI_PROP_APPLICATION_FILTER: UInt32 = 215
DISPID_RDPSRAPI_PROP_WINDOW_LIST: UInt32 = 216
DISPID_RDPSRAPI_PROP_APPLICATION_LIST: UInt32 = 217
DISPID_RDPSRAPI_PROP_APPFILTER_ENABLED: UInt32 = 218
DISPID_RDPSRAPI_PROP_APPFILTERENABLED: UInt32 = 219
DISPID_RDPSRAPI_PROP_SHARED: UInt32 = 220
DISPID_RDPSRAPI_PROP_INVITATIONITEM: UInt32 = 221
DISPID_RDPSRAPI_PROP_DBG_CLX_CMDLINE: UInt32 = 222
DISPID_RDPSRAPI_PROP_APPFLAGS: UInt32 = 223
DISPID_RDPSRAPI_PROP_WNDFLAGS: UInt32 = 224
DISPID_RDPSRAPI_PROP_PROTOCOL_TYPE: UInt32 = 225
DISPID_RDPSRAPI_PROP_LOCAL_PORT: UInt32 = 226
DISPID_RDPSRAPI_PROP_LOCAL_IP: UInt32 = 227
DISPID_RDPSRAPI_PROP_PEER_PORT: UInt32 = 228
DISPID_RDPSRAPI_PROP_PEER_IP: UInt32 = 229
DISPID_RDPSRAPI_PROP_ATTENDEE_FLAGS: UInt32 = 230
DISPID_RDPSRAPI_PROP_CONINFO: UInt32 = 231
DISPID_RDPSRAPI_PROP_CONNECTION_STRING: UInt32 = 232
DISPID_RDPSRAPI_PROP_GROUP_NAME: UInt32 = 233
DISPID_RDPSRAPI_PROP_PASSWORD: UInt32 = 234
DISPID_RDPSRAPI_PROP_ATTENDEELIMIT: UInt32 = 235
DISPID_RDPSRAPI_PROP_REVOKED: UInt32 = 236
DISPID_RDPSRAPI_PROP_DISCONNECTED_STRING: UInt32 = 237
DISPID_RDPSRAPI_PROP_USESMARTSIZING: UInt32 = 238
DISPID_RDPSRAPI_PROP_SESSION_COLORDEPTH: UInt32 = 239
DISPID_RDPSRAPI_PROP_REASON: UInt32 = 240
DISPID_RDPSRAPI_PROP_CODE: UInt32 = 241
DISPID_RDPSRAPI_PROP_CTRL_LEVEL: UInt32 = 242
DISPID_RDPSRAPI_PROP_REMOTENAME: UInt32 = 243
DISPID_RDPSRAPI_PROP_COUNT: UInt32 = 244
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_HEIGHT: UInt32 = 251
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_WIDTH: UInt32 = 252
DISPID_RDPSRAPI_PROP_FRAMEBUFFER_BPP: UInt32 = 253
DISPID_RDPSRAPI_PROP_FRAMEBUFFER: UInt32 = 254
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_CONNECTED: UInt32 = 301
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_DISCONNECTED: UInt32 = 302
DISPID_RDPSRAPI_EVENT_ON_ATTENDEE_UPDATE: UInt32 = 303
DISPID_RDPSRAPI_EVENT_ON_ERROR: UInt32 = 304
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTED: UInt32 = 305
DISPID_RDPSRAPI_EVENT_ON_VIEWER_DISCONNECTED: UInt32 = 306
DISPID_RDPSRAPI_EVENT_ON_VIEWER_AUTHENTICATED: UInt32 = 307
DISPID_RDPSRAPI_EVENT_ON_VIEWER_CONNECTFAILED: UInt32 = 308
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_REQUEST: UInt32 = 309
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_PAUSED: UInt32 = 310
DISPID_RDPSRAPI_EVENT_ON_GRAPHICS_STREAM_RESUMED: UInt32 = 311
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_JOIN: UInt32 = 312
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_LEAVE: UInt32 = 313
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_DATARECEIVED: UInt32 = 314
DISPID_RDPSRAPI_EVENT_ON_VIRTUAL_CHANNEL_SENDCOMPLETED: UInt32 = 315
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_OPEN: UInt32 = 316
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_CLOSE: UInt32 = 317
DISPID_RDPSRAPI_EVENT_ON_APPLICATION_UPDATE: UInt32 = 318
DISPID_RDPSRAPI_EVENT_ON_WINDOW_OPEN: UInt32 = 319
DISPID_RDPSRAPI_EVENT_ON_WINDOW_CLOSE: UInt32 = 320
DISPID_RDPSRAPI_EVENT_ON_WINDOW_UPDATE: UInt32 = 321
DISPID_RDPSRAPI_EVENT_ON_APPFILTER_UPDATE: UInt32 = 322
DISPID_RDPSRAPI_EVENT_ON_SHARED_RECT_CHANGED: UInt32 = 323
DISPID_RDPSRAPI_EVENT_ON_FOCUSRELEASED: UInt32 = 324
DISPID_RDPSRAPI_EVENT_ON_SHARED_DESKTOP_SETTINGS_CHANGED: UInt32 = 325
DISPID_RDPSRAPI_EVENT_ON_CTRLLEVEL_CHANGE_RESPONSE: UInt32 = 338
DISPID_RDPAPI_EVENT_ON_BOUNDING_RECT_CHANGED: UInt32 = 340
DISPID_RDPSRAPI_METHOD_STREAM_ALLOCBUFFER: UInt32 = 421
DISPID_RDPSRAPI_METHOD_STREAM_FREEBUFFER: UInt32 = 422
DISPID_RDPSRAPI_METHOD_STREAMSENDDATA: UInt32 = 423
DISPID_RDPSRAPI_METHOD_STREAMREADDATA: UInt32 = 424
DISPID_RDPSRAPI_METHOD_STREAMOPEN: UInt32 = 425
DISPID_RDPSRAPI_METHOD_STREAMCLOSE: UInt32 = 426
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORAGE: UInt32 = 555
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADSIZE: UInt32 = 558
DISPID_RDPSRAPI_PROP_STREAMBUFFER_PAYLOADOFFSET: UInt32 = 559
DISPID_RDPSRAPI_PROP_STREAMBUFFER_CONTEXT: UInt32 = 560
DISPID_RDPSRAPI_PROP_STREAMBUFFER_FLAGS: UInt32 = 561
DISPID_RDPSRAPI_PROP_STREAMBUFFER_STORESIZE: UInt32 = 562
DISPID_RDPSRAPI_EVENT_ON_STREAM_SENDCOMPLETED: UInt32 = 632
DISPID_RDPSRAPI_EVENT_ON_STREAM_DATARECEIVED: UInt32 = 633
DISPID_RDPSRAPI_EVENT_ON_STREAM_CLOSED: UInt32 = 634
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_BUTTON_RECEIVED: UInt32 = 700
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_MOVE_RECEIVED: UInt32 = 701
DISPID_RDPSRAPI_EVENT_VIEW_MOUSE_WHEEL_RECEIVED: UInt32 = 702
CHANNEL_ACCESS_ENUM = Int32
CHANNEL_ACCESS_ENUM_NONE: CHANNEL_ACCESS_ENUM = 0
CHANNEL_ACCESS_ENUM_SENDRECEIVE: CHANNEL_ACCESS_ENUM = 1
CHANNEL_FLAGS = Int32
CHANNEL_FLAGS_LEGACY: CHANNEL_FLAGS = 1
CHANNEL_FLAGS_UNCOMPRESSED: CHANNEL_FLAGS = 2
CHANNEL_FLAGS_DYNAMIC: CHANNEL_FLAGS = 4
CHANNEL_PRIORITY = Int32
CHANNEL_PRIORITY_LO: CHANNEL_PRIORITY = 0
CHANNEL_PRIORITY_MED: CHANNEL_PRIORITY = 1
CHANNEL_PRIORITY_HI: CHANNEL_PRIORITY = 2
CTRL_LEVEL = Int32
CTRL_LEVEL_MIN: CTRL_LEVEL = 0
CTRL_LEVEL_INVALID: CTRL_LEVEL = 0
CTRL_LEVEL_NONE: CTRL_LEVEL = 1
CTRL_LEVEL_VIEW: CTRL_LEVEL = 2
CTRL_LEVEL_INTERACTIVE: CTRL_LEVEL = 3
CTRL_LEVEL_REQCTRL_VIEW: CTRL_LEVEL = 4
CTRL_LEVEL_REQCTRL_INTERACTIVE: CTRL_LEVEL = 5
CTRL_LEVEL_MAX: CTRL_LEVEL = 5
class IRDPSRAPIApplication(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('41e7a09d-eb7a-436e-93-5d-78-0c-a2-62-83-24')
    @commethod(7)
    def get_Windows(self, pWindowList: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIWindowList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Shared(self, pRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Shared(self, NewVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Flags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIApplicationFilter(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d20f10ca-6637-4f06-b1-d5-27-7e-a7-e5-16-0d')
    @commethod(7)
    def get_Applications(self, pApplications: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Windows(self, pWindows: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIWindowList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Enabled(self, pRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Enabled(self, NewVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIApplicationList(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d4b4aeb3-22dc-4837-b3-b6-42-ea-25-17-84-9a')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Int32, pApplication: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendee(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ec0671b3-1b78-4b80-a4-64-91-32-24-75-43-e3')
    @commethod(7)
    def get_Id(self, pId: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_RemoteName(self, pVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ControlLevel(self, pVal: POINTER(Windows.Win32.System.DesktopSharing.CTRL_LEVEL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_ControlLevel(self, pNewVal: Windows.Win32.System.DesktopSharing.CTRL_LEVEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Invitation(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def TerminateConnection(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Flags(self, plFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ConnectivityInfo(self, ppVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendeeDisconnectInfo(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c187689f-447c-44a1-9c-14-ff-fb-b3-b7-ec-17')
    @commethod(7)
    def get_Attendee(self, retval: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Reason(self, pReason: POINTER(Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Code(self, pVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAttendeeManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('ba3a37e8-33da-4749-8d-a0-07-fa-34-da-79-44')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, id: Int32, ppItem: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIAudioStream(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('e3e30ef9-89c6-4541-ba-3b-19-33-6a-c6-d3-1c')
    @commethod(3)
    def Initialize(self, pnPeriodInHundredNsIntervals: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetBuffer(self, ppbData: POINTER(POINTER(Byte)), pcbData: POINTER(UInt32), pTimestamp: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def FreeBuffer(self) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIClipboardUseEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('d559f59a-7a27-4138-87-63-24-7c-e5-f6-59-a8')
    @commethod(3)
    def OnPasteFromClipboard(self, clipboardFormat: UInt32, pAttendee: Windows.Win32.System.Com.IDispatch_head, pRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIDebug(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('aa1e42b5-496d-4ca4-a6-90-34-8d-cb-2e-c4-ad')
    @commethod(3)
    def put_CLXCmdLine(self, CLXCmdLine: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_CLXCmdLine(self, pCLXCmdLine: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIFrameBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3d67e7d2-b27b-448e-81-b3-c6-11-0e-d8-b4-be')
    @commethod(7)
    def get_Width(self, plWidth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Height(self, plHeight: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Bpp(self, plBpp: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetFrameBufferBits(self, x: Int32, y: Int32, Width: Int32, Heigth: Int32, ppBits: POINTER(POINTER(Windows.Win32.System.Com.SAFEARRAY_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIInvitation(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4fac1d43-fc51-45bb-b1-b4-2b-53-aa-56-2f-a3')
    @commethod(7)
    def get_ConnectionString(self, pbstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_GroupName(self, pbstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Password(self, pbstrVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_AttendeeLimit(self, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def put_AttendeeLimit(self, NewVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Revoked(self, pRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_Revoked(self, NewVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIInvitationManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4722b049-92c3-4c2d-8a-65-f7-34-8f-64-4d-cf')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Windows.Win32.System.Com.VARIANT, ppInvitation: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Count(self, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def CreateInvitation(self, bstrAuthString: Windows.Win32.Foundation.BSTR, bstrGroupName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, AttendeeLimit: Int32, ppInvitation: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitation_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIPerfCounterLogger(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('071c2533-0fa4-4e8f-ae-83-9c-10-b4-30-5a-b5')
    @commethod(3)
    def LogValue(self, lValue: Int64) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIPerfCounterLoggingManager(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('9a512c86-ac6e-4a8e-b1-a4-fc-ef-36-3f-6e-64')
    @commethod(3)
    def CreateLogger(self, bstrCounterName: Windows.Win32.Foundation.BSTR, ppLogger: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIPerfCounterLogger_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISessionProperties(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('339b24f2-9bc0-4f16-9a-ac-f1-65-43-3d-13-d4')
    @commethod(7)
    def get_Property(self, PropertyName: Windows.Win32.Foundation.BSTR, pVal: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Property(self, PropertyName: Windows.Win32.Foundation.BSTR, newVal: Windows.Win32.System.Com.VARIANT) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISharingSession(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('eeb20886-e470-4cf6-84-2b-27-39-c0-ec-5c-fb')
    @commethod(7)
    def Open(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_ColorDepth(self, colorDepth: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_ColorDepth(self, pColorDepth: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Properties(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPISessionProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_Attendees(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendeeManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Invitations(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitationManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_ApplicationFilter(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_VirtualChannelManager(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannelManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def Pause(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def Resume(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def ConnectToClient(self, bstrConnectionString: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def SetDesktopSharedRect(self, left: Int32, top: Int32, right: Int32, bottom: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDesktopSharedRect(self, pleft: POINTER(Int32), ptop: POINTER(Int32), pright: POINTER(Int32), pbottom: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPISharingSession2(c_void_p):
    extends: Windows.Win32.System.DesktopSharing.IRDPSRAPISharingSession
    Guid = Guid('fee4ee57-e3e8-4205-8f-b0-8f-d1-d0-67-5c-21')
    @commethod(21)
    def ConnectUsingTransportStream(self, pStream: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStream_head, bstrGroup: Windows.Win32.Foundation.BSTR, bstrAuthenticatedAttendeeName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_FrameBuffer(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIFrameBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def SendControlLevelChangeResponse(self, pAttendee: Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendee_head, RequestedLevel: Windows.Win32.System.DesktopSharing.CTRL_LEVEL, ReasonCode: Int32) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITcpConnectionInfo(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f74049a4-3d06-4028-81-93-0a-8c-29-bc-24-52')
    @commethod(7)
    def get_Protocol(self, plProtocol: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_LocalPort(self, plPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_LocalIP(self, pbsrLocalIP: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_PeerPort(self, plPort: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PeerIP(self, pbstrIP: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStream(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('36cfa065-43bb-4ef7-ae-d7-9b-88-a5-05-30-36')
    @commethod(3)
    def AllocBuffer(self, maxPayload: Int32, ppBuffer: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def FreeBuffer(self, pBuffer: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteBuffer(self, pBuffer: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ReadBuffer(self, pBuffer: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Open(self, pCallbacks: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStreamBuffer(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('81c80290-5085-44b0-b4-60-f8-65-c3-9c-b4-a9')
    @commethod(3)
    def get_Storage(self, ppbStorage: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def get_StorageSize(self, plMaxStore: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def get_PayloadSize(self, plRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def put_PayloadSize(self, lVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def get_PayloadOffset(self, plRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PayloadOffset(self, lRetVal: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Flags(self, plFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Flags(self, lFlags: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Context(self, ppContext: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Context(self, pContext: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPITransportStreamEvents(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('ea81c254-f5af-4e40-98-2e-3e-63-bb-59-52-76')
    @commethod(3)
    def OnWriteCompleted(self, pBuffer: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head) -> Void: ...
    @commethod(4)
    def OnReadCompleted(self, pBuffer: Windows.Win32.System.DesktopSharing.IRDPSRAPITransportStreamBuffer_head) -> Void: ...
    @commethod(5)
    def OnStreamClosed(self, hrReason: Windows.Win32.Foundation.HRESULT) -> Void: ...
class IRDPSRAPIViewer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('c6bfcd38-8ce9-404d-8a-e8-f3-1d-00-c6-5c-b5')
    @commethod(7)
    def Connect(self, bstrConnectionString: Windows.Win32.Foundation.BSTR, bstrName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Attendees(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIAttendeeManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Invitations(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIInvitationManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_ApplicationFilter(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIApplicationFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_VirtualChannelManager(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannelManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def put_SmartSizing(self, vbSmartSizing: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_SmartSizing(self, pvbSmartSizing: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def RequestControl(self, CtrlLevel: Windows.Win32.System.DesktopSharing.CTRL_LEVEL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_DisconnectedText(self, bstrDisconnectedText: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_DisconnectedText(self, pbstrDisconnectedText: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def RequestColorDepthChange(self, Bpp: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Properties(self, ppVal: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPISessionProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def StartReverseConnectListener(self, bstrConnectionString: Windows.Win32.Foundation.BSTR, bstrUserName: Windows.Win32.Foundation.BSTR, bstrPassword: Windows.Win32.Foundation.BSTR, pbstrReverseConnectString: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIVirtualChannel(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('05e12f95-28b3-4c9a-87-80-d0-24-85-74-a1-e0')
    @commethod(7)
    def SendData(self, bstrData: Windows.Win32.Foundation.BSTR, lAttendeeId: Int32, ChannelSendFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetAccess(self, lAttendeeId: Int32, AccessType: Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbstrName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Flags(self, plFlags: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Priority(self, pPriority: POINTER(Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIVirtualChannelManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0d11c661-5d0d-4ee4-89-df-21-66-ae-1f-df-ed')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Windows.Win32.System.Com.VARIANT, pChannel: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannel_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def CreateVirtualChannel(self, bstrChannelName: Windows.Win32.Foundation.BSTR, Priority: Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY, ChannelFlags: UInt32, ppChannel: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIVirtualChannel_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIWindow(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('beafe0f9-c77b-4933-ba-9f-a2-4c-dd-cc-27-cf')
    @commethod(7)
    def get_Id(self, pRetVal: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Application(self, pApplication: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIApplication_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Shared(self, pRetVal: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Shared(self, NewVal: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_Name(self, pRetVal: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Show(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Flags(self, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPSRAPIWindowList(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('8a05ce44-715a-4116-a1-89-a1-18-f3-0a-07-bd')
    @commethod(7)
    def get__NewEnum(self, retval: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, item: Int32, pWindow: POINTER(Windows.Win32.System.DesktopSharing.IRDPSRAPIWindow_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IRDPViewerInputSink(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('bb590853-a6c5-4a7b-8d-d4-76-b6-9e-ea-12-d5')
    @commethod(3)
    def SendMouseButtonEvent(self, buttonType: Windows.Win32.System.DesktopSharing.RDPSRAPI_MOUSE_BUTTON_TYPE, vbButtonDown: Windows.Win32.Foundation.VARIANT_BOOL, xPos: UInt32, yPos: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SendMouseMoveEvent(self, xPos: UInt32, yPos: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SendMouseWheelEvent(self, wheelRotation: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SendKeyboardEvent(self, codeType: Windows.Win32.System.DesktopSharing.RDPSRAPI_KBD_CODE_TYPE, keycode: UInt16, vbKeyUp: Windows.Win32.Foundation.VARIANT_BOOL, vbRepeat: Windows.Win32.Foundation.VARIANT_BOOL, vbExtended: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SendSyncEvent(self, syncFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginTouchFrame(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def AddTouchInput(self, contactId: UInt32, event: UInt32, x: Int32, y: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EndTouchFrame(self) -> Windows.Win32.Foundation.HRESULT: ...
RDPENCOMAPI_ATTENDEE_FLAGS = Int32
ATTENDEE_FLAGS_LOCAL: RDPENCOMAPI_ATTENDEE_FLAGS = 1
RDPENCOMAPI_CONSTANTS = Int32
CONST_MAX_CHANNEL_MESSAGE_SIZE: RDPENCOMAPI_CONSTANTS = 1024
CONST_MAX_CHANNEL_NAME_LEN: RDPENCOMAPI_CONSTANTS = 8
CONST_MAX_LEGACY_CHANNEL_MESSAGE_SIZE: RDPENCOMAPI_CONSTANTS = 409600
CONST_ATTENDEE_ID_EVERYONE: RDPENCOMAPI_CONSTANTS = -1
CONST_ATTENDEE_ID_HOST: RDPENCOMAPI_CONSTANTS = 0
CONST_CONN_INTERVAL: RDPENCOMAPI_CONSTANTS = 50
CONST_ATTENDEE_ID_DEFAULT: RDPENCOMAPI_CONSTANTS = -1
RDPSRAPIApplication = Guid('c116a484-4b25-4b9f-8a-54-b9-34-b0-6e-57-fa')
RDPSRAPIApplicationFilter = Guid('e35ace89-c7e8-427e-a4-f9-b9-da-07-28-26-bd')
RDPSRAPIApplicationList = Guid('9e31c815-7433-4876-97-fb-ed-59-fe-2b-aa-22')
RDPSRAPIAttendee = Guid('74f93bb5-755f-488e-8a-29-23-90-10-8a-ef-55')
RDPSRAPIAttendeeDisconnectInfo = Guid('b47d7250-5bdb-405d-b4-87-ca-ad-9c-56-f4-f8')
RDPSRAPIAttendeeManager = Guid('d7b13a01-f7d4-42a6-85-95-12-fc-8c-24-e8-51')
RDPSRAPIFrameBuffer = Guid('a4f66bcc-538e-4101-95-1d-30-84-7a-db-51-01')
RDPSRAPIInvitation = Guid('49174dc6-0731-4b5e-8e-e1-83-a6-3d-38-68-fa')
RDPSRAPIInvitationManager = Guid('53d9c9db-75ab-4271-94-8a-4c-4e-b3-6a-8f-2b')
RDPSRAPISessionProperties = Guid('dd7594ff-ea2a-4c06-8f-df-13-2d-e4-8b-65-10')
RDPSRAPITcpConnectionInfo = Guid('be49db3f-ebb6-4278-8c-e0-d5-45-58-33-ea-ee')
RDPSRAPIWindow = Guid('03cf46db-ce45-4d36-86-ed-ed-28-b7-43-98-bf')
RDPSRAPIWindowList = Guid('9c21e2b8-5dd4-42cc-81-ba-1c-09-98-52-e6-fa')
RDPSRAPI_APP_FLAGS = Int32
APP_FLAG_PRIVILEGED: RDPSRAPI_APP_FLAGS = 1
RDPSRAPI_KBD_CODE_TYPE = Int32
RDPSRAPI_KBD_CODE_SCANCODE: RDPSRAPI_KBD_CODE_TYPE = 0
RDPSRAPI_KBD_CODE_UNICODE: RDPSRAPI_KBD_CODE_TYPE = 1
RDPSRAPI_KBD_SYNC_FLAG = Int32
RDPSRAPI_KBD_SYNC_FLAG_SCROLL_LOCK: RDPSRAPI_KBD_SYNC_FLAG = 1
RDPSRAPI_KBD_SYNC_FLAG_NUM_LOCK: RDPSRAPI_KBD_SYNC_FLAG = 2
RDPSRAPI_KBD_SYNC_FLAG_CAPS_LOCK: RDPSRAPI_KBD_SYNC_FLAG = 4
RDPSRAPI_KBD_SYNC_FLAG_KANA_LOCK: RDPSRAPI_KBD_SYNC_FLAG = 8
RDPSRAPI_MOUSE_BUTTON_TYPE = Int32
RDPSRAPI_MOUSE_BUTTON_BUTTON1: RDPSRAPI_MOUSE_BUTTON_TYPE = 0
RDPSRAPI_MOUSE_BUTTON_BUTTON2: RDPSRAPI_MOUSE_BUTTON_TYPE = 1
RDPSRAPI_MOUSE_BUTTON_BUTTON3: RDPSRAPI_MOUSE_BUTTON_TYPE = 2
RDPSRAPI_MOUSE_BUTTON_XBUTTON1: RDPSRAPI_MOUSE_BUTTON_TYPE = 3
RDPSRAPI_MOUSE_BUTTON_XBUTTON2: RDPSRAPI_MOUSE_BUTTON_TYPE = 4
RDPSRAPI_MOUSE_BUTTON_XBUTTON3: RDPSRAPI_MOUSE_BUTTON_TYPE = 5
RDPSRAPI_WND_FLAGS = Int32
WND_FLAG_PRIVILEGED: RDPSRAPI_WND_FLAGS = 1
RDPSession = Guid('9b78f0e6-3e05-4a5b-b2-e8-e7-43-a8-95-6b-65')
RDPTransportStreamBuffer = Guid('8d4a1c69-f17f-4549-a6-99-76-1c-6e-6b-5c-0a')
RDPTransportStreamEvents = Guid('31e3ab20-5350-483f-9d-c6-67-48-66-5e-fd-eb')
RDPViewer = Guid('32be5ed2-5c86-480f-a9-14-0f-f8-88-5a-1b-3f')
class _IRDPSessionEvents(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('98a97042-6698-40e9-8e-fd-b3-20-09-90-00-4b')
class __ReferenceRemainingTypes__(EasyCastStructure):
    __ctrlLevel__: Windows.Win32.System.DesktopSharing.CTRL_LEVEL
    __attendeeDisconnectReason__: Windows.Win32.System.DesktopSharing.ATTENDEE_DISCONNECT_REASON
    __channelPriority__: Windows.Win32.System.DesktopSharing.CHANNEL_PRIORITY
    __channelFlags__: Windows.Win32.System.DesktopSharing.CHANNEL_FLAGS
    __channelAccessEnum__: Windows.Win32.System.DesktopSharing.CHANNEL_ACCESS_ENUM
    __rdpencomapiAttendeeFlags__: Windows.Win32.System.DesktopSharing.RDPENCOMAPI_ATTENDEE_FLAGS
    __rdpsrapiWndFlags__: Windows.Win32.System.DesktopSharing.RDPSRAPI_WND_FLAGS
    __rdpsrapiAppFlags__: Windows.Win32.System.DesktopSharing.RDPSRAPI_APP_FLAGS
make_head(_module, 'IRDPSRAPIApplication')
make_head(_module, 'IRDPSRAPIApplicationFilter')
make_head(_module, 'IRDPSRAPIApplicationList')
make_head(_module, 'IRDPSRAPIAttendee')
make_head(_module, 'IRDPSRAPIAttendeeDisconnectInfo')
make_head(_module, 'IRDPSRAPIAttendeeManager')
make_head(_module, 'IRDPSRAPIAudioStream')
make_head(_module, 'IRDPSRAPIClipboardUseEvents')
make_head(_module, 'IRDPSRAPIDebug')
make_head(_module, 'IRDPSRAPIFrameBuffer')
make_head(_module, 'IRDPSRAPIInvitation')
make_head(_module, 'IRDPSRAPIInvitationManager')
make_head(_module, 'IRDPSRAPIPerfCounterLogger')
make_head(_module, 'IRDPSRAPIPerfCounterLoggingManager')
make_head(_module, 'IRDPSRAPISessionProperties')
make_head(_module, 'IRDPSRAPISharingSession')
make_head(_module, 'IRDPSRAPISharingSession2')
make_head(_module, 'IRDPSRAPITcpConnectionInfo')
make_head(_module, 'IRDPSRAPITransportStream')
make_head(_module, 'IRDPSRAPITransportStreamBuffer')
make_head(_module, 'IRDPSRAPITransportStreamEvents')
make_head(_module, 'IRDPSRAPIViewer')
make_head(_module, 'IRDPSRAPIVirtualChannel')
make_head(_module, 'IRDPSRAPIVirtualChannelManager')
make_head(_module, 'IRDPSRAPIWindow')
make_head(_module, 'IRDPSRAPIWindowList')
make_head(_module, 'IRDPViewerInputSink')
make_head(_module, '_IRDPSessionEvents')
make_head(_module, '__ReferenceRemainingTypes__')
