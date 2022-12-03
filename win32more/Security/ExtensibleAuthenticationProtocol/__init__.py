from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Security.Cryptography
import win32more.Security.ExtensibleAuthenticationProtocol
import win32more.System.Com
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
FACILITY_EAP_MESSAGE = 2114
EAP_GROUP_MASK = 65280
EAP_E_EAPHOST_FIRST = -2143158272
EAP_E_EAPHOST_LAST = -2143158017
EAP_I_EAPHOST_FIRST = -2143158272
EAP_I_EAPHOST_LAST = -2143158017
EAP_E_CERT_STORE_INACCESSIBLE = 2151809040
EAP_E_EAPHOST_METHOD_NOT_INSTALLED = 2151809041
EAP_E_EAPHOST_THIRDPARTY_METHOD_HOST_RESET = 2151809042
EAP_E_EAPHOST_EAPQEC_INACCESSIBLE = 2151809043
EAP_E_EAPHOST_IDENTITY_UNKNOWN = 2151809044
EAP_E_AUTHENTICATION_FAILED = 2151809045
EAP_I_EAPHOST_EAP_NEGOTIATION_FAILED = 1078067222
EAP_E_EAPHOST_METHOD_INVALID_PACKET = 2151809047
EAP_E_EAPHOST_REMOTE_INVALID_PACKET = 2151809048
EAP_E_EAPHOST_XML_MALFORMED = 2151809049
EAP_E_METHOD_CONFIG_DOES_NOT_SUPPORT_SSO = 2151809050
EAP_E_EAPHOST_METHOD_OPERATION_NOT_SUPPORTED = 2151809056
EAP_E_USER_FIRST = -2143158016
EAP_E_USER_LAST = -2143157761
EAP_I_USER_FIRST = 1078067456
EAP_I_USER_LAST = 1078067711
EAP_E_USER_CERT_NOT_FOUND = 2151809280
EAP_E_USER_CERT_INVALID = 2151809281
EAP_E_USER_CERT_EXPIRED = 2151809282
EAP_E_USER_CERT_REVOKED = 2151809283
EAP_E_USER_CERT_OTHER_ERROR = 2151809284
EAP_E_USER_CERT_REJECTED = 2151809285
EAP_I_USER_ACCOUNT_OTHER_ERROR = 1078067472
EAP_E_USER_CREDENTIALS_REJECTED = 2151809297
EAP_E_USER_NAME_PASSWORD_REJECTED = 2151809298
EAP_E_NO_SMART_CARD_READER = 2151809299
EAP_E_SERVER_FIRST = -2143157760
EAP_E_SERVER_LAST = -2143157505
EAP_E_SERVER_CERT_NOT_FOUND = 2151809536
EAP_E_SERVER_CERT_INVALID = 2151809537
EAP_E_SERVER_CERT_EXPIRED = 2151809538
EAP_E_SERVER_CERT_REVOKED = 2151809539
EAP_E_SERVER_CERT_OTHER_ERROR = 2151809540
EAP_E_USER_ROOT_CERT_FIRST = -2143157504
EAP_E_USER_ROOT_CERT_LAST = -2143157249
EAP_E_USER_ROOT_CERT_NOT_FOUND = 2151809792
EAP_E_USER_ROOT_CERT_INVALID = 2151809793
EAP_E_USER_ROOT_CERT_EXPIRED = 2151809794
EAP_E_SERVER_ROOT_CERT_FIRST = -2143157248
EAP_E_SERVER_ROOT_CERT_LAST = -2143156993
EAP_E_SERVER_ROOT_CERT_NOT_FOUND = 2151810048
EAP_E_SERVER_ROOT_CERT_INVALID = 2151810049
EAP_E_SERVER_ROOT_CERT_NAME_REQUIRED = 2151810054
EAP_E_SIM_NOT_VALID = 2151810304
EAP_METHOD_INVALID_PACKET = 2151809047
EAP_INVALID_PACKET = 2151809048
EAP_PEER_FLAG_GUEST_ACCESS = 64
eapPropCipherSuiteNegotiation = 1
eapPropMutualAuth = 2
eapPropIntegrity = 4
eapPropReplayProtection = 8
eapPropConfidentiality = 16
eapPropKeyDerivation = 32
eapPropKeyStrength64 = 64
eapPropKeyStrength128 = 128
eapPropKeyStrength256 = 256
eapPropKeyStrength512 = 512
eapPropKeyStrength1024 = 1024
eapPropDictionaryAttackResistance = 2048
eapPropFastReconnect = 4096
eapPropCryptoBinding = 8192
eapPropSessionIndependence = 16384
eapPropFragmentation = 32768
eapPropChannelBinding = 65536
eapPropNap = 131072
eapPropStandalone = 262144
eapPropMppeEncryption = 524288
eapPropTunnelMethod = 1048576
eapPropSupportsConfig = 2097152
eapPropCertifiedMethod = 4194304
eapPropHiddenMethod = 8388608
eapPropMachineAuth = 16777216
eapPropUserAuth = 33554432
eapPropIdentityPrivacy = 67108864
eapPropMethodChaining = 134217728
eapPropSharedStateEquivalence = 268435456
eapPropReserved = 2147483648
EAP_VALUENAME_PROPERTIES = 'Properties'
EAP_FLAG_Reserved1 = 1
EAP_FLAG_NON_INTERACTIVE = 2
EAP_FLAG_LOGON = 4
EAP_FLAG_PREVIEW = 8
EAP_FLAG_Reserved2 = 16
EAP_FLAG_MACHINE_AUTH = 32
EAP_FLAG_GUEST_ACCESS = 64
EAP_FLAG_Reserved3 = 128
EAP_FLAG_Reserved4 = 256
EAP_FLAG_RESUME_FROM_HIBERNATE = 512
EAP_FLAG_Reserved5 = 1024
EAP_FLAG_Reserved6 = 2048
EAP_FLAG_FULL_AUTH = 4096
EAP_FLAG_PREFER_ALT_CREDENTIALS = 8192
EAP_FLAG_Reserved7 = 16384
EAP_PEER_FLAG_HEALTH_STATE_CHANGE = 32768
EAP_FLAG_SUPRESS_UI = 65536
EAP_FLAG_PRE_LOGON = 131072
EAP_FLAG_USER_AUTH = 262144
EAP_FLAG_CONFG_READONLY = 524288
EAP_FLAG_Reserved8 = 1048576
EAP_FLAG_Reserved9 = 4194304
EAP_FLAG_VPN = 8388608
EAP_FLAG_ONLY_EAP_TLS = 16777216
EAP_FLAG_SERVER_VALIDATION_REQUIRED = 33554432
EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT = 0
EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE = 1
EAP_CONFIG_INPUT_FIELD_PROPS_NON_PERSIST = 2
EAP_UI_INPUT_FIELD_PROPS_DEFAULT = 0
EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE = 1
EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST = 2
EAP_UI_INPUT_FIELD_PROPS_READ_ONLY = 4
EAP_CREDENTIAL_VERSION = 1
EAP_INTERACTIVE_UI_DATA_VERSION = 1
EAPHOST_PEER_API_VERSION = 1
EAPHOST_METHOD_API_VERSION = 1
MAX_EAP_CONFIG_INPUT_FIELD_LENGTH = 256
MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH = 1024
CERTIFICATE_HASH_LENGTH = 20
NCRYPT_PIN_CACHE_PIN_BYTE_LENGTH = 90
EAP_REGISTRY_LOCATION = 'System\\CurrentControlSet\\Services\\EapHost\\Methods'
EAP_PEER_VALUENAME_DLL_PATH = 'PeerDllPath'
EAP_PEER_VALUENAME_FRIENDLY_NAME = 'PeerFriendlyName'
EAP_PEER_VALUENAME_CONFIGUI = 'PeerConfigUIPath'
EAP_PEER_VALUENAME_REQUIRE_CONFIGUI = 'PeerRequireConfigUI'
EAP_PEER_VALUENAME_IDENTITY = 'PeerIdentityPath'
EAP_PEER_VALUENAME_INTERACTIVEUI = 'PeerInteractiveUIPath'
EAP_PEER_VALUENAME_INVOKE_NAMEDLG = 'PeerInvokeUsernameDialog'
EAP_PEER_VALUENAME_INVOKE_PWDDLG = 'PeerInvokePasswordDialog'
EAP_PEER_VALUENAME_PROPERTIES = 'Properties'
EAP_AUTHENTICATOR_VALUENAME_DLL_PATH = 'AuthenticatorDllPath'
EAP_AUTHENTICATOR_VALUENAME_FRIENDLY_NAME = 'AuthenticatorFriendlyName'
EAP_AUTHENTICATOR_VALUENAME_PROPERTIES = 'Properties'
EAP_AUTHENTICATOR_VALUENAME_CONFIGUI = 'AuthenticatorConfigUIPath'
EAP_METHOD_AUTHENTICATOR_CONFIG_IS_IDENTITY_PRIVACY = 1
RAS_EAP_REGISTRY_LOCATION = 'System\\CurrentControlSet\\Services\\Rasman\\PPP\\EAP'
RAS_EAP_VALUENAME_PATH = 'Path'
RAS_EAP_VALUENAME_CONFIGUI = 'ConfigUIPath'
RAS_EAP_VALUENAME_INTERACTIVEUI = 'InteractiveUIPath'
RAS_EAP_VALUENAME_IDENTITY = 'IdentityPath'
RAS_EAP_VALUENAME_FRIENDLY_NAME = 'FriendlyName'
RAS_EAP_VALUENAME_DEFAULT_DATA = 'ConfigData'
RAS_EAP_VALUENAME_REQUIRE_CONFIGUI = 'RequireConfigUI'
RAS_EAP_VALUENAME_ENCRYPTION = 'MPPEEncryptionSupported'
RAS_EAP_VALUENAME_INVOKE_NAMEDLG = 'InvokeUsernameDialog'
RAS_EAP_VALUENAME_INVOKE_PWDDLG = 'InvokePasswordDialog'
RAS_EAP_VALUENAME_CONFIG_CLSID = 'ConfigCLSID'
RAS_EAP_VALUENAME_STANDALONE_SUPPORTED = 'StandaloneSupported'
RAS_EAP_VALUENAME_ROLES_SUPPORTED = 'RolesSupported'
RAS_EAP_VALUENAME_PER_POLICY_CONFIG = 'PerPolicyConfig'
RAS_EAP_VALUENAME_ISTUNNEL_METHOD = 'IsTunnelMethod'
RAS_EAP_VALUENAME_FILTER_INNERMETHODS = 'FilterInnerMethods'
RAS_EAP_ROLE_AUTHENTICATOR = 1
RAS_EAP_ROLE_AUTHENTICATEE = 2
RAS_EAP_ROLE_EXCLUDE_IN_EAP = 4
RAS_EAP_ROLE_EXCLUDE_IN_PEAP = 8
RAS_EAP_ROLE_EXCLUDE_IN_VPN = 16
raatARAPChallenge = 33
raatARAPOldPassword = 19
raatARAPNewPassword = 20
raatARAPPasswordChangeReason = 21
EAPCODE_Request = 1
EAPCODE_Response = 2
EAPCODE_Success = 3
EAPCODE_Failure = 4
MAXEAPCODE = 4
RAS_EAP_FLAG_ROUTER = 1
RAS_EAP_FLAG_NON_INTERACTIVE = 2
RAS_EAP_FLAG_LOGON = 4
RAS_EAP_FLAG_PREVIEW = 8
RAS_EAP_FLAG_FIRST_LINK = 16
RAS_EAP_FLAG_MACHINE_AUTH = 32
RAS_EAP_FLAG_GUEST_ACCESS = 64
RAS_EAP_FLAG_8021X_AUTH = 128
RAS_EAP_FLAG_HOSTED_IN_PEAP = 256
RAS_EAP_FLAG_RESUME_FROM_HIBERNATE = 512
RAS_EAP_FLAG_PEAP_UPFRONT = 1024
RAS_EAP_FLAG_ALTERNATIVE_USER_DB = 2048
RAS_EAP_FLAG_PEAP_FORCE_FULL_AUTH = 4096
RAS_EAP_FLAG_PRE_LOGON = 131072
RAS_EAP_FLAG_CONFG_READONLY = 524288
RAS_EAP_FLAG_RESERVED = 1048576
RAS_EAP_FLAG_SAVE_CREDMAN = 2097152
RAS_EAP_FLAG_SERVER_VALIDATION_REQUIRED = 33554432
def _define_GUID_EapHost_Default():
    return Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
def _define_GUID_EapHost_Cause_MethodDLLNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-01')
def _define_GUID_EapHost_Repair_ContactSysadmin():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-02')
def _define_GUID_EapHost_Cause_CertStoreInaccessible():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-04')
def _define_GUID_EapHost_Cause_Generic_AuthFailure():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-04')
def _define_GUID_EapHost_Cause_IdentityUnknown():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-04')
def _define_GUID_EapHost_Cause_SimNotValid():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-03-04')
def _define_GUID_EapHost_Cause_Server_CertExpired():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-05')
def _define_GUID_EapHost_Cause_Server_CertInvalid():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-06')
def _define_GUID_EapHost_Cause_Server_CertNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-07')
def _define_GUID_EapHost_Cause_Server_CertRevoked():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-08')
def _define_GUID_EapHost_Cause_Server_CertOtherError():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-08')
def _define_GUID_EapHost_Cause_User_CertExpired():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-09')
def _define_GUID_EapHost_Cause_User_CertInvalid():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0a')
def _define_GUID_EapHost_Cause_User_CertNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0b')
def _define_GUID_EapHost_Cause_User_CertOtherError():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0c')
def _define_GUID_EapHost_Cause_User_CertRejected():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0d')
def _define_GUID_EapHost_Cause_User_CertRevoked():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0e')
def _define_GUID_EapHost_Cause_User_Account_OtherProblem():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-0e')
def _define_GUID_EapHost_Cause_User_CredsRejected():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-0e')
def _define_GUID_EapHost_Cause_User_Root_CertExpired():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-0f')
def _define_GUID_EapHost_Cause_User_Root_CertInvalid():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-10')
def _define_GUID_EapHost_Cause_User_Root_CertNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-11')
def _define_GUID_EapHost_Cause_Server_Root_CertNameRequired():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-12')
def _define_GUID_EapHost_Cause_Server_Root_CertNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-12')
def _define_GUID_EapHost_Cause_ThirdPartyMethod_Host_Reset():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-02-12')
def _define_GUID_EapHost_Cause_EapQecInaccessible():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-03-12')
def _define_GUID_EapHost_Repair_Server_ClientSelectServerCert():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-18')
def _define_GUID_EapHost_Repair_User_AuthFailure():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-19')
def _define_GUID_EapHost_Repair_User_GetNewCert():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1a')
def _define_GUID_EapHost_Repair_User_SelectValidCert():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1b')
def _define_GUID_EapHost_Repair_Retry_Authentication():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-01-1b')
def _define_GUID_EapHost_Cause_EapNegotiationFailed():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1c')
def _define_GUID_EapHost_Cause_XmlMalformed():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1d')
def _define_GUID_EapHost_Cause_MethodDoesNotSupportOperation():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1e')
def _define_GUID_EapHost_Repair_ContactAdmin_AuthFailure():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-1f')
def _define_GUID_EapHost_Repair_ContactAdmin_IdentityUnknown():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-20')
def _define_GUID_EapHost_Repair_ContactAdmin_NegotiationFailed():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-21')
def _define_GUID_EapHost_Repair_ContactAdmin_MethodNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-22')
def _define_GUID_EapHost_Repair_RestartNap():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-23')
def _define_GUID_EapHost_Repair_ContactAdmin_CertStoreInaccessible():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-24')
def _define_GUID_EapHost_Repair_ContactAdmin_InvalidUserAccount():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-25')
def _define_GUID_EapHost_Repair_ContactAdmin_RootCertInvalid():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-26')
def _define_GUID_EapHost_Repair_ContactAdmin_RootCertNotFound():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-27')
def _define_GUID_EapHost_Repair_ContactAdmin_RootExpired():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-28')
def _define_GUID_EapHost_Repair_ContactAdmin_CertNameAbsent():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-29')
def _define_GUID_EapHost_Repair_ContactAdmin_NoSmartCardReader():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2a')
def _define_GUID_EapHost_Cause_No_SmartCardReader_Found():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2b')
def _define_GUID_EapHost_Repair_ContactAdmin_InvalidUserCert():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2c')
def _define_GUID_EapHost_Repair_Method_Not_Support_Sso():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2d')
def _define_GUID_EapHost_Repair_No_ValidSim_Found():
    return Guid('9612fc67-6150-4209-a8-5e-a8-d8-00-00-00-2e')
