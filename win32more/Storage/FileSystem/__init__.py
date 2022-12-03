from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Security
import win32more.Storage.FileSystem
import win32more.System.Com
import win32more.System.IO
import win32more.System.WindowsProgramming
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
MAXIMUM_REPARSE_DATA_BUFFER_SIZE = 16384
EA_CONTAINER_NAME = 'ContainerName'
EA_CONTAINER_SIZE = 'ContainerSize'
CLFS_BASELOG_EXTENSION = '.blf'
CLFS_FLAG_REENTRANT_FILE_SYSTEM = 8
CLFS_FLAG_NON_REENTRANT_FILTER = 16
CLFS_FLAG_REENTRANT_FILTER = 32
CLFS_FLAG_IGNORE_SHARE_ACCESS = 64
CLFS_FLAG_READ_IN_PROGRESS = 128
CLFS_FLAG_MINIFILTER_LEVEL = 256
CLFS_FLAG_HIDDEN_SYSTEM_LOG = 512
CLFS_MARSHALLING_FLAG_NONE = 0
CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT = 1
CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL = 16
CLFS_FLAG_FILTER_TOP_LEVEL = 32
CLFS_CONTAINER_STREAM_PREFIX = '%BLF%:'
CLFS_CONTAINER_RELATIVE_PREFIX = '%BLF%\\'
TRANSACTION_MANAGER_VOLATILE = 1
TRANSACTION_MANAGER_COMMIT_DEFAULT = 0
TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME = 2
TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES = 4
TRANSACTION_MANAGER_COMMIT_LOWEST = 8
TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY = 16
TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS = 32
TRANSACTION_MANAGER_MAXIMUM_OPTION = 63
TRANSACTION_DO_NOT_PROMOTE = 1
TRANSACTION_MAXIMUM_OPTION = 1
RESOURCE_MANAGER_VOLATILE = 1
RESOURCE_MANAGER_COMMUNICATION = 2
RESOURCE_MANAGER_MAXIMUM_OPTION = 3
CRM_PROTOCOL_EXPLICIT_MARSHAL_ONLY = 1
CRM_PROTOCOL_DYNAMIC_MARSHAL_INFO = 2
CRM_PROTOCOL_MAXIMUM_OPTION = 3
ENLISTMENT_SUPERIOR = 1
ENLISTMENT_MAXIMUM_OPTION = 1
TRANSACTION_NOTIFY_MASK = 1073741823
TRANSACTION_NOTIFY_PREPREPARE = 1
TRANSACTION_NOTIFY_PREPARE = 2
TRANSACTION_NOTIFY_COMMIT = 4
TRANSACTION_NOTIFY_ROLLBACK = 8
TRANSACTION_NOTIFY_PREPREPARE_COMPLETE = 16
TRANSACTION_NOTIFY_PREPARE_COMPLETE = 32
TRANSACTION_NOTIFY_COMMIT_COMPLETE = 64
TRANSACTION_NOTIFY_ROLLBACK_COMPLETE = 128
TRANSACTION_NOTIFY_RECOVER = 256
TRANSACTION_NOTIFY_SINGLE_PHASE_COMMIT = 512
TRANSACTION_NOTIFY_DELEGATE_COMMIT = 1024
TRANSACTION_NOTIFY_RECOVER_QUERY = 2048
TRANSACTION_NOTIFY_ENLIST_PREPREPARE = 4096
TRANSACTION_NOTIFY_LAST_RECOVER = 8192
TRANSACTION_NOTIFY_INDOUBT = 16384
TRANSACTION_NOTIFY_PROPAGATE_PULL = 32768
TRANSACTION_NOTIFY_PROPAGATE_PUSH = 65536
TRANSACTION_NOTIFY_MARSHAL = 131072
TRANSACTION_NOTIFY_ENLIST_MASK = 262144
TRANSACTION_NOTIFY_RM_DISCONNECTED = 16777216
TRANSACTION_NOTIFY_TM_ONLINE = 33554432
TRANSACTION_NOTIFY_COMMIT_REQUEST = 67108864
TRANSACTION_NOTIFY_PROMOTE = 134217728
TRANSACTION_NOTIFY_PROMOTE_NEW = 268435456
TRANSACTION_NOTIFY_REQUEST_OUTCOME = 536870912
TRANSACTION_NOTIFY_COMMIT_FINALIZE = 1073741824
TRANSACTIONMANAGER_OBJECT_PATH = '\\TransactionManager\\'
TRANSACTION_OBJECT_PATH = '\\Transaction\\'
ENLISTMENT_OBJECT_PATH = '\\Enlistment\\'
RESOURCE_MANAGER_OBJECT_PATH = '\\ResourceManager\\'
TRANSACTION_NOTIFICATION_TM_ONLINE_FLAG_IS_CLUSTERED = 1
KTM_MARSHAL_BLOB_VERSION_MAJOR = 1
KTM_MARSHAL_BLOB_VERSION_MINOR = 1
MAX_TRANSACTION_DESCRIPTION_LENGTH = 64
MAX_RESOURCEMANAGER_DESCRIPTION_LENGTH = 64
IOCTL_VOLUME_BASE = 86
IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS = 5636096
IOCTL_VOLUME_ONLINE = 5685256
IOCTL_VOLUME_OFFLINE = 5685260
IOCTL_VOLUME_IS_CLUSTERED = 5636144
IOCTL_VOLUME_GET_GPT_ATTRIBUTES = 5636152
IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE = 5636100
IOCTL_VOLUME_IS_OFFLINE = 5636112
IOCTL_VOLUME_IS_IO_CAPABLE = 5636116
IOCTL_VOLUME_QUERY_FAILOVER_SET = 5636120
IOCTL_VOLUME_QUERY_VOLUME_NUMBER = 5636124
IOCTL_VOLUME_LOGICAL_TO_PHYSICAL = 5636128
IOCTL_VOLUME_PHYSICAL_TO_LOGICAL = 5636132
IOCTL_VOLUME_IS_PARTITION = 5636136
IOCTL_VOLUME_READ_PLEX = 5652526
IOCTL_VOLUME_SET_GPT_ATTRIBUTES = 5636148
IOCTL_VOLUME_GET_BC_PROPERTIES = 5652540
IOCTL_VOLUME_ALLOCATE_BC_STREAM = 5685312
IOCTL_VOLUME_FREE_BC_STREAM = 5685316
IOCTL_VOLUME_BC_VERSION = 1
IOCTL_VOLUME_IS_DYNAMIC = 5636168
IOCTL_VOLUME_PREPARE_FOR_CRITICAL_IO = 5685324
IOCTL_VOLUME_QUERY_ALLOCATION_HINT = 5652562
IOCTL_VOLUME_UPDATE_PROPERTIES = 5636180
IOCTL_VOLUME_QUERY_MINIMUM_SHRINK_SIZE = 5652568
IOCTL_VOLUME_PREPARE_FOR_SHRINK = 5685340
IOCTL_VOLUME_IS_CSV = 5636192
IOCTL_VOLUME_POST_ONLINE = 5685348
IOCTL_VOLUME_GET_CSVBLOCKCACHE_CALLBACK = 5685352
CSV_BLOCK_CACHE_CALLBACK_VERSION = 1
CSV_BLOCK_AND_FILE_CACHE_CALLBACK_VERSION = 2
def _define_PARTITION_BASIC_DATA_GUID():
    return Guid('ebd0a0a2-b9e5-4433-87-c0-68-b6-b7-26-99-c7')
def _define_PARTITION_BSP_GUID():
    return Guid('57434f53-4df9-45b9-8e-9e-23-70-f0-06-45-7c')
def _define_PARTITION_CLUSTER_GUID():
    return Guid('db97dba9-0840-4bae-97-f0-ff-b9-a3-27-c7-e1')
def _define_PARTITION_DPP_GUID():
    return Guid('57434f53-94cb-43f0-a5-33-d7-3c-10-cf-a5-7d')
def _define_PARTITION_ENTRY_UNUSED_GUID():
    return Guid('00000000-0000-0000-00-00-00-00-00-00-00-00')
def _define_PARTITION_LDM_DATA_GUID():
    return Guid('af9b60a0-1431-4f62-bc-68-33-11-71-4a-69-ad')
def _define_PARTITION_LDM_METADATA_GUID():
    return Guid('5808c8aa-7e8f-42e0-85-d2-e1-e9-04-34-cf-b3')
def _define_PARTITION_LEGACY_BL_GUID():
    return Guid('424ca0e2-7cb2-4fb9-81-43-c5-2a-99-39-8b-c6')
def _define_PARTITION_LEGACY_BL_GUID_BACKUP():
    return Guid('424c3e6c-d79f-49cb-93-5d-36-d7-14-67-a2-88')
def _define_PARTITION_MAIN_OS_GUID():
    return Guid('57434f53-8f45-405e-8a-23-18-6d-8a-43-30-d3')
def _define_PARTITION_MSFT_RECOVERY_GUID():
    return Guid('de94bba4-06d1-4d40-a1-6a-bf-d5-01-79-d6-ac')
def _define_PARTITION_MSFT_RESERVED_GUID():
    return Guid('e3c9e316-0b5c-4db8-81-7d-f9-2d-f0-02-15-ae')
def _define_PARTITION_MSFT_SNAPSHOT_GUID():
    return Guid('caddebf1-4400-4de8-b1-03-12-11-7d-cf-3c-cf')
def _define_PARTITION_OS_DATA_GUID():
    return Guid('57434f53-23f2-44d5-a8-30-67-bb-da-a6-09-f9')
def _define_PARTITION_PATCH_GUID():
    return Guid('8967a686-96aa-6aa8-95-89-a8-42-56-54-10-90')
def _define_PARTITION_PRE_INSTALLED_GUID():
    return Guid('57434f53-7fe0-4196-9b-42-42-7b-51-64-34-84')
def _define_PARTITION_SERVICING_FILES_GUID():
    return Guid('57434f53-432e-4014-ae-4c-8d-ea-a9-c0-00-6a')
def _define_PARTITION_SERVICING_METADATA_GUID():
    return Guid('57434f53-c691-4a05-bb-4e-70-3d-af-d2-29-ce')
def _define_PARTITION_SERVICING_RESERVE_GUID():
    return Guid('57434f53-4b81-460b-a3-19-ff-b6-fe-13-6d-14')
def _define_PARTITION_SERVICING_STAGING_ROOT_GUID():
    return Guid('57434f53-e84d-4e84-aa-f3-ec-bb-bd-04-b9-df')
def _define_PARTITION_SPACES_GUID():
    return Guid('e75caf8f-f680-4cee-af-a3-b0-01-e5-6e-fc-2d')
def _define_PARTITION_SPACES_DATA_GUID():
    return Guid('e7addcb4-dc34-4539-9a-76-eb-bd-07-be-6f-7e')
def _define_PARTITION_SYSTEM_GUID():
    return Guid('c12a7328-f81f-11d2-ba-4b-00-a0-c9-3e-c9-3b')
def _define_PARTITION_WINDOWS_SYSTEM_GUID():
    return Guid('57434f53-e3e3-4631-a5-c5-26-d2-24-38-73-aa')
_FT_TYPES_DEFINITION_ = 1
CLFS_MGMT_POLICY_VERSION = 1
LOG_POLICY_OVERWRITE = 1
LOG_POLICY_PERSIST = 2
CLFS_MGMT_CLIENT_REGISTRATION_VERSION = 1
def _define_CLSID_DiskQuotaControl():
    return Guid('7988b571-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
DISKQUOTA_STATE_DISABLED = 0
DISKQUOTA_STATE_TRACK = 1
DISKQUOTA_STATE_ENFORCE = 2
DISKQUOTA_STATE_MASK = 3
DISKQUOTA_FILESTATE_INCOMPLETE = 256
DISKQUOTA_FILESTATE_REBUILDING = 512
DISKQUOTA_FILESTATE_MASK = 768
DISKQUOTA_LOGFLAG_USER_THRESHOLD = 1
DISKQUOTA_LOGFLAG_USER_LIMIT = 2
DISKQUOTA_USER_ACCOUNT_RESOLVED = 0
DISKQUOTA_USER_ACCOUNT_UNAVAILABLE = 1
DISKQUOTA_USER_ACCOUNT_DELETED = 2
DISKQUOTA_USER_ACCOUNT_INVALID = 3
DISKQUOTA_USER_ACCOUNT_UNKNOWN = 4
DISKQUOTA_USER_ACCOUNT_UNRESOLVED = 5
INVALID_SET_FILE_POINTER = 4294967295
INVALID_FILE_ATTRIBUTES = 4294967295
SHARE_NETNAME_PARMNUM = 1
SHARE_TYPE_PARMNUM = 3
SHARE_REMARK_PARMNUM = 4
SHARE_PERMISSIONS_PARMNUM = 5
SHARE_MAX_USES_PARMNUM = 6
SHARE_CURRENT_USES_PARMNUM = 7
SHARE_PATH_PARMNUM = 8
SHARE_PASSWD_PARMNUM = 9
SHARE_FILE_SD_PARMNUM = 501
SHARE_SERVER_PARMNUM = 503
SHI1_NUM_ELEMENTS = 4
SHI2_NUM_ELEMENTS = 10
STYPE_RESERVED1 = 16777216
STYPE_RESERVED2 = 33554432
STYPE_RESERVED3 = 67108864
STYPE_RESERVED4 = 134217728
STYPE_RESERVED5 = 1048576
STYPE_RESERVED_ALL = 1073741568
SHI_USES_UNLIMITED = 4294967295
SHI1005_FLAGS_DFS = 1
SHI1005_FLAGS_DFS_ROOT = 2
CSC_MASK_EXT = 8240
CSC_MASK = 48
CSC_CACHE_MANUAL_REINT = 0
CSC_CACHE_AUTO_REINT = 16
CSC_CACHE_VDO = 32
CSC_CACHE_NONE = 48
SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS = 256
SHI1005_FLAGS_FORCE_SHARED_DELETE = 512
SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING = 1024
SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM = 2048
SHI1005_FLAGS_FORCE_LEVELII_OPLOCK = 4096
SHI1005_FLAGS_ENABLE_HASH = 8192
SHI1005_FLAGS_ENABLE_CA = 16384
SHI1005_FLAGS_ENCRYPT_DATA = 32768
SHI1005_FLAGS_RESERVED = 65536
SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING = 131072
SHI1005_FLAGS_IDENTITY_REMOTING = 262144
SHI1005_FLAGS_CLUSTER_MANAGED = 524288
SHI1005_FLAGS_COMPRESS_DATA = 1048576
SESI1_NUM_ELEMENTS = 8
SESI2_NUM_ELEMENTS = 9
STATSOPT_CLR = 1
LZERROR_BADINHANDLE = -1
LZERROR_BADOUTHANDLE = -2
LZERROR_READ = -3
LZERROR_WRITE = -4
LZERROR_GLOBALLOC = -5
LZERROR_GLOBLOCK = -6
LZERROR_BADVALUE = -7
LZERROR_UNKNOWNALG = -8
NTMS_OBJECTNAME_LENGTH = 64
NTMS_DESCRIPTION_LENGTH = 127
NTMS_DEVICENAME_LENGTH = 64
NTMS_SERIALNUMBER_LENGTH = 32
NTMS_REVISION_LENGTH = 32
NTMS_BARCODE_LENGTH = 64
NTMS_SEQUENCE_LENGTH = 32
NTMS_VENDORNAME_LENGTH = 128
NTMS_PRODUCTNAME_LENGTH = 128
NTMS_USERNAME_LENGTH = 64
NTMS_APPLICATIONNAME_LENGTH = 64
NTMS_COMPUTERNAME_LENGTH = 64
NTMS_I1_MESSAGE_LENGTH = 127
NTMS_MESSAGE_LENGTH = 256
NTMS_POOLHIERARCHY_LENGTH = 512
NTMS_OMIDLABELID_LENGTH = 255
NTMS_OMIDLABELTYPE_LENGTH = 64
NTMS_OMIDLABELINFO_LENGTH = 256
NTMS_MAXATTR_LENGTH = 65536
NTMS_MAXATTR_NAMELEN = 32
NTMSMLI_MAXTYPE = 64
NTMSMLI_MAXIDSIZE = 256
NTMSMLI_MAXAPPDESCR = 256
TXF_LOG_RECORD_GENERIC_TYPE_COMMIT = 1
TXF_LOG_RECORD_GENERIC_TYPE_ABORT = 2
TXF_LOG_RECORD_GENERIC_TYPE_PREPARE = 4
TXF_LOG_RECORD_GENERIC_TYPE_DATA = 8
VS_VERSION_INFO = 1
VS_USER_DEFINED = 100
VS_FFI_SIGNATURE = -17890115
VS_FFI_STRUCVERSION = 65536
VS_FFI_FILEFLAGSMASK = 63
WINEFS_SETUSERKEY_SET_CAPABILITIES = 1
EFS_COMPATIBILITY_VERSION_NCRYPT_PROTECTOR = 5
EFS_COMPATIBILITY_VERSION_PFILE_PROTECTOR = 6
EFS_SUBVER_UNKNOWN = 0
EFS_EFS_SUBVER_EFS_CERT = 1
EFS_PFILE_SUBVER_RMS = 2
EFS_PFILE_SUBVER_APPX = 3
MAX_SID_SIZE = 256
EFS_METADATA_ADD_USER = 1
EFS_METADATA_REMOVE_USER = 2
EFS_METADATA_REPLACE_USER = 4
EFS_METADATA_GENERAL_OP = 8
WOF_PROVIDER_WIM = 1
WOF_PROVIDER_FILE = 2
WIM_PROVIDER_HASH_SIZE = 20
WIM_BOOT_OS_WIM = 1
WIM_BOOT_NOT_OS_WIM = 0
WIM_ENTRY_FLAG_NOT_ACTIVE = 1
WIM_ENTRY_FLAG_SUSPENDED = 2
WIM_EXTERNAL_FILE_INFO_FLAG_NOT_ACTIVE = 1
WIM_EXTERNAL_FILE_INFO_FLAG_SUSPENDED = 2
FILE_PROVIDER_COMPRESSION_XPRESS4K = 0
FILE_PROVIDER_COMPRESSION_LZX = 1
FILE_PROVIDER_COMPRESSION_XPRESS8K = 2
FILE_PROVIDER_COMPRESSION_XPRESS16K = 3
ClfsNullRecord = 0
ClfsDataRecord = 1
ClfsRestartRecord = 2
ClfsClientRecord = 3
ClsContainerInitializing = 1
ClsContainerInactive = 2
ClsContainerActive = 4
ClsContainerActivePendingDelete = 8
ClsContainerPendingArchive = 16
ClsContainerPendingArchiveAndDelete = 32
ClfsContainerInitializing = 1
ClfsContainerInactive = 2
ClfsContainerActive = 4
ClfsContainerActivePendingDelete = 8
ClfsContainerPendingArchive = 16
ClfsContainerPendingArchiveAndDelete = 32
CLFS_MAX_CONTAINER_INFO = 256
CLFS_SCAN_INIT = 1
CLFS_SCAN_FORWARD = 2
CLFS_SCAN_BACKWARD = 4
CLFS_SCAN_CLOSE = 8
CLFS_SCAN_INITIALIZED = 16
CLFS_SCAN_BUFFERED = 32
def _define_SearchPathW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('SearchPathW', windll['KERNEL32.dll']), ((1, 'lpPath'),(1, 'lpFileName'),(1, 'lpExtension'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SearchPathA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR))(('SearchPathA', windll['KERNEL32.dll']), ((1, 'lpPath'),(1, 'lpFileName'),(1, 'lpExtension'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CompareFileTime():
    try:
        return WINFUNCTYPE(Int32,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('CompareFileTime', windll['KERNEL32.dll']), ((1, 'lpFileTime1'),(1, 'lpFileTime2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDirectoryA', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDirectoryW', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.Foundation.HANDLE)(('CreateFileA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwCreationDisposition'),(1, 'dwFlagsAndAttributes'),(1, 'hTemplateFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.Foundation.HANDLE)(('CreateFileW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwCreationDisposition'),(1, 'dwFlagsAndAttributes'),(1, 'hTemplateFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DefineDosDeviceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('DefineDosDeviceW', windll['KERNEL32.dll']), ((1, 'dwFlags'),(1, 'lpDeviceName'),(1, 'lpTargetPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('DeleteFileA', windll['KERNEL32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('DeleteFileW', windll['KERNEL32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteVolumeMountPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('DeleteVolumeMountPointW', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileTimeToLocalFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('FileTimeToLocalFileTime', windll['KERNEL32.dll']), ((1, 'lpFileTime'),(1, 'lpLocalFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindFileHandle)(('FindClose', windll['KERNEL32.dll']), ((1, 'hFindFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindCloseChangeNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindChangeNotificationHandle)(('FindCloseChangeNotification', windll['KERNEL32.dll']), ((1, 'hChangeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstChangeNotificationA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindChangeNotificationHandle,win32more.Foundation.PSTR,win32more.Foundation.BOOL,win32more.Storage.FileSystem.FILE_NOTIFY_CHANGE)(('FindFirstChangeNotificationA', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'bWatchSubtree'),(1, 'dwNotifyFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstChangeNotificationW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindChangeNotificationHandle,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Storage.FileSystem.FILE_NOTIFY_CHANGE)(('FindFirstChangeNotificationW', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'bWatchSubtree'),(1, 'dwNotifyFilter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PSTR,POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAA_head))(('FindFirstFileA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFindFileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAW_head))(('FindFirstFileW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFindFileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileExA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PSTR,win32more.Storage.FileSystem.FINDEX_INFO_LEVELS,c_void_p,win32more.Storage.FileSystem.FINDEX_SEARCH_OPS,c_void_p,win32more.Storage.FileSystem.FIND_FIRST_EX_FLAGS)(('FindFirstFileExA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFindFileData'),(1, 'fSearchOp'),(1, 'lpSearchFilter'),(1, 'dwAdditionalFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileExW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FINDEX_INFO_LEVELS,c_void_p,win32more.Storage.FileSystem.FINDEX_SEARCH_OPS,c_void_p,win32more.Storage.FileSystem.FIND_FIRST_EX_FLAGS)(('FindFirstFileExW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFindFileData'),(1, 'fSearchOp'),(1, 'lpSearchFilter'),(1, 'dwAdditionalFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstVolumeW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindVolumeHandle,win32more.Foundation.PWSTR,UInt32)(('FindFirstVolumeW', windll['KERNEL32.dll']), ((1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextChangeNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindChangeNotificationHandle)(('FindNextChangeNotification', windll['KERNEL32.dll']), ((1, 'hChangeHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindFileHandle,POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAA_head))(('FindNextFileA', windll['KERNEL32.dll']), ((1, 'hFindFile'),(1, 'lpFindFileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindFileHandle,POINTER(win32more.Storage.FileSystem.WIN32_FIND_DATAW_head))(('FindNextFileW', windll['KERNEL32.dll']), ((1, 'hFindFile'),(1, 'lpFindFileData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextVolumeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeHandle,win32more.Foundation.PWSTR,UInt32)(('FindNextVolumeW', windll['KERNEL32.dll']), ((1, 'hFindVolume'),(1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindVolumeClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeHandle)(('FindVolumeClose', windll['KERNEL32.dll']), ((1, 'hFindVolume'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushFileBuffers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('FlushFileBuffers', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskFreeSpaceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetDiskFreeSpaceA', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpSectorsPerCluster'),(1, 'lpBytesPerSector'),(1, 'lpNumberOfFreeClusters'),(1, 'lpTotalNumberOfClusters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskFreeSpaceW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetDiskFreeSpaceW', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpSectorsPerCluster'),(1, 'lpBytesPerSector'),(1, 'lpNumberOfFreeClusters'),(1, 'lpTotalNumberOfClusters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskFreeSpaceExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(win32more.Foundation.ULARGE_INTEGER_head),POINTER(win32more.Foundation.ULARGE_INTEGER_head),POINTER(win32more.Foundation.ULARGE_INTEGER_head))(('GetDiskFreeSpaceExA', windll['KERNEL32.dll']), ((1, 'lpDirectoryName'),(1, 'lpFreeBytesAvailableToCaller'),(1, 'lpTotalNumberOfBytes'),(1, 'lpTotalNumberOfFreeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskFreeSpaceExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.ULARGE_INTEGER_head),POINTER(win32more.Foundation.ULARGE_INTEGER_head),POINTER(win32more.Foundation.ULARGE_INTEGER_head))(('GetDiskFreeSpaceExW', windll['KERNEL32.dll']), ((1, 'lpDirectoryName'),(1, 'lpFreeBytesAvailableToCaller'),(1, 'lpTotalNumberOfBytes'),(1, 'lpTotalNumberOfFreeBytes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskSpaceInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSTR,POINTER(win32more.Storage.FileSystem.DISK_SPACE_INFORMATION_head))(('GetDiskSpaceInformationA', windll['KERNEL32.dll']), ((1, 'rootPath'),(1, 'diskSpaceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDiskSpaceInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.DISK_SPACE_INFORMATION_head))(('GetDiskSpaceInformationW', windll['KERNEL32.dll']), ((1, 'rootPath'),(1, 'diskSpaceInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDriveTypeA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR)(('GetDriveTypeA', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetDriveTypeW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR)(('GetDriveTypeW', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR)(('GetFileAttributesA', windll['KERNEL32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR)(('GetFileAttributesW', windll['KERNEL32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Storage.FileSystem.GET_FILEEX_INFO_LEVELS,c_void_p)(('GetFileAttributesExA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFileInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.GET_FILEEX_INFO_LEVELS,c_void_p)(('GetFileAttributesExW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFileInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileInformationByHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.BY_HANDLE_FILE_INFORMATION_head))(('GetFileInformationByHandle', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpFileInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileSize():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,POINTER(UInt32))(('GetFileSize', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileSizeEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('GetFileSizeEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpFileSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileType():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FILE_TYPE,win32more.Foundation.HANDLE)(('GetFileType', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFinalPathNameByHandleA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,win32more.Storage.FileSystem.FILE_NAME)(('GetFinalPathNameByHandleA', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpszFilePath'),(1, 'cchFilePath'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFinalPathNameByHandleW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,win32more.Storage.FileSystem.FILE_NAME)(('GetFinalPathNameByHandleW', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpszFilePath'),(1, 'cchFilePath'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('GetFileTime', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpCreationTime'),(1, 'lpLastAccessTime'),(1, 'lpLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFullPathNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR))(('GetFullPathNameW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFullPathNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR))(('GetFullPathNameA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogicalDrives():
    try:
        return WINFUNCTYPE(UInt32,)(('GetLogicalDrives', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogicalDriveStringsW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('GetLogicalDriveStringsW', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLongPathNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetLongPathNameA', windll['KERNEL32.dll']), ((1, 'lpszShortPath'),(1, 'lpszLongPath'),(1, 'cchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLongPathNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetLongPathNameW', windll['KERNEL32.dll']), ((1, 'lpszShortPath'),(1, 'lpszLongPath'),(1, 'cchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreShortNamesEnabled():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.BOOL))(('AreShortNamesEnabled', windll['KERNEL32.dll']), ((1, 'Handle'),(1, 'Enabled'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetShortPathNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetShortPathNameW', windll['KERNEL32.dll']), ((1, 'lpszLongPath'),(1, 'lpszShortPath'),(1, 'cchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempFileNameW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR)(('GetTempFileNameW', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'lpPrefixString'),(1, 'uUnique'),(1, 'lpTempFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumeInformationByHandleW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,UInt32)(('GetVolumeInformationByHandleW', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpVolumeNameBuffer'),(1, 'nVolumeNameSize'),(1, 'lpVolumeSerialNumber'),(1, 'lpMaximumComponentLength'),(1, 'lpFileSystemFlags'),(1, 'lpFileSystemNameBuffer'),(1, 'nFileSystemNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumeInformationW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PWSTR,UInt32)(('GetVolumeInformationW', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpVolumeNameBuffer'),(1, 'nVolumeNameSize'),(1, 'lpVolumeSerialNumber'),(1, 'lpMaximumComponentLength'),(1, 'lpFileSystemFlags'),(1, 'lpFileSystemNameBuffer'),(1, 'nFileSystemNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumePathNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetVolumePathNameW', windll['KERNEL32.dll']), ((1, 'lpszFileName'),(1, 'lpszVolumePathName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LocalFileTimeToFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('LocalFileTimeToFileTime', windll['KERNEL32.dll']), ((1, 'lpLocalFileTime'),(1, 'lpFileTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,UInt32)(('LockFile', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'dwFileOffsetLow'),(1, 'dwFileOffsetHigh'),(1, 'nNumberOfBytesToLockLow'),(1, 'nNumberOfBytesToLockHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LockFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.LOCK_FILE_FLAGS,UInt32,UInt32,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(('LockFileEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'dwFlags'),(1, 'dwReserved'),(1, 'nNumberOfBytesToLockLow'),(1, 'nNumberOfBytesToLockHigh'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDosDeviceW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('QueryDosDeviceW', windll['KERNEL32.dll']), ((1, 'lpDeviceName'),(1, 'lpTargetPath'),(1, 'ucchMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadFile', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToRead'),(1, 'lpNumberOfBytesRead'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE)(('ReadFileEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToRead'),(1, 'lpOverlapped'),(1, 'lpCompletionRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadFileScatter():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head),UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadFileScatter', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'aSegmentArray'),(1, 'nNumberOfBytesToRead'),(1, 'lpReserved'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDirectoryA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('RemoveDirectoryA', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDirectoryW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('RemoveDirectoryW', windll['KERNEL32.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEndOfFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('SetEndOfFile', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileAttributesA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES)(('SetFileAttributesA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFileAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileAttributesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES)(('SetFileAttributesW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFileAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileInformationByHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS,c_void_p,UInt32)(('SetFileInformationByHandle', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'FileInformationClass'),(1, 'lpFileInformation'),(1, 'dwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFilePointer():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,Int32,POINTER(Int32),win32more.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD)(('SetFilePointer', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lDistanceToMove'),(1, 'lpDistanceToMoveHigh'),(1, 'dwMoveMethod'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFilePointerEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.LARGE_INTEGER,POINTER(win32more.Foundation.LARGE_INTEGER_head),win32more.Storage.FileSystem.SET_FILE_POINTER_MOVE_METHOD)(('SetFilePointerEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'liDistanceToMove'),(1, 'lpNewFilePointer'),(1, 'dwMoveMethod'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head),POINTER(win32more.Foundation.FILETIME_head))(('SetFileTime', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpCreationTime'),(1, 'lpLastAccessTime'),(1, 'lpLastWriteTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileValidData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Int64)(('SetFileValidData', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'ValidDataLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnlockFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,UInt32)(('UnlockFile', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'dwFileOffsetLow'),(1, 'dwFileOffsetHigh'),(1, 'nNumberOfBytesToUnlockLow'),(1, 'nNumberOfBytesToUnlockHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_UnlockFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(('UnlockFileEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'dwReserved'),(1, 'nNumberOfBytesToUnlockLow'),(1, 'nNumberOfBytesToUnlockHigh'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('WriteFile', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToWrite'),(1, 'lpNumberOfBytesWritten'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteFileEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,POINTER(win32more.System.IO.OVERLAPPED_head),win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE)(('WriteFileEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToWrite'),(1, 'lpOverlapped'),(1, 'lpCompletionRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteFileGather():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head),UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('WriteFileGather', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'aSegmentArray'),(1, 'nNumberOfBytesToWrite'),(1, 'lpReserved'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempPathW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('GetTempPathW', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumeNameForVolumeMountPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('GetVolumeNameForVolumeMountPointW', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),(1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumePathNamesForVolumeNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('GetVolumePathNamesForVolumeNameW', windll['KERNEL32.dll']), ((1, 'lpszVolumeName'),(1, 'lpszVolumePathNames'),(1, 'cchBufferLength'),(1, 'lpcchReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFile2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,POINTER(win32more.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head))(('CreateFile2', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'dwCreationDisposition'),(1, 'pCreateExParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileIoOverlappedRange():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_char_p_no,UInt32)(('SetFileIoOverlappedRange', windll['KERNEL32.dll']), ((1, 'FileHandle'),(1, 'OverlappedRangeStart'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCompressedFileSizeA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32))(('GetCompressedFileSizeA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCompressedFileSizeW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetCompressedFileSizeW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFileSizeHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstStreamW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindStreamHandle,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.STREAM_INFO_LEVELS,c_void_p,UInt32)(('FindFirstStreamW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'InfoLevel'),(1, 'lpFindStreamData'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextStreamW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindStreamHandle,c_void_p)(('FindNextStreamW', windll['KERNEL32.dll']), ((1, 'hFindStream'),(1, 'lpFindStreamData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AreFileApisANSI():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('AreFileApisANSI', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempPathA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('GetTempPathA', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileNameW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileNameHandle,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR)(('FindFirstFileNameW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFlags'),(1, 'StringLength'),(1, 'LinkName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextFileNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindFileNameHandle,POINTER(UInt32),win32more.Foundation.PWSTR)(('FindNextFileNameW', windll['KERNEL32.dll']), ((1, 'hFindStream'),(1, 'StringLength'),(1, 'LinkName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumeInformationA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),win32more.Foundation.PSTR,UInt32)(('GetVolumeInformationA', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpVolumeNameBuffer'),(1, 'nVolumeNameSize'),(1, 'lpVolumeSerialNumber'),(1, 'lpMaximumComponentLength'),(1, 'lpFileSystemFlags'),(1, 'lpFileSystemNameBuffer'),(1, 'nFileSystemNameSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempFileNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR)(('GetTempFileNameA', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'lpPrefixString'),(1, 'uUnique'),(1, 'lpTempFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileApisToOEM():
    try:
        return WINFUNCTYPE(Void,)(('SetFileApisToOEM', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileApisToANSI():
    try:
        return WINFUNCTYPE(Void,)(('SetFileApisToANSI', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempPath2W():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR)(('GetTempPath2W', windll['KERNEL32.dll']), ((1, 'BufferLength'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTempPath2A():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('GetTempPath2A', windll['KERNEL32.dll']), ((1, 'BufferLength'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CopyFileFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'bFailIfExists'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDirectoryFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpPathName'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,UInt32,win32more.Foundation.HANDLE)(('CreateFileFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwCreationDisposition'),(1, 'dwFlagsAndAttributes'),(1, 'hTemplateFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFile2FromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32,UInt32,POINTER(win32more.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head))(('CreateFile2FromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'dwCreationDisposition'),(1, 'pCreateExParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFileFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('DeleteFileFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileExFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FINDEX_INFO_LEVELS,c_void_p,win32more.Storage.FileSystem.FINDEX_SEARCH_OPS,c_void_p,UInt32)(('FindFirstFileExFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFindFileData'),(1, 'fSearchOp'),(1, 'lpSearchFilter'),(1, 'dwAdditionalFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesExFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.GET_FILEEX_INFO_LEVELS,c_void_p)(('GetFileAttributesExFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFileInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('MoveFileFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDirectoryFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('RemoveDirectoryFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpPathName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplaceFileFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_void_p,c_void_p)(('ReplaceFileFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpReplacedFileName'),(1, 'lpReplacementFileName'),(1, 'lpBackupFileName'),(1, 'dwReplaceFlags'),(1, 'lpExclude'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileAttributesFromAppW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32)(('SetFileAttributesFromAppW', windll['api-ms-win-core-file-fromapp-l1-1-0.dll']), ((1, 'lpFileName'),(1, 'dwFileAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerFindFileA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.VER_FIND_FILE_STATUS,win32more.Storage.FileSystem.VER_FIND_FILE_FLAGS,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.PSTR,POINTER(UInt32))(('VerFindFileA', windll['VERSION.dll']), ((1, 'uFlags'),(1, 'szFileName'),(1, 'szWinDir'),(1, 'szAppDir'),(1, 'szCurDir'),(1, 'puCurDirLen'),(1, 'szDestDir'),(1, 'puDestDirLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerFindFileW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.VER_FIND_FILE_STATUS,win32more.Storage.FileSystem.VER_FIND_FILE_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.PWSTR,POINTER(UInt32))(('VerFindFileW', windll['VERSION.dll']), ((1, 'uFlags'),(1, 'szFileName'),(1, 'szWinDir'),(1, 'szAppDir'),(1, 'szCurDir'),(1, 'puCurDirLen'),(1, 'szDestDir'),(1, 'puDestDirLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerInstallFileA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.VER_INSTALL_FILE_STATUS,win32more.Storage.FileSystem.VER_INSTALL_FILE_FLAGS,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(UInt32))(('VerInstallFileA', windll['VERSION.dll']), ((1, 'uFlags'),(1, 'szSrcFileName'),(1, 'szDestFileName'),(1, 'szSrcDir'),(1, 'szDestDir'),(1, 'szCurDir'),(1, 'szTmpFile'),(1, 'puTmpFileLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerInstallFileW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.VER_INSTALL_FILE_STATUS,win32more.Storage.FileSystem.VER_INSTALL_FILE_FLAGS,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('VerInstallFileW', windll['VERSION.dll']), ((1, 'uFlags'),(1, 'szSrcFileName'),(1, 'szDestFileName'),(1, 'szSrcDir'),(1, 'szDestDir'),(1, 'szCurDir'),(1, 'szTmpFile'),(1, 'puTmpFileLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoSizeA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32))(('GetFileVersionInfoSizeA', windll['VERSION.dll']), ((1, 'lptstrFilename'),(1, 'lpdwHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoSizeW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetFileVersionInfoSizeW', windll['VERSION.dll']), ((1, 'lptstrFilename'),(1, 'lpdwHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,UInt32,c_void_p)(('GetFileVersionInfoA', windll['VERSION.dll']), ((1, 'lptstrFilename'),(1, 'dwHandle'),(1, 'dwLen'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32,c_void_p)(('GetFileVersionInfoW', windll['VERSION.dll']), ((1, 'lptstrFilename'),(1, 'dwHandle'),(1, 'dwLen'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoSizeExA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS,win32more.Foundation.PSTR,POINTER(UInt32))(('GetFileVersionInfoSizeExA', windll['VERSION.dll']), ((1, 'dwFlags'),(1, 'lpwstrFilename'),(1, 'lpdwHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoSizeExW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetFileVersionInfoSizeExW', windll['VERSION.dll']), ((1, 'dwFlags'),(1, 'lpwstrFilename'),(1, 'lpdwHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS,win32more.Foundation.PSTR,UInt32,UInt32,c_void_p)(('GetFileVersionInfoExA', windll['VERSION.dll']), ((1, 'dwFlags'),(1, 'lpwstrFilename'),(1, 'dwHandle'),(1, 'dwLen'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileVersionInfoExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.GET_FILE_VERSION_INFO_FLAGS,win32more.Foundation.PWSTR,UInt32,UInt32,c_void_p)(('GetFileVersionInfoExW', windll['VERSION.dll']), ((1, 'dwFlags'),(1, 'lpwstrFilename'),(1, 'dwHandle'),(1, 'dwLen'),(1, 'lpData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerLanguageNameA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR,UInt32)(('VerLanguageNameA', windll['KERNEL32.dll']), ((1, 'wLang'),(1, 'szLang'),(1, 'cchLang'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerLanguageNameW():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PWSTR,UInt32)(('VerLanguageNameW', windll['KERNEL32.dll']), ((1, 'wLang'),(1, 'szLang'),(1, 'cchLang'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerQueryValueA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PSTR,POINTER(c_void_p),POINTER(UInt32))(('VerQueryValueA', windll['VERSION.dll']), ((1, 'pBlock'),(1, 'lpSubBlock'),(1, 'lplpBuffer'),(1, 'puLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_VerQueryValueW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR,POINTER(c_void_p),POINTER(UInt32))(('VerQueryValueW', windll['VERSION.dll']), ((1, 'pBlock'),(1, 'lpSubBlock'),(1, 'lplpBuffer'),(1, 'puLen'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnEqual():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnEqual', windll['clfsw32.dll']), ((1, 'plsn1'),(1, 'plsn2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnLess():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnLess', windll['clfsw32.dll']), ((1, 'plsn1'),(1, 'plsn2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnGreater():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnGreater', windll['clfsw32.dll']), ((1, 'plsn1'),(1, 'plsn2'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnNull():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnNull', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnContainer():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnContainer', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnCreate():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.CLS_LSN,UInt32,UInt32,UInt32)(('LsnCreate', windll['clfsw32.dll']), ((1, 'cidContainer'),(1, 'offBlock'),(1, 'cRecord'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnBlockOffset():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnBlockOffset', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnRecordSequence():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnRecordSequence', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnInvalid():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnInvalid', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LsnIncrement():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.CLS_LSN,POINTER(win32more.Storage.FileSystem.CLS_LSN_head))(('LsnIncrement', windll['clfsw32.dll']), ((1, 'plsn'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateLogFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES)(('CreateLogFile', windll['clfsw32.dll']), ((1, 'pszLogFileName'),(1, 'fDesiredAccess'),(1, 'dwShareMode'),(1, 'psaLogFile'),(1, 'fCreateDisposition'),(1, 'fFlagsAndAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteLogByHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('DeleteLogByHandle', windll['clfsw32.dll']), ((1, 'hLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteLogFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p)(('DeleteLogFile', windll['clfsw32.dll']), ((1, 'pszLogFileName'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddLogContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt64),win32more.Foundation.PWSTR,c_void_p)(('AddLogContainer', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pcbContainer'),(1, 'pwszContainerPath'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddLogContainerSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16,POINTER(UInt64),POINTER(win32more.Foundation.PWSTR),c_void_p)(('AddLogContainerSet', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'cContainer'),(1, 'pcbContainer'),(1, 'rgwszContainerPath'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveLogContainer():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,c_void_p)(('RemoveLogContainer', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pwszContainerPath'),(1, 'fForce'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveLogContainerSet():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt16,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.BOOL,c_void_p)(('RemoveLogContainerSet', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'cContainer'),(1, 'rgwszContainerPath'),(1, 'fForce'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetLogArchiveTail():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),c_void_p)(('SetLogArchiveTail', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'plsnArchiveTail'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEndOfLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('SetEndOfLog', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'plsnEnd'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TruncateLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('TruncateLog', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'plsnEnd'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateLogContainerScanContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,Byte,POINTER(win32more.Storage.FileSystem.CLS_SCAN_CONTEXT_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('CreateLogContainerScanContext', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'cFromContainer'),(1, 'cContainers'),(1, 'eScanMode'),(1, 'pcxScan'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ScanLogContainers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.FileSystem.CLS_SCAN_CONTEXT_head),Byte,c_void_p)(('ScanLogContainers', windll['clfsw32.dll']), ((1, 'pcxScan'),(1, 'eScanMode'),(1, 'pReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AlignReservedLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,POINTER(Int64),POINTER(Int64))(('AlignReservedLog', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'cReservedRecords'),(1, 'rgcbReservation'),(1, 'pcbAlignReservation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AllocReservedLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,POINTER(Int64))(('AllocReservedLog', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'cReservedRecords'),(1, 'pcbAdjustment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeReservedLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,POINTER(Int64))(('FreeReservedLog', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'cReservedRecords'),(1, 'pcbAdjustment'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogFileInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.CLS_INFORMATION_head),POINTER(UInt32))(('GetLogFileInformation', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pinfoBuffer'),(1, 'cbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetLogArchiveMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CLFS_LOG_ARCHIVE_MODE)(('SetLogArchiveMode', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'eMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadLogRestartArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(c_void_p),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadLogRestartArea', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'ppvRestartBuffer'),(1, 'pcbRestartBuffer'),(1, 'plsn'),(1, 'ppvContext'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadPreviousLogRestartArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(c_void_p),POINTER(UInt32),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadPreviousLogRestartArea', windll['clfsw32.dll']), ((1, 'pvReadContext'),(1, 'ppvRestartBuffer'),(1, 'pcbRestartBuffer'),(1, 'plsnRestart'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteLogRestartArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p,UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),win32more.Storage.FileSystem.CLFS_FLAG,POINTER(UInt32),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('WriteLogRestartArea', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'pvRestartBuffer'),(1, 'cbRestartBuffer'),(1, 'plsnBase'),(1, 'fFlags'),(1, 'pcbWritten'),(1, 'plsnNext'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogReservationInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(UInt32),POINTER(Int64),POINTER(Int64))(('GetLogReservationInfo', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'pcbRecordNumber'),(1, 'pcbUserReservation'),(1, 'pcbCommitReservation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AdvanceLogBase():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),UInt32,POINTER(win32more.System.IO.OVERLAPPED_head))(('AdvanceLogBase', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'plsnBase'),(1, 'fFlags'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseAndResetLogFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CloseAndResetLogFile', windll['clfsw32.dll']), ((1, 'hLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateLogMarshallingArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CLFS_BLOCK_ALLOCATION,win32more.Storage.FileSystem.CLFS_BLOCK_DEALLOCATION,c_void_p,UInt32,UInt32,UInt32,POINTER(c_void_p))(('CreateLogMarshallingArea', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pfnAllocBuffer'),(1, 'pfnFreeBuffer'),(1, 'pvBlockAllocContext'),(1, 'cbMarshallingBuffer'),(1, 'cMaxWriteBuffers'),(1, 'cMaxReadBuffers'),(1, 'ppvMarshal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteLogMarshallingArea():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('DeleteLogMarshallingArea', windll['clfsw32.dll']), ((1, 'pvMarshal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReserveAndAppendLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_WRITE_ENTRY_head),UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),UInt32,POINTER(Int64),win32more.Storage.FileSystem.CLFS_FLAG,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReserveAndAppendLog', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'rgWriteEntries'),(1, 'cWriteEntries'),(1, 'plsnUndoNext'),(1, 'plsnPrevious'),(1, 'cReserveRecords'),(1, 'rgcbReservation'),(1, 'fFlags'),(1, 'plsn'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReserveAndAppendLogAligned():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_WRITE_ENTRY_head),UInt32,UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),UInt32,POINTER(Int64),win32more.Storage.FileSystem.CLFS_FLAG,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReserveAndAppendLogAligned', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'rgWriteEntries'),(1, 'cWriteEntries'),(1, 'cbEntryAlignment'),(1, 'plsnUndoNext'),(1, 'plsnPrevious'),(1, 'cReserveRecords'),(1, 'rgcbReservation'),(1, 'fFlags'),(1, 'plsn'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushLogBuffers():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.System.IO.OVERLAPPED_head))(('FlushLogBuffers', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FlushLogToLsn():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('FlushLogToLsn', windll['clfsw32.dll']), ((1, 'pvMarshalContext'),(1, 'plsnFlush'),(1, 'plsnLastFlushed'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadLogRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),win32more.Storage.FileSystem.CLFS_CONTEXT_MODE,POINTER(c_void_p),POINTER(UInt32),c_char_p_no,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(c_void_p),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadLogRecord', windll['clfsw32.dll']), ((1, 'pvMarshal'),(1, 'plsnFirst'),(1, 'eContextMode'),(1, 'ppvReadBuffer'),(1, 'pcbReadBuffer'),(1, 'peRecordType'),(1, 'plsnUndoNext'),(1, 'plsnPrevious'),(1, 'ppvReadContext'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadNextLogRecord():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(c_void_p),POINTER(UInt32),c_char_p_no,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadNextLogRecord', windll['clfsw32.dll']), ((1, 'pvReadContext'),(1, 'ppvBuffer'),(1, 'pcbBuffer'),(1, 'peRecordType'),(1, 'plsnUser'),(1, 'plsnUndoNext'),(1, 'plsnPrevious'),(1, 'plsnRecord'),(1, 'pOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateReadLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('TerminateReadLog', windll['clfsw32.dll']), ((1, 'pvCursorContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrepareLogArchive():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(UInt32),POINTER(UInt64),POINTER(UInt64),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(c_void_p))(('PrepareLogArchive', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pszBaseLogFileName'),(1, 'cLen'),(1, 'plsnLow'),(1, 'plsnHigh'),(1, 'pcActualLength'),(1, 'poffBaseLogFileData'),(1, 'pcbBaseLogFileLength'),(1, 'plsnBase'),(1, 'plsnLast'),(1, 'plsnCurrentArchiveTail'),(1, 'ppvArchiveContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadLogArchiveMetadata():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,UInt32,c_char_p_no,POINTER(UInt32))(('ReadLogArchiveMetadata', windll['clfsw32.dll']), ((1, 'pvArchiveContext'),(1, 'cbOffset'),(1, 'cbBytesToRead'),(1, 'pbReadBuffer'),(1, 'pcbBytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNextLogArchiveExtent():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(win32more.Storage.FileSystem.CLS_ARCHIVE_DESCRIPTOR_head),UInt32,POINTER(UInt32))(('GetNextLogArchiveExtent', windll['clfsw32.dll']), ((1, 'pvArchiveContext'),(1, 'rgadExtent'),(1, 'cDescriptors'),(1, 'pcDescriptorsReturned'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TerminateLogArchive():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('TerminateLogArchive', windll['clfsw32.dll']), ((1, 'pvArchiveContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ValidateLog():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(win32more.Storage.FileSystem.CLS_INFORMATION_head),POINTER(UInt32))(('ValidateLog', windll['clfsw32.dll']), ((1, 'pszLogFileName'),(1, 'psaLogFile'),(1, 'pinfoBuffer'),(1, 'pcbBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogContainerName():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32))(('GetLogContainerName', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'cidLogicalContainer'),(1, 'pwstrContainerName'),(1, 'cLenContainerName'),(1, 'pcActualLenContainerName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogIoStatistics():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Storage.FileSystem.CLFS_IOSTATS_CLASS,POINTER(UInt32))(('GetLogIoStatistics', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pvStatsBuffer'),(1, 'cbStatsBuffer'),(1, 'eStatsClass'),(1, 'pcbStatsWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterManageableLogClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.LOG_MANAGEMENT_CALLBACKS_head))(('RegisterManageableLogClient', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pCallbacks'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeregisterManageableLogClient():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('DeregisterManageableLogClient', windll['clfsw32.dll']), ((1, 'hLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadLogNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_head),POINTER(win32more.System.IO.OVERLAPPED_head))(('ReadLogNotification', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pNotification'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_InstallLogPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.CLFS_MGMT_POLICY_head))(('InstallLogPolicy', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pPolicy'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveLogPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE)(('RemoveLogPolicy', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'ePolicyType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryLogPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE,POINTER(win32more.Storage.FileSystem.CLFS_MGMT_POLICY_head),POINTER(UInt32))(('QueryLogPolicy', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'ePolicyType'),(1, 'pPolicyBuffer'),(1, 'pcbPolicyBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetLogFileSizeWithPolicy():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt64),POINTER(UInt64))(('SetLogFileSizeWithPolicy', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'pDesiredSize'),(1, 'pResultingSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HandleLogFull():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('HandleLogFull', windll['clfsw32.dll']), ((1, 'hLog'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LogTailAdvanceFailure():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32)(('LogTailAdvanceFailure', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'dwReason'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RegisterForLogWriteNotification():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL)(('RegisterForLogWriteNotification', windll['clfsw32.dll']), ((1, 'hLog'),(1, 'cbThreshold'),(1, 'fEnable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryUsersOnEncryptedFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)))(('QueryUsersOnEncryptedFile', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pUsers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryRecoveryAgentsOnEncryptedFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)))(('QueryRecoveryAgentsOnEncryptedFile', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pRecoveryAgents'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveUsersFromEncryptedFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))(('RemoveUsersFromEncryptedFile', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pHashes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AddUsersToEncryptedFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_LIST_head))(('AddUsersToEncryptedFile', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pEncryptionCertificates'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserFileEncryptionKey():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head))(('SetUserFileEncryptionKey', windll['ADVAPI32.dll']), ((1, 'pEncryptionCertificate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetUserFileEncryptionKeyEx():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head),UInt32,UInt32,c_void_p)(('SetUserFileEncryptionKeyEx', windll['ADVAPI32.dll']), ((1, 'pEncryptionCertificate'),(1, 'dwCapabilities'),(1, 'dwFlags'),(1, 'pvReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeEncryptionCertificateHashList():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))(('FreeEncryptionCertificateHashList', windll['ADVAPI32.dll']), ((1, 'pUsers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EncryptionDisable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('EncryptionDisable', windll['ADVAPI32.dll']), ((1, 'DirPath'),(1, 'Disable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DuplicateEncryptionInfoFile():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('DuplicateEncryptionInfoFile', windll['ADVAPI32.dll']), ((1, 'SrcFileName'),(1, 'DstFileName'),(1, 'dwCreationDistribution'),(1, 'dwAttributes'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEncryptedFileMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(c_char_p_no))(('GetEncryptedFileMetadata', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pcbMetadata'),(1, 'ppbMetadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEncryptedFileMetadata():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,c_char_p_no,c_char_p_no,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head),UInt32,POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head))(('SetEncryptedFileMetadata', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'pbOldMetadata'),(1, 'pbNewMetadata'),(1, 'pOwnerHash'),(1, 'dwOperation'),(1, 'pCertificatesAdded'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FreeEncryptedFileMetadata():
    try:
        return WINFUNCTYPE(Void,c_char_p_no)(('FreeEncryptedFileMetadata', windll['ADVAPI32.dll']), ((1, 'pbMetadata'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZStart():
    try:
        return WINFUNCTYPE(Int32,)(('LZStart', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZDone():
    try:
        return WINFUNCTYPE(Void,)(('LZDone', windll['KERNEL32.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyLZFile():
    try:
        return WINFUNCTYPE(Int32,Int32,Int32)(('CopyLZFile', windll['KERNEL32.dll']), ((1, 'hfSource'),(1, 'hfDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZCopy():
    try:
        return WINFUNCTYPE(Int32,Int32,Int32)(('LZCopy', windll['KERNEL32.dll']), ((1, 'hfSource'),(1, 'hfDest'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZInit():
    try:
        return WINFUNCTYPE(Int32,Int32)(('LZInit', windll['KERNEL32.dll']), ((1, 'hfSource'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExpandedNameA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('GetExpandedNameA', windll['KERNEL32.dll']), ((1, 'lpszSource'),(1, 'lpszBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetExpandedNameW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('GetExpandedNameW', windll['KERNEL32.dll']), ((1, 'lpszSource'),(1, 'lpszBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZOpenFileA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(win32more.Storage.FileSystem.OFSTRUCT_head),win32more.Storage.FileSystem.LZOPENFILE_STYLE)(('LZOpenFileA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpReOpenBuf'),(1, 'wStyle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZOpenFileW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.OFSTRUCT_head),win32more.Storage.FileSystem.LZOPENFILE_STYLE)(('LZOpenFileW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpReOpenBuf'),(1, 'wStyle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZSeek():
    try:
        return WINFUNCTYPE(Int32,Int32,Int32,Int32)(('LZSeek', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lOffset'),(1, 'iOrigin'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZRead():
    try:
        return WINFUNCTYPE(Int32,Int32,win32more.Foundation.PSTR,Int32)(('LZRead', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'cbRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_LZClose():
    try:
        return WINFUNCTYPE(Void,Int32)(('LZClose', windll['KERNEL32.dll']), ((1, 'hFile'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofShouldCompressBinaries():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32))(('WofShouldCompressBinaries', windll['WOFUTIL.dll']), ((1, 'Volume'),(1, 'Algorithm'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofGetDriverVersion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,POINTER(UInt32))(('WofGetDriverVersion', windll['WOFUTIL.dll']), ((1, 'FileOrVolumeHandle'),(1, 'Provider'),(1, 'WofVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofSetFileDataLocation():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.HANDLE,UInt32,c_void_p,UInt32)(('WofSetFileDataLocation', windll['WOFUTIL.dll']), ((1, 'FileHandle'),(1, 'Provider'),(1, 'ExternalFileInfo'),(1, 'Length'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofIsExternalFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.BOOL),POINTER(UInt32),c_void_p,POINTER(UInt32))(('WofIsExternalFile', windll['WOFUTIL.dll']), ((1, 'FilePath'),(1, 'IsExternalFile'),(1, 'Provider'),(1, 'ExternalFileInfo'),(1, 'BufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofEnumEntries():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Storage.FileSystem.WofEnumEntryProc,c_void_p)(('WofEnumEntries', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'Provider'),(1, 'EnumProc'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofWimAddEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('WofWimAddEntry', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'WimPath'),(1, 'WimType'),(1, 'WimIndex'),(1, 'DataSourceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofWimEnumFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.LARGE_INTEGER,win32more.Storage.FileSystem.WofEnumFilesProc,c_void_p)(('WofWimEnumFiles', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'DataSourceId'),(1, 'EnumProc'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofWimSuspendEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.LARGE_INTEGER)(('WofWimSuspendEntry', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'DataSourceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofWimRemoveEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.LARGE_INTEGER)(('WofWimRemoveEntry', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'DataSourceId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofWimUpdateEntry():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.PWSTR)(('WofWimUpdateEntry', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'DataSourceId'),(1, 'NewWimPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WofFileEnumFiles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Storage.FileSystem.WofEnumFilesProc,c_void_p)(('WofFileEnumFiles', windll['WOFUTIL.dll']), ((1, 'VolumeName'),(1, 'Algorithm'),(1, 'EnumProc'),(1, 'UserData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogCreateFileReadContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.CLS_LSN,win32more.Storage.FileSystem.CLS_LSN,POINTER(win32more.Storage.FileSystem.TXF_ID_head),POINTER(c_void_p))(('TxfLogCreateFileReadContext', windll['txfw32.dll']), ((1, 'LogPath'),(1, 'BeginningLsn'),(1, 'EndingLsn'),(1, 'TxfFileId'),(1, 'TxfLogContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogCreateRangeReadContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.CLS_LSN,win32more.Storage.FileSystem.CLS_LSN,POINTER(win32more.Foundation.LARGE_INTEGER_head),POINTER(win32more.Foundation.LARGE_INTEGER_head),UInt32,POINTER(c_void_p))(('TxfLogCreateRangeReadContext', windll['txfw32.dll']), ((1, 'LogPath'),(1, 'BeginningLsn'),(1, 'EndingLsn'),(1, 'BeginningVirtualClock'),(1, 'EndingVirtualClock'),(1, 'RecordTypeMask'),(1, 'TxfLogContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogDestroyReadContext():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('TxfLogDestroyReadContext', windll['txfw32.dll']), ((1, 'TxfLogContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogReadRecords():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,c_void_p,POINTER(UInt32),POINTER(UInt32))(('TxfLogReadRecords', windll['txfw32.dll']), ((1, 'TxfLogContext'),(1, 'BufferLength'),(1, 'Buffer'),(1, 'BytesUsed'),(1, 'RecordCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfReadMetadataInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.TXF_ID_head),POINTER(win32more.Storage.FileSystem.CLS_LSN_head),POINTER(UInt32),POINTER(Guid))(('TxfReadMetadataInfo', windll['txfw32.dll']), ((1, 'FileHandle'),(1, 'TxfFileId'),(1, 'LastLsn'),(1, 'TransactionState'),(1, 'LockingTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogRecordGetFileName():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),POINTER(win32more.Storage.FileSystem.TXF_ID_head))(('TxfLogRecordGetFileName', windll['txfw32.dll']), ((1, 'RecordBuffer'),(1, 'RecordBufferLengthInBytes'),(1, 'NameBuffer'),(1, 'NameBufferLengthInBytes'),(1, 'TxfId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfLogRecordGetGenericType():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Foundation.LARGE_INTEGER_head))(('TxfLogRecordGetGenericType', windll['txfw32.dll']), ((1, 'RecordBuffer'),(1, 'RecordBufferLengthInBytes'),(1, 'GenericType'),(1, 'VirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfSetThreadMiniVersionForCreate():
    try:
        return WINFUNCTYPE(Void,UInt16)(('TxfSetThreadMiniVersionForCreate', windll['txfw32.dll']), ((1, 'MiniVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_TxfGetThreadMiniVersionForCreate():
    try:
        return WINFUNCTYPE(Void,POINTER(UInt16))(('TxfGetThreadMiniVersionForCreate', windll['txfw32.dll']), ((1, 'MiniVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(Guid),UInt32,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('CreateTransaction', windll['ktmw32.dll']), ((1, 'lpTransactionAttributes'),(1, 'UOW'),(1, 'CreateOptions'),(1, 'IsolationLevel'),(1, 'IsolationFlags'),(1, 'Timeout'),(1, 'Description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,POINTER(Guid))(('OpenTransaction', windll['ktmw32.dll']), ((1, 'dwDesiredAccess'),(1, 'TransactionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommitTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CommitTransaction', windll['ktmw32.dll']), ((1, 'TransactionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommitTransactionAsync():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('CommitTransactionAsync', windll['ktmw32.dll']), ((1, 'TransactionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RollbackTransaction():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RollbackTransaction', windll['ktmw32.dll']), ((1, 'TransactionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RollbackTransactionAsync():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RollbackTransactionAsync', windll['ktmw32.dll']), ((1, 'TransactionHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTransactionId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Guid))(('GetTransactionId', windll['ktmw32.dll']), ((1, 'TransactionHandle'),(1, 'TransactionId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTransactionInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),POINTER(UInt32),UInt32,win32more.Foundation.PWSTR)(('GetTransactionInformation', windll['ktmw32.dll']), ((1, 'TransactionHandle'),(1, 'Outcome'),(1, 'IsolationLevel'),(1, 'IsolationFlags'),(1, 'Timeout'),(1, 'BufferLength'),(1, 'Description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTransactionInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,UInt32,win32more.Foundation.PWSTR)(('SetTransactionInformation', windll['ktmw32.dll']), ((1, 'TransactionHandle'),(1, 'IsolationLevel'),(1, 'IsolationFlags'),(1, 'Timeout'),(1, 'Description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.PWSTR,UInt32,UInt32)(('CreateTransactionManager', windll['ktmw32.dll']), ((1, 'lpTransactionAttributes'),(1, 'LogFileName'),(1, 'CreateOptions'),(1, 'CommitStrength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,UInt32)(('OpenTransactionManager', windll['ktmw32.dll']), ((1, 'LogFileName'),(1, 'DesiredAccess'),(1, 'OpenOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenTransactionManagerById():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(Guid),UInt32,UInt32)(('OpenTransactionManagerById', windll['ktmw32.dll']), ((1, 'TransactionManagerId'),(1, 'DesiredAccess'),(1, 'OpenOptions'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RenameTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(Guid))(('RenameTransactionManager', windll['ktmw32.dll']), ((1, 'LogFileName'),(1, 'ExistingTransactionManagerGuid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RollforwardTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('RollforwardTransactionManager', windll['ktmw32.dll']), ((1, 'TransactionManagerHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecoverTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RecoverTransactionManager', windll['ktmw32.dll']), ((1, 'TransactionManagerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCurrentClockTransactionManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('GetCurrentClockTransactionManager', windll['ktmw32.dll']), ((1, 'TransactionManagerHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTransactionManagerId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Guid))(('GetTransactionManagerId', windll['ktmw32.dll']), ((1, 'TransactionManagerHandle'),(1, 'TransactionManagerId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),POINTER(Guid),UInt32,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('CreateResourceManager', windll['ktmw32.dll']), ((1, 'lpResourceManagerAttributes'),(1, 'ResourceManagerId'),(1, 'CreateOptions'),(1, 'TmHandle'),(1, 'Description'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE,POINTER(Guid))(('OpenResourceManager', windll['ktmw32.dll']), ((1, 'dwDesiredAccess'),(1, 'TmHandle'),(1, 'ResourceManagerId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecoverResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE)(('RecoverResourceManager', windll['ktmw32.dll']), ((1, 'ResourceManagerHandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNotificationResourceManager():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_head),UInt32,UInt32,POINTER(UInt32))(('GetNotificationResourceManager', windll['ktmw32.dll']), ((1, 'ResourceManagerHandle'),(1, 'TransactionNotification'),(1, 'NotificationLength'),(1, 'dwMilliseconds'),(1, 'ReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetNotificationResourceManagerAsync():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_head),UInt32,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head))(('GetNotificationResourceManagerAsync', windll['ktmw32.dll']), ((1, 'ResourceManagerHandle'),(1, 'TransactionNotification'),(1, 'TransactionNotificationLength'),(1, 'ReturnLength'),(1, 'lpOverlapped'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetResourceManagerCompletionPort():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UIntPtr)(('SetResourceManagerCompletionPort', windll['ktmw32.dll']), ((1, 'ResourceManagerHandle'),(1, 'IoCompletionPortHandle'),(1, 'CompletionKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,UInt32,UInt32,c_void_p)(('CreateEnlistment', windll['ktmw32.dll']), ((1, 'lpEnlistmentAttributes'),(1, 'ResourceManagerHandle'),(1, 'TransactionHandle'),(1, 'NotificationMask'),(1, 'CreateOptions'),(1, 'EnlistmentKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,UInt32,win32more.Foundation.HANDLE,POINTER(Guid))(('OpenEnlistment', windll['ktmw32.dll']), ((1, 'dwDesiredAccess'),(1, 'ResourceManagerHandle'),(1, 'EnlistmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RecoverEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p)(('RecoverEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'EnlistmentKey'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnlistmentRecoveryInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p,POINTER(UInt32))(('GetEnlistmentRecoveryInformation', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'BufferSize'),(1, 'Buffer'),(1, 'BufferUsed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetEnlistmentId():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(Guid))(('GetEnlistmentId', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'EnlistmentId'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetEnlistmentRecoveryInformation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,c_void_p)(('SetEnlistmentRecoveryInformation', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'BufferSize'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrepareEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('PrepareEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrePrepareEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('PrePrepareEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommitEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('CommitEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RollbackEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('RollbackEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrePrepareComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('PrePrepareComplete', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrepareComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('PrepareComplete', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadOnlyEnlistment():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('ReadOnlyEnlistment', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CommitComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('CommitComplete', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RollbackComplete():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('RollbackComplete', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SinglePhaseReject():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(win32more.Foundation.LARGE_INTEGER_head))(('SinglePhaseReject', windll['ktmw32.dll']), ((1, 'EnlistmentHandle'),(1, 'TmVirtualClock'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetShareAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetShareEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareEnumSticky():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetShareEnumSticky', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetShareGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'netname'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareSetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,c_char_p_no,POINTER(UInt32))(('NetShareSetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'netname'),(1, 'level'),(1, 'buf'),(1, 'parm_err'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetShareDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'netname'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareDelSticky():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('NetShareDelSticky', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'netname'),(1, 'reserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareCheck():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(UInt32))(('NetShareCheck', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'device'),(1, 'type'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetShareDelEx():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetShareDelEx', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerAliasAdd():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetServerAliasAdd', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerAliasDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,c_char_p_no)(('NetServerAliasDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'buf'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetServerAliasEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetServerAliasEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resumehandle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetSessionEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetSessionEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'UncClientName'),(1, 'username'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetSessionDel():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('NetSessionDel', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'UncClientName'),(1, 'username'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetSessionGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no))(('NetSessionGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'UncClientName'),(1, 'username'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetConnectionEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('NetConnectionEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'qualifier'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetFileClose():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32)(('NetFileClose', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'fileid'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetFileEnum():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,POINTER(c_char_p_no),UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(UIntPtr))(('NetFileEnum', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'basepath'),(1, 'username'),(1, 'level'),(1, 'bufptr'),(1, 'prefmaxlen'),(1, 'entriesread'),(1, 'totalentries'),(1, 'resume_handle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetFileGetInfo():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(c_char_p_no))(('NetFileGetInfo', windll['NETAPI32.dll']), ((1, 'servername'),(1, 'fileid'),(1, 'level'),(1, 'bufptr'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NetStatisticsGet():
    try:
        return WINFUNCTYPE(UInt32,POINTER(SByte),POINTER(SByte),UInt32,UInt32,POINTER(c_char_p_no))(('NetStatisticsGet', windll['NETAPI32.dll']), ((1, 'ServerName'),(1, 'Service'),(1, 'Level'),(1, 'Options'),(1, 'Buffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryIoRingCapabilities():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.IORING_CAPABILITIES_head))(('QueryIoRingCapabilities', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'capabilities'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_IsIoRingOpSupported():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Storage.FileSystem.HIORING___head),win32more.Storage.FileSystem.IORING_OP_CODE)(('IsIoRingOpSupported', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'op'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateIoRing():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IORING_VERSION,win32more.Storage.FileSystem.IORING_CREATE_FLAGS,UInt32,UInt32,POINTER(POINTER(win32more.Storage.FileSystem.HIORING___head)))(('CreateIoRing', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioringVersion'),(1, 'flags'),(1, 'submissionQueueSize'),(1, 'completionQueueSize'),(1, 'h'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetIoRingInfo():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),POINTER(win32more.Storage.FileSystem.IORING_INFO_head))(('GetIoRingInfo', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'info'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SubmitIoRing():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),UInt32,UInt32,POINTER(UInt32))(('SubmitIoRing', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'waitOperations'),(1, 'milliseconds'),(1, 'submittedEntries'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseIoRing():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head))(('CloseIoRing', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PopIoRingCompletion():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),POINTER(win32more.Storage.FileSystem.IORING_CQE_head))(('PopIoRingCompletion', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'cqe'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetIoRingCompletionEvent():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),win32more.Foundation.HANDLE)(('SetIoRingCompletionEvent', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'hEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildIoRingCancelRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),win32more.Storage.FileSystem.IORING_HANDLE_REF,UIntPtr,UIntPtr)(('BuildIoRingCancelRequest', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'file'),(1, 'opToCancel'),(1, 'userData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildIoRingReadFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),win32more.Storage.FileSystem.IORING_HANDLE_REF,win32more.Storage.FileSystem.IORING_BUFFER_REF,UInt32,UInt64,UIntPtr,win32more.Storage.FileSystem.IORING_SQE_FLAGS)(('BuildIoRingReadFile', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'fileRef'),(1, 'dataRef'),(1, 'numberOfBytesToRead'),(1, 'fileOffset'),(1, 'userData'),(1, 'flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildIoRingRegisterFileHandles():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),UInt32,POINTER(win32more.Foundation.HANDLE),UIntPtr)(('BuildIoRingRegisterFileHandles', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'count'),(1, 'handles'),(1, 'userData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BuildIoRingRegisterBuffers():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.HIORING___head),UInt32,POINTER(win32more.Storage.FileSystem.IORING_BUFFER_INFO_head),UIntPtr)(('BuildIoRingRegisterBuffers', windll['api-ms-win-core-ioring-l1-1-0.dll']), ((1, 'ioRing'),(1, 'count'),(1, 'buffers'),(1, 'userData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Wow64EnableWow64FsRedirection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.BOOLEAN)(('Wow64EnableWow64FsRedirection', windll['KERNEL32.dll']), ((1, 'Wow64FsEnableRedirection'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Wow64DisableWow64FsRedirection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(c_void_p))(('Wow64DisableWow64FsRedirection', windll['KERNEL32.dll']), ((1, 'OldValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Wow64RevertWow64FsRedirection():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('Wow64RevertWow64FsRedirection', windll['KERNEL32.dll']), ((1, 'OlValue'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBinaryTypeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(UInt32))(('GetBinaryTypeA', windll['KERNEL32.dll']), ((1, 'lpApplicationName'),(1, 'lpBinaryType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetBinaryTypeW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32))(('GetBinaryTypeW', windll['KERNEL32.dll']), ((1, 'lpApplicationName'),(1, 'lpBinaryType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetShortPathNameA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetShortPathNameA', windll['KERNEL32.dll']), ((1, 'lpszLongPath'),(1, 'lpszShortPath'),(1, 'cchBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLongPathNameTransactedA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,win32more.Foundation.HANDLE)(('GetLongPathNameTransactedA', windll['KERNEL32.dll']), ((1, 'lpszShortPath'),(1, 'lpszLongPath'),(1, 'cchBuffer'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLongPathNameTransactedW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.HANDLE)(('GetLongPathNameTransactedW', windll['KERNEL32.dll']), ((1, 'lpszShortPath'),(1, 'lpszLongPath'),(1, 'cchBuffer'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileCompletionNotificationModes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,Byte)(('SetFileCompletionNotificationModes', windll['KERNEL32.dll']), ((1, 'FileHandle'),(1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileShortNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PSTR)(('SetFileShortNameA', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpShortName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileShortNameW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Foundation.PWSTR)(('SetFileShortNameW', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpShortName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTapePosition():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.TAPE_POSITION_METHOD,UInt32,UInt32,UInt32,win32more.Foundation.BOOL)(('SetTapePosition', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwPositionMethod'),(1, 'dwPartition'),(1, 'dwOffsetLow'),(1, 'dwOffsetHigh'),(1, 'bImmediate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTapePosition():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.TAPE_POSITION_TYPE,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('GetTapePosition', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwPositionType'),(1, 'lpdwPartition'),(1, 'lpdwOffsetLow'),(1, 'lpdwOffsetHigh'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrepareTape():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.PREPARE_TAPE_OPERATION,win32more.Foundation.BOOL)(('PrepareTape', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwOperation'),(1, 'bImmediate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EraseTape():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.ERASE_TAPE_TYPE,win32more.Foundation.BOOL)(('EraseTape', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwEraseType'),(1, 'bImmediate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateTapePartition():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CREATE_TAPE_PARTITION_METHOD,UInt32,UInt32)(('CreateTapePartition', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwPartitionMethod'),(1, 'dwCount'),(1, 'dwSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteTapemark():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.TAPEMARK_TYPE,UInt32,win32more.Foundation.BOOL)(('WriteTapemark', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwTapemarkType'),(1, 'dwTapemarkCount'),(1, 'bImmediate'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTapeStatus():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE)(('GetTapeStatus', windll['KERNEL32.dll']), ((1, 'hDevice'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetTapeParameters():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.GET_TAPE_DRIVE_PARAMETERS_OPERATION,POINTER(UInt32),c_void_p)(('GetTapeParameters', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwOperation'),(1, 'lpdwSize'),(1, 'lpTapeInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetTapeParameters():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.TAPE_INFORMATION_TYPE,c_void_p)(('SetTapeParameters', windll['KERNEL32.dll']), ((1, 'hDevice'),(1, 'dwOperation'),(1, 'lpTapeInformation'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EncryptFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('EncryptFileA', windll['ADVAPI32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EncryptFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR)(('EncryptFileW', windll['ADVAPI32.dll']), ((1, 'lpFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DecryptFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32)(('DecryptFileA', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DecryptFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32)(('DecryptFileW', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileEncryptionStatusA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,POINTER(UInt32))(('FileEncryptionStatusA', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'lpStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FileEncryptionStatusW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(UInt32))(('FileEncryptionStatusW', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'lpStatus'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEncryptedFileRawA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,POINTER(c_void_p))(('OpenEncryptedFileRawA', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'ulFlags'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenEncryptedFileRawW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,POINTER(c_void_p))(('OpenEncryptedFileRawW', windll['ADVAPI32.dll']), ((1, 'lpFileName'),(1, 'ulFlags'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadEncryptedFileRaw():
    try:
        return WINFUNCTYPE(UInt32,win32more.Storage.FileSystem.PFE_EXPORT_FUNC,c_void_p,c_void_p)(('ReadEncryptedFileRaw', windll['ADVAPI32.dll']), ((1, 'pfExportCallback'),(1, 'pvCallbackContext'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WriteEncryptedFileRaw():
    try:
        return WINFUNCTYPE(UInt32,win32more.Storage.FileSystem.PFE_IMPORT_FUNC,c_void_p,c_void_p)(('WriteEncryptedFileRaw', windll['ADVAPI32.dll']), ((1, 'pfImportCallback'),(1, 'pvCallbackContext'),(1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CloseEncryptedFileRaw():
    try:
        return WINFUNCTYPE(Void,c_void_p)(('CloseEncryptedFileRaw', windll['ADVAPI32.dll']), ((1, 'pvContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenFile():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,POINTER(win32more.Storage.FileSystem.OFSTRUCT_head),UInt32)(('OpenFile', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpReOpenBuff'),(1, 'uStyle'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BackupRead():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_char_p_no,UInt32,POINTER(UInt32),win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(c_void_p))(('BackupRead', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToRead'),(1, 'lpNumberOfBytesRead'),(1, 'bAbort'),(1, 'bProcessSecurity'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BackupSeek():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,POINTER(UInt32),POINTER(UInt32),POINTER(c_void_p))(('BackupSeek', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'dwLowBytesToSeek'),(1, 'dwHighBytesToSeek'),(1, 'lpdwLowByteSeeked'),(1, 'lpdwHighByteSeeked'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BackupWrite():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_char_p_no,UInt32,POINTER(UInt32),win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(c_void_p))(('BackupWrite', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpBuffer'),(1, 'nNumberOfBytesToWrite'),(1, 'lpNumberOfBytesWritten'),(1, 'bAbort'),(1, 'bProcessSecurity'),(1, 'lpContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetLogicalDriveStringsA():
    try:
        return WINFUNCTYPE(UInt32,UInt32,win32more.Foundation.PSTR)(('GetLogicalDriveStringsA', windll['KERNEL32.dll']), ((1, 'nBufferLength'),(1, 'lpBuffer'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetSearchPathMode():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32)(('SetSearchPathMode', windll['KERNEL32.dll']), ((1, 'Flags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDirectoryExA', windll['KERNEL32.dll']), ((1, 'lpTemplateDirectory'),(1, 'lpNewDirectory'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateDirectoryExW', windll['KERNEL32.dll']), ((1, 'lpTemplateDirectory'),(1, 'lpNewDirectory'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.HANDLE)(('CreateDirectoryTransactedA', windll['KERNEL32.dll']), ((1, 'lpTemplateDirectory'),(1, 'lpNewDirectory'),(1, 'lpSecurityAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateDirectoryTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.HANDLE)(('CreateDirectoryTransactedW', windll['KERNEL32.dll']), ((1, 'lpTemplateDirectory'),(1, 'lpNewDirectory'),(1, 'lpSecurityAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDirectoryTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.HANDLE)(('RemoveDirectoryTransactedA', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_RemoveDirectoryTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE)(('RemoveDirectoryTransactedW', windll['KERNEL32.dll']), ((1, 'lpPathName'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFullPathNameTransactedA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,UInt32,win32more.Foundation.PSTR,POINTER(win32more.Foundation.PSTR),win32more.Foundation.HANDLE)(('GetFullPathNameTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFullPathNameTransactedW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),win32more.Foundation.HANDLE)(('GetFullPathNameTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'nBufferLength'),(1, 'lpBuffer'),(1, 'lpFilePart'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DefineDosDeviceA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.DEFINE_DOS_DEVICE_FLAGS,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('DefineDosDeviceA', windll['KERNEL32.dll']), ((1, 'dwFlags'),(1, 'lpDeviceName'),(1, 'lpTargetPath'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_QueryDosDeviceA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('QueryDosDeviceA', windll['KERNEL32.dll']), ((1, 'lpDeviceName'),(1, 'lpTargetPath'),(1, 'ucchMax'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,UInt32,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.TXFS_MINIVERSION),c_void_p)(('CreateFileTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwCreationDisposition'),(1, 'dwFlagsAndAttributes'),(1, 'hTemplateFile'),(1, 'hTransaction'),(1, 'pusMiniVersion'),(1, 'lpExtendedParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateFileTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PWSTR,UInt32,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_CREATION_DISPOSITION,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.TXFS_MINIVERSION),c_void_p)(('CreateFileTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwCreationDisposition'),(1, 'dwFlagsAndAttributes'),(1, 'hTemplateFile'),(1, 'hTransaction'),(1, 'pusMiniVersion'),(1, 'lpExtendedParameter'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReOpenFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES)(('ReOpenFile', windll['KERNEL32.dll']), ((1, 'hOriginalFile'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'dwFlagsAndAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileAttributesTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,UInt32,win32more.Foundation.HANDLE)(('SetFileAttributesTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFileAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileAttributesTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.HANDLE)(('SetFileAttributesTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFileAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Storage.FileSystem.GET_FILEEX_INFO_LEVELS,c_void_p,win32more.Foundation.HANDLE)(('GetFileAttributesTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFileInformation'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileAttributesTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.GET_FILEEX_INFO_LEVELS,c_void_p,win32more.Foundation.HANDLE)(('GetFileAttributesTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFileInformation'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCompressedFileSizeTransactedA():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PSTR,POINTER(UInt32),win32more.Foundation.HANDLE)(('GetCompressedFileSizeTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFileSizeHigh'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetCompressedFileSizeTransactedW():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.PWSTR,POINTER(UInt32),win32more.Foundation.HANDLE)(('GetCompressedFileSizeTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpFileSizeHigh'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFileTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.HANDLE)(('DeleteFileTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteFileTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.HANDLE)(('DeleteFileTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckNameLegalDOS8Dot3A():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(('CheckNameLegalDOS8Dot3A', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpOemName'),(1, 'OemNameSize'),(1, 'pbNameContainsSpaces'),(1, 'pbNameLegal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CheckNameLegalDOS8Dot3W():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PSTR,UInt32,POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))(('CheckNameLegalDOS8Dot3W', windll['KERNEL32.dll']), ((1, 'lpName'),(1, 'lpOemName'),(1, 'OemNameSize'),(1, 'pbNameContainsSpaces'),(1, 'pbNameLegal'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileTransactedA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PSTR,win32more.Storage.FileSystem.FINDEX_INFO_LEVELS,c_void_p,win32more.Storage.FileSystem.FINDEX_SEARCH_OPS,c_void_p,UInt32,win32more.Foundation.HANDLE)(('FindFirstFileTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFindFileData'),(1, 'fSearchOp'),(1, 'lpSearchFilter'),(1, 'dwAdditionalFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileTransactedW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileHandle,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.FINDEX_INFO_LEVELS,c_void_p,win32more.Storage.FileSystem.FINDEX_SEARCH_OPS,c_void_p,UInt32,win32more.Foundation.HANDLE)(('FindFirstFileTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'fInfoLevelId'),(1, 'lpFindFileData'),(1, 'fSearchOp'),(1, 'lpSearchFilter'),(1, 'dwAdditionalFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.BOOL)(('CopyFileA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'bFailIfExists'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(('CopyFileW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'bFailIfExists'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,POINTER(Int32),UInt32)(('CopyFileExA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'pbCancel'),(1, 'dwCopyFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,POINTER(Int32),UInt32)(('CopyFileExW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'pbCancel'),(1, 'dwCopyFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,POINTER(Int32),UInt32,win32more.Foundation.HANDLE)(('CopyFileTransactedA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'pbCancel'),(1, 'dwCopyFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFileTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,POINTER(Int32),UInt32,win32more.Foundation.HANDLE)(('CopyFileTransactedW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'pbCancel'),(1, 'dwCopyFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CopyFile2():
    try:
        return WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS_head))(('CopyFile2', windll['KERNEL32.dll']), ((1, 'pwszExistingFileName'),(1, 'pwszNewFileName'),(1, 'pExtendedParameters'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('MoveFileA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('MoveFileW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileExA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.MOVE_FILE_FLAGS)(('MoveFileExA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.MOVE_FILE_FLAGS)(('MoveFileExW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileWithProgressA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,win32more.Storage.FileSystem.MOVE_FILE_FLAGS)(('MoveFileWithProgressA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileWithProgressW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,win32more.Storage.FileSystem.MOVE_FILE_FLAGS)(('MoveFileWithProgressW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,win32more.Storage.FileSystem.MOVE_FILE_FLAGS,win32more.Foundation.HANDLE)(('MoveFileTransactedA', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'dwFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_MoveFileTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE,c_void_p,win32more.Storage.FileSystem.MOVE_FILE_FLAGS,win32more.Foundation.HANDLE)(('MoveFileTransactedW', windll['KERNEL32.dll']), ((1, 'lpExistingFileName'),(1, 'lpNewFileName'),(1, 'lpProgressRoutine'),(1, 'lpData'),(1, 'dwFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplaceFileA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.REPLACE_FILE_FLAGS,c_void_p,c_void_p)(('ReplaceFileA', windll['KERNEL32.dll']), ((1, 'lpReplacedFileName'),(1, 'lpReplacementFileName'),(1, 'lpBackupFileName'),(1, 'dwReplaceFlags'),(1, 'lpExclude'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReplaceFileW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.REPLACE_FILE_FLAGS,c_void_p,c_void_p)(('ReplaceFileW', windll['KERNEL32.dll']), ((1, 'lpReplacedFileName'),(1, 'lpReplacementFileName'),(1, 'lpBackupFileName'),(1, 'dwReplaceFlags'),(1, 'lpExclude'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHardLinkA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateHardLinkA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpExistingFileName'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHardLinkW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head))(('CreateHardLinkW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpExistingFileName'),(1, 'lpSecurityAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHardLinkTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.HANDLE)(('CreateHardLinkTransactedA', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpExistingFileName'),(1, 'lpSecurityAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateHardLinkTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Foundation.HANDLE)(('CreateHardLinkTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'lpExistingFileName'),(1, 'lpSecurityAttributes'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstStreamTransactedW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindStreamHandle,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.STREAM_INFO_LEVELS,c_void_p,UInt32,win32more.Foundation.HANDLE)(('FindFirstStreamTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'InfoLevel'),(1, 'lpFindStreamData'),(1, 'dwFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstFileNameTransactedW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindFileNameHandle,win32more.Foundation.PWSTR,UInt32,POINTER(UInt32),win32more.Foundation.PWSTR,win32more.Foundation.HANDLE)(('FindFirstFileNameTransactedW', windll['KERNEL32.dll']), ((1, 'lpFileName'),(1, 'dwFlags'),(1, 'StringLength'),(1, 'LinkName'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVolumeLabelA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SetVolumeLabelA', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpVolumeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVolumeLabelW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SetVolumeLabelW', windll['KERNEL32.dll']), ((1, 'lpRootPathName'),(1, 'lpVolumeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetFileBandwidthReservation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,UInt32,UInt32,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(UInt32))(('SetFileBandwidthReservation', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'nPeriodMilliseconds'),(1, 'nBytesPerPeriod'),(1, 'bDiscardable'),(1, 'lpTransferSize'),(1, 'lpNumOutstandingRequests'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileBandwidthReservation():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,POINTER(UInt32),POINTER(UInt32),POINTER(Int32),POINTER(UInt32),POINTER(UInt32))(('GetFileBandwidthReservation', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'lpPeriodMilliseconds'),(1, 'lpBytesPerPeriod'),(1, 'pDiscardable'),(1, 'lpTransferSize'),(1, 'lpNumOutstandingRequests'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadDirectoryChangesW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.BOOL,win32more.Storage.FileSystem.FILE_NOTIFY_CHANGE,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head),win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE)(('ReadDirectoryChangesW', windll['KERNEL32.dll']), ((1, 'hDirectory'),(1, 'lpBuffer'),(1, 'nBufferLength'),(1, 'bWatchSubtree'),(1, 'dwNotifyFilter'),(1, 'lpBytesReturned'),(1, 'lpOverlapped'),(1, 'lpCompletionRoutine'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ReadDirectoryChangesExW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,c_void_p,UInt32,win32more.Foundation.BOOL,win32more.Storage.FileSystem.FILE_NOTIFY_CHANGE,POINTER(UInt32),POINTER(win32more.System.IO.OVERLAPPED_head),win32more.System.IO.LPOVERLAPPED_COMPLETION_ROUTINE,win32more.Storage.FileSystem.READ_DIRECTORY_NOTIFY_INFORMATION_CLASS)(('ReadDirectoryChangesExW', windll['KERNEL32.dll']), ((1, 'hDirectory'),(1, 'lpBuffer'),(1, 'nBufferLength'),(1, 'bWatchSubtree'),(1, 'dwNotifyFilter'),(1, 'lpBytesReturned'),(1, 'lpOverlapped'),(1, 'lpCompletionRoutine'),(1, 'ReadDirectoryNotifyInformationClass'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstVolumeA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindVolumeHandle,win32more.Foundation.PSTR,UInt32)(('FindFirstVolumeA', windll['KERNEL32.dll']), ((1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextVolumeA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeHandle,win32more.Foundation.PSTR,UInt32)(('FindNextVolumeA', windll['KERNEL32.dll']), ((1, 'hFindVolume'),(1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstVolumeMountPointA():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindVolumeMointPointHandle,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('FindFirstVolumeMountPointA', windll['KERNEL32.dll']), ((1, 'lpszRootPathName'),(1, 'lpszVolumeMountPoint'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindFirstVolumeMountPointW():
    try:
        return WINFUNCTYPE(win32more.Storage.FileSystem.FindVolumeMointPointHandle,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('FindFirstVolumeMountPointW', windll['KERNEL32.dll']), ((1, 'lpszRootPathName'),(1, 'lpszVolumeMountPoint'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextVolumeMountPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeMointPointHandle,win32more.Foundation.PSTR,UInt32)(('FindNextVolumeMountPointA', windll['KERNEL32.dll']), ((1, 'hFindVolumeMountPoint'),(1, 'lpszVolumeMountPoint'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindNextVolumeMountPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeMointPointHandle,win32more.Foundation.PWSTR,UInt32)(('FindNextVolumeMountPointW', windll['KERNEL32.dll']), ((1, 'hFindVolumeMountPoint'),(1, 'lpszVolumeMountPoint'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_FindVolumeMountPointClose():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Storage.FileSystem.FindVolumeMointPointHandle)(('FindVolumeMountPointClose', windll['KERNEL32.dll']), ((1, 'hFindVolumeMountPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVolumeMountPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR)(('SetVolumeMountPointA', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),(1, 'lpszVolumeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetVolumeMountPointW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(('SetVolumeMountPointW', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),(1, 'lpszVolumeName'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeleteVolumeMountPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR)(('DeleteVolumeMountPointA', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumeNameForVolumeMountPointA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetVolumeNameForVolumeMountPointA', windll['KERNEL32.dll']), ((1, 'lpszVolumeMountPoint'),(1, 'lpszVolumeName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumePathNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32)(('GetVolumePathNameA', windll['KERNEL32.dll']), ((1, 'lpszFileName'),(1, 'lpszVolumePathName'),(1, 'cchBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetVolumePathNamesForVolumeNameA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PSTR,win32more.Foundation.PSTR,UInt32,POINTER(UInt32))(('GetVolumePathNamesForVolumeNameA', windll['KERNEL32.dll']), ((1, 'lpszVolumeName'),(1, 'lpszVolumePathNames'),(1, 'cchBufferLength'),(1, 'lpcchReturnLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_GetFileInformationByHandleEx():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.FILE_INFO_BY_HANDLE_CLASS,c_void_p,UInt32)(('GetFileInformationByHandleEx', windll['KERNEL32.dll']), ((1, 'hFile'),(1, 'FileInformationClass'),(1, 'lpFileInformation'),(1, 'dwBufferSize'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_OpenFileById():
    try:
        return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,POINTER(win32more.Storage.FileSystem.FILE_ID_DESCRIPTOR_head),win32more.Storage.FileSystem.FILE_ACCESS_FLAGS,win32more.Storage.FileSystem.FILE_SHARE_MODE,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),win32more.Storage.FileSystem.FILE_FLAGS_AND_ATTRIBUTES)(('OpenFileById', windll['KERNEL32.dll']), ((1, 'hVolumeHint'),(1, 'lpFileId'),(1, 'dwDesiredAccess'),(1, 'dwShareMode'),(1, 'lpSecurityAttributes'),(1, 'dwFlagsAndAttributes'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSymbolicLinkA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.SYMBOLIC_LINK_FLAGS)(('CreateSymbolicLinkA', windll['KERNEL32.dll']), ((1, 'lpSymlinkFileName'),(1, 'lpTargetFileName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSymbolicLinkW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.SYMBOLIC_LINK_FLAGS)(('CreateSymbolicLinkW', windll['KERNEL32.dll']), ((1, 'lpSymlinkFileName'),(1, 'lpTargetFileName'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSymbolicLinkTransactedA():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.FileSystem.SYMBOLIC_LINK_FLAGS,win32more.Foundation.HANDLE)(('CreateSymbolicLinkTransactedA', windll['KERNEL32.dll']), ((1, 'lpSymlinkFileName'),(1, 'lpTargetFileName'),(1, 'dwFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_CreateSymbolicLinkTransactedW():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOLEAN,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.SYMBOLIC_LINK_FLAGS,win32more.Foundation.HANDLE)(('CreateSymbolicLinkTransactedW', windll['KERNEL32.dll']), ((1, 'lpSymlinkFileName'),(1, 'lpTargetFileName'),(1, 'dwFlags'),(1, 'hTransaction'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_NtCreateFile():
    try:
        return WINFUNCTYPE(win32more.Foundation.NTSTATUS,POINTER(win32more.Foundation.HANDLE),UInt32,POINTER(win32more.System.WindowsProgramming.OBJECT_ATTRIBUTES_head),POINTER(win32more.System.WindowsProgramming.IO_STATUS_BLOCK_head),POINTER(win32more.Foundation.LARGE_INTEGER_head),UInt32,win32more.Storage.FileSystem.FILE_SHARE_MODE,win32more.Storage.FileSystem.NT_CREATE_FILE_DISPOSITION,UInt32,c_void_p,UInt32)(('NtCreateFile', windll['ntdll.dll']), ((1, 'FileHandle'),(1, 'DesiredAccess'),(1, 'ObjectAttributes'),(1, 'IoStatusBlock'),(1, 'AllocationSize'),(1, 'FileAttributes'),(1, 'ShareAccess'),(1, 'CreateDisposition'),(1, 'CreateOptions'),(1, 'EaBuffer'),(1, 'EaLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_BY_HANDLE_FILE_INFORMATION_head():
    class BY_HANDLE_FILE_INFORMATION(Structure):
        pass
    return BY_HANDLE_FILE_INFORMATION
def _define_BY_HANDLE_FILE_INFORMATION():
    BY_HANDLE_FILE_INFORMATION = win32more.Storage.FileSystem.BY_HANDLE_FILE_INFORMATION_head
    BY_HANDLE_FILE_INFORMATION._fields_ = [
        ('dwFileAttributes', UInt32),
        ('ftCreationTime', win32more.Foundation.FILETIME),
        ('ftLastAccessTime', win32more.Foundation.FILETIME),
        ('ftLastWriteTime', win32more.Foundation.FILETIME),
        ('dwVolumeSerialNumber', UInt32),
        ('nFileSizeHigh', UInt32),
        ('nFileSizeLow', UInt32),
        ('nNumberOfLinks', UInt32),
        ('nFileIndexHigh', UInt32),
        ('nFileIndexLow', UInt32),
    ]
    return BY_HANDLE_FILE_INFORMATION
def _define_CACHE_ACCESS_CHECK():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Security.PSECURITY_DESCRIPTOR,win32more.Foundation.HANDLE,UInt32,POINTER(win32more.Security.GENERIC_MAPPING_head),POINTER(win32more.Security.PRIVILEGE_SET_head),POINTER(UInt32),POINTER(UInt32),POINTER(Int32))
def _define_CACHE_DESTROY_CALLBACK():
    return WINFUNCTYPE(Void,UInt32,c_char_p_no)
def _define_CACHE_KEY_COMPARE():
    return WINFUNCTYPE(Int32,UInt32,c_char_p_no,UInt32,c_char_p_no)
def _define_CACHE_KEY_HASH():
    return WINFUNCTYPE(UInt32,c_char_p_no,UInt32)
def _define_CACHE_READ_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,c_char_p_no,c_void_p)
def _define_CLAIMMEDIALABEL():
    return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,POINTER(win32more.Storage.FileSystem.MediaLabelInfo_head))
def _define_CLAIMMEDIALABELEX():
    return WINFUNCTYPE(UInt32,c_char_p_no,UInt32,POINTER(win32more.Storage.FileSystem.MediaLabelInfo_head),POINTER(Guid))
def _define_CLFS_BLOCK_ALLOCATION():
    return WINFUNCTYPE(c_void_p,UInt32,c_void_p)
def _define_CLFS_BLOCK_DEALLOCATION():
    return WINFUNCTYPE(Void,c_void_p,c_void_p)
CLFS_CONTEXT_MODE = Int32
CLFS_CONTEXT_MODE_ClfsContextNone = 0
CLFS_CONTEXT_MODE_ClfsContextUndoNext = 1
CLFS_CONTEXT_MODE_ClfsContextPrevious = 2
CLFS_CONTEXT_MODE_ClfsContextForward = 3
CLFS_FLAG = UInt32
CLFS_FLAG_FORCE_APPEND = 1
CLFS_FLAG_FORCE_FLUSH = 2
CLFS_FLAG_NO_FLAGS = 0
CLFS_FLAG_USE_RESERVATION = 4
CLFS_IOSTATS_CLASS = Int32
CLFS_IOSTATS_CLASS_ClfsIoStatsDefault = 0
CLFS_IOSTATS_CLASS_ClfsIoStatsMax = 65535
CLFS_LOG_ARCHIVE_MODE = Int32
CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveEnabled = 1
CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveDisabled = 2
def _define_CLFS_LOG_NAME_INFORMATION_head():
    class CLFS_LOG_NAME_INFORMATION(Structure):
        pass
    return CLFS_LOG_NAME_INFORMATION
def _define_CLFS_LOG_NAME_INFORMATION():
    CLFS_LOG_NAME_INFORMATION = win32more.Storage.FileSystem.CLFS_LOG_NAME_INFORMATION_head
    CLFS_LOG_NAME_INFORMATION._fields_ = [
        ('NameLengthInBytes', UInt16),
        ('Name', Char * 1),
    ]
    return CLFS_LOG_NAME_INFORMATION
def _define_CLFS_MGMT_NOTIFICATION_head():
    class CLFS_MGMT_NOTIFICATION(Structure):
        pass
    return CLFS_MGMT_NOTIFICATION
def _define_CLFS_MGMT_NOTIFICATION():
    CLFS_MGMT_NOTIFICATION = win32more.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_head
    CLFS_MGMT_NOTIFICATION._fields_ = [
        ('Notification', win32more.Storage.FileSystem.CLFS_MGMT_NOTIFICATION_TYPE),
        ('Lsn', win32more.Storage.FileSystem.CLS_LSN),
        ('LogIsPinned', UInt16),
    ]
    return CLFS_MGMT_NOTIFICATION
CLFS_MGMT_NOTIFICATION_TYPE = Int32
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtAdvanceTailNotification = 0
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogFullHandlerNotification = 1
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogUnpinnedNotification = 2
CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogWriteNotification = 3
def _define_CLFS_MGMT_POLICY_head():
    class CLFS_MGMT_POLICY(Structure):
        pass
    return CLFS_MGMT_POLICY
def _define_CLFS_MGMT_POLICY():
    CLFS_MGMT_POLICY = win32more.Storage.FileSystem.CLFS_MGMT_POLICY_head
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union(Union):
        pass
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__MaximumSize_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__MaximumSize_e__Struct._fields_ = [
        ('Containers', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__MinimumSize_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__MinimumSize_e__Struct._fields_ = [
        ('Containers', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSize_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSize_e__Struct._fields_ = [
        ('SizeInBytes', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__GrowthRate_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__GrowthRate_e__Struct._fields_ = [
        ('AbsoluteGrowthInContainers', UInt32),
        ('RelativeGrowthPercentage', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__LogTail_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__LogTail_e__Struct._fields_ = [
        ('MinimumAvailablePercentage', UInt32),
        ('MinimumAvailableContainers', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoShrink_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoShrink_e__Struct._fields_ = [
        ('Percentage', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoGrow_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoGrow_e__Struct._fields_ = [
        ('Enabled', UInt32),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerPrefix_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerPrefix_e__Struct._fields_ = [
        ('PrefixLengthInBytes', UInt16),
        ('PrefixString', Char * 1),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSuffix_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSuffix_e__Struct._fields_ = [
        ('NextContainerSuffix', UInt64),
    ]
    class CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerExtension_e__Struct(Structure):
        pass
    CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerExtension_e__Struct._fields_ = [
        ('ExtensionLengthInBytes', UInt16),
        ('ExtensionString', Char * 1),
    ]
    CLFS_MGMT_POLICY__PolicyParameters_e__Union._fields_ = [
        ('MaximumSize', CLFS_MGMT_POLICY__PolicyParameters_e__Union__MaximumSize_e__Struct),
        ('MinimumSize', CLFS_MGMT_POLICY__PolicyParameters_e__Union__MinimumSize_e__Struct),
        ('NewContainerSize', CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSize_e__Struct),
        ('GrowthRate', CLFS_MGMT_POLICY__PolicyParameters_e__Union__GrowthRate_e__Struct),
        ('LogTail', CLFS_MGMT_POLICY__PolicyParameters_e__Union__LogTail_e__Struct),
        ('AutoShrink', CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoShrink_e__Struct),
        ('AutoGrow', CLFS_MGMT_POLICY__PolicyParameters_e__Union__AutoGrow_e__Struct),
        ('NewContainerPrefix', CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerPrefix_e__Struct),
        ('NewContainerSuffix', CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerSuffix_e__Struct),
        ('NewContainerExtension', CLFS_MGMT_POLICY__PolicyParameters_e__Union__NewContainerExtension_e__Struct),
    ]
    CLFS_MGMT_POLICY._fields_ = [
        ('Version', UInt32),
        ('LengthInBytes', UInt32),
        ('PolicyFlags', UInt32),
        ('PolicyType', win32more.Storage.FileSystem.CLFS_MGMT_POLICY_TYPE),
        ('PolicyParameters', CLFS_MGMT_POLICY__PolicyParameters_e__Union),
    ]
    return CLFS_MGMT_POLICY
CLFS_MGMT_POLICY_TYPE = Int32
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMaximumSize = 0
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMinimumSize = 1
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSize = 2
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyGrowthRate = 3
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyLogTail = 4
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoShrink = 5
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoGrow = 6
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerPrefix = 7
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSuffix = 8
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerExtension = 9
CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyInvalid = 10
def _define_CLFS_NODE_ID_head():
    class CLFS_NODE_ID(Structure):
        pass
    return CLFS_NODE_ID
def _define_CLFS_NODE_ID():
    CLFS_NODE_ID = win32more.Storage.FileSystem.CLFS_NODE_ID_head
    CLFS_NODE_ID._fields_ = [
        ('cType', UInt32),
        ('cbNode', UInt32),
    ]
    return CLFS_NODE_ID
def _define_CLFS_PHYSICAL_LSN_INFORMATION_head():
    class CLFS_PHYSICAL_LSN_INFORMATION(Structure):
        pass
    return CLFS_PHYSICAL_LSN_INFORMATION
def _define_CLFS_PHYSICAL_LSN_INFORMATION():
    CLFS_PHYSICAL_LSN_INFORMATION = win32more.Storage.FileSystem.CLFS_PHYSICAL_LSN_INFORMATION_head
    CLFS_PHYSICAL_LSN_INFORMATION._fields_ = [
        ('StreamIdentifier', Byte),
        ('VirtualLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('PhysicalLsn', win32more.Storage.FileSystem.CLS_LSN),
    ]
    return CLFS_PHYSICAL_LSN_INFORMATION
def _define_CLFS_STREAM_ID_INFORMATION_head():
    class CLFS_STREAM_ID_INFORMATION(Structure):
        pass
    return CLFS_STREAM_ID_INFORMATION
def _define_CLFS_STREAM_ID_INFORMATION():
    CLFS_STREAM_ID_INFORMATION = win32more.Storage.FileSystem.CLFS_STREAM_ID_INFORMATION_head
    CLFS_STREAM_ID_INFORMATION._fields_ = [
        ('StreamIdentifier', Byte),
    ]
    return CLFS_STREAM_ID_INFORMATION
def _define_CLS_ARCHIVE_DESCRIPTOR_head():
    class CLS_ARCHIVE_DESCRIPTOR(Structure):
        pass
    return CLS_ARCHIVE_DESCRIPTOR
def _define_CLS_ARCHIVE_DESCRIPTOR():
    CLS_ARCHIVE_DESCRIPTOR = win32more.Storage.FileSystem.CLS_ARCHIVE_DESCRIPTOR_head
    CLS_ARCHIVE_DESCRIPTOR._fields_ = [
        ('coffLow', UInt64),
        ('coffHigh', UInt64),
        ('infoContainer', win32more.Storage.FileSystem.CLS_CONTAINER_INFORMATION),
    ]
    return CLS_ARCHIVE_DESCRIPTOR
def _define_CLS_CONTAINER_INFORMATION_head():
    class CLS_CONTAINER_INFORMATION(Structure):
        pass
    return CLS_CONTAINER_INFORMATION
def _define_CLS_CONTAINER_INFORMATION():
    CLS_CONTAINER_INFORMATION = win32more.Storage.FileSystem.CLS_CONTAINER_INFORMATION_head
    CLS_CONTAINER_INFORMATION._fields_ = [
        ('FileAttributes', UInt32),
        ('CreationTime', UInt64),
        ('LastAccessTime', UInt64),
        ('LastWriteTime', UInt64),
        ('ContainerSize', Int64),
        ('FileNameActualLength', UInt32),
        ('FileNameLength', UInt32),
        ('FileName', Char * 256),
        ('State', UInt32),
        ('PhysicalContainerId', UInt32),
        ('LogicalContainerId', UInt32),
    ]
    return CLS_CONTAINER_INFORMATION
CLS_CONTEXT_MODE = Int32
CLS_CONTEXT_MODE_ClsContextNone = 0
CLS_CONTEXT_MODE_ClsContextUndoNext = 1
CLS_CONTEXT_MODE_ClsContextPrevious = 2
CLS_CONTEXT_MODE_ClsContextForward = 3
def _define_CLS_INFORMATION_head():
    class CLS_INFORMATION(Structure):
        pass
    return CLS_INFORMATION
def _define_CLS_INFORMATION():
    CLS_INFORMATION = win32more.Storage.FileSystem.CLS_INFORMATION_head
    CLS_INFORMATION._fields_ = [
        ('TotalAvailable', Int64),
        ('CurrentAvailable', Int64),
        ('TotalReservation', Int64),
        ('BaseFileSize', UInt64),
        ('ContainerSize', UInt64),
        ('TotalContainers', UInt32),
        ('FreeContainers', UInt32),
        ('TotalClients', UInt32),
        ('Attributes', UInt32),
        ('FlushThreshold', UInt32),
        ('SectorSize', UInt32),
        ('MinArchiveTailLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('BaseLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('LastFlushedLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('LastLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('RestartLsn', win32more.Storage.FileSystem.CLS_LSN),
        ('Identity', Guid),
    ]
    return CLS_INFORMATION
def _define_CLS_IO_STATISTICS_head():
    class CLS_IO_STATISTICS(Structure):
        pass
    return CLS_IO_STATISTICS
def _define_CLS_IO_STATISTICS():
    CLS_IO_STATISTICS = win32more.Storage.FileSystem.CLS_IO_STATISTICS_head
    CLS_IO_STATISTICS._fields_ = [
        ('hdrIoStats', win32more.Storage.FileSystem.CLS_IO_STATISTICS_HEADER),
        ('cFlush', UInt64),
        ('cbFlush', UInt64),
        ('cMetaFlush', UInt64),
        ('cbMetaFlush', UInt64),
    ]
    return CLS_IO_STATISTICS
def _define_CLS_IO_STATISTICS_HEADER_head():
    class CLS_IO_STATISTICS_HEADER(Structure):
        pass
    return CLS_IO_STATISTICS_HEADER
def _define_CLS_IO_STATISTICS_HEADER():
    CLS_IO_STATISTICS_HEADER = win32more.Storage.FileSystem.CLS_IO_STATISTICS_HEADER_head
    CLS_IO_STATISTICS_HEADER._fields_ = [
        ('ubMajorVersion', Byte),
        ('ubMinorVersion', Byte),
        ('eStatsClass', win32more.Storage.FileSystem.CLFS_IOSTATS_CLASS),
        ('cbLength', UInt16),
        ('coffData', UInt32),
    ]
    return CLS_IO_STATISTICS_HEADER
CLS_IOSTATS_CLASS = Int32
CLS_IOSTATS_CLASS_ClsIoStatsDefault = 0
CLS_IOSTATS_CLASS_ClsIoStatsMax = 65535
CLS_LOG_INFORMATION_CLASS = Int32
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformation = 0
CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformationPhysical = 1
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalNameInformation = 2
CLS_LOG_INFORMATION_CLASS_ClfsLogStreamIdentifierInformation = 3
CLS_LOG_INFORMATION_CLASS_ClfsLogSystemMarkingInformation = 4
CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalLsnInformation = 5
def _define_CLS_LSN_head():
    class CLS_LSN(Structure):
        pass
    return CLS_LSN
def _define_CLS_LSN():
    CLS_LSN = win32more.Storage.FileSystem.CLS_LSN_head
    CLS_LSN._fields_ = [
        ('Internal', UInt64),
    ]
    return CLS_LSN
def _define_CLS_SCAN_CONTEXT_head():
    class CLS_SCAN_CONTEXT(Structure):
        pass
    return CLS_SCAN_CONTEXT
def _define_CLS_SCAN_CONTEXT():
    CLS_SCAN_CONTEXT = win32more.Storage.FileSystem.CLS_SCAN_CONTEXT_head
    CLS_SCAN_CONTEXT._fields_ = [
        ('cidNode', win32more.Storage.FileSystem.CLFS_NODE_ID),
        ('hLog', win32more.Foundation.HANDLE),
        ('cIndex', UInt32),
        ('cContainers', UInt32),
        ('cContainersReturned', UInt32),
        ('eScanMode', Byte),
        ('pinfoContainer', POINTER(win32more.Storage.FileSystem.CLS_CONTAINER_INFORMATION_head)),
    ]
    return CLS_SCAN_CONTEXT
def _define_CLS_WRITE_ENTRY_head():
    class CLS_WRITE_ENTRY(Structure):
        pass
    return CLS_WRITE_ENTRY
def _define_CLS_WRITE_ENTRY():
    CLS_WRITE_ENTRY = win32more.Storage.FileSystem.CLS_WRITE_ENTRY_head
    CLS_WRITE_ENTRY._fields_ = [
        ('Buffer', c_void_p),
        ('ByteLength', UInt32),
    ]
    return CLS_WRITE_ENTRY
COMPRESSION_FORMAT = UInt16
COMPRESSION_FORMAT_NONE = 0
COMPRESSION_FORMAT_DEFAULT = 1
COMPRESSION_FORMAT_LZNT1 = 2
COMPRESSION_FORMAT_XPRESS = 3
COMPRESSION_FORMAT_XPRESS_HUFF = 4
COMPRESSION_FORMAT_XP10 = 5
def _define_CONNECTION_INFO_0_head():
    class CONNECTION_INFO_0(Structure):
        pass
    return CONNECTION_INFO_0
def _define_CONNECTION_INFO_0():
    CONNECTION_INFO_0 = win32more.Storage.FileSystem.CONNECTION_INFO_0_head
    CONNECTION_INFO_0._fields_ = [
        ('coni0_id', UInt32),
    ]
    return CONNECTION_INFO_0
def _define_CONNECTION_INFO_1_head():
    class CONNECTION_INFO_1(Structure):
        pass
    return CONNECTION_INFO_1
def _define_CONNECTION_INFO_1():
    CONNECTION_INFO_1 = win32more.Storage.FileSystem.CONNECTION_INFO_1_head
    CONNECTION_INFO_1._fields_ = [
        ('coni1_id', UInt32),
        ('coni1_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('coni1_num_opens', UInt32),
        ('coni1_num_users', UInt32),
        ('coni1_time', UInt32),
        ('coni1_username', win32more.Foundation.PWSTR),
        ('coni1_netname', win32more.Foundation.PWSTR),
    ]
    return CONNECTION_INFO_1
COPYFILE2_COPY_PHASE = Int32
COPYFILE2_PHASE_NONE = 0
COPYFILE2_PHASE_PREPARE_SOURCE = 1
COPYFILE2_PHASE_PREPARE_DEST = 2
COPYFILE2_PHASE_READ_SOURCE = 3
COPYFILE2_PHASE_WRITE_DESTINATION = 4
COPYFILE2_PHASE_SERVER_COPY = 5
COPYFILE2_PHASE_NAMEGRAFT_COPY = 6
COPYFILE2_PHASE_MAX = 7
def _define_COPYFILE2_EXTENDED_PARAMETERS_head():
    class COPYFILE2_EXTENDED_PARAMETERS(Structure):
        pass
    return COPYFILE2_EXTENDED_PARAMETERS
def _define_COPYFILE2_EXTENDED_PARAMETERS():
    COPYFILE2_EXTENDED_PARAMETERS = win32more.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS_head
    COPYFILE2_EXTENDED_PARAMETERS._fields_ = [
        ('dwSize', UInt32),
        ('dwCopyFlags', UInt32),
        ('pfCancel', POINTER(win32more.Foundation.BOOL)),
        ('pProgressRoutine', win32more.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE),
        ('pvCallbackContext', c_void_p),
    ]
    return COPYFILE2_EXTENDED_PARAMETERS
def _define_COPYFILE2_EXTENDED_PARAMETERS_V2_head():
    class COPYFILE2_EXTENDED_PARAMETERS_V2(Structure):
        pass
    return COPYFILE2_EXTENDED_PARAMETERS_V2
def _define_COPYFILE2_EXTENDED_PARAMETERS_V2():
    COPYFILE2_EXTENDED_PARAMETERS_V2 = win32more.Storage.FileSystem.COPYFILE2_EXTENDED_PARAMETERS_V2_head
    COPYFILE2_EXTENDED_PARAMETERS_V2._fields_ = [
        ('dwSize', UInt32),
        ('dwCopyFlags', UInt32),
        ('pfCancel', POINTER(win32more.Foundation.BOOL)),
        ('pProgressRoutine', win32more.Storage.FileSystem.PCOPYFILE2_PROGRESS_ROUTINE),
        ('pvCallbackContext', c_void_p),
        ('dwCopyFlagsV2', UInt32),
        ('ioDesiredSize', UInt32),
        ('ioDesiredRate', UInt32),
        ('reserved', c_void_p * 8),
    ]
    return COPYFILE2_EXTENDED_PARAMETERS_V2
def _define_COPYFILE2_MESSAGE_head():
    class COPYFILE2_MESSAGE(Structure):
        pass
    return COPYFILE2_MESSAGE
def _define_COPYFILE2_MESSAGE():
    COPYFILE2_MESSAGE = win32more.Storage.FileSystem.COPYFILE2_MESSAGE_head
    class COPYFILE2_MESSAGE__Info_e__Union(Union):
        pass
    class COPYFILE2_MESSAGE__Info_e__Union__ChunkStarted_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__ChunkStarted_e__Struct._fields_ = [
        ('dwStreamNumber', UInt32),
        ('dwReserved', UInt32),
        ('hSourceFile', win32more.Foundation.HANDLE),
        ('hDestinationFile', win32more.Foundation.HANDLE),
        ('uliChunkNumber', win32more.Foundation.ULARGE_INTEGER),
        ('uliChunkSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalFileSize', win32more.Foundation.ULARGE_INTEGER),
    ]
    class COPYFILE2_MESSAGE__Info_e__Union__ChunkFinished_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__ChunkFinished_e__Struct._fields_ = [
        ('dwStreamNumber', UInt32),
        ('dwFlags', UInt32),
        ('hSourceFile', win32more.Foundation.HANDLE),
        ('hDestinationFile', win32more.Foundation.HANDLE),
        ('uliChunkNumber', win32more.Foundation.ULARGE_INTEGER),
        ('uliChunkSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalFileSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
    ]
    class COPYFILE2_MESSAGE__Info_e__Union__StreamStarted_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__StreamStarted_e__Struct._fields_ = [
        ('dwStreamNumber', UInt32),
        ('dwReserved', UInt32),
        ('hSourceFile', win32more.Foundation.HANDLE),
        ('hDestinationFile', win32more.Foundation.HANDLE),
        ('uliStreamSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalFileSize', win32more.Foundation.ULARGE_INTEGER),
    ]
    class COPYFILE2_MESSAGE__Info_e__Union__StreamFinished_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__StreamFinished_e__Struct._fields_ = [
        ('dwStreamNumber', UInt32),
        ('dwReserved', UInt32),
        ('hSourceFile', win32more.Foundation.HANDLE),
        ('hDestinationFile', win32more.Foundation.HANDLE),
        ('uliStreamSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalFileSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
    ]
    class COPYFILE2_MESSAGE__Info_e__Union__PollContinue_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__PollContinue_e__Struct._fields_ = [
        ('dwReserved', UInt32),
    ]
    class COPYFILE2_MESSAGE__Info_e__Union__Error_e__Struct(Structure):
        pass
    COPYFILE2_MESSAGE__Info_e__Union__Error_e__Struct._fields_ = [
        ('CopyPhase', win32more.Storage.FileSystem.COPYFILE2_COPY_PHASE),
        ('dwStreamNumber', UInt32),
        ('hrFailure', win32more.Foundation.HRESULT),
        ('dwReserved', UInt32),
        ('uliChunkNumber', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliStreamBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalFileSize', win32more.Foundation.ULARGE_INTEGER),
        ('uliTotalBytesTransferred', win32more.Foundation.ULARGE_INTEGER),
    ]
    COPYFILE2_MESSAGE__Info_e__Union._fields_ = [
        ('ChunkStarted', COPYFILE2_MESSAGE__Info_e__Union__ChunkStarted_e__Struct),
        ('ChunkFinished', COPYFILE2_MESSAGE__Info_e__Union__ChunkFinished_e__Struct),
        ('StreamStarted', COPYFILE2_MESSAGE__Info_e__Union__StreamStarted_e__Struct),
        ('StreamFinished', COPYFILE2_MESSAGE__Info_e__Union__StreamFinished_e__Struct),
        ('PollContinue', COPYFILE2_MESSAGE__Info_e__Union__PollContinue_e__Struct),
        ('Error', COPYFILE2_MESSAGE__Info_e__Union__Error_e__Struct),
    ]
    COPYFILE2_MESSAGE._fields_ = [
        ('Type', win32more.Storage.FileSystem.COPYFILE2_MESSAGE_TYPE),
        ('dwPadding', UInt32),
        ('Info', COPYFILE2_MESSAGE__Info_e__Union),
    ]
    return COPYFILE2_MESSAGE
COPYFILE2_MESSAGE_ACTION = Int32
COPYFILE2_PROGRESS_CONTINUE = 0
COPYFILE2_PROGRESS_CANCEL = 1
COPYFILE2_PROGRESS_STOP = 2
COPYFILE2_PROGRESS_QUIET = 3
COPYFILE2_PROGRESS_PAUSE = 4
COPYFILE2_MESSAGE_TYPE = Int32
COPYFILE2_CALLBACK_NONE = 0
COPYFILE2_CALLBACK_CHUNK_STARTED = 1
COPYFILE2_CALLBACK_CHUNK_FINISHED = 2
COPYFILE2_CALLBACK_STREAM_STARTED = 3
COPYFILE2_CALLBACK_STREAM_FINISHED = 4
COPYFILE2_CALLBACK_POLL_CONTINUE = 5
COPYFILE2_CALLBACK_ERROR = 6
COPYFILE2_CALLBACK_MAX = 7
CREATE_TAPE_PARTITION_METHOD = Int32
TAPE_FIXED_PARTITIONS = 0
TAPE_INITIATOR_PARTITIONS = 2
TAPE_SELECT_PARTITIONS = 1
def _define_CREATEFILE2_EXTENDED_PARAMETERS_head():
    class CREATEFILE2_EXTENDED_PARAMETERS(Structure):
        pass
    return CREATEFILE2_EXTENDED_PARAMETERS
def _define_CREATEFILE2_EXTENDED_PARAMETERS():
    CREATEFILE2_EXTENDED_PARAMETERS = win32more.Storage.FileSystem.CREATEFILE2_EXTENDED_PARAMETERS_head
    CREATEFILE2_EXTENDED_PARAMETERS._fields_ = [
        ('dwSize', UInt32),
        ('dwFileAttributes', UInt32),
        ('dwFileFlags', UInt32),
        ('dwSecurityQosFlags', UInt32),
        ('lpSecurityAttributes', POINTER(win32more.Security.SECURITY_ATTRIBUTES_head)),
        ('hTemplateFile', win32more.Foundation.HANDLE),
    ]
    return CREATEFILE2_EXTENDED_PARAMETERS
DEFINE_DOS_DEVICE_FLAGS = UInt32
DDD_RAW_TARGET_PATH = 1
DDD_REMOVE_DEFINITION = 2
DDD_EXACT_MATCH_ON_REMOVE = 4
DDD_NO_BROADCAST_SYSTEM = 8
DDD_LUID_BROADCAST_DRIVE = 16
def _define_DISK_SPACE_INFORMATION_head():
    class DISK_SPACE_INFORMATION(Structure):
        pass
    return DISK_SPACE_INFORMATION
def _define_DISK_SPACE_INFORMATION():
    DISK_SPACE_INFORMATION = win32more.Storage.FileSystem.DISK_SPACE_INFORMATION_head
    DISK_SPACE_INFORMATION._fields_ = [
        ('ActualTotalAllocationUnits', UInt64),
        ('ActualAvailableAllocationUnits', UInt64),
        ('ActualPoolUnavailableAllocationUnits', UInt64),
        ('CallerTotalAllocationUnits', UInt64),
        ('CallerAvailableAllocationUnits', UInt64),
        ('CallerPoolUnavailableAllocationUnits', UInt64),
        ('UsedAllocationUnits', UInt64),
        ('TotalReservedAllocationUnits', UInt64),
        ('VolumeStorageReserveAllocationUnits', UInt64),
        ('AvailableCommittedAllocationUnits', UInt64),
        ('PoolAvailableAllocationUnits', UInt64),
        ('SectorsPerAllocationUnit', UInt32),
        ('BytesPerSector', UInt32),
    ]
    return DISK_SPACE_INFORMATION
def _define_DISKQUOTA_USER_INFORMATION_head():
    class DISKQUOTA_USER_INFORMATION(Structure):
        pass
    return DISKQUOTA_USER_INFORMATION
def _define_DISKQUOTA_USER_INFORMATION():
    DISKQUOTA_USER_INFORMATION = win32more.Storage.FileSystem.DISKQUOTA_USER_INFORMATION_head
    DISKQUOTA_USER_INFORMATION._fields_ = [
        ('QuotaUsed', Int64),
        ('QuotaThreshold', Int64),
        ('QuotaLimit', Int64),
    ]
    return DISKQUOTA_USER_INFORMATION
DISKQUOTA_USERNAME_RESOLVE = UInt32
DISKQUOTA_USERNAME_RESOLVE_ASYNC = 2
DISKQUOTA_USERNAME_RESOLVE_NONE = 0
DISKQUOTA_USERNAME_RESOLVE_SYNC = 1
def _define_EFS_CERTIFICATE_BLOB_head():
    class EFS_CERTIFICATE_BLOB(Structure):
        pass
    return EFS_CERTIFICATE_BLOB
def _define_EFS_CERTIFICATE_BLOB():
    EFS_CERTIFICATE_BLOB = win32more.Storage.FileSystem.EFS_CERTIFICATE_BLOB_head
    EFS_CERTIFICATE_BLOB._fields_ = [
        ('dwCertEncodingType', UInt32),
        ('cbData', UInt32),
        ('pbData', c_char_p_no),
    ]
    return EFS_CERTIFICATE_BLOB
def _define_EFS_COMPATIBILITY_INFO_head():
    class EFS_COMPATIBILITY_INFO(Structure):
        pass
    return EFS_COMPATIBILITY_INFO
def _define_EFS_COMPATIBILITY_INFO():
    EFS_COMPATIBILITY_INFO = win32more.Storage.FileSystem.EFS_COMPATIBILITY_INFO_head
    EFS_COMPATIBILITY_INFO._fields_ = [
        ('EfsVersion', UInt32),
    ]
    return EFS_COMPATIBILITY_INFO
def _define_EFS_DECRYPTION_STATUS_INFO_head():
    class EFS_DECRYPTION_STATUS_INFO(Structure):
        pass
    return EFS_DECRYPTION_STATUS_INFO
def _define_EFS_DECRYPTION_STATUS_INFO():
    EFS_DECRYPTION_STATUS_INFO = win32more.Storage.FileSystem.EFS_DECRYPTION_STATUS_INFO_head
    EFS_DECRYPTION_STATUS_INFO._fields_ = [
        ('dwDecryptionError', UInt32),
        ('dwHashOffset', UInt32),
        ('cbHash', UInt32),
    ]
    return EFS_DECRYPTION_STATUS_INFO
def _define_EFS_ENCRYPTION_STATUS_INFO_head():
    class EFS_ENCRYPTION_STATUS_INFO(Structure):
        pass
    return EFS_ENCRYPTION_STATUS_INFO
def _define_EFS_ENCRYPTION_STATUS_INFO():
    EFS_ENCRYPTION_STATUS_INFO = win32more.Storage.FileSystem.EFS_ENCRYPTION_STATUS_INFO_head
    EFS_ENCRYPTION_STATUS_INFO._fields_ = [
        ('bHasCurrentKey', win32more.Foundation.BOOL),
        ('dwEncryptionError', UInt32),
    ]
    return EFS_ENCRYPTION_STATUS_INFO
def _define_EFS_HASH_BLOB_head():
    class EFS_HASH_BLOB(Structure):
        pass
    return EFS_HASH_BLOB
def _define_EFS_HASH_BLOB():
    EFS_HASH_BLOB = win32more.Storage.FileSystem.EFS_HASH_BLOB_head
    EFS_HASH_BLOB._fields_ = [
        ('cbData', UInt32),
        ('pbData', c_char_p_no),
    ]
    return EFS_HASH_BLOB
def _define_EFS_KEY_INFO_head():
    class EFS_KEY_INFO(Structure):
        pass
    return EFS_KEY_INFO
def _define_EFS_KEY_INFO():
    EFS_KEY_INFO = win32more.Storage.FileSystem.EFS_KEY_INFO_head
    EFS_KEY_INFO._fields_ = [
        ('dwVersion', UInt32),
        ('Entropy', UInt32),
        ('Algorithm', UInt32),
        ('KeyLength', UInt32),
    ]
    return EFS_KEY_INFO
def _define_EFS_PIN_BLOB_head():
    class EFS_PIN_BLOB(Structure):
        pass
    return EFS_PIN_BLOB
def _define_EFS_PIN_BLOB():
    EFS_PIN_BLOB = win32more.Storage.FileSystem.EFS_PIN_BLOB_head
    EFS_PIN_BLOB._fields_ = [
        ('cbPadding', UInt32),
        ('cbData', UInt32),
        ('pbData', c_char_p_no),
    ]
    return EFS_PIN_BLOB
def _define_EFS_RPC_BLOB_head():
    class EFS_RPC_BLOB(Structure):
        pass
    return EFS_RPC_BLOB
def _define_EFS_RPC_BLOB():
    EFS_RPC_BLOB = win32more.Storage.FileSystem.EFS_RPC_BLOB_head
    EFS_RPC_BLOB._fields_ = [
        ('cbData', UInt32),
        ('pbData', c_char_p_no),
    ]
    return EFS_RPC_BLOB
def _define_EFS_VERSION_INFO_head():
    class EFS_VERSION_INFO(Structure):
        pass
    return EFS_VERSION_INFO
def _define_EFS_VERSION_INFO():
    EFS_VERSION_INFO = win32more.Storage.FileSystem.EFS_VERSION_INFO_head
    EFS_VERSION_INFO._fields_ = [
        ('EfsVersion', UInt32),
        ('SubVersion', UInt32),
    ]
    return EFS_VERSION_INFO
def _define_ENCRYPTED_FILE_METADATA_SIGNATURE_head():
    class ENCRYPTED_FILE_METADATA_SIGNATURE(Structure):
        pass
    return ENCRYPTED_FILE_METADATA_SIGNATURE
def _define_ENCRYPTED_FILE_METADATA_SIGNATURE():
    ENCRYPTED_FILE_METADATA_SIGNATURE = win32more.Storage.FileSystem.ENCRYPTED_FILE_METADATA_SIGNATURE_head
    ENCRYPTED_FILE_METADATA_SIGNATURE._fields_ = [
        ('dwEfsAccessType', UInt32),
        ('pCertificatesAdded', POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head)),
        ('pEncryptionCertificate', POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head)),
        ('pEfsStreamSignature', POINTER(win32more.Storage.FileSystem.EFS_RPC_BLOB_head)),
    ]
    return ENCRYPTED_FILE_METADATA_SIGNATURE
def _define_ENCRYPTION_CERTIFICATE_head():
    class ENCRYPTION_CERTIFICATE(Structure):
        pass
    return ENCRYPTION_CERTIFICATE
def _define_ENCRYPTION_CERTIFICATE():
    ENCRYPTION_CERTIFICATE = win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head
    ENCRYPTION_CERTIFICATE._fields_ = [
        ('cbTotalLength', UInt32),
        ('pUserSid', POINTER(win32more.Security.SID_head)),
        ('pCertBlob', POINTER(win32more.Storage.FileSystem.EFS_CERTIFICATE_BLOB_head)),
    ]
    return ENCRYPTION_CERTIFICATE
def _define_ENCRYPTION_CERTIFICATE_HASH_head():
    class ENCRYPTION_CERTIFICATE_HASH(Structure):
        pass
    return ENCRYPTION_CERTIFICATE_HASH
def _define_ENCRYPTION_CERTIFICATE_HASH():
    ENCRYPTION_CERTIFICATE_HASH = win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head
    ENCRYPTION_CERTIFICATE_HASH._fields_ = [
        ('cbTotalLength', UInt32),
        ('pUserSid', POINTER(win32more.Security.SID_head)),
        ('pHash', POINTER(win32more.Storage.FileSystem.EFS_HASH_BLOB_head)),
        ('lpDisplayInformation', win32more.Foundation.PWSTR),
    ]
    return ENCRYPTION_CERTIFICATE_HASH
def _define_ENCRYPTION_CERTIFICATE_HASH_LIST_head():
    class ENCRYPTION_CERTIFICATE_HASH_LIST(Structure):
        pass
    return ENCRYPTION_CERTIFICATE_HASH_LIST
def _define_ENCRYPTION_CERTIFICATE_HASH_LIST():
    ENCRYPTION_CERTIFICATE_HASH_LIST = win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_LIST_head
    ENCRYPTION_CERTIFICATE_HASH_LIST._fields_ = [
        ('nCert_Hash', UInt32),
        ('pUsers', POINTER(POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_HASH_head))),
    ]
    return ENCRYPTION_CERTIFICATE_HASH_LIST
def _define_ENCRYPTION_CERTIFICATE_LIST_head():
    class ENCRYPTION_CERTIFICATE_LIST(Structure):
        pass
    return ENCRYPTION_CERTIFICATE_LIST
def _define_ENCRYPTION_CERTIFICATE_LIST():
    ENCRYPTION_CERTIFICATE_LIST = win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_LIST_head
    ENCRYPTION_CERTIFICATE_LIST._fields_ = [
        ('nUsers', UInt32),
        ('pUsers', POINTER(POINTER(win32more.Storage.FileSystem.ENCRYPTION_CERTIFICATE_head))),
    ]
    return ENCRYPTION_CERTIFICATE_LIST
def _define_ENCRYPTION_PROTECTOR_head():
    class ENCRYPTION_PROTECTOR(Structure):
        pass
    return ENCRYPTION_PROTECTOR
def _define_ENCRYPTION_PROTECTOR():
    ENCRYPTION_PROTECTOR = win32more.Storage.FileSystem.ENCRYPTION_PROTECTOR_head
    ENCRYPTION_PROTECTOR._fields_ = [
        ('cbTotalLength', UInt32),
        ('pUserSid', POINTER(win32more.Security.SID_head)),
        ('lpProtectorDescriptor', win32more.Foundation.PWSTR),
    ]
    return ENCRYPTION_PROTECTOR
def _define_ENCRYPTION_PROTECTOR_LIST_head():
    class ENCRYPTION_PROTECTOR_LIST(Structure):
        pass
    return ENCRYPTION_PROTECTOR_LIST
def _define_ENCRYPTION_PROTECTOR_LIST():
    ENCRYPTION_PROTECTOR_LIST = win32more.Storage.FileSystem.ENCRYPTION_PROTECTOR_LIST_head
    ENCRYPTION_PROTECTOR_LIST._fields_ = [
        ('nProtectors', UInt32),
        ('pProtectors', POINTER(POINTER(win32more.Storage.FileSystem.ENCRYPTION_PROTECTOR_head))),
    ]
    return ENCRYPTION_PROTECTOR_LIST
ERASE_TAPE_TYPE = Int32
TAPE_ERASE_LONG = 1
TAPE_ERASE_SHORT = 0
def _define_FCACHE_CREATE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,POINTER(UInt32),POINTER(UInt32))
def _define_FCACHE_RICHCREATE_CALLBACK():
    return WINFUNCTYPE(win32more.Foundation.HANDLE,win32more.Foundation.PSTR,c_void_p,POINTER(UInt32),POINTER(UInt32),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Foundation.BOOL))
def _define_FH_OVERLAPPED_head():
    class FH_OVERLAPPED(Structure):
        pass
    return FH_OVERLAPPED
def _define_FH_OVERLAPPED():
    FH_OVERLAPPED = win32more.Storage.FileSystem.FH_OVERLAPPED_head
    FH_OVERLAPPED._fields_ = [
        ('Internal', UIntPtr),
        ('InternalHigh', UIntPtr),
        ('Offset', UInt32),
        ('OffsetHigh', UInt32),
        ('hEvent', win32more.Foundation.HANDLE),
        ('pfnCompletion', win32more.Storage.FileSystem.PFN_IO_COMPLETION),
        ('Reserved1', UIntPtr),
        ('Reserved2', UIntPtr),
        ('Reserved3', UIntPtr),
        ('Reserved4', UIntPtr),
    ]
    return FH_OVERLAPPED
FILE_ACCESS_FLAGS = UInt32
FILE_READ_DATA = 1
FILE_LIST_DIRECTORY = 1
FILE_WRITE_DATA = 2
FILE_ADD_FILE = 2
FILE_APPEND_DATA = 4
FILE_ADD_SUBDIRECTORY = 4
FILE_CREATE_PIPE_INSTANCE = 4
FILE_READ_EA = 8
FILE_WRITE_EA = 16
FILE_EXECUTE = 32
FILE_TRAVERSE = 32
FILE_DELETE_CHILD = 64
FILE_READ_ATTRIBUTES = 128
FILE_WRITE_ATTRIBUTES = 256
DELETE = 65536
READ_CONTROL = 131072
WRITE_DAC = 262144
WRITE_OWNER = 524288
SYNCHRONIZE = 1048576
STANDARD_RIGHTS_REQUIRED = 983040
STANDARD_RIGHTS_READ = 131072
STANDARD_RIGHTS_WRITE = 131072
STANDARD_RIGHTS_EXECUTE = 131072
STANDARD_RIGHTS_ALL = 2031616
SPECIFIC_RIGHTS_ALL = 65535
FILE_ALL_ACCESS = 2032127
FILE_GENERIC_READ = 1179785
FILE_GENERIC_WRITE = 1179926
FILE_GENERIC_EXECUTE = 1179808
FILE_ACTION = UInt32
FILE_ACTION_ADDED = 1
FILE_ACTION_REMOVED = 2
FILE_ACTION_MODIFIED = 3
FILE_ACTION_RENAMED_OLD_NAME = 4
FILE_ACTION_RENAMED_NEW_NAME = 5
def _define_FILE_ALIGNMENT_INFO_head():
    class FILE_ALIGNMENT_INFO(Structure):
        pass
    return FILE_ALIGNMENT_INFO
def _define_FILE_ALIGNMENT_INFO():
    FILE_ALIGNMENT_INFO = win32more.Storage.FileSystem.FILE_ALIGNMENT_INFO_head
    FILE_ALIGNMENT_INFO._fields_ = [
        ('AlignmentRequirement', UInt32),
    ]
    return FILE_ALIGNMENT_INFO
def _define_FILE_ALLOCATION_INFO_head():
    class FILE_ALLOCATION_INFO(Structure):
        pass
    return FILE_ALLOCATION_INFO
def _define_FILE_ALLOCATION_INFO():
    FILE_ALLOCATION_INFO = win32more.Storage.FileSystem.FILE_ALLOCATION_INFO_head
    FILE_ALLOCATION_INFO._fields_ = [
        ('AllocationSize', win32more.Foundation.LARGE_INTEGER),
    ]
    return FILE_ALLOCATION_INFO
def _define_FILE_ATTRIBUTE_TAG_INFO_head():
    class FILE_ATTRIBUTE_TAG_INFO(Structure):
        pass
    return FILE_ATTRIBUTE_TAG_INFO
def _define_FILE_ATTRIBUTE_TAG_INFO():
    FILE_ATTRIBUTE_TAG_INFO = win32more.Storage.FileSystem.FILE_ATTRIBUTE_TAG_INFO_head
    FILE_ATTRIBUTE_TAG_INFO._fields_ = [
        ('FileAttributes', UInt32),
        ('ReparseTag', UInt32),
    ]
    return FILE_ATTRIBUTE_TAG_INFO
def _define_FILE_BASIC_INFO_head():
    class FILE_BASIC_INFO(Structure):
        pass
    return FILE_BASIC_INFO
def _define_FILE_BASIC_INFO():
    FILE_BASIC_INFO = win32more.Storage.FileSystem.FILE_BASIC_INFO_head
    FILE_BASIC_INFO._fields_ = [
        ('CreationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastAccessTime', win32more.Foundation.LARGE_INTEGER),
        ('LastWriteTime', win32more.Foundation.LARGE_INTEGER),
        ('ChangeTime', win32more.Foundation.LARGE_INTEGER),
        ('FileAttributes', UInt32),
    ]
    return FILE_BASIC_INFO
def _define_FILE_COMPRESSION_INFO_head():
    class FILE_COMPRESSION_INFO(Structure):
        pass
    return FILE_COMPRESSION_INFO
def _define_FILE_COMPRESSION_INFO():
    FILE_COMPRESSION_INFO = win32more.Storage.FileSystem.FILE_COMPRESSION_INFO_head
    FILE_COMPRESSION_INFO._fields_ = [
        ('CompressedFileSize', win32more.Foundation.LARGE_INTEGER),
        ('CompressionFormat', win32more.Storage.FileSystem.COMPRESSION_FORMAT),
        ('CompressionUnitShift', Byte),
        ('ChunkShift', Byte),
        ('ClusterShift', Byte),
        ('Reserved', Byte * 3),
    ]
    return FILE_COMPRESSION_INFO
FILE_CREATION_DISPOSITION = UInt32
CREATE_NEW = 1
CREATE_ALWAYS = 2
OPEN_EXISTING = 3
OPEN_ALWAYS = 4
TRUNCATE_EXISTING = 5
FILE_DEVICE_TYPE = UInt32
FILE_DEVICE_CD_ROM = 2
FILE_DEVICE_DISK = 7
FILE_DEVICE_TAPE = 31
FILE_DEVICE_DVD = 51
def _define_FILE_DISPOSITION_INFO_head():
    class FILE_DISPOSITION_INFO(Structure):
        pass
    return FILE_DISPOSITION_INFO
def _define_FILE_DISPOSITION_INFO():
    FILE_DISPOSITION_INFO = win32more.Storage.FileSystem.FILE_DISPOSITION_INFO_head
    FILE_DISPOSITION_INFO._fields_ = [
        ('DeleteFile', win32more.Foundation.BOOLEAN),
    ]
    return FILE_DISPOSITION_INFO
def _define_FILE_END_OF_FILE_INFO_head():
    class FILE_END_OF_FILE_INFO(Structure):
        pass
    return FILE_END_OF_FILE_INFO
def _define_FILE_END_OF_FILE_INFO():
    FILE_END_OF_FILE_INFO = win32more.Storage.FileSystem.FILE_END_OF_FILE_INFO_head
    FILE_END_OF_FILE_INFO._fields_ = [
        ('EndOfFile', win32more.Foundation.LARGE_INTEGER),
    ]
    return FILE_END_OF_FILE_INFO
def _define_FILE_EXTENT_head():
    class FILE_EXTENT(Structure):
        pass
    return FILE_EXTENT
def _define_FILE_EXTENT():
    FILE_EXTENT = win32more.Storage.FileSystem.FILE_EXTENT_head
    FILE_EXTENT._fields_ = [
        ('VolumeOffset', UInt64),
        ('ExtentLength', UInt64),
    ]
    return FILE_EXTENT
FILE_FLAGS_AND_ATTRIBUTES = UInt32
FILE_ATTRIBUTE_READONLY = 1
FILE_ATTRIBUTE_HIDDEN = 2
FILE_ATTRIBUTE_SYSTEM = 4
FILE_ATTRIBUTE_DIRECTORY = 16
FILE_ATTRIBUTE_ARCHIVE = 32
FILE_ATTRIBUTE_DEVICE = 64
FILE_ATTRIBUTE_NORMAL = 128
FILE_ATTRIBUTE_TEMPORARY = 256
FILE_ATTRIBUTE_SPARSE_FILE = 512
FILE_ATTRIBUTE_REPARSE_POINT = 1024
FILE_ATTRIBUTE_COMPRESSED = 2048
FILE_ATTRIBUTE_OFFLINE = 4096
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 8192
FILE_ATTRIBUTE_ENCRYPTED = 16384
FILE_ATTRIBUTE_INTEGRITY_STREAM = 32768
FILE_ATTRIBUTE_VIRTUAL = 65536
FILE_ATTRIBUTE_NO_SCRUB_DATA = 131072
FILE_ATTRIBUTE_EA = 262144
FILE_ATTRIBUTE_PINNED = 524288
FILE_ATTRIBUTE_UNPINNED = 1048576
FILE_ATTRIBUTE_RECALL_ON_OPEN = 262144
FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 4194304
FILE_FLAG_WRITE_THROUGH = 2147483648
FILE_FLAG_OVERLAPPED = 1073741824
FILE_FLAG_NO_BUFFERING = 536870912
FILE_FLAG_RANDOM_ACCESS = 268435456
FILE_FLAG_SEQUENTIAL_SCAN = 134217728
FILE_FLAG_DELETE_ON_CLOSE = 67108864
FILE_FLAG_BACKUP_SEMANTICS = 33554432
FILE_FLAG_POSIX_SEMANTICS = 16777216
FILE_FLAG_SESSION_AWARE = 8388608
FILE_FLAG_OPEN_REPARSE_POINT = 2097152
FILE_FLAG_OPEN_NO_RECALL = 1048576
FILE_FLAG_FIRST_PIPE_INSTANCE = 524288
PIPE_ACCESS_DUPLEX = 3
PIPE_ACCESS_INBOUND = 1
PIPE_ACCESS_OUTBOUND = 2
SECURITY_ANONYMOUS = 0
SECURITY_IDENTIFICATION = 65536
SECURITY_IMPERSONATION = 131072
SECURITY_DELEGATION = 196608
SECURITY_CONTEXT_TRACKING = 262144
SECURITY_EFFECTIVE_ONLY = 524288
SECURITY_SQOS_PRESENT = 1048576
SECURITY_VALID_SQOS_FLAGS = 2031616
def _define_FILE_FULL_DIR_INFO_head():
    class FILE_FULL_DIR_INFO(Structure):
        pass
    return FILE_FULL_DIR_INFO
def _define_FILE_FULL_DIR_INFO():
    FILE_FULL_DIR_INFO = win32more.Storage.FileSystem.FILE_FULL_DIR_INFO_head
    FILE_FULL_DIR_INFO._fields_ = [
        ('NextEntryOffset', UInt32),
        ('FileIndex', UInt32),
        ('CreationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastAccessTime', win32more.Foundation.LARGE_INTEGER),
        ('LastWriteTime', win32more.Foundation.LARGE_INTEGER),
        ('ChangeTime', win32more.Foundation.LARGE_INTEGER),
        ('EndOfFile', win32more.Foundation.LARGE_INTEGER),
        ('AllocationSize', win32more.Foundation.LARGE_INTEGER),
        ('FileAttributes', UInt32),
        ('FileNameLength', UInt32),
        ('EaSize', UInt32),
        ('FileName', Char * 1),
    ]
    return FILE_FULL_DIR_INFO
def _define_FILE_ID_128_head():
    class FILE_ID_128(Structure):
        pass
    return FILE_ID_128
def _define_FILE_ID_128():
    FILE_ID_128 = win32more.Storage.FileSystem.FILE_ID_128_head
    FILE_ID_128._fields_ = [
        ('Identifier', Byte * 16),
    ]
    return FILE_ID_128
def _define_FILE_ID_BOTH_DIR_INFO_head():
    class FILE_ID_BOTH_DIR_INFO(Structure):
        pass
    return FILE_ID_BOTH_DIR_INFO
def _define_FILE_ID_BOTH_DIR_INFO():
    FILE_ID_BOTH_DIR_INFO = win32more.Storage.FileSystem.FILE_ID_BOTH_DIR_INFO_head
    FILE_ID_BOTH_DIR_INFO._fields_ = [
        ('NextEntryOffset', UInt32),
        ('FileIndex', UInt32),
        ('CreationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastAccessTime', win32more.Foundation.LARGE_INTEGER),
        ('LastWriteTime', win32more.Foundation.LARGE_INTEGER),
        ('ChangeTime', win32more.Foundation.LARGE_INTEGER),
        ('EndOfFile', win32more.Foundation.LARGE_INTEGER),
        ('AllocationSize', win32more.Foundation.LARGE_INTEGER),
        ('FileAttributes', UInt32),
        ('FileNameLength', UInt32),
        ('EaSize', UInt32),
        ('ShortNameLength', SByte),
        ('ShortName', Char * 12),
        ('FileId', win32more.Foundation.LARGE_INTEGER),
        ('FileName', Char * 1),
    ]
    return FILE_ID_BOTH_DIR_INFO
def _define_FILE_ID_DESCRIPTOR_head():
    class FILE_ID_DESCRIPTOR(Structure):
        pass
    return FILE_ID_DESCRIPTOR
def _define_FILE_ID_DESCRIPTOR():
    FILE_ID_DESCRIPTOR = win32more.Storage.FileSystem.FILE_ID_DESCRIPTOR_head
    class FILE_ID_DESCRIPTOR__Anonymous_e__Union(Union):
        pass
    FILE_ID_DESCRIPTOR__Anonymous_e__Union._fields_ = [
        ('FileId', win32more.Foundation.LARGE_INTEGER),
        ('ObjectId', Guid),
        ('ExtendedFileId', win32more.Storage.FileSystem.FILE_ID_128),
    ]
    FILE_ID_DESCRIPTOR._anonymous_ = [
        'Anonymous',
    ]
    FILE_ID_DESCRIPTOR._fields_ = [
        ('dwSize', UInt32),
        ('Type', win32more.Storage.FileSystem.FILE_ID_TYPE),
        ('Anonymous', FILE_ID_DESCRIPTOR__Anonymous_e__Union),
    ]
    return FILE_ID_DESCRIPTOR
def _define_FILE_ID_EXTD_DIR_INFO_head():
    class FILE_ID_EXTD_DIR_INFO(Structure):
        pass
    return FILE_ID_EXTD_DIR_INFO
def _define_FILE_ID_EXTD_DIR_INFO():
    FILE_ID_EXTD_DIR_INFO = win32more.Storage.FileSystem.FILE_ID_EXTD_DIR_INFO_head
    FILE_ID_EXTD_DIR_INFO._fields_ = [
        ('NextEntryOffset', UInt32),
        ('FileIndex', UInt32),
        ('CreationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastAccessTime', win32more.Foundation.LARGE_INTEGER),
        ('LastWriteTime', win32more.Foundation.LARGE_INTEGER),
        ('ChangeTime', win32more.Foundation.LARGE_INTEGER),
        ('EndOfFile', win32more.Foundation.LARGE_INTEGER),
        ('AllocationSize', win32more.Foundation.LARGE_INTEGER),
        ('FileAttributes', UInt32),
        ('FileNameLength', UInt32),
        ('EaSize', UInt32),
        ('ReparsePointTag', UInt32),
        ('FileId', win32more.Storage.FileSystem.FILE_ID_128),
        ('FileName', Char * 1),
    ]
    return FILE_ID_EXTD_DIR_INFO
def _define_FILE_ID_INFO_head():
    class FILE_ID_INFO(Structure):
        pass
    return FILE_ID_INFO
def _define_FILE_ID_INFO():
    FILE_ID_INFO = win32more.Storage.FileSystem.FILE_ID_INFO_head
    FILE_ID_INFO._fields_ = [
        ('VolumeSerialNumber', UInt64),
        ('FileId', win32more.Storage.FileSystem.FILE_ID_128),
    ]
    return FILE_ID_INFO
FILE_ID_TYPE = Int32
FILE_ID_TYPE_FileIdType = 0
FILE_ID_TYPE_ObjectIdType = 1
FILE_ID_TYPE_ExtendedFileIdType = 2
FILE_ID_TYPE_MaximumFileIdType = 3
def _define_FILE_INFO_2_head():
    class FILE_INFO_2(Structure):
        pass
    return FILE_INFO_2
def _define_FILE_INFO_2():
    FILE_INFO_2 = win32more.Storage.FileSystem.FILE_INFO_2_head
    FILE_INFO_2._fields_ = [
        ('fi2_id', UInt32),
    ]
    return FILE_INFO_2
def _define_FILE_INFO_3_head():
    class FILE_INFO_3(Structure):
        pass
    return FILE_INFO_3
def _define_FILE_INFO_3():
    FILE_INFO_3 = win32more.Storage.FileSystem.FILE_INFO_3_head
    FILE_INFO_3._fields_ = [
        ('fi3_id', UInt32),
        ('fi3_permissions', win32more.Storage.FileSystem.FILE_INFO_FLAGS_PERMISSIONS),
        ('fi3_num_locks', UInt32),
        ('fi3_pathname', win32more.Foundation.PWSTR),
        ('fi3_username', win32more.Foundation.PWSTR),
    ]
    return FILE_INFO_3
FILE_INFO_BY_HANDLE_CLASS = Int32
FILE_INFO_BY_HANDLE_CLASS_FileBasicInfo = 0
FILE_INFO_BY_HANDLE_CLASS_FileStandardInfo = 1
FILE_INFO_BY_HANDLE_CLASS_FileNameInfo = 2
FILE_INFO_BY_HANDLE_CLASS_FileRenameInfo = 3
FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfo = 4
FILE_INFO_BY_HANDLE_CLASS_FileAllocationInfo = 5
FILE_INFO_BY_HANDLE_CLASS_FileEndOfFileInfo = 6
FILE_INFO_BY_HANDLE_CLASS_FileStreamInfo = 7
FILE_INFO_BY_HANDLE_CLASS_FileCompressionInfo = 8
FILE_INFO_BY_HANDLE_CLASS_FileAttributeTagInfo = 9
FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryInfo = 10
FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryRestartInfo = 11
FILE_INFO_BY_HANDLE_CLASS_FileIoPriorityHintInfo = 12
FILE_INFO_BY_HANDLE_CLASS_FileRemoteProtocolInfo = 13
FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryInfo = 14
FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryRestartInfo = 15
FILE_INFO_BY_HANDLE_CLASS_FileStorageInfo = 16
FILE_INFO_BY_HANDLE_CLASS_FileAlignmentInfo = 17
FILE_INFO_BY_HANDLE_CLASS_FileIdInfo = 18
FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryInfo = 19
FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryRestartInfo = 20
FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfoEx = 21
FILE_INFO_BY_HANDLE_CLASS_FileRenameInfoEx = 22
FILE_INFO_BY_HANDLE_CLASS_FileCaseSensitiveInfo = 23
FILE_INFO_BY_HANDLE_CLASS_FileNormalizedNameInfo = 24
FILE_INFO_BY_HANDLE_CLASS_MaximumFileInfoByHandleClass = 25
FILE_INFO_FLAGS_PERMISSIONS = UInt32
PERM_FILE_READ = 1
PERM_FILE_WRITE = 2
PERM_FILE_CREATE = 4
def _define_FILE_IO_PRIORITY_HINT_INFO_head():
    class FILE_IO_PRIORITY_HINT_INFO(Structure):
        pass
    return FILE_IO_PRIORITY_HINT_INFO
def _define_FILE_IO_PRIORITY_HINT_INFO():
    FILE_IO_PRIORITY_HINT_INFO = win32more.Storage.FileSystem.FILE_IO_PRIORITY_HINT_INFO_head
    FILE_IO_PRIORITY_HINT_INFO._fields_ = [
        ('PriorityHint', win32more.Storage.FileSystem.PRIORITY_HINT),
    ]
    return FILE_IO_PRIORITY_HINT_INFO
FILE_NAME = UInt32
FILE_NAME_NORMALIZED = 0
FILE_NAME_OPENED = 8
def _define_FILE_NAME_INFO_head():
    class FILE_NAME_INFO(Structure):
        pass
    return FILE_NAME_INFO
def _define_FILE_NAME_INFO():
    FILE_NAME_INFO = win32more.Storage.FileSystem.FILE_NAME_INFO_head
    FILE_NAME_INFO._fields_ = [
        ('FileNameLength', UInt32),
        ('FileName', Char * 1),
    ]
    return FILE_NAME_INFO
FILE_NOTIFY_CHANGE = UInt32
FILE_NOTIFY_CHANGE_FILE_NAME = 1
FILE_NOTIFY_CHANGE_DIR_NAME = 2
FILE_NOTIFY_CHANGE_ATTRIBUTES = 4
FILE_NOTIFY_CHANGE_SIZE = 8
FILE_NOTIFY_CHANGE_LAST_WRITE = 16
FILE_NOTIFY_CHANGE_LAST_ACCESS = 32
FILE_NOTIFY_CHANGE_CREATION = 64
FILE_NOTIFY_CHANGE_SECURITY = 256
def _define_FILE_NOTIFY_EXTENDED_INFORMATION_head():
    class FILE_NOTIFY_EXTENDED_INFORMATION(Structure):
        pass
    return FILE_NOTIFY_EXTENDED_INFORMATION
def _define_FILE_NOTIFY_EXTENDED_INFORMATION():
    FILE_NOTIFY_EXTENDED_INFORMATION = win32more.Storage.FileSystem.FILE_NOTIFY_EXTENDED_INFORMATION_head
    FILE_NOTIFY_EXTENDED_INFORMATION._fields_ = [
        ('NextEntryOffset', UInt32),
        ('Action', win32more.Storage.FileSystem.FILE_ACTION),
        ('CreationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastModificationTime', win32more.Foundation.LARGE_INTEGER),
        ('LastChangeTime', win32more.Foundation.LARGE_INTEGER),
        ('LastAccessTime', win32more.Foundation.LARGE_INTEGER),
        ('AllocatedLength', win32more.Foundation.LARGE_INTEGER),
        ('FileSize', win32more.Foundation.LARGE_INTEGER),
        ('FileAttributes', UInt32),
        ('ReparsePointTag', UInt32),
        ('FileId', win32more.Foundation.LARGE_INTEGER),
        ('ParentFileId', win32more.Foundation.LARGE_INTEGER),
        ('FileNameLength', UInt32),
        ('FileName', Char * 1),
    ]
    return FILE_NOTIFY_EXTENDED_INFORMATION
def _define_FILE_NOTIFY_INFORMATION_head():
    class FILE_NOTIFY_INFORMATION(Structure):
        pass
    return FILE_NOTIFY_INFORMATION
def _define_FILE_NOTIFY_INFORMATION():
    FILE_NOTIFY_INFORMATION = win32more.Storage.FileSystem.FILE_NOTIFY_INFORMATION_head
    FILE_NOTIFY_INFORMATION._fields_ = [
        ('NextEntryOffset', UInt32),
        ('Action', win32more.Storage.FileSystem.FILE_ACTION),
        ('FileNameLength', UInt32),
        ('FileName', Char * 1),
    ]
    return FILE_NOTIFY_INFORMATION
def _define_FILE_REMOTE_PROTOCOL_INFO_head():
    class FILE_REMOTE_PROTOCOL_INFO(Structure):
        pass
    return FILE_REMOTE_PROTOCOL_INFO
def _define_FILE_REMOTE_PROTOCOL_INFO():
    FILE_REMOTE_PROTOCOL_INFO = win32more.Storage.FileSystem.FILE_REMOTE_PROTOCOL_INFO_head
    class FILE_REMOTE_PROTOCOL_INFO__GenericReserved_e__Struct(Structure):
        pass
    FILE_REMOTE_PROTOCOL_INFO__GenericReserved_e__Struct._fields_ = [
        ('Reserved', UInt32 * 8),
    ]
    class FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union(Union):
        pass
    class FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct(Structure):
        pass
    class FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Server_e__Struct(Structure):
        pass
    FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Server_e__Struct._fields_ = [
        ('Capabilities', UInt32),
    ]
    class FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Share_e__Struct(Structure):
        pass
    FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Share_e__Struct._fields_ = [
        ('Capabilities', UInt32),
        ('CachingFlags', UInt32),
    ]
    FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct._fields_ = [
        ('Server', FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Server_e__Struct),
        ('Share', FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct__Share_e__Struct),
    ]
    FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union._fields_ = [
        ('Smb2', FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union__Smb2_e__Struct),
        ('Reserved', UInt32 * 16),
    ]
    FILE_REMOTE_PROTOCOL_INFO._fields_ = [
        ('StructureVersion', UInt16),
        ('StructureSize', UInt16),
        ('Protocol', UInt32),
        ('ProtocolMajorVersion', UInt16),
        ('ProtocolMinorVersion', UInt16),
        ('ProtocolRevision', UInt16),
        ('Reserved', UInt16),
        ('Flags', UInt32),
        ('GenericReserved', FILE_REMOTE_PROTOCOL_INFO__GenericReserved_e__Struct),
        ('ProtocolSpecific', FILE_REMOTE_PROTOCOL_INFO__ProtocolSpecific_e__Union),
    ]
    return FILE_REMOTE_PROTOCOL_INFO
def _define_FILE_RENAME_INFO_head():
    class FILE_RENAME_INFO(Structure):
        pass
    return FILE_RENAME_INFO
def _define_FILE_RENAME_INFO():
    FILE_RENAME_INFO = win32more.Storage.FileSystem.FILE_RENAME_INFO_head
    class FILE_RENAME_INFO__Anonymous_e__Union(Union):
        pass
    FILE_RENAME_INFO__Anonymous_e__Union._fields_ = [
        ('ReplaceIfExists', win32more.Foundation.BOOLEAN),
        ('Flags', UInt32),
    ]
    FILE_RENAME_INFO._anonymous_ = [
        'Anonymous',
    ]
    FILE_RENAME_INFO._fields_ = [
        ('Anonymous', FILE_RENAME_INFO__Anonymous_e__Union),
        ('RootDirectory', win32more.Foundation.HANDLE),
        ('FileNameLength', UInt32),
        ('FileName', Char * 1),
    ]
    return FILE_RENAME_INFO
def _define_FILE_SEGMENT_ELEMENT_head():
    class FILE_SEGMENT_ELEMENT(Union):
        pass
    return FILE_SEGMENT_ELEMENT
def _define_FILE_SEGMENT_ELEMENT():
    FILE_SEGMENT_ELEMENT = win32more.Storage.FileSystem.FILE_SEGMENT_ELEMENT_head
    FILE_SEGMENT_ELEMENT._fields_ = [
        ('Buffer', c_void_p),
        ('Alignment', UInt64),
    ]
    return FILE_SEGMENT_ELEMENT
FILE_SHARE_MODE = UInt32
FILE_SHARE_NONE = 0
FILE_SHARE_DELETE = 4
FILE_SHARE_READ = 1
FILE_SHARE_WRITE = 2
def _define_FILE_STANDARD_INFO_head():
    class FILE_STANDARD_INFO(Structure):
        pass
    return FILE_STANDARD_INFO
def _define_FILE_STANDARD_INFO():
    FILE_STANDARD_INFO = win32more.Storage.FileSystem.FILE_STANDARD_INFO_head
    FILE_STANDARD_INFO._fields_ = [
        ('AllocationSize', win32more.Foundation.LARGE_INTEGER),
        ('EndOfFile', win32more.Foundation.LARGE_INTEGER),
        ('NumberOfLinks', UInt32),
        ('DeletePending', win32more.Foundation.BOOLEAN),
        ('Directory', win32more.Foundation.BOOLEAN),
    ]
    return FILE_STANDARD_INFO
def _define_FILE_STORAGE_INFO_head():
    class FILE_STORAGE_INFO(Structure):
        pass
    return FILE_STORAGE_INFO
def _define_FILE_STORAGE_INFO():
    FILE_STORAGE_INFO = win32more.Storage.FileSystem.FILE_STORAGE_INFO_head
    FILE_STORAGE_INFO._fields_ = [
        ('LogicalBytesPerSector', UInt32),
        ('PhysicalBytesPerSectorForAtomicity', UInt32),
        ('PhysicalBytesPerSectorForPerformance', UInt32),
        ('FileSystemEffectivePhysicalBytesPerSectorForAtomicity', UInt32),
        ('Flags', UInt32),
        ('ByteOffsetForSectorAlignment', UInt32),
        ('ByteOffsetForPartitionAlignment', UInt32),
    ]
    return FILE_STORAGE_INFO
def _define_FILE_STREAM_INFO_head():
    class FILE_STREAM_INFO(Structure):
        pass
    return FILE_STREAM_INFO
def _define_FILE_STREAM_INFO():
    FILE_STREAM_INFO = win32more.Storage.FileSystem.FILE_STREAM_INFO_head
    FILE_STREAM_INFO._fields_ = [
        ('NextEntryOffset', UInt32),
        ('StreamNameLength', UInt32),
        ('StreamSize', win32more.Foundation.LARGE_INTEGER),
        ('StreamAllocationSize', win32more.Foundation.LARGE_INTEGER),
        ('StreamName', Char * 1),
    ]
    return FILE_STREAM_INFO
FILE_TYPE = UInt32
FILE_TYPE_UNKNOWN = 0
FILE_TYPE_DISK = 1
FILE_TYPE_CHAR = 2
FILE_TYPE_PIPE = 3
FILE_TYPE_REMOTE = 32768
FIND_FIRST_EX_FLAGS = UInt32
FIND_FIRST_EX_CASE_SENSITIVE = 1
FIND_FIRST_EX_LARGE_FETCH = 2
FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY = 4
FindChangeNotificationHandle = IntPtr
FINDEX_INFO_LEVELS = Int32
FINDEX_INFO_LEVELS_FindExInfoStandard = 0
FINDEX_INFO_LEVELS_FindExInfoBasic = 1
FINDEX_INFO_LEVELS_FindExInfoMaxInfoLevel = 2
FINDEX_SEARCH_OPS = Int32
FINDEX_SEARCH_OPS_FindExSearchNameMatch = 0
FINDEX_SEARCH_OPS_FindExSearchLimitToDirectories = 1
FINDEX_SEARCH_OPS_FindExSearchLimitToDevices = 2
FINDEX_SEARCH_OPS_FindExSearchMaxSearchOp = 3
FindFileHandle = IntPtr
FindFileNameHandle = IntPtr
FindStreamHandle = IntPtr
FindVolumeHandle = IntPtr
FindVolumeMointPointHandle = IntPtr
def _define_FIO_CONTEXT_head():
    class FIO_CONTEXT(Structure):
        pass
    return FIO_CONTEXT
def _define_FIO_CONTEXT():
    FIO_CONTEXT = win32more.Storage.FileSystem.FIO_CONTEXT_head
    FIO_CONTEXT._fields_ = [
        ('m_dwTempHack', UInt32),
        ('m_dwSignature', UInt32),
        ('m_hFile', win32more.Foundation.HANDLE),
        ('m_dwLinesOffset', UInt32),
        ('m_dwHeaderLength', UInt32),
    ]
    return FIO_CONTEXT
GET_FILE_VERSION_INFO_FLAGS = UInt32
FILE_VER_GET_LOCALISED = 1
FILE_VER_GET_NEUTRAL = 2
FILE_VER_GET_PREFETCHED = 4
GET_FILEEX_INFO_LEVELS = Int32
GET_FILEEX_INFO_LEVELS_GetFileExInfoStandard = 0
GET_FILEEX_INFO_LEVELS_GetFileExMaxInfoLevel = 1
GET_TAPE_DRIVE_PARAMETERS_OPERATION = UInt32
GET_TAPE_DRIVE_INFORMATION = 1
GET_TAPE_MEDIA_INFORMATION = 0
def _define_HIORING___head():
    class HIORING__(Structure):
        pass
    return HIORING__
def _define_HIORING__():
    HIORING__ = win32more.Storage.FileSystem.HIORING___head
    HIORING__._fields_ = [
        ('unused', Int32),
    ]
    return HIORING__
def _define_IDiskQuotaControl_head():
    class IDiskQuotaControl(win32more.System.Com.IConnectionPointContainer_head):
        Guid = Guid('7988b572-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    return IDiskQuotaControl
def _define_IDiskQuotaControl():
    IDiskQuotaControl = win32more.Storage.FileSystem.IDiskQuotaControl_head
    IDiskQuotaControl.Initialize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL)(5, 'Initialize', ((1, 'pszPath'),(1, 'bReadWrite'),)))
    IDiskQuotaControl.SetQuotaState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'SetQuotaState', ((1, 'dwState'),)))
    IDiskQuotaControl.GetQuotaState = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(7, 'GetQuotaState', ((1, 'pdwState'),)))
    IDiskQuotaControl.SetQuotaLogFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'SetQuotaLogFlags', ((1, 'dwFlags'),)))
    IDiskQuotaControl.GetQuotaLogFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetQuotaLogFlags', ((1, 'pdwFlags'),)))
    IDiskQuotaControl.SetDefaultQuotaThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(10, 'SetDefaultQuotaThreshold', ((1, 'llThreshold'),)))
    IDiskQuotaControl.GetDefaultQuotaThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(11, 'GetDefaultQuotaThreshold', ((1, 'pllThreshold'),)))
    IDiskQuotaControl.GetDefaultQuotaThresholdText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(12, 'GetDefaultQuotaThresholdText', ((1, 'pszText'),(1, 'cchText'),)))
    IDiskQuotaControl.SetDefaultQuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(13, 'SetDefaultQuotaLimit', ((1, 'llLimit'),)))
    IDiskQuotaControl.GetDefaultQuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(14, 'GetDefaultQuotaLimit', ((1, 'pllLimit'),)))
    IDiskQuotaControl.GetDefaultQuotaLimitText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(15, 'GetDefaultQuotaLimitText', ((1, 'pszText'),(1, 'cchText'),)))
    IDiskQuotaControl.AddUserSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE,POINTER(win32more.Storage.FileSystem.IDiskQuotaUser_head))(16, 'AddUserSid', ((1, 'pUserSid'),(1, 'fNameResolution'),(1, 'ppUser'),)))
    IDiskQuotaControl.AddUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE,POINTER(win32more.Storage.FileSystem.IDiskQuotaUser_head))(17, 'AddUserName', ((1, 'pszLogonName'),(1, 'fNameResolution'),(1, 'ppUser'),)))
    IDiskQuotaControl.DeleteUser = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IDiskQuotaUser_head)(18, 'DeleteUser', ((1, 'pUser'),)))
    IDiskQuotaControl.FindUserSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PSID,win32more.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE,POINTER(win32more.Storage.FileSystem.IDiskQuotaUser_head))(19, 'FindUserSid', ((1, 'pUserSid'),(1, 'fNameResolution'),(1, 'ppUser'),)))
    IDiskQuotaControl.FindUserName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.FileSystem.IDiskQuotaUser_head))(20, 'FindUserName', ((1, 'pszLogonName'),(1, 'ppUser'),)))
    IDiskQuotaControl.CreateEnumUsers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PSID),UInt32,win32more.Storage.FileSystem.DISKQUOTA_USERNAME_RESOLVE,POINTER(win32more.Storage.FileSystem.IEnumDiskQuotaUsers_head))(21, 'CreateEnumUsers', ((1, 'rgpUserSids'),(1, 'cpSids'),(1, 'fNameResolution'),(1, 'ppEnum'),)))
    IDiskQuotaControl.CreateUserBatch = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.IDiskQuotaUserBatch_head))(22, 'CreateUserBatch', ((1, 'ppBatch'),)))
    IDiskQuotaControl.InvalidateSidNameCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(23, 'InvalidateSidNameCache', ()))
    IDiskQuotaControl.GiveUserNameResolutionPriority = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IDiskQuotaUser_head)(24, 'GiveUserNameResolutionPriority', ((1, 'pUser'),)))
    IDiskQuotaControl.ShutdownNameResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(25, 'ShutdownNameResolution', ()))
    win32more.System.Com.IConnectionPointContainer
    return IDiskQuotaControl
def _define_IDiskQuotaEvents_head():
    class IDiskQuotaEvents(win32more.System.Com.IUnknown_head):
        Guid = Guid('7988b579-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    return IDiskQuotaEvents
def _define_IDiskQuotaEvents():
    IDiskQuotaEvents = win32more.Storage.FileSystem.IDiskQuotaEvents_head
    IDiskQuotaEvents.OnUserNameChanged = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IDiskQuotaUser_head)(3, 'OnUserNameChanged', ((1, 'pUser'),)))
    win32more.System.Com.IUnknown
    return IDiskQuotaEvents
def _define_IDiskQuotaUser_head():
    class IDiskQuotaUser(win32more.System.Com.IUnknown_head):
        Guid = Guid('7988b574-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    return IDiskQuotaUser
def _define_IDiskQuotaUser():
    IDiskQuotaUser = win32more.Storage.FileSystem.IDiskQuotaUser_head
    IDiskQuotaUser.GetID = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetID', ((1, 'pulID'),)))
    IDiskQuotaUser.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32,win32more.Foundation.PWSTR,UInt32)(4, 'GetName', ((1, 'pszAccountContainer'),(1, 'cchAccountContainer'),(1, 'pszLogonName'),(1, 'cchLogonName'),(1, 'pszDisplayName'),(1, 'cchDisplayName'),)))
    IDiskQuotaUser.GetSidLength = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetSidLength', ((1, 'pdwLength'),)))
    IDiskQuotaUser.GetSid = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(6, 'GetSid', ((1, 'pbSidBuffer'),(1, 'cbSidBuffer'),)))
    IDiskQuotaUser.GetQuotaThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(7, 'GetQuotaThreshold', ((1, 'pllThreshold'),)))
    IDiskQuotaUser.GetQuotaThresholdText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(8, 'GetQuotaThresholdText', ((1, 'pszText'),(1, 'cchText'),)))
    IDiskQuotaUser.GetQuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(9, 'GetQuotaLimit', ((1, 'pllLimit'),)))
    IDiskQuotaUser.GetQuotaLimitText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(10, 'GetQuotaLimitText', ((1, 'pszText'),(1, 'cchText'),)))
    IDiskQuotaUser.GetQuotaUsed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(11, 'GetQuotaUsed', ((1, 'pllUsed'),)))
    IDiskQuotaUser.GetQuotaUsedText = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,UInt32)(12, 'GetQuotaUsedText', ((1, 'pszText'),(1, 'cchText'),)))
    IDiskQuotaUser.GetQuotaInformation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_void_p,UInt32)(13, 'GetQuotaInformation', ((1, 'pbQuotaInfo'),(1, 'cbQuotaInfo'),)))
    IDiskQuotaUser.SetQuotaThreshold = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,win32more.Foundation.BOOL)(14, 'SetQuotaThreshold', ((1, 'llThreshold'),(1, 'fWriteThrough'),)))
    IDiskQuotaUser.SetQuotaLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,win32more.Foundation.BOOL)(15, 'SetQuotaLimit', ((1, 'llLimit'),(1, 'fWriteThrough'),)))
    IDiskQuotaUser.Invalidate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(16, 'Invalidate', ()))
    IDiskQuotaUser.GetAccountStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(17, 'GetAccountStatus', ((1, 'pdwStatus'),)))
    win32more.System.Com.IUnknown
    return IDiskQuotaUser
def _define_IDiskQuotaUserBatch_head():
    class IDiskQuotaUserBatch(win32more.System.Com.IUnknown_head):
        Guid = Guid('7988b576-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    return IDiskQuotaUserBatch
def _define_IDiskQuotaUserBatch():
    IDiskQuotaUserBatch = win32more.Storage.FileSystem.IDiskQuotaUserBatch_head
    IDiskQuotaUserBatch.Add = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IDiskQuotaUser_head)(3, 'Add', ((1, 'pUser'),)))
    IDiskQuotaUserBatch.Remove = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.FileSystem.IDiskQuotaUser_head)(4, 'Remove', ((1, 'pUser'),)))
    IDiskQuotaUserBatch.RemoveAll = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'RemoveAll', ()))
    IDiskQuotaUserBatch.FlushToDisk = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'FlushToDisk', ()))
    win32more.System.Com.IUnknown
    return IDiskQuotaUserBatch
def _define_IEnumDiskQuotaUsers_head():
    class IEnumDiskQuotaUsers(win32more.System.Com.IUnknown_head):
        Guid = Guid('7988b577-ec89-11cf-9c-00-00-aa-00-a1-4f-56')
    return IEnumDiskQuotaUsers
def _define_IEnumDiskQuotaUsers():
    IEnumDiskQuotaUsers = win32more.Storage.FileSystem.IEnumDiskQuotaUsers_head
    IEnumDiskQuotaUsers.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.FileSystem.IDiskQuotaUser_head),POINTER(UInt32))(3, 'Next', ((1, 'cUsers'),(1, 'rgUsers'),(1, 'pcUsersFetched'),)))
    IEnumDiskQuotaUsers.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'cUsers'),)))
    IEnumDiskQuotaUsers.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumDiskQuotaUsers.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.FileSystem.IEnumDiskQuotaUsers_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumDiskQuotaUsers
def _define_IORING_BUFFER_INFO_head():
    class IORING_BUFFER_INFO(Structure):
        pass
    return IORING_BUFFER_INFO
def _define_IORING_BUFFER_INFO():
    IORING_BUFFER_INFO = win32more.Storage.FileSystem.IORING_BUFFER_INFO_head
    IORING_BUFFER_INFO._fields_ = [
        ('Address', c_void_p),
        ('Length', UInt32),
    ]
    return IORING_BUFFER_INFO
def _define_IORING_BUFFER_REF_head():
    class IORING_BUFFER_REF(Structure):
        pass
    return IORING_BUFFER_REF
def _define_IORING_BUFFER_REF():
    IORING_BUFFER_REF = win32more.Storage.FileSystem.IORING_BUFFER_REF_head
    class IORING_BUFFER_REF_BufferUnion(Union):
        pass
    IORING_BUFFER_REF_BufferUnion._fields_ = [
        ('Address', c_void_p),
        ('IndexAndOffset', win32more.Storage.FileSystem.IORING_REGISTERED_BUFFER),
    ]
    IORING_BUFFER_REF._fields_ = [
        ('Kind', win32more.Storage.FileSystem.IORING_REF_KIND),
        ('Buffer', IORING_BUFFER_REF_BufferUnion),
    ]
    return IORING_BUFFER_REF
def _define_IORING_CAPABILITIES_head():
    class IORING_CAPABILITIES(Structure):
        pass
    return IORING_CAPABILITIES
def _define_IORING_CAPABILITIES():
    IORING_CAPABILITIES = win32more.Storage.FileSystem.IORING_CAPABILITIES_head
    IORING_CAPABILITIES._fields_ = [
        ('MaxVersion', win32more.Storage.FileSystem.IORING_VERSION),
        ('MaxSubmissionQueueSize', UInt32),
        ('MaxCompletionQueueSize', UInt32),
        ('FeatureFlags', win32more.Storage.FileSystem.IORING_FEATURE_FLAGS),
    ]
    return IORING_CAPABILITIES
def _define_IORING_CQE_head():
    class IORING_CQE(Structure):
        pass
    return IORING_CQE
def _define_IORING_CQE():
    IORING_CQE = win32more.Storage.FileSystem.IORING_CQE_head
    IORING_CQE._fields_ = [
        ('UserData', UIntPtr),
        ('ResultCode', win32more.Foundation.HRESULT),
        ('Information', UIntPtr),
    ]
    return IORING_CQE
IORING_CREATE_ADVISORY_FLAGS = Int32
IORING_CREATE_ADVISORY_FLAGS_NONE = 0
def _define_IORING_CREATE_FLAGS_head():
    class IORING_CREATE_FLAGS(Structure):
        pass
    return IORING_CREATE_FLAGS
def _define_IORING_CREATE_FLAGS():
    IORING_CREATE_FLAGS = win32more.Storage.FileSystem.IORING_CREATE_FLAGS_head
    IORING_CREATE_FLAGS._fields_ = [
        ('Required', win32more.Storage.FileSystem.IORING_CREATE_REQUIRED_FLAGS),
        ('Advisory', win32more.Storage.FileSystem.IORING_CREATE_ADVISORY_FLAGS),
    ]
    return IORING_CREATE_FLAGS
IORING_CREATE_REQUIRED_FLAGS = Int32
IORING_CREATE_REQUIRED_FLAGS_NONE = 0
IORING_FEATURE_FLAGS = Int32
IORING_FEATURE_FLAGS_NONE = 0
IORING_FEATURE_UM_EMULATION = 1
IORING_FEATURE_SET_COMPLETION_EVENT = 2
def _define_IORING_HANDLE_REF_head():
    class IORING_HANDLE_REF(Structure):
        pass
    return IORING_HANDLE_REF
def _define_IORING_HANDLE_REF():
    IORING_HANDLE_REF = win32more.Storage.FileSystem.IORING_HANDLE_REF_head
    class IORING_HANDLE_REF_HandleUnion(Union):
        pass
    IORING_HANDLE_REF_HandleUnion._fields_ = [
        ('Handle', win32more.Foundation.HANDLE),
        ('Index', UInt32),
    ]
    IORING_HANDLE_REF._fields_ = [
        ('Kind', win32more.Storage.FileSystem.IORING_REF_KIND),
        ('Handle', IORING_HANDLE_REF_HandleUnion),
    ]
    return IORING_HANDLE_REF
def _define_IORING_INFO_head():
    class IORING_INFO(Structure):
        pass
    return IORING_INFO
def _define_IORING_INFO():
    IORING_INFO = win32more.Storage.FileSystem.IORING_INFO_head
    IORING_INFO._fields_ = [
        ('IoRingVersion', win32more.Storage.FileSystem.IORING_VERSION),
        ('Flags', win32more.Storage.FileSystem.IORING_CREATE_FLAGS),
        ('SubmissionQueueSize', UInt32),
        ('CompletionQueueSize', UInt32),
    ]
    return IORING_INFO
IORING_OP_CODE = Int32
IORING_OP_NOP = 0
IORING_OP_READ = 1
IORING_OP_REGISTER_FILES = 2
IORING_OP_REGISTER_BUFFERS = 3
IORING_OP_CANCEL = 4
IORING_REF_KIND = Int32
IORING_REF_RAW = 0
IORING_REF_REGISTERED = 1
def _define_IORING_REGISTERED_BUFFER_head():
    class IORING_REGISTERED_BUFFER(Structure):
        pass
    return IORING_REGISTERED_BUFFER
def _define_IORING_REGISTERED_BUFFER():
    IORING_REGISTERED_BUFFER = win32more.Storage.FileSystem.IORING_REGISTERED_BUFFER_head
    IORING_REGISTERED_BUFFER._fields_ = [
        ('BufferIndex', UInt32),
        ('Offset', UInt32),
    ]
    return IORING_REGISTERED_BUFFER
IORING_SQE_FLAGS = Int32
IOSQE_FLAGS_NONE = 0
IORING_VERSION = Int32
IORING_VERSION_INVALID = 0
IORING_VERSION_1 = 1
def _define_KCRM_MARSHAL_HEADER_head():
    class KCRM_MARSHAL_HEADER(Structure):
        pass
    return KCRM_MARSHAL_HEADER
def _define_KCRM_MARSHAL_HEADER():
    KCRM_MARSHAL_HEADER = win32more.Storage.FileSystem.KCRM_MARSHAL_HEADER_head
    KCRM_MARSHAL_HEADER._fields_ = [
        ('VersionMajor', UInt32),
        ('VersionMinor', UInt32),
        ('NumProtocols', UInt32),
        ('Unused', UInt32),
    ]
    return KCRM_MARSHAL_HEADER
def _define_KCRM_PROTOCOL_BLOB_head():
    class KCRM_PROTOCOL_BLOB(Structure):
        pass
    return KCRM_PROTOCOL_BLOB
def _define_KCRM_PROTOCOL_BLOB():
    KCRM_PROTOCOL_BLOB = win32more.Storage.FileSystem.KCRM_PROTOCOL_BLOB_head
    KCRM_PROTOCOL_BLOB._fields_ = [
        ('ProtocolId', Guid),
        ('StaticInfoLength', UInt32),
        ('TransactionIdInfoLength', UInt32),
        ('Unused1', UInt32),
        ('Unused2', UInt32),
    ]
    return KCRM_PROTOCOL_BLOB
def _define_KCRM_TRANSACTION_BLOB_head():
    class KCRM_TRANSACTION_BLOB(Structure):
        pass
    return KCRM_TRANSACTION_BLOB
def _define_KCRM_TRANSACTION_BLOB():
    KCRM_TRANSACTION_BLOB = win32more.Storage.FileSystem.KCRM_TRANSACTION_BLOB_head
    KCRM_TRANSACTION_BLOB._fields_ = [
        ('UOW', Guid),
        ('TmIdentity', Guid),
        ('IsolationLevel', UInt32),
        ('IsolationFlags', UInt32),
        ('Timeout', UInt32),
        ('Description', Char * 64),
    ]
    return KCRM_TRANSACTION_BLOB
LOCK_FILE_FLAGS = UInt32
LOCKFILE_EXCLUSIVE_LOCK = 2
LOCKFILE_FAIL_IMMEDIATELY = 1
def _define_LOG_MANAGEMENT_CALLBACKS_head():
    class LOG_MANAGEMENT_CALLBACKS(Structure):
        pass
    return LOG_MANAGEMENT_CALLBACKS
def _define_LOG_MANAGEMENT_CALLBACKS():
    LOG_MANAGEMENT_CALLBACKS = win32more.Storage.FileSystem.LOG_MANAGEMENT_CALLBACKS_head
    LOG_MANAGEMENT_CALLBACKS._fields_ = [
        ('CallbackContext', c_void_p),
        ('AdvanceTailCallback', win32more.Storage.FileSystem.PLOG_TAIL_ADVANCE_CALLBACK),
        ('LogFullHandlerCallback', win32more.Storage.FileSystem.PLOG_FULL_HANDLER_CALLBACK),
        ('LogUnpinnedCallback', win32more.Storage.FileSystem.PLOG_UNPINNED_CALLBACK),
    ]
    return LOG_MANAGEMENT_CALLBACKS
def _define_LPPROGRESS_ROUTINE():
    return WINFUNCTYPE(UInt32,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,win32more.Foundation.LARGE_INTEGER,UInt32,win32more.Storage.FileSystem.LPPROGRESS_ROUTINE_CALLBACK_REASON,win32more.Foundation.HANDLE,win32more.Foundation.HANDLE,c_void_p)
LPPROGRESS_ROUTINE_CALLBACK_REASON = UInt32
CALLBACK_CHUNK_FINISHED = 0
CALLBACK_STREAM_SWITCH = 1
LZOPENFILE_STYLE = UInt16
OF_CANCEL = 2048
OF_CREATE = 4096
OF_DELETE = 512
OF_EXIST = 16384
OF_PARSE = 256
OF_PROMPT = 8192
OF_READ = 0
OF_READWRITE = 2
OF_REOPEN = 32768
OF_SHARE_DENY_NONE = 64
OF_SHARE_DENY_READ = 48
OF_SHARE_DENY_WRITE = 32
OF_SHARE_EXCLUSIVE = 16
OF_WRITE = 1
OF_SHARE_COMPAT = 0
OF_VERIFY = 1024
def _define_MAXMEDIALABEL():
    return WINFUNCTYPE(UInt32,POINTER(UInt32))
def _define_MediaLabelInfo_head():
    class MediaLabelInfo(Structure):
        pass
    return MediaLabelInfo
def _define_MediaLabelInfo():
    MediaLabelInfo = win32more.Storage.FileSystem.MediaLabelInfo_head
    MediaLabelInfo._fields_ = [
        ('LabelType', Char * 64),
        ('LabelIDSize', UInt32),
        ('LabelID', Byte * 256),
        ('LabelAppDescr', Char * 256),
    ]
    return MediaLabelInfo
MOVE_FILE_FLAGS = UInt32
MOVEFILE_COPY_ALLOWED = 2
MOVEFILE_CREATE_HARDLINK = 16
MOVEFILE_DELAY_UNTIL_REBOOT = 4
MOVEFILE_REPLACE_EXISTING = 1
MOVEFILE_WRITE_THROUGH = 8
MOVEFILE_FAIL_IF_NOT_TRACKABLE = 32
def _define_NAME_CACHE_CONTEXT_head():
    class NAME_CACHE_CONTEXT(Structure):
        pass
    return NAME_CACHE_CONTEXT
def _define_NAME_CACHE_CONTEXT():
    NAME_CACHE_CONTEXT = win32more.Storage.FileSystem.NAME_CACHE_CONTEXT_head
    NAME_CACHE_CONTEXT._fields_ = [
        ('m_dwSignature', UInt32),
    ]
    return NAME_CACHE_CONTEXT
NT_CREATE_FILE_DISPOSITION = UInt32
FILE_SUPERSEDE = 0
FILE_CREATE = 2
FILE_OPEN = 1
FILE_OPEN_IF = 3
FILE_OVERWRITE = 4
FILE_OVERWRITE_IF = 5
def _define_NTMS_ALLOCATION_INFORMATION_head():
    class NTMS_ALLOCATION_INFORMATION(Structure):
        pass
    return NTMS_ALLOCATION_INFORMATION
def _define_NTMS_ALLOCATION_INFORMATION():
    NTMS_ALLOCATION_INFORMATION = win32more.Storage.FileSystem.NTMS_ALLOCATION_INFORMATION_head
    NTMS_ALLOCATION_INFORMATION._fields_ = [
        ('dwSize', UInt32),
        ('lpReserved', c_void_p),
        ('AllocatedFrom', Guid),
    ]
    return NTMS_ALLOCATION_INFORMATION
def _define_NTMS_ASYNC_IO_head():
    class NTMS_ASYNC_IO(Structure):
        pass
    return NTMS_ASYNC_IO
def _define_NTMS_ASYNC_IO():
    NTMS_ASYNC_IO = win32more.Storage.FileSystem.NTMS_ASYNC_IO_head
    NTMS_ASYNC_IO._fields_ = [
        ('OperationId', Guid),
        ('EventId', Guid),
        ('dwOperationType', UInt32),
        ('dwResult', UInt32),
        ('dwAsyncState', UInt32),
        ('hEvent', win32more.Foundation.HANDLE),
        ('bOnStateChange', win32more.Foundation.BOOL),
    ]
    return NTMS_ASYNC_IO
def _define_NTMS_CHANGERINFORMATIONA_head():
    class NTMS_CHANGERINFORMATIONA(Structure):
        pass
    return NTMS_CHANGERINFORMATIONA
def _define_NTMS_CHANGERINFORMATIONA():
    NTMS_CHANGERINFORMATIONA = win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONA_head
    NTMS_CHANGERINFORMATIONA._fields_ = [
        ('Number', UInt32),
        ('ChangerType', Guid),
        ('szSerialNumber', win32more.Foundation.CHAR * 32),
        ('szRevision', win32more.Foundation.CHAR * 32),
        ('szDeviceName', win32more.Foundation.CHAR * 64),
        ('ScsiPort', UInt16),
        ('ScsiBus', UInt16),
        ('ScsiTarget', UInt16),
        ('ScsiLun', UInt16),
        ('Library', Guid),
    ]
    return NTMS_CHANGERINFORMATIONA
def _define_NTMS_CHANGERINFORMATIONW_head():
    class NTMS_CHANGERINFORMATIONW(Structure):
        pass
    return NTMS_CHANGERINFORMATIONW
def _define_NTMS_CHANGERINFORMATIONW():
    NTMS_CHANGERINFORMATIONW = win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONW_head
    NTMS_CHANGERINFORMATIONW._fields_ = [
        ('Number', UInt32),
        ('ChangerType', Guid),
        ('szSerialNumber', Char * 32),
        ('szRevision', Char * 32),
        ('szDeviceName', Char * 64),
        ('ScsiPort', UInt16),
        ('ScsiBus', UInt16),
        ('ScsiTarget', UInt16),
        ('ScsiLun', UInt16),
        ('Library', Guid),
    ]
    return NTMS_CHANGERINFORMATIONW
def _define_NTMS_CHANGERTYPEINFORMATIONA_head():
    class NTMS_CHANGERTYPEINFORMATIONA(Structure):
        pass
    return NTMS_CHANGERTYPEINFORMATIONA
def _define_NTMS_CHANGERTYPEINFORMATIONA():
    NTMS_CHANGERTYPEINFORMATIONA = win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA_head
    NTMS_CHANGERTYPEINFORMATIONA._fields_ = [
        ('szVendor', win32more.Foundation.CHAR * 128),
        ('szProduct', win32more.Foundation.CHAR * 128),
        ('DeviceType', UInt32),
    ]
    return NTMS_CHANGERTYPEINFORMATIONA
def _define_NTMS_CHANGERTYPEINFORMATIONW_head():
    class NTMS_CHANGERTYPEINFORMATIONW(Structure):
        pass
    return NTMS_CHANGERTYPEINFORMATIONW
def _define_NTMS_CHANGERTYPEINFORMATIONW():
    NTMS_CHANGERTYPEINFORMATIONW = win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW_head
    NTMS_CHANGERTYPEINFORMATIONW._fields_ = [
        ('szVendor', Char * 128),
        ('szProduct', Char * 128),
        ('DeviceType', UInt32),
    ]
    return NTMS_CHANGERTYPEINFORMATIONW
def _define_NTMS_COMPUTERINFORMATION_head():
    class NTMS_COMPUTERINFORMATION(Structure):
        pass
    return NTMS_COMPUTERINFORMATION
def _define_NTMS_COMPUTERINFORMATION():
    NTMS_COMPUTERINFORMATION = win32more.Storage.FileSystem.NTMS_COMPUTERINFORMATION_head
    NTMS_COMPUTERINFORMATION._fields_ = [
        ('dwLibRequestPurgeTime', UInt32),
        ('dwOpRequestPurgeTime', UInt32),
        ('dwLibRequestFlags', UInt32),
        ('dwOpRequestFlags', UInt32),
        ('dwMediaPoolPolicy', UInt32),
    ]
    return NTMS_COMPUTERINFORMATION
def _define_NTMS_DRIVEINFORMATIONA_head():
    class NTMS_DRIVEINFORMATIONA(Structure):
        pass
    return NTMS_DRIVEINFORMATIONA
def _define_NTMS_DRIVEINFORMATIONA():
    NTMS_DRIVEINFORMATIONA = win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONA_head
    NTMS_DRIVEINFORMATIONA._fields_ = [
        ('Number', UInt32),
        ('State', win32more.Storage.FileSystem.NtmsDriveState),
        ('DriveType', Guid),
        ('szDeviceName', win32more.Foundation.CHAR * 64),
        ('szSerialNumber', win32more.Foundation.CHAR * 32),
        ('szRevision', win32more.Foundation.CHAR * 32),
        ('ScsiPort', UInt16),
        ('ScsiBus', UInt16),
        ('ScsiTarget', UInt16),
        ('ScsiLun', UInt16),
        ('dwMountCount', UInt32),
        ('LastCleanedTs', win32more.Foundation.SYSTEMTIME),
        ('SavedPartitionId', Guid),
        ('Library', Guid),
        ('Reserved', Guid),
        ('dwDeferDismountDelay', UInt32),
    ]
    return NTMS_DRIVEINFORMATIONA
def _define_NTMS_DRIVEINFORMATIONW_head():
    class NTMS_DRIVEINFORMATIONW(Structure):
        pass
    return NTMS_DRIVEINFORMATIONW
def _define_NTMS_DRIVEINFORMATIONW():
    NTMS_DRIVEINFORMATIONW = win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONW_head
    NTMS_DRIVEINFORMATIONW._fields_ = [
        ('Number', UInt32),
        ('State', win32more.Storage.FileSystem.NtmsDriveState),
        ('DriveType', Guid),
        ('szDeviceName', Char * 64),
        ('szSerialNumber', Char * 32),
        ('szRevision', Char * 32),
        ('ScsiPort', UInt16),
        ('ScsiBus', UInt16),
        ('ScsiTarget', UInt16),
        ('ScsiLun', UInt16),
        ('dwMountCount', UInt32),
        ('LastCleanedTs', win32more.Foundation.SYSTEMTIME),
        ('SavedPartitionId', Guid),
        ('Library', Guid),
        ('Reserved', Guid),
        ('dwDeferDismountDelay', UInt32),
    ]
    return NTMS_DRIVEINFORMATIONW
def _define_NTMS_DRIVETYPEINFORMATIONA_head():
    class NTMS_DRIVETYPEINFORMATIONA(Structure):
        pass
    return NTMS_DRIVETYPEINFORMATIONA
def _define_NTMS_DRIVETYPEINFORMATIONA():
    NTMS_DRIVETYPEINFORMATIONA = win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA_head
    NTMS_DRIVETYPEINFORMATIONA._fields_ = [
        ('szVendor', win32more.Foundation.CHAR * 128),
        ('szProduct', win32more.Foundation.CHAR * 128),
        ('NumberOfHeads', UInt32),
        ('DeviceType', win32more.Storage.FileSystem.FILE_DEVICE_TYPE),
    ]
    return NTMS_DRIVETYPEINFORMATIONA
def _define_NTMS_DRIVETYPEINFORMATIONW_head():
    class NTMS_DRIVETYPEINFORMATIONW(Structure):
        pass
    return NTMS_DRIVETYPEINFORMATIONW
def _define_NTMS_DRIVETYPEINFORMATIONW():
    NTMS_DRIVETYPEINFORMATIONW = win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW_head
    NTMS_DRIVETYPEINFORMATIONW._fields_ = [
        ('szVendor', Char * 128),
        ('szProduct', Char * 128),
        ('NumberOfHeads', UInt32),
        ('DeviceType', win32more.Storage.FileSystem.FILE_DEVICE_TYPE),
    ]
    return NTMS_DRIVETYPEINFORMATIONW
def _define_NTMS_FILESYSTEM_INFO_head():
    class NTMS_FILESYSTEM_INFO(Structure):
        pass
    return NTMS_FILESYSTEM_INFO
def _define_NTMS_FILESYSTEM_INFO():
    NTMS_FILESYSTEM_INFO = win32more.Storage.FileSystem.NTMS_FILESYSTEM_INFO_head
    NTMS_FILESYSTEM_INFO._fields_ = [
        ('FileSystemType', Char * 64),
        ('VolumeName', Char * 256),
        ('SerialNumber', UInt32),
    ]
    return NTMS_FILESYSTEM_INFO
def _define_NTMS_I1_LIBRARYINFORMATION_head():
    class NTMS_I1_LIBRARYINFORMATION(Structure):
        pass
    return NTMS_I1_LIBRARYINFORMATION
def _define_NTMS_I1_LIBRARYINFORMATION():
    NTMS_I1_LIBRARYINFORMATION = win32more.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION_head
    NTMS_I1_LIBRARYINFORMATION._fields_ = [
        ('LibraryType', UInt32),
        ('CleanerSlot', Guid),
        ('CleanerSlotDefault', Guid),
        ('LibrarySupportsDriveCleaning', win32more.Foundation.BOOL),
        ('BarCodeReaderInstalled', win32more.Foundation.BOOL),
        ('InventoryMethod', UInt32),
        ('dwCleanerUsesRemaining', UInt32),
        ('FirstDriveNumber', UInt32),
        ('dwNumberOfDrives', UInt32),
        ('FirstSlotNumber', UInt32),
        ('dwNumberOfSlots', UInt32),
        ('FirstDoorNumber', UInt32),
        ('dwNumberOfDoors', UInt32),
        ('FirstPortNumber', UInt32),
        ('dwNumberOfPorts', UInt32),
        ('FirstChangerNumber', UInt32),
        ('dwNumberOfChangers', UInt32),
        ('dwNumberOfMedia', UInt32),
        ('dwNumberOfMediaTypes', UInt32),
        ('dwNumberOfLibRequests', UInt32),
        ('Reserved', Guid),
    ]
    return NTMS_I1_LIBRARYINFORMATION
def _define_NTMS_I1_LIBREQUESTINFORMATIONA_head():
    class NTMS_I1_LIBREQUESTINFORMATIONA(Structure):
        pass
    return NTMS_I1_LIBREQUESTINFORMATIONA
def _define_NTMS_I1_LIBREQUESTINFORMATIONA():
    NTMS_I1_LIBREQUESTINFORMATIONA = win32more.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONA_head
    NTMS_I1_LIBREQUESTINFORMATIONA._fields_ = [
        ('OperationCode', UInt32),
        ('OperationOption', UInt32),
        ('State', UInt32),
        ('PartitionId', Guid),
        ('DriveId', Guid),
        ('PhysMediaId', Guid),
        ('Library', Guid),
        ('SlotId', Guid),
        ('TimeQueued', win32more.Foundation.SYSTEMTIME),
        ('TimeCompleted', win32more.Foundation.SYSTEMTIME),
        ('szApplication', win32more.Foundation.CHAR * 64),
        ('szUser', win32more.Foundation.CHAR * 64),
        ('szComputer', win32more.Foundation.CHAR * 64),
    ]
    return NTMS_I1_LIBREQUESTINFORMATIONA
def _define_NTMS_I1_LIBREQUESTINFORMATIONW_head():
    class NTMS_I1_LIBREQUESTINFORMATIONW(Structure):
        pass
    return NTMS_I1_LIBREQUESTINFORMATIONW
def _define_NTMS_I1_LIBREQUESTINFORMATIONW():
    NTMS_I1_LIBREQUESTINFORMATIONW = win32more.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONW_head
    NTMS_I1_LIBREQUESTINFORMATIONW._fields_ = [
        ('OperationCode', UInt32),
        ('OperationOption', UInt32),
        ('State', UInt32),
        ('PartitionId', Guid),
        ('DriveId', Guid),
        ('PhysMediaId', Guid),
        ('Library', Guid),
        ('SlotId', Guid),
        ('TimeQueued', win32more.Foundation.SYSTEMTIME),
        ('TimeCompleted', win32more.Foundation.SYSTEMTIME),
        ('szApplication', Char * 64),
        ('szUser', Char * 64),
        ('szComputer', Char * 64),
    ]
    return NTMS_I1_LIBREQUESTINFORMATIONW
def _define_NTMS_I1_OBJECTINFORMATIONA_head():
    class NTMS_I1_OBJECTINFORMATIONA(Structure):
        pass
    return NTMS_I1_OBJECTINFORMATIONA
def _define_NTMS_I1_OBJECTINFORMATIONA():
    NTMS_I1_OBJECTINFORMATIONA = win32more.Storage.FileSystem.NTMS_I1_OBJECTINFORMATIONA_head
    class NTMS_I1_OBJECTINFORMATIONA__Info_e__Union(Union):
        pass
    NTMS_I1_OBJECTINFORMATIONA__Info_e__Union._fields_ = [
        ('Drive', win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONA),
        ('DriveType', win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA),
        ('Library', win32more.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION),
        ('Changer', win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONA),
        ('ChangerType', win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA),
        ('StorageSlot', win32more.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION),
        ('IEDoor', win32more.Storage.FileSystem.NTMS_IEDOORINFORMATION),
        ('IEPort', win32more.Storage.FileSystem.NTMS_IEPORTINFORMATION),
        ('PhysicalMedia', win32more.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONA),
        ('LogicalMedia', win32more.Storage.FileSystem.NTMS_LMIDINFORMATION),
        ('Partition', win32more.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONA),
        ('MediaPool', win32more.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION),
        ('MediaType', win32more.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION),
        ('LibRequest', win32more.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONA),
        ('OpRequest', win32more.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONA),
    ]
    NTMS_I1_OBJECTINFORMATIONA._fields_ = [
        ('dwSize', UInt32),
        ('dwType', UInt32),
        ('Created', win32more.Foundation.SYSTEMTIME),
        ('Modified', win32more.Foundation.SYSTEMTIME),
        ('ObjectGuid', Guid),
        ('Enabled', win32more.Foundation.BOOL),
        ('dwOperationalState', UInt32),
        ('szName', win32more.Foundation.CHAR * 64),
        ('szDescription', win32more.Foundation.CHAR * 127),
        ('Info', NTMS_I1_OBJECTINFORMATIONA__Info_e__Union),
    ]
    return NTMS_I1_OBJECTINFORMATIONA
def _define_NTMS_I1_OBJECTINFORMATIONW_head():
    class NTMS_I1_OBJECTINFORMATIONW(Structure):
        pass
    return NTMS_I1_OBJECTINFORMATIONW
def _define_NTMS_I1_OBJECTINFORMATIONW():
    NTMS_I1_OBJECTINFORMATIONW = win32more.Storage.FileSystem.NTMS_I1_OBJECTINFORMATIONW_head
    class NTMS_I1_OBJECTINFORMATIONW__Info_e__Union(Union):
        pass
    NTMS_I1_OBJECTINFORMATIONW__Info_e__Union._fields_ = [
        ('Drive', win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONW),
        ('DriveType', win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW),
        ('Library', win32more.Storage.FileSystem.NTMS_I1_LIBRARYINFORMATION),
        ('Changer', win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONW),
        ('ChangerType', win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW),
        ('StorageSlot', win32more.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION),
        ('IEDoor', win32more.Storage.FileSystem.NTMS_IEDOORINFORMATION),
        ('IEPort', win32more.Storage.FileSystem.NTMS_IEPORTINFORMATION),
        ('PhysicalMedia', win32more.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONW),
        ('LogicalMedia', win32more.Storage.FileSystem.NTMS_LMIDINFORMATION),
        ('Partition', win32more.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONW),
        ('MediaPool', win32more.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION),
        ('MediaType', win32more.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION),
        ('LibRequest', win32more.Storage.FileSystem.NTMS_I1_LIBREQUESTINFORMATIONW),
        ('OpRequest', win32more.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONW),
    ]
    NTMS_I1_OBJECTINFORMATIONW._fields_ = [
        ('dwSize', UInt32),
        ('dwType', UInt32),
        ('Created', win32more.Foundation.SYSTEMTIME),
        ('Modified', win32more.Foundation.SYSTEMTIME),
        ('ObjectGuid', Guid),
        ('Enabled', win32more.Foundation.BOOL),
        ('dwOperationalState', UInt32),
        ('szName', Char * 64),
        ('szDescription', Char * 127),
        ('Info', NTMS_I1_OBJECTINFORMATIONW__Info_e__Union),
    ]
    return NTMS_I1_OBJECTINFORMATIONW
def _define_NTMS_I1_OPREQUESTINFORMATIONA_head():
    class NTMS_I1_OPREQUESTINFORMATIONA(Structure):
        pass
    return NTMS_I1_OPREQUESTINFORMATIONA
def _define_NTMS_I1_OPREQUESTINFORMATIONA():
    NTMS_I1_OPREQUESTINFORMATIONA = win32more.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONA_head
    NTMS_I1_OPREQUESTINFORMATIONA._fields_ = [
        ('Request', UInt32),
        ('Submitted', win32more.Foundation.SYSTEMTIME),
        ('State', UInt32),
        ('szMessage', win32more.Foundation.CHAR * 127),
        ('Arg1Type', UInt32),
        ('Arg1', Guid),
        ('Arg2Type', UInt32),
        ('Arg2', Guid),
        ('szApplication', win32more.Foundation.CHAR * 64),
        ('szUser', win32more.Foundation.CHAR * 64),
        ('szComputer', win32more.Foundation.CHAR * 64),
    ]
    return NTMS_I1_OPREQUESTINFORMATIONA
def _define_NTMS_I1_OPREQUESTINFORMATIONW_head():
    class NTMS_I1_OPREQUESTINFORMATIONW(Structure):
        pass
    return NTMS_I1_OPREQUESTINFORMATIONW
def _define_NTMS_I1_OPREQUESTINFORMATIONW():
    NTMS_I1_OPREQUESTINFORMATIONW = win32more.Storage.FileSystem.NTMS_I1_OPREQUESTINFORMATIONW_head
    NTMS_I1_OPREQUESTINFORMATIONW._fields_ = [
        ('Request', UInt32),
        ('Submitted', win32more.Foundation.SYSTEMTIME),
        ('State', UInt32),
        ('szMessage', Char * 127),
        ('Arg1Type', UInt32),
        ('Arg1', Guid),
        ('Arg2Type', UInt32),
        ('Arg2', Guid),
        ('szApplication', Char * 64),
        ('szUser', Char * 64),
        ('szComputer', Char * 64),
    ]
    return NTMS_I1_OPREQUESTINFORMATIONW
def _define_NTMS_I1_PARTITIONINFORMATIONA_head():
    class NTMS_I1_PARTITIONINFORMATIONA(Structure):
        pass
    return NTMS_I1_PARTITIONINFORMATIONA
def _define_NTMS_I1_PARTITIONINFORMATIONA():
    NTMS_I1_PARTITIONINFORMATIONA = win32more.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONA_head
    NTMS_I1_PARTITIONINFORMATIONA._fields_ = [
        ('PhysicalMedia', Guid),
        ('LogicalMedia', Guid),
        ('State', UInt32),
        ('Side', UInt16),
        ('dwOmidLabelIdLength', UInt32),
        ('OmidLabelId', Byte * 255),
        ('szOmidLabelType', win32more.Foundation.CHAR * 64),
        ('szOmidLabelInfo', win32more.Foundation.CHAR * 256),
        ('dwMountCount', UInt32),
        ('dwAllocateCount', UInt32),
    ]
    return NTMS_I1_PARTITIONINFORMATIONA
def _define_NTMS_I1_PARTITIONINFORMATIONW_head():
    class NTMS_I1_PARTITIONINFORMATIONW(Structure):
        pass
    return NTMS_I1_PARTITIONINFORMATIONW
def _define_NTMS_I1_PARTITIONINFORMATIONW():
    NTMS_I1_PARTITIONINFORMATIONW = win32more.Storage.FileSystem.NTMS_I1_PARTITIONINFORMATIONW_head
    NTMS_I1_PARTITIONINFORMATIONW._fields_ = [
        ('PhysicalMedia', Guid),
        ('LogicalMedia', Guid),
        ('State', UInt32),
        ('Side', UInt16),
        ('dwOmidLabelIdLength', UInt32),
        ('OmidLabelId', Byte * 255),
        ('szOmidLabelType', Char * 64),
        ('szOmidLabelInfo', Char * 256),
        ('dwMountCount', UInt32),
        ('dwAllocateCount', UInt32),
    ]
    return NTMS_I1_PARTITIONINFORMATIONW
def _define_NTMS_I1_PMIDINFORMATIONA_head():
    class NTMS_I1_PMIDINFORMATIONA(Structure):
        pass
    return NTMS_I1_PMIDINFORMATIONA
def _define_NTMS_I1_PMIDINFORMATIONA():
    NTMS_I1_PMIDINFORMATIONA = win32more.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONA_head
    NTMS_I1_PMIDINFORMATIONA._fields_ = [
        ('CurrentLibrary', Guid),
        ('MediaPool', Guid),
        ('Location', Guid),
        ('LocationType', UInt32),
        ('MediaType', Guid),
        ('HomeSlot', Guid),
        ('szBarCode', win32more.Foundation.CHAR * 64),
        ('BarCodeState', UInt32),
        ('szSequenceNumber', win32more.Foundation.CHAR * 32),
        ('MediaState', UInt32),
        ('dwNumberOfPartitions', UInt32),
    ]
    return NTMS_I1_PMIDINFORMATIONA
def _define_NTMS_I1_PMIDINFORMATIONW_head():
    class NTMS_I1_PMIDINFORMATIONW(Structure):
        pass
    return NTMS_I1_PMIDINFORMATIONW
def _define_NTMS_I1_PMIDINFORMATIONW():
    NTMS_I1_PMIDINFORMATIONW = win32more.Storage.FileSystem.NTMS_I1_PMIDINFORMATIONW_head
    NTMS_I1_PMIDINFORMATIONW._fields_ = [
        ('CurrentLibrary', Guid),
        ('MediaPool', Guid),
        ('Location', Guid),
        ('LocationType', UInt32),
        ('MediaType', Guid),
        ('HomeSlot', Guid),
        ('szBarCode', Char * 64),
        ('BarCodeState', UInt32),
        ('szSequenceNumber', Char * 32),
        ('MediaState', UInt32),
        ('dwNumberOfPartitions', UInt32),
    ]
    return NTMS_I1_PMIDINFORMATIONW
def _define_NTMS_IEDOORINFORMATION_head():
    class NTMS_IEDOORINFORMATION(Structure):
        pass
    return NTMS_IEDOORINFORMATION
def _define_NTMS_IEDOORINFORMATION():
    NTMS_IEDOORINFORMATION = win32more.Storage.FileSystem.NTMS_IEDOORINFORMATION_head
    NTMS_IEDOORINFORMATION._fields_ = [
        ('Number', UInt32),
        ('State', win32more.Storage.FileSystem.NtmsDoorState),
        ('MaxOpenSecs', UInt16),
        ('Library', Guid),
    ]
    return NTMS_IEDOORINFORMATION
def _define_NTMS_IEPORTINFORMATION_head():
    class NTMS_IEPORTINFORMATION(Structure):
        pass
    return NTMS_IEPORTINFORMATION
def _define_NTMS_IEPORTINFORMATION():
    NTMS_IEPORTINFORMATION = win32more.Storage.FileSystem.NTMS_IEPORTINFORMATION_head
    NTMS_IEPORTINFORMATION._fields_ = [
        ('Number', UInt32),
        ('Content', win32more.Storage.FileSystem.NtmsPortContent),
        ('Position', win32more.Storage.FileSystem.NtmsPortPosition),
        ('MaxExtendSecs', UInt16),
        ('Library', Guid),
    ]
    return NTMS_IEPORTINFORMATION
def _define_NTMS_LIBRARYINFORMATION_head():
    class NTMS_LIBRARYINFORMATION(Structure):
        pass
    return NTMS_LIBRARYINFORMATION
def _define_NTMS_LIBRARYINFORMATION():
    NTMS_LIBRARYINFORMATION = win32more.Storage.FileSystem.NTMS_LIBRARYINFORMATION_head
    NTMS_LIBRARYINFORMATION._fields_ = [
        ('LibraryType', win32more.Storage.FileSystem.NtmsLibraryType),
        ('CleanerSlot', Guid),
        ('CleanerSlotDefault', Guid),
        ('LibrarySupportsDriveCleaning', win32more.Foundation.BOOL),
        ('BarCodeReaderInstalled', win32more.Foundation.BOOL),
        ('InventoryMethod', win32more.Storage.FileSystem.NtmsInventoryMethod),
        ('dwCleanerUsesRemaining', UInt32),
        ('FirstDriveNumber', UInt32),
        ('dwNumberOfDrives', UInt32),
        ('FirstSlotNumber', UInt32),
        ('dwNumberOfSlots', UInt32),
        ('FirstDoorNumber', UInt32),
        ('dwNumberOfDoors', UInt32),
        ('FirstPortNumber', UInt32),
        ('dwNumberOfPorts', UInt32),
        ('FirstChangerNumber', UInt32),
        ('dwNumberOfChangers', UInt32),
        ('dwNumberOfMedia', UInt32),
        ('dwNumberOfMediaTypes', UInt32),
        ('dwNumberOfLibRequests', UInt32),
        ('Reserved', Guid),
        ('AutoRecovery', win32more.Foundation.BOOL),
        ('dwFlags', win32more.Storage.FileSystem.NtmsLibraryFlags),
    ]
    return NTMS_LIBRARYINFORMATION
def _define_NTMS_LIBREQUESTINFORMATIONA_head():
    class NTMS_LIBREQUESTINFORMATIONA(Structure):
        pass
    return NTMS_LIBREQUESTINFORMATIONA
def _define_NTMS_LIBREQUESTINFORMATIONA():
    NTMS_LIBREQUESTINFORMATIONA = win32more.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONA_head
    NTMS_LIBREQUESTINFORMATIONA._fields_ = [
        ('OperationCode', win32more.Storage.FileSystem.NtmsLmOperation),
        ('OperationOption', UInt32),
        ('State', win32more.Storage.FileSystem.NtmsLmState),
        ('PartitionId', Guid),
        ('DriveId', Guid),
        ('PhysMediaId', Guid),
        ('Library', Guid),
        ('SlotId', Guid),
        ('TimeQueued', win32more.Foundation.SYSTEMTIME),
        ('TimeCompleted', win32more.Foundation.SYSTEMTIME),
        ('szApplication', win32more.Foundation.CHAR * 64),
        ('szUser', win32more.Foundation.CHAR * 64),
        ('szComputer', win32more.Foundation.CHAR * 64),
        ('dwErrorCode', UInt32),
        ('WorkItemId', Guid),
        ('dwPriority', UInt32),
    ]
    return NTMS_LIBREQUESTINFORMATIONA
def _define_NTMS_LIBREQUESTINFORMATIONW_head():
    class NTMS_LIBREQUESTINFORMATIONW(Structure):
        pass
    return NTMS_LIBREQUESTINFORMATIONW
def _define_NTMS_LIBREQUESTINFORMATIONW():
    NTMS_LIBREQUESTINFORMATIONW = win32more.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONW_head
    NTMS_LIBREQUESTINFORMATIONW._fields_ = [
        ('OperationCode', win32more.Storage.FileSystem.NtmsLmOperation),
        ('OperationOption', UInt32),
        ('State', win32more.Storage.FileSystem.NtmsLmState),
        ('PartitionId', Guid),
        ('DriveId', Guid),
        ('PhysMediaId', Guid),
        ('Library', Guid),
        ('SlotId', Guid),
        ('TimeQueued', win32more.Foundation.SYSTEMTIME),
        ('TimeCompleted', win32more.Foundation.SYSTEMTIME),
        ('szApplication', Char * 64),
        ('szUser', Char * 64),
        ('szComputer', Char * 64),
        ('dwErrorCode', UInt32),
        ('WorkItemId', Guid),
        ('dwPriority', UInt32),
    ]
    return NTMS_LIBREQUESTINFORMATIONW
def _define_NTMS_LMIDINFORMATION_head():
    class NTMS_LMIDINFORMATION(Structure):
        pass
    return NTMS_LMIDINFORMATION
def _define_NTMS_LMIDINFORMATION():
    NTMS_LMIDINFORMATION = win32more.Storage.FileSystem.NTMS_LMIDINFORMATION_head
    NTMS_LMIDINFORMATION._fields_ = [
        ('MediaPool', Guid),
        ('dwNumberOfPartitions', UInt32),
    ]
    return NTMS_LMIDINFORMATION
def _define_NTMS_MEDIAPOOLINFORMATION_head():
    class NTMS_MEDIAPOOLINFORMATION(Structure):
        pass
    return NTMS_MEDIAPOOLINFORMATION
def _define_NTMS_MEDIAPOOLINFORMATION():
    NTMS_MEDIAPOOLINFORMATION = win32more.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION_head
    NTMS_MEDIAPOOLINFORMATION._fields_ = [
        ('PoolType', UInt32),
        ('MediaType', Guid),
        ('Parent', Guid),
        ('AllocationPolicy', UInt32),
        ('DeallocationPolicy', UInt32),
        ('dwMaxAllocates', UInt32),
        ('dwNumberOfPhysicalMedia', UInt32),
        ('dwNumberOfLogicalMedia', UInt32),
        ('dwNumberOfMediaPools', UInt32),
    ]
    return NTMS_MEDIAPOOLINFORMATION
def _define_NTMS_MEDIATYPEINFORMATION_head():
    class NTMS_MEDIATYPEINFORMATION(Structure):
        pass
    return NTMS_MEDIATYPEINFORMATION
def _define_NTMS_MEDIATYPEINFORMATION():
    NTMS_MEDIATYPEINFORMATION = win32more.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION_head
    NTMS_MEDIATYPEINFORMATION._fields_ = [
        ('MediaType', UInt32),
        ('NumberOfSides', UInt32),
        ('ReadWriteCharacteristics', win32more.Storage.FileSystem.NtmsReadWriteCharacteristics),
        ('DeviceType', win32more.Storage.FileSystem.FILE_DEVICE_TYPE),
    ]
    return NTMS_MEDIATYPEINFORMATION
def _define_NTMS_MOUNT_INFORMATION_head():
    class NTMS_MOUNT_INFORMATION(Structure):
        pass
    return NTMS_MOUNT_INFORMATION
def _define_NTMS_MOUNT_INFORMATION():
    NTMS_MOUNT_INFORMATION = win32more.Storage.FileSystem.NTMS_MOUNT_INFORMATION_head
    NTMS_MOUNT_INFORMATION._fields_ = [
        ('dwSize', UInt32),
        ('lpReserved', c_void_p),
    ]
    return NTMS_MOUNT_INFORMATION
def _define_NTMS_NOTIFICATIONINFORMATION_head():
    class NTMS_NOTIFICATIONINFORMATION(Structure):
        pass
    return NTMS_NOTIFICATIONINFORMATION
def _define_NTMS_NOTIFICATIONINFORMATION():
    NTMS_NOTIFICATIONINFORMATION = win32more.Storage.FileSystem.NTMS_NOTIFICATIONINFORMATION_head
    NTMS_NOTIFICATIONINFORMATION._fields_ = [
        ('dwOperation', win32more.Storage.FileSystem.NtmsNotificationOperations),
        ('ObjectId', Guid),
    ]
    return NTMS_NOTIFICATIONINFORMATION
def _define_NTMS_OBJECTINFORMATIONA_head():
    class NTMS_OBJECTINFORMATIONA(Structure):
        pass
    return NTMS_OBJECTINFORMATIONA
def _define_NTMS_OBJECTINFORMATIONA():
    NTMS_OBJECTINFORMATIONA = win32more.Storage.FileSystem.NTMS_OBJECTINFORMATIONA_head
    class NTMS_OBJECTINFORMATIONA__Info_e__Union(Union):
        pass
    NTMS_OBJECTINFORMATIONA__Info_e__Union._fields_ = [
        ('Drive', win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONA),
        ('DriveType', win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONA),
        ('Library', win32more.Storage.FileSystem.NTMS_LIBRARYINFORMATION),
        ('Changer', win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONA),
        ('ChangerType', win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONA),
        ('StorageSlot', win32more.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION),
        ('IEDoor', win32more.Storage.FileSystem.NTMS_IEDOORINFORMATION),
        ('IEPort', win32more.Storage.FileSystem.NTMS_IEPORTINFORMATION),
        ('PhysicalMedia', win32more.Storage.FileSystem.NTMS_PMIDINFORMATIONA),
        ('LogicalMedia', win32more.Storage.FileSystem.NTMS_LMIDINFORMATION),
        ('Partition', win32more.Storage.FileSystem.NTMS_PARTITIONINFORMATIONA),
        ('MediaPool', win32more.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION),
        ('MediaType', win32more.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION),
        ('LibRequest', win32more.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONA),
        ('OpRequest', win32more.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONA),
        ('Computer', win32more.Storage.FileSystem.NTMS_COMPUTERINFORMATION),
    ]
    NTMS_OBJECTINFORMATIONA._fields_ = [
        ('dwSize', UInt32),
        ('dwType', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Created', win32more.Foundation.SYSTEMTIME),
        ('Modified', win32more.Foundation.SYSTEMTIME),
        ('ObjectGuid', Guid),
        ('Enabled', win32more.Foundation.BOOL),
        ('dwOperationalState', win32more.Storage.FileSystem.NtmsOperationalState),
        ('szName', win32more.Foundation.CHAR * 64),
        ('szDescription', win32more.Foundation.CHAR * 127),
        ('Info', NTMS_OBJECTINFORMATIONA__Info_e__Union),
    ]
    return NTMS_OBJECTINFORMATIONA
def _define_NTMS_OBJECTINFORMATIONW_head():
    class NTMS_OBJECTINFORMATIONW(Structure):
        pass
    return NTMS_OBJECTINFORMATIONW
def _define_NTMS_OBJECTINFORMATIONW():
    NTMS_OBJECTINFORMATIONW = win32more.Storage.FileSystem.NTMS_OBJECTINFORMATIONW_head
    class NTMS_OBJECTINFORMATIONW__Info_e__Union(Union):
        pass
    NTMS_OBJECTINFORMATIONW__Info_e__Union._fields_ = [
        ('Drive', win32more.Storage.FileSystem.NTMS_DRIVEINFORMATIONW),
        ('DriveType', win32more.Storage.FileSystem.NTMS_DRIVETYPEINFORMATIONW),
        ('Library', win32more.Storage.FileSystem.NTMS_LIBRARYINFORMATION),
        ('Changer', win32more.Storage.FileSystem.NTMS_CHANGERINFORMATIONW),
        ('ChangerType', win32more.Storage.FileSystem.NTMS_CHANGERTYPEINFORMATIONW),
        ('StorageSlot', win32more.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION),
        ('IEDoor', win32more.Storage.FileSystem.NTMS_IEDOORINFORMATION),
        ('IEPort', win32more.Storage.FileSystem.NTMS_IEPORTINFORMATION),
        ('PhysicalMedia', win32more.Storage.FileSystem.NTMS_PMIDINFORMATIONW),
        ('LogicalMedia', win32more.Storage.FileSystem.NTMS_LMIDINFORMATION),
        ('Partition', win32more.Storage.FileSystem.NTMS_PARTITIONINFORMATIONW),
        ('MediaPool', win32more.Storage.FileSystem.NTMS_MEDIAPOOLINFORMATION),
        ('MediaType', win32more.Storage.FileSystem.NTMS_MEDIATYPEINFORMATION),
        ('LibRequest', win32more.Storage.FileSystem.NTMS_LIBREQUESTINFORMATIONW),
        ('OpRequest', win32more.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONW),
        ('Computer', win32more.Storage.FileSystem.NTMS_COMPUTERINFORMATION),
    ]
    NTMS_OBJECTINFORMATIONW._fields_ = [
        ('dwSize', UInt32),
        ('dwType', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Created', win32more.Foundation.SYSTEMTIME),
        ('Modified', win32more.Foundation.SYSTEMTIME),
        ('ObjectGuid', Guid),
        ('Enabled', win32more.Foundation.BOOL),
        ('dwOperationalState', win32more.Storage.FileSystem.NtmsOperationalState),
        ('szName', Char * 64),
        ('szDescription', Char * 127),
        ('Info', NTMS_OBJECTINFORMATIONW__Info_e__Union),
    ]
    return NTMS_OBJECTINFORMATIONW
NTMS_OMID_TYPE = UInt32
NTMS_OMID_TYPE_FILESYSTEM_INFO = 2
NTMS_OMID_TYPE_RAW_LABEL = 1
def _define_NTMS_OPREQUESTINFORMATIONA_head():
    class NTMS_OPREQUESTINFORMATIONA(Structure):
        pass
    return NTMS_OPREQUESTINFORMATIONA
def _define_NTMS_OPREQUESTINFORMATIONA():
    NTMS_OPREQUESTINFORMATIONA = win32more.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONA_head
    NTMS_OPREQUESTINFORMATIONA._fields_ = [
        ('Request', win32more.Storage.FileSystem.NtmsOpreqCommand),
        ('Submitted', win32more.Foundation.SYSTEMTIME),
        ('State', win32more.Storage.FileSystem.NtmsOpreqState),
        ('szMessage', win32more.Foundation.CHAR * 256),
        ('Arg1Type', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Arg1', Guid),
        ('Arg2Type', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Arg2', Guid),
        ('szApplication', win32more.Foundation.CHAR * 64),
        ('szUser', win32more.Foundation.CHAR * 64),
        ('szComputer', win32more.Foundation.CHAR * 64),
    ]
    return NTMS_OPREQUESTINFORMATIONA
def _define_NTMS_OPREQUESTINFORMATIONW_head():
    class NTMS_OPREQUESTINFORMATIONW(Structure):
        pass
    return NTMS_OPREQUESTINFORMATIONW
def _define_NTMS_OPREQUESTINFORMATIONW():
    NTMS_OPREQUESTINFORMATIONW = win32more.Storage.FileSystem.NTMS_OPREQUESTINFORMATIONW_head
    NTMS_OPREQUESTINFORMATIONW._fields_ = [
        ('Request', win32more.Storage.FileSystem.NtmsOpreqCommand),
        ('Submitted', win32more.Foundation.SYSTEMTIME),
        ('State', win32more.Storage.FileSystem.NtmsOpreqState),
        ('szMessage', Char * 256),
        ('Arg1Type', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Arg1', Guid),
        ('Arg2Type', win32more.Storage.FileSystem.NtmsObjectsTypes),
        ('Arg2', Guid),
        ('szApplication', Char * 64),
        ('szUser', Char * 64),
        ('szComputer', Char * 64),
    ]
    return NTMS_OPREQUESTINFORMATIONW
def _define_NTMS_PARTITIONINFORMATIONA_head():
    class NTMS_PARTITIONINFORMATIONA(Structure):
        pass
    return NTMS_PARTITIONINFORMATIONA
def _define_NTMS_PARTITIONINFORMATIONA():
    NTMS_PARTITIONINFORMATIONA = win32more.Storage.FileSystem.NTMS_PARTITIONINFORMATIONA_head
    NTMS_PARTITIONINFORMATIONA._fields_ = [
        ('PhysicalMedia', Guid),
        ('LogicalMedia', Guid),
        ('State', win32more.Storage.FileSystem.NtmsPartitionState),
        ('Side', UInt16),
        ('dwOmidLabelIdLength', UInt32),
        ('OmidLabelId', Byte * 255),
        ('szOmidLabelType', win32more.Foundation.CHAR * 64),
        ('szOmidLabelInfo', win32more.Foundation.CHAR * 256),
        ('dwMountCount', UInt32),
        ('dwAllocateCount', UInt32),
        ('Capacity', win32more.Foundation.LARGE_INTEGER),
    ]
    return NTMS_PARTITIONINFORMATIONA
def _define_NTMS_PARTITIONINFORMATIONW_head():
    class NTMS_PARTITIONINFORMATIONW(Structure):
        pass
    return NTMS_PARTITIONINFORMATIONW
def _define_NTMS_PARTITIONINFORMATIONW():
    NTMS_PARTITIONINFORMATIONW = win32more.Storage.FileSystem.NTMS_PARTITIONINFORMATIONW_head
    NTMS_PARTITIONINFORMATIONW._fields_ = [
        ('PhysicalMedia', Guid),
        ('LogicalMedia', Guid),
        ('State', win32more.Storage.FileSystem.NtmsPartitionState),
        ('Side', UInt16),
        ('dwOmidLabelIdLength', UInt32),
        ('OmidLabelId', Byte * 255),
        ('szOmidLabelType', Char * 64),
        ('szOmidLabelInfo', Char * 256),
        ('dwMountCount', UInt32),
        ('dwAllocateCount', UInt32),
        ('Capacity', win32more.Foundation.LARGE_INTEGER),
    ]
    return NTMS_PARTITIONINFORMATIONW
def _define_NTMS_PMIDINFORMATIONA_head():
    class NTMS_PMIDINFORMATIONA(Structure):
        pass
    return NTMS_PMIDINFORMATIONA
def _define_NTMS_PMIDINFORMATIONA():
    NTMS_PMIDINFORMATIONA = win32more.Storage.FileSystem.NTMS_PMIDINFORMATIONA_head
    NTMS_PMIDINFORMATIONA._fields_ = [
        ('CurrentLibrary', Guid),
        ('MediaPool', Guid),
        ('Location', Guid),
        ('LocationType', UInt32),
        ('MediaType', Guid),
        ('HomeSlot', Guid),
        ('szBarCode', win32more.Foundation.CHAR * 64),
        ('BarCodeState', win32more.Storage.FileSystem.NtmsBarCodeState),
        ('szSequenceNumber', win32more.Foundation.CHAR * 32),
        ('MediaState', win32more.Storage.FileSystem.NtmsMediaState),
        ('dwNumberOfPartitions', UInt32),
        ('dwMediaTypeCode', UInt32),
        ('dwDensityCode', UInt32),
        ('MountedPartition', Guid),
    ]
    return NTMS_PMIDINFORMATIONA
def _define_NTMS_PMIDINFORMATIONW_head():
    class NTMS_PMIDINFORMATIONW(Structure):
        pass
    return NTMS_PMIDINFORMATIONW
def _define_NTMS_PMIDINFORMATIONW():
    NTMS_PMIDINFORMATIONW = win32more.Storage.FileSystem.NTMS_PMIDINFORMATIONW_head
    NTMS_PMIDINFORMATIONW._fields_ = [
        ('CurrentLibrary', Guid),
        ('MediaPool', Guid),
        ('Location', Guid),
        ('LocationType', UInt32),
        ('MediaType', Guid),
        ('HomeSlot', Guid),
        ('szBarCode', Char * 64),
        ('BarCodeState', win32more.Storage.FileSystem.NtmsBarCodeState),
        ('szSequenceNumber', Char * 32),
        ('MediaState', win32more.Storage.FileSystem.NtmsMediaState),
        ('dwNumberOfPartitions', UInt32),
        ('dwMediaTypeCode', UInt32),
        ('dwDensityCode', UInt32),
        ('MountedPartition', Guid),
    ]
    return NTMS_PMIDINFORMATIONW
def _define_NTMS_STORAGESLOTINFORMATION_head():
    class NTMS_STORAGESLOTINFORMATION(Structure):
        pass
    return NTMS_STORAGESLOTINFORMATION
def _define_NTMS_STORAGESLOTINFORMATION():
    NTMS_STORAGESLOTINFORMATION = win32more.Storage.FileSystem.NTMS_STORAGESLOTINFORMATION_head
    NTMS_STORAGESLOTINFORMATION._fields_ = [
        ('Number', UInt32),
        ('State', UInt32),
        ('Library', Guid),
    ]
    return NTMS_STORAGESLOTINFORMATION
NtmsAccessMask = Int32
NTMS_USE_ACCESS = 1
NTMS_MODIFY_ACCESS = 2
NTMS_CONTROL_ACCESS = 4
NtmsAllocateOptions = Int32
NTMS_ALLOCATE_NEW = 1
NTMS_ALLOCATE_NEXT = 2
NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE = 4
NtmsAllocationPolicy = Int32
NTMS_ALLOCATE_FROMSCRATCH = 1
NtmsAsyncOperations = Int32
NTMS_ASYNCOP_MOUNT = 1
NtmsAsyncStatus = Int32
NTMS_ASYNCSTATE_QUEUED = 0
NTMS_ASYNCSTATE_WAIT_RESOURCE = 1
NTMS_ASYNCSTATE_WAIT_OPERATOR = 2
NTMS_ASYNCSTATE_INPROCESS = 3
NTMS_ASYNCSTATE_COMPLETE = 4
NtmsBarCodeState = Int32
NTMS_BARCODESTATE_OK = 1
NTMS_BARCODESTATE_UNREADABLE = 2
NtmsCreateNtmsMediaOptions = Int32
NTMS_ERROR_ON_DUPLICATE = 1
NtmsCreateOptions = Int32
NTMS_OPEN_EXISTING = 1
NTMS_CREATE_NEW = 2
NTMS_OPEN_ALWAYS = 3
NtmsDeallocationPolicy = Int32
NTMS_DEALLOCATE_TOSCRATCH = 1
NtmsDismountOptions = Int32
NTMS_DISMOUNT_DEFERRED = 1
NTMS_DISMOUNT_IMMEDIATE = 2
NtmsDoorState = Int32
NTMS_DOORSTATE_UNKNOWN = 0
NTMS_DOORSTATE_CLOSED = 1
NTMS_DOORSTATE_OPEN = 2
NtmsDriveState = Int32
NTMS_DRIVESTATE_DISMOUNTED = 0
NTMS_DRIVESTATE_MOUNTED = 1
NTMS_DRIVESTATE_LOADED = 2
NTMS_DRIVESTATE_UNLOADED = 5
NTMS_DRIVESTATE_BEING_CLEANED = 6
NTMS_DRIVESTATE_DISMOUNTABLE = 7
NtmsDriveType = Int32
NTMS_UNKNOWN_DRIVE = 0
NtmsEjectOperation = Int32
NTMS_EJECT_START = 0
NTMS_EJECT_STOP = 1
NTMS_EJECT_QUEUE = 2
NTMS_EJECT_FORCE = 3
NTMS_EJECT_IMMEDIATE = 4
NTMS_EJECT_ASK_USER = 5
NtmsEnumerateOption = Int32
NTMS_ENUM_DEFAULT = 0
NTMS_ENUM_ROOTPOOL = 1
NtmsInjectOperation = Int32
NTMS_INJECT_START = 0
NTMS_INJECT_STOP = 1
NTMS_INJECT_RETRACT = 2
NTMS_INJECT_STARTMANY = 3
NtmsInventoryMethod = Int32
NTMS_INVENTORY_NONE = 0
NTMS_INVENTORY_FAST = 1
NTMS_INVENTORY_OMID = 2
NTMS_INVENTORY_DEFAULT = 3
NTMS_INVENTORY_SLOT = 4
NTMS_INVENTORY_STOP = 5
NTMS_INVENTORY_MAX = 6
NtmsLibraryFlags = Int32
NTMS_LIBRARYFLAG_FIXEDOFFLINE = 1
NTMS_LIBRARYFLAG_CLEANERPRESENT = 2
NTMS_LIBRARYFLAG_AUTODETECTCHANGE = 4
NTMS_LIBRARYFLAG_IGNORECLEANERUSESREMAINING = 8
NTMS_LIBRARYFLAG_RECOGNIZECLEANERBARCODE = 16
NtmsLibraryType = Int32
NTMS_LIBRARYTYPE_UNKNOWN = 0
NTMS_LIBRARYTYPE_OFFLINE = 1
NTMS_LIBRARYTYPE_ONLINE = 2
NTMS_LIBRARYTYPE_STANDALONE = 3
NtmsLibRequestFlags = Int32
NTMS_LIBREQFLAGS_NOAUTOPURGE = 1
NTMS_LIBREQFLAGS_NOFAILEDPURGE = 2
NtmsLmOperation = Int32
NTMS_LM_REMOVE = 0
NTMS_LM_DISABLECHANGER = 1
NTMS_LM_DISABLELIBRARY = 1
NTMS_LM_ENABLECHANGER = 2
NTMS_LM_ENABLELIBRARY = 2
NTMS_LM_DISABLEDRIVE = 3
NTMS_LM_ENABLEDRIVE = 4
NTMS_LM_DISABLEMEDIA = 5
NTMS_LM_ENABLEMEDIA = 6
NTMS_LM_UPDATEOMID = 7
NTMS_LM_INVENTORY = 8
NTMS_LM_DOORACCESS = 9
NTMS_LM_EJECT = 10
NTMS_LM_EJECTCLEANER = 11
NTMS_LM_INJECT = 12
NTMS_LM_INJECTCLEANER = 13
NTMS_LM_PROCESSOMID = 14
NTMS_LM_CLEANDRIVE = 15
NTMS_LM_DISMOUNT = 16
NTMS_LM_MOUNT = 17
NTMS_LM_WRITESCRATCH = 18
NTMS_LM_CLASSIFY = 19
NTMS_LM_RESERVECLEANER = 20
NTMS_LM_RELEASECLEANER = 21
NTMS_LM_MAXWORKITEM = 22
NtmsLmState = Int32
NTMS_LM_QUEUED = 0
NTMS_LM_INPROCESS = 1
NTMS_LM_PASSED = 2
NTMS_LM_FAILED = 3
NTMS_LM_INVALID = 4
NTMS_LM_WAITING = 5
NTMS_LM_DEFERRED = 6
NTMS_LM_DEFFERED = 6
NTMS_LM_CANCELLED = 7
NTMS_LM_STOPPED = 8
NtmsMediaPoolPolicy = Int32
NTMS_POOLPOLICY_PURGEOFFLINESCRATCH = 1
NTMS_POOLPOLICY_KEEPOFFLINEIMPORT = 2
NtmsMediaState = Int32
NTMS_MEDIASTATE_IDLE = 0
NTMS_MEDIASTATE_INUSE = 1
NTMS_MEDIASTATE_MOUNTED = 2
NTMS_MEDIASTATE_LOADED = 3
NTMS_MEDIASTATE_UNLOADED = 4
NTMS_MEDIASTATE_OPERROR = 5
NTMS_MEDIASTATE_OPREQ = 6
NtmsMountOptions = Int32
NTMS_MOUNT_READ = 1
NTMS_MOUNT_WRITE = 2
NTMS_MOUNT_ERROR_NOT_AVAILABLE = 4
NTMS_MOUNT_ERROR_IF_UNAVAILABLE = 4
NTMS_MOUNT_ERROR_OFFLINE = 8
NTMS_MOUNT_ERROR_IF_OFFLINE = 8
NTMS_MOUNT_SPECIFIC_DRIVE = 16
NTMS_MOUNT_NOWAIT = 32
NtmsMountPriority = Int32
NTMS_PRIORITY_DEFAULT = 0
NTMS_PRIORITY_HIGHEST = 15
NTMS_PRIORITY_HIGH = 7
NTMS_PRIORITY_NORMAL = 0
NTMS_PRIORITY_LOW = -7
NTMS_PRIORITY_LOWEST = -15
NtmsNotificationOperations = Int32
NTMS_OBJ_UPDATE = 1
NTMS_OBJ_INSERT = 2
NTMS_OBJ_DELETE = 3
NTMS_EVENT_SIGNAL = 4
NTMS_EVENT_COMPLETE = 5
NtmsObjectsTypes = Int32
NTMS_UNKNOWN = 0
NTMS_OBJECT = 1
NTMS_CHANGER = 2
NTMS_CHANGER_TYPE = 3
NTMS_COMPUTER = 4
NTMS_DRIVE = 5
NTMS_DRIVE_TYPE = 6
NTMS_IEDOOR = 7
NTMS_IEPORT = 8
NTMS_LIBRARY = 9
NTMS_LIBREQUEST = 10
NTMS_LOGICAL_MEDIA = 11
NTMS_MEDIA_POOL = 12
NTMS_MEDIA_TYPE = 13
NTMS_PARTITION = 14
NTMS_PHYSICAL_MEDIA = 15
NTMS_STORAGESLOT = 16
NTMS_OPREQUEST = 17
NTMS_UI_DESTINATION = 18
NTMS_NUMBER_OF_OBJECT_TYPES = 19
NtmsOperationalState = Int32
NTMS_READY = 0
NTMS_INITIALIZING = 10
NTMS_NEEDS_SERVICE = 20
NTMS_NOT_PRESENT = 21
NtmsOpreqCommand = Int32
NTMS_OPREQ_UNKNOWN = 0
NTMS_OPREQ_NEWMEDIA = 1
NTMS_OPREQ_CLEANER = 2
NTMS_OPREQ_DEVICESERVICE = 3
NTMS_OPREQ_MOVEMEDIA = 4
NTMS_OPREQ_MESSAGE = 5
NtmsOpreqState = Int32
NTMS_OPSTATE_UNKNOWN = 0
NTMS_OPSTATE_SUBMITTED = 1
NTMS_OPSTATE_ACTIVE = 2
NTMS_OPSTATE_INPROGRESS = 3
NTMS_OPSTATE_REFUSED = 4
NTMS_OPSTATE_COMPLETE = 5
NtmsOpRequestFlags = Int32
NTMS_OPREQFLAGS_NOAUTOPURGE = 1
NTMS_OPREQFLAGS_NOFAILEDPURGE = 2
NTMS_OPREQFLAGS_NOALERTS = 16
NTMS_OPREQFLAGS_NOTRAYICON = 32
NtmsPartitionState = Int32
NTMS_PARTSTATE_UNKNOWN = 0
NTMS_PARTSTATE_UNPREPARED = 1
NTMS_PARTSTATE_INCOMPATIBLE = 2
NTMS_PARTSTATE_DECOMMISSIONED = 3
NTMS_PARTSTATE_AVAILABLE = 4
NTMS_PARTSTATE_ALLOCATED = 5
NTMS_PARTSTATE_COMPLETE = 6
NTMS_PARTSTATE_FOREIGN = 7
NTMS_PARTSTATE_IMPORT = 8
NTMS_PARTSTATE_RESERVED = 9
NtmsPoolType = Int32
NTMS_POOLTYPE_UNKNOWN = 0
NTMS_POOLTYPE_SCRATCH = 1
NTMS_POOLTYPE_FOREIGN = 2
NTMS_POOLTYPE_IMPORT = 3
NTMS_POOLTYPE_APPLICATION = 1000
NtmsPortContent = Int32
NTMS_PORTCONTENT_UNKNOWN = 0
NTMS_PORTCONTENT_FULL = 1
NTMS_PORTCONTENT_EMPTY = 2
NtmsPortPosition = Int32
NTMS_PORTPOSITION_UNKNOWN = 0
NTMS_PORTPOSITION_EXTENDED = 1
NTMS_PORTPOSITION_RETRACTED = 2
NtmsReadWriteCharacteristics = Int32
NTMS_MEDIARW_UNKNOWN = 0
NTMS_MEDIARW_REWRITABLE = 1
NTMS_MEDIARW_WRITEONCE = 2
NTMS_MEDIARW_READONLY = 3
NtmsSessionOptions = Int32
NTMS_SESSION_QUERYEXPEDITE = 1
NtmsSlotState = Int32
NTMS_SLOTSTATE_UNKNOWN = 0
NTMS_SLOTSTATE_FULL = 1
NTMS_SLOTSTATE_EMPTY = 2
NTMS_SLOTSTATE_NOTPRESENT = 3
NTMS_SLOTSTATE_NEEDSINVENTORY = 4
NtmsUIOperations = Int32
NTMS_UIDEST_ADD = 1
NTMS_UIDEST_DELETE = 2
NTMS_UIDEST_DELETEALL = 3
NTMS_UIOPERATION_MAX = 4
NtmsUITypes = Int32
NTMS_UITYPE_INVALID = 0
NTMS_UITYPE_INFO = 1
NTMS_UITYPE_REQ = 2
NTMS_UITYPE_ERR = 3
NTMS_UITYPE_MAX = 4
def _define_OFSTRUCT_head():
    class OFSTRUCT(Structure):
        pass
    return OFSTRUCT
def _define_OFSTRUCT():
    OFSTRUCT = win32more.Storage.FileSystem.OFSTRUCT_head
    OFSTRUCT._fields_ = [
        ('cBytes', Byte),
        ('fFixedDisk', Byte),
        ('nErrCode', UInt16),
        ('Reserved1', UInt16),
        ('Reserved2', UInt16),
        ('szPathName', win32more.Foundation.CHAR * 128),
    ]
    return OFSTRUCT
def _define_PCLFS_COMPLETION_ROUTINE():
    return WINFUNCTYPE(Void,c_void_p,UInt32)
def _define_PCOPYFILE2_PROGRESS_ROUTINE():
    return WINFUNCTYPE(win32more.Storage.FileSystem.COPYFILE2_MESSAGE_ACTION,POINTER(win32more.Storage.FileSystem.COPYFILE2_MESSAGE_head),c_void_p)
def _define_PFE_EXPORT_FUNC():
    return WINFUNCTYPE(UInt32,c_char_p_no,c_void_p,UInt32)
def _define_PFE_IMPORT_FUNC():
    return WINFUNCTYPE(UInt32,c_char_p_no,c_void_p,POINTER(UInt32))
def _define_PFN_IO_COMPLETION():
    return WINFUNCTYPE(Void,POINTER(win32more.Storage.FileSystem.FIO_CONTEXT_head),POINTER(win32more.Storage.FileSystem.FH_OVERLAPPED_head),UInt32,UInt32)
def _define_PLOG_FULL_HANDLER_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,UInt32,win32more.Foundation.BOOL,c_void_p)
def _define_PLOG_TAIL_ADVANCE_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,win32more.Storage.FileSystem.CLS_LSN,c_void_p)
def _define_PLOG_UNPINNED_CALLBACK():
    return WINFUNCTYPE(Void,win32more.Foundation.HANDLE,c_void_p)
PREPARE_TAPE_OPERATION = Int32
TAPE_FORMAT = 5
TAPE_LOAD = 0
TAPE_LOCK = 3
TAPE_TENSION = 2
TAPE_UNLOAD = 1
TAPE_UNLOCK = 4
PRIORITY_HINT = Int32
PRIORITY_HINT_IoPriorityHintVeryLow = 0
PRIORITY_HINT_IoPriorityHintLow = 1
PRIORITY_HINT_IoPriorityHintNormal = 2
PRIORITY_HINT_MaximumIoPriorityHintType = 3
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS = Int32
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyInformation = 1
READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyExtendedInformation = 2
def _define_REPARSE_GUID_DATA_BUFFER_head():
    class REPARSE_GUID_DATA_BUFFER(Structure):
        pass
    return REPARSE_GUID_DATA_BUFFER
def _define_REPARSE_GUID_DATA_BUFFER():
    REPARSE_GUID_DATA_BUFFER = win32more.Storage.FileSystem.REPARSE_GUID_DATA_BUFFER_head
    class REPARSE_GUID_DATA_BUFFER__GenericReparseBuffer_e__Struct(Structure):
        pass
    REPARSE_GUID_DATA_BUFFER__GenericReparseBuffer_e__Struct._fields_ = [
        ('DataBuffer', Byte * 1),
    ]
    REPARSE_GUID_DATA_BUFFER._fields_ = [
        ('ReparseTag', UInt32),
        ('ReparseDataLength', UInt16),
        ('Reserved', UInt16),
        ('ReparseGuid', Guid),
        ('GenericReparseBuffer', REPARSE_GUID_DATA_BUFFER__GenericReparseBuffer_e__Struct),
    ]
    return REPARSE_GUID_DATA_BUFFER
REPLACE_FILE_FLAGS = UInt32
REPLACEFILE_WRITE_THROUGH = 1
REPLACEFILE_IGNORE_MERGE_ERRORS = 2
REPLACEFILE_IGNORE_ACL_ERRORS = 4
def _define_SERVER_ALIAS_INFO_0_head():
    class SERVER_ALIAS_INFO_0(Structure):
        pass
    return SERVER_ALIAS_INFO_0
def _define_SERVER_ALIAS_INFO_0():
    SERVER_ALIAS_INFO_0 = win32more.Storage.FileSystem.SERVER_ALIAS_INFO_0_head
    SERVER_ALIAS_INFO_0._fields_ = [
        ('srvai0_alias', win32more.Foundation.PWSTR),
        ('srvai0_target', win32more.Foundation.PWSTR),
        ('srvai0_default', win32more.Foundation.BOOLEAN),
        ('srvai0_reserved', UInt32),
    ]
    return SERVER_ALIAS_INFO_0
def _define_SERVER_CERTIFICATE_INFO_0_head():
    class SERVER_CERTIFICATE_INFO_0(Structure):
        pass
    return SERVER_CERTIFICATE_INFO_0
def _define_SERVER_CERTIFICATE_INFO_0():
    SERVER_CERTIFICATE_INFO_0 = win32more.Storage.FileSystem.SERVER_CERTIFICATE_INFO_0_head
    SERVER_CERTIFICATE_INFO_0._fields_ = [
        ('srvci0_name', win32more.Foundation.PWSTR),
        ('srvci0_subject', win32more.Foundation.PWSTR),
        ('srvci0_issuer', win32more.Foundation.PWSTR),
        ('srvci0_thumbprint', win32more.Foundation.PWSTR),
        ('srvci0_friendlyname', win32more.Foundation.PWSTR),
        ('srvci0_notbefore', win32more.Foundation.PWSTR),
        ('srvci0_notafter', win32more.Foundation.PWSTR),
        ('srvci0_storelocation', win32more.Foundation.PWSTR),
        ('srvci0_storename', win32more.Foundation.PWSTR),
        ('srvci0_renewalchain', win32more.Foundation.PWSTR),
        ('srvci0_type', UInt32),
        ('srvci0_flags', UInt32),
    ]
    return SERVER_CERTIFICATE_INFO_0
SERVER_CERTIFICATE_TYPE = Int32
QUIC = 0
def _define_SESSION_INFO_0_head():
    class SESSION_INFO_0(Structure):
        pass
    return SESSION_INFO_0
def _define_SESSION_INFO_0():
    SESSION_INFO_0 = win32more.Storage.FileSystem.SESSION_INFO_0_head
    SESSION_INFO_0._fields_ = [
        ('sesi0_cname', win32more.Foundation.PWSTR),
    ]
    return SESSION_INFO_0
def _define_SESSION_INFO_1_head():
    class SESSION_INFO_1(Structure):
        pass
    return SESSION_INFO_1
def _define_SESSION_INFO_1():
    SESSION_INFO_1 = win32more.Storage.FileSystem.SESSION_INFO_1_head
    SESSION_INFO_1._fields_ = [
        ('sesi1_cname', win32more.Foundation.PWSTR),
        ('sesi1_username', win32more.Foundation.PWSTR),
        ('sesi1_num_opens', UInt32),
        ('sesi1_time', UInt32),
        ('sesi1_idle_time', UInt32),
        ('sesi1_user_flags', win32more.Storage.FileSystem.SESSION_INFO_USER_FLAGS),
    ]
    return SESSION_INFO_1
def _define_SESSION_INFO_10_head():
    class SESSION_INFO_10(Structure):
        pass
    return SESSION_INFO_10
def _define_SESSION_INFO_10():
    SESSION_INFO_10 = win32more.Storage.FileSystem.SESSION_INFO_10_head
    SESSION_INFO_10._fields_ = [
        ('sesi10_cname', win32more.Foundation.PWSTR),
        ('sesi10_username', win32more.Foundation.PWSTR),
        ('sesi10_time', UInt32),
        ('sesi10_idle_time', UInt32),
    ]
    return SESSION_INFO_10
def _define_SESSION_INFO_2_head():
    class SESSION_INFO_2(Structure):
        pass
    return SESSION_INFO_2
def _define_SESSION_INFO_2():
    SESSION_INFO_2 = win32more.Storage.FileSystem.SESSION_INFO_2_head
    SESSION_INFO_2._fields_ = [
        ('sesi2_cname', win32more.Foundation.PWSTR),
        ('sesi2_username', win32more.Foundation.PWSTR),
        ('sesi2_num_opens', UInt32),
        ('sesi2_time', UInt32),
        ('sesi2_idle_time', UInt32),
        ('sesi2_user_flags', win32more.Storage.FileSystem.SESSION_INFO_USER_FLAGS),
        ('sesi2_cltype_name', win32more.Foundation.PWSTR),
    ]
    return SESSION_INFO_2
def _define_SESSION_INFO_502_head():
    class SESSION_INFO_502(Structure):
        pass
    return SESSION_INFO_502
def _define_SESSION_INFO_502():
    SESSION_INFO_502 = win32more.Storage.FileSystem.SESSION_INFO_502_head
    SESSION_INFO_502._fields_ = [
        ('sesi502_cname', win32more.Foundation.PWSTR),
        ('sesi502_username', win32more.Foundation.PWSTR),
        ('sesi502_num_opens', UInt32),
        ('sesi502_time', UInt32),
        ('sesi502_idle_time', UInt32),
        ('sesi502_user_flags', win32more.Storage.FileSystem.SESSION_INFO_USER_FLAGS),
        ('sesi502_cltype_name', win32more.Foundation.PWSTR),
        ('sesi502_transport', win32more.Foundation.PWSTR),
    ]
    return SESSION_INFO_502
SESSION_INFO_USER_FLAGS = UInt32
SESS_GUEST = 1
SESS_NOENCRYPTION = 2
SET_FILE_POINTER_MOVE_METHOD = UInt32
FILE_BEGIN = 0
FILE_CURRENT = 1
FILE_END = 2
def _define_SHARE_INFO_0_head():
    class SHARE_INFO_0(Structure):
        pass
    return SHARE_INFO_0
def _define_SHARE_INFO_0():
    SHARE_INFO_0 = win32more.Storage.FileSystem.SHARE_INFO_0_head
    SHARE_INFO_0._fields_ = [
        ('shi0_netname', win32more.Foundation.PWSTR),
    ]
    return SHARE_INFO_0
def _define_SHARE_INFO_1_head():
    class SHARE_INFO_1(Structure):
        pass
    return SHARE_INFO_1
def _define_SHARE_INFO_1():
    SHARE_INFO_1 = win32more.Storage.FileSystem.SHARE_INFO_1_head
    SHARE_INFO_1._fields_ = [
        ('shi1_netname', win32more.Foundation.PWSTR),
        ('shi1_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('shi1_remark', win32more.Foundation.PWSTR),
    ]
    return SHARE_INFO_1
def _define_SHARE_INFO_1004_head():
    class SHARE_INFO_1004(Structure):
        pass
    return SHARE_INFO_1004
def _define_SHARE_INFO_1004():
    SHARE_INFO_1004 = win32more.Storage.FileSystem.SHARE_INFO_1004_head
    SHARE_INFO_1004._fields_ = [
        ('shi1004_remark', win32more.Foundation.PWSTR),
    ]
    return SHARE_INFO_1004
def _define_SHARE_INFO_1005_head():
    class SHARE_INFO_1005(Structure):
        pass
    return SHARE_INFO_1005
def _define_SHARE_INFO_1005():
    SHARE_INFO_1005 = win32more.Storage.FileSystem.SHARE_INFO_1005_head
    SHARE_INFO_1005._fields_ = [
        ('shi1005_flags', UInt32),
    ]
    return SHARE_INFO_1005
def _define_SHARE_INFO_1006_head():
    class SHARE_INFO_1006(Structure):
        pass
    return SHARE_INFO_1006
def _define_SHARE_INFO_1006():
    SHARE_INFO_1006 = win32more.Storage.FileSystem.SHARE_INFO_1006_head
    SHARE_INFO_1006._fields_ = [
        ('shi1006_max_uses', UInt32),
    ]
    return SHARE_INFO_1006
def _define_SHARE_INFO_1501_head():
    class SHARE_INFO_1501(Structure):
        pass
    return SHARE_INFO_1501
def _define_SHARE_INFO_1501():
    SHARE_INFO_1501 = win32more.Storage.FileSystem.SHARE_INFO_1501_head
    SHARE_INFO_1501._fields_ = [
        ('shi1501_reserved', UInt32),
        ('shi1501_security_descriptor', win32more.Security.PSECURITY_DESCRIPTOR),
    ]
    return SHARE_INFO_1501
def _define_SHARE_INFO_1503_head():
    class SHARE_INFO_1503(Structure):
        pass
    return SHARE_INFO_1503
def _define_SHARE_INFO_1503():
    SHARE_INFO_1503 = win32more.Storage.FileSystem.SHARE_INFO_1503_head
    SHARE_INFO_1503._fields_ = [
        ('shi1503_sharefilter', Guid),
    ]
    return SHARE_INFO_1503
def _define_SHARE_INFO_2_head():
    class SHARE_INFO_2(Structure):
        pass
    return SHARE_INFO_2
def _define_SHARE_INFO_2():
    SHARE_INFO_2 = win32more.Storage.FileSystem.SHARE_INFO_2_head
    SHARE_INFO_2._fields_ = [
        ('shi2_netname', win32more.Foundation.PWSTR),
        ('shi2_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('shi2_remark', win32more.Foundation.PWSTR),
        ('shi2_permissions', win32more.Storage.FileSystem.SHARE_INFO_PERMISSIONS),
        ('shi2_max_uses', UInt32),
        ('shi2_current_uses', UInt32),
        ('shi2_path', win32more.Foundation.PWSTR),
        ('shi2_passwd', win32more.Foundation.PWSTR),
    ]
    return SHARE_INFO_2
def _define_SHARE_INFO_501_head():
    class SHARE_INFO_501(Structure):
        pass
    return SHARE_INFO_501
def _define_SHARE_INFO_501():
    SHARE_INFO_501 = win32more.Storage.FileSystem.SHARE_INFO_501_head
    SHARE_INFO_501._fields_ = [
        ('shi501_netname', win32more.Foundation.PWSTR),
        ('shi501_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('shi501_remark', win32more.Foundation.PWSTR),
        ('shi501_flags', UInt32),
    ]
    return SHARE_INFO_501
def _define_SHARE_INFO_502_head():
    class SHARE_INFO_502(Structure):
        pass
    return SHARE_INFO_502
def _define_SHARE_INFO_502():
    SHARE_INFO_502 = win32more.Storage.FileSystem.SHARE_INFO_502_head
    SHARE_INFO_502._fields_ = [
        ('shi502_netname', win32more.Foundation.PWSTR),
        ('shi502_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('shi502_remark', win32more.Foundation.PWSTR),
        ('shi502_permissions', win32more.Storage.FileSystem.SHARE_INFO_PERMISSIONS),
        ('shi502_max_uses', UInt32),
        ('shi502_current_uses', UInt32),
        ('shi502_path', win32more.Foundation.PWSTR),
        ('shi502_passwd', win32more.Foundation.PWSTR),
        ('shi502_reserved', UInt32),
        ('shi502_security_descriptor', win32more.Security.PSECURITY_DESCRIPTOR),
    ]
    return SHARE_INFO_502
def _define_SHARE_INFO_503_head():
    class SHARE_INFO_503(Structure):
        pass
    return SHARE_INFO_503
def _define_SHARE_INFO_503():
    SHARE_INFO_503 = win32more.Storage.FileSystem.SHARE_INFO_503_head
    SHARE_INFO_503._fields_ = [
        ('shi503_netname', win32more.Foundation.PWSTR),
        ('shi503_type', win32more.Storage.FileSystem.SHARE_TYPE),
        ('shi503_remark', win32more.Foundation.PWSTR),
        ('shi503_permissions', win32more.Storage.FileSystem.SHARE_INFO_PERMISSIONS),
        ('shi503_max_uses', UInt32),
        ('shi503_current_uses', UInt32),
        ('shi503_path', win32more.Foundation.PWSTR),
        ('shi503_passwd', win32more.Foundation.PWSTR),
        ('shi503_servername', win32more.Foundation.PWSTR),
        ('shi503_reserved', UInt32),
        ('shi503_security_descriptor', win32more.Security.PSECURITY_DESCRIPTOR),
    ]
    return SHARE_INFO_503
SHARE_INFO_PERMISSIONS = UInt32
ACCESS_READ = 1
ACCESS_WRITE = 2
ACCESS_CREATE = 4
ACCESS_EXEC = 8
ACCESS_DELETE = 16
ACCESS_ATRIB = 32
ACCESS_PERM = 64
ACCESS_ALL = 32768
SHARE_TYPE = UInt32
STYPE_DISKTREE = 0
STYPE_PRINTQ = 1
STYPE_DEVICE = 2
STYPE_IPC = 3
STYPE_SPECIAL = 2147483648
STYPE_TEMPORARY = 1073741824
STYPE_MASK = 255
def _define_STAT_SERVER_0_head():
    class STAT_SERVER_0(Structure):
        pass
    return STAT_SERVER_0
def _define_STAT_SERVER_0():
    STAT_SERVER_0 = win32more.Storage.FileSystem.STAT_SERVER_0_head
    STAT_SERVER_0._fields_ = [
        ('sts0_start', UInt32),
        ('sts0_fopens', UInt32),
        ('sts0_devopens', UInt32),
        ('sts0_jobsqueued', UInt32),
        ('sts0_sopens', UInt32),
        ('sts0_stimedout', UInt32),
        ('sts0_serrorout', UInt32),
        ('sts0_pwerrors', UInt32),
        ('sts0_permerrors', UInt32),
        ('sts0_syserrors', UInt32),
        ('sts0_bytessent_low', UInt32),
        ('sts0_bytessent_high', UInt32),
        ('sts0_bytesrcvd_low', UInt32),
        ('sts0_bytesrcvd_high', UInt32),
        ('sts0_avresponse', UInt32),
        ('sts0_reqbufneed', UInt32),
        ('sts0_bigbufneed', UInt32),
    ]
    return STAT_SERVER_0
def _define_STAT_WORKSTATION_0_head():
    class STAT_WORKSTATION_0(Structure):
        pass
    return STAT_WORKSTATION_0
def _define_STAT_WORKSTATION_0():
    STAT_WORKSTATION_0 = win32more.Storage.FileSystem.STAT_WORKSTATION_0_head
    STAT_WORKSTATION_0._fields_ = [
        ('StatisticsStartTime', win32more.Foundation.LARGE_INTEGER),
        ('BytesReceived', win32more.Foundation.LARGE_INTEGER),
        ('SmbsReceived', win32more.Foundation.LARGE_INTEGER),
        ('PagingReadBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('NonPagingReadBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('CacheReadBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('NetworkReadBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('BytesTransmitted', win32more.Foundation.LARGE_INTEGER),
        ('SmbsTransmitted', win32more.Foundation.LARGE_INTEGER),
        ('PagingWriteBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('NonPagingWriteBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('CacheWriteBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('NetworkWriteBytesRequested', win32more.Foundation.LARGE_INTEGER),
        ('InitiallyFailedOperations', UInt32),
        ('FailedCompletionOperations', UInt32),
        ('ReadOperations', UInt32),
        ('RandomReadOperations', UInt32),
        ('ReadSmbs', UInt32),
        ('LargeReadSmbs', UInt32),
        ('SmallReadSmbs', UInt32),
        ('WriteOperations', UInt32),
        ('RandomWriteOperations', UInt32),
        ('WriteSmbs', UInt32),
        ('LargeWriteSmbs', UInt32),
        ('SmallWriteSmbs', UInt32),
        ('RawReadsDenied', UInt32),
        ('RawWritesDenied', UInt32),
        ('NetworkErrors', UInt32),
        ('Sessions', UInt32),
        ('FailedSessions', UInt32),
        ('Reconnects', UInt32),
        ('CoreConnects', UInt32),
        ('Lanman20Connects', UInt32),
        ('Lanman21Connects', UInt32),
        ('LanmanNtConnects', UInt32),
        ('ServerDisconnects', UInt32),
        ('HungSessions', UInt32),
        ('UseCount', UInt32),
        ('FailedUseCount', UInt32),
        ('CurrentCommands', UInt32),
    ]
    return STAT_WORKSTATION_0
STORAGE_BUS_TYPE = Int32
STORAGE_BUS_TYPE_BusTypeUnknown = 0
STORAGE_BUS_TYPE_BusTypeScsi = 1
STORAGE_BUS_TYPE_BusTypeAtapi = 2
STORAGE_BUS_TYPE_BusTypeAta = 3
STORAGE_BUS_TYPE_BusType1394 = 4
STORAGE_BUS_TYPE_BusTypeSsa = 5
STORAGE_BUS_TYPE_BusTypeFibre = 6
STORAGE_BUS_TYPE_BusTypeUsb = 7
STORAGE_BUS_TYPE_BusTypeRAID = 8
STORAGE_BUS_TYPE_BusTypeiScsi = 9
STORAGE_BUS_TYPE_BusTypeSas = 10
STORAGE_BUS_TYPE_BusTypeSata = 11
STORAGE_BUS_TYPE_BusTypeSd = 12
STORAGE_BUS_TYPE_BusTypeMmc = 13
STORAGE_BUS_TYPE_BusTypeVirtual = 14
STORAGE_BUS_TYPE_BusTypeFileBackedVirtual = 15
STORAGE_BUS_TYPE_BusTypeSpaces = 16
STORAGE_BUS_TYPE_BusTypeNvme = 17
STORAGE_BUS_TYPE_BusTypeSCM = 18
STORAGE_BUS_TYPE_BusTypeUfs = 19
STORAGE_BUS_TYPE_BusTypeMax = 20
STORAGE_BUS_TYPE_BusTypeMaxReserved = 127
STREAM_INFO_LEVELS = Int32
STREAM_INFO_LEVELS_FindStreamInfoStandard = 0
STREAM_INFO_LEVELS_FindStreamInfoMaxInfoLevel = 1
SYMBOLIC_LINK_FLAGS = UInt32
SYMBOLIC_LINK_FLAG_DIRECTORY = 1
SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE = 2
def _define_TAPE_ERASE_head():
    class TAPE_ERASE(Structure):
        pass
    return TAPE_ERASE
def _define_TAPE_ERASE():
    TAPE_ERASE = win32more.Storage.FileSystem.TAPE_ERASE_head
    TAPE_ERASE._fields_ = [
        ('Type', win32more.Storage.FileSystem.ERASE_TAPE_TYPE),
        ('Immediate', win32more.Foundation.BOOLEAN),
    ]
    return TAPE_ERASE
def _define_TAPE_GET_POSITION_head():
    class TAPE_GET_POSITION(Structure):
        pass
    return TAPE_GET_POSITION
def _define_TAPE_GET_POSITION():
    TAPE_GET_POSITION = win32more.Storage.FileSystem.TAPE_GET_POSITION_head
    TAPE_GET_POSITION._fields_ = [
        ('Type', win32more.Storage.FileSystem.TAPE_POSITION_TYPE),
        ('Partition', UInt32),
        ('Offset', win32more.Foundation.LARGE_INTEGER),
    ]
    return TAPE_GET_POSITION
TAPE_INFORMATION_TYPE = UInt32
SET_TAPE_DRIVE_INFORMATION = 1
SET_TAPE_MEDIA_INFORMATION = 0
TAPE_POSITION_METHOD = Int32
TAPE_ABSOLUTE_BLOCK = 1
TAPE_LOGICAL_BLOCK = 2
TAPE_REWIND = 0
TAPE_SPACE_END_OF_DATA = 4
TAPE_SPACE_FILEMARKS = 6
TAPE_SPACE_RELATIVE_BLOCKS = 5
TAPE_SPACE_SEQUENTIAL_FMKS = 7
TAPE_SPACE_SEQUENTIAL_SMKS = 9
TAPE_SPACE_SETMARKS = 8
TAPE_POSITION_TYPE = Int32
TAPE_ABSOLUTE_POSITION = 0
TAPE_LOGICAL_POSITION = 1
def _define_TAPE_PREPARE_head():
    class TAPE_PREPARE(Structure):
        pass
    return TAPE_PREPARE
def _define_TAPE_PREPARE():
    TAPE_PREPARE = win32more.Storage.FileSystem.TAPE_PREPARE_head
    TAPE_PREPARE._fields_ = [
        ('Operation', win32more.Storage.FileSystem.PREPARE_TAPE_OPERATION),
        ('Immediate', win32more.Foundation.BOOLEAN),
    ]
    return TAPE_PREPARE
def _define_TAPE_SET_POSITION_head():
    class TAPE_SET_POSITION(Structure):
        pass
    return TAPE_SET_POSITION
def _define_TAPE_SET_POSITION():
    TAPE_SET_POSITION = win32more.Storage.FileSystem.TAPE_SET_POSITION_head
    TAPE_SET_POSITION._fields_ = [
        ('Method', win32more.Storage.FileSystem.TAPE_POSITION_METHOD),
        ('Partition', UInt32),
        ('Offset', win32more.Foundation.LARGE_INTEGER),
        ('Immediate', win32more.Foundation.BOOLEAN),
    ]
    return TAPE_SET_POSITION
def _define_TAPE_WRITE_MARKS_head():
    class TAPE_WRITE_MARKS(Structure):
        pass
    return TAPE_WRITE_MARKS
def _define_TAPE_WRITE_MARKS():
    TAPE_WRITE_MARKS = win32more.Storage.FileSystem.TAPE_WRITE_MARKS_head
    TAPE_WRITE_MARKS._fields_ = [
        ('Type', win32more.Storage.FileSystem.TAPEMARK_TYPE),
        ('Count', UInt32),
        ('Immediate', win32more.Foundation.BOOLEAN),
    ]
    return TAPE_WRITE_MARKS
TAPEMARK_TYPE = Int32
TAPE_FILEMARKS = 1
TAPE_LONG_FILEMARKS = 3
TAPE_SETMARKS = 0
TAPE_SHORT_FILEMARKS = 2
def _define_TRANSACTION_NOTIFICATION_head():
    class TRANSACTION_NOTIFICATION(Structure):
        pass
    return TRANSACTION_NOTIFICATION
def _define_TRANSACTION_NOTIFICATION():
    TRANSACTION_NOTIFICATION = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_head
    TRANSACTION_NOTIFICATION._fields_ = [
        ('TransactionKey', c_void_p),
        ('TransactionNotification', UInt32),
        ('TmVirtualClock', win32more.Foundation.LARGE_INTEGER),
        ('ArgumentLength', UInt32),
    ]
    return TRANSACTION_NOTIFICATION
def _define_TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT_head():
    class TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT(Structure):
        pass
    return TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT():
    TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT_head
    TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT._fields_ = [
        ('MarshalCookie', UInt32),
        ('UOW', Guid),
    ]
    return TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT_head():
    class TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT(Structure):
        pass
    return TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT():
    TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT_head
    TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT._fields_ = [
        ('PropagationCookie', UInt32),
        ('UOW', Guid),
        ('TmIdentity', Guid),
        ('BufferLength', UInt32),
    ]
    return TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT_head():
    class TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT(Structure):
        pass
    return TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT():
    TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT_head
    TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT._fields_ = [
        ('EnlistmentId', Guid),
        ('UOW', Guid),
    ]
    return TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT_head():
    class TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT(Structure):
        pass
    return TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT():
    TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT_head
    TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT._fields_ = [
        ('SavepointId', UInt32),
    ]
    return TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT_head():
    class TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT(Structure):
        pass
    return TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT
def _define_TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT():
    TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT = win32more.Storage.FileSystem.TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT_head
    TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT._fields_ = [
        ('TmIdentity', Guid),
        ('Flags', UInt32),
    ]
    return TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT
TRANSACTION_OUTCOME = Int32
TRANSACTION_OUTCOME_TransactionOutcomeUndetermined = 1
TRANSACTION_OUTCOME_TransactionOutcomeCommitted = 2
TRANSACTION_OUTCOME_TransactionOutcomeAborted = 3
def _define_TXF_ID_head():
    class TXF_ID(Structure):
        pass
    return TXF_ID
def _define_TXF_ID():
    TXF_ID = win32more.Storage.FileSystem.TXF_ID_head
    class TXF_ID__Anonymous_e__Struct(Structure):
        pass
    TXF_ID__Anonymous_e__Struct._pack_ = 4
    TXF_ID__Anonymous_e__Struct._fields_ = [
        ('LowPart', Int64),
        ('HighPart', Int64),
    ]
    TXF_ID._pack_ = 4
    TXF_ID._anonymous_ = [
        'Anonymous',
    ]
    TXF_ID._fields_ = [
        ('Anonymous', TXF_ID__Anonymous_e__Struct),
    ]
    return TXF_ID
def _define_TXF_LOG_RECORD_AFFECTED_FILE_head():
    class TXF_LOG_RECORD_AFFECTED_FILE(Structure):
        pass
    return TXF_LOG_RECORD_AFFECTED_FILE
def _define_TXF_LOG_RECORD_AFFECTED_FILE():
    TXF_LOG_RECORD_AFFECTED_FILE = win32more.Storage.FileSystem.TXF_LOG_RECORD_AFFECTED_FILE_head
    TXF_LOG_RECORD_AFFECTED_FILE._pack_ = 4
    TXF_LOG_RECORD_AFFECTED_FILE._fields_ = [
        ('Version', UInt16),
        ('RecordLength', UInt32),
        ('Flags', UInt32),
        ('TxfFileId', win32more.Storage.FileSystem.TXF_ID),
        ('KtmGuid', Guid),
        ('FileNameLength', UInt32),
        ('FileNameByteOffsetInStructure', UInt32),
    ]
    return TXF_LOG_RECORD_AFFECTED_FILE
def _define_TXF_LOG_RECORD_BASE_head():
    class TXF_LOG_RECORD_BASE(Structure):
        pass
    return TXF_LOG_RECORD_BASE
def _define_TXF_LOG_RECORD_BASE():
    TXF_LOG_RECORD_BASE = win32more.Storage.FileSystem.TXF_LOG_RECORD_BASE_head
    TXF_LOG_RECORD_BASE._pack_ = 4
    TXF_LOG_RECORD_BASE._fields_ = [
        ('Version', UInt16),
        ('RecordType', win32more.Storage.FileSystem.TXF_LOG_RECORD_TYPE),
        ('RecordLength', UInt32),
    ]
    return TXF_LOG_RECORD_BASE
def _define_TXF_LOG_RECORD_TRUNCATE_head():
    class TXF_LOG_RECORD_TRUNCATE(Structure):
        pass
    return TXF_LOG_RECORD_TRUNCATE
def _define_TXF_LOG_RECORD_TRUNCATE():
    TXF_LOG_RECORD_TRUNCATE = win32more.Storage.FileSystem.TXF_LOG_RECORD_TRUNCATE_head
    TXF_LOG_RECORD_TRUNCATE._pack_ = 4
    TXF_LOG_RECORD_TRUNCATE._fields_ = [
        ('Version', UInt16),
        ('RecordType', UInt16),
        ('RecordLength', UInt32),
        ('Flags', UInt32),
        ('TxfFileId', win32more.Storage.FileSystem.TXF_ID),
        ('KtmGuid', Guid),
        ('NewFileSize', Int64),
        ('FileNameLength', UInt32),
        ('FileNameByteOffsetInStructure', UInt32),
    ]
    return TXF_LOG_RECORD_TRUNCATE
TXF_LOG_RECORD_TYPE = UInt16
TXF_LOG_RECORD_TYPE_AFFECTED_FILE = 4
TXF_LOG_RECORD_TYPE_TRUNCATE = 2
TXF_LOG_RECORD_TYPE_WRITE = 1
def _define_TXF_LOG_RECORD_WRITE_head():
    class TXF_LOG_RECORD_WRITE(Structure):
        pass
    return TXF_LOG_RECORD_WRITE
def _define_TXF_LOG_RECORD_WRITE():
    TXF_LOG_RECORD_WRITE = win32more.Storage.FileSystem.TXF_LOG_RECORD_WRITE_head
    TXF_LOG_RECORD_WRITE._pack_ = 4
    TXF_LOG_RECORD_WRITE._fields_ = [
        ('Version', UInt16),
        ('RecordType', UInt16),
        ('RecordLength', UInt32),
        ('Flags', UInt32),
        ('TxfFileId', win32more.Storage.FileSystem.TXF_ID),
        ('KtmGuid', Guid),
        ('ByteOffsetInFile', Int64),
        ('NumBytesWritten', UInt32),
        ('ByteOffsetInStructure', UInt32),
        ('FileNameLength', UInt32),
        ('FileNameByteOffsetInStructure', UInt32),
    ]
    return TXF_LOG_RECORD_WRITE
TXFS_MINIVERSION = UInt32
TXFS_MINIVERSION_COMMITTED_VIEW = 0
TXFS_MINIVERSION_DIRTY_VIEW = 65535
TXFS_MINIVERSION_DEFAULT_VIEW = 65534
VER_FIND_FILE_FLAGS = UInt32
VFFF_ISSHAREDFILE = 1
VER_FIND_FILE_STATUS = UInt32
VFF_CURNEDEST = 1
VFF_FILEINUSE = 2
VFF_BUFFTOOSMALL = 4
VER_INSTALL_FILE_FLAGS = UInt32
VIFF_FORCEINSTALL = 1
VIFF_DONTDELETEOLD = 2
VER_INSTALL_FILE_STATUS = UInt32
VIF_TEMPFILE = 1
VIF_MISMATCH = 2
VIF_SRCOLD = 4
VIF_DIFFLANG = 8
VIF_DIFFCODEPG = 16
VIF_DIFFTYPE = 32
VIF_WRITEPROT = 64
VIF_FILEINUSE = 128
VIF_OUTOFSPACE = 256
VIF_ACCESSVIOLATION = 512
VIF_SHARINGVIOLATION = 1024
VIF_CANNOTCREATE = 2048
VIF_CANNOTDELETE = 4096
VIF_CANNOTRENAME = 8192
VIF_CANNOTDELETECUR = 16384
VIF_OUTOFMEMORY = 32768
VIF_CANNOTREADSRC = 65536
VIF_CANNOTREADDST = 131072
VIF_BUFFTOOSMALL = 262144
VIF_CANNOTLOADLZ32 = 524288
VIF_CANNOTLOADCABINET = 1048576
def _define_VOLUME_ALLOCATE_BC_STREAM_INPUT_head():
    class VOLUME_ALLOCATE_BC_STREAM_INPUT(Structure):
        pass
    return VOLUME_ALLOCATE_BC_STREAM_INPUT
def _define_VOLUME_ALLOCATE_BC_STREAM_INPUT():
    VOLUME_ALLOCATE_BC_STREAM_INPUT = win32more.Storage.FileSystem.VOLUME_ALLOCATE_BC_STREAM_INPUT_head
    VOLUME_ALLOCATE_BC_STREAM_INPUT._fields_ = [
        ('Version', UInt32),
        ('RequestsPerPeriod', UInt32),
        ('Period', UInt32),
        ('RetryFailures', win32more.Foundation.BOOLEAN),
        ('Discardable', win32more.Foundation.BOOLEAN),
        ('Reserved1', win32more.Foundation.BOOLEAN * 2),
        ('LowestByteOffset', UInt64),
        ('HighestByteOffset', UInt64),
        ('AccessType', UInt32),
        ('AccessMode', UInt32),
    ]
    return VOLUME_ALLOCATE_BC_STREAM_INPUT
def _define_VOLUME_ALLOCATE_BC_STREAM_OUTPUT_head():
    class VOLUME_ALLOCATE_BC_STREAM_OUTPUT(Structure):
        pass
    return VOLUME_ALLOCATE_BC_STREAM_OUTPUT
def _define_VOLUME_ALLOCATE_BC_STREAM_OUTPUT():
    VOLUME_ALLOCATE_BC_STREAM_OUTPUT = win32more.Storage.FileSystem.VOLUME_ALLOCATE_BC_STREAM_OUTPUT_head
    VOLUME_ALLOCATE_BC_STREAM_OUTPUT._fields_ = [
        ('RequestSize', UInt64),
        ('NumOutStandingRequests', UInt32),
    ]
    return VOLUME_ALLOCATE_BC_STREAM_OUTPUT
def _define_VOLUME_ALLOCATION_HINT_INPUT_head():
    class VOLUME_ALLOCATION_HINT_INPUT(Structure):
        pass
    return VOLUME_ALLOCATION_HINT_INPUT
def _define_VOLUME_ALLOCATION_HINT_INPUT():
    VOLUME_ALLOCATION_HINT_INPUT = win32more.Storage.FileSystem.VOLUME_ALLOCATION_HINT_INPUT_head
    VOLUME_ALLOCATION_HINT_INPUT._fields_ = [
        ('ClusterSize', UInt32),
        ('NumberOfClusters', UInt32),
        ('StartingClusterNumber', Int64),
    ]
    return VOLUME_ALLOCATION_HINT_INPUT
def _define_VOLUME_ALLOCATION_HINT_OUTPUT_head():
    class VOLUME_ALLOCATION_HINT_OUTPUT(Structure):
        pass
    return VOLUME_ALLOCATION_HINT_OUTPUT
def _define_VOLUME_ALLOCATION_HINT_OUTPUT():
    VOLUME_ALLOCATION_HINT_OUTPUT = win32more.Storage.FileSystem.VOLUME_ALLOCATION_HINT_OUTPUT_head
    VOLUME_ALLOCATION_HINT_OUTPUT._fields_ = [
        ('Bitmap', UInt32 * 1),
    ]
    return VOLUME_ALLOCATION_HINT_OUTPUT
def _define_VOLUME_CRITICAL_IO_head():
    class VOLUME_CRITICAL_IO(Structure):
        pass
    return VOLUME_CRITICAL_IO
def _define_VOLUME_CRITICAL_IO():
    VOLUME_CRITICAL_IO = win32more.Storage.FileSystem.VOLUME_CRITICAL_IO_head
    VOLUME_CRITICAL_IO._fields_ = [
        ('AccessType', UInt32),
        ('ExtentsCount', UInt32),
        ('Extents', win32more.Storage.FileSystem.FILE_EXTENT * 1),
    ]
    return VOLUME_CRITICAL_IO
def _define_VOLUME_FAILOVER_SET_head():
    class VOLUME_FAILOVER_SET(Structure):
        pass
    return VOLUME_FAILOVER_SET
def _define_VOLUME_FAILOVER_SET():
    VOLUME_FAILOVER_SET = win32more.Storage.FileSystem.VOLUME_FAILOVER_SET_head
    VOLUME_FAILOVER_SET._fields_ = [
        ('NumberOfDisks', UInt32),
        ('DiskNumbers', UInt32 * 1),
    ]
    return VOLUME_FAILOVER_SET
def _define_VOLUME_GET_BC_PROPERTIES_INPUT_head():
    class VOLUME_GET_BC_PROPERTIES_INPUT(Structure):
        pass
    return VOLUME_GET_BC_PROPERTIES_INPUT
def _define_VOLUME_GET_BC_PROPERTIES_INPUT():
    VOLUME_GET_BC_PROPERTIES_INPUT = win32more.Storage.FileSystem.VOLUME_GET_BC_PROPERTIES_INPUT_head
    VOLUME_GET_BC_PROPERTIES_INPUT._fields_ = [
        ('Version', UInt32),
        ('Reserved1', UInt32),
        ('LowestByteOffset', UInt64),
        ('HighestByteOffset', UInt64),
        ('AccessType', UInt32),
        ('AccessMode', UInt32),
    ]
    return VOLUME_GET_BC_PROPERTIES_INPUT
def _define_VOLUME_GET_BC_PROPERTIES_OUTPUT_head():
    class VOLUME_GET_BC_PROPERTIES_OUTPUT(Structure):
        pass
    return VOLUME_GET_BC_PROPERTIES_OUTPUT
def _define_VOLUME_GET_BC_PROPERTIES_OUTPUT():
    VOLUME_GET_BC_PROPERTIES_OUTPUT = win32more.Storage.FileSystem.VOLUME_GET_BC_PROPERTIES_OUTPUT_head
    VOLUME_GET_BC_PROPERTIES_OUTPUT._fields_ = [
        ('MaximumRequestsPerPeriod', UInt32),
        ('MinimumPeriod', UInt32),
        ('MaximumRequestSize', UInt64),
        ('EstimatedTimePerRequest', UInt32),
        ('NumOutStandingRequests', UInt32),
        ('RequestSize', UInt64),
    ]
    return VOLUME_GET_BC_PROPERTIES_OUTPUT
def _define_VOLUME_LOGICAL_OFFSET_head():
    class VOLUME_LOGICAL_OFFSET(Structure):
        pass
    return VOLUME_LOGICAL_OFFSET
def _define_VOLUME_LOGICAL_OFFSET():
    VOLUME_LOGICAL_OFFSET = win32more.Storage.FileSystem.VOLUME_LOGICAL_OFFSET_head
    VOLUME_LOGICAL_OFFSET._fields_ = [
        ('LogicalOffset', Int64),
    ]
    return VOLUME_LOGICAL_OFFSET
def _define_VOLUME_NUMBER_head():
    class VOLUME_NUMBER(Structure):
        pass
    return VOLUME_NUMBER
def _define_VOLUME_NUMBER():
    VOLUME_NUMBER = win32more.Storage.FileSystem.VOLUME_NUMBER_head
    VOLUME_NUMBER._fields_ = [
        ('VolumeNumber', UInt32),
        ('VolumeManagerName', Char * 8),
    ]
    return VOLUME_NUMBER
def _define_VOLUME_PHYSICAL_OFFSET_head():
    class VOLUME_PHYSICAL_OFFSET(Structure):
        pass
    return VOLUME_PHYSICAL_OFFSET
def _define_VOLUME_PHYSICAL_OFFSET():
    VOLUME_PHYSICAL_OFFSET = win32more.Storage.FileSystem.VOLUME_PHYSICAL_OFFSET_head
    VOLUME_PHYSICAL_OFFSET._fields_ = [
        ('DiskNumber', UInt32),
        ('Offset', Int64),
    ]
    return VOLUME_PHYSICAL_OFFSET
def _define_VOLUME_PHYSICAL_OFFSETS_head():
    class VOLUME_PHYSICAL_OFFSETS(Structure):
        pass
    return VOLUME_PHYSICAL_OFFSETS
def _define_VOLUME_PHYSICAL_OFFSETS():
    VOLUME_PHYSICAL_OFFSETS = win32more.Storage.FileSystem.VOLUME_PHYSICAL_OFFSETS_head
    VOLUME_PHYSICAL_OFFSETS._fields_ = [
        ('NumberOfPhysicalOffsets', UInt32),
        ('PhysicalOffset', win32more.Storage.FileSystem.VOLUME_PHYSICAL_OFFSET * 1),
    ]
    return VOLUME_PHYSICAL_OFFSETS
def _define_VOLUME_READ_PLEX_INPUT_head():
    class VOLUME_READ_PLEX_INPUT(Structure):
        pass
    return VOLUME_READ_PLEX_INPUT
def _define_VOLUME_READ_PLEX_INPUT():
    VOLUME_READ_PLEX_INPUT = win32more.Storage.FileSystem.VOLUME_READ_PLEX_INPUT_head
    VOLUME_READ_PLEX_INPUT._fields_ = [
        ('ByteOffset', win32more.Foundation.LARGE_INTEGER),
        ('Length', UInt32),
        ('PlexNumber', UInt32),
    ]
    return VOLUME_READ_PLEX_INPUT
def _define_VOLUME_SET_GPT_ATTRIBUTES_INFORMATION_head():
    class VOLUME_SET_GPT_ATTRIBUTES_INFORMATION(Structure):
        pass
    return VOLUME_SET_GPT_ATTRIBUTES_INFORMATION
def _define_VOLUME_SET_GPT_ATTRIBUTES_INFORMATION():
    VOLUME_SET_GPT_ATTRIBUTES_INFORMATION = win32more.Storage.FileSystem.VOLUME_SET_GPT_ATTRIBUTES_INFORMATION_head
    VOLUME_SET_GPT_ATTRIBUTES_INFORMATION._fields_ = [
        ('GptAttributes', UInt64),
        ('RevertOnClose', win32more.Foundation.BOOLEAN),
        ('ApplyToAllConnectedVolumes', win32more.Foundation.BOOLEAN),
        ('Reserved1', UInt16),
        ('Reserved2', UInt32),
    ]
    return VOLUME_SET_GPT_ATTRIBUTES_INFORMATION
def _define_VOLUME_SHRINK_INFO_head():
    class VOLUME_SHRINK_INFO(Structure):
        pass
    return VOLUME_SHRINK_INFO
def _define_VOLUME_SHRINK_INFO():
    VOLUME_SHRINK_INFO = win32more.Storage.FileSystem.VOLUME_SHRINK_INFO_head
    VOLUME_SHRINK_INFO._fields_ = [
        ('VolumeSize', UInt64),
    ]
    return VOLUME_SHRINK_INFO
def _define_VS_FIXEDFILEINFO_head():
    class VS_FIXEDFILEINFO(Structure):
        pass
    return VS_FIXEDFILEINFO
def _define_VS_FIXEDFILEINFO():
    VS_FIXEDFILEINFO = win32more.Storage.FileSystem.VS_FIXEDFILEINFO_head
    VS_FIXEDFILEINFO._fields_ = [
        ('dwSignature', UInt32),
        ('dwStrucVersion', UInt32),
        ('dwFileVersionMS', UInt32),
        ('dwFileVersionLS', UInt32),
        ('dwProductVersionMS', UInt32),
        ('dwProductVersionLS', UInt32),
        ('dwFileFlagsMask', UInt32),
        ('dwFileFlags', win32more.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_FLAGS),
        ('dwFileOS', win32more.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_OS),
        ('dwFileType', win32more.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_TYPE),
        ('dwFileSubtype', win32more.Storage.FileSystem.VS_FIXEDFILEINFO_FILE_SUBTYPE),
        ('dwFileDateMS', UInt32),
        ('dwFileDateLS', UInt32),
    ]
    return VS_FIXEDFILEINFO
VS_FIXEDFILEINFO_FILE_FLAGS = UInt32
VS_FF_DEBUG = 1
VS_FF_PRERELEASE = 2
VS_FF_PATCHED = 4
VS_FF_PRIVATEBUILD = 8
VS_FF_INFOINFERRED = 16
VS_FF_SPECIALBUILD = 32
VS_FIXEDFILEINFO_FILE_OS = Int32
VOS_UNKNOWN = 0
VOS_DOS = 65536
VOS_OS216 = 131072
VOS_OS232 = 196608
VOS_NT = 262144
VOS_WINCE = 327680
VOS__BASE = 0
VOS__WINDOWS16 = 1
VOS__PM16 = 2
VOS__PM32 = 3
VOS__WINDOWS32 = 4
VOS_DOS_WINDOWS16 = 65537
VOS_DOS_WINDOWS32 = 65540
VOS_OS216_PM16 = 131074
VOS_OS232_PM32 = 196611
VOS_NT_WINDOWS32 = 262148
VS_FIXEDFILEINFO_FILE_SUBTYPE = Int32
VFT2_UNKNOWN = 0
VFT2_DRV_PRINTER = 1
VFT2_DRV_KEYBOARD = 2
VFT2_DRV_LANGUAGE = 3
VFT2_DRV_DISPLAY = 4
VFT2_DRV_MOUSE = 5
VFT2_DRV_NETWORK = 6
VFT2_DRV_SYSTEM = 7
VFT2_DRV_INSTALLABLE = 8
VFT2_DRV_SOUND = 9
VFT2_DRV_COMM = 10
VFT2_DRV_INPUTMETHOD = 11
VFT2_DRV_VERSIONED_PRINTER = 12
VFT2_FONT_RASTER = 1
VFT2_FONT_VECTOR = 2
VFT2_FONT_TRUETYPE = 3
VS_FIXEDFILEINFO_FILE_TYPE = Int32
VFT_UNKNOWN = 0
VFT_APP = 1
VFT_DLL = 2
VFT_DRV = 3
VFT_FONT = 4
VFT_VXD = 5
VFT_STATIC_LIB = 7
def _define_WIM_ENTRY_INFO_head():
    class WIM_ENTRY_INFO(Structure):
        pass
    return WIM_ENTRY_INFO
def _define_WIM_ENTRY_INFO():
    WIM_ENTRY_INFO = win32more.Storage.FileSystem.WIM_ENTRY_INFO_head
    WIM_ENTRY_INFO._fields_ = [
        ('WimEntryInfoSize', UInt32),
        ('WimType', UInt32),
        ('DataSourceId', win32more.Foundation.LARGE_INTEGER),
        ('WimGuid', Guid),
        ('WimPath', win32more.Foundation.PWSTR),
        ('WimIndex', UInt32),
        ('Flags', UInt32),
    ]
    return WIM_ENTRY_INFO
def _define_WIM_EXTERNAL_FILE_INFO_head():
    class WIM_EXTERNAL_FILE_INFO(Structure):
        pass
    return WIM_EXTERNAL_FILE_INFO
def _define_WIM_EXTERNAL_FILE_INFO():
    WIM_EXTERNAL_FILE_INFO = win32more.Storage.FileSystem.WIM_EXTERNAL_FILE_INFO_head
    WIM_EXTERNAL_FILE_INFO._fields_ = [
        ('DataSourceId', win32more.Foundation.LARGE_INTEGER),
        ('ResourceHash', Byte * 20),
        ('Flags', UInt32),
    ]
    return WIM_EXTERNAL_FILE_INFO
WIN_STREAM_ID = UInt32
BACKUP_ALTERNATE_DATA = 4
BACKUP_DATA = 1
BACKUP_EA_DATA = 2
BACKUP_LINK = 5
BACKUP_OBJECT_ID = 7
BACKUP_PROPERTY_DATA = 6
BACKUP_REPARSE_DATA = 8
BACKUP_SECURITY_DATA = 3
BACKUP_SPARSE_BLOCK = 9
BACKUP_TXFS_DATA = 10
def _define_WIN32_FILE_ATTRIBUTE_DATA_head():
    class WIN32_FILE_ATTRIBUTE_DATA(Structure):
        pass
    return WIN32_FILE_ATTRIBUTE_DATA
def _define_WIN32_FILE_ATTRIBUTE_DATA():
    WIN32_FILE_ATTRIBUTE_DATA = win32more.Storage.FileSystem.WIN32_FILE_ATTRIBUTE_DATA_head
    WIN32_FILE_ATTRIBUTE_DATA._fields_ = [
        ('dwFileAttributes', UInt32),
        ('ftCreationTime', win32more.Foundation.FILETIME),
        ('ftLastAccessTime', win32more.Foundation.FILETIME),
        ('ftLastWriteTime', win32more.Foundation.FILETIME),
        ('nFileSizeHigh', UInt32),
        ('nFileSizeLow', UInt32),
    ]
    return WIN32_FILE_ATTRIBUTE_DATA
def _define_WIN32_FIND_DATAA_head():
    class WIN32_FIND_DATAA(Structure):
        pass
    return WIN32_FIND_DATAA
def _define_WIN32_FIND_DATAA():
    WIN32_FIND_DATAA = win32more.Storage.FileSystem.WIN32_FIND_DATAA_head
    WIN32_FIND_DATAA._fields_ = [
        ('dwFileAttributes', UInt32),
        ('ftCreationTime', win32more.Foundation.FILETIME),
        ('ftLastAccessTime', win32more.Foundation.FILETIME),
        ('ftLastWriteTime', win32more.Foundation.FILETIME),
        ('nFileSizeHigh', UInt32),
        ('nFileSizeLow', UInt32),
        ('dwReserved0', UInt32),
        ('dwReserved1', UInt32),
        ('cFileName', win32more.Foundation.CHAR * 260),
        ('cAlternateFileName', win32more.Foundation.CHAR * 14),
    ]
    return WIN32_FIND_DATAA
def _define_WIN32_FIND_DATAW_head():
    class WIN32_FIND_DATAW(Structure):
        pass
    return WIN32_FIND_DATAW
def _define_WIN32_FIND_DATAW():
    WIN32_FIND_DATAW = win32more.Storage.FileSystem.WIN32_FIND_DATAW_head
    WIN32_FIND_DATAW._fields_ = [
        ('dwFileAttributes', UInt32),
        ('ftCreationTime', win32more.Foundation.FILETIME),
        ('ftLastAccessTime', win32more.Foundation.FILETIME),
        ('ftLastWriteTime', win32more.Foundation.FILETIME),
        ('nFileSizeHigh', UInt32),
        ('nFileSizeLow', UInt32),
        ('dwReserved0', UInt32),
        ('dwReserved1', UInt32),
        ('cFileName', Char * 260),
        ('cAlternateFileName', Char * 14),
    ]
    return WIN32_FIND_DATAW
def _define_WIN32_FIND_STREAM_DATA_head():
    class WIN32_FIND_STREAM_DATA(Structure):
        pass
    return WIN32_FIND_STREAM_DATA
def _define_WIN32_FIND_STREAM_DATA():
    WIN32_FIND_STREAM_DATA = win32more.Storage.FileSystem.WIN32_FIND_STREAM_DATA_head
    WIN32_FIND_STREAM_DATA._fields_ = [
        ('StreamSize', win32more.Foundation.LARGE_INTEGER),
        ('cStreamName', Char * 296),
    ]
    return WIN32_FIND_STREAM_DATA
def _define_WIN32_STREAM_ID_head():
    class WIN32_STREAM_ID(Structure):
        pass
    return WIN32_STREAM_ID
def _define_WIN32_STREAM_ID():
    WIN32_STREAM_ID = win32more.Storage.FileSystem.WIN32_STREAM_ID_head
    WIN32_STREAM_ID._fields_ = [
        ('dwStreamId', win32more.Storage.FileSystem.WIN_STREAM_ID),
        ('dwStreamAttributes', UInt32),
        ('Size', win32more.Foundation.LARGE_INTEGER),
        ('dwStreamNameSize', UInt32),
        ('cStreamName', Char * 1),
    ]
    return WIN32_STREAM_ID
def _define_WOF_FILE_COMPRESSION_INFO_V0_head():
    class WOF_FILE_COMPRESSION_INFO_V0(Structure):
        pass
    return WOF_FILE_COMPRESSION_INFO_V0
def _define_WOF_FILE_COMPRESSION_INFO_V0():
    WOF_FILE_COMPRESSION_INFO_V0 = win32more.Storage.FileSystem.WOF_FILE_COMPRESSION_INFO_V0_head
    WOF_FILE_COMPRESSION_INFO_V0._fields_ = [
        ('Algorithm', UInt32),
    ]
    return WOF_FILE_COMPRESSION_INFO_V0
def _define_WOF_FILE_COMPRESSION_INFO_V1_head():
    class WOF_FILE_COMPRESSION_INFO_V1(Structure):
        pass
    return WOF_FILE_COMPRESSION_INFO_V1
def _define_WOF_FILE_COMPRESSION_INFO_V1():
    WOF_FILE_COMPRESSION_INFO_V1 = win32more.Storage.FileSystem.WOF_FILE_COMPRESSION_INFO_V1_head
    WOF_FILE_COMPRESSION_INFO_V1._fields_ = [
        ('Algorithm', UInt32),
        ('Flags', UInt32),
    ]
    return WOF_FILE_COMPRESSION_INFO_V1
def _define_WofEnumEntryProc():
    return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p)
def _define_WofEnumFilesProc():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,c_void_p,c_void_p)
__all__ = [
    "ACCESS_ALL",
    "ACCESS_ATRIB",
    "ACCESS_CREATE",
    "ACCESS_DELETE",
    "ACCESS_EXEC",
    "ACCESS_PERM",
    "ACCESS_READ",
    "ACCESS_WRITE",
    "AddLogContainer",
    "AddLogContainerSet",
    "AddUsersToEncryptedFile",
    "AdvanceLogBase",
    "AlignReservedLog",
    "AllocReservedLog",
    "AreFileApisANSI",
    "AreShortNamesEnabled",
    "BACKUP_ALTERNATE_DATA",
    "BACKUP_DATA",
    "BACKUP_EA_DATA",
    "BACKUP_LINK",
    "BACKUP_OBJECT_ID",
    "BACKUP_PROPERTY_DATA",
    "BACKUP_REPARSE_DATA",
    "BACKUP_SECURITY_DATA",
    "BACKUP_SPARSE_BLOCK",
    "BACKUP_TXFS_DATA",
    "BY_HANDLE_FILE_INFORMATION",
    "BackupRead",
    "BackupSeek",
    "BackupWrite",
    "BuildIoRingCancelRequest",
    "BuildIoRingReadFile",
    "BuildIoRingRegisterBuffers",
    "BuildIoRingRegisterFileHandles",
    "CACHE_ACCESS_CHECK",
    "CACHE_DESTROY_CALLBACK",
    "CACHE_KEY_COMPARE",
    "CACHE_KEY_HASH",
    "CACHE_READ_CALLBACK",
    "CALLBACK_CHUNK_FINISHED",
    "CALLBACK_STREAM_SWITCH",
    "CLAIMMEDIALABEL",
    "CLAIMMEDIALABELEX",
    "CLFS_BASELOG_EXTENSION",
    "CLFS_BLOCK_ALLOCATION",
    "CLFS_BLOCK_DEALLOCATION",
    "CLFS_CONTAINER_RELATIVE_PREFIX",
    "CLFS_CONTAINER_STREAM_PREFIX",
    "CLFS_CONTEXT_MODE",
    "CLFS_CONTEXT_MODE_ClfsContextForward",
    "CLFS_CONTEXT_MODE_ClfsContextNone",
    "CLFS_CONTEXT_MODE_ClfsContextPrevious",
    "CLFS_CONTEXT_MODE_ClfsContextUndoNext",
    "CLFS_FLAG",
    "CLFS_FLAG_FILTER_INTERMEDIATE_LEVEL",
    "CLFS_FLAG_FILTER_TOP_LEVEL",
    "CLFS_FLAG_FORCE_APPEND",
    "CLFS_FLAG_FORCE_FLUSH",
    "CLFS_FLAG_HIDDEN_SYSTEM_LOG",
    "CLFS_FLAG_IGNORE_SHARE_ACCESS",
    "CLFS_FLAG_MINIFILTER_LEVEL",
    "CLFS_FLAG_NON_REENTRANT_FILTER",
    "CLFS_FLAG_NO_FLAGS",
    "CLFS_FLAG_READ_IN_PROGRESS",
    "CLFS_FLAG_REENTRANT_FILE_SYSTEM",
    "CLFS_FLAG_REENTRANT_FILTER",
    "CLFS_FLAG_USE_RESERVATION",
    "CLFS_IOSTATS_CLASS",
    "CLFS_IOSTATS_CLASS_ClfsIoStatsDefault",
    "CLFS_IOSTATS_CLASS_ClfsIoStatsMax",
    "CLFS_LOG_ARCHIVE_MODE",
    "CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveDisabled",
    "CLFS_LOG_ARCHIVE_MODE_ClfsLogArchiveEnabled",
    "CLFS_LOG_NAME_INFORMATION",
    "CLFS_MARSHALLING_FLAG_DISABLE_BUFF_INIT",
    "CLFS_MARSHALLING_FLAG_NONE",
    "CLFS_MAX_CONTAINER_INFO",
    "CLFS_MGMT_CLIENT_REGISTRATION_VERSION",
    "CLFS_MGMT_NOTIFICATION",
    "CLFS_MGMT_NOTIFICATION_TYPE",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtAdvanceTailNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogFullHandlerNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogUnpinnedNotification",
    "CLFS_MGMT_NOTIFICATION_TYPE_ClfsMgmtLogWriteNotification",
    "CLFS_MGMT_POLICY",
    "CLFS_MGMT_POLICY_TYPE",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoGrow",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyAutoShrink",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyGrowthRate",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyInvalid",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyLogTail",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMaximumSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyMinimumSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerExtension",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerPrefix",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSize",
    "CLFS_MGMT_POLICY_TYPE_ClfsMgmtPolicyNewContainerSuffix",
    "CLFS_MGMT_POLICY_VERSION",
    "CLFS_NODE_ID",
    "CLFS_PHYSICAL_LSN_INFORMATION",
    "CLFS_SCAN_BACKWARD",
    "CLFS_SCAN_BUFFERED",
    "CLFS_SCAN_CLOSE",
    "CLFS_SCAN_FORWARD",
    "CLFS_SCAN_INIT",
    "CLFS_SCAN_INITIALIZED",
    "CLFS_STREAM_ID_INFORMATION",
    "CLSID_DiskQuotaControl",
    "CLS_ARCHIVE_DESCRIPTOR",
    "CLS_CONTAINER_INFORMATION",
    "CLS_CONTEXT_MODE",
    "CLS_CONTEXT_MODE_ClsContextForward",
    "CLS_CONTEXT_MODE_ClsContextNone",
    "CLS_CONTEXT_MODE_ClsContextPrevious",
    "CLS_CONTEXT_MODE_ClsContextUndoNext",
    "CLS_INFORMATION",
    "CLS_IOSTATS_CLASS",
    "CLS_IOSTATS_CLASS_ClsIoStatsDefault",
    "CLS_IOSTATS_CLASS_ClsIoStatsMax",
    "CLS_IO_STATISTICS",
    "CLS_IO_STATISTICS_HEADER",
    "CLS_LOG_INFORMATION_CLASS",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogBasicInformationPhysical",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalLsnInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogPhysicalNameInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogStreamIdentifierInformation",
    "CLS_LOG_INFORMATION_CLASS_ClfsLogSystemMarkingInformation",
    "CLS_LSN",
    "CLS_SCAN_CONTEXT",
    "CLS_WRITE_ENTRY",
    "COMPRESSION_FORMAT",
    "COMPRESSION_FORMAT_DEFAULT",
    "COMPRESSION_FORMAT_LZNT1",
    "COMPRESSION_FORMAT_NONE",
    "COMPRESSION_FORMAT_XP10",
    "COMPRESSION_FORMAT_XPRESS",
    "COMPRESSION_FORMAT_XPRESS_HUFF",
    "CONNECTION_INFO_0",
    "CONNECTION_INFO_1",
    "COPYFILE2_CALLBACK_CHUNK_FINISHED",
    "COPYFILE2_CALLBACK_CHUNK_STARTED",
    "COPYFILE2_CALLBACK_ERROR",
    "COPYFILE2_CALLBACK_MAX",
    "COPYFILE2_CALLBACK_NONE",
    "COPYFILE2_CALLBACK_POLL_CONTINUE",
    "COPYFILE2_CALLBACK_STREAM_FINISHED",
    "COPYFILE2_CALLBACK_STREAM_STARTED",
    "COPYFILE2_COPY_PHASE",
    "COPYFILE2_EXTENDED_PARAMETERS",
    "COPYFILE2_EXTENDED_PARAMETERS_V2",
    "COPYFILE2_MESSAGE",
    "COPYFILE2_MESSAGE_ACTION",
    "COPYFILE2_MESSAGE_TYPE",
    "COPYFILE2_PHASE_MAX",
    "COPYFILE2_PHASE_NAMEGRAFT_COPY",
    "COPYFILE2_PHASE_NONE",
    "COPYFILE2_PHASE_PREPARE_DEST",
    "COPYFILE2_PHASE_PREPARE_SOURCE",
    "COPYFILE2_PHASE_READ_SOURCE",
    "COPYFILE2_PHASE_SERVER_COPY",
    "COPYFILE2_PHASE_WRITE_DESTINATION",
    "COPYFILE2_PROGRESS_CANCEL",
    "COPYFILE2_PROGRESS_CONTINUE",
    "COPYFILE2_PROGRESS_PAUSE",
    "COPYFILE2_PROGRESS_QUIET",
    "COPYFILE2_PROGRESS_STOP",
    "CREATEFILE2_EXTENDED_PARAMETERS",
    "CREATE_ALWAYS",
    "CREATE_NEW",
    "CREATE_TAPE_PARTITION_METHOD",
    "CRM_PROTOCOL_DYNAMIC_MARSHAL_INFO",
    "CRM_PROTOCOL_EXPLICIT_MARSHAL_ONLY",
    "CRM_PROTOCOL_MAXIMUM_OPTION",
    "CSC_CACHE_AUTO_REINT",
    "CSC_CACHE_MANUAL_REINT",
    "CSC_CACHE_NONE",
    "CSC_CACHE_VDO",
    "CSC_MASK",
    "CSC_MASK_EXT",
    "CSV_BLOCK_AND_FILE_CACHE_CALLBACK_VERSION",
    "CSV_BLOCK_CACHE_CALLBACK_VERSION",
    "CheckNameLegalDOS8Dot3A",
    "CheckNameLegalDOS8Dot3W",
    "ClfsClientRecord",
    "ClfsContainerActive",
    "ClfsContainerActivePendingDelete",
    "ClfsContainerInactive",
    "ClfsContainerInitializing",
    "ClfsContainerPendingArchive",
    "ClfsContainerPendingArchiveAndDelete",
    "ClfsDataRecord",
    "ClfsNullRecord",
    "ClfsRestartRecord",
    "CloseAndResetLogFile",
    "CloseEncryptedFileRaw",
    "CloseIoRing",
    "ClsContainerActive",
    "ClsContainerActivePendingDelete",
    "ClsContainerInactive",
    "ClsContainerInitializing",
    "ClsContainerPendingArchive",
    "ClsContainerPendingArchiveAndDelete",
    "CommitComplete",
    "CommitEnlistment",
    "CommitTransaction",
    "CommitTransactionAsync",
    "CompareFileTime",
    "CopyFile2",
    "CopyFileA",
    "CopyFileExA",
    "CopyFileExW",
    "CopyFileFromAppW",
    "CopyFileTransactedA",
    "CopyFileTransactedW",
    "CopyFileW",
    "CopyLZFile",
    "CreateDirectoryA",
    "CreateDirectoryExA",
    "CreateDirectoryExW",
    "CreateDirectoryFromAppW",
    "CreateDirectoryTransactedA",
    "CreateDirectoryTransactedW",
    "CreateDirectoryW",
    "CreateEnlistment",
    "CreateFile2",
    "CreateFile2FromAppW",
    "CreateFileA",
    "CreateFileFromAppW",
    "CreateFileTransactedA",
    "CreateFileTransactedW",
    "CreateFileW",
    "CreateHardLinkA",
    "CreateHardLinkTransactedA",
    "CreateHardLinkTransactedW",
    "CreateHardLinkW",
    "CreateIoRing",
    "CreateLogContainerScanContext",
    "CreateLogFile",
    "CreateLogMarshallingArea",
    "CreateResourceManager",
    "CreateSymbolicLinkA",
    "CreateSymbolicLinkTransactedA",
    "CreateSymbolicLinkTransactedW",
    "CreateSymbolicLinkW",
    "CreateTapePartition",
    "CreateTransaction",
    "CreateTransactionManager",
    "DDD_EXACT_MATCH_ON_REMOVE",
    "DDD_LUID_BROADCAST_DRIVE",
    "DDD_NO_BROADCAST_SYSTEM",
    "DDD_RAW_TARGET_PATH",
    "DDD_REMOVE_DEFINITION",
    "DEFINE_DOS_DEVICE_FLAGS",
    "DELETE",
    "DISKQUOTA_FILESTATE_INCOMPLETE",
    "DISKQUOTA_FILESTATE_MASK",
    "DISKQUOTA_FILESTATE_REBUILDING",
    "DISKQUOTA_LOGFLAG_USER_LIMIT",
    "DISKQUOTA_LOGFLAG_USER_THRESHOLD",
    "DISKQUOTA_STATE_DISABLED",
    "DISKQUOTA_STATE_ENFORCE",
    "DISKQUOTA_STATE_MASK",
    "DISKQUOTA_STATE_TRACK",
    "DISKQUOTA_USERNAME_RESOLVE",
    "DISKQUOTA_USERNAME_RESOLVE_ASYNC",
    "DISKQUOTA_USERNAME_RESOLVE_NONE",
    "DISKQUOTA_USERNAME_RESOLVE_SYNC",
    "DISKQUOTA_USER_ACCOUNT_DELETED",
    "DISKQUOTA_USER_ACCOUNT_INVALID",
    "DISKQUOTA_USER_ACCOUNT_RESOLVED",
    "DISKQUOTA_USER_ACCOUNT_UNAVAILABLE",
    "DISKQUOTA_USER_ACCOUNT_UNKNOWN",
    "DISKQUOTA_USER_ACCOUNT_UNRESOLVED",
    "DISKQUOTA_USER_INFORMATION",
    "DISK_SPACE_INFORMATION",
    "DecryptFileA",
    "DecryptFileW",
    "DefineDosDeviceA",
    "DefineDosDeviceW",
    "DeleteFileA",
    "DeleteFileFromAppW",
    "DeleteFileTransactedA",
    "DeleteFileTransactedW",
    "DeleteFileW",
    "DeleteLogByHandle",
    "DeleteLogFile",
    "DeleteLogMarshallingArea",
    "DeleteVolumeMountPointA",
    "DeleteVolumeMountPointW",
    "DeregisterManageableLogClient",
    "DuplicateEncryptionInfoFile",
    "EA_CONTAINER_NAME",
    "EA_CONTAINER_SIZE",
    "EFS_CERTIFICATE_BLOB",
    "EFS_COMPATIBILITY_INFO",
    "EFS_COMPATIBILITY_VERSION_NCRYPT_PROTECTOR",
    "EFS_COMPATIBILITY_VERSION_PFILE_PROTECTOR",
    "EFS_DECRYPTION_STATUS_INFO",
    "EFS_EFS_SUBVER_EFS_CERT",
    "EFS_ENCRYPTION_STATUS_INFO",
    "EFS_HASH_BLOB",
    "EFS_KEY_INFO",
    "EFS_METADATA_ADD_USER",
    "EFS_METADATA_GENERAL_OP",
    "EFS_METADATA_REMOVE_USER",
    "EFS_METADATA_REPLACE_USER",
    "EFS_PFILE_SUBVER_APPX",
    "EFS_PFILE_SUBVER_RMS",
    "EFS_PIN_BLOB",
    "EFS_RPC_BLOB",
    "EFS_SUBVER_UNKNOWN",
    "EFS_VERSION_INFO",
    "ENCRYPTED_FILE_METADATA_SIGNATURE",
    "ENCRYPTION_CERTIFICATE",
    "ENCRYPTION_CERTIFICATE_HASH",
    "ENCRYPTION_CERTIFICATE_HASH_LIST",
    "ENCRYPTION_CERTIFICATE_LIST",
    "ENCRYPTION_PROTECTOR",
    "ENCRYPTION_PROTECTOR_LIST",
    "ENLISTMENT_MAXIMUM_OPTION",
    "ENLISTMENT_OBJECT_PATH",
    "ENLISTMENT_SUPERIOR",
    "ERASE_TAPE_TYPE",
    "EncryptFileA",
    "EncryptFileW",
    "EncryptionDisable",
    "EraseTape",
    "FCACHE_CREATE_CALLBACK",
    "FCACHE_RICHCREATE_CALLBACK",
    "FH_OVERLAPPED",
    "FILE_ACCESS_FLAGS",
    "FILE_ACTION",
    "FILE_ACTION_ADDED",
    "FILE_ACTION_MODIFIED",
    "FILE_ACTION_REMOVED",
    "FILE_ACTION_RENAMED_NEW_NAME",
    "FILE_ACTION_RENAMED_OLD_NAME",
    "FILE_ADD_FILE",
    "FILE_ADD_SUBDIRECTORY",
    "FILE_ALIGNMENT_INFO",
    "FILE_ALLOCATION_INFO",
    "FILE_ALL_ACCESS",
    "FILE_APPEND_DATA",
    "FILE_ATTRIBUTE_ARCHIVE",
    "FILE_ATTRIBUTE_COMPRESSED",
    "FILE_ATTRIBUTE_DEVICE",
    "FILE_ATTRIBUTE_DIRECTORY",
    "FILE_ATTRIBUTE_EA",
    "FILE_ATTRIBUTE_ENCRYPTED",
    "FILE_ATTRIBUTE_HIDDEN",
    "FILE_ATTRIBUTE_INTEGRITY_STREAM",
    "FILE_ATTRIBUTE_NORMAL",
    "FILE_ATTRIBUTE_NOT_CONTENT_INDEXED",
    "FILE_ATTRIBUTE_NO_SCRUB_DATA",
    "FILE_ATTRIBUTE_OFFLINE",
    "FILE_ATTRIBUTE_PINNED",
    "FILE_ATTRIBUTE_READONLY",
    "FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS",
    "FILE_ATTRIBUTE_RECALL_ON_OPEN",
    "FILE_ATTRIBUTE_REPARSE_POINT",
    "FILE_ATTRIBUTE_SPARSE_FILE",
    "FILE_ATTRIBUTE_SYSTEM",
    "FILE_ATTRIBUTE_TAG_INFO",
    "FILE_ATTRIBUTE_TEMPORARY",
    "FILE_ATTRIBUTE_UNPINNED",
    "FILE_ATTRIBUTE_VIRTUAL",
    "FILE_BASIC_INFO",
    "FILE_BEGIN",
    "FILE_COMPRESSION_INFO",
    "FILE_CREATE",
    "FILE_CREATE_PIPE_INSTANCE",
    "FILE_CREATION_DISPOSITION",
    "FILE_CURRENT",
    "FILE_DELETE_CHILD",
    "FILE_DEVICE_CD_ROM",
    "FILE_DEVICE_DISK",
    "FILE_DEVICE_DVD",
    "FILE_DEVICE_TAPE",
    "FILE_DEVICE_TYPE",
    "FILE_DISPOSITION_INFO",
    "FILE_END",
    "FILE_END_OF_FILE_INFO",
    "FILE_EXECUTE",
    "FILE_EXTENT",
    "FILE_FLAGS_AND_ATTRIBUTES",
    "FILE_FLAG_BACKUP_SEMANTICS",
    "FILE_FLAG_DELETE_ON_CLOSE",
    "FILE_FLAG_FIRST_PIPE_INSTANCE",
    "FILE_FLAG_NO_BUFFERING",
    "FILE_FLAG_OPEN_NO_RECALL",
    "FILE_FLAG_OPEN_REPARSE_POINT",
    "FILE_FLAG_OVERLAPPED",
    "FILE_FLAG_POSIX_SEMANTICS",
    "FILE_FLAG_RANDOM_ACCESS",
    "FILE_FLAG_SEQUENTIAL_SCAN",
    "FILE_FLAG_SESSION_AWARE",
    "FILE_FLAG_WRITE_THROUGH",
    "FILE_FULL_DIR_INFO",
    "FILE_GENERIC_EXECUTE",
    "FILE_GENERIC_READ",
    "FILE_GENERIC_WRITE",
    "FILE_ID_128",
    "FILE_ID_BOTH_DIR_INFO",
    "FILE_ID_DESCRIPTOR",
    "FILE_ID_EXTD_DIR_INFO",
    "FILE_ID_INFO",
    "FILE_ID_TYPE",
    "FILE_ID_TYPE_ExtendedFileIdType",
    "FILE_ID_TYPE_FileIdType",
    "FILE_ID_TYPE_MaximumFileIdType",
    "FILE_ID_TYPE_ObjectIdType",
    "FILE_INFO_2",
    "FILE_INFO_3",
    "FILE_INFO_BY_HANDLE_CLASS",
    "FILE_INFO_BY_HANDLE_CLASS_FileAlignmentInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileAllocationInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileAttributeTagInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileBasicInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileCaseSensitiveInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileCompressionInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileDispositionInfoEx",
    "FILE_INFO_BY_HANDLE_CLASS_FileEndOfFileInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileFullDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdBothDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdExtdDirectoryRestartInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIdInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileIoPriorityHintInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileNameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileNormalizedNameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRemoteProtocolInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRenameInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileRenameInfoEx",
    "FILE_INFO_BY_HANDLE_CLASS_FileStandardInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileStorageInfo",
    "FILE_INFO_BY_HANDLE_CLASS_FileStreamInfo",
    "FILE_INFO_BY_HANDLE_CLASS_MaximumFileInfoByHandleClass",
    "FILE_INFO_FLAGS_PERMISSIONS",
    "FILE_IO_PRIORITY_HINT_INFO",
    "FILE_LIST_DIRECTORY",
    "FILE_NAME",
    "FILE_NAME_INFO",
    "FILE_NAME_NORMALIZED",
    "FILE_NAME_OPENED",
    "FILE_NOTIFY_CHANGE",
    "FILE_NOTIFY_CHANGE_ATTRIBUTES",
    "FILE_NOTIFY_CHANGE_CREATION",
    "FILE_NOTIFY_CHANGE_DIR_NAME",
    "FILE_NOTIFY_CHANGE_FILE_NAME",
    "FILE_NOTIFY_CHANGE_LAST_ACCESS",
    "FILE_NOTIFY_CHANGE_LAST_WRITE",
    "FILE_NOTIFY_CHANGE_SECURITY",
    "FILE_NOTIFY_CHANGE_SIZE",
    "FILE_NOTIFY_EXTENDED_INFORMATION",
    "FILE_NOTIFY_INFORMATION",
    "FILE_OPEN",
    "FILE_OPEN_IF",
    "FILE_OVERWRITE",
    "FILE_OVERWRITE_IF",
    "FILE_PROVIDER_COMPRESSION_LZX",
    "FILE_PROVIDER_COMPRESSION_XPRESS16K",
    "FILE_PROVIDER_COMPRESSION_XPRESS4K",
    "FILE_PROVIDER_COMPRESSION_XPRESS8K",
    "FILE_READ_ATTRIBUTES",
    "FILE_READ_DATA",
    "FILE_READ_EA",
    "FILE_REMOTE_PROTOCOL_INFO",
    "FILE_RENAME_INFO",
    "FILE_SEGMENT_ELEMENT",
    "FILE_SHARE_DELETE",
    "FILE_SHARE_MODE",
    "FILE_SHARE_NONE",
    "FILE_SHARE_READ",
    "FILE_SHARE_WRITE",
    "FILE_STANDARD_INFO",
    "FILE_STORAGE_INFO",
    "FILE_STREAM_INFO",
    "FILE_SUPERSEDE",
    "FILE_TRAVERSE",
    "FILE_TYPE",
    "FILE_TYPE_CHAR",
    "FILE_TYPE_DISK",
    "FILE_TYPE_PIPE",
    "FILE_TYPE_REMOTE",
    "FILE_TYPE_UNKNOWN",
    "FILE_VER_GET_LOCALISED",
    "FILE_VER_GET_NEUTRAL",
    "FILE_VER_GET_PREFETCHED",
    "FILE_WRITE_ATTRIBUTES",
    "FILE_WRITE_DATA",
    "FILE_WRITE_EA",
    "FINDEX_INFO_LEVELS",
    "FINDEX_INFO_LEVELS_FindExInfoBasic",
    "FINDEX_INFO_LEVELS_FindExInfoMaxInfoLevel",
    "FINDEX_INFO_LEVELS_FindExInfoStandard",
    "FINDEX_SEARCH_OPS",
    "FINDEX_SEARCH_OPS_FindExSearchLimitToDevices",
    "FINDEX_SEARCH_OPS_FindExSearchLimitToDirectories",
    "FINDEX_SEARCH_OPS_FindExSearchMaxSearchOp",
    "FINDEX_SEARCH_OPS_FindExSearchNameMatch",
    "FIND_FIRST_EX_CASE_SENSITIVE",
    "FIND_FIRST_EX_FLAGS",
    "FIND_FIRST_EX_LARGE_FETCH",
    "FIND_FIRST_EX_ON_DISK_ENTRIES_ONLY",
    "FIO_CONTEXT",
    "FileEncryptionStatusA",
    "FileEncryptionStatusW",
    "FileTimeToLocalFileTime",
    "FindChangeNotificationHandle",
    "FindClose",
    "FindCloseChangeNotification",
    "FindFileHandle",
    "FindFileNameHandle",
    "FindFirstChangeNotificationA",
    "FindFirstChangeNotificationW",
    "FindFirstFileA",
    "FindFirstFileExA",
    "FindFirstFileExFromAppW",
    "FindFirstFileExW",
    "FindFirstFileNameTransactedW",
    "FindFirstFileNameW",
    "FindFirstFileTransactedA",
    "FindFirstFileTransactedW",
    "FindFirstFileW",
    "FindFirstStreamTransactedW",
    "FindFirstStreamW",
    "FindFirstVolumeA",
    "FindFirstVolumeMountPointA",
    "FindFirstVolumeMountPointW",
    "FindFirstVolumeW",
    "FindNextChangeNotification",
    "FindNextFileA",
    "FindNextFileNameW",
    "FindNextFileW",
    "FindNextStreamW",
    "FindNextVolumeA",
    "FindNextVolumeMountPointA",
    "FindNextVolumeMountPointW",
    "FindNextVolumeW",
    "FindStreamHandle",
    "FindVolumeClose",
    "FindVolumeHandle",
    "FindVolumeMointPointHandle",
    "FindVolumeMountPointClose",
    "FlushFileBuffers",
    "FlushLogBuffers",
    "FlushLogToLsn",
    "FreeEncryptedFileMetadata",
    "FreeEncryptionCertificateHashList",
    "FreeReservedLog",
    "GET_FILEEX_INFO_LEVELS",
    "GET_FILEEX_INFO_LEVELS_GetFileExInfoStandard",
    "GET_FILEEX_INFO_LEVELS_GetFileExMaxInfoLevel",
    "GET_FILE_VERSION_INFO_FLAGS",
    "GET_TAPE_DRIVE_INFORMATION",
    "GET_TAPE_DRIVE_PARAMETERS_OPERATION",
    "GET_TAPE_MEDIA_INFORMATION",
    "GetBinaryTypeA",
    "GetBinaryTypeW",
    "GetCompressedFileSizeA",
    "GetCompressedFileSizeTransactedA",
    "GetCompressedFileSizeTransactedW",
    "GetCompressedFileSizeW",
    "GetCurrentClockTransactionManager",
    "GetDiskFreeSpaceA",
    "GetDiskFreeSpaceExA",
    "GetDiskFreeSpaceExW",
    "GetDiskFreeSpaceW",
    "GetDiskSpaceInformationA",
    "GetDiskSpaceInformationW",
    "GetDriveTypeA",
    "GetDriveTypeW",
    "GetEncryptedFileMetadata",
    "GetEnlistmentId",
    "GetEnlistmentRecoveryInformation",
    "GetExpandedNameA",
    "GetExpandedNameW",
    "GetFileAttributesA",
    "GetFileAttributesExA",
    "GetFileAttributesExFromAppW",
    "GetFileAttributesExW",
    "GetFileAttributesTransactedA",
    "GetFileAttributesTransactedW",
    "GetFileAttributesW",
    "GetFileBandwidthReservation",
    "GetFileInformationByHandle",
    "GetFileInformationByHandleEx",
    "GetFileSize",
    "GetFileSizeEx",
    "GetFileTime",
    "GetFileType",
    "GetFileVersionInfoA",
    "GetFileVersionInfoExA",
    "GetFileVersionInfoExW",
    "GetFileVersionInfoSizeA",
    "GetFileVersionInfoSizeExA",
    "GetFileVersionInfoSizeExW",
    "GetFileVersionInfoSizeW",
    "GetFileVersionInfoW",
    "GetFinalPathNameByHandleA",
    "GetFinalPathNameByHandleW",
    "GetFullPathNameA",
    "GetFullPathNameTransactedA",
    "GetFullPathNameTransactedW",
    "GetFullPathNameW",
    "GetIoRingInfo",
    "GetLogContainerName",
    "GetLogFileInformation",
    "GetLogIoStatistics",
    "GetLogReservationInfo",
    "GetLogicalDriveStringsA",
    "GetLogicalDriveStringsW",
    "GetLogicalDrives",
    "GetLongPathNameA",
    "GetLongPathNameTransactedA",
    "GetLongPathNameTransactedW",
    "GetLongPathNameW",
    "GetNextLogArchiveExtent",
    "GetNotificationResourceManager",
    "GetNotificationResourceManagerAsync",
    "GetShortPathNameA",
    "GetShortPathNameW",
    "GetTapeParameters",
    "GetTapePosition",
    "GetTapeStatus",
    "GetTempFileNameA",
    "GetTempFileNameW",
    "GetTempPath2A",
    "GetTempPath2W",
    "GetTempPathA",
    "GetTempPathW",
    "GetTransactionId",
    "GetTransactionInformation",
    "GetTransactionManagerId",
    "GetVolumeInformationA",
    "GetVolumeInformationByHandleW",
    "GetVolumeInformationW",
    "GetVolumeNameForVolumeMountPointA",
    "GetVolumeNameForVolumeMountPointW",
    "GetVolumePathNameA",
    "GetVolumePathNameW",
    "GetVolumePathNamesForVolumeNameA",
    "GetVolumePathNamesForVolumeNameW",
    "HIORING__",
    "HandleLogFull",
    "IDiskQuotaControl",
    "IDiskQuotaEvents",
    "IDiskQuotaUser",
    "IDiskQuotaUserBatch",
    "IEnumDiskQuotaUsers",
    "INVALID_FILE_ATTRIBUTES",
    "INVALID_SET_FILE_POINTER",
    "IOCTL_VOLUME_ALLOCATE_BC_STREAM",
    "IOCTL_VOLUME_BASE",
    "IOCTL_VOLUME_BC_VERSION",
    "IOCTL_VOLUME_FREE_BC_STREAM",
    "IOCTL_VOLUME_GET_BC_PROPERTIES",
    "IOCTL_VOLUME_GET_CSVBLOCKCACHE_CALLBACK",
    "IOCTL_VOLUME_GET_GPT_ATTRIBUTES",
    "IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS",
    "IOCTL_VOLUME_IS_CLUSTERED",
    "IOCTL_VOLUME_IS_CSV",
    "IOCTL_VOLUME_IS_DYNAMIC",
    "IOCTL_VOLUME_IS_IO_CAPABLE",
    "IOCTL_VOLUME_IS_OFFLINE",
    "IOCTL_VOLUME_IS_PARTITION",
    "IOCTL_VOLUME_LOGICAL_TO_PHYSICAL",
    "IOCTL_VOLUME_OFFLINE",
    "IOCTL_VOLUME_ONLINE",
    "IOCTL_VOLUME_PHYSICAL_TO_LOGICAL",
    "IOCTL_VOLUME_POST_ONLINE",
    "IOCTL_VOLUME_PREPARE_FOR_CRITICAL_IO",
    "IOCTL_VOLUME_PREPARE_FOR_SHRINK",
    "IOCTL_VOLUME_QUERY_ALLOCATION_HINT",
    "IOCTL_VOLUME_QUERY_FAILOVER_SET",
    "IOCTL_VOLUME_QUERY_MINIMUM_SHRINK_SIZE",
    "IOCTL_VOLUME_QUERY_VOLUME_NUMBER",
    "IOCTL_VOLUME_READ_PLEX",
    "IOCTL_VOLUME_SET_GPT_ATTRIBUTES",
    "IOCTL_VOLUME_SUPPORTS_ONLINE_OFFLINE",
    "IOCTL_VOLUME_UPDATE_PROPERTIES",
    "IORING_BUFFER_INFO",
    "IORING_BUFFER_REF",
    "IORING_CAPABILITIES",
    "IORING_CQE",
    "IORING_CREATE_ADVISORY_FLAGS",
    "IORING_CREATE_ADVISORY_FLAGS_NONE",
    "IORING_CREATE_FLAGS",
    "IORING_CREATE_REQUIRED_FLAGS",
    "IORING_CREATE_REQUIRED_FLAGS_NONE",
    "IORING_FEATURE_FLAGS",
    "IORING_FEATURE_FLAGS_NONE",
    "IORING_FEATURE_SET_COMPLETION_EVENT",
    "IORING_FEATURE_UM_EMULATION",
    "IORING_HANDLE_REF",
    "IORING_INFO",
    "IORING_OP_CANCEL",
    "IORING_OP_CODE",
    "IORING_OP_NOP",
    "IORING_OP_READ",
    "IORING_OP_REGISTER_BUFFERS",
    "IORING_OP_REGISTER_FILES",
    "IORING_REF_KIND",
    "IORING_REF_RAW",
    "IORING_REF_REGISTERED",
    "IORING_REGISTERED_BUFFER",
    "IORING_SQE_FLAGS",
    "IORING_VERSION",
    "IORING_VERSION_1",
    "IORING_VERSION_INVALID",
    "IOSQE_FLAGS_NONE",
    "InstallLogPolicy",
    "IsIoRingOpSupported",
    "KCRM_MARSHAL_HEADER",
    "KCRM_PROTOCOL_BLOB",
    "KCRM_TRANSACTION_BLOB",
    "KTM_MARSHAL_BLOB_VERSION_MAJOR",
    "KTM_MARSHAL_BLOB_VERSION_MINOR",
    "LOCKFILE_EXCLUSIVE_LOCK",
    "LOCKFILE_FAIL_IMMEDIATELY",
    "LOCK_FILE_FLAGS",
    "LOG_MANAGEMENT_CALLBACKS",
    "LOG_POLICY_OVERWRITE",
    "LOG_POLICY_PERSIST",
    "LPPROGRESS_ROUTINE",
    "LPPROGRESS_ROUTINE_CALLBACK_REASON",
    "LZClose",
    "LZCopy",
    "LZDone",
    "LZERROR_BADINHANDLE",
    "LZERROR_BADOUTHANDLE",
    "LZERROR_BADVALUE",
    "LZERROR_GLOBALLOC",
    "LZERROR_GLOBLOCK",
    "LZERROR_READ",
    "LZERROR_UNKNOWNALG",
    "LZERROR_WRITE",
    "LZInit",
    "LZOPENFILE_STYLE",
    "LZOpenFileA",
    "LZOpenFileW",
    "LZRead",
    "LZSeek",
    "LZStart",
    "LocalFileTimeToFileTime",
    "LockFile",
    "LockFileEx",
    "LogTailAdvanceFailure",
    "LsnBlockOffset",
    "LsnContainer",
    "LsnCreate",
    "LsnEqual",
    "LsnGreater",
    "LsnIncrement",
    "LsnInvalid",
    "LsnLess",
    "LsnNull",
    "LsnRecordSequence",
    "MAXIMUM_REPARSE_DATA_BUFFER_SIZE",
    "MAXMEDIALABEL",
    "MAX_RESOURCEMANAGER_DESCRIPTION_LENGTH",
    "MAX_SID_SIZE",
    "MAX_TRANSACTION_DESCRIPTION_LENGTH",
    "MOVEFILE_COPY_ALLOWED",
    "MOVEFILE_CREATE_HARDLINK",
    "MOVEFILE_DELAY_UNTIL_REBOOT",
    "MOVEFILE_FAIL_IF_NOT_TRACKABLE",
    "MOVEFILE_REPLACE_EXISTING",
    "MOVEFILE_WRITE_THROUGH",
    "MOVE_FILE_FLAGS",
    "MediaLabelInfo",
    "MoveFileA",
    "MoveFileExA",
    "MoveFileExW",
    "MoveFileFromAppW",
    "MoveFileTransactedA",
    "MoveFileTransactedW",
    "MoveFileW",
    "MoveFileWithProgressA",
    "MoveFileWithProgressW",
    "NAME_CACHE_CONTEXT",
    "NTMSMLI_MAXAPPDESCR",
    "NTMSMLI_MAXIDSIZE",
    "NTMSMLI_MAXTYPE",
    "NTMS_ALLOCATE_ERROR_IF_UNAVAILABLE",
    "NTMS_ALLOCATE_FROMSCRATCH",
    "NTMS_ALLOCATE_NEW",
    "NTMS_ALLOCATE_NEXT",
    "NTMS_ALLOCATION_INFORMATION",
    "NTMS_APPLICATIONNAME_LENGTH",
    "NTMS_ASYNCOP_MOUNT",
    "NTMS_ASYNCSTATE_COMPLETE",
    "NTMS_ASYNCSTATE_INPROCESS",
    "NTMS_ASYNCSTATE_QUEUED",
    "NTMS_ASYNCSTATE_WAIT_OPERATOR",
    "NTMS_ASYNCSTATE_WAIT_RESOURCE",
    "NTMS_ASYNC_IO",
    "NTMS_BARCODESTATE_OK",
    "NTMS_BARCODESTATE_UNREADABLE",
    "NTMS_BARCODE_LENGTH",
    "NTMS_CHANGER",
    "NTMS_CHANGERINFORMATIONA",
    "NTMS_CHANGERINFORMATIONW",
    "NTMS_CHANGERTYPEINFORMATIONA",
    "NTMS_CHANGERTYPEINFORMATIONW",
    "NTMS_CHANGER_TYPE",
    "NTMS_COMPUTER",
    "NTMS_COMPUTERINFORMATION",
    "NTMS_COMPUTERNAME_LENGTH",
    "NTMS_CONTROL_ACCESS",
    "NTMS_CREATE_NEW",
    "NTMS_DEALLOCATE_TOSCRATCH",
    "NTMS_DESCRIPTION_LENGTH",
    "NTMS_DEVICENAME_LENGTH",
    "NTMS_DISMOUNT_DEFERRED",
    "NTMS_DISMOUNT_IMMEDIATE",
    "NTMS_DOORSTATE_CLOSED",
    "NTMS_DOORSTATE_OPEN",
    "NTMS_DOORSTATE_UNKNOWN",
    "NTMS_DRIVE",
    "NTMS_DRIVEINFORMATIONA",
    "NTMS_DRIVEINFORMATIONW",
    "NTMS_DRIVESTATE_BEING_CLEANED",
    "NTMS_DRIVESTATE_DISMOUNTABLE",
    "NTMS_DRIVESTATE_DISMOUNTED",
    "NTMS_DRIVESTATE_LOADED",
    "NTMS_DRIVESTATE_MOUNTED",
    "NTMS_DRIVESTATE_UNLOADED",
    "NTMS_DRIVETYPEINFORMATIONA",
    "NTMS_DRIVETYPEINFORMATIONW",
    "NTMS_DRIVE_TYPE",
    "NTMS_EJECT_ASK_USER",
    "NTMS_EJECT_FORCE",
    "NTMS_EJECT_IMMEDIATE",
    "NTMS_EJECT_QUEUE",
    "NTMS_EJECT_START",
    "NTMS_EJECT_STOP",
    "NTMS_ENUM_DEFAULT",
    "NTMS_ENUM_ROOTPOOL",
    "NTMS_ERROR_ON_DUPLICATE",
    "NTMS_EVENT_COMPLETE",
    "NTMS_EVENT_SIGNAL",
    "NTMS_FILESYSTEM_INFO",
    "NTMS_I1_LIBRARYINFORMATION",
    "NTMS_I1_LIBREQUESTINFORMATIONA",
    "NTMS_I1_LIBREQUESTINFORMATIONW",
    "NTMS_I1_MESSAGE_LENGTH",
    "NTMS_I1_OBJECTINFORMATIONA",
    "NTMS_I1_OBJECTINFORMATIONW",
    "NTMS_I1_OPREQUESTINFORMATIONA",
    "NTMS_I1_OPREQUESTINFORMATIONW",
    "NTMS_I1_PARTITIONINFORMATIONA",
    "NTMS_I1_PARTITIONINFORMATIONW",
    "NTMS_I1_PMIDINFORMATIONA",
    "NTMS_I1_PMIDINFORMATIONW",
    "NTMS_IEDOOR",
    "NTMS_IEDOORINFORMATION",
    "NTMS_IEPORT",
    "NTMS_IEPORTINFORMATION",
    "NTMS_INITIALIZING",
    "NTMS_INJECT_RETRACT",
    "NTMS_INJECT_START",
    "NTMS_INJECT_STARTMANY",
    "NTMS_INJECT_STOP",
    "NTMS_INVENTORY_DEFAULT",
    "NTMS_INVENTORY_FAST",
    "NTMS_INVENTORY_MAX",
    "NTMS_INVENTORY_NONE",
    "NTMS_INVENTORY_OMID",
    "NTMS_INVENTORY_SLOT",
    "NTMS_INVENTORY_STOP",
    "NTMS_LIBRARY",
    "NTMS_LIBRARYFLAG_AUTODETECTCHANGE",
    "NTMS_LIBRARYFLAG_CLEANERPRESENT",
    "NTMS_LIBRARYFLAG_FIXEDOFFLINE",
    "NTMS_LIBRARYFLAG_IGNORECLEANERUSESREMAINING",
    "NTMS_LIBRARYFLAG_RECOGNIZECLEANERBARCODE",
    "NTMS_LIBRARYINFORMATION",
    "NTMS_LIBRARYTYPE_OFFLINE",
    "NTMS_LIBRARYTYPE_ONLINE",
    "NTMS_LIBRARYTYPE_STANDALONE",
    "NTMS_LIBRARYTYPE_UNKNOWN",
    "NTMS_LIBREQFLAGS_NOAUTOPURGE",
    "NTMS_LIBREQFLAGS_NOFAILEDPURGE",
    "NTMS_LIBREQUEST",
    "NTMS_LIBREQUESTINFORMATIONA",
    "NTMS_LIBREQUESTINFORMATIONW",
    "NTMS_LMIDINFORMATION",
    "NTMS_LM_CANCELLED",
    "NTMS_LM_CLASSIFY",
    "NTMS_LM_CLEANDRIVE",
    "NTMS_LM_DEFERRED",
    "NTMS_LM_DEFFERED",
    "NTMS_LM_DISABLECHANGER",
    "NTMS_LM_DISABLEDRIVE",
    "NTMS_LM_DISABLELIBRARY",
    "NTMS_LM_DISABLEMEDIA",
    "NTMS_LM_DISMOUNT",
    "NTMS_LM_DOORACCESS",
    "NTMS_LM_EJECT",
    "NTMS_LM_EJECTCLEANER",
    "NTMS_LM_ENABLECHANGER",
    "NTMS_LM_ENABLEDRIVE",
    "NTMS_LM_ENABLELIBRARY",
    "NTMS_LM_ENABLEMEDIA",
    "NTMS_LM_FAILED",
    "NTMS_LM_INJECT",
    "NTMS_LM_INJECTCLEANER",
    "NTMS_LM_INPROCESS",
    "NTMS_LM_INVALID",
    "NTMS_LM_INVENTORY",
    "NTMS_LM_MAXWORKITEM",
    "NTMS_LM_MOUNT",
    "NTMS_LM_PASSED",
    "NTMS_LM_PROCESSOMID",
    "NTMS_LM_QUEUED",
    "NTMS_LM_RELEASECLEANER",
    "NTMS_LM_REMOVE",
    "NTMS_LM_RESERVECLEANER",
    "NTMS_LM_STOPPED",
    "NTMS_LM_UPDATEOMID",
    "NTMS_LM_WAITING",
    "NTMS_LM_WRITESCRATCH",
    "NTMS_LOGICAL_MEDIA",
    "NTMS_MAXATTR_LENGTH",
    "NTMS_MAXATTR_NAMELEN",
    "NTMS_MEDIAPOOLINFORMATION",
    "NTMS_MEDIARW_READONLY",
    "NTMS_MEDIARW_REWRITABLE",
    "NTMS_MEDIARW_UNKNOWN",
    "NTMS_MEDIARW_WRITEONCE",
    "NTMS_MEDIASTATE_IDLE",
    "NTMS_MEDIASTATE_INUSE",
    "NTMS_MEDIASTATE_LOADED",
    "NTMS_MEDIASTATE_MOUNTED",
    "NTMS_MEDIASTATE_OPERROR",
    "NTMS_MEDIASTATE_OPREQ",
    "NTMS_MEDIASTATE_UNLOADED",
    "NTMS_MEDIATYPEINFORMATION",
    "NTMS_MEDIA_POOL",
    "NTMS_MEDIA_TYPE",
    "NTMS_MESSAGE_LENGTH",
    "NTMS_MODIFY_ACCESS",
    "NTMS_MOUNT_ERROR_IF_OFFLINE",
    "NTMS_MOUNT_ERROR_IF_UNAVAILABLE",
    "NTMS_MOUNT_ERROR_NOT_AVAILABLE",
    "NTMS_MOUNT_ERROR_OFFLINE",
    "NTMS_MOUNT_INFORMATION",
    "NTMS_MOUNT_NOWAIT",
    "NTMS_MOUNT_READ",
    "NTMS_MOUNT_SPECIFIC_DRIVE",
    "NTMS_MOUNT_WRITE",
    "NTMS_NEEDS_SERVICE",
    "NTMS_NOTIFICATIONINFORMATION",
    "NTMS_NOT_PRESENT",
    "NTMS_NUMBER_OF_OBJECT_TYPES",
    "NTMS_OBJECT",
    "NTMS_OBJECTINFORMATIONA",
    "NTMS_OBJECTINFORMATIONW",
    "NTMS_OBJECTNAME_LENGTH",
    "NTMS_OBJ_DELETE",
    "NTMS_OBJ_INSERT",
    "NTMS_OBJ_UPDATE",
    "NTMS_OMIDLABELID_LENGTH",
    "NTMS_OMIDLABELINFO_LENGTH",
    "NTMS_OMIDLABELTYPE_LENGTH",
    "NTMS_OMID_TYPE",
    "NTMS_OMID_TYPE_FILESYSTEM_INFO",
    "NTMS_OMID_TYPE_RAW_LABEL",
    "NTMS_OPEN_ALWAYS",
    "NTMS_OPEN_EXISTING",
    "NTMS_OPREQFLAGS_NOALERTS",
    "NTMS_OPREQFLAGS_NOAUTOPURGE",
    "NTMS_OPREQFLAGS_NOFAILEDPURGE",
    "NTMS_OPREQFLAGS_NOTRAYICON",
    "NTMS_OPREQUEST",
    "NTMS_OPREQUESTINFORMATIONA",
    "NTMS_OPREQUESTINFORMATIONW",
    "NTMS_OPREQ_CLEANER",
    "NTMS_OPREQ_DEVICESERVICE",
    "NTMS_OPREQ_MESSAGE",
    "NTMS_OPREQ_MOVEMEDIA",
    "NTMS_OPREQ_NEWMEDIA",
    "NTMS_OPREQ_UNKNOWN",
    "NTMS_OPSTATE_ACTIVE",
    "NTMS_OPSTATE_COMPLETE",
    "NTMS_OPSTATE_INPROGRESS",
    "NTMS_OPSTATE_REFUSED",
    "NTMS_OPSTATE_SUBMITTED",
    "NTMS_OPSTATE_UNKNOWN",
    "NTMS_PARTITION",
    "NTMS_PARTITIONINFORMATIONA",
    "NTMS_PARTITIONINFORMATIONW",
    "NTMS_PARTSTATE_ALLOCATED",
    "NTMS_PARTSTATE_AVAILABLE",
    "NTMS_PARTSTATE_COMPLETE",
    "NTMS_PARTSTATE_DECOMMISSIONED",
    "NTMS_PARTSTATE_FOREIGN",
    "NTMS_PARTSTATE_IMPORT",
    "NTMS_PARTSTATE_INCOMPATIBLE",
    "NTMS_PARTSTATE_RESERVED",
    "NTMS_PARTSTATE_UNKNOWN",
    "NTMS_PARTSTATE_UNPREPARED",
    "NTMS_PHYSICAL_MEDIA",
    "NTMS_PMIDINFORMATIONA",
    "NTMS_PMIDINFORMATIONW",
    "NTMS_POOLHIERARCHY_LENGTH",
    "NTMS_POOLPOLICY_KEEPOFFLINEIMPORT",
    "NTMS_POOLPOLICY_PURGEOFFLINESCRATCH",
    "NTMS_POOLTYPE_APPLICATION",
    "NTMS_POOLTYPE_FOREIGN",
    "NTMS_POOLTYPE_IMPORT",
    "NTMS_POOLTYPE_SCRATCH",
    "NTMS_POOLTYPE_UNKNOWN",
    "NTMS_PORTCONTENT_EMPTY",
    "NTMS_PORTCONTENT_FULL",
    "NTMS_PORTCONTENT_UNKNOWN",
    "NTMS_PORTPOSITION_EXTENDED",
    "NTMS_PORTPOSITION_RETRACTED",
    "NTMS_PORTPOSITION_UNKNOWN",
    "NTMS_PRIORITY_DEFAULT",
    "NTMS_PRIORITY_HIGH",
    "NTMS_PRIORITY_HIGHEST",
    "NTMS_PRIORITY_LOW",
    "NTMS_PRIORITY_LOWEST",
    "NTMS_PRIORITY_NORMAL",
    "NTMS_PRODUCTNAME_LENGTH",
    "NTMS_READY",
    "NTMS_REVISION_LENGTH",
    "NTMS_SEQUENCE_LENGTH",
    "NTMS_SERIALNUMBER_LENGTH",
    "NTMS_SESSION_QUERYEXPEDITE",
    "NTMS_SLOTSTATE_EMPTY",
    "NTMS_SLOTSTATE_FULL",
    "NTMS_SLOTSTATE_NEEDSINVENTORY",
    "NTMS_SLOTSTATE_NOTPRESENT",
    "NTMS_SLOTSTATE_UNKNOWN",
    "NTMS_STORAGESLOT",
    "NTMS_STORAGESLOTINFORMATION",
    "NTMS_UIDEST_ADD",
    "NTMS_UIDEST_DELETE",
    "NTMS_UIDEST_DELETEALL",
    "NTMS_UIOPERATION_MAX",
    "NTMS_UITYPE_ERR",
    "NTMS_UITYPE_INFO",
    "NTMS_UITYPE_INVALID",
    "NTMS_UITYPE_MAX",
    "NTMS_UITYPE_REQ",
    "NTMS_UI_DESTINATION",
    "NTMS_UNKNOWN",
    "NTMS_UNKNOWN_DRIVE",
    "NTMS_USERNAME_LENGTH",
    "NTMS_USE_ACCESS",
    "NTMS_VENDORNAME_LENGTH",
    "NT_CREATE_FILE_DISPOSITION",
    "NetConnectionEnum",
    "NetFileClose",
    "NetFileEnum",
    "NetFileGetInfo",
    "NetServerAliasAdd",
    "NetServerAliasDel",
    "NetServerAliasEnum",
    "NetSessionDel",
    "NetSessionEnum",
    "NetSessionGetInfo",
    "NetShareAdd",
    "NetShareCheck",
    "NetShareDel",
    "NetShareDelEx",
    "NetShareDelSticky",
    "NetShareEnum",
    "NetShareEnumSticky",
    "NetShareGetInfo",
    "NetShareSetInfo",
    "NetStatisticsGet",
    "NtCreateFile",
    "NtmsAccessMask",
    "NtmsAllocateOptions",
    "NtmsAllocationPolicy",
    "NtmsAsyncOperations",
    "NtmsAsyncStatus",
    "NtmsBarCodeState",
    "NtmsCreateNtmsMediaOptions",
    "NtmsCreateOptions",
    "NtmsDeallocationPolicy",
    "NtmsDismountOptions",
    "NtmsDoorState",
    "NtmsDriveState",
    "NtmsDriveType",
    "NtmsEjectOperation",
    "NtmsEnumerateOption",
    "NtmsInjectOperation",
    "NtmsInventoryMethod",
    "NtmsLibRequestFlags",
    "NtmsLibraryFlags",
    "NtmsLibraryType",
    "NtmsLmOperation",
    "NtmsLmState",
    "NtmsMediaPoolPolicy",
    "NtmsMediaState",
    "NtmsMountOptions",
    "NtmsMountPriority",
    "NtmsNotificationOperations",
    "NtmsObjectsTypes",
    "NtmsOpRequestFlags",
    "NtmsOperationalState",
    "NtmsOpreqCommand",
    "NtmsOpreqState",
    "NtmsPartitionState",
    "NtmsPoolType",
    "NtmsPortContent",
    "NtmsPortPosition",
    "NtmsReadWriteCharacteristics",
    "NtmsSessionOptions",
    "NtmsSlotState",
    "NtmsUIOperations",
    "NtmsUITypes",
    "OFSTRUCT",
    "OF_CANCEL",
    "OF_CREATE",
    "OF_DELETE",
    "OF_EXIST",
    "OF_PARSE",
    "OF_PROMPT",
    "OF_READ",
    "OF_READWRITE",
    "OF_REOPEN",
    "OF_SHARE_COMPAT",
    "OF_SHARE_DENY_NONE",
    "OF_SHARE_DENY_READ",
    "OF_SHARE_DENY_WRITE",
    "OF_SHARE_EXCLUSIVE",
    "OF_VERIFY",
    "OF_WRITE",
    "OPEN_ALWAYS",
    "OPEN_EXISTING",
    "OpenEncryptedFileRawA",
    "OpenEncryptedFileRawW",
    "OpenEnlistment",
    "OpenFile",
    "OpenFileById",
    "OpenResourceManager",
    "OpenTransaction",
    "OpenTransactionManager",
    "OpenTransactionManagerById",
    "PARTITION_BASIC_DATA_GUID",
    "PARTITION_BSP_GUID",
    "PARTITION_CLUSTER_GUID",
    "PARTITION_DPP_GUID",
    "PARTITION_ENTRY_UNUSED_GUID",
    "PARTITION_LDM_DATA_GUID",
    "PARTITION_LDM_METADATA_GUID",
    "PARTITION_LEGACY_BL_GUID",
    "PARTITION_LEGACY_BL_GUID_BACKUP",
    "PARTITION_MAIN_OS_GUID",
    "PARTITION_MSFT_RECOVERY_GUID",
    "PARTITION_MSFT_RESERVED_GUID",
    "PARTITION_MSFT_SNAPSHOT_GUID",
    "PARTITION_OS_DATA_GUID",
    "PARTITION_PATCH_GUID",
    "PARTITION_PRE_INSTALLED_GUID",
    "PARTITION_SERVICING_FILES_GUID",
    "PARTITION_SERVICING_METADATA_GUID",
    "PARTITION_SERVICING_RESERVE_GUID",
    "PARTITION_SERVICING_STAGING_ROOT_GUID",
    "PARTITION_SPACES_DATA_GUID",
    "PARTITION_SPACES_GUID",
    "PARTITION_SYSTEM_GUID",
    "PARTITION_WINDOWS_SYSTEM_GUID",
    "PCLFS_COMPLETION_ROUTINE",
    "PCOPYFILE2_PROGRESS_ROUTINE",
    "PERM_FILE_CREATE",
    "PERM_FILE_READ",
    "PERM_FILE_WRITE",
    "PFE_EXPORT_FUNC",
    "PFE_IMPORT_FUNC",
    "PFN_IO_COMPLETION",
    "PIPE_ACCESS_DUPLEX",
    "PIPE_ACCESS_INBOUND",
    "PIPE_ACCESS_OUTBOUND",
    "PLOG_FULL_HANDLER_CALLBACK",
    "PLOG_TAIL_ADVANCE_CALLBACK",
    "PLOG_UNPINNED_CALLBACK",
    "PREPARE_TAPE_OPERATION",
    "PRIORITY_HINT",
    "PRIORITY_HINT_IoPriorityHintLow",
    "PRIORITY_HINT_IoPriorityHintNormal",
    "PRIORITY_HINT_IoPriorityHintVeryLow",
    "PRIORITY_HINT_MaximumIoPriorityHintType",
    "PopIoRingCompletion",
    "PrePrepareComplete",
    "PrePrepareEnlistment",
    "PrepareComplete",
    "PrepareEnlistment",
    "PrepareLogArchive",
    "PrepareTape",
    "QUIC",
    "QueryDosDeviceA",
    "QueryDosDeviceW",
    "QueryIoRingCapabilities",
    "QueryLogPolicy",
    "QueryRecoveryAgentsOnEncryptedFile",
    "QueryUsersOnEncryptedFile",
    "READ_CONTROL",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyExtendedInformation",
    "READ_DIRECTORY_NOTIFY_INFORMATION_CLASS_ReadDirectoryNotifyInformation",
    "REPARSE_GUID_DATA_BUFFER",
    "REPLACEFILE_IGNORE_ACL_ERRORS",
    "REPLACEFILE_IGNORE_MERGE_ERRORS",
    "REPLACEFILE_WRITE_THROUGH",
    "REPLACE_FILE_FLAGS",
    "RESOURCE_MANAGER_COMMUNICATION",
    "RESOURCE_MANAGER_MAXIMUM_OPTION",
    "RESOURCE_MANAGER_OBJECT_PATH",
    "RESOURCE_MANAGER_VOLATILE",
    "ReOpenFile",
    "ReadDirectoryChangesExW",
    "ReadDirectoryChangesW",
    "ReadEncryptedFileRaw",
    "ReadFile",
    "ReadFileEx",
    "ReadFileScatter",
    "ReadLogArchiveMetadata",
    "ReadLogNotification",
    "ReadLogRecord",
    "ReadLogRestartArea",
    "ReadNextLogRecord",
    "ReadOnlyEnlistment",
    "ReadPreviousLogRestartArea",
    "RecoverEnlistment",
    "RecoverResourceManager",
    "RecoverTransactionManager",
    "RegisterForLogWriteNotification",
    "RegisterManageableLogClient",
    "RemoveDirectoryA",
    "RemoveDirectoryFromAppW",
    "RemoveDirectoryTransactedA",
    "RemoveDirectoryTransactedW",
    "RemoveDirectoryW",
    "RemoveLogContainer",
    "RemoveLogContainerSet",
    "RemoveLogPolicy",
    "RemoveUsersFromEncryptedFile",
    "RenameTransactionManager",
    "ReplaceFileA",
    "ReplaceFileFromAppW",
    "ReplaceFileW",
    "ReserveAndAppendLog",
    "ReserveAndAppendLogAligned",
    "RollbackComplete",
    "RollbackEnlistment",
    "RollbackTransaction",
    "RollbackTransactionAsync",
    "RollforwardTransactionManager",
    "SECURITY_ANONYMOUS",
    "SECURITY_CONTEXT_TRACKING",
    "SECURITY_DELEGATION",
    "SECURITY_EFFECTIVE_ONLY",
    "SECURITY_IDENTIFICATION",
    "SECURITY_IMPERSONATION",
    "SECURITY_SQOS_PRESENT",
    "SECURITY_VALID_SQOS_FLAGS",
    "SERVER_ALIAS_INFO_0",
    "SERVER_CERTIFICATE_INFO_0",
    "SERVER_CERTIFICATE_TYPE",
    "SESI1_NUM_ELEMENTS",
    "SESI2_NUM_ELEMENTS",
    "SESSION_INFO_0",
    "SESSION_INFO_1",
    "SESSION_INFO_10",
    "SESSION_INFO_2",
    "SESSION_INFO_502",
    "SESSION_INFO_USER_FLAGS",
    "SESS_GUEST",
    "SESS_NOENCRYPTION",
    "SET_FILE_POINTER_MOVE_METHOD",
    "SET_TAPE_DRIVE_INFORMATION",
    "SET_TAPE_MEDIA_INFORMATION",
    "SHARE_CURRENT_USES_PARMNUM",
    "SHARE_FILE_SD_PARMNUM",
    "SHARE_INFO_0",
    "SHARE_INFO_1",
    "SHARE_INFO_1004",
    "SHARE_INFO_1005",
    "SHARE_INFO_1006",
    "SHARE_INFO_1501",
    "SHARE_INFO_1503",
    "SHARE_INFO_2",
    "SHARE_INFO_501",
    "SHARE_INFO_502",
    "SHARE_INFO_503",
    "SHARE_INFO_PERMISSIONS",
    "SHARE_MAX_USES_PARMNUM",
    "SHARE_NETNAME_PARMNUM",
    "SHARE_PASSWD_PARMNUM",
    "SHARE_PATH_PARMNUM",
    "SHARE_PERMISSIONS_PARMNUM",
    "SHARE_REMARK_PARMNUM",
    "SHARE_SERVER_PARMNUM",
    "SHARE_TYPE",
    "SHARE_TYPE_PARMNUM",
    "SHI1005_FLAGS_ACCESS_BASED_DIRECTORY_ENUM",
    "SHI1005_FLAGS_ALLOW_NAMESPACE_CACHING",
    "SHI1005_FLAGS_CLUSTER_MANAGED",
    "SHI1005_FLAGS_COMPRESS_DATA",
    "SHI1005_FLAGS_DFS",
    "SHI1005_FLAGS_DFS_ROOT",
    "SHI1005_FLAGS_DISABLE_CLIENT_BUFFERING",
    "SHI1005_FLAGS_ENABLE_CA",
    "SHI1005_FLAGS_ENABLE_HASH",
    "SHI1005_FLAGS_ENCRYPT_DATA",
    "SHI1005_FLAGS_FORCE_LEVELII_OPLOCK",
    "SHI1005_FLAGS_FORCE_SHARED_DELETE",
    "SHI1005_FLAGS_IDENTITY_REMOTING",
    "SHI1005_FLAGS_RESERVED",
    "SHI1005_FLAGS_RESTRICT_EXCLUSIVE_OPENS",
    "SHI1_NUM_ELEMENTS",
    "SHI2_NUM_ELEMENTS",
    "SHI_USES_UNLIMITED",
    "SPECIFIC_RIGHTS_ALL",
    "STANDARD_RIGHTS_ALL",
    "STANDARD_RIGHTS_EXECUTE",
    "STANDARD_RIGHTS_READ",
    "STANDARD_RIGHTS_REQUIRED",
    "STANDARD_RIGHTS_WRITE",
    "STATSOPT_CLR",
    "STAT_SERVER_0",
    "STAT_WORKSTATION_0",
    "STORAGE_BUS_TYPE",
    "STORAGE_BUS_TYPE_BusType1394",
    "STORAGE_BUS_TYPE_BusTypeAta",
    "STORAGE_BUS_TYPE_BusTypeAtapi",
    "STORAGE_BUS_TYPE_BusTypeFibre",
    "STORAGE_BUS_TYPE_BusTypeFileBackedVirtual",
    "STORAGE_BUS_TYPE_BusTypeMax",
    "STORAGE_BUS_TYPE_BusTypeMaxReserved",
    "STORAGE_BUS_TYPE_BusTypeMmc",
    "STORAGE_BUS_TYPE_BusTypeNvme",
    "STORAGE_BUS_TYPE_BusTypeRAID",
    "STORAGE_BUS_TYPE_BusTypeSCM",
    "STORAGE_BUS_TYPE_BusTypeSas",
    "STORAGE_BUS_TYPE_BusTypeSata",
    "STORAGE_BUS_TYPE_BusTypeScsi",
    "STORAGE_BUS_TYPE_BusTypeSd",
    "STORAGE_BUS_TYPE_BusTypeSpaces",
    "STORAGE_BUS_TYPE_BusTypeSsa",
    "STORAGE_BUS_TYPE_BusTypeUfs",
    "STORAGE_BUS_TYPE_BusTypeUnknown",
    "STORAGE_BUS_TYPE_BusTypeUsb",
    "STORAGE_BUS_TYPE_BusTypeVirtual",
    "STORAGE_BUS_TYPE_BusTypeiScsi",
    "STREAM_INFO_LEVELS",
    "STREAM_INFO_LEVELS_FindStreamInfoMaxInfoLevel",
    "STREAM_INFO_LEVELS_FindStreamInfoStandard",
    "STYPE_DEVICE",
    "STYPE_DISKTREE",
    "STYPE_IPC",
    "STYPE_MASK",
    "STYPE_PRINTQ",
    "STYPE_RESERVED1",
    "STYPE_RESERVED2",
    "STYPE_RESERVED3",
    "STYPE_RESERVED4",
    "STYPE_RESERVED5",
    "STYPE_RESERVED_ALL",
    "STYPE_SPECIAL",
    "STYPE_TEMPORARY",
    "SYMBOLIC_LINK_FLAGS",
    "SYMBOLIC_LINK_FLAG_ALLOW_UNPRIVILEGED_CREATE",
    "SYMBOLIC_LINK_FLAG_DIRECTORY",
    "SYNCHRONIZE",
    "ScanLogContainers",
    "SearchPathA",
    "SearchPathW",
    "SetEncryptedFileMetadata",
    "SetEndOfFile",
    "SetEndOfLog",
    "SetEnlistmentRecoveryInformation",
    "SetFileApisToANSI",
    "SetFileApisToOEM",
    "SetFileAttributesA",
    "SetFileAttributesFromAppW",
    "SetFileAttributesTransactedA",
    "SetFileAttributesTransactedW",
    "SetFileAttributesW",
    "SetFileBandwidthReservation",
    "SetFileCompletionNotificationModes",
    "SetFileInformationByHandle",
    "SetFileIoOverlappedRange",
    "SetFilePointer",
    "SetFilePointerEx",
    "SetFileShortNameA",
    "SetFileShortNameW",
    "SetFileTime",
    "SetFileValidData",
    "SetIoRingCompletionEvent",
    "SetLogArchiveMode",
    "SetLogArchiveTail",
    "SetLogFileSizeWithPolicy",
    "SetResourceManagerCompletionPort",
    "SetSearchPathMode",
    "SetTapeParameters",
    "SetTapePosition",
    "SetTransactionInformation",
    "SetUserFileEncryptionKey",
    "SetUserFileEncryptionKeyEx",
    "SetVolumeLabelA",
    "SetVolumeLabelW",
    "SetVolumeMountPointA",
    "SetVolumeMountPointW",
    "SinglePhaseReject",
    "SubmitIoRing",
    "TAPEMARK_TYPE",
    "TAPE_ABSOLUTE_BLOCK",
    "TAPE_ABSOLUTE_POSITION",
    "TAPE_ERASE",
    "TAPE_ERASE_LONG",
    "TAPE_ERASE_SHORT",
    "TAPE_FILEMARKS",
    "TAPE_FIXED_PARTITIONS",
    "TAPE_FORMAT",
    "TAPE_GET_POSITION",
    "TAPE_INFORMATION_TYPE",
    "TAPE_INITIATOR_PARTITIONS",
    "TAPE_LOAD",
    "TAPE_LOCK",
    "TAPE_LOGICAL_BLOCK",
    "TAPE_LOGICAL_POSITION",
    "TAPE_LONG_FILEMARKS",
    "TAPE_POSITION_METHOD",
    "TAPE_POSITION_TYPE",
    "TAPE_PREPARE",
    "TAPE_REWIND",
    "TAPE_SELECT_PARTITIONS",
    "TAPE_SETMARKS",
    "TAPE_SET_POSITION",
    "TAPE_SHORT_FILEMARKS",
    "TAPE_SPACE_END_OF_DATA",
    "TAPE_SPACE_FILEMARKS",
    "TAPE_SPACE_RELATIVE_BLOCKS",
    "TAPE_SPACE_SEQUENTIAL_FMKS",
    "TAPE_SPACE_SEQUENTIAL_SMKS",
    "TAPE_SPACE_SETMARKS",
    "TAPE_TENSION",
    "TAPE_UNLOAD",
    "TAPE_UNLOCK",
    "TAPE_WRITE_MARKS",
    "TRANSACTIONMANAGER_OBJECT_PATH",
    "TRANSACTION_DO_NOT_PROMOTE",
    "TRANSACTION_MANAGER_COMMIT_DEFAULT",
    "TRANSACTION_MANAGER_COMMIT_LOWEST",
    "TRANSACTION_MANAGER_COMMIT_SYSTEM_HIVES",
    "TRANSACTION_MANAGER_COMMIT_SYSTEM_VOLUME",
    "TRANSACTION_MANAGER_CORRUPT_FOR_PROGRESS",
    "TRANSACTION_MANAGER_CORRUPT_FOR_RECOVERY",
    "TRANSACTION_MANAGER_MAXIMUM_OPTION",
    "TRANSACTION_MANAGER_VOLATILE",
    "TRANSACTION_MAXIMUM_OPTION",
    "TRANSACTION_NOTIFICATION",
    "TRANSACTION_NOTIFICATION_MARSHAL_ARGUMENT",
    "TRANSACTION_NOTIFICATION_PROPAGATE_ARGUMENT",
    "TRANSACTION_NOTIFICATION_RECOVERY_ARGUMENT",
    "TRANSACTION_NOTIFICATION_SAVEPOINT_ARGUMENT",
    "TRANSACTION_NOTIFICATION_TM_ONLINE_ARGUMENT",
    "TRANSACTION_NOTIFICATION_TM_ONLINE_FLAG_IS_CLUSTERED",
    "TRANSACTION_NOTIFY_COMMIT",
    "TRANSACTION_NOTIFY_COMMIT_COMPLETE",
    "TRANSACTION_NOTIFY_COMMIT_FINALIZE",
    "TRANSACTION_NOTIFY_COMMIT_REQUEST",
    "TRANSACTION_NOTIFY_DELEGATE_COMMIT",
    "TRANSACTION_NOTIFY_ENLIST_MASK",
    "TRANSACTION_NOTIFY_ENLIST_PREPREPARE",
    "TRANSACTION_NOTIFY_INDOUBT",
    "TRANSACTION_NOTIFY_LAST_RECOVER",
    "TRANSACTION_NOTIFY_MARSHAL",
    "TRANSACTION_NOTIFY_MASK",
    "TRANSACTION_NOTIFY_PREPARE",
    "TRANSACTION_NOTIFY_PREPARE_COMPLETE",
    "TRANSACTION_NOTIFY_PREPREPARE",
    "TRANSACTION_NOTIFY_PREPREPARE_COMPLETE",
    "TRANSACTION_NOTIFY_PROMOTE",
    "TRANSACTION_NOTIFY_PROMOTE_NEW",
    "TRANSACTION_NOTIFY_PROPAGATE_PULL",
    "TRANSACTION_NOTIFY_PROPAGATE_PUSH",
    "TRANSACTION_NOTIFY_RECOVER",
    "TRANSACTION_NOTIFY_RECOVER_QUERY",
    "TRANSACTION_NOTIFY_REQUEST_OUTCOME",
    "TRANSACTION_NOTIFY_RM_DISCONNECTED",
    "TRANSACTION_NOTIFY_ROLLBACK",
    "TRANSACTION_NOTIFY_ROLLBACK_COMPLETE",
    "TRANSACTION_NOTIFY_SINGLE_PHASE_COMMIT",
    "TRANSACTION_NOTIFY_TM_ONLINE",
    "TRANSACTION_OBJECT_PATH",
    "TRANSACTION_OUTCOME",
    "TRANSACTION_OUTCOME_TransactionOutcomeAborted",
    "TRANSACTION_OUTCOME_TransactionOutcomeCommitted",
    "TRANSACTION_OUTCOME_TransactionOutcomeUndetermined",
    "TRUNCATE_EXISTING",
    "TXFS_MINIVERSION",
    "TXFS_MINIVERSION_COMMITTED_VIEW",
    "TXFS_MINIVERSION_DEFAULT_VIEW",
    "TXFS_MINIVERSION_DIRTY_VIEW",
    "TXF_ID",
    "TXF_LOG_RECORD_AFFECTED_FILE",
    "TXF_LOG_RECORD_BASE",
    "TXF_LOG_RECORD_GENERIC_TYPE_ABORT",
    "TXF_LOG_RECORD_GENERIC_TYPE_COMMIT",
    "TXF_LOG_RECORD_GENERIC_TYPE_DATA",
    "TXF_LOG_RECORD_GENERIC_TYPE_PREPARE",
    "TXF_LOG_RECORD_TRUNCATE",
    "TXF_LOG_RECORD_TYPE",
    "TXF_LOG_RECORD_TYPE_AFFECTED_FILE",
    "TXF_LOG_RECORD_TYPE_TRUNCATE",
    "TXF_LOG_RECORD_TYPE_WRITE",
    "TXF_LOG_RECORD_WRITE",
    "TerminateLogArchive",
    "TerminateReadLog",
    "TruncateLog",
    "TxfGetThreadMiniVersionForCreate",
    "TxfLogCreateFileReadContext",
    "TxfLogCreateRangeReadContext",
    "TxfLogDestroyReadContext",
    "TxfLogReadRecords",
    "TxfLogRecordGetFileName",
    "TxfLogRecordGetGenericType",
    "TxfReadMetadataInfo",
    "TxfSetThreadMiniVersionForCreate",
    "UnlockFile",
    "UnlockFileEx",
    "VER_FIND_FILE_FLAGS",
    "VER_FIND_FILE_STATUS",
    "VER_INSTALL_FILE_FLAGS",
    "VER_INSTALL_FILE_STATUS",
    "VFFF_ISSHAREDFILE",
    "VFF_BUFFTOOSMALL",
    "VFF_CURNEDEST",
    "VFF_FILEINUSE",
    "VFT2_DRV_COMM",
    "VFT2_DRV_DISPLAY",
    "VFT2_DRV_INPUTMETHOD",
    "VFT2_DRV_INSTALLABLE",
    "VFT2_DRV_KEYBOARD",
    "VFT2_DRV_LANGUAGE",
    "VFT2_DRV_MOUSE",
    "VFT2_DRV_NETWORK",
    "VFT2_DRV_PRINTER",
    "VFT2_DRV_SOUND",
    "VFT2_DRV_SYSTEM",
    "VFT2_DRV_VERSIONED_PRINTER",
    "VFT2_FONT_RASTER",
    "VFT2_FONT_TRUETYPE",
    "VFT2_FONT_VECTOR",
    "VFT2_UNKNOWN",
    "VFT_APP",
    "VFT_DLL",
    "VFT_DRV",
    "VFT_FONT",
    "VFT_STATIC_LIB",
    "VFT_UNKNOWN",
    "VFT_VXD",
    "VIFF_DONTDELETEOLD",
    "VIFF_FORCEINSTALL",
    "VIF_ACCESSVIOLATION",
    "VIF_BUFFTOOSMALL",
    "VIF_CANNOTCREATE",
    "VIF_CANNOTDELETE",
    "VIF_CANNOTDELETECUR",
    "VIF_CANNOTLOADCABINET",
    "VIF_CANNOTLOADLZ32",
    "VIF_CANNOTREADDST",
    "VIF_CANNOTREADSRC",
    "VIF_CANNOTRENAME",
    "VIF_DIFFCODEPG",
    "VIF_DIFFLANG",
    "VIF_DIFFTYPE",
    "VIF_FILEINUSE",
    "VIF_MISMATCH",
    "VIF_OUTOFMEMORY",
    "VIF_OUTOFSPACE",
    "VIF_SHARINGVIOLATION",
    "VIF_SRCOLD",
    "VIF_TEMPFILE",
    "VIF_WRITEPROT",
    "VOLUME_ALLOCATE_BC_STREAM_INPUT",
    "VOLUME_ALLOCATE_BC_STREAM_OUTPUT",
    "VOLUME_ALLOCATION_HINT_INPUT",
    "VOLUME_ALLOCATION_HINT_OUTPUT",
    "VOLUME_CRITICAL_IO",
    "VOLUME_FAILOVER_SET",
    "VOLUME_GET_BC_PROPERTIES_INPUT",
    "VOLUME_GET_BC_PROPERTIES_OUTPUT",
    "VOLUME_LOGICAL_OFFSET",
    "VOLUME_NUMBER",
    "VOLUME_PHYSICAL_OFFSET",
    "VOLUME_PHYSICAL_OFFSETS",
    "VOLUME_READ_PLEX_INPUT",
    "VOLUME_SET_GPT_ATTRIBUTES_INFORMATION",
    "VOLUME_SHRINK_INFO",
    "VOS_DOS",
    "VOS_DOS_WINDOWS16",
    "VOS_DOS_WINDOWS32",
    "VOS_NT",
    "VOS_NT_WINDOWS32",
    "VOS_OS216",
    "VOS_OS216_PM16",
    "VOS_OS232",
    "VOS_OS232_PM32",
    "VOS_UNKNOWN",
    "VOS_WINCE",
    "VOS__BASE",
    "VOS__PM16",
    "VOS__PM32",
    "VOS__WINDOWS16",
    "VOS__WINDOWS32",
    "VS_FFI_FILEFLAGSMASK",
    "VS_FFI_SIGNATURE",
    "VS_FFI_STRUCVERSION",
    "VS_FF_DEBUG",
    "VS_FF_INFOINFERRED",
    "VS_FF_PATCHED",
    "VS_FF_PRERELEASE",
    "VS_FF_PRIVATEBUILD",
    "VS_FF_SPECIALBUILD",
    "VS_FIXEDFILEINFO",
    "VS_FIXEDFILEINFO_FILE_FLAGS",
    "VS_FIXEDFILEINFO_FILE_OS",
    "VS_FIXEDFILEINFO_FILE_SUBTYPE",
    "VS_FIXEDFILEINFO_FILE_TYPE",
    "VS_USER_DEFINED",
    "VS_VERSION_INFO",
    "ValidateLog",
    "VerFindFileA",
    "VerFindFileW",
    "VerInstallFileA",
    "VerInstallFileW",
    "VerLanguageNameA",
    "VerLanguageNameW",
    "VerQueryValueA",
    "VerQueryValueW",
    "WIM_BOOT_NOT_OS_WIM",
    "WIM_BOOT_OS_WIM",
    "WIM_ENTRY_FLAG_NOT_ACTIVE",
    "WIM_ENTRY_FLAG_SUSPENDED",
    "WIM_ENTRY_INFO",
    "WIM_EXTERNAL_FILE_INFO",
    "WIM_EXTERNAL_FILE_INFO_FLAG_NOT_ACTIVE",
    "WIM_EXTERNAL_FILE_INFO_FLAG_SUSPENDED",
    "WIM_PROVIDER_HASH_SIZE",
    "WIN32_FILE_ATTRIBUTE_DATA",
    "WIN32_FIND_DATAA",
    "WIN32_FIND_DATAW",
    "WIN32_FIND_STREAM_DATA",
    "WIN32_STREAM_ID",
    "WINEFS_SETUSERKEY_SET_CAPABILITIES",
    "WIN_STREAM_ID",
    "WOF_FILE_COMPRESSION_INFO_V0",
    "WOF_FILE_COMPRESSION_INFO_V1",
    "WOF_PROVIDER_FILE",
    "WOF_PROVIDER_WIM",
    "WRITE_DAC",
    "WRITE_OWNER",
    "WofEnumEntries",
    "WofEnumEntryProc",
    "WofEnumFilesProc",
    "WofFileEnumFiles",
    "WofGetDriverVersion",
    "WofIsExternalFile",
    "WofSetFileDataLocation",
    "WofShouldCompressBinaries",
    "WofWimAddEntry",
    "WofWimEnumFiles",
    "WofWimRemoveEntry",
    "WofWimSuspendEntry",
    "WofWimUpdateEntry",
    "Wow64DisableWow64FsRedirection",
    "Wow64EnableWow64FsRedirection",
    "Wow64RevertWow64FsRedirection",
    "WriteEncryptedFileRaw",
    "WriteFile",
    "WriteFileEx",
    "WriteFileGather",
    "WriteLogRestartArea",
    "WriteTapemark",
    "_FT_TYPES_DEFINITION_",
]
