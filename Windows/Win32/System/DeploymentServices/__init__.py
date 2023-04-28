from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.DeploymentServices
import Windows.Win32.System.Registry
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
WDS_CLI_TRANSFER_ASYNCHRONOUS: UInt32 = 1
WDS_CLI_NO_SPARSE_FILE: UInt32 = 2
PXE_DHCP_SERVER_PORT: UInt32 = 67
PXE_DHCP_CLIENT_PORT: UInt32 = 68
PXE_SERVER_PORT: UInt32 = 4011
PXE_DHCPV6_SERVER_PORT: UInt32 = 547
PXE_DHCPV6_CLIENT_PORT: UInt32 = 546
PXE_DHCP_FILE_SIZE: UInt32 = 128
PXE_DHCP_SERVER_SIZE: UInt32 = 64
PXE_DHCP_HWAADR_SIZE: UInt32 = 16
PXE_DHCP_MAGIC_COOKIE_SIZE: UInt32 = 4
PXE_REG_INDEX_TOP: UInt32 = 0
PXE_REG_INDEX_BOTTOM: UInt32 = 4294967295
PXE_CALLBACK_RECV_REQUEST: UInt32 = 0
PXE_CALLBACK_SHUTDOWN: UInt32 = 1
PXE_CALLBACK_SERVICE_CONTROL: UInt32 = 2
PXE_CALLBACK_MAX: UInt32 = 3
PXE_GSI_TRACE_ENABLED: UInt32 = 1
PXE_GSI_SERVER_DUID: UInt32 = 2
PXE_MAX_ADDRESS: UInt32 = 16
PXE_ADDR_BROADCAST: UInt32 = 1
PXE_ADDR_USE_PORT: UInt32 = 2
PXE_ADDR_USE_ADDR: UInt32 = 4
PXE_ADDR_USE_DHCP_RULES: UInt32 = 8
PXE_DHCPV6_RELAY_HOP_COUNT_LIMIT: UInt32 = 32
PXE_BA_NBP: UInt32 = 1
PXE_BA_CUSTOM: UInt32 = 2
PXE_BA_IGNORE: UInt32 = 3
PXE_BA_REJECTED: UInt32 = 4
PXE_TRACE_VERBOSE: UInt32 = 65536
PXE_TRACE_INFO: UInt32 = 131072
PXE_TRACE_WARNING: UInt32 = 262144
PXE_TRACE_ERROR: UInt32 = 524288
PXE_TRACE_FATAL: UInt32 = 1048576
PXE_PROV_ATTR_FILTER: UInt32 = 0
PXE_PROV_ATTR_FILTER_IPV6: UInt32 = 1
PXE_PROV_ATTR_IPV6_CAPABLE: UInt32 = 2
PXE_PROV_FILTER_ALL: UInt32 = 0
PXE_PROV_FILTER_DHCP_ONLY: UInt32 = 1
PXE_PROV_FILTER_PXE_ONLY: UInt32 = 2
MC_SERVER_CURRENT_VERSION: UInt32 = 1
TRANSPORTPROVIDER_CURRENT_VERSION: UInt32 = 1
WDS_MC_TRACE_VERBOSE: UInt32 = 65536
WDS_MC_TRACE_INFO: UInt32 = 131072
WDS_MC_TRACE_WARNING: UInt32 = 262144
WDS_MC_TRACE_ERROR: UInt32 = 524288
WDS_MC_TRACE_FATAL: UInt32 = 1048576
WDS_TRANSPORTCLIENT_CURRENT_API_VERSION: UInt32 = 1
WDS_TRANSPORTCLIENT_PROTOCOL_MULTICAST: UInt32 = 1
WDS_TRANSPORTCLIENT_NO_CACHE: UInt32 = 0
WDS_TRANSPORTCLIENT_STATUS_IN_PROGRESS: UInt32 = 1
WDS_TRANSPORTCLIENT_STATUS_SUCCESS: UInt32 = 2
WDS_TRANSPORTCLIENT_STATUS_FAILURE: UInt32 = 3
WDSTRANSPORT_RESOURCE_UTILIZATION_UNKNOWN: UInt32 = 255
WDSBP_PK_TYPE_DHCP: UInt32 = 1
WDSBP_PK_TYPE_WDSNBP: UInt32 = 2
WDSBP_PK_TYPE_BCD: UInt32 = 4
WDSBP_PK_TYPE_DHCPV6: UInt32 = 8
WDSBP_OPT_TYPE_NONE: UInt32 = 0
WDSBP_OPT_TYPE_BYTE: UInt32 = 1
WDSBP_OPT_TYPE_USHORT: UInt32 = 2
WDSBP_OPT_TYPE_ULONG: UInt32 = 3
WDSBP_OPT_TYPE_WSTR: UInt32 = 4
WDSBP_OPT_TYPE_STR: UInt32 = 5
WDSBP_OPT_TYPE_IP4: UInt32 = 6
WDSBP_OPT_TYPE_IP6: UInt32 = 7
WDSBP_OPTVAL_ACTION_APPROVAL: UInt32 = 1
WDSBP_OPTVAL_ACTION_REFERRAL: UInt32 = 3
WDSBP_OPTVAL_ACTION_ABORT: UInt32 = 5
WDSBP_OPTVAL_PXE_PROMPT_OPTIN: UInt32 = 1
WDSBP_OPTVAL_PXE_PROMPT_NOPROMPT: UInt32 = 2
WDSBP_OPTVAL_PXE_PROMPT_OPTOUT: UInt32 = 3
WDSBP_OPTVAL_NBP_VER_7: UInt32 = 1792
WDSBP_OPTVAL_NBP_VER_8: UInt32 = 2048
FACILITY_WDSMCSERVER: UInt32 = 289
FACILITY_WDSMCCLIENT: UInt32 = 290
WDSMCSERVER_CATEGORY: Windows.Win32.Foundation.HRESULT = 1
WDSMCCLIENT_CATEGORY: Windows.Win32.Foundation.HRESULT = 2
WDSMCS_E_SESSION_SHUTDOWN_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1054801664
WDSMCS_E_REQCALLBACKS_NOT_REG: Windows.Win32.Foundation.HRESULT = -1054801663
WDSMCS_E_INCOMPATIBLE_VERSION: Windows.Win32.Foundation.HRESULT = -1054801662
WDSMCS_E_CONTENT_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1054801661
WDSMCS_E_CLIENT_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1054801660
WDSMCS_E_NAMESPACE_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1054801659
WDSMCS_E_CONTENT_PROVIDER_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -1054801658
WDSMCS_E_NAMESPACE_ALREADY_EXISTS: Windows.Win32.Foundation.HRESULT = -1054801657
WDSMCS_E_NAMESPACE_SHUTDOWN_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1054801656
WDSMCS_E_NAMESPACE_ALREADY_STARTED: Windows.Win32.Foundation.HRESULT = -1054801655
WDSMCS_E_NS_START_FAILED_NO_CLIENTS: Windows.Win32.Foundation.HRESULT = -1054801654
WDSMCS_E_START_TIME_IN_PAST: Windows.Win32.Foundation.HRESULT = -1054801653
WDSMCS_E_PACKET_NOT_HASHED: Windows.Win32.Foundation.HRESULT = -1054801652
WDSMCS_E_PACKET_NOT_SIGNED: Windows.Win32.Foundation.HRESULT = -1054801651
WDSMCS_E_PACKET_HAS_SECURITY: Windows.Win32.Foundation.HRESULT = -1054801650
WDSMCS_E_PACKET_NOT_CHECKSUMED: Windows.Win32.Foundation.HRESULT = -1054801649
WDSMCS_E_CLIENT_DOESNOT_SUPPORT_SECURITY_MODE: Windows.Win32.Foundation.HRESULT = -1054801648
EVT_WDSMCS_S_PARAMETERS_READ: Windows.Win32.Foundation.HRESULT = 1092682240
EVT_WDSMCS_E_PARAMETERS_READ_FAILED: Windows.Win32.Foundation.HRESULT = -1054801407
EVT_WDSMCS_E_DUPLICATE_MULTICAST_ADDR: Windows.Win32.Foundation.HRESULT = -1054801406
EVT_WDSMCS_E_NON_WDS_DUPLICATE_MULTICAST_ADDR: Windows.Win32.Foundation.HRESULT = -1054801405
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED: Windows.Win32.Foundation.HRESULT = -1054801328
EVT_WDSMCS_E_CP_INIT_FUNC_MISSING: Windows.Win32.Foundation.HRESULT = -1054801327
EVT_WDSMCS_E_CP_INIT_FUNC_FAILED: Windows.Win32.Foundation.HRESULT = -1054801326
EVT_WDSMCS_E_CP_INCOMPATIBLE_SERVER_VERSION: Windows.Win32.Foundation.HRESULT = -1054801325
EVT_WDSMCS_E_CP_CALLBACKS_NOT_REG: Windows.Win32.Foundation.HRESULT = -1054801324
EVT_WDSMCS_E_CP_SHUTDOWN_FUNC_FAILED: Windows.Win32.Foundation.HRESULT = -1054801323
EVT_WDSMCS_E_CP_MEMORY_LEAK: Windows.Win32.Foundation.HRESULT = -1054801322
EVT_WDSMCS_E_CP_OPEN_INSTANCE_FAILED: Windows.Win32.Foundation.HRESULT = -1054801321
EVT_WDSMCS_E_CP_CLOSE_INSTANCE_FAILED: Windows.Win32.Foundation.HRESULT = -1054801320
EVT_WDSMCS_E_CP_OPEN_CONTENT_FAILED: Windows.Win32.Foundation.HRESULT = -1054801319
EVT_WDSMCS_W_CP_DLL_LOAD_FAILED_NOT_CRITICAL: Windows.Win32.Foundation.HRESULT = -2128543142
EVT_WDSMCS_E_CP_DLL_LOAD_FAILED_CRITICAL: Windows.Win32.Foundation.HRESULT = -1054801317
EVT_WDSMCS_E_NSREG_START_TIME_IN_PAST: Windows.Win32.Foundation.HRESULT = -1054801152
EVT_WDSMCS_E_NSREG_CONTENT_PROVIDER_NOT_REG: Windows.Win32.Foundation.HRESULT = -1054801151
EVT_WDSMCS_E_NSREG_NAMESPACE_EXISTS: Windows.Win32.Foundation.HRESULT = -1054801150
EVT_WDSMCS_E_NSREG_FAILURE: Windows.Win32.Foundation.HRESULT = -1054801149
WDSTPC_E_CALLBACKS_NOT_REG: Windows.Win32.Foundation.HRESULT = -1054735616
WDSTPC_E_ALREADY_COMPLETED: Windows.Win32.Foundation.HRESULT = -1054735615
WDSTPC_E_ALREADY_IN_PROGRESS: Windows.Win32.Foundation.HRESULT = -1054735614
WDSTPC_E_UNKNOWN_ERROR: Windows.Win32.Foundation.HRESULT = -1054735613
WDSTPC_E_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -1054735612
WDSTPC_E_KICKED_POLICY_NOT_MET: Windows.Win32.Foundation.HRESULT = -1054735611
WDSTPC_E_KICKED_FALLBACK: Windows.Win32.Foundation.HRESULT = -1054735610
WDSTPC_E_KICKED_FAIL: Windows.Win32.Foundation.HRESULT = -1054735609
WDSTPC_E_KICKED_UNKNOWN: Windows.Win32.Foundation.HRESULT = -1054735608
WDSTPC_E_MULTISTREAM_NOT_ENABLED: Windows.Win32.Foundation.HRESULT = -1054735607
WDSTPC_E_ALREADY_IN_LOWEST_SESSION: Windows.Win32.Foundation.HRESULT = -1054735606
WDSTPC_E_CLIENT_DEMOTE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1054735605
WDSTPC_E_NO_IP4_INTERFACE: Windows.Win32.Foundation.HRESULT = -1054735604
WDSTPTC_E_WIM_APPLY_REQUIRES_REFERENCE_IMAGE: Windows.Win32.Foundation.HRESULT = -1054735603
FACILITY_WDSTPTMGMT: UInt32 = 272
WDSTPTMGMT_CATEGORY: Windows.Win32.Foundation.HRESULT = 1
WDSTPTMGMT_E_INVALID_PROPERTY: Windows.Win32.Foundation.HRESULT = -1055915776
WDSTPTMGMT_E_INVALID_OPERATION: Windows.Win32.Foundation.HRESULT = -1055915775
WDSTPTMGMT_E_INVALID_CLASS: Windows.Win32.Foundation.HRESULT = -1055915774
WDSTPTMGMT_E_CONTENT_PROVIDER_ALREADY_REGISTERED: Windows.Win32.Foundation.HRESULT = -1055915773
WDSTPTMGMT_E_CONTENT_PROVIDER_NOT_REGISTERED: Windows.Win32.Foundation.HRESULT = -1055915772
WDSTPTMGMT_E_INVALID_CONTENT_PROVIDER_NAME: Windows.Win32.Foundation.HRESULT = -1055915771
WDSTPTMGMT_E_TRANSPORT_SERVER_ROLE_NOT_CONFIGURED: Windows.Win32.Foundation.HRESULT = -1055915770
WDSTPTMGMT_E_NAMESPACE_ALREADY_REGISTERED: Windows.Win32.Foundation.HRESULT = -1055915769
WDSTPTMGMT_E_NAMESPACE_NOT_REGISTERED: Windows.Win32.Foundation.HRESULT = -1055915768
WDSTPTMGMT_E_CANNOT_REINITIALIZE_OBJECT: Windows.Win32.Foundation.HRESULT = -1055915767
WDSTPTMGMT_E_INVALID_NAMESPACE_NAME: Windows.Win32.Foundation.HRESULT = -1055915766
WDSTPTMGMT_E_INVALID_NAMESPACE_DATA: Windows.Win32.Foundation.HRESULT = -1055915765
WDSTPTMGMT_E_NAMESPACE_READ_ONLY: Windows.Win32.Foundation.HRESULT = -1055915764
WDSTPTMGMT_E_INVALID_NAMESPACE_START_TIME: Windows.Win32.Foundation.HRESULT = -1055915763
WDSTPTMGMT_E_INVALID_DIAGNOSTICS_COMPONENTS: Windows.Win32.Foundation.HRESULT = -1055915762
WDSTPTMGMT_E_CANNOT_REFRESH_DIRTY_OBJECT: Windows.Win32.Foundation.HRESULT = -1055915761
WDSTPTMGMT_E_INVALID_SERVICE_IP_ADDRESS_RANGE: Windows.Win32.Foundation.HRESULT = -1055915760
WDSTPTMGMT_E_INVALID_SERVICE_PORT_RANGE: Windows.Win32.Foundation.HRESULT = -1055915759
WDSTPTMGMT_E_INVALID_NAMESPACE_START_PARAMETERS: Windows.Win32.Foundation.HRESULT = -1055915758
WDSTPTMGMT_E_TRANSPORT_SERVER_UNAVAILABLE: Windows.Win32.Foundation.HRESULT = -1055915757
WDSTPTMGMT_E_NAMESPACE_NOT_ON_SERVER: Windows.Win32.Foundation.HRESULT = -1055915756
WDSTPTMGMT_E_NAMESPACE_REMOVED_FROM_SERVER: Windows.Win32.Foundation.HRESULT = -1055915755
WDSTPTMGMT_E_INVALID_IP_ADDRESS: Windows.Win32.Foundation.HRESULT = -1055915754
WDSTPTMGMT_E_INVALID_IPV4_MULTICAST_ADDRESS: Windows.Win32.Foundation.HRESULT = -1055915753
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS: Windows.Win32.Foundation.HRESULT = -1055915752
WDSTPTMGMT_E_IPV6_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915751
WDSTPTMGMT_E_INVALID_IPV6_MULTICAST_ADDRESS_SOURCE: Windows.Win32.Foundation.HRESULT = -1055915750
WDSTPTMGMT_E_INVALID_MULTISTREAM_STREAM_COUNT: Windows.Win32.Foundation.HRESULT = -1055915749
WDSTPTMGMT_E_INVALID_AUTO_DISCONNECT_THRESHOLD: Windows.Win32.Foundation.HRESULT = -1055915748
WDSTPTMGMT_E_MULTICAST_SESSION_POLICY_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915747
WDSTPTMGMT_E_INVALID_SLOW_CLIENT_HANDLING_TYPE: Windows.Win32.Foundation.HRESULT = -1055915746
WDSTPTMGMT_E_NETWORK_PROFILES_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915745
WDSTPTMGMT_E_UDP_PORT_POLICY_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915744
WDSTPTMGMT_E_TFTP_MAX_BLOCKSIZE_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915743
WDSTPTMGMT_E_TFTP_VAR_WINDOW_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -1055915742
WDSTPTMGMT_E_INVALID_TFTP_MAX_BLOCKSIZE: Windows.Win32.Foundation.HRESULT = -1055915741
WdsCliFlagEnumFilterVersion: Int32 = 1
WdsCliFlagEnumFilterFirmware: Int32 = 2
WDS_LOG_TYPE_CLIENT_ERROR: Int32 = 1
WDS_LOG_TYPE_CLIENT_STARTED: Int32 = 2
WDS_LOG_TYPE_CLIENT_FINISHED: Int32 = 3
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED: Int32 = 4
WDS_LOG_TYPE_CLIENT_APPLY_STARTED: Int32 = 5
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED: Int32 = 6
WDS_LOG_TYPE_CLIENT_GENERIC_MESSAGE: Int32 = 7
WDS_LOG_TYPE_CLIENT_UNATTEND_MODE: Int32 = 8
WDS_LOG_TYPE_CLIENT_TRANSFER_START: Int32 = 9
WDS_LOG_TYPE_CLIENT_TRANSFER_END: Int32 = 10
WDS_LOG_TYPE_CLIENT_TRANSFER_DOWNGRADE: Int32 = 11
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR: Int32 = 12
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_START: Int32 = 13
WDS_LOG_TYPE_CLIENT_POST_ACTIONS_END: Int32 = 14
WDS_LOG_TYPE_CLIENT_APPLY_STARTED_2: Int32 = 15
WDS_LOG_TYPE_CLIENT_APPLY_FINISHED_2: Int32 = 16
WDS_LOG_TYPE_CLIENT_DOMAINJOINERROR_2: Int32 = 17
WDS_LOG_TYPE_CLIENT_DRIVER_PACKAGE_NOT_ACCESSIBLE: Int32 = 18
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_START: Int32 = 19
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_END: Int32 = 20
WDS_LOG_TYPE_CLIENT_OFFLINE_DRIVER_INJECTION_FAILURE: Int32 = 21
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED2: Int32 = 22
WDS_LOG_TYPE_CLIENT_IMAGE_SELECTED3: Int32 = 23
WDS_LOG_TYPE_CLIENT_MAX_CODE: Int32 = 24
WDS_LOG_LEVEL_DISABLED: Int32 = 0
WDS_LOG_LEVEL_ERROR: Int32 = 1
WDS_LOG_LEVEL_WARNING: Int32 = 2
WDS_LOG_LEVEL_INFO: Int32 = 3
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliClose(Handle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliRegisterTrace(pfn: Windows.Win32.System.DeploymentServices.PFN_WdsCliTraceFunction) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFreeStringArray(ppwszArray: POINTER(Windows.Win32.Foundation.PWSTR), ulCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindFirstImage(hSession: Windows.Win32.Foundation.HANDLE, phFindHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliFindNextImage(Handle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetEnumerationFlags(Handle: Windows.Win32.Foundation.HANDLE, pdwFlags: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromFindHandle(FindHandle: Windows.Win32.Foundation.HANDLE, phImageHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHandleFromTransferHandle(hTransfer: Windows.Win32.Foundation.HANDLE, phImageHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCreateSession(pwszServer: Windows.Win32.Foundation.PWSTR, pCred: POINTER(Windows.Win32.System.DeploymentServices.WDS_CLI_CRED_head), phSession: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliAuthorizeSession(hSession: Windows.Win32.Foundation.HANDLE, pCred: POINTER(Windows.Win32.System.DeploymentServices.WDS_CLI_CRED_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliInitializeLog(hSession: Windows.Win32.Foundation.HANDLE, ulClientArchitecture: Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE, pwszClientId: Windows.Win32.Foundation.PWSTR, pwszClientAddress: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('WDSCLIENTAPI.dll', variadic=True)
def WdsCliLog(hSession: Windows.Win32.Foundation.HANDLE, ulLogLevel: UInt32, ulMessageCode: UInt32, *__arglist) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageName(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageDescription(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageType(hIfh: Windows.Win32.Foundation.HANDLE, pImageType: POINTER(Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageFiles(hIfh: Windows.Win32.Foundation.HANDLE, pppwszFiles: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguage(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLanguages(hIfh: Windows.Win32.Foundation.HANDLE, pppszValues: POINTER(POINTER(POINTER(SByte))), pdwNumValues: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageVersion(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImagePath(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageIndex(hIfh: Windows.Win32.Foundation.HANDLE, pdwValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageArchitecture(hIfh: Windows.Win32.Foundation.HANDLE, pdwValue: POINTER(Windows.Win32.System.DeploymentServices.CPU_ARCHITECTURE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageLastModifiedTime(hIfh: Windows.Win32.Foundation.HANDLE, ppSysTimeValue: POINTER(POINTER(Windows.Win32.Foundation.SYSTEMTIME_head))) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageSize(hIfh: Windows.Win32.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageHalName(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageGroup(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageNamespace(hIfh: Windows.Win32.Foundation.HANDLE, ppwszValue: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetImageParameter(hIfh: Windows.Win32.Foundation.HANDLE, ParamType: Windows.Win32.System.DeploymentServices.WDS_CLI_IMAGE_PARAM_TYPE, pResponse: c_void_p, uResponseLen: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetTransferSize(hIfh: Windows.Win32.Foundation.HANDLE, pullValue: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliSetTransferBufferSize(ulSizeInBytes: UInt32) -> Void: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferImage(hImage: Windows.Win32.Foundation.HANDLE, pwszLocalPath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: Windows.Win32.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: c_void_p, phTransfer: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliTransferFile(pwszServer: Windows.Win32.Foundation.PWSTR, pwszNamespace: Windows.Win32.Foundation.PWSTR, pwszRemoteFilePath: Windows.Win32.Foundation.PWSTR, pwszLocalFilePath: Windows.Win32.Foundation.PWSTR, dwFlags: UInt32, dwReserved: UInt32, pfnWdsCliCallback: Windows.Win32.System.DeploymentServices.PFN_WdsCliCallback, pvUserData: c_void_p, phTransfer: POINTER(Windows.Win32.Foundation.HANDLE)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliCancelTransfer(hTransfer: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliWaitForTransfer(hTransfer: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackages(hImage: Windows.Win32.Foundation.HANDLE, ppwszServerName: POINTER(Windows.Win32.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliObtainDriverPackagesEx(hSession: Windows.Win32.Foundation.HANDLE, pwszMachineInfo: Windows.Win32.Foundation.PWSTR, ppwszServerName: POINTER(Windows.Win32.Foundation.PWSTR), pppwszDriverPackages: POINTER(POINTER(Windows.Win32.Foundation.PWSTR)), pulCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSCLIENTAPI.dll')
def WdsCliGetDriverQueryXml(pwszWinDirPath: Windows.Win32.Foundation.PWSTR, ppwszDriverQuery: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSPXE.dll')
def PxeProviderRegister(pszProviderName: Windows.Win32.Foundation.PWSTR, pszModulePath: Windows.Win32.Foundation.PWSTR, Index: UInt32, bIsCritical: Windows.Win32.Foundation.BOOL, phProviderKey: POINTER(Windows.Win32.System.Registry.HKEY)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderUnRegister(pszProviderName: Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderQueryIndex(pszProviderName: Windows.Win32.Foundation.PWSTR, puIndex: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumFirst(phEnum: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumNext(hEnum: Windows.Win32.Foundation.HANDLE, ppProvider: POINTER(POINTER(Windows.Win32.System.DeploymentServices.PXE_PROVIDER_head))) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderEnumClose(hEnum: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderFreeInfo(pProvider: POINTER(Windows.Win32.System.DeploymentServices.PXE_PROVIDER_head)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeRegisterCallback(hProvider: Windows.Win32.Foundation.HANDLE, CallbackType: UInt32, pCallbackFunction: c_void_p, pContext: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeSendReply(hClientRequest: Windows.Win32.Foundation.HANDLE, pPacket: c_void_p, uPacketLen: UInt32, pAddress: POINTER(Windows.Win32.System.DeploymentServices.PXE_ADDRESS_head)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeAsyncRecvDone(hClientRequest: Windows.Win32.Foundation.HANDLE, Action: UInt32) -> UInt32: ...
@cfunctype('WDSPXE.dll', variadic=True)
def PxeTrace(hProvider: Windows.Win32.Foundation.HANDLE, Severity: UInt32, pszFormat: Windows.Win32.Foundation.PWSTR, *__arglist) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeTraceV(hProvider: Windows.Win32.Foundation.HANDLE, Severity: UInt32, pszFormat: Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxePacketAllocate(hProvider: Windows.Win32.Foundation.HANDLE, hClientRequest: Windows.Win32.Foundation.HANDLE, uSize: UInt32) -> c_void_p: ...
@winfunctype('WDSPXE.dll')
def PxePacketFree(hProvider: Windows.Win32.Foundation.HANDLE, hClientRequest: Windows.Win32.Foundation.HANDLE, pPacket: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeProviderSetAttribute(hProvider: Windows.Win32.Foundation.HANDLE, Attribute: UInt32, pParameterBuffer: c_void_p, uParamLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpInitialize(pRecvPacket: c_void_p, uRecvPacketLen: UInt32, pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6Initialize(pRequest: c_void_p, cbRequest: UInt32, pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOption(pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), bOption: Byte, bOptionLen: Byte, pValue: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOption(pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), wOptionType: UInt16, cbOption: UInt16, pOption: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpAppendOptionRaw(pReplyPacket: c_void_p, uMaxReplyPacketLen: UInt32, puReplyPacketLen: POINTER(UInt32), uBufferLen: UInt16, pBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6AppendOptionRaw(pReply: c_void_p, cbReply: UInt32, pcbReplyUsed: POINTER(UInt32), cbBuffer: UInt16, pBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpIsValid(pPacket: c_void_p, uPacketLen: UInt32, bRequestPacket: Windows.Win32.Foundation.BOOL, pbPxeOptionPresent: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6IsValid(pPacket: c_void_p, uPacketLen: UInt32, bRequestPacket: Windows.Win32.Foundation.BOOL, pbPxeOptionPresent: POINTER(Windows.Win32.Foundation.BOOL)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetOptionValue(pPacket: c_void_p, uPacketLen: UInt32, uInstance: UInt32, bOption: Byte, pbOptionLen: POINTER(Byte), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetOptionValue(pPacket: c_void_p, uPacketLen: UInt32, uInstance: UInt32, wOption: UInt16, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpGetVendorOptionValue(pPacket: c_void_p, uPacketLen: UInt32, bOption: Byte, uInstance: UInt32, pbOptionLen: POINTER(Byte), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6GetVendorOptionValue(pPacket: c_void_p, uPacketLen: UInt32, dwEnterpriseNumber: UInt32, wOption: UInt16, uInstance: UInt32, pwOptionLen: POINTER(UInt16), ppOptionValue: POINTER(c_void_p)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6ParseRelayForw(pRelayForwPacket: c_void_p, uRelayForwPacketLen: UInt32, pRelayMessages: POINTER(Windows.Win32.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head), nRelayMessages: UInt32, pnRelayMessages: POINTER(UInt32), ppInnerPacket: POINTER(POINTER(Byte)), pcbInnerPacket: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeDhcpv6CreateRelayRepl(pRelayMessages: POINTER(Windows.Win32.System.DeploymentServices.PXE_DHCPV6_NESTED_RELAY_MESSAGE_head), nRelayMessages: UInt32, pInnerPacket: POINTER(Byte), cbInnerPacket: UInt32, pReplyBuffer: c_void_p, cbReplyBuffer: UInt32, pcbReplyBuffer: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfo(uInfoType: UInt32, pBuffer: c_void_p, uBufferLen: UInt32) -> UInt32: ...
@winfunctype('WDSPXE.dll')
def PxeGetServerInfoEx(uInfoType: UInt32, pBuffer: c_void_p, uBufferLen: UInt32, puBufferUsed: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerRegisterCallback(hProvider: Windows.Win32.Foundation.HANDLE, CallbackId: Windows.Win32.System.DeploymentServices.TRANSPORTPROVIDER_CALLBACK_ID, pfnCallback: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerCompleteRead(hProvider: Windows.Win32.Foundation.HANDLE, ulBytesRead: UInt32, pvUserData: c_void_p, hReadResult: Windows.Win32.Foundation.HRESULT) -> Windows.Win32.Foundation.HRESULT: ...
@cfunctype('WDSMC.dll', variadic=True)
def WdsTransportServerTrace(hProvider: Windows.Win32.Foundation.HANDLE, Severity: UInt32, pwszFormat: Windows.Win32.Foundation.PWSTR, *__arglist) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerTraceV(hProvider: Windows.Win32.Foundation.HANDLE, Severity: UInt32, pwszFormat: Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerAllocateBuffer(hProvider: Windows.Win32.Foundation.HANDLE, ulBufferSize: UInt32) -> c_void_p: ...
@winfunctype('WDSMC.dll')
def WdsTransportServerFreeBuffer(hProvider: Windows.Win32.Foundation.HANDLE, pvBuffer: c_void_p) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitialize() -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientInitializeSession(pSessionRequest: POINTER(Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_head), pCallerData: c_void_p, hSessionKey: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientRegisterCallback(hSessionKey: Windows.Win32.Foundation.HANDLE, CallbackId: Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_CALLBACK_ID, pfnCallback: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientStartSession(hSessionKey: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCompleteReceive(hSessionKey: Windows.Win32.Foundation.HANDLE, ulSize: UInt32, pullOffset: POINTER(UInt64)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSession(hSessionKey: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCancelSessionEx(hSessionKey: Windows.Win32.Foundation.HANDLE, dwErrorCode: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientWaitForCompletion(hSessionKey: Windows.Win32.Foundation.HANDLE, uTimeout: UInt32) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientQueryStatus(hSessionKey: Windows.Win32.Foundation.HANDLE, puStatus: POINTER(UInt32), puErrorCode: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientCloseSession(hSessionKey: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientAddRefBuffer(pvBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientReleaseBuffer(pvBuffer: c_void_p) -> UInt32: ...
@winfunctype('WDSTPTC.dll')
def WdsTransportClientShutdown() -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitialize(pPacket: c_void_p, uPacketLen: UInt32, pbPacketType: POINTER(Byte), phHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpParseInitializev6(pPacket: c_void_p, uPacketLen: UInt32, pbPacketType: POINTER(Byte), phHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpInitialize(bPacketType: Byte, phHandle: POINTER(Windows.Win32.Foundation.HANDLE)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpCloseHandle(hHandle: Windows.Win32.Foundation.HANDLE) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpQueryOption(hHandle: Windows.Win32.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: c_void_p, puBytes: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpAddOption(hHandle: Windows.Win32.Foundation.HANDLE, uOption: UInt32, uValueLen: UInt32, pValue: c_void_p) -> UInt32: ...
@winfunctype('WDSBP.dll')
def WdsBpGetOptionBuffer(hHandle: Windows.Win32.Foundation.HANDLE, uBufferLen: UInt32, pBuffer: c_void_p, puBytes: POINTER(UInt32)) -> UInt32: ...
CPU_ARCHITECTURE = UInt32
CPU_ARCHITECTURE_AMD64: CPU_ARCHITECTURE = 9
CPU_ARCHITECTURE_IA64: CPU_ARCHITECTURE = 6
CPU_ARCHITECTURE_INTEL: CPU_ARCHITECTURE = 0
class IWdsTransportCacheable(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('46ad894b-0bab-47dc-84-b2-7b-55-3f-1d-8f-80')
    @commethod(7)
    def get_Dirty(self, pbDirty: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def Discard(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Commit(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportClient(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b5dbc93a-cabe-46ca-83-7f-3e-44-e9-3c-65-45')
    @commethod(7)
    def get_Session(self, ppWdsTransportSession: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportSession_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_MacAddress(self, pbszMacAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_IpAddress(self, pbszIpAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_PercentCompletion(self, pulPercentCompletion: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_JoinDuration(self, pulJoinDuration: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def get_CpuUtilization(self, pulCpuUtilization: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MemoryUtilization(self, pulMemoryUtilization: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def get_NetworkUtilization(self, pulNetworkUtilization: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_UserIdentity(self, pbszUserIdentity: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def Disconnect(self, DisconnectionType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportCollection(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b8ba4b1a-2ff4-43ab-99-6c-b2-b1-0a-91-a6-eb')
    @commethod(7)
    def get_Count(self, pulCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Item(self, ulIndex: UInt32, ppVal: POINTER(Windows.Win32.System.Com.IDispatch_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get__NewEnum(self, ppVal: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('84cc4779-42dd-4792-89-1e-13-21-d6-d7-4b-44')
    @commethod(7)
    def get_ServicePolicy(self, ppWdsTransportServicePolicy: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportServicePolicy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_DiagnosticsPolicy(self, ppWdsTransportDiagnosticsPolicy: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportDiagnosticsPolicy_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_WdsTransportServicesRunning(self, bRealtimeStatus: Windows.Win32.Foundation.VARIANT_BOOL, pbServicesRunning: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnableWdsTransportServices(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisableWdsTransportServices(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def StartWdsTransportServices(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def StopWdsTransportServices(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RestartWdsTransportServices(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def NotifyWdsTransportServices(self, ServiceNotification: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SERVICE_NOTIFICATION) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportConfigurationManager2(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportConfigurationManager
    Guid = Guid('d0d85caf-a153-4f1d-a9-dd-96-f4-31-c5-07-17')
    @commethod(16)
    def get_MulticastSessionPolicy(self, ppWdsTransportMulticastSessionPolicy: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportMulticastSessionPolicy_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportContent(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('d405d711-0296-4ab4-a8-60-ac-7d-32-e6-57-98')
    @commethod(7)
    def get_Namespace(self, ppWdsTransportNamespace: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RetrieveSessions(self, ppWdsTransportSessions: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Terminate(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportContentProvider(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b9489f24-f219-4acf-aa-d7-26-5c-7c-08-a6-ae')
    @commethod(7)
    def get_Name(self, pbszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Description(self, pbszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_FilePath(self, pbszFilePath: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_InitializationRoutine(self, pbszInitializationRoutine: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportDiagnosticsPolicy(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('13b33efc-7856-4f61-9a-59-8d-e6-7b-6b-87-b6')
    @commethod(11)
    def get_Enabled(self, pbEnabled: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_Enabled(self, bEnabled: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Components(self, pulComponents: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Components(self, ulComponents: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('5b0d35f5-1b13-4afd-b8-78-65-26-dc-34-0b-5d')
    @commethod(7)
    def GetWdsTransportServer(self, bszServerName: Windows.Win32.Foundation.BSTR, ppWdsTransportServer: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportServer_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportMulticastSessionPolicy(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('4e5753cf-68ec-4504-a9-51-4a-00-32-66-60-6b')
    @commethod(11)
    def get_SlowClientHandling(self, pSlowClientHandling: POINTER(Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_SlowClientHandling(self, SlowClientHandling: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_AutoDisconnectThreshold(self, pulThreshold: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_AutoDisconnectThreshold(self, ulThreshold: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_MultistreamStreamCount(self, pulStreamCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_MultistreamStreamCount(self, ulStreamCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_SlowClientFallback(self, pbClientFallback: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_SlowClientFallback(self, bClientFallback: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespace(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('fa561f57-fbef-4ed3-b0-56-12-7c-b1-b3-3b-84')
    @commethod(7)
    def get_Type(self, pType: POINTER(Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Name(self, pbszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def put_Name(self, bszName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FriendlyName(self, pbszFriendlyName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_FriendlyName(self, bszFriendlyName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_Description(self, pbszDescription: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_Description(self, bszDescription: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_ContentProvider(self, pbszContentProvider: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_ContentProvider(self, bszContentProvider: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_Configuration(self, pbszConfiguration: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_Configuration(self, bszConfiguration: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_Registered(self, pbRegistered: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def get_Tombstoned(self, pbTombstoned: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_TombstoneTime(self, pTombstoneTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def get_TransmissionStarted(self, pbTransmissionStarted: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(23)
    def Register(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def Deregister(self, bTerminateSessions: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def Clone(self, ppWdsTransportNamespaceClone: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def Refresh(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def RetrieveContents(self, ppWdsTransportContents: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceAutoCast(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportNamespace
    Guid = Guid('ad931a72-c4bd-4c41-8f-bc-59-c9-c7-48-df-9e')
class IWdsTransportNamespaceManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('3e22d9f6-3777-4d98-83-e1-f9-86-96-71-7b-a3')
    @commethod(7)
    def CreateNamespace(self, NamespaceType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NAMESPACE_TYPE, bszNamespaceName: Windows.Win32.Foundation.BSTR, bszContentProvider: Windows.Win32.Foundation.BSTR, bszConfiguration: Windows.Win32.Foundation.BSTR, ppWdsTransportNamespace: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RetrieveNamespace(self, bszNamespaceName: Windows.Win32.Foundation.BSTR, ppWdsTransportNamespace: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportNamespace_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def RetrieveNamespaces(self, bszContentProvider: Windows.Win32.Foundation.BSTR, bszNamespaceName: Windows.Win32.Foundation.BSTR, bIncludeTombstones: Windows.Win32.Foundation.VARIANT_BOOL, ppWdsTransportNamespaces: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCast(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportNamespace
    Guid = Guid('3840cecf-d76c-416e-a4-cc-31-c7-41-d2-87-4b')
    @commethod(28)
    def StartTransmission(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastAutoStart(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    Guid = Guid('d606af3d-ea9c-4219-96-1e-74-91-d6-18-d9-b9')
    @commethod(29)
    def get_MinimumClients(self, pulMinimumClients: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(30)
    def put_MinimumClients(self, ulMinimumClients: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(31)
    def get_StartTime(self, pStartTime: POINTER(Double)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(32)
    def put_StartTime(self, StartTime: Double) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportNamespaceScheduledCastManualStart(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceScheduledCast
    Guid = Guid('013e6e4c-e6a7-4fb5-b7-ff-d9-f5-da-80-5c-31')
class IWdsTransportServer(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('09ccd093-830d-4344-a3-0a-73-ae-8e-8f-ca-90')
    @commethod(7)
    def get_Name(self, pbszName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_SetupManager(self, ppWdsTransportSetupManager: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportSetupManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_ConfigurationManager(self, ppWdsTransportConfigurationManager: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportConfigurationManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NamespaceManager(self, ppWdsTransportNamespaceManager: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportNamespaceManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DisconnectClient(self, ulClientId: UInt32, DisconnectionType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_DISCONNECT_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServer2(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportServer
    Guid = Guid('256e999f-6df4-4538-81-b9-85-7b-9a-b8-fb-47')
    @commethod(12)
    def get_TftpManager(self, ppWdsTransportTftpManager: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportTftpManager_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServicePolicy(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportCacheable
    Guid = Guid('b9468578-9f2b-48cc-b2-7a-a6-07-99-c2-75-0c')
    @commethod(11)
    def get_IpAddressSource(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pSourceType: POINTER(Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def put_IpAddressSource(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, SourceType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_StartIpAddress(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszStartIpAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def put_StartIpAddress(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszStartIpAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def get_EndIpAddress(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, pbszEndIpAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def put_EndIpAddress(self, AddressType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_IP_ADDRESS_TYPE, bszEndIpAddress: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def get_StartPort(self, pulStartPort: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(18)
    def put_StartPort(self, ulStartPort: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def get_EndPort(self, pulEndPort: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def put_EndPort(self, ulEndPort: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(21)
    def get_NetworkProfile(self, pProfileType: POINTER(Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(22)
    def put_NetworkProfile(self, ProfileType: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_NETWORK_PROFILE_TYPE) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportServicePolicy2(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportServicePolicy
    Guid = Guid('65c19e5c-aa7e-4b91-89-44-91-e0-e5-57-27-97')
    @commethod(23)
    def get_UdpPortPolicy(self, pUdpPortPolicy: POINTER(Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(24)
    def put_UdpPortPolicy(self, UdpPortPolicy: Windows.Win32.System.DeploymentServices.WDSTRANSPORT_UDP_PORT_POLICY) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(25)
    def get_TftpMaximumBlockSize(self, pulTftpMaximumBlockSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(26)
    def put_TftpMaximumBlockSize(self, ulTftpMaximumBlockSize: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(27)
    def get_EnableTftpVariableWindowExtension(self, pbEnableTftpVariableWindowExtension: POINTER(Windows.Win32.Foundation.VARIANT_BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(28)
    def put_EnableTftpVariableWindowExtension(self, bEnableTftpVariableWindowExtension: Windows.Win32.Foundation.VARIANT_BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSession(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f4efea88-65b1-4f30-a4-b9-27-93-98-77-96-fb')
    @commethod(7)
    def get_Content(self, ppWdsTransportContent: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportContent_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_Id(self, pulId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_NetworkInterfaceName(self, pbszNetworkInterfaceName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_NetworkInterfaceAddress(self, pbszNetworkInterfaceAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_TransferRate(self, pulTransferRate: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_MasterClientId(self, pulMasterClientId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def RetrieveClients(self, ppWdsTransportClients: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def Terminate(self) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSetupManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('f7238425-efa8-40a4-ae-f9-c9-8d-96-9c-0b-75')
    @commethod(7)
    def get_Version(self, pullVersion: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_InstalledFeatures(self, pulInstalledFeatures: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Protocols(self, pulProtocols: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterContentProvider(self, bszName: Windows.Win32.Foundation.BSTR, bszDescription: Windows.Win32.Foundation.BSTR, bszFilePath: Windows.Win32.Foundation.BSTR, bszInitializationRoutine: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def DeregisterContentProvider(self, bszName: Windows.Win32.Foundation.BSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportSetupManager2(c_void_p):
    extends: Windows.Win32.System.DeploymentServices.IWdsTransportSetupManager
    Guid = Guid('02be79da-7e9e-4366-8b-6e-2a-a9-a9-1b-e4-7f')
    @commethod(12)
    def get_TftpCapabilities(self, pulTftpCapabilities: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_ContentProviders(self, ppProviderCollection: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportTftpClient(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('b022d3ae-884d-4d85-b1-46-53-32-0e-76-ef-62')
    @commethod(7)
    def get_FileName(self, pbszFileName: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def get_IpAddress(self, pbszIpAddress: POINTER(Windows.Win32.Foundation.BSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def get_Timeout(self, pulTimeout: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def get_CurrentFileOffset(self, pul64CurrentOffset: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def get_FileSize(self, pul64FileSize: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def get_BlockSize(self, pulBlockSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def get_WindowSize(self, pulWindowSize: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IWdsTransportTftpManager(c_void_p):
    extends: Windows.Win32.System.Com.IDispatch
    Guid = Guid('1327a7c8-ae8a-4fb3-81-50-13-62-27-c3-7e-9a')
    @commethod(7)
    def RetrieveTftpClients(self, ppWdsTransportTftpClients: POINTER(Windows.Win32.System.DeploymentServices.IWdsTransportCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
PFN_WDS_CLI_CALLBACK_MESSAGE_ID = UInt32
WDS_CLI_MSG_START: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 0
WDS_CLI_MSG_COMPLETE: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 1
WDS_CLI_MSG_PROGRESS: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 2
WDS_CLI_MSG_TEXT: PFN_WDS_CLI_CALLBACK_MESSAGE_ID = 3
@winfunctype_pointer
def PFN_WdsCliCallback(dwMessageId: Windows.Win32.System.DeploymentServices.PFN_WDS_CLI_CALLBACK_MESSAGE_ID, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM, pvUserData: c_void_p) -> Void: ...
@winfunctype_pointer
def PFN_WdsCliTraceFunction(pwszFormat: Windows.Win32.Foundation.PWSTR, Params: POINTER(SByte)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveContents(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, pContents: c_void_p, ulSize: UInt32, pullContentOffset: POINTER(UInt64)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientReceiveMetadata(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, pMetadata: c_void_p, ulSize: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionComplete(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, dwError: UInt32) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionNegotiate(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, pInfo: POINTER(Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head), hNegotiateKey: Windows.Win32.Foundation.HANDLE) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStart(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, ullFileSize: POINTER(UInt64)) -> Void: ...
@winfunctype_pointer
def PFN_WdsTransportClientSessionStartEx(hSessionKey: Windows.Win32.Foundation.HANDLE, pCallerData: c_void_p, Info: POINTER(Windows.Win32.System.DeploymentServices.TRANSPORTCLIENT_SESSION_INFO_head)) -> Void: ...
class PXE_ADDRESS(EasyCastStructure):
    uFlags: UInt32
    Anonymous: _Anonymous_e__Union
    uAddrLen: UInt32
    uPort: UInt16
    class _Anonymous_e__Union(EasyCastUnion):
        bAddress: Byte * 16
        uIpAddress: UInt32
class PXE_DHCPV6_MESSAGE(EasyCastStructure):
    MessageType: Byte
    TransactionIDByte1: Byte
    TransactionIDByte2: Byte
    TransactionIDByte3: Byte
    Options: Windows.Win32.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_DHCPV6_MESSAGE_HEADER(EasyCastStructure):
    MessageType: Byte
    Message: Byte * 1
    _pack_ = 1
class PXE_DHCPV6_NESTED_RELAY_MESSAGE(EasyCastStructure):
    pRelayMessage: POINTER(Windows.Win32.System.DeploymentServices.PXE_DHCPV6_RELAY_MESSAGE_head)
    cbRelayMessage: UInt32
    pInterfaceIdOption: c_void_p
    cbInterfaceIdOption: UInt16
class PXE_DHCPV6_OPTION(EasyCastStructure):
    OptionCode: UInt16
    DataLength: UInt16
    Data: Byte * 1
    _pack_ = 1
class PXE_DHCPV6_RELAY_MESSAGE(EasyCastStructure):
    MessageType: Byte
    HopCount: Byte
    LinkAddress: Byte * 16
    PeerAddress: Byte * 16
    Options: Windows.Win32.System.DeploymentServices.PXE_DHCPV6_OPTION * 1
    _pack_ = 1
class PXE_DHCP_MESSAGE(EasyCastStructure):
    Operation: Byte
    HardwareAddressType: Byte
    HardwareAddressLength: Byte
    HopCount: Byte
    TransactionID: UInt32
    SecondsSinceBoot: UInt16
    Reserved: UInt16
    ClientIpAddress: UInt32
    YourIpAddress: UInt32
    BootstrapServerAddress: UInt32
    RelayAgentIpAddress: UInt32
    HardwareAddress: Byte * 16
    HostName: Byte * 64
    BootFileName: Byte * 128
    Anonymous: _Anonymous_e__Union
    Option: Windows.Win32.System.DeploymentServices.PXE_DHCP_OPTION
    _pack_ = 1
    class _Anonymous_e__Union(EasyCastUnion):
        bMagicCookie: Byte * 4
        uMagicCookie: UInt32
        _pack_ = 1
class PXE_DHCP_OPTION(EasyCastStructure):
    OptionType: Byte
    OptionLength: Byte
    OptionValue: Byte * 1
    _pack_ = 1
class PXE_PROVIDER(EasyCastStructure):
    uSizeOfStruct: UInt32
    pwszName: Windows.Win32.Foundation.PWSTR
    pwszFilePath: Windows.Win32.Foundation.PWSTR
    bIsCritical: Windows.Win32.Foundation.BOOL
    uIndex: UInt32
TRANSPORTCLIENT_CALLBACK_ID = Int32
WDS_TRANSPORTCLIENT_SESSION_START: TRANSPORTCLIENT_CALLBACK_ID = 0
WDS_TRANSPORTCLIENT_RECEIVE_CONTENTS: TRANSPORTCLIENT_CALLBACK_ID = 1
WDS_TRANSPORTCLIENT_SESSION_COMPLETE: TRANSPORTCLIENT_CALLBACK_ID = 2
WDS_TRANSPORTCLIENT_RECEIVE_METADATA: TRANSPORTCLIENT_CALLBACK_ID = 3
WDS_TRANSPORTCLIENT_SESSION_STARTEX: TRANSPORTCLIENT_CALLBACK_ID = 4
WDS_TRANSPORTCLIENT_SESSION_NEGOTIATE: TRANSPORTCLIENT_CALLBACK_ID = 5
WDS_TRANSPORTCLIENT_MAX_CALLBACKS: TRANSPORTCLIENT_CALLBACK_ID = 6
class TRANSPORTCLIENT_SESSION_INFO(EasyCastStructure):
    ulStructureLength: UInt32
    ullFileSize: UInt64
    ulBlockSize: UInt32
TRANSPORTPROVIDER_CALLBACK_ID = Int32
WDS_TRANSPORTPROVIDER_CREATE_INSTANCE: TRANSPORTPROVIDER_CALLBACK_ID = 0
WDS_TRANSPORTPROVIDER_COMPARE_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 1
WDS_TRANSPORTPROVIDER_OPEN_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 2
WDS_TRANSPORTPROVIDER_USER_ACCESS_CHECK: TRANSPORTPROVIDER_CALLBACK_ID = 3
WDS_TRANSPORTPROVIDER_GET_CONTENT_SIZE: TRANSPORTPROVIDER_CALLBACK_ID = 4
WDS_TRANSPORTPROVIDER_READ_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 5
WDS_TRANSPORTPROVIDER_CLOSE_CONTENT: TRANSPORTPROVIDER_CALLBACK_ID = 6
WDS_TRANSPORTPROVIDER_CLOSE_INSTANCE: TRANSPORTPROVIDER_CALLBACK_ID = 7
WDS_TRANSPORTPROVIDER_SHUTDOWN: TRANSPORTPROVIDER_CALLBACK_ID = 8
WDS_TRANSPORTPROVIDER_DUMP_STATE: TRANSPORTPROVIDER_CALLBACK_ID = 9
WDS_TRANSPORTPROVIDER_REFRESH_SETTINGS: TRANSPORTPROVIDER_CALLBACK_ID = 10
WDS_TRANSPORTPROVIDER_GET_CONTENT_METADATA: TRANSPORTPROVIDER_CALLBACK_ID = 11
WDS_TRANSPORTPROVIDER_MAX_CALLBACKS: TRANSPORTPROVIDER_CALLBACK_ID = 12
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = Int32
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentPxe: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 1
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentTftp: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 2
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentImageServer: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 4
WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS_WdsTptDiagnosticsComponentMulticast: WDSTRANSPORT_DIAGNOSTICS_COMPONENT_FLAGS = 8
WDSTRANSPORT_DISCONNECT_TYPE = Int32
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectUnknown: WDSTRANSPORT_DISCONNECT_TYPE = 0
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectFallback: WDSTRANSPORT_DISCONNECT_TYPE = 1
WDSTRANSPORT_DISCONNECT_TYPE_WdsTptDisconnectAbort: WDSTRANSPORT_DISCONNECT_TYPE = 2
WDSTRANSPORT_FEATURE_FLAGS = Int32
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureAdminPack: WDSTRANSPORT_FEATURE_FLAGS = 1
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureTransportServer: WDSTRANSPORT_FEATURE_FLAGS = 2
WDSTRANSPORT_FEATURE_FLAGS_WdsTptFeatureDeploymentServer: WDSTRANSPORT_FEATURE_FLAGS = 4
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceUnknown: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 0
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceDhcp: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 1
WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE_WdsTptIpAddressSourceRange: WDSTRANSPORT_IP_ADDRESS_SOURCE_TYPE = 2
WDSTRANSPORT_IP_ADDRESS_TYPE = Int32
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressUnknown: WDSTRANSPORT_IP_ADDRESS_TYPE = 0
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv4: WDSTRANSPORT_IP_ADDRESS_TYPE = 1
WDSTRANSPORT_IP_ADDRESS_TYPE_WdsTptIpAddressIpv6: WDSTRANSPORT_IP_ADDRESS_TYPE = 2
WDSTRANSPORT_NAMESPACE_TYPE = Int32
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeUnknown: WDSTRANSPORT_NAMESPACE_TYPE = 0
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeAutoCast: WDSTRANSPORT_NAMESPACE_TYPE = 1
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastManualStart: WDSTRANSPORT_NAMESPACE_TYPE = 2
WDSTRANSPORT_NAMESPACE_TYPE_WdsTptNamespaceTypeScheduledCastAutoStart: WDSTRANSPORT_NAMESPACE_TYPE = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE = Int32
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileUnknown: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 0
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfileCustom: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 1
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile10Mbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 2
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile100Mbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 3
WDSTRANSPORT_NETWORK_PROFILE_TYPE_WdsTptNetworkProfile1Gbps: WDSTRANSPORT_NETWORK_PROFILE_TYPE = 4
WDSTRANSPORT_PROTOCOL_FLAGS = Int32
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolUnicast: WDSTRANSPORT_PROTOCOL_FLAGS = 1
WDSTRANSPORT_PROTOCOL_FLAGS_WdsTptProtocolMulticast: WDSTRANSPORT_PROTOCOL_FLAGS = 2
WDSTRANSPORT_SERVICE_NOTIFICATION = Int32
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyUnknown: WDSTRANSPORT_SERVICE_NOTIFICATION = 0
WDSTRANSPORT_SERVICE_NOTIFICATION_WdsTptServiceNotifyReadSettings: WDSTRANSPORT_SERVICE_NOTIFICATION = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = Int32
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingUnknown: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 0
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingNone: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 1
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingAutoDisconnect: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 2
WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE_WdsTptSlowClientHandlingMultistream: WDSTRANSPORT_SLOW_CLIENT_HANDLING_TYPE = 3
WDSTRANSPORT_TFTP_CAPABILITY = Int32
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapMaximumBlockSize: WDSTRANSPORT_TFTP_CAPABILITY = 1
WDSTRANSPORT_TFTP_CAPABILITY_WdsTptTftpCapVariableWindow: WDSTRANSPORT_TFTP_CAPABILITY = 2
WDSTRANSPORT_UDP_PORT_POLICY = Int32
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyDynamic: WDSTRANSPORT_UDP_PORT_POLICY = 0
WDSTRANSPORT_UDP_PORT_POLICY_WdsTptUdpPortPolicyFixed: WDSTRANSPORT_UDP_PORT_POLICY = 1
class WDS_CLI_CRED(EasyCastStructure):
    pwszUserName: Windows.Win32.Foundation.PWSTR
    pwszDomain: Windows.Win32.Foundation.PWSTR
    pwszPassword: Windows.Win32.Foundation.PWSTR
WDS_CLI_FIRMWARE_TYPE = Int32
WDS_CLI_FIRMWARE_UNKNOWN: WDS_CLI_FIRMWARE_TYPE = 0
WDS_CLI_FIRMWARE_BIOS: WDS_CLI_FIRMWARE_TYPE = 1
WDS_CLI_FIRMWARE_EFI: WDS_CLI_FIRMWARE_TYPE = 2
WDS_CLI_IMAGE_PARAM_TYPE = Int32
WDS_CLI_IMAGE_PARAM_UNKNOWN: WDS_CLI_IMAGE_PARAM_TYPE = 0
WDS_CLI_IMAGE_PARAM_SPARSE_FILE: WDS_CLI_IMAGE_PARAM_TYPE = 1
WDS_CLI_IMAGE_PARAM_SUPPORTED_FIRMWARES: WDS_CLI_IMAGE_PARAM_TYPE = 2
WDS_CLI_IMAGE_TYPE = Int32
WDS_CLI_IMAGE_TYPE_UNKNOWN: WDS_CLI_IMAGE_TYPE = 0
WDS_CLI_IMAGE_TYPE_WIM: WDS_CLI_IMAGE_TYPE = 1
WDS_CLI_IMAGE_TYPE_VHD: WDS_CLI_IMAGE_TYPE = 2
WDS_CLI_IMAGE_TYPE_VHDX: WDS_CLI_IMAGE_TYPE = 3
class WDS_TRANSPORTCLIENT_CALLBACKS(EasyCastStructure):
    SessionStart: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionStart
    SessionStartEx: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionStartEx
    ReceiveContents: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientReceiveContents
    ReceiveMetadata: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientReceiveMetadata
    SessionComplete: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionComplete
    SessionNegotiate: Windows.Win32.System.DeploymentServices.PFN_WdsTransportClientSessionNegotiate
class WDS_TRANSPORTCLIENT_REQUEST(EasyCastStructure):
    ulLength: UInt32
    ulApiVersion: UInt32
    ulAuthLevel: Windows.Win32.System.DeploymentServices.WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL
    pwszServer: Windows.Win32.Foundation.PWSTR
    pwszNamespace: Windows.Win32.Foundation.PWSTR
    pwszObjectName: Windows.Win32.Foundation.PWSTR
    ulCacheSize: UInt32
    ulProtocol: UInt32
    pvProtocolData: c_void_p
    ulProtocolDataLength: UInt32
WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = UInt32
WDS_TRANSPORTCLIENT_AUTH: WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 1
WDS_TRANSPORTCLIENT_NO_AUTH: WDS_TRANSPORTCLIENT_REQUEST_AUTH_LEVEL = 2
class WDS_TRANSPORTPROVIDER_INIT_PARAMS(EasyCastStructure):
    ulLength: UInt32
    ulMcServerVersion: UInt32
    hRegistryKey: Windows.Win32.System.Registry.HKEY
    hProvider: Windows.Win32.Foundation.HANDLE
class WDS_TRANSPORTPROVIDER_SETTINGS(EasyCastStructure):
    ulLength: UInt32
    ulProviderVersion: UInt32
WdsTransportCacheable = Guid('70590b16-f146-46bd-bd-9d-4a-aa-90-08-4b-f5')
WdsTransportClient = Guid('66d2c5e9-0ff6-49ec-97-33-da-fb-1e-01-df-1c')
WdsTransportCollection = Guid('c7f18b09-391e-436e-b1-0b-c3-ef-46-f2-c3-4f')
WdsTransportConfigurationManager = Guid('8743f674-904c-47ca-85-12-35-fe-98-f6-b0-ac')
WdsTransportContent = Guid('0a891fe7-4a3f-4c65-b6-f2-14-67-61-96-79-ea')
WdsTransportContentProvider = Guid('e0be741f-5a75-4eb9-8a-2d-5e-18-9b-45-f3-27')
WdsTransportDiagnosticsPolicy = Guid('eb3333e1-a7ad-46f5-80-d6-6b-74-02-04-e5-09')
WdsTransportManager = Guid('f21523f6-837c-4a58-af-99-8a-7e-27-f8-ff-59')
WdsTransportMulticastSessionPolicy = Guid('3c6bc3f4-6418-472a-b6-f1-52-d4-57-19-54-37')
WdsTransportNamespace = Guid('d8385768-0732-4ec1-95-ea-16-da-58-19-08-a1')
WdsTransportNamespaceAutoCast = Guid('b091f5a8-6a99-478d-b2-3b-09-e8-fe-e0-45-74')
WdsTransportNamespaceManager = Guid('f08cdb63-85de-4a28-a1-a9-5c-a3-e7-ef-da-73')
WdsTransportNamespaceScheduledCast = Guid('badc1897-7025-44eb-91-08-fb-61-c4-05-57-92')
WdsTransportNamespaceScheduledCastAutoStart = Guid('a1107052-122c-4b81-9b-7c-38-6e-68-55-38-3f')
WdsTransportNamespaceScheduledCastManualStart = Guid('d3e1a2aa-caac-460e-b9-8a-47-f9-f3-18-a1-fa')
WdsTransportServer = Guid('ea19b643-4adf-4413-94-2c-14-f3-79-11-87-60')
WdsTransportServicePolicy = Guid('65aceadc-2f0b-4f43-9f-4d-81-18-65-d8-ce-ad')
WdsTransportSession = Guid('749ac4e0-67bc-4743-bf-e5-ca-cb-1f-26-f5-7f')
WdsTransportSetupManager = Guid('c7beeaad-9f04-4923-9f-0c-fb-f5-2b-c7-59-0f')
WdsTransportTftpClient = Guid('50343925-7c5c-4c8c-96-c4-ad-9f-a5-00-5f-ba')
WdsTransportTftpManager = Guid('c8e9dca2-3241-4e4d-b8-06-bc-74-01-9d-fe-da')
make_head(_module, 'IWdsTransportCacheable')
make_head(_module, 'IWdsTransportClient')
make_head(_module, 'IWdsTransportCollection')
make_head(_module, 'IWdsTransportConfigurationManager')
make_head(_module, 'IWdsTransportConfigurationManager2')
make_head(_module, 'IWdsTransportContent')
make_head(_module, 'IWdsTransportContentProvider')
make_head(_module, 'IWdsTransportDiagnosticsPolicy')
make_head(_module, 'IWdsTransportManager')
make_head(_module, 'IWdsTransportMulticastSessionPolicy')
make_head(_module, 'IWdsTransportNamespace')
make_head(_module, 'IWdsTransportNamespaceAutoCast')
make_head(_module, 'IWdsTransportNamespaceManager')
make_head(_module, 'IWdsTransportNamespaceScheduledCast')
make_head(_module, 'IWdsTransportNamespaceScheduledCastAutoStart')
make_head(_module, 'IWdsTransportNamespaceScheduledCastManualStart')
make_head(_module, 'IWdsTransportServer')
make_head(_module, 'IWdsTransportServer2')
make_head(_module, 'IWdsTransportServicePolicy')
make_head(_module, 'IWdsTransportServicePolicy2')
make_head(_module, 'IWdsTransportSession')
make_head(_module, 'IWdsTransportSetupManager')
make_head(_module, 'IWdsTransportSetupManager2')
make_head(_module, 'IWdsTransportTftpClient')
make_head(_module, 'IWdsTransportTftpManager')
make_head(_module, 'PFN_WdsCliCallback')
make_head(_module, 'PFN_WdsCliTraceFunction')
make_head(_module, 'PFN_WdsTransportClientReceiveContents')
make_head(_module, 'PFN_WdsTransportClientReceiveMetadata')
make_head(_module, 'PFN_WdsTransportClientSessionComplete')
make_head(_module, 'PFN_WdsTransportClientSessionNegotiate')
make_head(_module, 'PFN_WdsTransportClientSessionStart')
make_head(_module, 'PFN_WdsTransportClientSessionStartEx')
make_head(_module, 'PXE_ADDRESS')
make_head(_module, 'PXE_DHCPV6_MESSAGE')
make_head(_module, 'PXE_DHCPV6_MESSAGE_HEADER')
make_head(_module, 'PXE_DHCPV6_NESTED_RELAY_MESSAGE')
make_head(_module, 'PXE_DHCPV6_OPTION')
make_head(_module, 'PXE_DHCPV6_RELAY_MESSAGE')
make_head(_module, 'PXE_DHCP_MESSAGE')
make_head(_module, 'PXE_DHCP_OPTION')
make_head(_module, 'PXE_PROVIDER')
make_head(_module, 'TRANSPORTCLIENT_SESSION_INFO')
make_head(_module, 'WDS_CLI_CRED')
make_head(_module, 'WDS_TRANSPORTCLIENT_CALLBACKS')
make_head(_module, 'WDS_TRANSPORTCLIENT_REQUEST')
make_head(_module, 'WDS_TRANSPORTPROVIDER_INIT_PARAMS')
make_head(_module, 'WDS_TRANSPORTPROVIDER_SETTINGS')