def _define_GUID_EapHost_Help_ObtainingCerts():
    return Guid('f535eea3-1bdd-46ca-a2-fc-a6-65-59-39-b7-e8')
def _define_GUID_EapHost_Help_Troubleshooting():
    return Guid('33307acf-0698-41ba-b0-14-ea-0a-2e-b8-d0-a8')
def _define_GUID_EapHost_Cause_Method_Config_Does_Not_Support_Sso():
    return Guid('da18bd32-004f-41fa-ae-08-0b-c8-5e-58-45-ac')
def _define_EapHostPeerGetMethods():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetMethods', windll['eappcfg.dll']), ((1, 'pEapMethodInfoArray'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetMethodProperties():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,win32more.Foundation.HANDLE,UInt32,c_char_p_no,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_ARRAY_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetMethodProperties', windll['eappcfg.dll']), ((1, 'dwVersion'),(1, 'dwFlags'),(1, 'eapMethodType'),(1, 'hUserImpersonationToken'),(1, 'dwEapConnDataSize'),(1, 'pbEapConnData'),(1, 'dwUserDataSize'),(1, 'pbUserData'),(1, 'pMethodPropertyArray'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerInvokeConfigUI():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerInvokeConfigUI', windll['eappcfg.dll']), ((1, 'hwndParent'),(1, 'dwFlags'),(1, 'eapMethodType'),(1, 'dwSizeOfConfigIn'),(1, 'pConfigIn'),(1, 'pdwSizeOfConfigOut'),(1, 'ppConfigOut'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerQueryCredentialInputFields():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerQueryCredentialInputFields', windll['eappcfg.dll']), ((1, 'hUserImpersonationToken'),(1, 'eapMethodType'),(1, 'dwFlags'),(1, 'dwEapConnDataSize'),(1, 'pbEapConnData'),(1, 'pEapConfigInputFieldArray'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerQueryUserBlobFromCredentialInputFields():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head),POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerQueryUserBlobFromCredentialInputFields', windll['eappcfg.dll']), ((1, 'hUserImpersonationToken'),(1, 'eapMethodType'),(1, 'dwFlags'),(1, 'dwEapConnDataSize'),(1, 'pbEapConnData'),(1, 'pEapConfigInputFieldArray'),(1, 'pdwUserBlobSize'),(1, 'ppbUserBlob'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerInvokeIdentityUI():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,win32more.Foundation.HWND,UInt32,c_char_p_no,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),POINTER(c_void_p))(('EapHostPeerInvokeIdentityUI', windll['eappcfg.dll']), ((1, 'dwVersion'),(1, 'eapMethodType'),(1, 'dwFlags'),(1, 'hwndParent'),(1, 'dwSizeofConnectionData'),(1, 'pConnectionData'),(1, 'dwSizeofUserData'),(1, 'pUserData'),(1, 'pdwSizeOfUserDataOut'),(1, 'ppUserDataOut'),(1, 'ppwszIdentity'),(1, 'ppEapError'),(1, 'ppvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerInvokeInteractiveUI():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HWND,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerInvokeInteractiveUI', windll['eappcfg.dll']), ((1, 'hwndParent'),(1, 'dwSizeofUIContextData'),(1, 'pUIContextData'),(1, 'pdwSizeOfDataFromInteractiveUI'),(1, 'ppDataFromInteractiveUI'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerQueryInteractiveUIInputFields():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),POINTER(c_void_p))(('EapHostPeerQueryInteractiveUIInputFields', windll['eappcfg.dll']), ((1, 'dwVersion'),(1, 'dwFlags'),(1, 'dwSizeofUIContextData'),(1, 'pUIContextData'),(1, 'pEapInteractiveUIData'),(1, 'ppEapError'),(1, 'ppvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerQueryUIBlobFromInteractiveUIInputFields():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head),POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),POINTER(c_void_p))(('EapHostPeerQueryUIBlobFromInteractiveUIInputFields', windll['eappcfg.dll']), ((1, 'dwVersion'),(1, 'dwFlags'),(1, 'dwSizeofUIContextData'),(1, 'pUIContextData'),(1, 'pEapInteractiveUIData'),(1, 'pdwSizeOfDataFromInteractiveUI'),(1, 'ppDataFromInteractiveUI'),(1, 'ppEapError'),(1, 'ppvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerConfigXml2Blob():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Data.Xml.MsXml.IXMLDOMNode_head,POINTER(UInt32),POINTER(c_char_p_no),POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerConfigXml2Blob', windll['eappcfg.dll']), ((1, 'dwFlags'),(1, 'pConfigDoc'),(1, 'pdwSizeOfConfigOut'),(1, 'ppConfigOut'),(1, 'pEapMethodType'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerCredentialsXml2Blob():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Data.Xml.MsXml.IXMLDOMNode_head,UInt32,c_char_p_no,POINTER(UInt32),POINTER(c_char_p_no),POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerCredentialsXml2Blob', windll['eappcfg.dll']), ((1, 'dwFlags'),(1, 'pCredentialsDoc'),(1, 'dwSizeOfConfigIn'),(1, 'pConfigIn'),(1, 'pdwSizeOfCredentialsOut'),(1, 'ppCredentialsOut'),(1, 'pEapMethodType'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerConfigBlob2Xml():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,c_char_p_no,POINTER(win32more.Data.Xml.MsXml.IXMLDOMDocument2_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerConfigBlob2Xml', windll['eappcfg.dll']), ((1, 'dwFlags'),(1, 'eapMethodType'),(1, 'dwSizeOfConfigIn'),(1, 'pConfigIn'),(1, 'ppConfigDoc'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerFreeMemory():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('EapHostPeerFreeMemory', windll['eappcfg.dll']), ((1, 'pData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerFreeErrorMemory():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))(('EapHostPeerFreeErrorMemory', windll['eappcfg.dll']), ((1, 'pEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerInitialize():
    try:
        return WINFUNCTYPE(UInt32,)(('EapHostPeerInitialize', windll['eappprxy.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerUninitialize():
    try:
        return WINFUNCTYPE(Void,)(('EapHostPeerUninitialize', windll['eappprxy.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerBeginSession():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head),win32more.Foundation.HANDLE,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,POINTER(Guid),win32more.Security.ExtensibleAuthenticationProtocol.NotificationHandler,c_void_p,POINTER(UInt32),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerBeginSession', windll['eappprxy.dll']), ((1, 'dwFlags'),(1, 'eapType'),(1, 'pAttributeArray'),(1, 'hTokenImpersonateUser'),(1, 'dwSizeofConnectionData'),(1, 'pConnectionData'),(1, 'dwSizeofUserData'),(1, 'pUserData'),(1, 'dwMaxSendPacketSize'),(1, 'pConnectionId'),(1, 'func'),(1, 'pContextData'),(1, 'pSessionId'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerProcessReceivedPacket():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerProcessReceivedPacket', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'cbReceivePacket'),(1, 'pReceivePacket'),(1, 'pEapOutput'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetSendPacket():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetSendPacket', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'pcbSendPacket'),(1, 'ppSendPacket'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetResult():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResultReason,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResult_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetResult', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'reason'),(1, 'ppResult'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetUIContext():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetUIContext', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'pdwSizeOfUIContextData'),(1, 'ppUIContextData'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerSetUIContext():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,c_char_p_no,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerSetUIContext', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'dwSizeOfUIContextData'),(1, 'pUIContextData'),(1, 'pEapOutput'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetResponseAttributes():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetResponseAttributes', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'pAttribs'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerSetResponseAttributes():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head),POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerResponseAction),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerSetResponseAttributes', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'pAttribs'),(1, 'pEapOutput'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetAuthStatus():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerAuthParams,POINTER(UInt32),POINTER(c_char_p_no),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerGetAuthStatus', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'authParam'),(1, 'pcbAuthData'),(1, 'ppAuthData'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerEndSession():
    try:
        return WINFUNCTYPE(UInt32,UInt32,POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerEndSession', windll['eappprxy.dll']), ((1, 'sessionHandle'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetDataToUnplumbCredentials():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(IntPtr),UInt32,POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),POINTER(win32more.Foundation.BOOL))(('EapHostPeerGetDataToUnplumbCredentials', windll['eappprxy.dll']), ((1, 'pConnectionIdThatLastSavedCreds'),(1, 'phCredentialImpersonationToken'),(1, 'sessionHandle'),(1, 'ppEapError'),(1, 'fSaveToCredMan'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerClearConnection():
    try:
        return WINFUNCTYPE(UInt32,POINTER(Guid),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)))(('EapHostPeerClearConnection', windll['eappprxy.dll']), ((1, 'pConnectionId'),(1, 'ppEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerFreeEapError():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head))(('EapHostPeerFreeEapError', windll['eappprxy.dll']), ((1, 'pEapError'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetIdentity():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE,UInt32,c_char_p_no,UInt32,c_char_p_no,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL),POINTER(UInt32),POINTER(c_char_p_no),POINTER(win32more.Foundation.PWSTR),POINTER(POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),POINTER(c_char_p_no))(('EapHostPeerGetIdentity', windll['eappprxy.dll']), ((1, 'dwVersion'),(1, 'dwFlags'),(1, 'eapMethodType'),(1, 'dwSizeofConnectionData'),(1, 'pConnectionData'),(1, 'dwSizeofUserData'),(1, 'pUserData'),(1, 'hTokenImpersonateUser'),(1, 'pfInvokeUI'),(1, 'pdwSizeOfUserDataOut'),(1, 'ppUserDataOut'),(1, 'ppwszIdentity'),(1, 'ppEapError'),(1, 'ppvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerGetEncryptedPassword():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('EapHostPeerGetEncryptedPassword', windll['eappprxy.dll']), ((1, 'dwSizeofPassword'),(1, 'szPassword'),(1, 'ppszEncPassword'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EapHostPeerFreeRuntimeMemory():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('EapHostPeerFreeRuntimeMemory', windll['eappprxy.dll']), ((1, 'pData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EAP_ATTRIBUTE_head():
    class EAP_ATTRIBUTE(Structure):
        pass
    return EAP_ATTRIBUTE
def _define_EAP_ATTRIBUTE():
    EAP_ATTRIBUTE = win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_head
    EAP_ATTRIBUTE._fields_ = [
        ('eaType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_TYPE),
        ('dwLength', UInt32),
        ('pValue', c_char_p_no),
    ]
    return EAP_ATTRIBUTE
EAP_ATTRIBUTE_TYPE = Int32
EAP_ATTRIBUTE_TYPE_eatMinimum = 0
EAP_ATTRIBUTE_TYPE_eatUserName = 1
EAP_ATTRIBUTE_TYPE_eatUserPassword = 2
EAP_ATTRIBUTE_TYPE_eatMD5CHAPPassword = 3
EAP_ATTRIBUTE_TYPE_eatNASIPAddress = 4
EAP_ATTRIBUTE_TYPE_eatNASPort = 5
EAP_ATTRIBUTE_TYPE_eatServiceType = 6
EAP_ATTRIBUTE_TYPE_eatFramedProtocol = 7
EAP_ATTRIBUTE_TYPE_eatFramedIPAddress = 8
EAP_ATTRIBUTE_TYPE_eatFramedIPNetmask = 9
EAP_ATTRIBUTE_TYPE_eatFramedRouting = 10
EAP_ATTRIBUTE_TYPE_eatFilterId = 11
EAP_ATTRIBUTE_TYPE_eatFramedMTU = 12
EAP_ATTRIBUTE_TYPE_eatFramedCompression = 13
EAP_ATTRIBUTE_TYPE_eatLoginIPHost = 14
EAP_ATTRIBUTE_TYPE_eatLoginService = 15
EAP_ATTRIBUTE_TYPE_eatLoginTCPPort = 16
EAP_ATTRIBUTE_TYPE_eatUnassigned17 = 17
EAP_ATTRIBUTE_TYPE_eatReplyMessage = 18
EAP_ATTRIBUTE_TYPE_eatCallbackNumber = 19
EAP_ATTRIBUTE_TYPE_eatCallbackId = 20
EAP_ATTRIBUTE_TYPE_eatUnassigned21 = 21
EAP_ATTRIBUTE_TYPE_eatFramedRoute = 22
EAP_ATTRIBUTE_TYPE_eatFramedIPXNetwork = 23
EAP_ATTRIBUTE_TYPE_eatState = 24
EAP_ATTRIBUTE_TYPE_eatClass = 25
EAP_ATTRIBUTE_TYPE_eatVendorSpecific = 26
EAP_ATTRIBUTE_TYPE_eatSessionTimeout = 27
EAP_ATTRIBUTE_TYPE_eatIdleTimeout = 28
EAP_ATTRIBUTE_TYPE_eatTerminationAction = 29
EAP_ATTRIBUTE_TYPE_eatCalledStationId = 30
EAP_ATTRIBUTE_TYPE_eatCallingStationId = 31
EAP_ATTRIBUTE_TYPE_eatNASIdentifier = 32
EAP_ATTRIBUTE_TYPE_eatProxyState = 33
EAP_ATTRIBUTE_TYPE_eatLoginLATService = 34
EAP_ATTRIBUTE_TYPE_eatLoginLATNode = 35
EAP_ATTRIBUTE_TYPE_eatLoginLATGroup = 36
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkLink = 37
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkNetwork = 38
EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkZone = 39
EAP_ATTRIBUTE_TYPE_eatAcctStatusType = 40
EAP_ATTRIBUTE_TYPE_eatAcctDelayTime = 41
EAP_ATTRIBUTE_TYPE_eatAcctInputOctets = 42
EAP_ATTRIBUTE_TYPE_eatAcctOutputOctets = 43
EAP_ATTRIBUTE_TYPE_eatAcctSessionId = 44
EAP_ATTRIBUTE_TYPE_eatAcctAuthentic = 45
EAP_ATTRIBUTE_TYPE_eatAcctSessionTime = 46
EAP_ATTRIBUTE_TYPE_eatAcctInputPackets = 47
EAP_ATTRIBUTE_TYPE_eatAcctOutputPackets = 48
EAP_ATTRIBUTE_TYPE_eatAcctTerminateCause = 49
EAP_ATTRIBUTE_TYPE_eatAcctMultiSessionId = 50
EAP_ATTRIBUTE_TYPE_eatAcctLinkCount = 51
EAP_ATTRIBUTE_TYPE_eatAcctEventTimeStamp = 55
EAP_ATTRIBUTE_TYPE_eatMD5CHAPChallenge = 60
EAP_ATTRIBUTE_TYPE_eatNASPortType = 61
EAP_ATTRIBUTE_TYPE_eatPortLimit = 62
EAP_ATTRIBUTE_TYPE_eatLoginLATPort = 63
EAP_ATTRIBUTE_TYPE_eatTunnelType = 64
EAP_ATTRIBUTE_TYPE_eatTunnelMediumType = 65
EAP_ATTRIBUTE_TYPE_eatTunnelClientEndpoint = 66
EAP_ATTRIBUTE_TYPE_eatTunnelServerEndpoint = 67
EAP_ATTRIBUTE_TYPE_eatARAPPassword = 70
EAP_ATTRIBUTE_TYPE_eatARAPFeatures = 71
EAP_ATTRIBUTE_TYPE_eatARAPZoneAccess = 72
EAP_ATTRIBUTE_TYPE_eatARAPSecurity = 73
EAP_ATTRIBUTE_TYPE_eatARAPSecurityData = 74
EAP_ATTRIBUTE_TYPE_eatPasswordRetry = 75
EAP_ATTRIBUTE_TYPE_eatPrompt = 76
EAP_ATTRIBUTE_TYPE_eatConnectInfo = 77
EAP_ATTRIBUTE_TYPE_eatConfigurationToken = 78
EAP_ATTRIBUTE_TYPE_eatEAPMessage = 79
EAP_ATTRIBUTE_TYPE_eatSignature = 80
EAP_ATTRIBUTE_TYPE_eatARAPChallengeResponse = 84
EAP_ATTRIBUTE_TYPE_eatAcctInterimInterval = 85
EAP_ATTRIBUTE_TYPE_eatNASIPv6Address = 95
EAP_ATTRIBUTE_TYPE_eatFramedInterfaceId = 96
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Prefix = 97
EAP_ATTRIBUTE_TYPE_eatLoginIPv6Host = 98
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Route = 99
EAP_ATTRIBUTE_TYPE_eatFramedIPv6Pool = 100
EAP_ATTRIBUTE_TYPE_eatARAPGuestLogon = 8096
EAP_ATTRIBUTE_TYPE_eatCertificateOID = 8097
EAP_ATTRIBUTE_TYPE_eatEAPConfiguration = 8098
EAP_ATTRIBUTE_TYPE_eatPEAPEmbeddedEAPTypeId = 8099
EAP_ATTRIBUTE_TYPE_eatPEAPFastRoamedSession = 8100
EAP_ATTRIBUTE_TYPE_eatFastRoamedSession = 8100
EAP_ATTRIBUTE_TYPE_eatEAPTLV = 8102
EAP_ATTRIBUTE_TYPE_eatCredentialsChanged = 8103
EAP_ATTRIBUTE_TYPE_eatInnerEapMethodType = 8104
EAP_ATTRIBUTE_TYPE_eatClearTextPassword = 8107
EAP_ATTRIBUTE_TYPE_eatQuarantineSoH = 8150
EAP_ATTRIBUTE_TYPE_eatCertificateThumbprint = 8250
EAP_ATTRIBUTE_TYPE_eatPeerId = 9000
EAP_ATTRIBUTE_TYPE_eatServerId = 9001
EAP_ATTRIBUTE_TYPE_eatMethodId = 9002
EAP_ATTRIBUTE_TYPE_eatEMSK = 9003
EAP_ATTRIBUTE_TYPE_eatSessionId = 9004
EAP_ATTRIBUTE_TYPE_eatReserved = -1
def _define_EAP_ATTRIBUTES_head():
    class EAP_ATTRIBUTES(Structure):
        pass
    return EAP_ATTRIBUTES
def _define_EAP_ATTRIBUTES():
    EAP_ATTRIBUTES = win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head
    EAP_ATTRIBUTES._fields_ = [
        ('dwNumberOfAttributes', UInt32),
        ('pAttribs', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTE_head)),
    ]
    return EAP_ATTRIBUTES
def _define_EAP_AUTHENTICATOR_METHOD_ROUTINES_head():
    class EAP_AUTHENTICATOR_METHOD_ROUTINES(Structure):
        pass
    return EAP_AUTHENTICATOR_METHOD_ROUTINES
def _define_EAP_AUTHENTICATOR_METHOD_ROUTINES():
    EAP_AUTHENTICATOR_METHOD_ROUTINES = win32more.Security.ExtensibleAuthenticationProtocol.EAP_AUTHENTICATOR_METHOD_ROUTINES_head
    EAP_AUTHENTICATOR_METHOD_ROUTINES._fields_ = [
        ('dwSizeInBytes', UInt32),
        ('pEapType', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head)),
        ('EapMethodAuthenticatorInitialize', IntPtr),
        ('EapMethodAuthenticatorBeginSession', IntPtr),
        ('EapMethodAuthenticatorUpdateInnerMethodParams', IntPtr),
        ('EapMethodAuthenticatorReceivePacket', IntPtr),
        ('EapMethodAuthenticatorSendPacket', IntPtr),
        ('EapMethodAuthenticatorGetAttributes', IntPtr),
        ('EapMethodAuthenticatorSetAttributes', IntPtr),
        ('EapMethodAuthenticatorGetResult', IntPtr),
        ('EapMethodAuthenticatorEndSession', IntPtr),
        ('EapMethodAuthenticatorShutdown', IntPtr),
    ]
    return EAP_AUTHENTICATOR_METHOD_ROUTINES
EAP_AUTHENTICATOR_SEND_TIMEOUT = Int32
EAP_AUTHENTICATOR_SEND_TIMEOUT_NONE = 0
EAP_AUTHENTICATOR_SEND_TIMEOUT_BASIC = 1
EAP_AUTHENTICATOR_SEND_TIMEOUT_INTERACTIVE = 2
def _define_EAP_CONFIG_INPUT_FIELD_ARRAY_head():
    class EAP_CONFIG_INPUT_FIELD_ARRAY(Structure):
        pass
    return EAP_CONFIG_INPUT_FIELD_ARRAY
def _define_EAP_CONFIG_INPUT_FIELD_ARRAY():
    EAP_CONFIG_INPUT_FIELD_ARRAY = win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head
    EAP_CONFIG_INPUT_FIELD_ARRAY._fields_ = [
        ('dwVersion', UInt32),
        ('dwNumberOfFields', UInt32),
        ('pFields', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_DATA_head)),
    ]
    return EAP_CONFIG_INPUT_FIELD_ARRAY
def _define_EAP_CONFIG_INPUT_FIELD_DATA_head():
    class EAP_CONFIG_INPUT_FIELD_DATA(Structure):
        pass
    return EAP_CONFIG_INPUT_FIELD_DATA
def _define_EAP_CONFIG_INPUT_FIELD_DATA():
    EAP_CONFIG_INPUT_FIELD_DATA = win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_DATA_head
    EAP_CONFIG_INPUT_FIELD_DATA._fields_ = [
        ('dwSize', UInt32),
        ('Type', win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_TYPE),
        ('dwFlagProps', UInt32),
        ('pwszLabel', win32more.Foundation.PWSTR),
        ('pwszData', win32more.Foundation.PWSTR),
        ('dwMinDataLength', UInt32),
        ('dwMaxDataLength', UInt32),
    ]
    return EAP_CONFIG_INPUT_FIELD_DATA
EAP_CONFIG_INPUT_FIELD_TYPE = Int32
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputUsername = 0
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPassword = 1
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkUsername = 2
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkPassword = 3
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPin = 4
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPSK = 5
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputEdit = 6
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardUsername = 7
EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardError = 8
def _define_EAP_CRED_EXPIRY_REQ_head():
    class EAP_CRED_EXPIRY_REQ(Structure):
        pass
    return EAP_CRED_EXPIRY_REQ
def _define_EAP_CRED_EXPIRY_REQ():
    EAP_CRED_EXPIRY_REQ = win32more.Security.ExtensibleAuthenticationProtocol.EAP_CRED_EXPIRY_REQ_head
    EAP_CRED_EXPIRY_REQ._fields_ = [
        ('curCreds', win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY),
        ('newCreds', win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY),
    ]
    return EAP_CRED_EXPIRY_REQ
def _define_EAP_ERROR_head():
    class EAP_ERROR(Structure):
        pass
    return EAP_ERROR
def _define_EAP_ERROR():
    EAP_ERROR = win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head
    EAP_ERROR._fields_ = [
        ('dwWinError', UInt32),
        ('type', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE),
        ('dwReasonCode', UInt32),
        ('rootCauseGuid', Guid),
        ('repairGuid', Guid),
        ('helpLinkGuid', Guid),
        ('pRootCauseString', win32more.Foundation.PWSTR),
        ('pRepairString', win32more.Foundation.PWSTR),
    ]
    return EAP_ERROR
def _define_EAP_INTERACTIVE_UI_DATA_head():
    class EAP_INTERACTIVE_UI_DATA(Structure):
        pass
    return EAP_INTERACTIVE_UI_DATA
def _define_EAP_INTERACTIVE_UI_DATA():
    EAP_INTERACTIVE_UI_DATA = win32more.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_head
    EAP_INTERACTIVE_UI_DATA._fields_ = [
        ('dwVersion', UInt32),
        ('dwSize', UInt32),
        ('dwDataType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_INTERACTIVE_UI_DATA_TYPE),
        ('cbUiData', UInt32),
        ('pbUiData', win32more.Security.ExtensibleAuthenticationProtocol.EAP_UI_DATA_FORMAT),
    ]
    return EAP_INTERACTIVE_UI_DATA
EAP_INTERACTIVE_UI_DATA_TYPE = Int32
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredReq = 0
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredResp = 1
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryReq = 2
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryResp = 3
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonReq = 4
EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonResp = 5
EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION = Int32
EAP_METHOD_AUTHENTICATOR_RESPONSE_DISCARD = 0
EAP_METHOD_AUTHENTICATOR_RESPONSE_SEND = 1
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESULT = 2
EAP_METHOD_AUTHENTICATOR_RESPONSE_RESPOND = 3
EAP_METHOD_AUTHENTICATOR_RESPONSE_AUTHENTICATE = 4
EAP_METHOD_AUTHENTICATOR_RESPONSE_HANDLE_IDENTITY = 5
def _define_EAP_METHOD_AUTHENTICATOR_RESULT_head():
    class EAP_METHOD_AUTHENTICATOR_RESULT(Structure):
        pass
    return EAP_METHOD_AUTHENTICATOR_RESULT
def _define_EAP_METHOD_AUTHENTICATOR_RESULT():
    EAP_METHOD_AUTHENTICATOR_RESULT = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_AUTHENTICATOR_RESULT_head
    EAP_METHOD_AUTHENTICATOR_RESULT._fields_ = [
        ('fIsSuccess', win32more.Foundation.BOOL),
        ('dwFailureReason', UInt32),
        ('pAuthAttribs', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)),
    ]
    return EAP_METHOD_AUTHENTICATOR_RESULT
def _define_EAP_METHOD_INFO_head():
    class EAP_METHOD_INFO(Structure):
        pass
    return EAP_METHOD_INFO
def _define_EAP_METHOD_INFO():
    EAP_METHOD_INFO = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head
    EAP_METHOD_INFO._fields_ = [
        ('eaptype', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE),
        ('pwszAuthorName', win32more.Foundation.PWSTR),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('eapProperties', UInt32),
        ('pInnerMethodInfo', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)),
    ]
    return EAP_METHOD_INFO
def _define_EAP_METHOD_INFO_ARRAY_head():
    class EAP_METHOD_INFO_ARRAY(Structure):
        pass
    return EAP_METHOD_INFO_ARRAY
def _define_EAP_METHOD_INFO_ARRAY():
    EAP_METHOD_INFO_ARRAY = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_head
    EAP_METHOD_INFO_ARRAY._fields_ = [
        ('dwNumberOfMethods', UInt32),
        ('pEapMethods', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)),
    ]
    return EAP_METHOD_INFO_ARRAY
def _define_EAP_METHOD_INFO_ARRAY_EX_head():
    class EAP_METHOD_INFO_ARRAY_EX(Structure):
        pass
    return EAP_METHOD_INFO_ARRAY_EX
def _define_EAP_METHOD_INFO_ARRAY_EX():
    EAP_METHOD_INFO_ARRAY_EX = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_EX_head
    EAP_METHOD_INFO_ARRAY_EX._fields_ = [
        ('dwNumberOfMethods', UInt32),
        ('pEapMethods', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_EX_head)),
    ]
    return EAP_METHOD_INFO_ARRAY_EX
def _define_EAP_METHOD_INFO_EX_head():
    class EAP_METHOD_INFO_EX(Structure):
        pass
    return EAP_METHOD_INFO_EX
def _define_EAP_METHOD_INFO_EX():
    EAP_METHOD_INFO_EX = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_EX_head
    EAP_METHOD_INFO_EX._fields_ = [
        ('eaptype', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE),
        ('pwszAuthorName', win32more.Foundation.PWSTR),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('eapProperties', UInt32),
        ('pInnerMethodInfoArray', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_ARRAY_EX_head)),
    ]
    return EAP_METHOD_INFO_EX
def _define_EAP_METHOD_PROPERTY_head():
    class EAP_METHOD_PROPERTY(Structure):
        pass
    return EAP_METHOD_PROPERTY
def _define_EAP_METHOD_PROPERTY():
    EAP_METHOD_PROPERTY = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_head
    EAP_METHOD_PROPERTY._fields_ = [
        ('eapMethodPropertyType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_TYPE),
        ('eapMethodPropertyValueType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_TYPE),
        ('eapMethodPropertyValue', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE),
    ]
    return EAP_METHOD_PROPERTY
def _define_EAP_METHOD_PROPERTY_ARRAY_head():
    class EAP_METHOD_PROPERTY_ARRAY(Structure):
        pass
    return EAP_METHOD_PROPERTY_ARRAY
def _define_EAP_METHOD_PROPERTY_ARRAY():
    EAP_METHOD_PROPERTY_ARRAY = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_ARRAY_head
    EAP_METHOD_PROPERTY_ARRAY._fields_ = [
        ('dwNumberOfProperties', UInt32),
        ('pMethodProperty', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_head)),
    ]
    return EAP_METHOD_PROPERTY_ARRAY
EAP_METHOD_PROPERTY_TYPE = Int32
EAP_METHOD_PROPERTY_TYPE_emptPropCipherSuiteNegotiation = 0
EAP_METHOD_PROPERTY_TYPE_emptPropMutualAuth = 1
EAP_METHOD_PROPERTY_TYPE_emptPropIntegrity = 2
EAP_METHOD_PROPERTY_TYPE_emptPropReplayProtection = 3
EAP_METHOD_PROPERTY_TYPE_emptPropConfidentiality = 4
EAP_METHOD_PROPERTY_TYPE_emptPropKeyDerivation = 5
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength64 = 6
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength128 = 7
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength256 = 8
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength512 = 9
EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength1024 = 10
EAP_METHOD_PROPERTY_TYPE_emptPropDictionaryAttackResistance = 11
EAP_METHOD_PROPERTY_TYPE_emptPropFastReconnect = 12
EAP_METHOD_PROPERTY_TYPE_emptPropCryptoBinding = 13
EAP_METHOD_PROPERTY_TYPE_emptPropSessionIndependence = 14
EAP_METHOD_PROPERTY_TYPE_emptPropFragmentation = 15
EAP_METHOD_PROPERTY_TYPE_emptPropChannelBinding = 16
EAP_METHOD_PROPERTY_TYPE_emptPropNap = 17
EAP_METHOD_PROPERTY_TYPE_emptPropStandalone = 18
EAP_METHOD_PROPERTY_TYPE_emptPropMppeEncryption = 19
EAP_METHOD_PROPERTY_TYPE_emptPropTunnelMethod = 20
EAP_METHOD_PROPERTY_TYPE_emptPropSupportsConfig = 21
EAP_METHOD_PROPERTY_TYPE_emptPropCertifiedMethod = 22
EAP_METHOD_PROPERTY_TYPE_emptPropHiddenMethod = 23
EAP_METHOD_PROPERTY_TYPE_emptPropMachineAuth = 24
EAP_METHOD_PROPERTY_TYPE_emptPropUserAuth = 25
EAP_METHOD_PROPERTY_TYPE_emptPropIdentityPrivacy = 26
EAP_METHOD_PROPERTY_TYPE_emptPropMethodChaining = 27
EAP_METHOD_PROPERTY_TYPE_emptPropSharedStateEquivalence = 28
EAP_METHOD_PROPERTY_TYPE_emptLegacyMethodPropertyFlag = 31
EAP_METHOD_PROPERTY_TYPE_emptPropVendorSpecific = 255
def _define_EAP_METHOD_PROPERTY_VALUE_head():
    class EAP_METHOD_PROPERTY_VALUE(Union):
        pass
    return EAP_METHOD_PROPERTY_VALUE
def _define_EAP_METHOD_PROPERTY_VALUE():
    EAP_METHOD_PROPERTY_VALUE = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_head
    EAP_METHOD_PROPERTY_VALUE._fields_ = [
        ('empvBool', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_BOOL),
        ('empvDword', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_DWORD),
        ('empvString', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_STRING),
    ]
    return EAP_METHOD_PROPERTY_VALUE
def _define_EAP_METHOD_PROPERTY_VALUE_BOOL_head():
    class EAP_METHOD_PROPERTY_VALUE_BOOL(Structure):
        pass
    return EAP_METHOD_PROPERTY_VALUE_BOOL
def _define_EAP_METHOD_PROPERTY_VALUE_BOOL():
    EAP_METHOD_PROPERTY_VALUE_BOOL = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_BOOL_head
    EAP_METHOD_PROPERTY_VALUE_BOOL._fields_ = [
        ('length', UInt32),
        ('value', win32more.Foundation.BOOL),
    ]
    return EAP_METHOD_PROPERTY_VALUE_BOOL
def _define_EAP_METHOD_PROPERTY_VALUE_DWORD_head():
    class EAP_METHOD_PROPERTY_VALUE_DWORD(Structure):
        pass
    return EAP_METHOD_PROPERTY_VALUE_DWORD
def _define_EAP_METHOD_PROPERTY_VALUE_DWORD():
    EAP_METHOD_PROPERTY_VALUE_DWORD = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_DWORD_head
    EAP_METHOD_PROPERTY_VALUE_DWORD._fields_ = [
        ('length', UInt32),
        ('value', UInt32),
    ]
    return EAP_METHOD_PROPERTY_VALUE_DWORD
def _define_EAP_METHOD_PROPERTY_VALUE_STRING_head():
    class EAP_METHOD_PROPERTY_VALUE_STRING(Structure):
        pass
    return EAP_METHOD_PROPERTY_VALUE_STRING
def _define_EAP_METHOD_PROPERTY_VALUE_STRING():
    EAP_METHOD_PROPERTY_VALUE_STRING = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_PROPERTY_VALUE_STRING_head
    EAP_METHOD_PROPERTY_VALUE_STRING._fields_ = [
        ('length', UInt32),
        ('value', c_char_p_no),
    ]
    return EAP_METHOD_PROPERTY_VALUE_STRING
EAP_METHOD_PROPERTY_VALUE_TYPE = Int32
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtBool = 0
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtDword = 1
EAP_METHOD_PROPERTY_VALUE_TYPE_empvtString = 2
def _define_EAP_METHOD_TYPE_head():
    class EAP_METHOD_TYPE(Structure):
        pass
    return EAP_METHOD_TYPE
def _define_EAP_METHOD_TYPE():
    EAP_METHOD_TYPE = win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE_head
    EAP_METHOD_TYPE._fields_ = [
        ('eapType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_TYPE),
        ('dwAuthorId', UInt32),
    ]
    return EAP_METHOD_TYPE
def _define_EAP_PEER_METHOD_ROUTINES_head():
    class EAP_PEER_METHOD_ROUTINES(Structure):
        pass
    return EAP_PEER_METHOD_ROUTINES
def _define_EAP_PEER_METHOD_ROUTINES():
    EAP_PEER_METHOD_ROUTINES = win32more.Security.ExtensibleAuthenticationProtocol.EAP_PEER_METHOD_ROUTINES_head
    EAP_PEER_METHOD_ROUTINES._fields_ = [
        ('dwVersion', UInt32),
        ('pEapType', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_TYPE_head)),
        ('EapPeerInitialize', IntPtr),
        ('EapPeerGetIdentity', IntPtr),
        ('EapPeerBeginSession', IntPtr),
        ('EapPeerSetCredentials', IntPtr),
        ('EapPeerProcessRequestPacket', IntPtr),
        ('EapPeerGetResponsePacket', IntPtr),
        ('EapPeerGetResult', IntPtr),
        ('EapPeerGetUIContext', IntPtr),
        ('EapPeerSetUIContext', IntPtr),
        ('EapPeerGetResponseAttributes', IntPtr),
        ('EapPeerSetResponseAttributes', IntPtr),
        ('EapPeerEndSession', IntPtr),
        ('EapPeerShutdown', IntPtr),
    ]
    return EAP_PEER_METHOD_ROUTINES
def _define_EAP_TYPE_head():
    class EAP_TYPE(Structure):
        pass
    return EAP_TYPE
def _define_EAP_TYPE():
    EAP_TYPE = win32more.Security.ExtensibleAuthenticationProtocol.EAP_TYPE_head
    EAP_TYPE._fields_ = [
        ('type', Byte),
        ('dwVendorId', UInt32),
        ('dwVendorType', UInt32),
    ]
    return EAP_TYPE
def _define_EAP_UI_DATA_FORMAT_head():
    class EAP_UI_DATA_FORMAT(Union):
        pass
    return EAP_UI_DATA_FORMAT
def _define_EAP_UI_DATA_FORMAT():
    EAP_UI_DATA_FORMAT = win32more.Security.ExtensibleAuthenticationProtocol.EAP_UI_DATA_FORMAT_head
    EAP_UI_DATA_FORMAT._fields_ = [
        ('credData', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)),
        ('credExpiryData', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CRED_EXPIRY_REQ_head)),
        ('credLogonData', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_CONFIG_INPUT_FIELD_ARRAY_head)),
    ]
    return EAP_UI_DATA_FORMAT
def _define_EapCertificateCredential_head():
    class EapCertificateCredential(Structure):
        pass
    return EapCertificateCredential
def _define_EapCertificateCredential():
    EapCertificateCredential = win32more.Security.ExtensibleAuthenticationProtocol.EapCertificateCredential_head
    EapCertificateCredential._fields_ = [
        ('certHash', Byte * 20),
        ('password', win32more.Foundation.PWSTR),
    ]
    return EapCertificateCredential
EapCode = Int32
EapCode_EapCodeMinimum = 1
EapCode_EapCodeRequest = 1
EapCode_EapCodeResponse = 2
EapCode_EapCodeSuccess = 3
EapCode_EapCodeFailure = 4
EapCode_EapCodeMaximum = 4
def _define_EapCredential_head():
    class EapCredential(Structure):
        pass
    return EapCredential
def _define_EapCredential():
    EapCredential = win32more.Security.ExtensibleAuthenticationProtocol.EapCredential_head
    EapCredential._fields_ = [
        ('credType', win32more.Security.ExtensibleAuthenticationProtocol.EapCredentialType),
        ('credData', win32more.Security.ExtensibleAuthenticationProtocol.EapCredentialTypeData),
    ]
    return EapCredential
EapCredentialType = Int32
EAP_EMPTY_CREDENTIAL = 0
EAP_USERNAME_PASSWORD_CREDENTIAL = 1
EAP_WINLOGON_CREDENTIAL = 2
EAP_CERTIFICATE_CREDENTIAL = 3
EAP_SIM_CREDENTIAL = 4
def _define_EapCredentialTypeData_head():
    class EapCredentialTypeData(Union):
        pass
    return EapCredentialTypeData
def _define_EapCredentialTypeData():
    EapCredentialTypeData = win32more.Security.ExtensibleAuthenticationProtocol.EapCredentialTypeData_head
    EapCredentialTypeData._fields_ = [
        ('username_password', win32more.Security.ExtensibleAuthenticationProtocol.EapUsernamePasswordCredential),
        ('certificate', win32more.Security.ExtensibleAuthenticationProtocol.EapCertificateCredential),
        ('sim', win32more.Security.ExtensibleAuthenticationProtocol.EapSimCredential),
    ]
    return EapCredentialTypeData
def _define_EAPHOST_AUTH_INFO_head():
    class EAPHOST_AUTH_INFO(Structure):
        pass
    return EAPHOST_AUTH_INFO
def _define_EAPHOST_AUTH_INFO():
    EAPHOST_AUTH_INFO = win32more.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_INFO_head
    EAPHOST_AUTH_INFO._fields_ = [
        ('status', win32more.Security.ExtensibleAuthenticationProtocol.EAPHOST_AUTH_STATUS),
        ('dwErrorCode', UInt32),
        ('dwReasonCode', UInt32),
    ]
    return EAPHOST_AUTH_INFO
EAPHOST_AUTH_STATUS = Int32
EAPHOST_AUTH_STATUS_EapHostInvalidSession = 0
EAPHOST_AUTH_STATUS_EapHostAuthNotStarted = 1
EAPHOST_AUTH_STATUS_EapHostAuthIdentityExchange = 2
EAPHOST_AUTH_STATUS_EapHostAuthNegotiatingType = 3
EAPHOST_AUTH_STATUS_EapHostAuthInProgress = 4
EAPHOST_AUTH_STATUS_EapHostAuthSucceeded = 5
EAPHOST_AUTH_STATUS_EapHostAuthFailed = 6
def _define_EAPHOST_IDENTITY_UI_PARAMS_head():
    class EAPHOST_IDENTITY_UI_PARAMS(Structure):
        pass
    return EAPHOST_IDENTITY_UI_PARAMS
def _define_EAPHOST_IDENTITY_UI_PARAMS():
    EAPHOST_IDENTITY_UI_PARAMS = win32more.Security.ExtensibleAuthenticationProtocol.EAPHOST_IDENTITY_UI_PARAMS_head
    EAPHOST_IDENTITY_UI_PARAMS._fields_ = [
        ('eapMethodType', win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_TYPE),
        ('dwFlags', UInt32),
        ('dwSizeofConnectionData', UInt32),
        ('pConnectionData', c_char_p_no),
        ('dwSizeofUserData', UInt32),
        ('pUserData', c_char_p_no),
        ('dwSizeofUserDataOut', UInt32),
        ('pUserDataOut', c_char_p_no),
        ('pwszIdentity', win32more.Foundation.PWSTR),
        ('dwError', UInt32),
        ('pEapError', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),
    ]
    return EAPHOST_IDENTITY_UI_PARAMS
def _define_EAPHOST_INTERACTIVE_UI_PARAMS_head():
    class EAPHOST_INTERACTIVE_UI_PARAMS(Structure):
        pass
    return EAPHOST_INTERACTIVE_UI_PARAMS
def _define_EAPHOST_INTERACTIVE_UI_PARAMS():
    EAPHOST_INTERACTIVE_UI_PARAMS = win32more.Security.ExtensibleAuthenticationProtocol.EAPHOST_INTERACTIVE_UI_PARAMS_head
    EAPHOST_INTERACTIVE_UI_PARAMS._fields_ = [
        ('dwSizeofContextData', UInt32),
        ('pContextData', c_char_p_no),
        ('dwSizeofInteractiveUIData', UInt32),
        ('pInteractiveUIData', c_char_p_no),
        ('dwError', UInt32),
        ('pEapError', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),
    ]
    return EAPHOST_INTERACTIVE_UI_PARAMS
EapHostPeerAuthParams = Int32
EapHostPeerAuthParams_EapHostPeerAuthStatus = 1
EapHostPeerAuthParams_EapHostPeerIdentity = 2
EapHostPeerAuthParams_EapHostPeerIdentityExtendedInfo = 3
EapHostPeerAuthParams_EapHostNapInfo = 4
def _define_EapHostPeerMethodResult_head():
    class EapHostPeerMethodResult(Structure):
        pass
    return EapHostPeerMethodResult
def _define_EapHostPeerMethodResult():
    EapHostPeerMethodResult = win32more.Security.ExtensibleAuthenticationProtocol.EapHostPeerMethodResult_head
    EapHostPeerMethodResult._fields_ = [
        ('fIsSuccess', win32more.Foundation.BOOL),
        ('dwFailureReasonCode', UInt32),
        ('fSaveConnectionData', win32more.Foundation.BOOL),
        ('dwSizeofConnectionData', UInt32),
        ('pConnectionData', c_char_p_no),
        ('fSaveUserData', win32more.Foundation.BOOL),
        ('dwSizeofUserData', UInt32),
        ('pUserData', c_char_p_no),
        ('pAttribArray', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)),
        ('isolationState', win32more.Security.ExtensibleAuthenticationProtocol.ISOLATION_STATE),
        ('pEapMethodInfo', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_METHOD_INFO_head)),
        ('pEapError', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),
    ]
    return EapHostPeerMethodResult
EapHostPeerMethodResultReason = Int32
EapHostPeerMethodResultReason_EapHostPeerMethodResultAltSuccessReceived = 1
EapHostPeerMethodResultReason_EapHostPeerMethodResultTimeout = 2
EapHostPeerMethodResultReason_EapHostPeerMethodResultFromMethod = 3
EapHostPeerResponseAction = Int32
EapHostPeerResponseAction_EapHostPeerResponseDiscard = 0
EapHostPeerResponseAction_EapHostPeerResponseSend = 1
EapHostPeerResponseAction_EapHostPeerResponseResult = 2
EapHostPeerResponseAction_EapHostPeerResponseInvokeUi = 3
EapHostPeerResponseAction_EapHostPeerResponseRespond = 4
EapHostPeerResponseAction_EapHostPeerResponseStartAuthentication = 5
EapHostPeerResponseAction_EapHostPeerResponseNone = 6
def _define_EapPacket_head():
    class EapPacket(Structure):
        pass
    return EapPacket
def _define_EapPacket():
    EapPacket = win32more.Security.ExtensibleAuthenticationProtocol.EapPacket_head
    EapPacket._fields_ = [
        ('Code', Byte),
        ('Id', Byte),
        ('Length', Byte * 2),
        ('Data', Byte * 1),
    ]
    return EapPacket
def _define_EapPeerMethodOutput_head():
    class EapPeerMethodOutput(Structure):
        pass
    return EapPeerMethodOutput
def _define_EapPeerMethodOutput():
    EapPeerMethodOutput = win32more.Security.ExtensibleAuthenticationProtocol.EapPeerMethodOutput_head
    EapPeerMethodOutput._fields_ = [
        ('action', win32more.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResponseAction),
        ('fAllowNotifications', win32more.Foundation.BOOL),
    ]
    return EapPeerMethodOutput
EapPeerMethodResponseAction = Int32
EapPeerMethodResponseAction_EapPeerMethodResponseActionDiscard = 0
EapPeerMethodResponseAction_EapPeerMethodResponseActionSend = 1
EapPeerMethodResponseAction_EapPeerMethodResponseActionResult = 2
EapPeerMethodResponseAction_EapPeerMethodResponseActionInvokeUI = 3
EapPeerMethodResponseAction_EapPeerMethodResponseActionRespond = 4
EapPeerMethodResponseAction_EapPeerMethodResponseActionNone = 5
def _define_EapPeerMethodResult_head():
    class EapPeerMethodResult(Structure):
        pass
    return EapPeerMethodResult
def _define_EapPeerMethodResult():
    EapPeerMethodResult = win32more.Security.ExtensibleAuthenticationProtocol.EapPeerMethodResult_head
    EapPeerMethodResult._fields_ = [
        ('fIsSuccess', win32more.Foundation.BOOL),
        ('dwFailureReasonCode', UInt32),
        ('fSaveConnectionData', win32more.Foundation.BOOL),
        ('dwSizeofConnectionData', UInt32),
        ('pConnectionData', c_char_p_no),
        ('fSaveUserData', win32more.Foundation.BOOL),
        ('dwSizeofUserData', UInt32),
        ('pUserData', c_char_p_no),
        ('pAttribArray', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ATTRIBUTES_head)),
        ('pEapError', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.EAP_ERROR_head)),
        ('pNgcKerbTicket', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)),
        ('fSaveToCredMan', win32more.Foundation.BOOL),
    ]
    return EapPeerMethodResult
EapPeerMethodResultReason = Int32
EapPeerMethodResultReason_EapPeerMethodResultUnknown = 1
EapPeerMethodResultReason_EapPeerMethodResultSuccess = 2
EapPeerMethodResultReason_EapPeerMethodResultFailure = 3
def _define_EapSimCredential_head():
    class EapSimCredential(Structure):
        pass
    return EapSimCredential
def _define_EapSimCredential():
    EapSimCredential = win32more.Security.ExtensibleAuthenticationProtocol.EapSimCredential_head
    EapSimCredential._fields_ = [
        ('iccID', win32more.Foundation.PWSTR),
    ]
    return EapSimCredential
def _define_EapUsernamePasswordCredential_head():
    class EapUsernamePasswordCredential(Structure):
        pass
    return EapUsernamePasswordCredential
def _define_EapUsernamePasswordCredential():
    EapUsernamePasswordCredential = win32more.Security.ExtensibleAuthenticationProtocol.EapUsernamePasswordCredential_head
    EapUsernamePasswordCredential._fields_ = [
        ('username', win32more.Foundation.PWSTR),
        ('password', win32more.Foundation.PWSTR),
    ]
    return EapUsernamePasswordCredential
def _define_IAccountingProviderConfig_head():
    class IAccountingProviderConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('66a2db18-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    return IAccountingProviderConfig
def _define_IAccountingProviderConfig():
    IAccountingProviderConfig = win32more.Security.ExtensibleAuthenticationProtocol.IAccountingProviderConfig_head
    IAccountingProviderConfig.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UIntPtr))(3, 'Initialize', ((1, 'pszMachineName'),(1, 'puConnectionParam'),)))
    IAccountingProviderConfig.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr)(4, 'Uninitialize', ((1, 'uConnectionParam'),)))
    IAccountingProviderConfig.Configure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.Foundation.HWND,UInt32,UIntPtr,UIntPtr)(5, 'Configure', ((1, 'uConnectionParam'),(1, 'hWnd'),(1, 'dwFlags'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    IAccountingProviderConfig.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,UIntPtr)(6, 'Activate', ((1, 'uConnectionParam'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    IAccountingProviderConfig.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,UIntPtr)(7, 'Deactivate', ((1, 'uConnectionParam'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    win32more.System.Com.IUnknown
    return IAccountingProviderConfig
def _define_IAuthenticationProviderConfig_head():
    class IAuthenticationProviderConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('66a2db17-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    return IAuthenticationProviderConfig
def _define_IAuthenticationProviderConfig():
    IAuthenticationProviderConfig = win32more.Security.ExtensibleAuthenticationProtocol.IAuthenticationProviderConfig_head
    IAuthenticationProviderConfig.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(UIntPtr))(3, 'Initialize', ((1, 'pszMachineName'),(1, 'puConnectionParam'),)))
    IAuthenticationProviderConfig.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr)(4, 'Uninitialize', ((1, 'uConnectionParam'),)))
    IAuthenticationProviderConfig.Configure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,win32more.Foundation.HWND,UInt32,UIntPtr,UIntPtr)(5, 'Configure', ((1, 'uConnectionParam'),(1, 'hWnd'),(1, 'dwFlags'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    IAuthenticationProviderConfig.Activate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,UIntPtr)(6, 'Activate', ((1, 'uConnectionParam'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    IAuthenticationProviderConfig.Deactivate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr,UIntPtr,UIntPtr)(7, 'Deactivate', ((1, 'uConnectionParam'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    win32more.System.Com.IUnknown
    return IAuthenticationProviderConfig
def _define_IEAPProviderConfig_head():
    class IEAPProviderConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('66a2db19-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    return IEAPProviderConfig
def _define_IEAPProviderConfig():
    IEAPProviderConfig = win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig_head
    IEAPProviderConfig.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,POINTER(UIntPtr))(3, 'Initialize', ((1, 'pszMachineName'),(1, 'dwEapTypeId'),(1, 'puConnectionParam'),)))
    IEAPProviderConfig.Uninitialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr)(4, 'Uninitialize', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),)))
    IEAPProviderConfig.ServerInvokeConfigUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.Foundation.HWND,UIntPtr,UIntPtr)(5, 'ServerInvokeConfigUI', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),(1, 'hWnd'),(1, 'uReserved1'),(1, 'uReserved2'),)))
    IEAPProviderConfig.RouterInvokeConfigUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.Foundation.HWND,UInt32,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(6, 'RouterInvokeConfigUI', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),(1, 'hwndParent'),(1, 'dwFlags'),(1, 'pConnectionDataIn'),(1, 'dwSizeOfConnectionDataIn'),(1, 'ppConnectionDataOut'),(1, 'pdwSizeOfConnectionDataOut'),)))
    IEAPProviderConfig.RouterInvokeCredentialsUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.Foundation.HWND,UInt32,c_char_p_no,UInt32,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(7, 'RouterInvokeCredentialsUI', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),(1, 'hwndParent'),(1, 'dwFlags'),(1, 'pConnectionDataIn'),(1, 'dwSizeOfConnectionDataIn'),(1, 'pUserDataIn'),(1, 'dwSizeOfUserDataIn'),(1, 'ppUserDataOut'),(1, 'pdwSizeOfUserDataOut'),)))
    win32more.System.Com.IUnknown
    return IEAPProviderConfig
