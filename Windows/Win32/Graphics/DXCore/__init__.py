from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Graphics.DXCore
import Windows.Win32.System.Com
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
_FACDXCORE: UInt32 = 2176
DXCORE_ADAPTER_ATTRIBUTE_D3D11_GRAPHICS: Guid = Guid('8c47866b-7583-450d-f0-f0-6b-ad-a8-95-af-4b')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_GRAPHICS: Guid = Guid('0c9ece4d-2f6e-4f01-8c-96-e8-9e-33-1b-47-b1')
DXCORE_ADAPTER_ATTRIBUTE_D3D12_CORE_COMPUTE: Guid = Guid('248e2800-a793-4724-ab-aa-23-a6-de-1b-e0-90')
@winfunctype('DXCORE.dll')
def DXCoreCreateAdapterFactory(riid: POINTER(Guid), ppvFactory: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class DXCoreAdapterMemoryBudget(EasyCastStructure):
    budget: UInt64
    currentUsage: UInt64
    availableForReservation: UInt64
    currentReservation: UInt64
class DXCoreAdapterMemoryBudgetNodeSegmentGroup(EasyCastStructure):
    nodeIndex: UInt32
    segmentGroup: Windows.Win32.Graphics.DXCore.DXCoreSegmentGroup
DXCoreAdapterPreference = UInt32
DXCoreAdapterPreference_Hardware: DXCoreAdapterPreference = 0
DXCoreAdapterPreference_MinimumPower: DXCoreAdapterPreference = 1
DXCoreAdapterPreference_HighPerformance: DXCoreAdapterPreference = 2
DXCoreAdapterProperty = UInt32
DXCoreAdapterProperty_InstanceLuid: DXCoreAdapterProperty = 0
DXCoreAdapterProperty_DriverVersion: DXCoreAdapterProperty = 1
DXCoreAdapterProperty_DriverDescription: DXCoreAdapterProperty = 2
DXCoreAdapterProperty_HardwareID: DXCoreAdapterProperty = 3
DXCoreAdapterProperty_KmdModelVersion: DXCoreAdapterProperty = 4
DXCoreAdapterProperty_ComputePreemptionGranularity: DXCoreAdapterProperty = 5
DXCoreAdapterProperty_GraphicsPreemptionGranularity: DXCoreAdapterProperty = 6
DXCoreAdapterProperty_DedicatedAdapterMemory: DXCoreAdapterProperty = 7
DXCoreAdapterProperty_DedicatedSystemMemory: DXCoreAdapterProperty = 8
DXCoreAdapterProperty_SharedSystemMemory: DXCoreAdapterProperty = 9
DXCoreAdapterProperty_AcgCompatible: DXCoreAdapterProperty = 10
DXCoreAdapterProperty_IsHardware: DXCoreAdapterProperty = 11
DXCoreAdapterProperty_IsIntegrated: DXCoreAdapterProperty = 12
DXCoreAdapterProperty_IsDetachable: DXCoreAdapterProperty = 13
DXCoreAdapterProperty_HardwareIDParts: DXCoreAdapterProperty = 14
DXCoreAdapterState = UInt32
DXCoreAdapterState_IsDriverUpdateInProgress: DXCoreAdapterState = 0
DXCoreAdapterState_AdapterMemoryBudget: DXCoreAdapterState = 1
class DXCoreHardwareID(EasyCastStructure):
    vendorID: UInt32
    deviceID: UInt32
    subSysID: UInt32
    revision: UInt32
class DXCoreHardwareIDParts(EasyCastStructure):
    vendorID: UInt32
    deviceID: UInt32
    subSystemID: UInt32
    subVendorID: UInt32
    revisionID: UInt32
DXCoreNotificationType = UInt32
DXCoreNotificationType_AdapterListStale: DXCoreNotificationType = 0
DXCoreNotificationType_AdapterNoLongerValid: DXCoreNotificationType = 1
DXCoreNotificationType_AdapterBudgetChange: DXCoreNotificationType = 2
DXCoreNotificationType_AdapterHardwareContentProtectionTeardown: DXCoreNotificationType = 3
DXCoreSegmentGroup = UInt32
DXCoreSegmentGroup_Local: DXCoreSegmentGroup = 0
DXCoreSegmentGroup_NonLocal: DXCoreSegmentGroup = 1
class IDXCoreAdapter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f0db4c7f-fe5a-42a2-bd-62-f2-a6-cf-6f-c8-3e')
    @commethod(3)
    def IsValid(self) -> Boolean: ...
    @commethod(4)
    def IsAttributeSupported(self, attributeGUID: POINTER(Guid)) -> Boolean: ...
    @commethod(5)
    def IsPropertySupported(self, property: Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty) -> Boolean: ...
    @commethod(6)
    def GetProperty(self, property: Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: UIntPtr, propertyData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPropertySize(self, property: Windows.Win32.Graphics.DXCore.DXCoreAdapterProperty, bufferSize: POINTER(UIntPtr)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsQueryStateSupported(self, property: Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(9)
    def QueryState(self, state: Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: c_void_p, outputBufferSize: UIntPtr, outputBuffer: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def IsSetStateSupported(self, property: Windows.Win32.Graphics.DXCore.DXCoreAdapterState) -> Boolean: ...
    @commethod(11)
    def SetState(self, state: Windows.Win32.Graphics.DXCore.DXCoreAdapterState, inputStateDetailsSize: UIntPtr, inputStateDetails: c_void_p, inputDataSize: UIntPtr, inputData: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterFactory(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('78ee5945-c36e-4b13-a6-69-00-5d-d1-1c-0f-06')
    @commethod(3)
    def CreateAdapterList(self, numAttributes: UInt32, filterAttributes: POINTER(Guid), riid: POINTER(Guid), ppvAdapterList: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterByLuid(self, adapterLUID: POINTER(Windows.Win32.Foundation.LUID_head), riid: POINTER(Guid), ppvAdapter: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsNotificationTypeSupported(self, notificationType: Windows.Win32.Graphics.DXCore.DXCoreNotificationType) -> Boolean: ...
    @commethod(6)
    def RegisterEventNotification(self, dxCoreObject: Windows.Win32.System.Com.IUnknown_head, notificationType: Windows.Win32.Graphics.DXCore.DXCoreNotificationType, callbackFunction: Windows.Win32.Graphics.DXCore.PFN_DXCORE_NOTIFICATION_CALLBACK, callbackContext: c_void_p, eventCookie: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterEventNotification(self, eventCookie: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IDXCoreAdapterList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('526c7776-40e9-459b-b7-11-f3-2a-d7-6d-fc-28')
    @commethod(3)
    def GetAdapter(self, index: UInt32, riid: POINTER(Guid), ppvAdapter: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetAdapterCount(self) -> UInt32: ...
    @commethod(5)
    def IsStale(self) -> Boolean: ...
    @commethod(6)
    def GetFactory(self, riid: POINTER(Guid), ppvFactory: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Sort(self, numPreferences: UInt32, preferences: POINTER(Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsAdapterPreferenceSupported(self, preference: Windows.Win32.Graphics.DXCore.DXCoreAdapterPreference) -> Boolean: ...
@winfunctype_pointer
def PFN_DXCORE_NOTIFICATION_CALLBACK(notificationType: Windows.Win32.Graphics.DXCore.DXCoreNotificationType, object: Windows.Win32.System.Com.IUnknown_head, context: c_void_p) -> Void: ...
make_head(_module, 'DXCoreAdapterMemoryBudget')
make_head(_module, 'DXCoreAdapterMemoryBudgetNodeSegmentGroup')
make_head(_module, 'DXCoreHardwareID')
make_head(_module, 'DXCoreHardwareIDParts')
make_head(_module, 'IDXCoreAdapter')
make_head(_module, 'IDXCoreAdapterFactory')
make_head(_module, 'IDXCoreAdapterList')
make_head(_module, 'PFN_DXCORE_NOTIFICATION_CALLBACK')
