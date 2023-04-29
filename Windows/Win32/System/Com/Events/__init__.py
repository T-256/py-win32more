from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Events
import Windows.Win32.System.Variant
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CEventClass = Guid('cdbec9c0-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
CEventPublisher = Guid('ab944620-79c6-11d1-88-f9-00-80-c7-d7-71-bf')
CEventSubscription = Guid('7542e960-79c7-11d1-88-f9-00-80-c7-d7-71-bf')
CEventSystem = Guid('4e14fba2-2e22-11d1-99-64-00-c0-4f-bb-b3-45')
class COMEVENTSYSCHANGEINFO(EasyCastStructure):
    cbSize: UInt32
    changeType: Windows.Win32.System.Com.Events.EOC_ChangeType
    objectId: Windows.Win32.Foundation.BSTR
    partitionId: Windows.Win32.Foundation.BSTR
    applicationId: Windows.Win32.Foundation.BSTR
    reserved: Guid * 10
EOC_ChangeType = Int32
EOC_NewObject: EOC_ChangeType = 0
EOC_ModifiedObject: EOC_ChangeType = 1
EOC_DeletedObject: EOC_ChangeType = 2
EventObjectChange = Guid('d0565000-9df4-11d1-a2-81-00-c0-4f-ca-0a-a7')
EventObjectChange2 = Guid('bb07bacd-cd56-4e63-a8-ff-cb-f0-35-5f-b9-f4')
class IDontSupportEventSubscription(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('784121f1-62a6-4b89-85-5f-d6-5f-29-6d-e8-3a')
class IEnumEventObject(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4a07d63-2e25-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(3)
    def Clone(self, ppInterface: POINTER(Windows.Win32.System.Com.Events.IEnumEventObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(self, cReqElem: UInt32, ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head), cRetElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(self, cSkipElem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IEventClass(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fb2b72a0-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
    @commethod(7)
    def get_EventClassID(self, pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_EventClassID(self, bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventClassName(self, pbstrEventClassName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EventClassName(self, bstrEventClassName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OwnerSID(self, bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FiringInterfaceID(self, pbstrFiringInterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FiringInterfaceID(self, bstrFiringInterfaceID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CustomConfigCLSID(self, pbstrCustomConfigCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CustomConfigCLSID(self, bstrCustomConfigCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TypeLib(self, pbstrTypeLib: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_TypeLib(self, bstrTypeLib: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventClass2(ComPtr):
    extends: Windows.Win32.System.Com.Events.IEventClass
    Guid = Guid('fb2b72a1-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
    @commethod(21)
    def get_PublisherID(self, pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PublisherID(self, bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_MultiInterfacePublisherFilterCLSID(self, pbstrPubFilCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MultiInterfacePublisherFilterCLSID(self, bstrPubFilCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowInprocActivation(self, fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_FireInParallel(self, pfFireInParallel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_FireInParallel(self, fFireInParallel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IEventControl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0343e2f4-86f6-11d1-b7-60-00-c0-4f-b9-26-af')
    @commethod(7)
    def SetPublisherFilter(self, methodName: Windows.Win32.Foundation.BSTR, pPublisherFilter: Windows.Win32.System.Com.Events.IPublisherFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowInprocActivation(self, fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSubscriptions(self, methodName: Windows.Win32.Foundation.BSTR, optionalCriteria: Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultQuery(self, methodName: Windows.Win32.Foundation.BSTR, criteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4a07d70-2e25-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(3)
    def ChangedSubscription(self, changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrSubscriptionID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(self, changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangedPublisher(self, changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7701a9c3-bd68-438f-83-e0-67-bf-4f-53-a4-22')
    @commethod(3)
    def ChangedSubscription(self, pInfo: POINTER(Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(self, pInfo: POINTER(Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectCollection(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f89ac270-d4eb-11d1-b6-82-00-80-5f-c7-92-16')
    @commethod(7)
    def get__NewEnum(self, ppUnkEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, objectID: Windows.Win32.Foundation.BSTR, pItem: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NewEnum(self, ppEnum: POINTER(Windows.Win32.System.Com.Events.IEnumEventObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(self, pCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(self, item: POINTER(Windows.Win32.System.Variant.VARIANT_head), objectID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(self, objectID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventProperty(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('da538ee2-f4de-11d1-b6-bb-00-80-5f-c7-92-16')
    @commethod(7)
    def get_Name(self, propertyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(self, propertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(self, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Value(self, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventPublisher(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e341516b-2e32-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(7)
    def get_PublisherID(self, pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PublisherID(self, bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PublisherName(self, pbstrPublisherName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PublisherName(self, bstrPublisherName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherType(self, pbstrPublisherType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherType(self, bstrPublisherType: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OwnerSID(self, bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDefaultProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PutDefaultProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveDefaultProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultPropertyCollection(self, collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventSubscription(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4a6b0e15-2e38-11d1-99-65-00-c0-4f-bb-b3-45')
    @commethod(7)
    def get_SubscriptionID(self, pbstrSubscriptionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SubscriptionID(self, bstrSubscriptionID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SubscriptionName(self, pbstrSubscriptionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SubscriptionName(self, bstrSubscriptionName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherID(self, pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherID(self, bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_EventClassID(self, pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_EventClassID(self, bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MethodName(self, pbstrMethodName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MethodName(self, bstrMethodName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SubscriberCLSID(self, pbstrSubscriberCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SubscriberCLSID(self, bstrSubscriberCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SubscriberInterface(self, ppSubscriberInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SubscriberInterface(self, pSubscriberInterface: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_PerUser(self, pfPerUser: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PerUser(self, fPerUser: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OwnerSID(self, pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OwnerSID(self, bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Enabled(self, pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Enabled(self, fEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Description(self, pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Description(self, bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MachineName(self, pbstrMachineName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MachineName(self, bstrMachineName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPublisherProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def PutPublisherProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemovePublisherProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetPublisherPropertyCollection(self, collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetSubscriberProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PutSubscriberProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Variant.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveSubscriberProperty(self, bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetSubscriberPropertyCollection(self, collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_InterfaceID(self, pbstrInterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_InterfaceID(self, bstrInterfaceID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventSystem(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4e14fb9f-2e22-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(7)
    def Query(self, progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32), ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Store(self, ProgID: Windows.Win32.Foundation.BSTR, pInterface: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(self, progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventObjectChangeEventClassID(self, pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def QueryS(self, progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveS(self, progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFiringControl(ComPtr):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e0498c93-4efe-11d1-99-71-00-c0-4f-bb-b3-45')
    @commethod(7)
    def FireSubscription(self, subscription: Windows.Win32.System.Com.Events.IEventSubscription_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfaceEventControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0343e2f5-86f6-11d1-b7-60-00-c0-4f-b9-26-af')
    @commethod(3)
    def SetMultiInterfacePublisherFilter(self, classFilter: Windows.Win32.System.Com.Events.IMultiInterfacePublisherFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSubscriptions(self, eventIID: POINTER(Guid), bstrMethodName: Windows.Win32.Foundation.BSTR, optionalCriteria: Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultQuery(self, eventIID: POINTER(Guid), bstrMethodName: Windows.Win32.Foundation.BSTR, bstrCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AllowInprocActivation(self, pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_AllowInprocActivation(self, fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FireInParallel(self, pfFireInParallel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FireInParallel(self, fFireInParallel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfacePublisherFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('465e5cc1-7b26-11d1-88-fb-00-80-c7-d7-71-bf')
    @commethod(3)
    def Initialize(self, pEIC: Windows.Win32.System.Com.Events.IMultiInterfaceEventControl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(self, iid: POINTER(Guid), methodName: Windows.Win32.Foundation.BSTR, firingControl: Windows.Win32.System.Com.Events.IFiringControl_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPublisherFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('465e5cc0-7b26-11d1-88-fb-00-80-c7-d7-71-bf')
    @commethod(3)
    def Initialize(self, methodName: Windows.Win32.Foundation.BSTR, dispUserDefined: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(self, methodName: Windows.Win32.Foundation.BSTR, firingControl: Windows.Win32.System.Com.Events.IFiringControl_head) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'COMEVENTSYSCHANGEINFO')
make_head(_module, 'IDontSupportEventSubscription')
make_head(_module, 'IEnumEventObject')
make_head(_module, 'IEventClass')
make_head(_module, 'IEventClass2')
make_head(_module, 'IEventControl')
make_head(_module, 'IEventObjectChange')
make_head(_module, 'IEventObjectChange2')
make_head(_module, 'IEventObjectCollection')
make_head(_module, 'IEventProperty')
make_head(_module, 'IEventPublisher')
make_head(_module, 'IEventSubscription')
make_head(_module, 'IEventSystem')
make_head(_module, 'IFiringControl')
make_head(_module, 'IMultiInterfaceEventControl')
make_head(_module, 'IMultiInterfacePublisherFilter')
make_head(_module, 'IPublisherFilter')