def _define_IEAPProviderConfig2_head():
    class IEAPProviderConfig2(win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig_head):
        Guid = Guid('d565917a-85c4-4466-85-6e-67-1c-37-42-ea-9a')
    return IEAPProviderConfig2
def _define_IEAPProviderConfig2():
    IEAPProviderConfig2 = win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig2_head
    IEAPProviderConfig2.ServerInvokeConfigUI2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.Foundation.HWND,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(8, 'ServerInvokeConfigUI2', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),(1, 'hWnd'),(1, 'pConfigDataIn'),(1, 'dwSizeOfConfigDataIn'),(1, 'ppConfigDataOut'),(1, 'pdwSizeOfConfigDataOut'),)))
    IEAPProviderConfig2.GetGlobalConfig = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(c_char_p_no),POINTER(UInt32))(9, 'GetGlobalConfig', ((1, 'dwEapTypeId'),(1, 'ppConfigDataOut'),(1, 'pdwSizeOfConfigDataOut'),)))
    win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig
    return IEAPProviderConfig2
def _define_IEAPProviderConfig3_head():
    class IEAPProviderConfig3(win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig2_head):
        Guid = Guid('b78ecd12-68bb-4f86-9b-f0-84-38-dd-3b-e9-82')
    return IEAPProviderConfig3
