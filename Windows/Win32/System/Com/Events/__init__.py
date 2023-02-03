from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.Com.Events
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
CEventClass = Guid('cdbec9c0-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
CEventPublisher = Guid('ab944620-79c6-11d1-88-f9-00-80-c7-d7-71-bf')
CEventSubscription = Guid('7542e960-79c7-11d1-88-f9-00-80-c7-d7-71-bf')
CEventSystem = Guid('4e14fba2-2e22-11d1-99-64-00-c0-4f-bb-b3-45')
class COMEVENTSYSCHANGEINFO(Structure):
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
class IDontSupportEventSubscription(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('784121f1-62a6-4b89-85-5f-d6-5f-29-6d-e8-3a')
class IEnumEventObject(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4a07d63-2e25-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(3)
    def Clone(ppInterface: POINTER(Windows.Win32.System.Com.Events.IEnumEventObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Next(cReqElem: UInt32, ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head), cRetElem: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Reset() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Skip(cSkipElem: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IEventClass(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fb2b72a0-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
    @commethod(7)
    def get_EventClassID(pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_EventClassID(bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_EventClassName(pbstrEventClassName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_EventClassName(bstrEventClassName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_OwnerSID(pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_OwnerSID(bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_FiringInterfaceID(pbstrFiringInterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_FiringInterfaceID(bstrFiringInterfaceID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_CustomConfigCLSID(pbstrCustomConfigCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_CustomConfigCLSID(bstrCustomConfigCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_TypeLib(pbstrTypeLib: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_TypeLib(bstrTypeLib: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventClass2(c_void_p):
    extends: Windows.Win32.System.Com.Events.IEventClass
    Guid = Guid('fb2b72a1-7a68-11d1-88-f9-00-80-c7-d7-71-bf')
    @commethod(21)
    def get_PublisherID(pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PublisherID(bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_MultiInterfacePublisherFilterCLSID(pbstrPubFilCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_MultiInterfacePublisherFilterCLSID(bstrPubFilCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_AllowInprocActivation(pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_AllowInprocActivation(fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_FireInParallel(pfFireInParallel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_FireInParallel(fFireInParallel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IEventControl(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('0343e2f4-86f6-11d1-b7-60-00-c0-4f-b9-26-af')
    @commethod(7)
    def SetPublisherFilter(methodName: Windows.Win32.Foundation.BSTR, pPublisherFilter: Windows.Win32.System.Com.Events.IPublisherFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_AllowInprocActivation(pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_AllowInprocActivation(fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetSubscriptions(methodName: Windows.Win32.Foundation.BSTR, optionalCriteria: Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDefaultQuery(methodName: Windows.Win32.Foundation.BSTR, criteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('f4a07d70-2e25-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(3)
    def ChangedSubscription(changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrSubscriptionID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ChangedPublisher(changeType: Windows.Win32.System.Com.Events.EOC_ChangeType, bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectChange2(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('7701a9c3-bd68-438f-83-e0-67-bf-4f-53-a4-22')
    @commethod(3)
    def ChangedSubscription(pInfo: POINTER(Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ChangedEventClass(pInfo: POINTER(Windows.Win32.System.Com.Events.COMEVENTSYSCHANGEINFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventObjectCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f89ac270-d4eb-11d1-b6-82-00-80-5f-c7-92-16')
    @commethod(7)
    def get__NewEnum(ppUnkEnum: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(objectID: Windows.Win32.Foundation.BSTR, pItem: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NewEnum(ppEnum: POINTER(Windows.Win32.System.Com.Events.IEnumEventObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_Count(pCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Add(item: POINTER(Windows.Win32.System.Com.VARIANT_head), objectID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Remove(objectID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventProperty(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('da538ee2-f4de-11d1-b6-bb-00-80-5f-c7-92-16')
    @commethod(7)
    def get_Name(propertyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_Name(propertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Value(propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Value(propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventPublisher(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e341516b-2e32-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(7)
    def get_PublisherID(pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_PublisherID(bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_PublisherName(pbstrPublisherName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_PublisherName(bstrPublisherName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherType(pbstrPublisherType: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherType(bstrPublisherType: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_OwnerSID(pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_OwnerSID(bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_Description(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_Description(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetDefaultProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def PutDefaultProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def RemoveDefaultProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def GetDefaultPropertyCollection(collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IEventSubscription(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4a6b0e15-2e38-11d1-99-65-00-c0-4f-bb-b3-45')
    @commethod(7)
    def get_SubscriptionID(pbstrSubscriptionID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def put_SubscriptionID(bstrSubscriptionID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_SubscriptionName(pbstrSubscriptionName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_SubscriptionName(bstrSubscriptionName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_PublisherID(pbstrPublisherID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_PublisherID(bstrPublisherID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_EventClassID(pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_EventClassID(bstrEventClassID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MethodName(pbstrMethodName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MethodName(bstrMethodName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SubscriberCLSID(pbstrSubscriberCLSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SubscriberCLSID(bstrSubscriberCLSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_SubscriberInterface(ppSubscriberInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_SubscriberInterface(pSubscriberInterface: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_PerUser(pfPerUser: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_PerUser(fPerUser: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def get_OwnerSID(pbstrOwnerSID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_OwnerSID(bstrOwnerSID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_Enabled(pfEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_Enabled(fEnabled: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_Description(pbstrDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_Description(bstrDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(29)
    def get_MachineName(pbstrMachineName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MachineName(bstrMachineName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def GetPublisherProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def PutPublisherProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(33)
    def RemovePublisherProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(34)
    def GetPublisherPropertyCollection(collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(35)
    def GetSubscriberProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(36)
    def PutSubscriberProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR, propertyValue: POINTER(Windows.Win32.System.Com.VARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(37)
    def RemoveSubscriberProperty(bstrPropertyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(38)
    def GetSubscriberPropertyCollection(collection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(39)
    def get_InterfaceID(pbstrInterfaceID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(40)
    def put_InterfaceID(bstrInterfaceID: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IEventSystem(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('4e14fb9f-2e22-11d1-99-64-00-c0-4f-bb-b3-45')
    @commethod(7)
    def Query(progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32), ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Store(ProgID: Windows.Win32.Foundation.BSTR, pInterface: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Remove(progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_EventObjectChangeEventClassID(pbstrEventClassID: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def QueryS(progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR, ppInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def RemoveS(progID: Windows.Win32.Foundation.BSTR, queryCriteria: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IFiringControl(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('e0498c93-4efe-11d1-99-71-00-c0-4f-bb-b3-45')
    @commethod(7)
    def FireSubscription(subscription: Windows.Win32.System.Com.Events.IEventSubscription_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfaceEventControl(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('0343e2f5-86f6-11d1-b7-60-00-c0-4f-b9-26-af')
    @commethod(3)
    def SetMultiInterfacePublisherFilter(classFilter: Windows.Win32.System.Com.Events.IMultiInterfacePublisherFilter_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSubscriptions(eventIID: POINTER(Guid), bstrMethodName: Windows.Win32.Foundation.BSTR, optionalCriteria: Windows.Win32.Foundation.BSTR, optionalErrorIndex: POINTER(Int32), ppCollection: POINTER(Windows.Win32.System.Com.Events.IEventObjectCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDefaultQuery(eventIID: POINTER(Guid), bstrMethodName: Windows.Win32.Foundation.BSTR, bstrCriteria: Windows.Win32.Foundation.BSTR, errorIndex: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def get_AllowInprocActivation(pfAllowInprocActivation: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def put_AllowInprocActivation(fAllowInprocActivation: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_FireInParallel(pfFireInParallel: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def put_FireInParallel(fFireInParallel: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IMultiInterfacePublisherFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('465e5cc1-7b26-11d1-88-fb-00-80-c7-d7-71-bf')
    @commethod(3)
    def Initialize(pEIC: Windows.Win32.System.Com.Events.IMultiInterfaceEventControl_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(iid: POINTER(Guid), methodName: Windows.Win32.Foundation.BSTR, firingControl: Windows.Win32.System.Com.Events.IFiringControl_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPublisherFilter(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('465e5cc0-7b26-11d1-88-fb-00-80-c7-d7-71-bf')
    @commethod(3)
    def Initialize(methodName: Windows.Win32.Foundation.BSTR, dispUserDefined: Windows.Win32.System.Com.IDispatch_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def PrepareToFire(methodName: Windows.Win32.Foundation.BSTR, firingControl: Windows.Win32.System.Com.Events.IFiringControl_head) -> Windows.Win32.Foundation.HRESULT: ...
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
__all__ = [
    "CEventClass",
    "CEventPublisher",
    "CEventSubscription",
    "CEventSystem",
    "COMEVENTSYSCHANGEINFO",
    "EOC_ChangeType",
    "EOC_DeletedObject",
    "EOC_ModifiedObject",
    "EOC_NewObject",
    "EventObjectChange",
    "EventObjectChange2",
    "IDontSupportEventSubscription",
    "IEnumEventObject",
    "IEventClass",
    "IEventClass2",
    "IEventControl",
    "IEventObjectChange",
    "IEventObjectChange2",
    "IEventObjectCollection",
    "IEventProperty",
    "IEventPublisher",
    "IEventSubscription",
    "IEventSystem",
    "IFiringControl",
    "IMultiInterfaceEventControl",
    "IMultiInterfacePublisherFilter",
    "IPublisherFilter",
]
_arch_optional = [
]