def _define_IEAPProviderConfig3():
    IEAPProviderConfig3 = win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig3_head
    IEAPProviderConfig3.ServerInvokeCertificateConfigUI = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UIntPtr,win32more.Foundation.HWND,c_char_p_no,UInt32,POINTER(c_char_p_no),POINTER(UInt32),UIntPtr)(10, 'ServerInvokeCertificateConfigUI', ((1, 'dwEapTypeId'),(1, 'uConnectionParam'),(1, 'hWnd'),(1, 'pConfigDataIn'),(1, 'dwSizeOfConfigDataIn'),(1, 'ppConfigDataOut'),(1, 'pdwSizeOfConfigDataOut'),(1, 'uReserved'),)))
    win32more.Security.ExtensibleAuthenticationProtocol.IEAPProviderConfig2
    return IEAPProviderConfig3
def _define_IRouterProtocolConfig_head():
    class IRouterProtocolConfig(win32more.System.Com.IUnknown_head):
        Guid = Guid('66a2db16-d706-11d0-a3-7b-00-c0-4f-c9-da-04')
    return IRouterProtocolConfig
def _define_IRouterProtocolConfig():
    IRouterProtocolConfig = win32more.Security.ExtensibleAuthenticationProtocol.IRouterProtocolConfig_head
    IRouterProtocolConfig.AddProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.HWND,UInt32,win32more.System.Com.IUnknown_head,UIntPtr)(3, 'AddProtocol', ((1, 'pszMachineName'),(1, 'dwTransportId'),(1, 'dwProtocolId'),(1, 'hWnd'),(1, 'dwFlags'),(1, 'pRouter'),(1, 'uReserved1'),)))
    IRouterProtocolConfig.RemoveProtocol = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,UInt32,win32more.Foundation.HWND,UInt32,win32more.System.Com.IUnknown_head,UIntPtr)(4, 'RemoveProtocol', ((1, 'pszMachineName'),(1, 'dwTransportId'),(1, 'dwProtocolId'),(1, 'hWnd'),(1, 'dwFlags'),(1, 'pRouter'),(1, 'uReserved1'),)))
    win32more.System.Com.IUnknown
    return IRouterProtocolConfig
ISOLATION_STATE = Int32
ISOLATION_STATE_UNKNOWN = 0
ISOLATION_STATE_NOT_RESTRICTED = 1
ISOLATION_STATE_IN_PROBATION = 2
ISOLATION_STATE_RESTRICTED_ACCESS = 3
def _define_LEGACY_IDENTITY_UI_PARAMS_head():
    class LEGACY_IDENTITY_UI_PARAMS(Structure):
        pass
    return LEGACY_IDENTITY_UI_PARAMS
def _define_LEGACY_IDENTITY_UI_PARAMS():
    LEGACY_IDENTITY_UI_PARAMS = win32more.Security.ExtensibleAuthenticationProtocol.LEGACY_IDENTITY_UI_PARAMS_head
    LEGACY_IDENTITY_UI_PARAMS._fields_ = [
        ('eapType', UInt32),
        ('dwFlags', UInt32),
        ('dwSizeofConnectionData', UInt32),
        ('pConnectionData', c_char_p_no),
        ('dwSizeofUserData', UInt32),
        ('pUserData', c_char_p_no),
        ('dwSizeofUserDataOut', UInt32),
        ('pUserDataOut', c_char_p_no),
        ('pwszIdentity', win32more.Foundation.PWSTR),
        ('dwError', UInt32),
    ]
    return LEGACY_IDENTITY_UI_PARAMS
def _define_LEGACY_INTERACTIVE_UI_PARAMS_head():
    class LEGACY_INTERACTIVE_UI_PARAMS(Structure):
        pass
    return LEGACY_INTERACTIVE_UI_PARAMS
def _define_LEGACY_INTERACTIVE_UI_PARAMS():
    LEGACY_INTERACTIVE_UI_PARAMS = win32more.Security.ExtensibleAuthenticationProtocol.LEGACY_INTERACTIVE_UI_PARAMS_head
    LEGACY_INTERACTIVE_UI_PARAMS._fields_ = [
        ('eapType', UInt32),
        ('dwSizeofContextData', UInt32),
        ('pContextData', c_char_p_no),
        ('dwSizeofInteractiveUIData', UInt32),
        ('pInteractiveUIData', c_char_p_no),
        ('dwError', UInt32),
    ]
    return LEGACY_INTERACTIVE_UI_PARAMS
def _define_NgcTicketContext_head():
    class NgcTicketContext(Structure):
        pass
    return NgcTicketContext
def _define_NgcTicketContext():
    NgcTicketContext = win32more.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head
    NgcTicketContext._fields_ = [
        ('wszTicket', Char * 45),
        ('hKey', win32more.Security.Cryptography.NCRYPT_KEY_HANDLE),
        ('hImpersonateToken', win32more.Foundation.HANDLE),
    ]
    return NgcTicketContext
def _define_NotificationHandler():
    return WINFUNCTYPE(Void,Guid,c_void_p)
PPP_EAP_ACTION = Int32
EAPACTION_NoAction = 0
EAPACTION_Authenticate = 1
EAPACTION_Done = 2
EAPACTION_SendAndDone = 3
EAPACTION_Send = 4
EAPACTION_SendWithTimeout = 5
EAPACTION_SendWithTimeoutInteractive = 6
EAPACTION_IndicateTLV = 7
EAPACTION_IndicateIdentity = 8
def _define_PPP_EAP_INFO_head():
    class PPP_EAP_INFO(Structure):
        pass
    return PPP_EAP_INFO
def _define_PPP_EAP_INFO():
    PPP_EAP_INFO = win32more.Security.ExtensibleAuthenticationProtocol.PPP_EAP_INFO_head
    PPP_EAP_INFO._fields_ = [
        ('dwSizeInBytes', UInt32),
        ('dwEapTypeId', UInt32),
        ('RasEapInitialize', IntPtr),
        ('RasEapBegin', IntPtr),
        ('RasEapEnd', IntPtr),
        ('RasEapMakeMessage', IntPtr),
    ]
    return PPP_EAP_INFO
def _define_PPP_EAP_INPUT_head():
    class PPP_EAP_INPUT(Structure):
        pass
    return PPP_EAP_INPUT
def _define_PPP_EAP_INPUT():
    PPP_EAP_INPUT = win32more.Security.ExtensibleAuthenticationProtocol.PPP_EAP_INPUT_head
    PPP_EAP_INPUT._fields_ = [
        ('dwSizeInBytes', UInt32),
        ('fFlags', UInt32),
        ('fAuthenticator', win32more.Foundation.BOOL),
        ('pwszIdentity', win32more.Foundation.PWSTR),
        ('pwszPassword', win32more.Foundation.PWSTR),
        ('bInitialId', Byte),
        ('pUserAttributes', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)),
        ('fAuthenticationComplete', win32more.Foundation.BOOL),
        ('dwAuthResultCode', UInt32),
        ('hTokenImpersonateUser', win32more.Foundation.HANDLE),
        ('fSuccessPacketReceived', win32more.Foundation.BOOL),
        ('fDataReceivedFromInteractiveUI', win32more.Foundation.BOOL),
        ('pDataFromInteractiveUI', c_char_p_no),
        ('dwSizeOfDataFromInteractiveUI', UInt32),
        ('pConnectionData', c_char_p_no),
        ('dwSizeOfConnectionData', UInt32),
        ('pUserData', c_char_p_no),
        ('dwSizeOfUserData', UInt32),
        ('hReserved', win32more.Foundation.HANDLE),
        ('guidConnectionId', Guid),
        ('isVpn', win32more.Foundation.BOOL),
    ]
    return PPP_EAP_INPUT
def _define_PPP_EAP_OUTPUT_head():
    class PPP_EAP_OUTPUT(Structure):
        pass
    return PPP_EAP_OUTPUT
def _define_PPP_EAP_OUTPUT():
    PPP_EAP_OUTPUT = win32more.Security.ExtensibleAuthenticationProtocol.PPP_EAP_OUTPUT_head
    PPP_EAP_OUTPUT._fields_ = [
        ('dwSizeInBytes', UInt32),
        ('Action', win32more.Security.ExtensibleAuthenticationProtocol.PPP_EAP_ACTION),
        ('dwAuthResultCode', UInt32),
        ('pUserAttributes', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head)),
        ('fInvokeInteractiveUI', win32more.Foundation.BOOL),
        ('pUIContextData', c_char_p_no),
        ('dwSizeOfUIContextData', UInt32),
        ('fSaveConnectionData', win32more.Foundation.BOOL),
        ('pConnectionData', c_char_p_no),
        ('dwSizeOfConnectionData', UInt32),
        ('fSaveUserData', win32more.Foundation.BOOL),
        ('pUserData', c_char_p_no),
        ('dwSizeOfUserData', UInt32),
        ('pNgcKerbTicket', POINTER(win32more.Security.ExtensibleAuthenticationProtocol.NgcTicketContext_head)),
        ('fSaveToCredMan', win32more.Foundation.BOOL),
    ]
    return PPP_EAP_OUTPUT
def _define_PPP_EAP_PACKET_head():
    class PPP_EAP_PACKET(Structure):
        pass
    return PPP_EAP_PACKET
def _define_PPP_EAP_PACKET():
    PPP_EAP_PACKET = win32more.Security.ExtensibleAuthenticationProtocol.PPP_EAP_PACKET_head
    PPP_EAP_PACKET._fields_ = [
        ('Code', Byte),
        ('Id', Byte),
        ('Length', Byte * 2),
        ('Data', Byte * 1),
    ]
    return PPP_EAP_PACKET
def _define_RAS_AUTH_ATTRIBUTE_head():
    class RAS_AUTH_ATTRIBUTE(Structure):
        pass
    return RAS_AUTH_ATTRIBUTE
def _define_RAS_AUTH_ATTRIBUTE():
    RAS_AUTH_ATTRIBUTE = win32more.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_head
    RAS_AUTH_ATTRIBUTE._fields_ = [
        ('raaType', win32more.Security.ExtensibleAuthenticationProtocol.RAS_AUTH_ATTRIBUTE_TYPE),
        ('dwLength', UInt32),
        ('Value', c_void_p),
    ]
    return RAS_AUTH_ATTRIBUTE
RAS_AUTH_ATTRIBUTE_TYPE = Int32
RAS_AUTH_ATTRIBUTE_TYPE_raatMinimum = 0
RAS_AUTH_ATTRIBUTE_TYPE_raatUserName = 1
RAS_AUTH_ATTRIBUTE_TYPE_raatUserPassword = 2
RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPPassword = 3
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPAddress = 4
RAS_AUTH_ATTRIBUTE_TYPE_raatNASPort = 5
RAS_AUTH_ATTRIBUTE_TYPE_raatServiceType = 6
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedProtocol = 7
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPAddress = 8
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPNetmask = 9
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRouting = 10
RAS_AUTH_ATTRIBUTE_TYPE_raatFilterId = 11
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedMTU = 12
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedCompression = 13
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPHost = 14
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginService = 15
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginTCPPort = 16
RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned17 = 17
RAS_AUTH_ATTRIBUTE_TYPE_raatReplyMessage = 18
RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackNumber = 19
RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackId = 20
RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned21 = 21
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRoute = 22
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPXNetwork = 23
RAS_AUTH_ATTRIBUTE_TYPE_raatState = 24
RAS_AUTH_ATTRIBUTE_TYPE_raatClass = 25
RAS_AUTH_ATTRIBUTE_TYPE_raatVendorSpecific = 26
RAS_AUTH_ATTRIBUTE_TYPE_raatSessionTimeout = 27
RAS_AUTH_ATTRIBUTE_TYPE_raatIdleTimeout = 28
RAS_AUTH_ATTRIBUTE_TYPE_raatTerminationAction = 29
RAS_AUTH_ATTRIBUTE_TYPE_raatCalledStationId = 30
RAS_AUTH_ATTRIBUTE_TYPE_raatCallingStationId = 31
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIdentifier = 32
RAS_AUTH_ATTRIBUTE_TYPE_raatProxyState = 33
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATService = 34
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATNode = 35
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATGroup = 36
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkLink = 37
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkNetwork = 38
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkZone = 39
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctStatusType = 40
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctDelayTime = 41
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputOctets = 42
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputOctets = 43
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionId = 44
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctAuthentic = 45
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionTime = 46
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputPackets = 47
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputPackets = 48
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctTerminateCause = 49
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctMultiSessionId = 50
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctLinkCount = 51
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctEventTimeStamp = 55
RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPChallenge = 60
RAS_AUTH_ATTRIBUTE_TYPE_raatNASPortType = 61
RAS_AUTH_ATTRIBUTE_TYPE_raatPortLimit = 62
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATPort = 63
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelType = 64
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelMediumType = 65
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelClientEndpoint = 66
RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelServerEndpoint = 67
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPPassword = 70
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPFeatures = 71
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPZoneAccess = 72
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurity = 73
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurityData = 74
RAS_AUTH_ATTRIBUTE_TYPE_raatPasswordRetry = 75
RAS_AUTH_ATTRIBUTE_TYPE_raatPrompt = 76
RAS_AUTH_ATTRIBUTE_TYPE_raatConnectInfo = 77
RAS_AUTH_ATTRIBUTE_TYPE_raatConfigurationToken = 78
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPMessage = 79
RAS_AUTH_ATTRIBUTE_TYPE_raatSignature = 80
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPChallengeResponse = 84
RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInterimInterval = 85
RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPv6Address = 95
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedInterfaceId = 96
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Prefix = 97
RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPv6Host = 98
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Route = 99
RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Pool = 100
RAS_AUTH_ATTRIBUTE_TYPE_raatARAPGuestLogon = 8096
RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateOID = 8097
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPConfiguration = 8098
RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPEmbeddedEAPTypeId = 8099
RAS_AUTH_ATTRIBUTE_TYPE_raatInnerEAPTypeId = 8099
RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPFastRoamedSession = 8100
RAS_AUTH_ATTRIBUTE_TYPE_raatFastRoamedSession = 8100
RAS_AUTH_ATTRIBUTE_TYPE_raatEAPTLV = 8102
RAS_AUTH_ATTRIBUTE_TYPE_raatCredentialsChanged = 8103
RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateThumbprint = 8250
RAS_AUTH_ATTRIBUTE_TYPE_raatPeerId = 9000
RAS_AUTH_ATTRIBUTE_TYPE_raatServerId = 9001
RAS_AUTH_ATTRIBUTE_TYPE_raatMethodId = 9002
RAS_AUTH_ATTRIBUTE_TYPE_raatEMSK = 9003
RAS_AUTH_ATTRIBUTE_TYPE_raatSessionId = 9004
RAS_AUTH_ATTRIBUTE_TYPE_raatReserved = -1
__all__ = [
    "CERTIFICATE_HASH_LENGTH",
    "EAPACTION_Authenticate",
    "EAPACTION_Done",
    "EAPACTION_IndicateIdentity",
    "EAPACTION_IndicateTLV",
    "EAPACTION_NoAction",
    "EAPACTION_Send",
    "EAPACTION_SendAndDone",
    "EAPACTION_SendWithTimeout",
    "EAPACTION_SendWithTimeoutInteractive",
    "EAPCODE_Failure",
    "EAPCODE_Request",
    "EAPCODE_Response",
    "EAPCODE_Success",
    "EAPHOST_AUTH_INFO",
    "EAPHOST_AUTH_STATUS",
    "EAPHOST_AUTH_STATUS_EapHostAuthFailed",
    "EAPHOST_AUTH_STATUS_EapHostAuthIdentityExchange",
    "EAPHOST_AUTH_STATUS_EapHostAuthInProgress",
    "EAPHOST_AUTH_STATUS_EapHostAuthNegotiatingType",
    "EAPHOST_AUTH_STATUS_EapHostAuthNotStarted",
    "EAPHOST_AUTH_STATUS_EapHostAuthSucceeded",
    "EAPHOST_AUTH_STATUS_EapHostInvalidSession",
    "EAPHOST_IDENTITY_UI_PARAMS",
    "EAPHOST_INTERACTIVE_UI_PARAMS",
    "EAPHOST_METHOD_API_VERSION",
    "EAPHOST_PEER_API_VERSION",
    "EAP_ATTRIBUTE",
    "EAP_ATTRIBUTES",
    "EAP_ATTRIBUTE_TYPE",
    "EAP_ATTRIBUTE_TYPE_eatARAPChallengeResponse",
    "EAP_ATTRIBUTE_TYPE_eatARAPFeatures",
    "EAP_ATTRIBUTE_TYPE_eatARAPGuestLogon",
    "EAP_ATTRIBUTE_TYPE_eatARAPPassword",
    "EAP_ATTRIBUTE_TYPE_eatARAPSecurity",
    "EAP_ATTRIBUTE_TYPE_eatARAPSecurityData",
    "EAP_ATTRIBUTE_TYPE_eatARAPZoneAccess",
    "EAP_ATTRIBUTE_TYPE_eatAcctAuthentic",
    "EAP_ATTRIBUTE_TYPE_eatAcctDelayTime",
    "EAP_ATTRIBUTE_TYPE_eatAcctEventTimeStamp",
    "EAP_ATTRIBUTE_TYPE_eatAcctInputOctets",
    "EAP_ATTRIBUTE_TYPE_eatAcctInputPackets",
    "EAP_ATTRIBUTE_TYPE_eatAcctInterimInterval",
    "EAP_ATTRIBUTE_TYPE_eatAcctLinkCount",
    "EAP_ATTRIBUTE_TYPE_eatAcctMultiSessionId",
    "EAP_ATTRIBUTE_TYPE_eatAcctOutputOctets",
    "EAP_ATTRIBUTE_TYPE_eatAcctOutputPackets",
    "EAP_ATTRIBUTE_TYPE_eatAcctSessionId",
    "EAP_ATTRIBUTE_TYPE_eatAcctSessionTime",
    "EAP_ATTRIBUTE_TYPE_eatAcctStatusType",
    "EAP_ATTRIBUTE_TYPE_eatAcctTerminateCause",
    "EAP_ATTRIBUTE_TYPE_eatCallbackId",
    "EAP_ATTRIBUTE_TYPE_eatCallbackNumber",
    "EAP_ATTRIBUTE_TYPE_eatCalledStationId",
    "EAP_ATTRIBUTE_TYPE_eatCallingStationId",
    "EAP_ATTRIBUTE_TYPE_eatCertificateOID",
    "EAP_ATTRIBUTE_TYPE_eatCertificateThumbprint",
    "EAP_ATTRIBUTE_TYPE_eatClass",
    "EAP_ATTRIBUTE_TYPE_eatClearTextPassword",
    "EAP_ATTRIBUTE_TYPE_eatConfigurationToken",
    "EAP_ATTRIBUTE_TYPE_eatConnectInfo",
    "EAP_ATTRIBUTE_TYPE_eatCredentialsChanged",
    "EAP_ATTRIBUTE_TYPE_eatEAPConfiguration",
    "EAP_ATTRIBUTE_TYPE_eatEAPMessage",
    "EAP_ATTRIBUTE_TYPE_eatEAPTLV",
    "EAP_ATTRIBUTE_TYPE_eatEMSK",
    "EAP_ATTRIBUTE_TYPE_eatFastRoamedSession",
    "EAP_ATTRIBUTE_TYPE_eatFilterId",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkLink",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkNetwork",
    "EAP_ATTRIBUTE_TYPE_eatFramedAppleTalkZone",
    "EAP_ATTRIBUTE_TYPE_eatFramedCompression",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPAddress",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPNetmask",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPXNetwork",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Pool",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Prefix",
    "EAP_ATTRIBUTE_TYPE_eatFramedIPv6Route",
    "EAP_ATTRIBUTE_TYPE_eatFramedInterfaceId",
    "EAP_ATTRIBUTE_TYPE_eatFramedMTU",
    "EAP_ATTRIBUTE_TYPE_eatFramedProtocol",
    "EAP_ATTRIBUTE_TYPE_eatFramedRoute",
    "EAP_ATTRIBUTE_TYPE_eatFramedRouting",
    "EAP_ATTRIBUTE_TYPE_eatIdleTimeout",
    "EAP_ATTRIBUTE_TYPE_eatInnerEapMethodType",
    "EAP_ATTRIBUTE_TYPE_eatLoginIPHost",
    "EAP_ATTRIBUTE_TYPE_eatLoginIPv6Host",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATGroup",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATNode",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATPort",
    "EAP_ATTRIBUTE_TYPE_eatLoginLATService",
    "EAP_ATTRIBUTE_TYPE_eatLoginService",
    "EAP_ATTRIBUTE_TYPE_eatLoginTCPPort",
    "EAP_ATTRIBUTE_TYPE_eatMD5CHAPChallenge",
    "EAP_ATTRIBUTE_TYPE_eatMD5CHAPPassword",
    "EAP_ATTRIBUTE_TYPE_eatMethodId",
    "EAP_ATTRIBUTE_TYPE_eatMinimum",
    "EAP_ATTRIBUTE_TYPE_eatNASIPAddress",
    "EAP_ATTRIBUTE_TYPE_eatNASIPv6Address",
    "EAP_ATTRIBUTE_TYPE_eatNASIdentifier",
    "EAP_ATTRIBUTE_TYPE_eatNASPort",
    "EAP_ATTRIBUTE_TYPE_eatNASPortType",
    "EAP_ATTRIBUTE_TYPE_eatPEAPEmbeddedEAPTypeId",
    "EAP_ATTRIBUTE_TYPE_eatPEAPFastRoamedSession",
    "EAP_ATTRIBUTE_TYPE_eatPasswordRetry",
    "EAP_ATTRIBUTE_TYPE_eatPeerId",
    "EAP_ATTRIBUTE_TYPE_eatPortLimit",
    "EAP_ATTRIBUTE_TYPE_eatPrompt",
    "EAP_ATTRIBUTE_TYPE_eatProxyState",
    "EAP_ATTRIBUTE_TYPE_eatQuarantineSoH",
    "EAP_ATTRIBUTE_TYPE_eatReplyMessage",
    "EAP_ATTRIBUTE_TYPE_eatReserved",
    "EAP_ATTRIBUTE_TYPE_eatServerId",
    "EAP_ATTRIBUTE_TYPE_eatServiceType",
    "EAP_ATTRIBUTE_TYPE_eatSessionId",
    "EAP_ATTRIBUTE_TYPE_eatSessionTimeout",
    "EAP_ATTRIBUTE_TYPE_eatSignature",
    "EAP_ATTRIBUTE_TYPE_eatState",
    "EAP_ATTRIBUTE_TYPE_eatTerminationAction",
    "EAP_ATTRIBUTE_TYPE_eatTunnelClientEndpoint",
    "EAP_ATTRIBUTE_TYPE_eatTunnelMediumType",
    "EAP_ATTRIBUTE_TYPE_eatTunnelServerEndpoint",
    "EAP_ATTRIBUTE_TYPE_eatTunnelType",
    "EAP_ATTRIBUTE_TYPE_eatUnassigned17",
    "EAP_ATTRIBUTE_TYPE_eatUnassigned21",
    "EAP_ATTRIBUTE_TYPE_eatUserName",
    "EAP_ATTRIBUTE_TYPE_eatUserPassword",
    "EAP_ATTRIBUTE_TYPE_eatVendorSpecific",
    "EAP_AUTHENTICATOR_METHOD_ROUTINES",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_BASIC",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_INTERACTIVE",
    "EAP_AUTHENTICATOR_SEND_TIMEOUT_NONE",
    "EAP_AUTHENTICATOR_VALUENAME_CONFIGUI",
    "EAP_AUTHENTICATOR_VALUENAME_DLL_PATH",
    "EAP_AUTHENTICATOR_VALUENAME_FRIENDLY_NAME",
    "EAP_AUTHENTICATOR_VALUENAME_PROPERTIES",
    "EAP_CERTIFICATE_CREDENTIAL",
    "EAP_CONFIG_INPUT_FIELD_ARRAY",
    "EAP_CONFIG_INPUT_FIELD_DATA",
    "EAP_CONFIG_INPUT_FIELD_PROPS_DEFAULT",
    "EAP_CONFIG_INPUT_FIELD_PROPS_NON_DISPLAYABLE",
    "EAP_CONFIG_INPUT_FIELD_PROPS_NON_PERSIST",
    "EAP_CONFIG_INPUT_FIELD_TYPE",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputEdit",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkPassword",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputNetworkUsername",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPSK",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPassword",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputPin",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigInputUsername",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardError",
    "EAP_CONFIG_INPUT_FIELD_TYPE_EapConfigSmartCardUsername",
    "EAP_CREDENTIAL_VERSION",
    "EAP_CRED_EXPIRY_REQ",
    "EAP_EMPTY_CREDENTIAL",
    "EAP_ERROR",
    "EAP_E_AUTHENTICATION_FAILED",
    "EAP_E_CERT_STORE_INACCESSIBLE",
    "EAP_E_EAPHOST_EAPQEC_INACCESSIBLE",
    "EAP_E_EAPHOST_FIRST",
    "EAP_E_EAPHOST_IDENTITY_UNKNOWN",
    "EAP_E_EAPHOST_LAST",
    "EAP_E_EAPHOST_METHOD_INVALID_PACKET",
    "EAP_E_EAPHOST_METHOD_NOT_INSTALLED",
    "EAP_E_EAPHOST_METHOD_OPERATION_NOT_SUPPORTED",
    "EAP_E_EAPHOST_REMOTE_INVALID_PACKET",
    "EAP_E_EAPHOST_THIRDPARTY_METHOD_HOST_RESET",
    "EAP_E_EAPHOST_XML_MALFORMED",
    "EAP_E_METHOD_CONFIG_DOES_NOT_SUPPORT_SSO",
    "EAP_E_NO_SMART_CARD_READER",
    "EAP_E_SERVER_CERT_EXPIRED",
    "EAP_E_SERVER_CERT_INVALID",
    "EAP_E_SERVER_CERT_NOT_FOUND",
    "EAP_E_SERVER_CERT_OTHER_ERROR",
    "EAP_E_SERVER_CERT_REVOKED",
    "EAP_E_SERVER_FIRST",
    "EAP_E_SERVER_LAST",
    "EAP_E_SERVER_ROOT_CERT_FIRST",
    "EAP_E_SERVER_ROOT_CERT_INVALID",
    "EAP_E_SERVER_ROOT_CERT_LAST",
    "EAP_E_SERVER_ROOT_CERT_NAME_REQUIRED",
    "EAP_E_SERVER_ROOT_CERT_NOT_FOUND",
    "EAP_E_SIM_NOT_VALID",
    "EAP_E_USER_CERT_EXPIRED",
    "EAP_E_USER_CERT_INVALID",
    "EAP_E_USER_CERT_NOT_FOUND",
    "EAP_E_USER_CERT_OTHER_ERROR",
    "EAP_E_USER_CERT_REJECTED",
    "EAP_E_USER_CERT_REVOKED",
    "EAP_E_USER_CREDENTIALS_REJECTED",
    "EAP_E_USER_FIRST",
    "EAP_E_USER_LAST",
    "EAP_E_USER_NAME_PASSWORD_REJECTED",
    "EAP_E_USER_ROOT_CERT_EXPIRED",
    "EAP_E_USER_ROOT_CERT_FIRST",
    "EAP_E_USER_ROOT_CERT_INVALID",
    "EAP_E_USER_ROOT_CERT_LAST",
    "EAP_E_USER_ROOT_CERT_NOT_FOUND",
    "EAP_FLAG_CONFG_READONLY",
    "EAP_FLAG_FULL_AUTH",
    "EAP_FLAG_GUEST_ACCESS",
    "EAP_FLAG_LOGON",
    "EAP_FLAG_MACHINE_AUTH",
    "EAP_FLAG_NON_INTERACTIVE",
    "EAP_FLAG_ONLY_EAP_TLS",
    "EAP_FLAG_PREFER_ALT_CREDENTIALS",
    "EAP_FLAG_PREVIEW",
    "EAP_FLAG_PRE_LOGON",
    "EAP_FLAG_RESUME_FROM_HIBERNATE",
    "EAP_FLAG_Reserved1",
    "EAP_FLAG_Reserved2",
    "EAP_FLAG_Reserved3",
    "EAP_FLAG_Reserved4",
    "EAP_FLAG_Reserved5",
    "EAP_FLAG_Reserved6",
    "EAP_FLAG_Reserved7",
    "EAP_FLAG_Reserved8",
    "EAP_FLAG_Reserved9",
    "EAP_FLAG_SERVER_VALIDATION_REQUIRED",
    "EAP_FLAG_SUPRESS_UI",
    "EAP_FLAG_USER_AUTH",
    "EAP_FLAG_VPN",
    "EAP_GROUP_MASK",
    "EAP_INTERACTIVE_UI_DATA",
    "EAP_INTERACTIVE_UI_DATA_TYPE",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredExpiryResp",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredLogonResp",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredReq",
    "EAP_INTERACTIVE_UI_DATA_TYPE_EapCredResp",
    "EAP_INTERACTIVE_UI_DATA_VERSION",
    "EAP_INVALID_PACKET",
    "EAP_I_EAPHOST_EAP_NEGOTIATION_FAILED",
    "EAP_I_EAPHOST_FIRST",
    "EAP_I_EAPHOST_LAST",
    "EAP_I_USER_ACCOUNT_OTHER_ERROR",
    "EAP_I_USER_FIRST",
    "EAP_I_USER_LAST",
    "EAP_METHOD_AUTHENTICATOR_CONFIG_IS_IDENTITY_PRIVACY",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_ACTION",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_AUTHENTICATE",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_DISCARD",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_HANDLE_IDENTITY",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_RESPOND",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_RESULT",
    "EAP_METHOD_AUTHENTICATOR_RESPONSE_SEND",
    "EAP_METHOD_AUTHENTICATOR_RESULT",
    "EAP_METHOD_INFO",
    "EAP_METHOD_INFO_ARRAY",
    "EAP_METHOD_INFO_ARRAY_EX",
    "EAP_METHOD_INFO_EX",
    "EAP_METHOD_INVALID_PACKET",
    "EAP_METHOD_PROPERTY",
    "EAP_METHOD_PROPERTY_ARRAY",
    "EAP_METHOD_PROPERTY_TYPE",
    "EAP_METHOD_PROPERTY_TYPE_emptLegacyMethodPropertyFlag",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCertifiedMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropChannelBinding",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCipherSuiteNegotiation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropConfidentiality",
    "EAP_METHOD_PROPERTY_TYPE_emptPropCryptoBinding",
    "EAP_METHOD_PROPERTY_TYPE_emptPropDictionaryAttackResistance",
    "EAP_METHOD_PROPERTY_TYPE_emptPropFastReconnect",
    "EAP_METHOD_PROPERTY_TYPE_emptPropFragmentation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropHiddenMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropIdentityPrivacy",
    "EAP_METHOD_PROPERTY_TYPE_emptPropIntegrity",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyDerivation",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength1024",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength128",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength256",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength512",
    "EAP_METHOD_PROPERTY_TYPE_emptPropKeyStrength64",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMachineAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMethodChaining",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMppeEncryption",
    "EAP_METHOD_PROPERTY_TYPE_emptPropMutualAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropNap",
    "EAP_METHOD_PROPERTY_TYPE_emptPropReplayProtection",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSessionIndependence",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSharedStateEquivalence",
    "EAP_METHOD_PROPERTY_TYPE_emptPropStandalone",
    "EAP_METHOD_PROPERTY_TYPE_emptPropSupportsConfig",
    "EAP_METHOD_PROPERTY_TYPE_emptPropTunnelMethod",
    "EAP_METHOD_PROPERTY_TYPE_emptPropUserAuth",
    "EAP_METHOD_PROPERTY_TYPE_emptPropVendorSpecific",
    "EAP_METHOD_PROPERTY_VALUE",
    "EAP_METHOD_PROPERTY_VALUE_BOOL",
    "EAP_METHOD_PROPERTY_VALUE_DWORD",
    "EAP_METHOD_PROPERTY_VALUE_STRING",
    "EAP_METHOD_PROPERTY_VALUE_TYPE",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtBool",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtDword",
    "EAP_METHOD_PROPERTY_VALUE_TYPE_empvtString",
    "EAP_METHOD_TYPE",
    "EAP_PEER_FLAG_GUEST_ACCESS",
    "EAP_PEER_FLAG_HEALTH_STATE_CHANGE",
    "EAP_PEER_METHOD_ROUTINES",
    "EAP_PEER_VALUENAME_CONFIGUI",
    "EAP_PEER_VALUENAME_DLL_PATH",
    "EAP_PEER_VALUENAME_FRIENDLY_NAME",
    "EAP_PEER_VALUENAME_IDENTITY",
    "EAP_PEER_VALUENAME_INTERACTIVEUI",
    "EAP_PEER_VALUENAME_INVOKE_NAMEDLG",
    "EAP_PEER_VALUENAME_INVOKE_PWDDLG",
    "EAP_PEER_VALUENAME_PROPERTIES",
    "EAP_PEER_VALUENAME_REQUIRE_CONFIGUI",
    "EAP_REGISTRY_LOCATION",
    "EAP_SIM_CREDENTIAL",
    "EAP_TYPE",
    "EAP_UI_DATA_FORMAT",
    "EAP_UI_INPUT_FIELD_PROPS_DEFAULT",
    "EAP_UI_INPUT_FIELD_PROPS_NON_DISPLAYABLE",
    "EAP_UI_INPUT_FIELD_PROPS_NON_PERSIST",
    "EAP_UI_INPUT_FIELD_PROPS_READ_ONLY",
    "EAP_USERNAME_PASSWORD_CREDENTIAL",
    "EAP_VALUENAME_PROPERTIES",
    "EAP_WINLOGON_CREDENTIAL",
    "EapCertificateCredential",
    "EapCode",
    "EapCode_EapCodeFailure",
    "EapCode_EapCodeMaximum",
    "EapCode_EapCodeMinimum",
    "EapCode_EapCodeRequest",
    "EapCode_EapCodeResponse",
    "EapCode_EapCodeSuccess",
    "EapCredential",
    "EapCredentialType",
    "EapCredentialTypeData",
    "EapHostPeerAuthParams",
    "EapHostPeerAuthParams_EapHostNapInfo",
    "EapHostPeerAuthParams_EapHostPeerAuthStatus",
    "EapHostPeerAuthParams_EapHostPeerIdentity",
    "EapHostPeerAuthParams_EapHostPeerIdentityExtendedInfo",
    "EapHostPeerBeginSession",
    "EapHostPeerClearConnection",
    "EapHostPeerConfigBlob2Xml",
    "EapHostPeerConfigXml2Blob",
    "EapHostPeerCredentialsXml2Blob",
    "EapHostPeerEndSession",
    "EapHostPeerFreeEapError",
    "EapHostPeerFreeErrorMemory",
    "EapHostPeerFreeMemory",
    "EapHostPeerFreeRuntimeMemory",
    "EapHostPeerGetAuthStatus",
    "EapHostPeerGetDataToUnplumbCredentials",
    "EapHostPeerGetEncryptedPassword",
    "EapHostPeerGetIdentity",
    "EapHostPeerGetMethodProperties",
    "EapHostPeerGetMethods",
    "EapHostPeerGetResponseAttributes",
    "EapHostPeerGetResult",
    "EapHostPeerGetSendPacket",
    "EapHostPeerGetUIContext",
    "EapHostPeerInitialize",
    "EapHostPeerInvokeConfigUI",
    "EapHostPeerInvokeIdentityUI",
    "EapHostPeerInvokeInteractiveUI",
    "EapHostPeerMethodResult",
    "EapHostPeerMethodResultReason",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultAltSuccessReceived",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultFromMethod",
    "EapHostPeerMethodResultReason_EapHostPeerMethodResultTimeout",
    "EapHostPeerProcessReceivedPacket",
    "EapHostPeerQueryCredentialInputFields",
    "EapHostPeerQueryInteractiveUIInputFields",
    "EapHostPeerQueryUIBlobFromInteractiveUIInputFields",
    "EapHostPeerQueryUserBlobFromCredentialInputFields",
    "EapHostPeerResponseAction",
    "EapHostPeerResponseAction_EapHostPeerResponseDiscard",
    "EapHostPeerResponseAction_EapHostPeerResponseInvokeUi",
    "EapHostPeerResponseAction_EapHostPeerResponseNone",
    "EapHostPeerResponseAction_EapHostPeerResponseRespond",
    "EapHostPeerResponseAction_EapHostPeerResponseResult",
    "EapHostPeerResponseAction_EapHostPeerResponseSend",
    "EapHostPeerResponseAction_EapHostPeerResponseStartAuthentication",
    "EapHostPeerSetResponseAttributes",
    "EapHostPeerSetUIContext",
    "EapHostPeerUninitialize",
    "EapPacket",
    "EapPeerMethodOutput",
    "EapPeerMethodResponseAction",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionDiscard",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionInvokeUI",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionNone",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionRespond",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionResult",
    "EapPeerMethodResponseAction_EapPeerMethodResponseActionSend",
    "EapPeerMethodResult",
    "EapPeerMethodResultReason",
    "EapPeerMethodResultReason_EapPeerMethodResultFailure",
    "EapPeerMethodResultReason_EapPeerMethodResultSuccess",
    "EapPeerMethodResultReason_EapPeerMethodResultUnknown",
    "EapSimCredential",
    "EapUsernamePasswordCredential",
    "FACILITY_EAP_MESSAGE",
    "GUID_EapHost_Cause_CertStoreInaccessible",
    "GUID_EapHost_Cause_EapNegotiationFailed",
    "GUID_EapHost_Cause_EapQecInaccessible",
    "GUID_EapHost_Cause_Generic_AuthFailure",
    "GUID_EapHost_Cause_IdentityUnknown",
    "GUID_EapHost_Cause_MethodDLLNotFound",
    "GUID_EapHost_Cause_MethodDoesNotSupportOperation",
    "GUID_EapHost_Cause_Method_Config_Does_Not_Support_Sso",
    "GUID_EapHost_Cause_No_SmartCardReader_Found",
    "GUID_EapHost_Cause_Server_CertExpired",
    "GUID_EapHost_Cause_Server_CertInvalid",
    "GUID_EapHost_Cause_Server_CertNotFound",
    "GUID_EapHost_Cause_Server_CertOtherError",
    "GUID_EapHost_Cause_Server_CertRevoked",
    "GUID_EapHost_Cause_Server_Root_CertNameRequired",
    "GUID_EapHost_Cause_Server_Root_CertNotFound",
    "GUID_EapHost_Cause_SimNotValid",
    "GUID_EapHost_Cause_ThirdPartyMethod_Host_Reset",
    "GUID_EapHost_Cause_User_Account_OtherProblem",
    "GUID_EapHost_Cause_User_CertExpired",
    "GUID_EapHost_Cause_User_CertInvalid",
    "GUID_EapHost_Cause_User_CertNotFound",
    "GUID_EapHost_Cause_User_CertOtherError",
    "GUID_EapHost_Cause_User_CertRejected",
    "GUID_EapHost_Cause_User_CertRevoked",
    "GUID_EapHost_Cause_User_CredsRejected",
    "GUID_EapHost_Cause_User_Root_CertExpired",
    "GUID_EapHost_Cause_User_Root_CertInvalid",
    "GUID_EapHost_Cause_User_Root_CertNotFound",
    "GUID_EapHost_Cause_XmlMalformed",
    "GUID_EapHost_Default",
    "GUID_EapHost_Help_ObtainingCerts",
    "GUID_EapHost_Help_Troubleshooting",
    "GUID_EapHost_Repair_ContactAdmin_AuthFailure",
    "GUID_EapHost_Repair_ContactAdmin_CertNameAbsent",
    "GUID_EapHost_Repair_ContactAdmin_CertStoreInaccessible",
    "GUID_EapHost_Repair_ContactAdmin_IdentityUnknown",
    "GUID_EapHost_Repair_ContactAdmin_InvalidUserAccount",
    "GUID_EapHost_Repair_ContactAdmin_InvalidUserCert",
    "GUID_EapHost_Repair_ContactAdmin_MethodNotFound",
    "GUID_EapHost_Repair_ContactAdmin_NegotiationFailed",
    "GUID_EapHost_Repair_ContactAdmin_NoSmartCardReader",
    "GUID_EapHost_Repair_ContactAdmin_RootCertInvalid",
    "GUID_EapHost_Repair_ContactAdmin_RootCertNotFound",
    "GUID_EapHost_Repair_ContactAdmin_RootExpired",
    "GUID_EapHost_Repair_ContactSysadmin",
    "GUID_EapHost_Repair_Method_Not_Support_Sso",
    "GUID_EapHost_Repair_No_ValidSim_Found",
    "GUID_EapHost_Repair_RestartNap",
    "GUID_EapHost_Repair_Retry_Authentication",
    "GUID_EapHost_Repair_Server_ClientSelectServerCert",
    "GUID_EapHost_Repair_User_AuthFailure",
    "GUID_EapHost_Repair_User_GetNewCert",
    "GUID_EapHost_Repair_User_SelectValidCert",
    "IAccountingProviderConfig",
    "IAuthenticationProviderConfig",
    "IEAPProviderConfig",
    "IEAPProviderConfig2",
    "IEAPProviderConfig3",
    "IRouterProtocolConfig",
    "ISOLATION_STATE",
    "ISOLATION_STATE_IN_PROBATION",
    "ISOLATION_STATE_NOT_RESTRICTED",
    "ISOLATION_STATE_RESTRICTED_ACCESS",
    "ISOLATION_STATE_UNKNOWN",
    "LEGACY_IDENTITY_UI_PARAMS",
    "LEGACY_INTERACTIVE_UI_PARAMS",
    "MAXEAPCODE",
    "MAX_EAP_CONFIG_INPUT_FIELD_LENGTH",
    "MAX_EAP_CONFIG_INPUT_FIELD_VALUE_LENGTH",
    "NCRYPT_PIN_CACHE_PIN_BYTE_LENGTH",
    "NgcTicketContext",
    "NotificationHandler",
    "PPP_EAP_ACTION",
    "PPP_EAP_INFO",
    "PPP_EAP_INPUT",
    "PPP_EAP_OUTPUT",
    "PPP_EAP_PACKET",
    "RAS_AUTH_ATTRIBUTE",
    "RAS_AUTH_ATTRIBUTE_TYPE",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPChallengeResponse",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPFeatures",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPGuestLogon",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurity",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPSecurityData",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatARAPZoneAccess",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctAuthentic",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctDelayTime",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctEventTimeStamp",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputOctets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInputPackets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctInterimInterval",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctLinkCount",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctMultiSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputOctets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctOutputPackets",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctSessionTime",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctStatusType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatAcctTerminateCause",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallbackNumber",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCalledStationId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCallingStationId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateOID",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCertificateThumbprint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatClass",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatConfigurationToken",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatConnectInfo",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatCredentialsChanged",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPConfiguration",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPMessage",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEAPTLV",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatEMSK",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFastRoamedSession",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFilterId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkLink",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkNetwork",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedAppleTalkZone",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedCompression",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPAddress",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPNetmask",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPXNetwork",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Pool",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Prefix",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedIPv6Route",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedInterfaceId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedMTU",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedProtocol",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRoute",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatFramedRouting",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatIdleTimeout",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatInnerEAPTypeId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPHost",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginIPv6Host",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATGroup",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATNode",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginLATService",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginService",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatLoginTCPPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPChallenge",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMD5CHAPPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMethodId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatMinimum",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPAddress",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIPv6Address",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASIdentifier",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASPort",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatNASPortType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPEmbeddedEAPTypeId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPEAPFastRoamedSession",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPasswordRetry",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPeerId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPortLimit",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatPrompt",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatProxyState",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatReplyMessage",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatReserved",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatServerId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatServiceType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSessionId",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSessionTimeout",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatSignature",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatState",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTerminationAction",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelClientEndpoint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelMediumType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelServerEndpoint",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatTunnelType",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned17",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUnassigned21",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUserName",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatUserPassword",
    "RAS_AUTH_ATTRIBUTE_TYPE_raatVendorSpecific",
    "RAS_EAP_FLAG_8021X_AUTH",
    "RAS_EAP_FLAG_ALTERNATIVE_USER_DB",
    "RAS_EAP_FLAG_CONFG_READONLY",
    "RAS_EAP_FLAG_FIRST_LINK",
    "RAS_EAP_FLAG_GUEST_ACCESS",
    "RAS_EAP_FLAG_HOSTED_IN_PEAP",
    "RAS_EAP_FLAG_LOGON",
    "RAS_EAP_FLAG_MACHINE_AUTH",
    "RAS_EAP_FLAG_NON_INTERACTIVE",
    "RAS_EAP_FLAG_PEAP_FORCE_FULL_AUTH",
    "RAS_EAP_FLAG_PEAP_UPFRONT",
    "RAS_EAP_FLAG_PREVIEW",
    "RAS_EAP_FLAG_PRE_LOGON",
    "RAS_EAP_FLAG_RESERVED",
    "RAS_EAP_FLAG_RESUME_FROM_HIBERNATE",
    "RAS_EAP_FLAG_ROUTER",
    "RAS_EAP_FLAG_SAVE_CREDMAN",
    "RAS_EAP_FLAG_SERVER_VALIDATION_REQUIRED",
    "RAS_EAP_REGISTRY_LOCATION",
    "RAS_EAP_ROLE_AUTHENTICATEE",
    "RAS_EAP_ROLE_AUTHENTICATOR",
    "RAS_EAP_ROLE_EXCLUDE_IN_EAP",
    "RAS_EAP_ROLE_EXCLUDE_IN_PEAP",
    "RAS_EAP_ROLE_EXCLUDE_IN_VPN",
    "RAS_EAP_VALUENAME_CONFIGUI",
    "RAS_EAP_VALUENAME_CONFIG_CLSID",
    "RAS_EAP_VALUENAME_DEFAULT_DATA",
    "RAS_EAP_VALUENAME_ENCRYPTION",
    "RAS_EAP_VALUENAME_FILTER_INNERMETHODS",
    "RAS_EAP_VALUENAME_FRIENDLY_NAME",
    "RAS_EAP_VALUENAME_IDENTITY",
    "RAS_EAP_VALUENAME_INTERACTIVEUI",
    "RAS_EAP_VALUENAME_INVOKE_NAMEDLG",
    "RAS_EAP_VALUENAME_INVOKE_PWDDLG",
    "RAS_EAP_VALUENAME_ISTUNNEL_METHOD",
    "RAS_EAP_VALUENAME_PATH",
    "RAS_EAP_VALUENAME_PER_POLICY_CONFIG",
    "RAS_EAP_VALUENAME_REQUIRE_CONFIGUI",
    "RAS_EAP_VALUENAME_ROLES_SUPPORTED",
    "RAS_EAP_VALUENAME_STANDALONE_SUPPORTED",
    "eapPropCertifiedMethod",
    "eapPropChannelBinding",
    "eapPropCipherSuiteNegotiation",
    "eapPropConfidentiality",
    "eapPropCryptoBinding",
    "eapPropDictionaryAttackResistance",
    "eapPropFastReconnect",
    "eapPropFragmentation",
    "eapPropHiddenMethod",
    "eapPropIdentityPrivacy",
    "eapPropIntegrity",
    "eapPropKeyDerivation",
    "eapPropKeyStrength1024",
    "eapPropKeyStrength128",
    "eapPropKeyStrength256",
    "eapPropKeyStrength512",
    "eapPropKeyStrength64",
    "eapPropMachineAuth",
    "eapPropMethodChaining",
    "eapPropMppeEncryption",
    "eapPropMutualAuth",
    "eapPropNap",
    "eapPropReplayProtection",
    "eapPropReserved",
    "eapPropSessionIndependence",
    "eapPropSharedStateEquivalence",
    "eapPropStandalone",
    "eapPropSupportsConfig",
    "eapPropTunnelMethod",
    "eapPropUserAuth",
    "raatARAPChallenge",
    "raatARAPNewPassword",
    "raatARAPOldPassword",
    "raatARAPPasswordChangeReason",
]
