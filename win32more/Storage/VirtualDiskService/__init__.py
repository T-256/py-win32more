from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Storage.VirtualDiskService
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
VDS_NF_VOLUME_ARRIVE = 4
VDS_NF_VOLUME_DEPART = 5
VDS_NF_VOLUME_MODIFY = 6
VDS_NF_VOLUME_REBUILDING_PROGRESS = 7
VDS_NF_PARTITION_ARRIVE = 11
VDS_NF_PARTITION_DEPART = 12
VDS_NF_PARTITION_MODIFY = 13
VDS_NF_SUB_SYSTEM_ARRIVE = 101
VDS_NF_SUB_SYSTEM_DEPART = 102
VDS_NF_PORTAL_ARRIVE = 123
VDS_NF_PORTAL_DEPART = 124
VDS_NF_PORTAL_MODIFY = 125
VDS_NF_TARGET_ARRIVE = 126
VDS_NF_TARGET_DEPART = 127
VDS_NF_TARGET_MODIFY = 128
VDS_NF_PORTAL_GROUP_ARRIVE = 129
VDS_NF_PORTAL_GROUP_DEPART = 130
VDS_NF_PORTAL_GROUP_MODIFY = 131
VDS_NF_SUB_SYSTEM_MODIFY = 151
VDS_NF_DRIVE_LETTER_FREE = 201
VDS_NF_DRIVE_LETTER_ASSIGN = 202
VDS_NF_MOUNT_POINTS_CHANGE = 205
VDS_NF_FILE_SYSTEM_SHRINKING_PROGRESS = 206
VDS_NF_SERVICE_OUT_OF_SYNC = 301
GPT_PARTITION_NAME_LENGTH = 36
VDS_HINT_FASTCRASHRECOVERYREQUIRED = 1
VDS_HINT_MOSTLYREADS = 2
VDS_HINT_OPTIMIZEFORSEQUENTIALREADS = 4
VDS_HINT_OPTIMIZEFORSEQUENTIALWRITES = 8
VDS_HINT_READBACKVERIFYENABLED = 16
VDS_HINT_REMAPENABLED = 32
VDS_HINT_WRITETHROUGHCACHINGENABLED = 64
VDS_HINT_HARDWARECHECKSUMENABLED = 128
VDS_HINT_ISYANKABLE = 256
VDS_HINT_ALLOCATEHOTSPARE = 512
VDS_HINT_BUSTYPE = 1024
VDS_HINT_USEMIRROREDCACHE = 2048
VDS_HINT_READCACHINGENABLED = 4096
VDS_HINT_WRITECACHINGENABLED = 8192
VDS_HINT_MEDIASCANENABLED = 16384
VDS_HINT_CONSISTENCYCHECKENABLED = 32768
VDS_REBUILD_PRIORITY_MIN = 0
VDS_REBUILD_PRIORITY_MAX = 16
VDS_POOL_ATTRIB_RAIDTYPE = 1
VDS_POOL_ATTRIB_BUSTYPE = 2
VDS_POOL_ATTRIB_ALLOW_SPINDOWN = 4
VDS_POOL_ATTRIB_THIN_PROVISION = 8
VDS_POOL_ATTRIB_NO_SINGLE_POF = 16
VDS_POOL_ATTRIB_DATA_RDNCY_MAX = 32
VDS_POOL_ATTRIB_DATA_RDNCY_MIN = 64
VDS_POOL_ATTRIB_DATA_RDNCY_DEF = 128
VDS_POOL_ATTRIB_PKG_RDNCY_MAX = 256
VDS_POOL_ATTRIB_PKG_RDNCY_MIN = 512
VDS_POOL_ATTRIB_PKG_RDNCY_DEF = 1024
VDS_POOL_ATTRIB_STRIPE_SIZE = 2048
VDS_POOL_ATTRIB_STRIPE_SIZE_MAX = 4096
VDS_POOL_ATTRIB_STRIPE_SIZE_MIN = 8192
VDS_POOL_ATTRIB_STRIPE_SIZE_DEF = 16384
VDS_POOL_ATTRIB_NUM_CLMNS = 32768
VDS_POOL_ATTRIB_NUM_CLMNS_MAX = 65536
VDS_POOL_ATTRIB_NUM_CLMNS_MIN = 131072
VDS_POOL_ATTRIB_NUM_CLMNS_DEF = 262144
VDS_POOL_ATTRIB_DATA_AVL_HINT = 524288
VDS_POOL_ATTRIB_ACCS_RNDM_HINT = 1048576
VDS_POOL_ATTRIB_ACCS_DIR_HINT = 2097152
VDS_POOL_ATTRIB_ACCS_SIZE_HINT = 4194304
VDS_POOL_ATTRIB_ACCS_LTNCY_HINT = 8388608
VDS_POOL_ATTRIB_ACCS_BDW_WT_HINT = 16777216
VDS_POOL_ATTRIB_STOR_COST_HINT = 33554432
VDS_POOL_ATTRIB_STOR_EFFCY_HINT = 67108864
VDS_POOL_ATTRIB_CUSTOM_ATTRIB = 134217728
VDS_ATTACH_VIRTUAL_DISK_FLAG_USE_FILE_ACL = 1
def _define_CLSID_VdsLoader():
    return Guid('9c38ed61-d565-4728-ae-ee-c8-09-52-f0-ec-de')
def _define_CLSID_VdsService():
    return Guid('7d1933cb-86f6-4a98-86-28-01-be-94-c9-a5-75')
MAX_FS_NAME_SIZE = 8
MAX_FS_FORMAT_SUPPORT_NAME_SIZE = 32
MAX_FS_ALLOWED_CLUSTER_SIZES_SIZE = 32
VER_VDS_LUN_INFORMATION = 1
VDS_E_NOT_SUPPORTED = -2147212288
VDS_E_INITIALIZED_FAILED = -2147212287
VDS_E_INITIALIZE_NOT_CALLED = -2147212286
VDS_E_ALREADY_REGISTERED = -2147212285
VDS_E_ANOTHER_CALL_IN_PROGRESS = -2147212284
VDS_E_OBJECT_NOT_FOUND = -2147212283
VDS_E_INVALID_SPACE = -2147212282
VDS_E_PARTITION_LIMIT_REACHED = -2147212281
VDS_E_PARTITION_NOT_EMPTY = -2147212280
VDS_E_OPERATION_PENDING = -2147212279
VDS_E_OPERATION_DENIED = -2147212278
VDS_E_OBJECT_DELETED = -2147212277
VDS_E_CANCEL_TOO_LATE = -2147212276
VDS_E_OPERATION_CANCELED = -2147212275
VDS_E_CANNOT_EXTEND = -2147212274
VDS_E_NOT_ENOUGH_SPACE = -2147212273
VDS_E_NOT_ENOUGH_DRIVE = -2147212272
VDS_E_BAD_COOKIE = -2147212271
VDS_E_NO_MEDIA = -2147212270
VDS_E_DEVICE_IN_USE = -2147212269
VDS_E_DISK_NOT_EMPTY = -2147212268
VDS_E_INVALID_OPERATION = -2147212267
VDS_E_PATH_NOT_FOUND = -2147212266
VDS_E_DISK_NOT_INITIALIZED = -2147212265
VDS_E_NOT_AN_UNALLOCATED_DISK = -2147212264
VDS_E_UNRECOVERABLE_ERROR = -2147212263
VDS_S_DISK_PARTIALLY_CLEANED = 271386
VDS_E_DMADMIN_SERVICE_CONNECTION_FAILED = -2147212261
VDS_E_PROVIDER_INITIALIZATION_FAILED = -2147212260
VDS_E_OBJECT_EXISTS = -2147212259
VDS_E_NO_DISKS_FOUND = -2147212258
VDS_E_PROVIDER_CACHE_CORRUPT = -2147212257
VDS_E_DMADMIN_METHOD_CALL_FAILED = -2147212256
VDS_S_PROVIDER_ERROR_LOADING_CACHE = 271393
VDS_E_PROVIDER_VOL_DEVICE_NAME_NOT_FOUND = -2147212254
VDS_E_PROVIDER_VOL_OPEN = -2147212253
VDS_E_DMADMIN_CORRUPT_NOTIFICATION = -2147212252
VDS_E_INCOMPATIBLE_FILE_SYSTEM = -2147212251
VDS_E_INCOMPATIBLE_MEDIA = -2147212250
VDS_E_ACCESS_DENIED = -2147212249
VDS_E_MEDIA_WRITE_PROTECTED = -2147212248
VDS_E_BAD_LABEL = -2147212247
VDS_E_CANT_QUICK_FORMAT = -2147212246
VDS_E_IO_ERROR = -2147212245
VDS_E_VOLUME_TOO_SMALL = -2147212244
VDS_E_VOLUME_TOO_BIG = -2147212243
VDS_E_CLUSTER_SIZE_TOO_SMALL = -2147212242
VDS_E_CLUSTER_SIZE_TOO_BIG = -2147212241
VDS_E_CLUSTER_COUNT_BEYOND_32BITS = -2147212240
VDS_E_OBJECT_STATUS_FAILED = -2147212239
VDS_E_VOLUME_INCOMPLETE = -2147212238
VDS_E_EXTENT_SIZE_LESS_THAN_MIN = -2147212237
VDS_S_UPDATE_BOOTFILE_FAILED = 271412
VDS_S_BOOT_PARTITION_NUMBER_CHANGE = 271414
VDS_E_BOOT_PARTITION_NUMBER_CHANGE = -2147212234
VDS_E_NO_FREE_SPACE = -2147212233
VDS_E_ACTIVE_PARTITION = -2147212232
VDS_E_PARTITION_OF_UNKNOWN_TYPE = -2147212231
VDS_E_LEGACY_VOLUME_FORMAT = -2147212230
VDS_E_NON_CONTIGUOUS_DATA_PARTITIONS = -2147212229
VDS_E_MIGRATE_OPEN_VOLUME = -2147212228
VDS_E_VOLUME_NOT_ONLINE = -2147212227
VDS_E_VOLUME_NOT_HEALTHY = -2147212226
VDS_E_VOLUME_SPANS_DISKS = -2147212225
VDS_E_REQUIRES_CONTIGUOUS_DISK_SPACE = -2147212224
VDS_E_BAD_PROVIDER_DATA = -2147212223
VDS_E_PROVIDER_FAILURE = -2147212222
VDS_S_VOLUME_COMPRESS_FAILED = 271427
VDS_E_PACK_OFFLINE = -2147212220
VDS_E_VOLUME_NOT_A_MIRROR = -2147212219
VDS_E_NO_EXTENTS_FOR_VOLUME = -2147212218
VDS_E_DISK_NOT_LOADED_TO_CACHE = -2147212217
VDS_E_INTERNAL_ERROR = -2147212216
VDS_S_ACCESS_PATH_NOT_DELETED = 279108
VDS_E_PROVIDER_TYPE_NOT_SUPPORTED = -2147212214
VDS_E_DISK_NOT_ONLINE = -2147212213
VDS_E_DISK_IN_USE_BY_VOLUME = -2147212212
VDS_S_IN_PROGRESS = 271437
VDS_E_ASYNC_OBJECT_FAILURE = -2147212210
VDS_E_VOLUME_NOT_MOUNTED = -2147212209
VDS_E_PACK_NOT_FOUND = -2147212208
VDS_E_IMPORT_SET_INCOMPLETE = -2147212207
VDS_E_DISK_NOT_IMPORTED = -2147212206
VDS_E_OBJECT_OUT_OF_SYNC = -2147212205
VDS_E_MISSING_DISK = -2147212204
VDS_E_DISK_PNP_REG_CORRUPT = -2147212203
VDS_E_LBN_REMAP_ENABLED_FLAG = -2147212202
VDS_E_NO_DRIVELETTER_FLAG = -2147212201
VDS_E_REVERT_ON_CLOSE = -2147212200
VDS_E_REVERT_ON_CLOSE_SET = -2147212199
VDS_E_IA64_BOOT_MIRRORED_TO_MBR = -2147212198
VDS_S_IA64_BOOT_MIRRORED_TO_MBR = 271450
VDS_S_UNABLE_TO_GET_GPT_ATTRIBUTES = 271451
VDS_E_VOLUME_TEMPORARILY_DISMOUNTED = -2147212196
VDS_E_VOLUME_PERMANENTLY_DISMOUNTED = -2147212195
VDS_E_VOLUME_HAS_PATH = -2147212194
VDS_E_TIMEOUT = -2147212193
VDS_E_REPAIR_VOLUMESTATE = -2147212192
VDS_E_LDM_TIMEOUT = -2147212191
VDS_E_REVERT_ON_CLOSE_MISMATCH = -2147212190
VDS_E_RETRY = -2147212189
VDS_E_ONLINE_PACK_EXISTS = -2147212188
VDS_S_EXTEND_FILE_SYSTEM_FAILED = 271461
VDS_E_EXTEND_FILE_SYSTEM_FAILED = -2147212186
VDS_S_MBR_BOOT_MIRRORED_TO_GPT = 271463
VDS_E_MAX_USABLE_MBR = -2147212184
VDS_S_GPT_BOOT_MIRRORED_TO_MBR = -2147212183
VDS_E_NO_SOFTWARE_PROVIDERS_LOADED = -2147212032
VDS_E_DISK_NOT_MISSING = -2147212031
VDS_E_NO_VOLUME_LAYOUT = -2147212030
VDS_E_CORRUPT_VOLUME_INFO = -2147212029
VDS_E_INVALID_ENUMERATOR = -2147212028
VDS_E_DRIVER_INTERNAL_ERROR = -2147212027
VDS_E_VOLUME_INVALID_NAME = -2147212025
VDS_S_DISK_IS_MISSING = 271624
VDS_E_CORRUPT_PARTITION_INFO = -2147212023
VDS_S_NONCONFORMANT_PARTITION_INFO = 271626
VDS_E_CORRUPT_EXTENT_INFO = -2147212021
VDS_E_DUP_EMPTY_PACK_GUID = -2147212020
VDS_E_DRIVER_NO_PACK_NAME = -2147212019
VDS_S_SYSTEM_PARTITION = 271630
VDS_E_BAD_PNP_MESSAGE = -2147212017
VDS_E_NO_PNP_DISK_ARRIVE = -2147212016
VDS_E_NO_PNP_VOLUME_ARRIVE = -2147212015
VDS_E_NO_PNP_DISK_REMOVE = -2147212014
VDS_E_NO_PNP_VOLUME_REMOVE = -2147212013
VDS_E_PROVIDER_EXITING = -2147212012
VDS_E_EXTENT_EXCEEDS_DISK_FREE_SPACE = -2147212011
VDS_E_MEMBER_SIZE_INVALID = -2147212010
VDS_S_NO_NOTIFICATION = 271639
VDS_S_DEFAULT_PLEX_MEMBER_IDS = 271640
VDS_E_INVALID_DISK = -2147212007
VDS_E_INVALID_PACK = -2147212006
VDS_E_VOLUME_ON_DISK = -2147212005
VDS_E_DRIVER_INVALID_PARAM = -2147212004
VDS_E_TARGET_PACK_NOT_EMPTY = -2147212003
VDS_E_CANNOT_SHRINK = -2147212002
VDS_E_MULTIPLE_PACKS = -2147212001
VDS_E_PACK_ONLINE = -2147212000
VDS_E_INVALID_PLEX_COUNT = -2147211999
VDS_E_INVALID_MEMBER_COUNT = -2147211998
VDS_E_INVALID_PLEX_ORDER = -2147211997
VDS_E_INVALID_MEMBER_ORDER = -2147211996
VDS_E_INVALID_STRIPE_SIZE = -2147211995
VDS_E_INVALID_DISK_COUNT = -2147211994
VDS_E_INVALID_EXTENT_COUNT = -2147211993
VDS_E_SOURCE_IS_TARGET_PACK = -2147211992
VDS_E_VOLUME_DISK_COUNT_MAX_EXCEEDED = -2147211991
VDS_E_CORRUPT_NOTIFICATION_INFO = -2147211990
VDS_E_INVALID_PLEX_GUID = -2147211988
VDS_E_DISK_NOT_FOUND_IN_PACK = -2147211987
VDS_E_DUPLICATE_DISK = -2147211986
VDS_E_LAST_VALID_DISK = -2147211985
VDS_E_INVALID_SECTOR_SIZE = -2147211984
VDS_E_ONE_EXTENT_PER_DISK = -2147211983
VDS_E_INVALID_BLOCK_SIZE = -2147211982
VDS_E_PLEX_SIZE_INVALID = -2147211981
VDS_E_NO_EXTENTS_FOR_PLEX = -2147211980
VDS_E_INVALID_PLEX_TYPE = -2147211979
VDS_E_INVALID_PLEX_BLOCK_SIZE = -2147211978
VDS_E_NO_HEALTHY_DISKS = -2147211977
VDS_E_CONFIG_LIMIT = -2147211976
VDS_E_DISK_CONFIGURATION_CORRUPTED = -2147211975
VDS_E_DISK_CONFIGURATION_NOT_IN_SYNC = -2147211974
VDS_E_DISK_CONFIGURATION_UPDATE_FAILED = -2147211973
VDS_E_DISK_DYNAMIC = -2147211972
VDS_E_DRIVER_OBJECT_NOT_FOUND = -2147211971
VDS_E_PARTITION_NOT_CYLINDER_ALIGNED = -2147211970
VDS_E_DISK_LAYOUT_PARTITIONS_TOO_SMALL = -2147211969
VDS_E_DISK_IO_FAILING = -2147211968
VDS_E_DYNAMIC_DISKS_NOT_SUPPORTED = -2147211967
VDS_E_FAULT_TOLERANT_DISKS_NOT_SUPPORTED = -2147211966
VDS_E_GPT_ATTRIBUTES_INVALID = -2147211965
VDS_E_MEMBER_IS_HEALTHY = -2147211964
VDS_E_MEMBER_REGENERATING = -2147211963
VDS_E_PACK_NAME_INVALID = -2147211962
VDS_E_PLEX_IS_HEALTHY = -2147211961
VDS_E_PLEX_LAST_ACTIVE = -2147211960
VDS_E_PLEX_MISSING = -2147211959
VDS_E_MEMBER_MISSING = -2147211958
VDS_E_PLEX_REGENERATING = -2147211957
VDS_E_UNEXPECTED_DISK_LAYOUT_CHANGE = -2147211955
VDS_E_INVALID_VOLUME_LENGTH = -2147211954
VDS_E_VOLUME_LENGTH_NOT_SECTOR_SIZE_MULTIPLE = -2147211953
VDS_E_VOLUME_NOT_RETAINED = -2147211952
VDS_E_VOLUME_RETAINED = -2147211951
VDS_E_ALIGN_BEYOND_FIRST_CYLINDER = -2147211949
VDS_E_ALIGN_NOT_SECTOR_SIZE_MULTIPLE = -2147211948
VDS_E_ALIGN_NOT_ZERO = -2147211947
VDS_E_CACHE_CORRUPT = -2147211946
VDS_E_CANNOT_CLEAR_VOLUME_FLAG = -2147211945
VDS_E_DISK_BEING_CLEANED = -2147211944
VDS_E_DISK_NOT_CONVERTIBLE = -2147211943
VDS_E_DISK_REMOVEABLE = -2147211942
VDS_E_DISK_REMOVEABLE_NOT_EMPTY = -2147211941
VDS_E_DRIVE_LETTER_NOT_FREE = -2147211940
VDS_E_EXTEND_MULTIPLE_DISKS_NOT_SUPPORTED = -2147211939
VDS_E_INVALID_DRIVE_LETTER = -2147211938
VDS_E_INVALID_DRIVE_LETTER_COUNT = -2147211937
VDS_E_INVALID_FS_FLAG = -2147211936
VDS_E_INVALID_FS_TYPE = -2147211935
VDS_E_INVALID_OBJECT_TYPE = -2147211934
VDS_E_INVALID_PARTITION_LAYOUT = -2147211933
VDS_E_INVALID_PARTITION_STYLE = -2147211932
VDS_E_INVALID_PARTITION_TYPE = -2147211931
VDS_E_INVALID_PROVIDER_CLSID = -2147211930
VDS_E_INVALID_PROVIDER_ID = -2147211929
VDS_E_INVALID_PROVIDER_NAME = -2147211928
VDS_E_INVALID_PROVIDER_TYPE = -2147211927
VDS_E_INVALID_PROVIDER_VERSION_GUID = -2147211926
VDS_E_INVALID_PROVIDER_VERSION_STRING = -2147211925
VDS_E_INVALID_QUERY_PROVIDER_FLAG = -2147211924
VDS_E_INVALID_SERVICE_FLAG = -2147211923
VDS_E_INVALID_VOLUME_FLAG = -2147211922
VDS_E_PARTITION_NOT_OEM = -2147211921
VDS_E_PARTITION_PROTECTED = -2147211920
VDS_E_PARTITION_STYLE_MISMATCH = -2147211919
VDS_E_PROVIDER_INTERNAL_ERROR = -2147211918
VDS_E_SHRINK_SIZE_LESS_THAN_MIN = -2147211917
VDS_E_SHRINK_SIZE_TOO_BIG = -2147211916
VDS_E_UNRECOVERABLE_PROVIDER_ERROR = -2147211915
VDS_E_VOLUME_HIDDEN = -2147211914
VDS_S_DISMOUNT_FAILED = 271735
VDS_S_REMOUNT_FAILED = 271736
VDS_E_FLAG_ALREADY_SET = -2147211911
VDS_S_RESYNC_NOTIFICATION_TASK_FAILED = 271738
VDS_E_DISTINCT_VOLUME = -2147211909
VDS_E_VOLUME_NOT_FOUND_IN_PACK = -2147211908
VDS_E_PARTITION_NON_DATA = -2147211907
VDS_E_CRITICAL_PLEX = -2147211906
VDS_E_VOLUME_SYNCHRONIZING = -2147211905
VDS_E_VOLUME_REGENERATING = -2147211904
VDS_S_VSS_FLUSH_AND_HOLD_WRITES = 271745
VDS_S_VSS_RELEASE_WRITES = 271746
VDS_S_FS_LOCK = 271747
VDS_E_READONLY = -2147211900
VDS_E_INVALID_VOLUME_TYPE = -2147211899
VDS_E_BAD_BOOT_DISK = -2147211898
VDS_E_LOG_UPDATE = -2147211897
VDS_E_VOLUME_MIRRORED = -2147211896
VDS_E_VOLUME_SIMPLE_SPANNED = -2147211895
VDS_E_NO_VALID_LOG_COPIES = -2147211894
VDS_S_PLEX_NOT_LOADED_TO_CACHE = 271755
VDS_E_PLEX_NOT_LOADED_TO_CACHE = -2147211893
VDS_E_PARTITION_MSR = -2147211892
VDS_E_PARTITION_LDM = -2147211891
VDS_S_WINPE_BOOTENTRY = 271758
VDS_E_ALIGN_NOT_A_POWER_OF_TWO = -2147211889
VDS_E_ALIGN_IS_ZERO = -2147211888
VDS_E_SHRINK_IN_PROGRESS = -2147211887
VDS_E_CANT_INVALIDATE_FVE = -2147211886
VDS_E_FS_NOT_DETERMINED = -2147211885
VDS_E_DISK_NOT_OFFLINE = -2147211883
VDS_E_FAILED_TO_ONLINE_DISK = -2147211882
VDS_E_FAILED_TO_OFFLINE_DISK = -2147211881
VDS_E_BAD_REVISION_NUMBER = -2147211880
VDS_E_SHRINK_USER_CANCELLED = -2147211879
VDS_E_SHRINK_DIRTY_VOLUME = -2147211878
VDS_S_NAME_TRUNCATED = 272128
VDS_E_NAME_NOT_UNIQUE = -2147211519
VDS_S_STATUSES_INCOMPLETELY_SET = 272130
VDS_E_ADDRESSES_INCOMPLETELY_SET = -2147211517
VDS_E_SECURITY_INCOMPLETELY_SET = -2147211515
VDS_E_TARGET_SPECIFIC_NOT_SUPPORTED = -2147211514
VDS_E_INITIATOR_SPECIFIC_NOT_SUPPORTED = -2147211513
VDS_E_ISCSI_LOGIN_FAILED = -2147211512
VDS_E_ISCSI_LOGOUT_FAILED = -2147211511
VDS_E_ISCSI_SESSION_NOT_FOUND = -2147211510
VDS_E_ASSOCIATED_LUNS_EXIST = -2147211509
VDS_E_ASSOCIATED_PORTALS_EXIST = -2147211508
VDS_E_NO_DISCOVERY_DOMAIN = -2147211507
VDS_E_MULTIPLE_DISCOVERY_DOMAINS = -2147211506
VDS_E_NO_DISK_PATHNAME = -2147211505
VDS_E_ISCSI_LOGOUT_INCOMPLETE = -2147211504
VDS_E_NO_VOLUME_PATHNAME = -2147211503
VDS_E_PROVIDER_CACHE_OUTOFSYNC = -2147211502
VDS_E_NO_IMPORT_TARGET = -2147211501
VDS_S_ALREADY_EXISTS = 272148
VDS_S_PROPERTIES_INCOMPLETE = 272149
VDS_S_ISCSI_SESSION_NOT_FOUND_PERSISTENT_LOGIN_REMOVED = 272384
VDS_S_ISCSI_PERSISTENT_LOGIN_MAY_NOT_BE_REMOVED = 272385
VDS_S_ISCSI_LOGIN_ALREAD_EXISTS = 272386
VDS_E_UNABLE_TO_FIND_BOOT_DISK = -2147211261
VDS_E_INCORRECT_BOOT_VOLUME_EXTENT_INFO = -2147211260
VDS_E_GET_SAN_POLICY = -2147211259
VDS_E_SET_SAN_POLICY = -2147211258
VDS_E_BOOT_DISK = -2147211257
VDS_S_DISK_MOUNT_FAILED = 272392
VDS_S_DISK_DISMOUNT_FAILED = 272393
VDS_E_DISK_IS_OFFLINE = -2147211254
VDS_E_DISK_IS_READ_ONLY = -2147211253
VDS_E_PAGEFILE_DISK = -2147211252
VDS_E_HIBERNATION_FILE_DISK = -2147211251
VDS_E_CRASHDUMP_DISK = -2147211250
VDS_E_UNABLE_TO_FIND_SYSTEM_DISK = -2147211249
VDS_E_INCORRECT_SYSTEM_VOLUME_EXTENT_INFO = -2147211248
VDS_E_SYSTEM_DISK = -2147211247
VDS_E_VOLUME_SHRINK_FVE_LOCKED = -2147211246
VDS_E_VOLUME_SHRINK_FVE_CORRUPT = -2147211245
VDS_E_VOLUME_SHRINK_FVE_RECOVERY = -2147211244
VDS_E_VOLUME_SHRINK_FVE = -2147211243
VDS_E_SHRINK_OVER_DATA = -2147211242
VDS_E_INVALID_SHRINK_SIZE = -2147211241
VDS_E_LUN_DISK_MISSING = -2147211240
VDS_E_LUN_DISK_FAILED = -2147211239
VDS_E_LUN_DISK_NOT_READY = -2147211238
VDS_E_LUN_DISK_NO_MEDIA = -2147211237
VDS_E_LUN_NOT_READY = -2147211236
VDS_E_LUN_OFFLINE = -2147211235
VDS_E_LUN_FAILED = -2147211234
VDS_E_VOLUME_EXTEND_FVE_LOCKED = -2147211233
VDS_E_VOLUME_EXTEND_FVE_CORRUPT = -2147211232
VDS_E_VOLUME_EXTEND_FVE_RECOVERY = -2147211231
VDS_E_VOLUME_EXTEND_FVE = -2147211230
VDS_E_SECTOR_SIZE_ERROR = -2147211229
VDS_E_INITIATOR_ADAPTER_NOT_FOUND = -2147211008
VDS_E_TARGET_PORTAL_NOT_FOUND = -2147211007
VDS_E_INVALID_PORT_PATH = -2147211006
VDS_E_INVALID_ISCSI_TARGET_NAME = -2147211005
VDS_E_SET_TUNNEL_MODE_OUTER_ADDRESS = -2147211004
VDS_E_ISCSI_GET_IKE_INFO = -2147211003
VDS_E_ISCSI_SET_IKE_INFO = -2147211002
VDS_E_SUBSYSTEM_ID_IS_NULL = -2147211001
VDS_E_ISCSI_INITIATOR_NODE_NAME = -2147211000
VDS_E_ISCSI_GROUP_PRESHARE_KEY = -2147210999
VDS_E_ISCSI_CHAP_SECRET = -2147210998
VDS_E_INVALID_IP_ADDRESS = -2147210997
VDS_E_REBOOT_REQUIRED = -2147210996
VDS_E_VOLUME_GUID_PATHNAME_NOT_ALLOWED = -2147210995
VDS_E_BOOT_PAGEFILE_DRIVE_LETTER = -2147210994
VDS_E_DELETE_WITH_CRITICAL = -2147210993
VDS_E_CLEAN_WITH_DATA = -2147210992
VDS_E_CLEAN_WITH_OEM = -2147210991
VDS_E_CLEAN_WITH_CRITICAL = -2147210990
VDS_E_FORMAT_CRITICAL = -2147210989
VDS_E_NTFS_FORMAT_NOT_SUPPORTED = -2147210988
VDS_E_FAT32_FORMAT_NOT_SUPPORTED = -2147210987
VDS_E_FAT_FORMAT_NOT_SUPPORTED = -2147210986
VDS_E_FORMAT_NOT_SUPPORTED = -2147210985
VDS_E_COMPRESSION_NOT_SUPPORTED = -2147210984
VDS_E_VDISK_NOT_OPEN = -2147210983
VDS_E_VDISK_INVALID_OP_STATE = -2147210982
VDS_E_INVALID_PATH = -2147210981
VDS_E_INVALID_ISCSI_PATH = -2147210980
VDS_E_SHRINK_LUN_NOT_UNMASKED = -2147210979
VDS_E_LUN_DISK_READ_ONLY = -2147210978
VDS_E_LUN_UPDATE_DISK = -2147210977
VDS_E_LUN_DYNAMIC = -2147210976
VDS_E_LUN_DYNAMIC_OFFLINE = -2147210975
VDS_E_LUN_SHRINK_GPT_HEADER = -2147210974
VDS_E_MIRROR_NOT_SUPPORTED = -2147210973
VDS_E_RAID5_NOT_SUPPORTED = -2147210972
VDS_E_DISK_NOT_CONVERTIBLE_SIZE = -2147210971
VDS_E_OFFLINE_NOT_SUPPORTED = -2147210970
VDS_E_VDISK_PATHNAME_INVALID = -2147210969
VDS_E_EXTEND_TOO_MANY_CLUSTERS = -2147210968
VDS_E_EXTEND_UNKNOWN_FILESYSTEM = -2147210967
VDS_E_SHRINK_UNKNOWN_FILESYSTEM = -2147210966
VDS_E_VD_DISK_NOT_OPEN = -2147210965
VDS_E_VD_DISK_IS_EXPANDING = -2147210964
VDS_E_VD_DISK_IS_COMPACTING = -2147210963
VDS_E_VD_DISK_IS_MERGING = -2147210962
VDS_E_VD_IS_ATTACHED = -2147210961
VDS_E_VD_DISK_ALREADY_OPEN = -2147210960
VDS_E_VD_DISK_ALREADY_EXPANDING = -2147210959
VDS_E_VD_ALREADY_COMPACTING = -2147210958
VDS_E_VD_ALREADY_MERGING = -2147210957
VDS_E_VD_ALREADY_ATTACHED = -2147210956
VDS_E_VD_ALREADY_DETACHED = -2147210955
VDS_E_VD_NOT_ATTACHED_READONLY = -2147210954
VDS_E_VD_IS_BEING_ATTACHED = -2147210953
VDS_E_VD_IS_BEING_DETACHED = -2147210952
VDS_E_NO_POOL = -2147210752
VDS_E_NO_POOL_CREATED = -2147210751
VDS_E_NO_MAINTENANCE_MODE = -2147210750
VDS_E_BLOCK_CLUSTERED = -2147210749
VDS_E_DISK_HAS_BANDS = -2147210748
VDS_E_INVALID_STATE = -2147210747
VDS_E_REFS_FORMAT_NOT_SUPPORTED = -2147210746
VDS_E_DELETE_WITH_BOOTBACKING = -2147210745
VDS_E_FORMAT_WITH_BOOTBACKING = -2147210744
VDS_E_CLEAN_WITH_BOOTBACKING = -2147210743
VDS_E_SHRINK_EXTEND_UNALIGNED = -2147210496
def _define_IEnumVdsObject_head():
    class IEnumVdsObject(win32more.System.Com.IUnknown_head):
        Guid = Guid('118610b7-8d94-4030-b5-b8-50-08-89-78-8e-4e')
    return IEnumVdsObject
def _define_IEnumVdsObject():
    IEnumVdsObject = win32more.Storage.VirtualDiskService.IEnumVdsObject_head
    IEnumVdsObject.Next = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.System.Com.IUnknown_head),POINTER(UInt32))(3, 'Next', ((1, 'celt'),(1, 'ppObjectArray'),(1, 'pcFetched'),)))
    IEnumVdsObject.Skip = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(4, 'Skip', ((1, 'celt'),)))
    IEnumVdsObject.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Reset', ()))
    IEnumVdsObject.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(6, 'Clone', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IEnumVdsObject
def _define_IVdsAdmin_head():
    class IVdsAdmin(win32more.System.Com.IUnknown_head):
        Guid = Guid('d188e97d-85aa-4d33-ab-c6-26-29-9a-10-ff-c1')
    return IVdsAdmin
def _define_IVdsAdmin():
    IVdsAdmin = win32more.Storage.VirtualDiskService.IVdsAdmin_head
    IVdsAdmin.RegisterProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid,win32more.Foundation.PWSTR,win32more.Storage.VirtualDiskService.VDS_PROVIDER_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,Guid)(3, 'RegisterProvider', ((1, 'providerId'),(1, 'providerClsid'),(1, 'pwszName'),(1, 'type'),(1, 'pwszMachineName'),(1, 'pwszVersion'),(1, 'guidVersionId'),)))
    IVdsAdmin.UnregisterProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid)(4, 'UnregisterProvider', ((1, 'providerId'),)))
    win32more.System.Com.IUnknown
    return IVdsAdmin
def _define_IVdsAdviseSink_head():
    class IVdsAdviseSink(win32more.System.Com.IUnknown_head):
        Guid = Guid('8326cd1d-cf59-4936-b7-86-5e-fc-08-79-8e-25')
    return IVdsAdviseSink
def _define_IVdsAdviseSink():
    IVdsAdviseSink = win32more.Storage.VirtualDiskService.IVdsAdviseSink_head
    IVdsAdviseSink.OnNotify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,POINTER(win32more.Storage.VirtualDiskService.VDS_NOTIFICATION_head))(3, 'OnNotify', ((1, 'lNumberOfNotifications'),(1, 'pNotificationArray'),)))
    win32more.System.Com.IUnknown
    return IVdsAdviseSink
def _define_IVdsAsync_head():
    class IVdsAsync(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5d23b6d-5a55-4492-98-89-39-7a-3c-2d-2d-bc')
    return IVdsAsync
def _define_IVdsAsync():
    IVdsAsync = win32more.Storage.VirtualDiskService.IVdsAsync_head
    IVdsAsync.Cancel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'Cancel', ()))
    IVdsAsync.Wait = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),POINTER(win32more.Storage.VirtualDiskService.VDS_ASYNC_OUTPUT_head))(4, 'Wait', ((1, 'pHrResult'),(1, 'pAsyncOut'),)))
    IVdsAsync.QueryStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.HRESULT),POINTER(UInt32))(5, 'QueryStatus', ((1, 'pHrResult'),(1, 'pulPercentCompleted'),)))
    win32more.System.Com.IUnknown
    return IVdsAsync
def _define_IVdsController_head():
    class IVdsController(win32more.System.Com.IUnknown_head):
        Guid = Guid('cb53d96e-dffb-474a-a0-78-79-0d-1e-2b-c0-82')
    return IVdsController
def _define_IVdsController():
    IVdsController = win32more.Storage.VirtualDiskService.IVdsController_head
    IVdsController.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_CONTROLLER_PROP_head))(3, 'GetProperties', ((1, 'pControllerProp'),)))
    IVdsController.GetSubSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsSubSystem_head))(4, 'GetSubSystem', ((1, 'ppSubSystem'),)))
    IVdsController.GetPortProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,POINTER(win32more.Storage.VirtualDiskService.VDS_PORT_PROP_head))(5, 'GetPortProperties', ((1, 'sPortNumber'),(1, 'pPortProp'),)))
    IVdsController.FlushCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'FlushCache', ()))
    IVdsController.InvalidateCache = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(7, 'InvalidateCache', ()))
    IVdsController.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(8, 'Reset', ()))
    IVdsController.QueryAssociatedLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(9, 'QueryAssociatedLuns', ((1, 'ppEnum'),)))
    IVdsController.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_CONTROLLER_STATUS)(10, 'SetStatus', ((1, 'status'),)))
    win32more.System.Com.IUnknown
    return IVdsController
def _define_IVdsControllerControllerPort_head():
    class IVdsControllerControllerPort(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca5d735f-6bae-42c0-b3-0e-f2-66-60-45-ce-71')
    return IVdsControllerControllerPort
def _define_IVdsControllerControllerPort():
    IVdsControllerControllerPort = win32more.Storage.VirtualDiskService.IVdsControllerControllerPort_head
    IVdsControllerControllerPort.QueryControllerPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(3, 'QueryControllerPorts', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVdsControllerControllerPort
def _define_IVdsControllerPort_head():
    class IVdsControllerPort(win32more.System.Com.IUnknown_head):
        Guid = Guid('18691d0d-4e7f-43e8-92-e4-cf-44-be-ee-d1-1c')
    return IVdsControllerPort
def _define_IVdsControllerPort():
    IVdsControllerPort = win32more.Storage.VirtualDiskService.IVdsControllerPort_head
    IVdsControllerPort.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_PORT_PROP_head))(3, 'GetProperties', ((1, 'pPortProp'),)))
    IVdsControllerPort.GetController = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsController_head))(4, 'GetController', ((1, 'ppController'),)))
    IVdsControllerPort.QueryAssociatedLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(5, 'QueryAssociatedLuns', ((1, 'ppEnum'),)))
    IVdsControllerPort.Reset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Reset', ()))
    IVdsControllerPort.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_PORT_STATUS)(7, 'SetStatus', ((1, 'status'),)))
    win32more.System.Com.IUnknown
    return IVdsControllerPort
def _define_IVdsDrive_head():
    class IVdsDrive(win32more.System.Com.IUnknown_head):
        Guid = Guid('ff24efa4-aade-4b6b-89-8b-ea-a6-a2-08-87-c7')
    return IVdsDrive
def _define_IVdsDrive():
    IVdsDrive = win32more.Storage.VirtualDiskService.IVdsDrive_head
    IVdsDrive.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_DRIVE_PROP_head))(3, 'GetProperties', ((1, 'pDriveProp'),)))
    IVdsDrive.GetSubSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsSubSystem_head))(4, 'GetSubSystem', ((1, 'ppSubSystem'),)))
    IVdsDrive.QueryExtents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.VirtualDiskService.VDS_DRIVE_EXTENT_head)),POINTER(Int32))(5, 'QueryExtents', ((1, 'ppExtentArray'),(1, 'plNumberOfExtents'),)))
    IVdsDrive.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'SetFlags', ((1, 'ulFlags'),)))
    IVdsDrive.ClearFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(7, 'ClearFlags', ((1, 'ulFlags'),)))
    IVdsDrive.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_DRIVE_STATUS)(8, 'SetStatus', ((1, 'status'),)))
    win32more.System.Com.IUnknown
    return IVdsDrive
def _define_IVdsDrive2_head():
    class IVdsDrive2(win32more.System.Com.IUnknown_head):
        Guid = Guid('60b5a730-addf-4436-8c-a7-57-69-e2-d1-ff-a4')
    return IVdsDrive2
def _define_IVdsDrive2():
    IVdsDrive2 = win32more.Storage.VirtualDiskService.IVdsDrive2_head
    IVdsDrive2.GetProperties2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_DRIVE_PROP2_head))(3, 'GetProperties2', ((1, 'pDriveProp2'),)))
    win32more.System.Com.IUnknown
    return IVdsDrive2
def _define_IVdsHwProvider_head():
    class IVdsHwProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('d99bdaae-b13a-4178-9f-db-e2-7f-16-b4-60-3e')
    return IVdsHwProvider
def _define_IVdsHwProvider():
    IVdsHwProvider = win32more.Storage.VirtualDiskService.IVdsHwProvider_head
    IVdsHwProvider.QuerySubSystems = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(3, 'QuerySubSystems', ((1, 'ppEnum'),)))
    IVdsHwProvider.Reenumerate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(4, 'Reenumerate', ()))
    IVdsHwProvider.Refresh = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(5, 'Refresh', ()))
    win32more.System.Com.IUnknown
    return IVdsHwProvider
def _define_IVdsHwProviderPrivate_head():
    class IVdsHwProviderPrivate(win32more.System.Com.IUnknown_head):
        Guid = Guid('98f17bf3-9f33-4f12-87-14-8b-40-75-09-2c-2e')
    return IVdsHwProviderPrivate
def _define_IVdsHwProviderPrivate():
    IVdsHwProviderPrivate = win32more.Storage.VirtualDiskService.IVdsHwProviderPrivate_head
    IVdsHwProviderPrivate.QueryIfCreatedLun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head),POINTER(Guid))(3, 'QueryIfCreatedLun', ((1, 'pwszDevicePath'),(1, 'pVdsLunInformation'),(1, 'pLunId'),)))
    win32more.System.Com.IUnknown
    return IVdsHwProviderPrivate
def _define_IVdsHwProviderPrivateMpio_head():
    class IVdsHwProviderPrivateMpio(win32more.System.Com.IUnknown_head):
        Guid = Guid('310a7715-ac2b-4c6f-98-27-3d-74-2f-35-16-76')
    return IVdsHwProviderPrivateMpio
def _define_IVdsHwProviderPrivateMpio():
    IVdsHwProviderPrivateMpio = win32more.Storage.VirtualDiskService.IVdsHwProviderPrivateMpio_head
    IVdsHwProviderPrivateMpio.SetAllPathStatusesFromHbaPort = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_HBAPORT_PROP,win32more.Storage.VirtualDiskService.VDS_PATH_STATUS)(3, 'SetAllPathStatusesFromHbaPort', ((1, 'hbaPortProp'),(1, 'status'),)))
    win32more.System.Com.IUnknown
    return IVdsHwProviderPrivateMpio
def _define_IVdsHwProviderStoragePools_head():
    class IVdsHwProviderStoragePools(win32more.System.Com.IUnknown_head):
        Guid = Guid('d5b5937a-f188-4c79-b8-6c-11-c9-20-ad-11-b8')
    return IVdsHwProviderStoragePools
def _define_IVdsHwProviderStoragePools():
    IVdsHwProviderStoragePools = win32more.Storage.VirtualDiskService.IVdsHwProviderStoragePools_head
    IVdsHwProviderStoragePools.QueryStoragePools = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt64,POINTER(win32more.Storage.VirtualDiskService.VDS_POOL_ATTRIBUTES_head),POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(3, 'QueryStoragePools', ((1, 'ulFlags'),(1, 'ullRemainingFreeSpace'),(1, 'pPoolAttributes'),(1, 'ppEnum'),)))
    IVdsHwProviderStoragePools.CreateLunInStoragePool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,UInt64,Guid,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head),POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(4, 'CreateLunInStoragePool', ((1, 'type'),(1, 'ullSizeInBytes'),(1, 'StoragePoolId'),(1, 'pwszUnmaskingList'),(1, 'pHints2'),(1, 'ppAsync'),)))
    IVdsHwProviderStoragePools.QueryMaxLunCreateSizeInStoragePool = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,Guid,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head),POINTER(UInt64))(5, 'QueryMaxLunCreateSizeInStoragePool', ((1, 'type'),(1, 'StoragePoolId'),(1, 'pHints2'),(1, 'pullMaxLunSize'),)))
    win32more.System.Com.IUnknown
    return IVdsHwProviderStoragePools
def _define_IVdsHwProviderType_head():
    class IVdsHwProviderType(win32more.System.Com.IUnknown_head):
        Guid = Guid('3e0f5166-542d-4fc6-94-7a-01-21-74-24-0b-7e')
    return IVdsHwProviderType
def _define_IVdsHwProviderType():
    IVdsHwProviderType = win32more.Storage.VirtualDiskService.IVdsHwProviderType_head
    IVdsHwProviderType.GetProviderType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HWPROVIDER_TYPE))(3, 'GetProviderType', ((1, 'pType'),)))
    win32more.System.Com.IUnknown
    return IVdsHwProviderType
def _define_IVdsHwProviderType2_head():
    class IVdsHwProviderType2(win32more.System.Com.IUnknown_head):
        Guid = Guid('8190236f-c4d0-4e81-80-11-d6-95-12-fc-c9-84')
    return IVdsHwProviderType2
def _define_IVdsHwProviderType2():
    IVdsHwProviderType2 = win32more.Storage.VirtualDiskService.IVdsHwProviderType2_head
    IVdsHwProviderType2.GetProviderType2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HWPROVIDER_TYPE))(3, 'GetProviderType2', ((1, 'pType'),)))
    win32more.System.Com.IUnknown
    return IVdsHwProviderType2
def _define_IVdsIscsiPortal_head():
    class IVdsIscsiPortal(win32more.System.Com.IUnknown_head):
        Guid = Guid('7fa1499d-ec85-4a8a-a4-7b-ff-69-20-1f-cd-34')
    return IVdsIscsiPortal
def _define_IVdsIscsiPortal():
    IVdsIscsiPortal = win32more.Storage.VirtualDiskService.IVdsIscsiPortal_head
    IVdsIscsiPortal.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTAL_PROP_head))(3, 'GetProperties', ((1, 'pPortalProp'),)))
    IVdsIscsiPortal.GetSubSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsSubSystem_head))(4, 'GetSubSystem', ((1, 'ppSubSystem'),)))
    IVdsIscsiPortal.QueryAssociatedPortalGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(5, 'QueryAssociatedPortalGroups', ((1, 'ppEnum'),)))
    IVdsIscsiPortal.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTAL_STATUS)(6, 'SetStatus', ((1, 'status'),)))
    IVdsIscsiPortal.SetIpsecTunnelAddress = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head),POINTER(win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head))(7, 'SetIpsecTunnelAddress', ((1, 'pTunnelAddress'),(1, 'pDestinationAddress'),)))
    IVdsIscsiPortal.GetIpsecSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head),POINTER(UInt64))(8, 'GetIpsecSecurity', ((1, 'pInitiatorPortalAddress'),(1, 'pullSecurityFlags'),)))
    IVdsIscsiPortal.SetIpsecSecurity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head),UInt64,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_IPSEC_KEY_head))(9, 'SetIpsecSecurity', ((1, 'pInitiatorPortalAddress'),(1, 'ullSecurityFlags'),(1, 'pIpsecKey'),)))
    win32more.System.Com.IUnknown
    return IVdsIscsiPortal
def _define_IVdsIscsiPortalGroup_head():
    class IVdsIscsiPortalGroup(win32more.System.Com.IUnknown_head):
        Guid = Guid('fef5f89d-a3dd-4b36-bf-28-e7-dd-e0-45-c5-93')
    return IVdsIscsiPortalGroup
def _define_IVdsIscsiPortalGroup():
    IVdsIscsiPortalGroup = win32more.Storage.VirtualDiskService.IVdsIscsiPortalGroup_head
    IVdsIscsiPortalGroup.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTALGROUP_PROP_head))(3, 'GetProperties', ((1, 'pPortalGroupProp'),)))
    IVdsIscsiPortalGroup.GetTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsIscsiTarget_head))(4, 'GetTarget', ((1, 'ppTarget'),)))
    IVdsIscsiPortalGroup.QueryAssociatedPortals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(5, 'QueryAssociatedPortals', ((1, 'ppEnum'),)))
    IVdsIscsiPortalGroup.AddPortal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(6, 'AddPortal', ((1, 'portalId'),(1, 'ppAsync'),)))
    IVdsIscsiPortalGroup.RemovePortal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(7, 'RemovePortal', ((1, 'portalId'),(1, 'ppAsync'),)))
    IVdsIscsiPortalGroup.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(8, 'Delete', ((1, 'ppAsync'),)))
    win32more.System.Com.IUnknown
    return IVdsIscsiPortalGroup
def _define_IVdsIscsiTarget_head():
    class IVdsIscsiTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('aa8f5055-83e5-4bcc-aa-73-19-85-1a-36-a8-49')
    return IVdsIscsiTarget
def _define_IVdsIscsiTarget():
    IVdsIscsiTarget = win32more.Storage.VirtualDiskService.IVdsIscsiTarget_head
    IVdsIscsiTarget.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_TARGET_PROP_head))(3, 'GetProperties', ((1, 'pTargetProp'),)))
    IVdsIscsiTarget.GetSubSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsSubSystem_head))(4, 'GetSubSystem', ((1, 'ppSubSystem'),)))
    IVdsIscsiTarget.QueryPortalGroups = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(5, 'QueryPortalGroups', ((1, 'ppEnum'),)))
    IVdsIscsiTarget.QueryAssociatedLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(6, 'QueryAssociatedLuns', ((1, 'ppEnum'),)))
    IVdsIscsiTarget.CreatePortalGroup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(7, 'CreatePortalGroup', ((1, 'ppAsync'),)))
    IVdsIscsiTarget.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(8, 'Delete', ((1, 'ppAsync'),)))
    IVdsIscsiTarget.SetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'SetFriendlyName', ((1, 'pwszFriendlyName'),)))
    IVdsIscsiTarget.SetSharedSecret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_SHARED_SECRET_head),win32more.Foundation.PWSTR)(10, 'SetSharedSecret', ((1, 'pTargetSharedSecret'),(1, 'pwszInitiatorName'),)))
    IVdsIscsiTarget.RememberInitiatorSharedSecret = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_SHARED_SECRET_head))(11, 'RememberInitiatorSharedSecret', ((1, 'pwszInitiatorName'),(1, 'pInitiatorSharedSecret'),)))
    IVdsIscsiTarget.GetConnectedInitiators = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Foundation.PWSTR)),POINTER(Int32))(12, 'GetConnectedInitiators', ((1, 'pppwszInitiatorList'),(1, 'plNumberOfInitiators'),)))
    win32more.System.Com.IUnknown
    return IVdsIscsiTarget
def _define_IVdsLun_head():
    class IVdsLun(win32more.System.Com.IUnknown_head):
        Guid = Guid('3540a9c7-e60f-4111-a8-40-8b-ba-6c-2c-83-d8')
    return IVdsLun
def _define_IVdsLun():
    IVdsLun = win32more.Storage.VirtualDiskService.IVdsLun_head
    IVdsLun.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_PROP_head))(3, 'GetProperties', ((1, 'pLunProp'),)))
    IVdsLun.GetSubSystem = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsSubSystem_head))(4, 'GetSubSystem', ((1, 'ppSubSystem'),)))
    IVdsLun.GetIdentificationData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head))(5, 'GetIdentificationData', ((1, 'pLunInfo'),)))
    IVdsLun.QueryActiveControllers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(6, 'QueryActiveControllers', ((1, 'ppEnum'),)))
    IVdsLun.Extend = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(Guid),Int32,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(7, 'Extend', ((1, 'ullNumberOfBytesToAdd'),(1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'ppAsync'),)))
    IVdsLun.Shrink = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt64,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(8, 'Shrink', ((1, 'ullNumberOfBytesToRemove'),(1, 'ppAsync'),)))
    IVdsLun.QueryPlexes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(9, 'QueryPlexes', ((1, 'ppEnum'),)))
    IVdsLun.AddPlex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(10, 'AddPlex', ((1, 'lunId'),(1, 'ppAsync'),)))
    IVdsLun.RemovePlex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(11, 'RemovePlex', ((1, 'plexId'),(1, 'ppAsync'),)))
    IVdsLun.Recover = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(12, 'Recover', ((1, 'ppAsync'),)))
    IVdsLun.SetMask = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(13, 'SetMask', ((1, 'pwszUnmaskingList'),)))
    IVdsLun.Delete = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(14, 'Delete', ()))
    IVdsLun.AssociateControllers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),Int32,POINTER(Guid),Int32)(15, 'AssociateControllers', ((1, 'pActiveControllerIdArray'),(1, 'lNumberOfActiveControllers'),(1, 'pInactiveControllerIdArray'),(1, 'lNumberOfInactiveControllers'),)))
    IVdsLun.QueryHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head))(16, 'QueryHints', ((1, 'pHints'),)))
    IVdsLun.ApplyHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head))(17, 'ApplyHints', ((1, 'pHints'),)))
    IVdsLun.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_STATUS)(18, 'SetStatus', ((1, 'status'),)))
    IVdsLun.QueryMaxLunExtendSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),Int32,POINTER(UInt64))(19, 'QueryMaxLunExtendSize', ((1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'pullMaxBytesToBeAdded'),)))
    win32more.System.Com.IUnknown
    return IVdsLun
def _define_IVdsLun2_head():
    class IVdsLun2(win32more.System.Com.IUnknown_head):
        Guid = Guid('e5b3a735-9efb-499a-80-71-43-94-d9-ee-6f-cb')
    return IVdsLun2
def _define_IVdsLun2():
    IVdsLun2 = win32more.Storage.VirtualDiskService.IVdsLun2_head
    IVdsLun2.QueryHints2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head))(3, 'QueryHints2', ((1, 'pHints2'),)))
    IVdsLun2.ApplyHints2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head))(4, 'ApplyHints2', ((1, 'pHints2'),)))
    win32more.System.Com.IUnknown
    return IVdsLun2
def _define_IVdsLunControllerPorts_head():
    class IVdsLunControllerPorts(win32more.System.Com.IUnknown_head):
        Guid = Guid('451fe266-da6d-406a-bb-60-82-e5-34-f8-5a-eb')
    return IVdsLunControllerPorts
def _define_IVdsLunControllerPorts():
    IVdsLunControllerPorts = win32more.Storage.VirtualDiskService.IVdsLunControllerPorts_head
    IVdsLunControllerPorts.AssociateControllerPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),Int32,POINTER(Guid),Int32)(3, 'AssociateControllerPorts', ((1, 'pActiveControllerPortIdArray'),(1, 'lNumberOfActiveControllerPorts'),(1, 'pInactiveControllerPortIdArray'),(1, 'lNumberOfInactiveControllerPorts'),)))
    IVdsLunControllerPorts.QueryActiveControllerPorts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(4, 'QueryActiveControllerPorts', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVdsLunControllerPorts
def _define_IVdsLunIscsi_head():
    class IVdsLunIscsi(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d7c1e64-b59b-45ae-b8-6a-2c-2c-c6-a4-20-67')
    return IVdsLunIscsi
def _define_IVdsLunIscsi():
    IVdsLunIscsi = win32more.Storage.VirtualDiskService.IVdsLunIscsi_head
    IVdsLunIscsi.AssociateTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),Int32)(3, 'AssociateTargets', ((1, 'pTargetIdArray'),(1, 'lNumberOfTargets'),)))
    IVdsLunIscsi.QueryAssociatedTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(4, 'QueryAssociatedTargets', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVdsLunIscsi
def _define_IVdsLunMpio_head():
    class IVdsLunMpio(win32more.System.Com.IUnknown_head):
        Guid = Guid('7c5fbae3-333a-48a1-a9-82-33-c1-57-88-cd-e3')
    return IVdsLunMpio
def _define_IVdsLunMpio():
    IVdsLunMpio = win32more.Storage.VirtualDiskService.IVdsLunMpio_head
    IVdsLunMpio.GetPathInfo = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.VirtualDiskService.VDS_PATH_INFO_head)),POINTER(Int32))(3, 'GetPathInfo', ((1, 'ppPaths'),(1, 'plNumberOfPaths'),)))
    IVdsLunMpio.GetLoadBalancePolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LOADBALANCE_POLICY_ENUM),POINTER(POINTER(win32more.Storage.VirtualDiskService.VDS_PATH_POLICY_head)),POINTER(Int32))(4, 'GetLoadBalancePolicy', ((1, 'pPolicy'),(1, 'ppPaths'),(1, 'plNumberOfPaths'),)))
    IVdsLunMpio.SetLoadBalancePolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LOADBALANCE_POLICY_ENUM,POINTER(win32more.Storage.VirtualDiskService.VDS_PATH_POLICY_head),Int32)(5, 'SetLoadBalancePolicy', ((1, 'policy'),(1, 'pPaths'),(1, 'lNumberOfPaths'),)))
    IVdsLunMpio.GetSupportedLbPolicies = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetSupportedLbPolicies', ((1, 'pulLbFlags'),)))
    win32more.System.Com.IUnknown
    return IVdsLunMpio
def _define_IVdsLunNaming_head():
    class IVdsLunNaming(win32more.System.Com.IUnknown_head):
        Guid = Guid('907504cb-6b4e-4d88-a3-4d-17-ba-66-1f-bb-06')
    return IVdsLunNaming
def _define_IVdsLunNaming():
    IVdsLunNaming = win32more.Storage.VirtualDiskService.IVdsLunNaming_head
    IVdsLunNaming.SetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'SetFriendlyName', ((1, 'pwszFriendlyName'),)))
    win32more.System.Com.IUnknown
    return IVdsLunNaming
def _define_IVdsLunNumber_head():
    class IVdsLunNumber(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3f95e46-54b3-41f9-b6-78-0f-18-71-44-3a-08')
    return IVdsLunNumber
def _define_IVdsLunNumber():
    IVdsLunNumber = win32more.Storage.VirtualDiskService.IVdsLunNumber_head
    IVdsLunNumber.GetLunNumber = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetLunNumber', ((1, 'pulLunNumber'),)))
    win32more.System.Com.IUnknown
    return IVdsLunNumber
def _define_IVdsLunPlex_head():
    class IVdsLunPlex(win32more.System.Com.IUnknown_head):
        Guid = Guid('0ee1a790-5d2e-4abb-8c-99-c4-81-e8-be-21-38')
    return IVdsLunPlex
def _define_IVdsLunPlex():
    IVdsLunPlex = win32more.Storage.VirtualDiskService.IVdsLunPlex_head
    IVdsLunPlex.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_LUN_PLEX_PROP_head))(3, 'GetProperties', ((1, 'pPlexProp'),)))
    IVdsLunPlex.GetLun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsLun_head))(4, 'GetLun', ((1, 'ppLun'),)))
    IVdsLunPlex.QueryExtents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.VirtualDiskService.VDS_DRIVE_EXTENT_head)),POINTER(Int32))(5, 'QueryExtents', ((1, 'ppExtentArray'),(1, 'plNumberOfExtents'),)))
    IVdsLunPlex.QueryHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head))(6, 'QueryHints', ((1, 'pHints'),)))
    IVdsLunPlex.ApplyHints = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head))(7, 'ApplyHints', ((1, 'pHints'),)))
    win32more.System.Com.IUnknown
    return IVdsLunPlex
def _define_IVdsMaintenance_head():
    class IVdsMaintenance(win32more.System.Com.IUnknown_head):
        Guid = Guid('daebeef3-8523-47ed-a2-b9-05-ce-cc-e2-a1-ae')
    return IVdsMaintenance
def _define_IVdsMaintenance():
    IVdsMaintenance = win32more.Storage.VirtualDiskService.IVdsMaintenance_head
    IVdsMaintenance.StartMaintenance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_MAINTENANCE_OPERATION)(3, 'StartMaintenance', ((1, 'operation'),)))
    IVdsMaintenance.StopMaintenance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_MAINTENANCE_OPERATION)(4, 'StopMaintenance', ((1, 'operation'),)))
    IVdsMaintenance.PulseMaintenance = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_MAINTENANCE_OPERATION,UInt32)(5, 'PulseMaintenance', ((1, 'operation'),(1, 'ulCount'),)))
    win32more.System.Com.IUnknown
    return IVdsMaintenance
def _define_IVdsProvider_head():
    class IVdsProvider(win32more.System.Com.IUnknown_head):
        Guid = Guid('10c5e575-7984-4e81-a5-6b-43-1f-5f-92-ae-42')
    return IVdsProvider
def _define_IVdsProvider():
    IVdsProvider = win32more.Storage.VirtualDiskService.IVdsProvider_head
    IVdsProvider.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_PROVIDER_PROP_head))(3, 'GetProperties', ((1, 'pProviderProp'),)))
    win32more.System.Com.IUnknown
    return IVdsProvider
def _define_IVdsProviderPrivate_head():
    class IVdsProviderPrivate(win32more.System.Com.IUnknown_head):
        Guid = Guid('11f3cd41-b7e8-48ff-94-72-9d-ff-01-8a-a2-92')
    return IVdsProviderPrivate
def _define_IVdsProviderPrivate():
    IVdsProviderPrivate = win32more.Storage.VirtualDiskService.IVdsProviderPrivate_head
    IVdsProviderPrivate.GetObject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,win32more.Storage.VirtualDiskService.VDS_OBJECT_TYPE,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetObject', ((1, 'ObjectId'),(1, 'type'),(1, 'ppObjectUnk'),)))
    IVdsProviderPrivate.OnLoad = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.System.Com.IUnknown_head)(4, 'OnLoad', ((1, 'pwszMachineName'),(1, 'pCallbackObject'),)))
    IVdsProviderPrivate.OnUnload = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(5, 'OnUnload', ((1, 'bForceUnload'),)))
    win32more.System.Com.IUnknown
    return IVdsProviderPrivate
def _define_IVdsProviderSupport_head():
    class IVdsProviderSupport(win32more.System.Com.IUnknown_head):
        Guid = Guid('1732be13-e8f9-4a03-bf-bc-5f-61-6a-a6-6c-e1')
    return IVdsProviderSupport
def _define_IVdsProviderSupport():
    IVdsProviderSupport = win32more.Storage.VirtualDiskService.IVdsProviderSupport_head
    IVdsProviderSupport.GetVersionSupport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetVersionSupport', ((1, 'ulVersionSupport'),)))
    win32more.System.Com.IUnknown
    return IVdsProviderSupport
def _define_IVdsStoragePool_head():
    class IVdsStoragePool(win32more.System.Com.IUnknown_head):
        Guid = Guid('932ca8cf-0eb3-4ba8-96-20-22-66-5d-7f-84-50')
    return IVdsStoragePool
def _define_IVdsStoragePool():
    IVdsStoragePool = win32more.Storage.VirtualDiskService.IVdsStoragePool_head
    IVdsStoragePool.GetProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsProvider_head))(3, 'GetProvider', ((1, 'ppProvider'),)))
    IVdsStoragePool.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_PROP_head))(4, 'GetProperties', ((1, 'pStoragePoolProp'),)))
    IVdsStoragePool.GetAttributes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_POOL_ATTRIBUTES_head))(5, 'GetAttributes', ((1, 'pStoragePoolAttributes'),)))
    IVdsStoragePool.QueryDriveExtents = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(POINTER(win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_DRIVE_EXTENT_head)),POINTER(Int32))(6, 'QueryDriveExtents', ((1, 'ppExtentArray'),(1, 'plNumberOfExtents'),)))
    IVdsStoragePool.QueryAllocatedLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(7, 'QueryAllocatedLuns', ((1, 'ppEnum'),)))
    IVdsStoragePool.QueryAllocatedStoragePools = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(8, 'QueryAllocatedStoragePools', ((1, 'ppEnum'),)))
    win32more.System.Com.IUnknown
    return IVdsStoragePool
def _define_IVdsSubSystem_head():
    class IVdsSubSystem(win32more.System.Com.IUnknown_head):
        Guid = Guid('6fcee2d3-6d90-4f91-80-e2-a5-c7-ca-ac-a9-d8')
    return IVdsSubSystem
def _define_IVdsSubSystem():
    IVdsSubSystem = win32more.Storage.VirtualDiskService.IVdsSubSystem_head
    IVdsSubSystem.GetProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_PROP_head))(3, 'GetProperties', ((1, 'pSubSystemProp'),)))
    IVdsSubSystem.GetProvider = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IVdsProvider_head))(4, 'GetProvider', ((1, 'ppProvider'),)))
    IVdsSubSystem.QueryControllers = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(5, 'QueryControllers', ((1, 'ppEnum'),)))
    IVdsSubSystem.QueryLuns = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(6, 'QueryLuns', ((1, 'ppEnum'),)))
    IVdsSubSystem.QueryDrives = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(7, 'QueryDrives', ((1, 'ppEnum'),)))
    IVdsSubSystem.GetDrive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int16,POINTER(win32more.Storage.VirtualDiskService.IVdsDrive_head))(8, 'GetDrive', ((1, 'sBusNumber'),(1, 'sSlotNumber'),(1, 'ppDrive'),)))
    IVdsSubSystem.Reenumerate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(9, 'Reenumerate', ()))
    IVdsSubSystem.SetControllerStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Guid),Int32,POINTER(Guid),Int32)(10, 'SetControllerStatus', ((1, 'pOnlineControllerIdArray'),(1, 'lNumberOfOnlineControllers'),(1, 'pOfflineControllerIdArray'),(1, 'lNumberOfOfflineControllers'),)))
    IVdsSubSystem.CreateLun = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,UInt64,POINTER(Guid),Int32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head),POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(11, 'CreateLun', ((1, 'type'),(1, 'ullSizeInBytes'),(1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'pwszUnmaskingList'),(1, 'pHints'),(1, 'ppAsync'),)))
    IVdsSubSystem.ReplaceDrive = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Guid,Guid)(12, 'ReplaceDrive', ((1, 'DriveToBeReplaced'),(1, 'ReplacementDrive'),)))
    IVdsSubSystem.SetStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_STATUS)(13, 'SetStatus', ((1, 'status'),)))
    IVdsSubSystem.QueryMaxLunCreateSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,POINTER(Guid),Int32,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS_head),POINTER(UInt64))(14, 'QueryMaxLunCreateSize', ((1, 'type'),(1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'pHints'),(1, 'pullMaxLunSize'),)))
    win32more.System.Com.IUnknown
    return IVdsSubSystem
def _define_IVdsSubSystem2_head():
    class IVdsSubSystem2(win32more.System.Com.IUnknown_head):
        Guid = Guid('be666735-7800-4a77-9d-9c-40-f8-5b-87-e2-92')
    return IVdsSubSystem2
def _define_IVdsSubSystem2():
    IVdsSubSystem2 = win32more.Storage.VirtualDiskService.IVdsSubSystem2_head
    IVdsSubSystem2.GetProperties2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_PROP2_head))(3, 'GetProperties2', ((1, 'pSubSystemProp2'),)))
    IVdsSubSystem2.GetDrive2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16,Int16,UInt32,POINTER(win32more.Storage.VirtualDiskService.IVdsDrive_head))(4, 'GetDrive2', ((1, 'sBusNumber'),(1, 'sSlotNumber'),(1, 'ulEnclosureNumber'),(1, 'ppDrive'),)))
    IVdsSubSystem2.CreateLun2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,UInt64,POINTER(Guid),Int32,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head),POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(5, 'CreateLun2', ((1, 'type'),(1, 'ullSizeInBytes'),(1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'pwszUnmaskingList'),(1, 'pHints2'),(1, 'ppAsync'),)))
    IVdsSubSystem2.QueryMaxLunCreateSize2 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.VirtualDiskService.VDS_LUN_TYPE,POINTER(Guid),Int32,POINTER(win32more.Storage.VirtualDiskService.VDS_HINTS2_head),POINTER(UInt64))(6, 'QueryMaxLunCreateSize2', ((1, 'type'),(1, 'pDriveIdArray'),(1, 'lNumberOfDrives'),(1, 'pHints2'),(1, 'pullMaxLunSize'),)))
    win32more.System.Com.IUnknown
    return IVdsSubSystem2
def _define_IVdsSubSystemInterconnect_head():
    class IVdsSubSystemInterconnect(win32more.System.Com.IUnknown_head):
        Guid = Guid('9e6fa560-c141-477b-83-ba-0b-6c-38-f7-fe-bf')
    return IVdsSubSystemInterconnect
def _define_IVdsSubSystemInterconnect():
    IVdsSubSystemInterconnect = win32more.Storage.VirtualDiskService.IVdsSubSystemInterconnect_head
    IVdsSubSystemInterconnect.GetSupportedInterconnects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetSupportedInterconnects', ((1, 'pulSupportedInterconnectsFlag'),)))
    win32more.System.Com.IUnknown
    return IVdsSubSystemInterconnect
def _define_IVdsSubSystemIscsi_head():
    class IVdsSubSystemIscsi(win32more.System.Com.IUnknown_head):
        Guid = Guid('0027346f-40d0-4b45-8c-ec-59-06-dc-03-80-c8')
    return IVdsSubSystemIscsi
def _define_IVdsSubSystemIscsi():
    IVdsSubSystemIscsi = win32more.Storage.VirtualDiskService.IVdsSubSystemIscsi_head
    IVdsSubSystemIscsi.QueryTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(3, 'QueryTargets', ((1, 'ppEnum'),)))
    IVdsSubSystemIscsi.QueryPortals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.IEnumVdsObject_head))(4, 'QueryPortals', ((1, 'ppEnum'),)))
    IVdsSubSystemIscsi.CreateTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Storage.VirtualDiskService.IVdsAsync_head))(5, 'CreateTarget', ((1, 'pwszIscsiName'),(1, 'pwszFriendlyName'),(1, 'ppAsync'),)))
    IVdsSubSystemIscsi.SetIpsecGroupPresharedKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.VirtualDiskService.VDS_ISCSI_IPSEC_KEY_head))(6, 'SetIpsecGroupPresharedKey', ((1, 'pIpsecKey'),)))
    win32more.System.Com.IUnknown
    return IVdsSubSystemIscsi
def _define_IVdsSubSystemNaming_head():
    class IVdsSubSystemNaming(win32more.System.Com.IUnknown_head):
        Guid = Guid('0d70faa3-9cd4-4900-aa-20-69-81-b6-aa-fc-75')
    return IVdsSubSystemNaming
def _define_IVdsSubSystemNaming():
    IVdsSubSystemNaming = win32more.Storage.VirtualDiskService.IVdsSubSystemNaming_head
    IVdsSubSystemNaming.SetFriendlyName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'SetFriendlyName', ((1, 'pwszFriendlyName'),)))
    win32more.System.Com.IUnknown
    return IVdsSubSystemNaming
def _define_VDS_ASYNC_OUTPUT_head():
    class VDS_ASYNC_OUTPUT(Structure):
        pass
    return VDS_ASYNC_OUTPUT
def _define_VDS_ASYNC_OUTPUT():
    VDS_ASYNC_OUTPUT = win32more.Storage.VirtualDiskService.VDS_ASYNC_OUTPUT_head
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union(Union):
        pass
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__cp(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__cp._fields_ = [
        ('ullOffset', UInt64),
        ('volumeId', Guid),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__cv(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__cv._fields_ = [
        ('pVolumeUnk', win32more.System.Com.IUnknown_head),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__bvp(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__bvp._fields_ = [
        ('pVolumeUnk', win32more.System.Com.IUnknown_head),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__sv(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__sv._fields_ = [
        ('ullReclaimedBytes', UInt64),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__cl(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__cl._fields_ = [
        ('pLunUnk', win32more.System.Com.IUnknown_head),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__ct(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__ct._fields_ = [
        ('pTargetUnk', win32more.System.Com.IUnknown_head),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__cpg(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__cpg._fields_ = [
        ('pPortalGroupUnk', win32more.System.Com.IUnknown_head),
    ]
    class VDS_ASYNC_OUTPUT__Anonymous_e__Union__cvd(Structure):
        pass
    VDS_ASYNC_OUTPUT__Anonymous_e__Union__cvd._fields_ = [
        ('pVDiskUnk', win32more.System.Com.IUnknown_head),
    ]
    VDS_ASYNC_OUTPUT__Anonymous_e__Union._fields_ = [
        ('cp', VDS_ASYNC_OUTPUT__Anonymous_e__Union__cp),
        ('cv', VDS_ASYNC_OUTPUT__Anonymous_e__Union__cv),
        ('bvp', VDS_ASYNC_OUTPUT__Anonymous_e__Union__bvp),
        ('sv', VDS_ASYNC_OUTPUT__Anonymous_e__Union__sv),
        ('cl', VDS_ASYNC_OUTPUT__Anonymous_e__Union__cl),
        ('ct', VDS_ASYNC_OUTPUT__Anonymous_e__Union__ct),
        ('cpg', VDS_ASYNC_OUTPUT__Anonymous_e__Union__cpg),
        ('cvd', VDS_ASYNC_OUTPUT__Anonymous_e__Union__cvd),
    ]
    VDS_ASYNC_OUTPUT._anonymous_ = [
        'Anonymous',
    ]
    VDS_ASYNC_OUTPUT._fields_ = [
        ('type', win32more.Storage.VirtualDiskService.VDS_ASYNC_OUTPUT_TYPE),
        ('Anonymous', VDS_ASYNC_OUTPUT__Anonymous_e__Union),
    ]
    return VDS_ASYNC_OUTPUT
VDS_ASYNC_OUTPUT_TYPE = Int32
VDS_ASYNCOUT_UNKNOWN = 0
VDS_ASYNCOUT_CREATEVOLUME = 1
VDS_ASYNCOUT_EXTENDVOLUME = 2
VDS_ASYNCOUT_SHRINKVOLUME = 3
VDS_ASYNCOUT_ADDVOLUMEPLEX = 4
VDS_ASYNCOUT_BREAKVOLUMEPLEX = 5
VDS_ASYNCOUT_REMOVEVOLUMEPLEX = 6
VDS_ASYNCOUT_REPAIRVOLUMEPLEX = 7
VDS_ASYNCOUT_RECOVERPACK = 8
VDS_ASYNCOUT_REPLACEDISK = 9
VDS_ASYNCOUT_CREATEPARTITION = 10
VDS_ASYNCOUT_CLEAN = 11
VDS_ASYNCOUT_CREATELUN = 50
VDS_ASYNCOUT_ADDLUNPLEX = 52
VDS_ASYNCOUT_REMOVELUNPLEX = 53
VDS_ASYNCOUT_EXTENDLUN = 54
VDS_ASYNCOUT_SHRINKLUN = 55
VDS_ASYNCOUT_RECOVERLUN = 56
VDS_ASYNCOUT_LOGINTOTARGET = 60
VDS_ASYNCOUT_LOGOUTFROMTARGET = 61
VDS_ASYNCOUT_CREATETARGET = 62
VDS_ASYNCOUT_CREATEPORTALGROUP = 63
VDS_ASYNCOUT_DELETETARGET = 64
VDS_ASYNCOUT_ADDPORTAL = 65
VDS_ASYNCOUT_REMOVEPORTAL = 66
VDS_ASYNCOUT_DELETEPORTALGROUP = 67
VDS_ASYNCOUT_FORMAT = 101
VDS_ASYNCOUT_CREATE_VDISK = 200
VDS_ASYNCOUT_ATTACH_VDISK = 201
VDS_ASYNCOUT_COMPACT_VDISK = 202
VDS_ASYNCOUT_MERGE_VDISK = 203
VDS_ASYNCOUT_EXPAND_VDISK = 204
def _define_VDS_CONTROLLER_NOTIFICATION_head():
    class VDS_CONTROLLER_NOTIFICATION(Structure):
        pass
    return VDS_CONTROLLER_NOTIFICATION
def _define_VDS_CONTROLLER_NOTIFICATION():
    VDS_CONTROLLER_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_CONTROLLER_NOTIFICATION_head
    VDS_CONTROLLER_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_CONTROLLER),
        ('controllerId', Guid),
    ]
    return VDS_CONTROLLER_NOTIFICATION
def _define_VDS_CONTROLLER_PROP_head():
    class VDS_CONTROLLER_PROP(Structure):
        pass
    return VDS_CONTROLLER_PROP
def _define_VDS_CONTROLLER_PROP():
    VDS_CONTROLLER_PROP = win32more.Storage.VirtualDiskService.VDS_CONTROLLER_PROP_head
    VDS_CONTROLLER_PROP._fields_ = [
        ('id', Guid),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('status', win32more.Storage.VirtualDiskService.VDS_CONTROLLER_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('sNumberOfPorts', Int16),
    ]
    return VDS_CONTROLLER_PROP
VDS_CONTROLLER_STATUS = Int32
VDS_CS_UNKNOWN = 0
VDS_CS_ONLINE = 1
VDS_CS_NOT_READY = 2
VDS_CS_OFFLINE = 4
VDS_CS_FAILED = 5
VDS_CS_REMOVED = 8
def _define_VDS_DISK_NOTIFICATION_head():
    class VDS_DISK_NOTIFICATION(Structure):
        pass
    return VDS_DISK_NOTIFICATION
def _define_VDS_DISK_NOTIFICATION():
    VDS_DISK_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_DISK_NOTIFICATION_head
    VDS_DISK_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_DISK),
        ('diskId', Guid),
    ]
    return VDS_DISK_NOTIFICATION
def _define_VDS_DRIVE_EXTENT_head():
    class VDS_DRIVE_EXTENT(Structure):
        pass
    return VDS_DRIVE_EXTENT
def _define_VDS_DRIVE_EXTENT():
    VDS_DRIVE_EXTENT = win32more.Storage.VirtualDiskService.VDS_DRIVE_EXTENT_head
    VDS_DRIVE_EXTENT._fields_ = [
        ('id', Guid),
        ('LunId', Guid),
        ('ullSize', UInt64),
        ('bUsed', win32more.Foundation.BOOL),
    ]
    return VDS_DRIVE_EXTENT
VDS_DRIVE_FLAG = Int32
VDS_DRF_HOTSPARE = 1
VDS_DRF_ASSIGNED = 2
VDS_DRF_UNASSIGNED = 4
VDS_DRF_HOTSPARE_IN_USE = 8
VDS_DRF_HOTSPARE_STANDBY = 16
def _define_VDS_DRIVE_LETTER_NOTIFICATION_head():
    class VDS_DRIVE_LETTER_NOTIFICATION(Structure):
        pass
    return VDS_DRIVE_LETTER_NOTIFICATION
def _define_VDS_DRIVE_LETTER_NOTIFICATION():
    VDS_DRIVE_LETTER_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_DRIVE_LETTER_NOTIFICATION_head
    VDS_DRIVE_LETTER_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('wcLetter', Char),
        ('volumeId', Guid),
    ]
    return VDS_DRIVE_LETTER_NOTIFICATION
def _define_VDS_DRIVE_NOTIFICATION_head():
    class VDS_DRIVE_NOTIFICATION(Structure):
        pass
    return VDS_DRIVE_NOTIFICATION
def _define_VDS_DRIVE_NOTIFICATION():
    VDS_DRIVE_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_DRIVE_NOTIFICATION_head
    VDS_DRIVE_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_DRIVE),
        ('driveId', Guid),
    ]
    return VDS_DRIVE_NOTIFICATION
def _define_VDS_DRIVE_PROP_head():
    class VDS_DRIVE_PROP(Structure):
        pass
    return VDS_DRIVE_PROP
def _define_VDS_DRIVE_PROP():
    VDS_DRIVE_PROP = win32more.Storage.VirtualDiskService.VDS_DRIVE_PROP_head
    VDS_DRIVE_PROP._fields_ = [
        ('id', Guid),
        ('ullSize', UInt64),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('ulFlags', UInt32),
        ('status', win32more.Storage.VirtualDiskService.VDS_DRIVE_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('sInternalBusNumber', Int16),
        ('sSlotNumber', Int16),
    ]
    return VDS_DRIVE_PROP
def _define_VDS_DRIVE_PROP2_head():
    class VDS_DRIVE_PROP2(Structure):
        pass
    return VDS_DRIVE_PROP2
def _define_VDS_DRIVE_PROP2():
    VDS_DRIVE_PROP2 = win32more.Storage.VirtualDiskService.VDS_DRIVE_PROP2_head
    VDS_DRIVE_PROP2._fields_ = [
        ('id', Guid),
        ('ullSize', UInt64),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('ulFlags', UInt32),
        ('status', win32more.Storage.VirtualDiskService.VDS_DRIVE_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('sInternalBusNumber', Int16),
        ('sSlotNumber', Int16),
        ('ulEnclosureNumber', UInt32),
        ('busType', win32more.Storage.VirtualDiskService.VDS_STORAGE_BUS_TYPE),
        ('ulSpindleSpeed', UInt32),
    ]
    return VDS_DRIVE_PROP2
VDS_DRIVE_STATUS = Int32
VDS_DRS_UNKNOWN = 0
VDS_DRS_ONLINE = 1
VDS_DRS_NOT_READY = 2
VDS_DRS_OFFLINE = 4
VDS_DRS_FAILED = 5
VDS_DRS_REMOVED = 8
def _define_VDS_FILE_SYSTEM_NOTIFICATION_head():
    class VDS_FILE_SYSTEM_NOTIFICATION(Structure):
        pass
    return VDS_FILE_SYSTEM_NOTIFICATION
def _define_VDS_FILE_SYSTEM_NOTIFICATION():
    VDS_FILE_SYSTEM_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_FILE_SYSTEM_NOTIFICATION_head
    VDS_FILE_SYSTEM_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_FILE_SYSTEM),
        ('volumeId', Guid),
        ('dwPercentCompleted', UInt32),
    ]
    return VDS_FILE_SYSTEM_NOTIFICATION
VDS_FILE_SYSTEM_TYPE = Int32
VDS_FST_UNKNOWN = 0
VDS_FST_RAW = 1
VDS_FST_FAT = 2
VDS_FST_FAT32 = 3
VDS_FST_NTFS = 4
VDS_FST_CDFS = 5
VDS_FST_UDF = 6
VDS_FST_EXFAT = 7
VDS_FST_CSVFS = 8
VDS_FST_REFS = 9
def _define_VDS_HBAPORT_PROP_head():
    class VDS_HBAPORT_PROP(Structure):
        pass
    return VDS_HBAPORT_PROP
def _define_VDS_HBAPORT_PROP():
    VDS_HBAPORT_PROP = win32more.Storage.VirtualDiskService.VDS_HBAPORT_PROP_head
    VDS_HBAPORT_PROP._fields_ = [
        ('id', Guid),
        ('wwnNode', win32more.Storage.VirtualDiskService.VDS_WWN),
        ('wwnPort', win32more.Storage.VirtualDiskService.VDS_WWN),
        ('type', win32more.Storage.VirtualDiskService.VDS_HBAPORT_TYPE),
        ('status', win32more.Storage.VirtualDiskService.VDS_HBAPORT_STATUS),
        ('ulPortSpeed', UInt32),
        ('ulSupportedPortSpeed', UInt32),
    ]
    return VDS_HBAPORT_PROP
VDS_HBAPORT_SPEED_FLAG = Int32
VDS_HSF_UNKNOWN = 0
VDS_HSF_1GBIT = 1
VDS_HSF_2GBIT = 2
VDS_HSF_10GBIT = 4
VDS_HSF_4GBIT = 8
VDS_HSF_NOT_NEGOTIATED = 32768
VDS_HBAPORT_STATUS = Int32
VDS_HPS_UNKNOWN = 1
VDS_HPS_ONLINE = 2
VDS_HPS_OFFLINE = 3
VDS_HPS_BYPASSED = 4
VDS_HPS_DIAGNOSTICS = 5
VDS_HPS_LINKDOWN = 6
VDS_HPS_ERROR = 7
VDS_HPS_LOOPBACK = 8
VDS_HBAPORT_TYPE = Int32
VDS_HPT_UNKNOWN = 1
VDS_HPT_OTHER = 2
VDS_HPT_NOTPRESENT = 3
VDS_HPT_NPORT = 5
VDS_HPT_NLPORT = 6
VDS_HPT_FLPORT = 7
VDS_HPT_FPORT = 8
VDS_HPT_EPORT = 9
VDS_HPT_GPORT = 10
VDS_HPT_LPORT = 20
VDS_HPT_PTP = 21
VDS_HEALTH = Int32
VDS_H_UNKNOWN = 0
VDS_H_HEALTHY = 1
VDS_H_REBUILDING = 2
VDS_H_STALE = 3
VDS_H_FAILING = 4
VDS_H_FAILING_REDUNDANCY = 5
VDS_H_FAILED_REDUNDANCY = 6
VDS_H_FAILED_REDUNDANCY_FAILING = 7
VDS_H_FAILED = 8
VDS_H_REPLACED = 9
VDS_H_PENDING_FAILURE = 10
VDS_H_DEGRADED = 11
def _define_VDS_HINTS_head():
    class VDS_HINTS(Structure):
        pass
    return VDS_HINTS
def _define_VDS_HINTS():
    VDS_HINTS = win32more.Storage.VirtualDiskService.VDS_HINTS_head
    VDS_HINTS._fields_ = [
        ('ullHintMask', UInt64),
        ('ullExpectedMaximumSize', UInt64),
        ('ulOptimalReadSize', UInt32),
        ('ulOptimalReadAlignment', UInt32),
        ('ulOptimalWriteSize', UInt32),
        ('ulOptimalWriteAlignment', UInt32),
        ('ulMaximumDriveCount', UInt32),
        ('ulStripeSize', UInt32),
        ('bFastCrashRecoveryRequired', win32more.Foundation.BOOL),
        ('bMostlyReads', win32more.Foundation.BOOL),
        ('bOptimizeForSequentialReads', win32more.Foundation.BOOL),
        ('bOptimizeForSequentialWrites', win32more.Foundation.BOOL),
        ('bRemapEnabled', win32more.Foundation.BOOL),
        ('bReadBackVerifyEnabled', win32more.Foundation.BOOL),
        ('bWriteThroughCachingEnabled', win32more.Foundation.BOOL),
        ('bHardwareChecksumEnabled', win32more.Foundation.BOOL),
        ('bIsYankable', win32more.Foundation.BOOL),
        ('sRebuildPriority', Int16),
    ]
    return VDS_HINTS
def _define_VDS_HINTS2_head():
    class VDS_HINTS2(Structure):
        pass
    return VDS_HINTS2
def _define_VDS_HINTS2():
    VDS_HINTS2 = win32more.Storage.VirtualDiskService.VDS_HINTS2_head
    VDS_HINTS2._fields_ = [
        ('ullHintMask', UInt64),
        ('ullExpectedMaximumSize', UInt64),
        ('ulOptimalReadSize', UInt32),
        ('ulOptimalReadAlignment', UInt32),
        ('ulOptimalWriteSize', UInt32),
        ('ulOptimalWriteAlignment', UInt32),
        ('ulMaximumDriveCount', UInt32),
        ('ulStripeSize', UInt32),
        ('ulReserved1', UInt32),
        ('ulReserved2', UInt32),
        ('ulReserved3', UInt32),
        ('bFastCrashRecoveryRequired', win32more.Foundation.BOOL),
        ('bMostlyReads', win32more.Foundation.BOOL),
        ('bOptimizeForSequentialReads', win32more.Foundation.BOOL),
        ('bOptimizeForSequentialWrites', win32more.Foundation.BOOL),
        ('bRemapEnabled', win32more.Foundation.BOOL),
        ('bReadBackVerifyEnabled', win32more.Foundation.BOOL),
        ('bWriteThroughCachingEnabled', win32more.Foundation.BOOL),
        ('bHardwareChecksumEnabled', win32more.Foundation.BOOL),
        ('bIsYankable', win32more.Foundation.BOOL),
        ('bAllocateHotSpare', win32more.Foundation.BOOL),
        ('bUseMirroredCache', win32more.Foundation.BOOL),
        ('bReadCachingEnabled', win32more.Foundation.BOOL),
        ('bWriteCachingEnabled', win32more.Foundation.BOOL),
        ('bMediaScanEnabled', win32more.Foundation.BOOL),
        ('bConsistencyCheckEnabled', win32more.Foundation.BOOL),
        ('BusType', win32more.Storage.VirtualDiskService.VDS_STORAGE_BUS_TYPE),
        ('bReserved1', win32more.Foundation.BOOL),
        ('bReserved2', win32more.Foundation.BOOL),
        ('bReserved3', win32more.Foundation.BOOL),
        ('sRebuildPriority', Int16),
    ]
    return VDS_HINTS2
VDS_HWPROVIDER_TYPE = Int32
VDS_HWT_UNKNOWN = 0
VDS_HWT_PCI_RAID = 1
VDS_HWT_FIBRE_CHANNEL = 2
VDS_HWT_ISCSI = 3
VDS_HWT_SAS = 4
VDS_HWT_HYBRID = 5
def _define_VDS_INTERCONNECT_head():
    class VDS_INTERCONNECT(Structure):
        pass
    return VDS_INTERCONNECT
def _define_VDS_INTERCONNECT():
    VDS_INTERCONNECT = win32more.Storage.VirtualDiskService.VDS_INTERCONNECT_head
    VDS_INTERCONNECT._fields_ = [
        ('m_addressType', win32more.Storage.VirtualDiskService.VDS_INTERCONNECT_ADDRESS_TYPE),
        ('m_cbPort', UInt32),
        ('m_pbPort', c_char_p_no),
        ('m_cbAddress', UInt32),
        ('m_pbAddress', c_char_p_no),
    ]
    return VDS_INTERCONNECT
VDS_INTERCONNECT_ADDRESS_TYPE = Int32
VDS_IA_UNKNOWN = 0
VDS_IA_FCFS = 1
VDS_IA_FCPH = 2
VDS_IA_FCPH3 = 3
VDS_IA_MAC = 4
VDS_IA_SCSI = 5
VDS_INTERCONNECT_FLAG = Int32
VDS_ITF_PCI_RAID = 1
VDS_ITF_FIBRE_CHANNEL = 2
VDS_ITF_ISCSI = 4
VDS_ITF_SAS = 8
def _define_VDS_IPADDRESS_head():
    class VDS_IPADDRESS(Structure):
        pass
    return VDS_IPADDRESS
def _define_VDS_IPADDRESS():
    VDS_IPADDRESS = win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head
    VDS_IPADDRESS._fields_ = [
        ('type', win32more.Storage.VirtualDiskService.VDS_IPADDRESS_TYPE),
        ('ipv4Address', UInt32),
        ('ipv6Address', Byte * 16),
        ('ulIpv6FlowInfo', UInt32),
        ('ulIpv6ScopeId', UInt32),
        ('wszTextAddress', Char * 257),
        ('ulPort', UInt32),
    ]
    return VDS_IPADDRESS
VDS_IPADDRESS_TYPE = Int32
VDS_IPT_TEXT = 0
VDS_IPT_IPV4 = 1
VDS_IPT_IPV6 = 2
VDS_IPT_EMPTY = 3
VDS_ISCSI_AUTH_TYPE = Int32
VDS_IAT_NONE = 0
VDS_IAT_CHAP = 1
VDS_IAT_MUTUAL_CHAP = 2
def _define_VDS_ISCSI_INITIATOR_ADAPTER_PROP_head():
    class VDS_ISCSI_INITIATOR_ADAPTER_PROP(Structure):
        pass
    return VDS_ISCSI_INITIATOR_ADAPTER_PROP
def _define_VDS_ISCSI_INITIATOR_ADAPTER_PROP():
    VDS_ISCSI_INITIATOR_ADAPTER_PROP = win32more.Storage.VirtualDiskService.VDS_ISCSI_INITIATOR_ADAPTER_PROP_head
    VDS_ISCSI_INITIATOR_ADAPTER_PROP._fields_ = [
        ('id', Guid),
        ('pwszName', win32more.Foundation.PWSTR),
    ]
    return VDS_ISCSI_INITIATOR_ADAPTER_PROP
def _define_VDS_ISCSI_INITIATOR_PORTAL_PROP_head():
    class VDS_ISCSI_INITIATOR_PORTAL_PROP(Structure):
        pass
    return VDS_ISCSI_INITIATOR_PORTAL_PROP
def _define_VDS_ISCSI_INITIATOR_PORTAL_PROP():
    VDS_ISCSI_INITIATOR_PORTAL_PROP = win32more.Storage.VirtualDiskService.VDS_ISCSI_INITIATOR_PORTAL_PROP_head
    VDS_ISCSI_INITIATOR_PORTAL_PROP._fields_ = [
        ('id', Guid),
        ('address', win32more.Storage.VirtualDiskService.VDS_IPADDRESS),
        ('ulPortIndex', UInt32),
    ]
    return VDS_ISCSI_INITIATOR_PORTAL_PROP
VDS_ISCSI_IPSEC_FLAG = Int32
VDS_IIF_VALID = 1
VDS_IIF_IKE = 2
VDS_IIF_MAIN_MODE = 4
VDS_IIF_AGGRESSIVE_MODE = 8
VDS_IIF_PFS_ENABLE = 16
VDS_IIF_TRANSPORT_MODE_PREFERRED = 32
VDS_IIF_TUNNEL_MODE_PREFERRED = 64
def _define_VDS_ISCSI_IPSEC_KEY_head():
    class VDS_ISCSI_IPSEC_KEY(Structure):
        pass
    return VDS_ISCSI_IPSEC_KEY
def _define_VDS_ISCSI_IPSEC_KEY():
    VDS_ISCSI_IPSEC_KEY = win32more.Storage.VirtualDiskService.VDS_ISCSI_IPSEC_KEY_head
    VDS_ISCSI_IPSEC_KEY._fields_ = [
        ('pKey', c_char_p_no),
        ('ulKeySize', UInt32),
    ]
    return VDS_ISCSI_IPSEC_KEY
VDS_ISCSI_LOGIN_FLAG = Int32
VDS_ILF_REQUIRE_IPSEC = 1
VDS_ILF_MULTIPATH_ENABLED = 2
VDS_ISCSI_LOGIN_TYPE = Int32
VDS_ILT_MANUAL = 0
VDS_ILT_PERSISTENT = 1
VDS_ILT_BOOT = 2
def _define_VDS_ISCSI_PORTAL_PROP_head():
    class VDS_ISCSI_PORTAL_PROP(Structure):
        pass
    return VDS_ISCSI_PORTAL_PROP
def _define_VDS_ISCSI_PORTAL_PROP():
    VDS_ISCSI_PORTAL_PROP = win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTAL_PROP_head
    VDS_ISCSI_PORTAL_PROP._fields_ = [
        ('id', Guid),
        ('address', win32more.Storage.VirtualDiskService.VDS_IPADDRESS),
        ('status', win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTAL_STATUS),
    ]
    return VDS_ISCSI_PORTAL_PROP
VDS_ISCSI_PORTAL_STATUS = Int32
VDS_IPS_UNKNOWN = 0
VDS_IPS_ONLINE = 1
VDS_IPS_NOT_READY = 2
VDS_IPS_OFFLINE = 4
VDS_IPS_FAILED = 5
def _define_VDS_ISCSI_PORTALGROUP_PROP_head():
    class VDS_ISCSI_PORTALGROUP_PROP(Structure):
        pass
    return VDS_ISCSI_PORTALGROUP_PROP
def _define_VDS_ISCSI_PORTALGROUP_PROP():
    VDS_ISCSI_PORTALGROUP_PROP = win32more.Storage.VirtualDiskService.VDS_ISCSI_PORTALGROUP_PROP_head
    VDS_ISCSI_PORTALGROUP_PROP._fields_ = [
        ('id', Guid),
        ('tag', UInt16),
    ]
    return VDS_ISCSI_PORTALGROUP_PROP
def _define_VDS_ISCSI_SHARED_SECRET_head():
    class VDS_ISCSI_SHARED_SECRET(Structure):
        pass
    return VDS_ISCSI_SHARED_SECRET
def _define_VDS_ISCSI_SHARED_SECRET():
    VDS_ISCSI_SHARED_SECRET = win32more.Storage.VirtualDiskService.VDS_ISCSI_SHARED_SECRET_head
    VDS_ISCSI_SHARED_SECRET._fields_ = [
        ('pSharedSecret', c_char_p_no),
        ('ulSharedSecretSize', UInt32),
    ]
    return VDS_ISCSI_SHARED_SECRET
def _define_VDS_ISCSI_TARGET_PROP_head():
    class VDS_ISCSI_TARGET_PROP(Structure):
        pass
    return VDS_ISCSI_TARGET_PROP
def _define_VDS_ISCSI_TARGET_PROP():
    VDS_ISCSI_TARGET_PROP = win32more.Storage.VirtualDiskService.VDS_ISCSI_TARGET_PROP_head
    VDS_ISCSI_TARGET_PROP._fields_ = [
        ('id', Guid),
        ('pwszIscsiName', win32more.Foundation.PWSTR),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('bChapEnabled', win32more.Foundation.BOOL),
    ]
    return VDS_ISCSI_TARGET_PROP
VDS_LOADBALANCE_POLICY_ENUM = Int32
VDS_LBP_UNKNOWN = 0
VDS_LBP_FAILOVER = 1
VDS_LBP_ROUND_ROBIN = 2
VDS_LBP_ROUND_ROBIN_WITH_SUBSET = 3
VDS_LBP_DYN_LEAST_QUEUE_DEPTH = 4
VDS_LBP_WEIGHTED_PATHS = 5
VDS_LBP_LEAST_BLOCKS = 6
VDS_LBP_VENDOR_SPECIFIC = 7
VDS_LUN_FLAG = Int32
VDS_LF_LBN_REMAP_ENABLED = 1
VDS_LF_READ_BACK_VERIFY_ENABLED = 2
VDS_LF_WRITE_THROUGH_CACHING_ENABLED = 4
VDS_LF_HARDWARE_CHECKSUM_ENABLED = 8
VDS_LF_READ_CACHE_ENABLED = 16
VDS_LF_WRITE_CACHE_ENABLED = 32
VDS_LF_MEDIA_SCAN_ENABLED = 64
VDS_LF_CONSISTENCY_CHECK_ENABLED = 128
VDS_LF_SNAPSHOT = 256
def _define_VDS_LUN_INFORMATION_head():
    class VDS_LUN_INFORMATION(Structure):
        pass
    return VDS_LUN_INFORMATION
def _define_VDS_LUN_INFORMATION():
    VDS_LUN_INFORMATION = win32more.Storage.VirtualDiskService.VDS_LUN_INFORMATION_head
    VDS_LUN_INFORMATION._fields_ = [
        ('m_version', UInt32),
        ('m_DeviceType', Byte),
        ('m_DeviceTypeModifier', Byte),
        ('m_bCommandQueueing', win32more.Foundation.BOOL),
        ('m_BusType', win32more.Storage.VirtualDiskService.VDS_STORAGE_BUS_TYPE),
        ('m_szVendorId', c_char_p_no),
        ('m_szProductId', c_char_p_no),
        ('m_szProductRevision', c_char_p_no),
        ('m_szSerialNumber', c_char_p_no),
        ('m_diskSignature', Guid),
        ('m_deviceIdDescriptor', win32more.Storage.VirtualDiskService.VDS_STORAGE_DEVICE_ID_DESCRIPTOR),
        ('m_cInterconnects', UInt32),
        ('m_rgInterconnects', POINTER(win32more.Storage.VirtualDiskService.VDS_INTERCONNECT_head)),
    ]
    return VDS_LUN_INFORMATION
def _define_VDS_LUN_NOTIFICATION_head():
    class VDS_LUN_NOTIFICATION(Structure):
        pass
    return VDS_LUN_NOTIFICATION
def _define_VDS_LUN_NOTIFICATION():
    VDS_LUN_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_LUN_NOTIFICATION_head
    VDS_LUN_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_LUN),
        ('LunId', Guid),
    ]
    return VDS_LUN_NOTIFICATION
VDS_LUN_PLEX_FLAG = Int32
VDS_LPF_LBN_REMAP_ENABLED = 1
def _define_VDS_LUN_PLEX_PROP_head():
    class VDS_LUN_PLEX_PROP(Structure):
        pass
    return VDS_LUN_PLEX_PROP
def _define_VDS_LUN_PLEX_PROP():
    VDS_LUN_PLEX_PROP = win32more.Storage.VirtualDiskService.VDS_LUN_PLEX_PROP_head
    VDS_LUN_PLEX_PROP._fields_ = [
        ('id', Guid),
        ('ullSize', UInt64),
        ('type', win32more.Storage.VirtualDiskService.VDS_LUN_PLEX_TYPE),
        ('status', win32more.Storage.VirtualDiskService.VDS_LUN_PLEX_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('TransitionState', win32more.Storage.VirtualDiskService.VDS_TRANSITION_STATE),
        ('ulFlags', UInt32),
        ('ulStripeSize', UInt32),
        ('sRebuildPriority', Int16),
    ]
    return VDS_LUN_PLEX_PROP
VDS_LUN_PLEX_STATUS = Int32
VDS_LPS_UNKNOWN = 0
VDS_LPS_ONLINE = 1
VDS_LPS_NOT_READY = 2
VDS_LPS_OFFLINE = 4
VDS_LPS_FAILED = 5
VDS_LUN_PLEX_TYPE = Int32
VDS_LPT_UNKNOWN = 0
VDS_LPT_SIMPLE = 10
VDS_LPT_SPAN = 11
VDS_LPT_STRIPE = 12
VDS_LPT_PARITY = 14
VDS_LPT_RAID2 = 15
VDS_LPT_RAID3 = 16
VDS_LPT_RAID4 = 17
VDS_LPT_RAID5 = 18
VDS_LPT_RAID6 = 19
VDS_LPT_RAID03 = 21
VDS_LPT_RAID05 = 22
VDS_LPT_RAID10 = 23
VDS_LPT_RAID15 = 24
VDS_LPT_RAID30 = 25
VDS_LPT_RAID50 = 26
VDS_LPT_RAID53 = 28
VDS_LPT_RAID60 = 29
def _define_VDS_LUN_PROP_head():
    class VDS_LUN_PROP(Structure):
        pass
    return VDS_LUN_PROP
def _define_VDS_LUN_PROP():
    VDS_LUN_PROP = win32more.Storage.VirtualDiskService.VDS_LUN_PROP_head
    VDS_LUN_PROP._fields_ = [
        ('id', Guid),
        ('ullSize', UInt64),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('pwszUnmaskingList', win32more.Foundation.PWSTR),
        ('ulFlags', UInt32),
        ('type', win32more.Storage.VirtualDiskService.VDS_LUN_TYPE),
        ('status', win32more.Storage.VirtualDiskService.VDS_LUN_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('TransitionState', win32more.Storage.VirtualDiskService.VDS_TRANSITION_STATE),
        ('sRebuildPriority', Int16),
    ]
    return VDS_LUN_PROP
VDS_LUN_STATUS = Int32
VDS_LS_UNKNOWN = 0
VDS_LS_ONLINE = 1
VDS_LS_NOT_READY = 2
VDS_LS_OFFLINE = 4
VDS_LS_FAILED = 5
VDS_LUN_TYPE = Int32
VDS_LT_UNKNOWN = 0
VDS_LT_DEFAULT = 1
VDS_LT_FAULT_TOLERANT = 2
VDS_LT_NON_FAULT_TOLERANT = 3
VDS_LT_SIMPLE = 10
VDS_LT_SPAN = 11
VDS_LT_STRIPE = 12
VDS_LT_MIRROR = 13
VDS_LT_PARITY = 14
VDS_LT_RAID2 = 15
VDS_LT_RAID3 = 16
VDS_LT_RAID4 = 17
VDS_LT_RAID5 = 18
VDS_LT_RAID6 = 19
VDS_LT_RAID01 = 20
VDS_LT_RAID03 = 21
VDS_LT_RAID05 = 22
VDS_LT_RAID10 = 23
VDS_LT_RAID15 = 24
VDS_LT_RAID30 = 25
VDS_LT_RAID50 = 26
VDS_LT_RAID51 = 27
VDS_LT_RAID53 = 28
VDS_LT_RAID60 = 29
VDS_LT_RAID61 = 30
VDS_MAINTENANCE_OPERATION = Int32
VDS_MAINTENANCE_OPERATION_BlinkLight = 1
VDS_MAINTENANCE_OPERATION_BeepAlarm = 2
VDS_MAINTENANCE_OPERATION_SpinDown = 3
VDS_MAINTENANCE_OPERATION_SpinUp = 4
VDS_MAINTENANCE_OPERATION_Ping = 5
def _define_VDS_MOUNT_POINT_NOTIFICATION_head():
    class VDS_MOUNT_POINT_NOTIFICATION(Structure):
        pass
    return VDS_MOUNT_POINT_NOTIFICATION
def _define_VDS_MOUNT_POINT_NOTIFICATION():
    VDS_MOUNT_POINT_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_MOUNT_POINT_NOTIFICATION_head
    VDS_MOUNT_POINT_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('volumeId', Guid),
    ]
    return VDS_MOUNT_POINT_NOTIFICATION
VDS_NF_CONTROLLER = UInt32
VDS_NF_CONTROLLER_ARRIVE = 103
VDS_NF_CONTROLLER_DEPART = 104
VDS_NF_CONTROLLER_MODIFY = 350
VDS_NF_CONTROLLER_REMOVED = 351
VDS_NF_DISK = UInt32
VDS_NF_DISK_ARRIVE = 8
VDS_NF_DISK_DEPART = 9
VDS_NF_DISK_MODIFY = 10
VDS_NF_DRIVE = UInt32
VDS_NF_DRIVE_ARRIVE = 105
VDS_NF_DRIVE_DEPART = 106
VDS_NF_DRIVE_MODIFY = 107
VDS_NF_DRIVE_REMOVED = 354
VDS_NF_FILE_SYSTEM = UInt32
VDS_NF_FILE_SYSTEM_MODIFY = 203
VDS_NF_FILE_SYSTEM_FORMAT_PROGRESS = 204
VDS_NF_LUN = UInt32
VDS_NF_LUN_ARRIVE = 108
VDS_NF_LUN_DEPART = 109
VDS_NF_LUN_MODIFY = 110
VDS_NF_PACK = UInt32
VDS_NF_PACK_ARRIVE = 1
VDS_NF_PACK_DEPART = 2
VDS_NF_PACK_MODIFY = 3
VDS_NF_PORT = UInt32
VDS_NF_PORT_ARRIVE = 121
VDS_NF_PORT_DEPART = 122
VDS_NF_PORT_MODIFY = 352
VDS_NF_PORT_REMOVED = 353
def _define_VDS_NOTIFICATION_head():
    class VDS_NOTIFICATION(Structure):
        pass
    return VDS_NOTIFICATION
def _define_VDS_NOTIFICATION():
    VDS_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_NOTIFICATION_head
    class VDS_NOTIFICATION__Anonymous_e__Union(Union):
        pass
    VDS_NOTIFICATION__Anonymous_e__Union._fields_ = [
        ('Pack', win32more.Storage.VirtualDiskService.VDS_PACK_NOTIFICATION),
        ('Disk', win32more.Storage.VirtualDiskService.VDS_DISK_NOTIFICATION),
        ('Volume', win32more.Storage.VirtualDiskService.VDS_VOLUME_NOTIFICATION),
        ('Partition', win32more.Storage.VirtualDiskService.VDS_PARTITION_NOTIFICATION),
        ('Letter', win32more.Storage.VirtualDiskService.VDS_DRIVE_LETTER_NOTIFICATION),
        ('FileSystem', win32more.Storage.VirtualDiskService.VDS_FILE_SYSTEM_NOTIFICATION),
        ('MountPoint', win32more.Storage.VirtualDiskService.VDS_MOUNT_POINT_NOTIFICATION),
        ('SubSystem', win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_NOTIFICATION),
        ('Controller', win32more.Storage.VirtualDiskService.VDS_CONTROLLER_NOTIFICATION),
        ('Drive', win32more.Storage.VirtualDiskService.VDS_DRIVE_NOTIFICATION),
        ('Lun', win32more.Storage.VirtualDiskService.VDS_LUN_NOTIFICATION),
        ('Port', win32more.Storage.VirtualDiskService.VDS_PORT_NOTIFICATION),
        ('Portal', win32more.Storage.VirtualDiskService.VDS_PORTAL_NOTIFICATION),
        ('Target', win32more.Storage.VirtualDiskService.VDS_TARGET_NOTIFICATION),
        ('PortalGroup', win32more.Storage.VirtualDiskService.VDS_PORTAL_GROUP_NOTIFICATION),
        ('Service', win32more.Storage.VirtualDiskService.VDS_SERVICE_NOTIFICATION),
    ]
    VDS_NOTIFICATION._anonymous_ = [
        'Anonymous',
    ]
    VDS_NOTIFICATION._fields_ = [
        ('objectType', win32more.Storage.VirtualDiskService.VDS_NOTIFICATION_TARGET_TYPE),
        ('Anonymous', VDS_NOTIFICATION__Anonymous_e__Union),
    ]
    return VDS_NOTIFICATION
VDS_NOTIFICATION_TARGET_TYPE = Int32
VDS_NTT_UNKNOWN = 0
VDS_NTT_PACK = 10
VDS_NTT_VOLUME = 11
VDS_NTT_DISK = 13
VDS_NTT_PARTITION = 60
VDS_NTT_DRIVE_LETTER = 61
VDS_NTT_FILE_SYSTEM = 62
VDS_NTT_MOUNT_POINT = 63
VDS_NTT_SUB_SYSTEM = 30
VDS_NTT_CONTROLLER = 31
VDS_NTT_DRIVE = 32
VDS_NTT_LUN = 33
VDS_NTT_PORT = 35
VDS_NTT_PORTAL = 36
VDS_NTT_TARGET = 37
VDS_NTT_PORTAL_GROUP = 38
VDS_NTT_SERVICE = 200
VDS_OBJECT_TYPE = Int32
VDS_OT_UNKNOWN = 0
VDS_OT_PROVIDER = 1
VDS_OT_PACK = 10
VDS_OT_VOLUME = 11
VDS_OT_VOLUME_PLEX = 12
VDS_OT_DISK = 13
VDS_OT_SUB_SYSTEM = 30
VDS_OT_CONTROLLER = 31
VDS_OT_DRIVE = 32
VDS_OT_LUN = 33
VDS_OT_LUN_PLEX = 34
VDS_OT_PORT = 35
VDS_OT_PORTAL = 36
VDS_OT_TARGET = 37
VDS_OT_PORTAL_GROUP = 38
VDS_OT_STORAGE_POOL = 39
VDS_OT_HBAPORT = 90
VDS_OT_INIT_ADAPTER = 91
VDS_OT_INIT_PORTAL = 92
VDS_OT_ASYNC = 100
VDS_OT_ENUM = 101
VDS_OT_VDISK = 200
VDS_OT_OPEN_VDISK = 201
def _define_VDS_PACK_NOTIFICATION_head():
    class VDS_PACK_NOTIFICATION(Structure):
        pass
    return VDS_PACK_NOTIFICATION
def _define_VDS_PACK_NOTIFICATION():
    VDS_PACK_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_PACK_NOTIFICATION_head
    VDS_PACK_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_PACK),
        ('packId', Guid),
    ]
    return VDS_PACK_NOTIFICATION
def _define_VDS_PARTITION_NOTIFICATION_head():
    class VDS_PARTITION_NOTIFICATION(Structure):
        pass
    return VDS_PARTITION_NOTIFICATION
def _define_VDS_PARTITION_NOTIFICATION():
    VDS_PARTITION_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_PARTITION_NOTIFICATION_head
    VDS_PARTITION_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('diskId', Guid),
        ('ullOffset', UInt64),
    ]
    return VDS_PARTITION_NOTIFICATION
def _define_VDS_PATH_ID_head():
    class VDS_PATH_ID(Structure):
        pass
    return VDS_PATH_ID
def _define_VDS_PATH_ID():
    VDS_PATH_ID = win32more.Storage.VirtualDiskService.VDS_PATH_ID_head
    VDS_PATH_ID._fields_ = [
        ('ullSourceId', UInt64),
        ('ullPathId', UInt64),
    ]
    return VDS_PATH_ID
def _define_VDS_PATH_INFO_head():
    class VDS_PATH_INFO(Structure):
        pass
    return VDS_PATH_INFO
def _define_VDS_PATH_INFO():
    VDS_PATH_INFO = win32more.Storage.VirtualDiskService.VDS_PATH_INFO_head
    class VDS_PATH_INFO__Anonymous1_e__Union(Union):
        pass
    VDS_PATH_INFO__Anonymous1_e__Union._fields_ = [
        ('controllerPortId', Guid),
        ('targetPortalId', Guid),
    ]
    class VDS_PATH_INFO__Anonymous2_e__Union(Union):
        pass
    VDS_PATH_INFO__Anonymous2_e__Union._fields_ = [
        ('hbaPortId', Guid),
        ('initiatorAdapterId', Guid),
    ]
    class VDS_PATH_INFO__Anonymous3_e__Union(Union):
        pass
    VDS_PATH_INFO__Anonymous3_e__Union._fields_ = [
        ('pHbaPortProp', POINTER(win32more.Storage.VirtualDiskService.VDS_HBAPORT_PROP_head)),
        ('pInitiatorPortalIpAddr', POINTER(win32more.Storage.VirtualDiskService.VDS_IPADDRESS_head)),
    ]
    VDS_PATH_INFO._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
        'Anonymous3',
    ]
    VDS_PATH_INFO._fields_ = [
        ('pathId', win32more.Storage.VirtualDiskService.VDS_PATH_ID),
        ('type', win32more.Storage.VirtualDiskService.VDS_HWPROVIDER_TYPE),
        ('status', win32more.Storage.VirtualDiskService.VDS_PATH_STATUS),
        ('Anonymous1', VDS_PATH_INFO__Anonymous1_e__Union),
        ('Anonymous2', VDS_PATH_INFO__Anonymous2_e__Union),
        ('Anonymous3', VDS_PATH_INFO__Anonymous3_e__Union),
    ]
    return VDS_PATH_INFO
def _define_VDS_PATH_POLICY_head():
    class VDS_PATH_POLICY(Structure):
        pass
    return VDS_PATH_POLICY
def _define_VDS_PATH_POLICY():
    VDS_PATH_POLICY = win32more.Storage.VirtualDiskService.VDS_PATH_POLICY_head
    VDS_PATH_POLICY._fields_ = [
        ('pathId', win32more.Storage.VirtualDiskService.VDS_PATH_ID),
        ('bPrimaryPath', win32more.Foundation.BOOL),
        ('ulWeight', UInt32),
    ]
    return VDS_PATH_POLICY
VDS_PATH_STATUS = Int32
VDS_MPS_UNKNOWN = 0
VDS_MPS_ONLINE = 1
VDS_MPS_FAILED = 5
VDS_MPS_STANDBY = 7
def _define_VDS_POOL_ATTRIBUTES_head():
    class VDS_POOL_ATTRIBUTES(Structure):
        pass
    return VDS_POOL_ATTRIBUTES
def _define_VDS_POOL_ATTRIBUTES():
    VDS_POOL_ATTRIBUTES = win32more.Storage.VirtualDiskService.VDS_POOL_ATTRIBUTES_head
    VDS_POOL_ATTRIBUTES._fields_ = [
        ('ullAttributeMask', UInt64),
        ('raidType', win32more.Storage.VirtualDiskService.VDS_RAID_TYPE),
        ('busType', win32more.Storage.VirtualDiskService.VDS_STORAGE_BUS_TYPE),
        ('pwszIntendedUsage', win32more.Foundation.PWSTR),
        ('bSpinDown', win32more.Foundation.BOOL),
        ('bIsThinProvisioned', win32more.Foundation.BOOL),
        ('ullProvisionedSpace', UInt64),
        ('bNoSinglePointOfFailure', win32more.Foundation.BOOL),
        ('ulDataRedundancyMax', UInt32),
        ('ulDataRedundancyMin', UInt32),
        ('ulDataRedundancyDefault', UInt32),
        ('ulPackageRedundancyMax', UInt32),
        ('ulPackageRedundancyMin', UInt32),
        ('ulPackageRedundancyDefault', UInt32),
        ('ulStripeSize', UInt32),
        ('ulStripeSizeMax', UInt32),
        ('ulStripeSizeMin', UInt32),
        ('ulDefaultStripeSize', UInt32),
        ('ulNumberOfColumns', UInt32),
        ('ulNumberOfColumnsMax', UInt32),
        ('ulNumberOfColumnsMin', UInt32),
        ('ulDefaultNumberofColumns', UInt32),
        ('ulDataAvailabilityHint', UInt32),
        ('ulAccessRandomnessHint', UInt32),
        ('ulAccessDirectionHint', UInt32),
        ('ulAccessSizeHint', UInt32),
        ('ulAccessLatencyHint', UInt32),
        ('ulAccessBandwidthWeightHint', UInt32),
        ('ulStorageCostHint', UInt32),
        ('ulStorageEfficiencyHint', UInt32),
        ('ulNumOfCustomAttributes', UInt32),
        ('pPoolCustomAttributes', POINTER(win32more.Storage.VirtualDiskService.VDS_POOL_CUSTOM_ATTRIBUTES_head)),
        ('bReserved1', win32more.Foundation.BOOL),
        ('bReserved2', win32more.Foundation.BOOL),
        ('ulReserved1', UInt32),
        ('ulReserved2', UInt32),
        ('ullReserved1', UInt64),
        ('ullReserved2', UInt64),
    ]
    return VDS_POOL_ATTRIBUTES
def _define_VDS_POOL_CUSTOM_ATTRIBUTES_head():
    class VDS_POOL_CUSTOM_ATTRIBUTES(Structure):
        pass
    return VDS_POOL_CUSTOM_ATTRIBUTES
def _define_VDS_POOL_CUSTOM_ATTRIBUTES():
    VDS_POOL_CUSTOM_ATTRIBUTES = win32more.Storage.VirtualDiskService.VDS_POOL_CUSTOM_ATTRIBUTES_head
    VDS_POOL_CUSTOM_ATTRIBUTES._fields_ = [
        ('pwszName', win32more.Foundation.PWSTR),
        ('pwszValue', win32more.Foundation.PWSTR),
    ]
    return VDS_POOL_CUSTOM_ATTRIBUTES
def _define_VDS_PORT_NOTIFICATION_head():
    class VDS_PORT_NOTIFICATION(Structure):
        pass
    return VDS_PORT_NOTIFICATION
def _define_VDS_PORT_NOTIFICATION():
    VDS_PORT_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_PORT_NOTIFICATION_head
    VDS_PORT_NOTIFICATION._fields_ = [
        ('ulEvent', win32more.Storage.VirtualDiskService.VDS_NF_PORT),
        ('portId', Guid),
    ]
    return VDS_PORT_NOTIFICATION
def _define_VDS_PORT_PROP_head():
    class VDS_PORT_PROP(Structure):
        pass
    return VDS_PORT_PROP
def _define_VDS_PORT_PROP():
    VDS_PORT_PROP = win32more.Storage.VirtualDiskService.VDS_PORT_PROP_head
    VDS_PORT_PROP._fields_ = [
        ('id', Guid),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('status', win32more.Storage.VirtualDiskService.VDS_PORT_STATUS),
    ]
    return VDS_PORT_PROP
VDS_PORT_STATUS = Int32
VDS_PRS_UNKNOWN = 0
VDS_PRS_ONLINE = 1
VDS_PRS_NOT_READY = 2
VDS_PRS_OFFLINE = 4
VDS_PRS_FAILED = 5
VDS_PRS_REMOVED = 8
def _define_VDS_PORTAL_GROUP_NOTIFICATION_head():
    class VDS_PORTAL_GROUP_NOTIFICATION(Structure):
        pass
    return VDS_PORTAL_GROUP_NOTIFICATION
def _define_VDS_PORTAL_GROUP_NOTIFICATION():
    VDS_PORTAL_GROUP_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_PORTAL_GROUP_NOTIFICATION_head
    VDS_PORTAL_GROUP_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('portalGroupId', Guid),
    ]
    return VDS_PORTAL_GROUP_NOTIFICATION
def _define_VDS_PORTAL_NOTIFICATION_head():
    class VDS_PORTAL_NOTIFICATION(Structure):
        pass
    return VDS_PORTAL_NOTIFICATION
def _define_VDS_PORTAL_NOTIFICATION():
    VDS_PORTAL_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_PORTAL_NOTIFICATION_head
    VDS_PORTAL_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('portalId', Guid),
    ]
    return VDS_PORTAL_NOTIFICATION
VDS_PROVIDER_FLAG = Int32
VDS_PF_DYNAMIC = 1
VDS_PF_INTERNAL_HARDWARE_PROVIDER = 2
VDS_PF_ONE_DISK_ONLY_PER_PACK = 4
VDS_PF_ONE_PACK_ONLINE_ONLY = 8
VDS_PF_VOLUME_SPACE_MUST_BE_CONTIGUOUS = 16
VDS_PF_SUPPORT_DYNAMIC = -2147483648
VDS_PF_SUPPORT_FAULT_TOLERANT = 1073741824
VDS_PF_SUPPORT_DYNAMIC_1394 = 536870912
VDS_PF_SUPPORT_MIRROR = 32
VDS_PF_SUPPORT_RAID5 = 64
VDS_PROVIDER_LBSUPPORT_FLAG = Int32
VDS_LBF_FAILOVER = 1
VDS_LBF_ROUND_ROBIN = 2
VDS_LBF_ROUND_ROBIN_WITH_SUBSET = 4
VDS_LBF_DYN_LEAST_QUEUE_DEPTH = 8
VDS_LBF_WEIGHTED_PATHS = 16
VDS_LBF_LEAST_BLOCKS = 32
VDS_LBF_VENDOR_SPECIFIC = 64
def _define_VDS_PROVIDER_PROP_head():
    class VDS_PROVIDER_PROP(Structure):
        pass
    return VDS_PROVIDER_PROP
def _define_VDS_PROVIDER_PROP():
    VDS_PROVIDER_PROP = win32more.Storage.VirtualDiskService.VDS_PROVIDER_PROP_head
    VDS_PROVIDER_PROP._fields_ = [
        ('id', Guid),
        ('pwszName', win32more.Foundation.PWSTR),
        ('guidVersionId', Guid),
        ('pwszVersion', win32more.Foundation.PWSTR),
        ('type', win32more.Storage.VirtualDiskService.VDS_PROVIDER_TYPE),
        ('ulFlags', UInt32),
        ('ulStripeSizeFlags', UInt32),
        ('sRebuildPriority', Int16),
    ]
    return VDS_PROVIDER_PROP
VDS_PROVIDER_TYPE = Int32
VDS_PT_UNKNOWN = 0
VDS_PT_SOFTWARE = 1
VDS_PT_HARDWARE = 2
VDS_PT_VIRTUALDISK = 3
VDS_PT_MAX = 4
VDS_RAID_TYPE = Int32
VDS_RT_UNKNOWN = 0
VDS_RT_RAID0 = 10
VDS_RT_RAID1 = 11
VDS_RT_RAID2 = 12
VDS_RT_RAID3 = 13
VDS_RT_RAID4 = 14
VDS_RT_RAID5 = 15
VDS_RT_RAID6 = 16
VDS_RT_RAID01 = 17
VDS_RT_RAID03 = 18
VDS_RT_RAID05 = 19
VDS_RT_RAID10 = 20
VDS_RT_RAID15 = 21
VDS_RT_RAID30 = 22
VDS_RT_RAID50 = 23
VDS_RT_RAID51 = 24
VDS_RT_RAID53 = 25
VDS_RT_RAID60 = 26
VDS_RT_RAID61 = 27
VDS_RECOVER_ACTION = Int32
VDS_RA_UNKNOWN = 0
VDS_RA_REFRESH = 1
VDS_RA_RESTART = 2
def _define_VDS_SERVICE_NOTIFICATION_head():
    class VDS_SERVICE_NOTIFICATION(Structure):
        pass
    return VDS_SERVICE_NOTIFICATION
def _define_VDS_SERVICE_NOTIFICATION():
    VDS_SERVICE_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_SERVICE_NOTIFICATION_head
    VDS_SERVICE_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('action', win32more.Storage.VirtualDiskService.VDS_RECOVER_ACTION),
    ]
    return VDS_SERVICE_NOTIFICATION
VDS_STORAGE_BUS_TYPE = Int32
VDS_STORAGE_BUS_TYPE_VDSBusTypeUnknown = 0
VDS_STORAGE_BUS_TYPE_VDSBusTypeScsi = 1
VDS_STORAGE_BUS_TYPE_VDSBusTypeAtapi = 2
VDS_STORAGE_BUS_TYPE_VDSBusTypeAta = 3
VDS_STORAGE_BUS_TYPE_VDSBusType1394 = 4
VDS_STORAGE_BUS_TYPE_VDSBusTypeSsa = 5
VDS_STORAGE_BUS_TYPE_VDSBusTypeFibre = 6
VDS_STORAGE_BUS_TYPE_VDSBusTypeUsb = 7
VDS_STORAGE_BUS_TYPE_VDSBusTypeRAID = 8
VDS_STORAGE_BUS_TYPE_VDSBusTypeiScsi = 9
VDS_STORAGE_BUS_TYPE_VDSBusTypeSas = 10
VDS_STORAGE_BUS_TYPE_VDSBusTypeSata = 11
VDS_STORAGE_BUS_TYPE_VDSBusTypeSd = 12
VDS_STORAGE_BUS_TYPE_VDSBusTypeMmc = 13
VDS_STORAGE_BUS_TYPE_VDSBusTypeMax = 14
VDS_STORAGE_BUS_TYPE_VDSBusTypeVirtual = 14
VDS_STORAGE_BUS_TYPE_VDSBusTypeFileBackedVirtual = 15
VDS_STORAGE_BUS_TYPE_VDSBusTypeSpaces = 16
VDS_STORAGE_BUS_TYPE_VDSBusTypeNVMe = 17
VDS_STORAGE_BUS_TYPE_VDSBusTypeScm = 18
VDS_STORAGE_BUS_TYPE_VDSBusTypeUfs = 19
VDS_STORAGE_BUS_TYPE_VDSBusTypeMaxReserved = 127
def _define_VDS_STORAGE_DEVICE_ID_DESCRIPTOR_head():
    class VDS_STORAGE_DEVICE_ID_DESCRIPTOR(Structure):
        pass
    return VDS_STORAGE_DEVICE_ID_DESCRIPTOR
def _define_VDS_STORAGE_DEVICE_ID_DESCRIPTOR():
    VDS_STORAGE_DEVICE_ID_DESCRIPTOR = win32more.Storage.VirtualDiskService.VDS_STORAGE_DEVICE_ID_DESCRIPTOR_head
    VDS_STORAGE_DEVICE_ID_DESCRIPTOR._fields_ = [
        ('m_version', UInt32),
        ('m_cIdentifiers', UInt32),
        ('m_rgIdentifiers', POINTER(win32more.Storage.VirtualDiskService.VDS_STORAGE_IDENTIFIER_head)),
    ]
    return VDS_STORAGE_DEVICE_ID_DESCRIPTOR
def _define_VDS_STORAGE_IDENTIFIER_head():
    class VDS_STORAGE_IDENTIFIER(Structure):
        pass
    return VDS_STORAGE_IDENTIFIER
def _define_VDS_STORAGE_IDENTIFIER():
    VDS_STORAGE_IDENTIFIER = win32more.Storage.VirtualDiskService.VDS_STORAGE_IDENTIFIER_head
    VDS_STORAGE_IDENTIFIER._fields_ = [
        ('m_CodeSet', win32more.Storage.VirtualDiskService.VDS_STORAGE_IDENTIFIER_CODE_SET),
        ('m_Type', win32more.Storage.VirtualDiskService.VDS_STORAGE_IDENTIFIER_TYPE),
        ('m_cbIdentifier', UInt32),
        ('m_rgbIdentifier', c_char_p_no),
    ]
    return VDS_STORAGE_IDENTIFIER
VDS_STORAGE_IDENTIFIER_CODE_SET = Int32
VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetReserved = 0
VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetBinary = 1
VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetAscii = 2
VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetUtf8 = 3
VDS_STORAGE_IDENTIFIER_TYPE = Int32
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeVendorSpecific = 0
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeVendorId = 1
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeEUI64 = 2
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeFCPHName = 3
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypePortRelative = 4
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeTargetPortGroup = 5
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeLogicalUnitGroup = 6
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeMD5LogicalUnitIdentifier = 7
VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeScsiNameString = 8
def _define_VDS_STORAGE_POOL_DRIVE_EXTENT_head():
    class VDS_STORAGE_POOL_DRIVE_EXTENT(Structure):
        pass
    return VDS_STORAGE_POOL_DRIVE_EXTENT
def _define_VDS_STORAGE_POOL_DRIVE_EXTENT():
    VDS_STORAGE_POOL_DRIVE_EXTENT = win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_DRIVE_EXTENT_head
    VDS_STORAGE_POOL_DRIVE_EXTENT._fields_ = [
        ('id', Guid),
        ('ullSize', UInt64),
        ('bUsed', win32more.Foundation.BOOL),
    ]
    return VDS_STORAGE_POOL_DRIVE_EXTENT
def _define_VDS_STORAGE_POOL_PROP_head():
    class VDS_STORAGE_POOL_PROP(Structure):
        pass
    return VDS_STORAGE_POOL_PROP
def _define_VDS_STORAGE_POOL_PROP():
    VDS_STORAGE_POOL_PROP = win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_PROP_head
    VDS_STORAGE_POOL_PROP._fields_ = [
        ('id', Guid),
        ('status', win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('type', win32more.Storage.VirtualDiskService.VDS_STORAGE_POOL_TYPE),
        ('pwszName', win32more.Foundation.PWSTR),
        ('pwszDescription', win32more.Foundation.PWSTR),
        ('ullTotalConsumedSpace', UInt64),
        ('ullTotalManagedSpace', UInt64),
        ('ullRemainingFreeSpace', UInt64),
    ]
    return VDS_STORAGE_POOL_PROP
VDS_STORAGE_POOL_STATUS = Int32
VDS_SPS_UNKNOWN = 0
VDS_SPS_ONLINE = 1
VDS_SPS_NOT_READY = 2
VDS_SPS_OFFLINE = 4
VDS_STORAGE_POOL_TYPE = Int32
VDS_SPT_UNKNOWN = 0
VDS_SPT_PRIMORDIAL = 1
VDS_SPT_CONCRETE = 2
VDS_SUB_SYSTEM_FLAG = Int32
VDS_SF_LUN_MASKING_CAPABLE = 1
VDS_SF_LUN_PLEXING_CAPABLE = 2
VDS_SF_LUN_REMAPPING_CAPABLE = 4
VDS_SF_DRIVE_EXTENT_CAPABLE = 8
VDS_SF_HARDWARE_CHECKSUM_CAPABLE = 16
VDS_SF_RADIUS_CAPABLE = 32
VDS_SF_READ_BACK_VERIFY_CAPABLE = 64
VDS_SF_WRITE_THROUGH_CACHING_CAPABLE = 128
VDS_SF_SUPPORTS_FAULT_TOLERANT_LUNS = 512
VDS_SF_SUPPORTS_NON_FAULT_TOLERANT_LUNS = 1024
VDS_SF_SUPPORTS_SIMPLE_LUNS = 2048
VDS_SF_SUPPORTS_SPAN_LUNS = 4096
VDS_SF_SUPPORTS_STRIPE_LUNS = 8192
VDS_SF_SUPPORTS_MIRROR_LUNS = 16384
VDS_SF_SUPPORTS_PARITY_LUNS = 32768
VDS_SF_SUPPORTS_AUTH_CHAP = 65536
VDS_SF_SUPPORTS_AUTH_MUTUAL_CHAP = 131072
VDS_SF_SUPPORTS_SIMPLE_TARGET_CONFIG = 262144
VDS_SF_SUPPORTS_LUN_NUMBER = 524288
VDS_SF_SUPPORTS_MIRRORED_CACHE = 1048576
VDS_SF_READ_CACHING_CAPABLE = 2097152
VDS_SF_WRITE_CACHING_CAPABLE = 4194304
VDS_SF_MEDIA_SCAN_CAPABLE = 8388608
VDS_SF_CONSISTENCY_CHECK_CAPABLE = 16777216
def _define_VDS_SUB_SYSTEM_NOTIFICATION_head():
    class VDS_SUB_SYSTEM_NOTIFICATION(Structure):
        pass
    return VDS_SUB_SYSTEM_NOTIFICATION
def _define_VDS_SUB_SYSTEM_NOTIFICATION():
    VDS_SUB_SYSTEM_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_NOTIFICATION_head
    VDS_SUB_SYSTEM_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('subSystemId', Guid),
    ]
    return VDS_SUB_SYSTEM_NOTIFICATION
def _define_VDS_SUB_SYSTEM_PROP_head():
    class VDS_SUB_SYSTEM_PROP(Structure):
        pass
    return VDS_SUB_SYSTEM_PROP
def _define_VDS_SUB_SYSTEM_PROP():
    VDS_SUB_SYSTEM_PROP = win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_PROP_head
    VDS_SUB_SYSTEM_PROP._fields_ = [
        ('id', Guid),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('ulFlags', UInt32),
        ('ulStripeSizeFlags', UInt32),
        ('status', win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('sNumberOfInternalBuses', Int16),
        ('sMaxNumberOfSlotsEachBus', Int16),
        ('sMaxNumberOfControllers', Int16),
        ('sRebuildPriority', Int16),
    ]
    return VDS_SUB_SYSTEM_PROP
def _define_VDS_SUB_SYSTEM_PROP2_head():
    class VDS_SUB_SYSTEM_PROP2(Structure):
        pass
    return VDS_SUB_SYSTEM_PROP2
def _define_VDS_SUB_SYSTEM_PROP2():
    VDS_SUB_SYSTEM_PROP2 = win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_PROP2_head
    VDS_SUB_SYSTEM_PROP2._fields_ = [
        ('id', Guid),
        ('pwszFriendlyName', win32more.Foundation.PWSTR),
        ('pwszIdentification', win32more.Foundation.PWSTR),
        ('ulFlags', UInt32),
        ('ulStripeSizeFlags', UInt32),
        ('ulSupportedRaidTypeFlags', UInt32),
        ('status', win32more.Storage.VirtualDiskService.VDS_SUB_SYSTEM_STATUS),
        ('health', win32more.Storage.VirtualDiskService.VDS_HEALTH),
        ('sNumberOfInternalBuses', Int16),
        ('sMaxNumberOfSlotsEachBus', Int16),
        ('sMaxNumberOfControllers', Int16),
        ('sRebuildPriority', Int16),
        ('ulNumberOfEnclosures', UInt32),
    ]
    return VDS_SUB_SYSTEM_PROP2
VDS_SUB_SYSTEM_STATUS = Int32
VDS_SSS_UNKNOWN = 0
VDS_SSS_ONLINE = 1
VDS_SSS_NOT_READY = 2
VDS_SSS_OFFLINE = 4
VDS_SSS_FAILED = 5
VDS_SSS_PARTIALLY_MANAGED = 9
VDS_SUB_SYSTEM_SUPPORTED_RAID_TYPE_FLAG = Int32
VDS_SF_SUPPORTS_RAID2_LUNS = 1
VDS_SF_SUPPORTS_RAID3_LUNS = 2
VDS_SF_SUPPORTS_RAID4_LUNS = 4
VDS_SF_SUPPORTS_RAID5_LUNS = 8
VDS_SF_SUPPORTS_RAID6_LUNS = 16
VDS_SF_SUPPORTS_RAID01_LUNS = 32
VDS_SF_SUPPORTS_RAID03_LUNS = 64
VDS_SF_SUPPORTS_RAID05_LUNS = 128
VDS_SF_SUPPORTS_RAID10_LUNS = 256
VDS_SF_SUPPORTS_RAID15_LUNS = 512
VDS_SF_SUPPORTS_RAID30_LUNS = 1024
VDS_SF_SUPPORTS_RAID50_LUNS = 2048
VDS_SF_SUPPORTS_RAID51_LUNS = 4096
VDS_SF_SUPPORTS_RAID53_LUNS = 8192
VDS_SF_SUPPORTS_RAID60_LUNS = 16384
VDS_SF_SUPPORTS_RAID61_LUNS = 32768
def _define_VDS_TARGET_NOTIFICATION_head():
    class VDS_TARGET_NOTIFICATION(Structure):
        pass
    return VDS_TARGET_NOTIFICATION
def _define_VDS_TARGET_NOTIFICATION():
    VDS_TARGET_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_TARGET_NOTIFICATION_head
    VDS_TARGET_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('targetId', Guid),
    ]
    return VDS_TARGET_NOTIFICATION
VDS_TRANSITION_STATE = Int32
VDS_TS_UNKNOWN = 0
VDS_TS_STABLE = 1
VDS_TS_EXTENDING = 2
VDS_TS_SHRINKING = 3
VDS_TS_RECONFIGING = 4
VDS_TS_RESTRIPING = 5
VDS_VERSION_SUPPORT_FLAG = Int32
VDS_VSF_1_0 = 1
VDS_VSF_1_1 = 2
VDS_VSF_2_0 = 4
VDS_VSF_2_1 = 8
VDS_VSF_3_0 = 16
def _define_VDS_VOLUME_NOTIFICATION_head():
    class VDS_VOLUME_NOTIFICATION(Structure):
        pass
    return VDS_VOLUME_NOTIFICATION
def _define_VDS_VOLUME_NOTIFICATION():
    VDS_VOLUME_NOTIFICATION = win32more.Storage.VirtualDiskService.VDS_VOLUME_NOTIFICATION_head
    VDS_VOLUME_NOTIFICATION._fields_ = [
        ('ulEvent', UInt32),
        ('volumeId', Guid),
        ('plexId', Guid),
        ('ulPercentCompleted', UInt32),
    ]
    return VDS_VOLUME_NOTIFICATION
def _define_VDS_WWN_head():
    class VDS_WWN(Structure):
        pass
    return VDS_WWN
def _define_VDS_WWN():
    VDS_WWN = win32more.Storage.VirtualDiskService.VDS_WWN_head
    VDS_WWN._fields_ = [
        ('rguchWwn', Byte * 8),
    ]
    return VDS_WWN
__all__ = [
    "CLSID_VdsLoader",
    "CLSID_VdsService",
    "GPT_PARTITION_NAME_LENGTH",
    "IEnumVdsObject",
    "IVdsAdmin",
    "IVdsAdviseSink",
    "IVdsAsync",
    "IVdsController",
    "IVdsControllerControllerPort",
    "IVdsControllerPort",
    "IVdsDrive",
    "IVdsDrive2",
    "IVdsHwProvider",
    "IVdsHwProviderPrivate",
    "IVdsHwProviderPrivateMpio",
    "IVdsHwProviderStoragePools",
    "IVdsHwProviderType",
    "IVdsHwProviderType2",
    "IVdsIscsiPortal",
    "IVdsIscsiPortalGroup",
    "IVdsIscsiTarget",
    "IVdsLun",
    "IVdsLun2",
    "IVdsLunControllerPorts",
    "IVdsLunIscsi",
    "IVdsLunMpio",
    "IVdsLunNaming",
    "IVdsLunNumber",
    "IVdsLunPlex",
    "IVdsMaintenance",
    "IVdsProvider",
    "IVdsProviderPrivate",
    "IVdsProviderSupport",
    "IVdsStoragePool",
    "IVdsSubSystem",
    "IVdsSubSystem2",
    "IVdsSubSystemInterconnect",
    "IVdsSubSystemIscsi",
    "IVdsSubSystemNaming",
    "MAX_FS_ALLOWED_CLUSTER_SIZES_SIZE",
    "MAX_FS_FORMAT_SUPPORT_NAME_SIZE",
    "MAX_FS_NAME_SIZE",
    "VDS_ASYNCOUT_ADDLUNPLEX",
    "VDS_ASYNCOUT_ADDPORTAL",
    "VDS_ASYNCOUT_ADDVOLUMEPLEX",
    "VDS_ASYNCOUT_ATTACH_VDISK",
    "VDS_ASYNCOUT_BREAKVOLUMEPLEX",
    "VDS_ASYNCOUT_CLEAN",
    "VDS_ASYNCOUT_COMPACT_VDISK",
    "VDS_ASYNCOUT_CREATELUN",
    "VDS_ASYNCOUT_CREATEPARTITION",
    "VDS_ASYNCOUT_CREATEPORTALGROUP",
    "VDS_ASYNCOUT_CREATETARGET",
    "VDS_ASYNCOUT_CREATEVOLUME",
    "VDS_ASYNCOUT_CREATE_VDISK",
    "VDS_ASYNCOUT_DELETEPORTALGROUP",
    "VDS_ASYNCOUT_DELETETARGET",
    "VDS_ASYNCOUT_EXPAND_VDISK",
    "VDS_ASYNCOUT_EXTENDLUN",
    "VDS_ASYNCOUT_EXTENDVOLUME",
    "VDS_ASYNCOUT_FORMAT",
    "VDS_ASYNCOUT_LOGINTOTARGET",
    "VDS_ASYNCOUT_LOGOUTFROMTARGET",
    "VDS_ASYNCOUT_MERGE_VDISK",
    "VDS_ASYNCOUT_RECOVERLUN",
    "VDS_ASYNCOUT_RECOVERPACK",
    "VDS_ASYNCOUT_REMOVELUNPLEX",
    "VDS_ASYNCOUT_REMOVEPORTAL",
    "VDS_ASYNCOUT_REMOVEVOLUMEPLEX",
    "VDS_ASYNCOUT_REPAIRVOLUMEPLEX",
    "VDS_ASYNCOUT_REPLACEDISK",
    "VDS_ASYNCOUT_SHRINKLUN",
    "VDS_ASYNCOUT_SHRINKVOLUME",
    "VDS_ASYNCOUT_UNKNOWN",
    "VDS_ASYNC_OUTPUT",
    "VDS_ASYNC_OUTPUT_TYPE",
    "VDS_ATTACH_VIRTUAL_DISK_FLAG_USE_FILE_ACL",
    "VDS_CONTROLLER_NOTIFICATION",
    "VDS_CONTROLLER_PROP",
    "VDS_CONTROLLER_STATUS",
    "VDS_CS_FAILED",
    "VDS_CS_NOT_READY",
    "VDS_CS_OFFLINE",
    "VDS_CS_ONLINE",
    "VDS_CS_REMOVED",
    "VDS_CS_UNKNOWN",
    "VDS_DISK_NOTIFICATION",
    "VDS_DRF_ASSIGNED",
    "VDS_DRF_HOTSPARE",
    "VDS_DRF_HOTSPARE_IN_USE",
    "VDS_DRF_HOTSPARE_STANDBY",
    "VDS_DRF_UNASSIGNED",
    "VDS_DRIVE_EXTENT",
    "VDS_DRIVE_FLAG",
    "VDS_DRIVE_LETTER_NOTIFICATION",
    "VDS_DRIVE_NOTIFICATION",
    "VDS_DRIVE_PROP",
    "VDS_DRIVE_PROP2",
    "VDS_DRIVE_STATUS",
    "VDS_DRS_FAILED",
    "VDS_DRS_NOT_READY",
    "VDS_DRS_OFFLINE",
    "VDS_DRS_ONLINE",
    "VDS_DRS_REMOVED",
    "VDS_DRS_UNKNOWN",
    "VDS_E_ACCESS_DENIED",
    "VDS_E_ACTIVE_PARTITION",
    "VDS_E_ADDRESSES_INCOMPLETELY_SET",
    "VDS_E_ALIGN_BEYOND_FIRST_CYLINDER",
    "VDS_E_ALIGN_IS_ZERO",
    "VDS_E_ALIGN_NOT_A_POWER_OF_TWO",
    "VDS_E_ALIGN_NOT_SECTOR_SIZE_MULTIPLE",
    "VDS_E_ALIGN_NOT_ZERO",
    "VDS_E_ALREADY_REGISTERED",
    "VDS_E_ANOTHER_CALL_IN_PROGRESS",
    "VDS_E_ASSOCIATED_LUNS_EXIST",
    "VDS_E_ASSOCIATED_PORTALS_EXIST",
    "VDS_E_ASYNC_OBJECT_FAILURE",
    "VDS_E_BAD_BOOT_DISK",
    "VDS_E_BAD_COOKIE",
    "VDS_E_BAD_LABEL",
    "VDS_E_BAD_PNP_MESSAGE",
    "VDS_E_BAD_PROVIDER_DATA",
    "VDS_E_BAD_REVISION_NUMBER",
    "VDS_E_BLOCK_CLUSTERED",
    "VDS_E_BOOT_DISK",
    "VDS_E_BOOT_PAGEFILE_DRIVE_LETTER",
    "VDS_E_BOOT_PARTITION_NUMBER_CHANGE",
    "VDS_E_CACHE_CORRUPT",
    "VDS_E_CANCEL_TOO_LATE",
    "VDS_E_CANNOT_CLEAR_VOLUME_FLAG",
    "VDS_E_CANNOT_EXTEND",
    "VDS_E_CANNOT_SHRINK",
    "VDS_E_CANT_INVALIDATE_FVE",
    "VDS_E_CANT_QUICK_FORMAT",
    "VDS_E_CLEAN_WITH_BOOTBACKING",
    "VDS_E_CLEAN_WITH_CRITICAL",
    "VDS_E_CLEAN_WITH_DATA",
    "VDS_E_CLEAN_WITH_OEM",
    "VDS_E_CLUSTER_COUNT_BEYOND_32BITS",
    "VDS_E_CLUSTER_SIZE_TOO_BIG",
    "VDS_E_CLUSTER_SIZE_TOO_SMALL",
    "VDS_E_COMPRESSION_NOT_SUPPORTED",
    "VDS_E_CONFIG_LIMIT",
    "VDS_E_CORRUPT_EXTENT_INFO",
    "VDS_E_CORRUPT_NOTIFICATION_INFO",
    "VDS_E_CORRUPT_PARTITION_INFO",
    "VDS_E_CORRUPT_VOLUME_INFO",
    "VDS_E_CRASHDUMP_DISK",
    "VDS_E_CRITICAL_PLEX",
    "VDS_E_DELETE_WITH_BOOTBACKING",
    "VDS_E_DELETE_WITH_CRITICAL",
    "VDS_E_DEVICE_IN_USE",
    "VDS_E_DISK_BEING_CLEANED",
    "VDS_E_DISK_CONFIGURATION_CORRUPTED",
    "VDS_E_DISK_CONFIGURATION_NOT_IN_SYNC",
    "VDS_E_DISK_CONFIGURATION_UPDATE_FAILED",
    "VDS_E_DISK_DYNAMIC",
    "VDS_E_DISK_HAS_BANDS",
    "VDS_E_DISK_IN_USE_BY_VOLUME",
    "VDS_E_DISK_IO_FAILING",
    "VDS_E_DISK_IS_OFFLINE",
    "VDS_E_DISK_IS_READ_ONLY",
    "VDS_E_DISK_LAYOUT_PARTITIONS_TOO_SMALL",
    "VDS_E_DISK_NOT_CONVERTIBLE",
    "VDS_E_DISK_NOT_CONVERTIBLE_SIZE",
    "VDS_E_DISK_NOT_EMPTY",
    "VDS_E_DISK_NOT_FOUND_IN_PACK",
    "VDS_E_DISK_NOT_IMPORTED",
    "VDS_E_DISK_NOT_INITIALIZED",
    "VDS_E_DISK_NOT_LOADED_TO_CACHE",
    "VDS_E_DISK_NOT_MISSING",
    "VDS_E_DISK_NOT_OFFLINE",
    "VDS_E_DISK_NOT_ONLINE",
    "VDS_E_DISK_PNP_REG_CORRUPT",
    "VDS_E_DISK_REMOVEABLE",
    "VDS_E_DISK_REMOVEABLE_NOT_EMPTY",
    "VDS_E_DISTINCT_VOLUME",
    "VDS_E_DMADMIN_CORRUPT_NOTIFICATION",
    "VDS_E_DMADMIN_METHOD_CALL_FAILED",
    "VDS_E_DMADMIN_SERVICE_CONNECTION_FAILED",
    "VDS_E_DRIVER_INTERNAL_ERROR",
    "VDS_E_DRIVER_INVALID_PARAM",
    "VDS_E_DRIVER_NO_PACK_NAME",
    "VDS_E_DRIVER_OBJECT_NOT_FOUND",
    "VDS_E_DRIVE_LETTER_NOT_FREE",
    "VDS_E_DUPLICATE_DISK",
    "VDS_E_DUP_EMPTY_PACK_GUID",
    "VDS_E_DYNAMIC_DISKS_NOT_SUPPORTED",
    "VDS_E_EXTEND_FILE_SYSTEM_FAILED",
    "VDS_E_EXTEND_MULTIPLE_DISKS_NOT_SUPPORTED",
    "VDS_E_EXTEND_TOO_MANY_CLUSTERS",
    "VDS_E_EXTEND_UNKNOWN_FILESYSTEM",
    "VDS_E_EXTENT_EXCEEDS_DISK_FREE_SPACE",
    "VDS_E_EXTENT_SIZE_LESS_THAN_MIN",
    "VDS_E_FAILED_TO_OFFLINE_DISK",
    "VDS_E_FAILED_TO_ONLINE_DISK",
    "VDS_E_FAT32_FORMAT_NOT_SUPPORTED",
    "VDS_E_FAT_FORMAT_NOT_SUPPORTED",
    "VDS_E_FAULT_TOLERANT_DISKS_NOT_SUPPORTED",
    "VDS_E_FLAG_ALREADY_SET",
    "VDS_E_FORMAT_CRITICAL",
    "VDS_E_FORMAT_NOT_SUPPORTED",
    "VDS_E_FORMAT_WITH_BOOTBACKING",
    "VDS_E_FS_NOT_DETERMINED",
    "VDS_E_GET_SAN_POLICY",
    "VDS_E_GPT_ATTRIBUTES_INVALID",
    "VDS_E_HIBERNATION_FILE_DISK",
    "VDS_E_IA64_BOOT_MIRRORED_TO_MBR",
    "VDS_E_IMPORT_SET_INCOMPLETE",
    "VDS_E_INCOMPATIBLE_FILE_SYSTEM",
    "VDS_E_INCOMPATIBLE_MEDIA",
    "VDS_E_INCORRECT_BOOT_VOLUME_EXTENT_INFO",
    "VDS_E_INCORRECT_SYSTEM_VOLUME_EXTENT_INFO",
    "VDS_E_INITIALIZED_FAILED",
    "VDS_E_INITIALIZE_NOT_CALLED",
    "VDS_E_INITIATOR_ADAPTER_NOT_FOUND",
    "VDS_E_INITIATOR_SPECIFIC_NOT_SUPPORTED",
    "VDS_E_INTERNAL_ERROR",
    "VDS_E_INVALID_BLOCK_SIZE",
    "VDS_E_INVALID_DISK",
    "VDS_E_INVALID_DISK_COUNT",
    "VDS_E_INVALID_DRIVE_LETTER",
    "VDS_E_INVALID_DRIVE_LETTER_COUNT",
    "VDS_E_INVALID_ENUMERATOR",
    "VDS_E_INVALID_EXTENT_COUNT",
    "VDS_E_INVALID_FS_FLAG",
    "VDS_E_INVALID_FS_TYPE",
    "VDS_E_INVALID_IP_ADDRESS",
    "VDS_E_INVALID_ISCSI_PATH",
    "VDS_E_INVALID_ISCSI_TARGET_NAME",
    "VDS_E_INVALID_MEMBER_COUNT",
    "VDS_E_INVALID_MEMBER_ORDER",
    "VDS_E_INVALID_OBJECT_TYPE",
    "VDS_E_INVALID_OPERATION",
    "VDS_E_INVALID_PACK",
    "VDS_E_INVALID_PARTITION_LAYOUT",
    "VDS_E_INVALID_PARTITION_STYLE",
    "VDS_E_INVALID_PARTITION_TYPE",
    "VDS_E_INVALID_PATH",
    "VDS_E_INVALID_PLEX_BLOCK_SIZE",
    "VDS_E_INVALID_PLEX_COUNT",
    "VDS_E_INVALID_PLEX_GUID",
    "VDS_E_INVALID_PLEX_ORDER",
    "VDS_E_INVALID_PLEX_TYPE",
    "VDS_E_INVALID_PORT_PATH",
    "VDS_E_INVALID_PROVIDER_CLSID",
    "VDS_E_INVALID_PROVIDER_ID",
    "VDS_E_INVALID_PROVIDER_NAME",
    "VDS_E_INVALID_PROVIDER_TYPE",
    "VDS_E_INVALID_PROVIDER_VERSION_GUID",
    "VDS_E_INVALID_PROVIDER_VERSION_STRING",
    "VDS_E_INVALID_QUERY_PROVIDER_FLAG",
    "VDS_E_INVALID_SECTOR_SIZE",
    "VDS_E_INVALID_SERVICE_FLAG",
    "VDS_E_INVALID_SHRINK_SIZE",
    "VDS_E_INVALID_SPACE",
    "VDS_E_INVALID_STATE",
    "VDS_E_INVALID_STRIPE_SIZE",
    "VDS_E_INVALID_VOLUME_FLAG",
    "VDS_E_INVALID_VOLUME_LENGTH",
    "VDS_E_INVALID_VOLUME_TYPE",
    "VDS_E_IO_ERROR",
    "VDS_E_ISCSI_CHAP_SECRET",
    "VDS_E_ISCSI_GET_IKE_INFO",
    "VDS_E_ISCSI_GROUP_PRESHARE_KEY",
    "VDS_E_ISCSI_INITIATOR_NODE_NAME",
    "VDS_E_ISCSI_LOGIN_FAILED",
    "VDS_E_ISCSI_LOGOUT_FAILED",
    "VDS_E_ISCSI_LOGOUT_INCOMPLETE",
    "VDS_E_ISCSI_SESSION_NOT_FOUND",
    "VDS_E_ISCSI_SET_IKE_INFO",
    "VDS_E_LAST_VALID_DISK",
    "VDS_E_LBN_REMAP_ENABLED_FLAG",
    "VDS_E_LDM_TIMEOUT",
    "VDS_E_LEGACY_VOLUME_FORMAT",
    "VDS_E_LOG_UPDATE",
    "VDS_E_LUN_DISK_FAILED",
    "VDS_E_LUN_DISK_MISSING",
    "VDS_E_LUN_DISK_NOT_READY",
    "VDS_E_LUN_DISK_NO_MEDIA",
    "VDS_E_LUN_DISK_READ_ONLY",
    "VDS_E_LUN_DYNAMIC",
    "VDS_E_LUN_DYNAMIC_OFFLINE",
    "VDS_E_LUN_FAILED",
    "VDS_E_LUN_NOT_READY",
    "VDS_E_LUN_OFFLINE",
    "VDS_E_LUN_SHRINK_GPT_HEADER",
    "VDS_E_LUN_UPDATE_DISK",
    "VDS_E_MAX_USABLE_MBR",
    "VDS_E_MEDIA_WRITE_PROTECTED",
    "VDS_E_MEMBER_IS_HEALTHY",
    "VDS_E_MEMBER_MISSING",
    "VDS_E_MEMBER_REGENERATING",
    "VDS_E_MEMBER_SIZE_INVALID",
    "VDS_E_MIGRATE_OPEN_VOLUME",
    "VDS_E_MIRROR_NOT_SUPPORTED",
    "VDS_E_MISSING_DISK",
    "VDS_E_MULTIPLE_DISCOVERY_DOMAINS",
    "VDS_E_MULTIPLE_PACKS",
    "VDS_E_NAME_NOT_UNIQUE",
    "VDS_E_NON_CONTIGUOUS_DATA_PARTITIONS",
    "VDS_E_NOT_AN_UNALLOCATED_DISK",
    "VDS_E_NOT_ENOUGH_DRIVE",
    "VDS_E_NOT_ENOUGH_SPACE",
    "VDS_E_NOT_SUPPORTED",
    "VDS_E_NO_DISCOVERY_DOMAIN",
    "VDS_E_NO_DISKS_FOUND",
    "VDS_E_NO_DISK_PATHNAME",
    "VDS_E_NO_DRIVELETTER_FLAG",
    "VDS_E_NO_EXTENTS_FOR_PLEX",
    "VDS_E_NO_EXTENTS_FOR_VOLUME",
    "VDS_E_NO_FREE_SPACE",
    "VDS_E_NO_HEALTHY_DISKS",
    "VDS_E_NO_IMPORT_TARGET",
    "VDS_E_NO_MAINTENANCE_MODE",
    "VDS_E_NO_MEDIA",
    "VDS_E_NO_PNP_DISK_ARRIVE",
    "VDS_E_NO_PNP_DISK_REMOVE",
    "VDS_E_NO_PNP_VOLUME_ARRIVE",
    "VDS_E_NO_PNP_VOLUME_REMOVE",
    "VDS_E_NO_POOL",
    "VDS_E_NO_POOL_CREATED",
    "VDS_E_NO_SOFTWARE_PROVIDERS_LOADED",
    "VDS_E_NO_VALID_LOG_COPIES",
    "VDS_E_NO_VOLUME_LAYOUT",
    "VDS_E_NO_VOLUME_PATHNAME",
    "VDS_E_NTFS_FORMAT_NOT_SUPPORTED",
    "VDS_E_OBJECT_DELETED",
    "VDS_E_OBJECT_EXISTS",
    "VDS_E_OBJECT_NOT_FOUND",
    "VDS_E_OBJECT_OUT_OF_SYNC",
    "VDS_E_OBJECT_STATUS_FAILED",
    "VDS_E_OFFLINE_NOT_SUPPORTED",
    "VDS_E_ONE_EXTENT_PER_DISK",
    "VDS_E_ONLINE_PACK_EXISTS",
    "VDS_E_OPERATION_CANCELED",
    "VDS_E_OPERATION_DENIED",
    "VDS_E_OPERATION_PENDING",
    "VDS_E_PACK_NAME_INVALID",
    "VDS_E_PACK_NOT_FOUND",
    "VDS_E_PACK_OFFLINE",
    "VDS_E_PACK_ONLINE",
    "VDS_E_PAGEFILE_DISK",
    "VDS_E_PARTITION_LDM",
    "VDS_E_PARTITION_LIMIT_REACHED",
    "VDS_E_PARTITION_MSR",
    "VDS_E_PARTITION_NON_DATA",
    "VDS_E_PARTITION_NOT_CYLINDER_ALIGNED",
    "VDS_E_PARTITION_NOT_EMPTY",
    "VDS_E_PARTITION_NOT_OEM",
    "VDS_E_PARTITION_OF_UNKNOWN_TYPE",
    "VDS_E_PARTITION_PROTECTED",
    "VDS_E_PARTITION_STYLE_MISMATCH",
    "VDS_E_PATH_NOT_FOUND",
    "VDS_E_PLEX_IS_HEALTHY",
    "VDS_E_PLEX_LAST_ACTIVE",
    "VDS_E_PLEX_MISSING",
    "VDS_E_PLEX_NOT_LOADED_TO_CACHE",
    "VDS_E_PLEX_REGENERATING",
    "VDS_E_PLEX_SIZE_INVALID",
    "VDS_E_PROVIDER_CACHE_CORRUPT",
    "VDS_E_PROVIDER_CACHE_OUTOFSYNC",
    "VDS_E_PROVIDER_EXITING",
    "VDS_E_PROVIDER_FAILURE",
    "VDS_E_PROVIDER_INITIALIZATION_FAILED",
    "VDS_E_PROVIDER_INTERNAL_ERROR",
    "VDS_E_PROVIDER_TYPE_NOT_SUPPORTED",
    "VDS_E_PROVIDER_VOL_DEVICE_NAME_NOT_FOUND",
    "VDS_E_PROVIDER_VOL_OPEN",
    "VDS_E_RAID5_NOT_SUPPORTED",
    "VDS_E_READONLY",
    "VDS_E_REBOOT_REQUIRED",
    "VDS_E_REFS_FORMAT_NOT_SUPPORTED",
    "VDS_E_REPAIR_VOLUMESTATE",
    "VDS_E_REQUIRES_CONTIGUOUS_DISK_SPACE",
    "VDS_E_RETRY",
    "VDS_E_REVERT_ON_CLOSE",
    "VDS_E_REVERT_ON_CLOSE_MISMATCH",
    "VDS_E_REVERT_ON_CLOSE_SET",
    "VDS_E_SECTOR_SIZE_ERROR",
    "VDS_E_SECURITY_INCOMPLETELY_SET",
    "VDS_E_SET_SAN_POLICY",
    "VDS_E_SET_TUNNEL_MODE_OUTER_ADDRESS",
    "VDS_E_SHRINK_DIRTY_VOLUME",
    "VDS_E_SHRINK_EXTEND_UNALIGNED",
    "VDS_E_SHRINK_IN_PROGRESS",
    "VDS_E_SHRINK_LUN_NOT_UNMASKED",
    "VDS_E_SHRINK_OVER_DATA",
    "VDS_E_SHRINK_SIZE_LESS_THAN_MIN",
    "VDS_E_SHRINK_SIZE_TOO_BIG",
    "VDS_E_SHRINK_UNKNOWN_FILESYSTEM",
    "VDS_E_SHRINK_USER_CANCELLED",
    "VDS_E_SOURCE_IS_TARGET_PACK",
    "VDS_E_SUBSYSTEM_ID_IS_NULL",
    "VDS_E_SYSTEM_DISK",
    "VDS_E_TARGET_PACK_NOT_EMPTY",
    "VDS_E_TARGET_PORTAL_NOT_FOUND",
    "VDS_E_TARGET_SPECIFIC_NOT_SUPPORTED",
    "VDS_E_TIMEOUT",
    "VDS_E_UNABLE_TO_FIND_BOOT_DISK",
    "VDS_E_UNABLE_TO_FIND_SYSTEM_DISK",
    "VDS_E_UNEXPECTED_DISK_LAYOUT_CHANGE",
    "VDS_E_UNRECOVERABLE_ERROR",
    "VDS_E_UNRECOVERABLE_PROVIDER_ERROR",
    "VDS_E_VDISK_INVALID_OP_STATE",
    "VDS_E_VDISK_NOT_OPEN",
    "VDS_E_VDISK_PATHNAME_INVALID",
    "VDS_E_VD_ALREADY_ATTACHED",
    "VDS_E_VD_ALREADY_COMPACTING",
    "VDS_E_VD_ALREADY_DETACHED",
    "VDS_E_VD_ALREADY_MERGING",
    "VDS_E_VD_DISK_ALREADY_EXPANDING",
    "VDS_E_VD_DISK_ALREADY_OPEN",
    "VDS_E_VD_DISK_IS_COMPACTING",
    "VDS_E_VD_DISK_IS_EXPANDING",
    "VDS_E_VD_DISK_IS_MERGING",
    "VDS_E_VD_DISK_NOT_OPEN",
    "VDS_E_VD_IS_ATTACHED",
    "VDS_E_VD_IS_BEING_ATTACHED",
    "VDS_E_VD_IS_BEING_DETACHED",
    "VDS_E_VD_NOT_ATTACHED_READONLY",
    "VDS_E_VOLUME_DISK_COUNT_MAX_EXCEEDED",
    "VDS_E_VOLUME_EXTEND_FVE",
    "VDS_E_VOLUME_EXTEND_FVE_CORRUPT",
    "VDS_E_VOLUME_EXTEND_FVE_LOCKED",
    "VDS_E_VOLUME_EXTEND_FVE_RECOVERY",
    "VDS_E_VOLUME_GUID_PATHNAME_NOT_ALLOWED",
    "VDS_E_VOLUME_HAS_PATH",
    "VDS_E_VOLUME_HIDDEN",
    "VDS_E_VOLUME_INCOMPLETE",
    "VDS_E_VOLUME_INVALID_NAME",
    "VDS_E_VOLUME_LENGTH_NOT_SECTOR_SIZE_MULTIPLE",
    "VDS_E_VOLUME_MIRRORED",
    "VDS_E_VOLUME_NOT_A_MIRROR",
    "VDS_E_VOLUME_NOT_FOUND_IN_PACK",
    "VDS_E_VOLUME_NOT_HEALTHY",
    "VDS_E_VOLUME_NOT_MOUNTED",
    "VDS_E_VOLUME_NOT_ONLINE",
    "VDS_E_VOLUME_NOT_RETAINED",
    "VDS_E_VOLUME_ON_DISK",
    "VDS_E_VOLUME_PERMANENTLY_DISMOUNTED",
    "VDS_E_VOLUME_REGENERATING",
    "VDS_E_VOLUME_RETAINED",
    "VDS_E_VOLUME_SHRINK_FVE",
    "VDS_E_VOLUME_SHRINK_FVE_CORRUPT",
    "VDS_E_VOLUME_SHRINK_FVE_LOCKED",
    "VDS_E_VOLUME_SHRINK_FVE_RECOVERY",
    "VDS_E_VOLUME_SIMPLE_SPANNED",
    "VDS_E_VOLUME_SPANS_DISKS",
    "VDS_E_VOLUME_SYNCHRONIZING",
    "VDS_E_VOLUME_TEMPORARILY_DISMOUNTED",
    "VDS_E_VOLUME_TOO_BIG",
    "VDS_E_VOLUME_TOO_SMALL",
    "VDS_FILE_SYSTEM_NOTIFICATION",
    "VDS_FILE_SYSTEM_TYPE",
    "VDS_FST_CDFS",
    "VDS_FST_CSVFS",
    "VDS_FST_EXFAT",
    "VDS_FST_FAT",
    "VDS_FST_FAT32",
    "VDS_FST_NTFS",
    "VDS_FST_RAW",
    "VDS_FST_REFS",
    "VDS_FST_UDF",
    "VDS_FST_UNKNOWN",
    "VDS_HBAPORT_PROP",
    "VDS_HBAPORT_SPEED_FLAG",
    "VDS_HBAPORT_STATUS",
    "VDS_HBAPORT_TYPE",
    "VDS_HEALTH",
    "VDS_HINTS",
    "VDS_HINTS2",
    "VDS_HINT_ALLOCATEHOTSPARE",
    "VDS_HINT_BUSTYPE",
    "VDS_HINT_CONSISTENCYCHECKENABLED",
    "VDS_HINT_FASTCRASHRECOVERYREQUIRED",
    "VDS_HINT_HARDWARECHECKSUMENABLED",
    "VDS_HINT_ISYANKABLE",
    "VDS_HINT_MEDIASCANENABLED",
    "VDS_HINT_MOSTLYREADS",
    "VDS_HINT_OPTIMIZEFORSEQUENTIALREADS",
    "VDS_HINT_OPTIMIZEFORSEQUENTIALWRITES",
    "VDS_HINT_READBACKVERIFYENABLED",
    "VDS_HINT_READCACHINGENABLED",
    "VDS_HINT_REMAPENABLED",
    "VDS_HINT_USEMIRROREDCACHE",
    "VDS_HINT_WRITECACHINGENABLED",
    "VDS_HINT_WRITETHROUGHCACHINGENABLED",
    "VDS_HPS_BYPASSED",
    "VDS_HPS_DIAGNOSTICS",
    "VDS_HPS_ERROR",
    "VDS_HPS_LINKDOWN",
    "VDS_HPS_LOOPBACK",
    "VDS_HPS_OFFLINE",
    "VDS_HPS_ONLINE",
    "VDS_HPS_UNKNOWN",
    "VDS_HPT_EPORT",
    "VDS_HPT_FLPORT",
    "VDS_HPT_FPORT",
    "VDS_HPT_GPORT",
    "VDS_HPT_LPORT",
    "VDS_HPT_NLPORT",
    "VDS_HPT_NOTPRESENT",
    "VDS_HPT_NPORT",
    "VDS_HPT_OTHER",
    "VDS_HPT_PTP",
    "VDS_HPT_UNKNOWN",
    "VDS_HSF_10GBIT",
    "VDS_HSF_1GBIT",
    "VDS_HSF_2GBIT",
    "VDS_HSF_4GBIT",
    "VDS_HSF_NOT_NEGOTIATED",
    "VDS_HSF_UNKNOWN",
    "VDS_HWPROVIDER_TYPE",
    "VDS_HWT_FIBRE_CHANNEL",
    "VDS_HWT_HYBRID",
    "VDS_HWT_ISCSI",
    "VDS_HWT_PCI_RAID",
    "VDS_HWT_SAS",
    "VDS_HWT_UNKNOWN",
    "VDS_H_DEGRADED",
    "VDS_H_FAILED",
    "VDS_H_FAILED_REDUNDANCY",
    "VDS_H_FAILED_REDUNDANCY_FAILING",
    "VDS_H_FAILING",
    "VDS_H_FAILING_REDUNDANCY",
    "VDS_H_HEALTHY",
    "VDS_H_PENDING_FAILURE",
    "VDS_H_REBUILDING",
    "VDS_H_REPLACED",
    "VDS_H_STALE",
    "VDS_H_UNKNOWN",
    "VDS_IAT_CHAP",
    "VDS_IAT_MUTUAL_CHAP",
    "VDS_IAT_NONE",
    "VDS_IA_FCFS",
    "VDS_IA_FCPH",
    "VDS_IA_FCPH3",
    "VDS_IA_MAC",
    "VDS_IA_SCSI",
    "VDS_IA_UNKNOWN",
    "VDS_IIF_AGGRESSIVE_MODE",
    "VDS_IIF_IKE",
    "VDS_IIF_MAIN_MODE",
    "VDS_IIF_PFS_ENABLE",
    "VDS_IIF_TRANSPORT_MODE_PREFERRED",
    "VDS_IIF_TUNNEL_MODE_PREFERRED",
    "VDS_IIF_VALID",
    "VDS_ILF_MULTIPATH_ENABLED",
    "VDS_ILF_REQUIRE_IPSEC",
    "VDS_ILT_BOOT",
    "VDS_ILT_MANUAL",
    "VDS_ILT_PERSISTENT",
    "VDS_INTERCONNECT",
    "VDS_INTERCONNECT_ADDRESS_TYPE",
    "VDS_INTERCONNECT_FLAG",
    "VDS_IPADDRESS",
    "VDS_IPADDRESS_TYPE",
    "VDS_IPS_FAILED",
    "VDS_IPS_NOT_READY",
    "VDS_IPS_OFFLINE",
    "VDS_IPS_ONLINE",
    "VDS_IPS_UNKNOWN",
    "VDS_IPT_EMPTY",
    "VDS_IPT_IPV4",
    "VDS_IPT_IPV6",
    "VDS_IPT_TEXT",
    "VDS_ISCSI_AUTH_TYPE",
    "VDS_ISCSI_INITIATOR_ADAPTER_PROP",
    "VDS_ISCSI_INITIATOR_PORTAL_PROP",
    "VDS_ISCSI_IPSEC_FLAG",
    "VDS_ISCSI_IPSEC_KEY",
    "VDS_ISCSI_LOGIN_FLAG",
    "VDS_ISCSI_LOGIN_TYPE",
    "VDS_ISCSI_PORTALGROUP_PROP",
    "VDS_ISCSI_PORTAL_PROP",
    "VDS_ISCSI_PORTAL_STATUS",
    "VDS_ISCSI_SHARED_SECRET",
    "VDS_ISCSI_TARGET_PROP",
    "VDS_ITF_FIBRE_CHANNEL",
    "VDS_ITF_ISCSI",
    "VDS_ITF_PCI_RAID",
    "VDS_ITF_SAS",
    "VDS_LBF_DYN_LEAST_QUEUE_DEPTH",
    "VDS_LBF_FAILOVER",
    "VDS_LBF_LEAST_BLOCKS",
    "VDS_LBF_ROUND_ROBIN",
    "VDS_LBF_ROUND_ROBIN_WITH_SUBSET",
    "VDS_LBF_VENDOR_SPECIFIC",
    "VDS_LBF_WEIGHTED_PATHS",
    "VDS_LBP_DYN_LEAST_QUEUE_DEPTH",
    "VDS_LBP_FAILOVER",
    "VDS_LBP_LEAST_BLOCKS",
    "VDS_LBP_ROUND_ROBIN",
    "VDS_LBP_ROUND_ROBIN_WITH_SUBSET",
    "VDS_LBP_UNKNOWN",
    "VDS_LBP_VENDOR_SPECIFIC",
    "VDS_LBP_WEIGHTED_PATHS",
    "VDS_LF_CONSISTENCY_CHECK_ENABLED",
    "VDS_LF_HARDWARE_CHECKSUM_ENABLED",
    "VDS_LF_LBN_REMAP_ENABLED",
    "VDS_LF_MEDIA_SCAN_ENABLED",
    "VDS_LF_READ_BACK_VERIFY_ENABLED",
    "VDS_LF_READ_CACHE_ENABLED",
    "VDS_LF_SNAPSHOT",
    "VDS_LF_WRITE_CACHE_ENABLED",
    "VDS_LF_WRITE_THROUGH_CACHING_ENABLED",
    "VDS_LOADBALANCE_POLICY_ENUM",
    "VDS_LPF_LBN_REMAP_ENABLED",
    "VDS_LPS_FAILED",
    "VDS_LPS_NOT_READY",
    "VDS_LPS_OFFLINE",
    "VDS_LPS_ONLINE",
    "VDS_LPS_UNKNOWN",
    "VDS_LPT_PARITY",
    "VDS_LPT_RAID03",
    "VDS_LPT_RAID05",
    "VDS_LPT_RAID10",
    "VDS_LPT_RAID15",
    "VDS_LPT_RAID2",
    "VDS_LPT_RAID3",
    "VDS_LPT_RAID30",
    "VDS_LPT_RAID4",
    "VDS_LPT_RAID5",
    "VDS_LPT_RAID50",
    "VDS_LPT_RAID53",
    "VDS_LPT_RAID6",
    "VDS_LPT_RAID60",
    "VDS_LPT_SIMPLE",
    "VDS_LPT_SPAN",
    "VDS_LPT_STRIPE",
    "VDS_LPT_UNKNOWN",
    "VDS_LS_FAILED",
    "VDS_LS_NOT_READY",
    "VDS_LS_OFFLINE",
    "VDS_LS_ONLINE",
    "VDS_LS_UNKNOWN",
    "VDS_LT_DEFAULT",
    "VDS_LT_FAULT_TOLERANT",
    "VDS_LT_MIRROR",
    "VDS_LT_NON_FAULT_TOLERANT",
    "VDS_LT_PARITY",
    "VDS_LT_RAID01",
    "VDS_LT_RAID03",
    "VDS_LT_RAID05",
    "VDS_LT_RAID10",
    "VDS_LT_RAID15",
    "VDS_LT_RAID2",
    "VDS_LT_RAID3",
    "VDS_LT_RAID30",
    "VDS_LT_RAID4",
    "VDS_LT_RAID5",
    "VDS_LT_RAID50",
    "VDS_LT_RAID51",
    "VDS_LT_RAID53",
    "VDS_LT_RAID6",
    "VDS_LT_RAID60",
    "VDS_LT_RAID61",
    "VDS_LT_SIMPLE",
    "VDS_LT_SPAN",
    "VDS_LT_STRIPE",
    "VDS_LT_UNKNOWN",
    "VDS_LUN_FLAG",
    "VDS_LUN_INFORMATION",
    "VDS_LUN_NOTIFICATION",
    "VDS_LUN_PLEX_FLAG",
    "VDS_LUN_PLEX_PROP",
    "VDS_LUN_PLEX_STATUS",
    "VDS_LUN_PLEX_TYPE",
    "VDS_LUN_PROP",
    "VDS_LUN_STATUS",
    "VDS_LUN_TYPE",
    "VDS_MAINTENANCE_OPERATION",
    "VDS_MAINTENANCE_OPERATION_BeepAlarm",
    "VDS_MAINTENANCE_OPERATION_BlinkLight",
    "VDS_MAINTENANCE_OPERATION_Ping",
    "VDS_MAINTENANCE_OPERATION_SpinDown",
    "VDS_MAINTENANCE_OPERATION_SpinUp",
    "VDS_MOUNT_POINT_NOTIFICATION",
    "VDS_MPS_FAILED",
    "VDS_MPS_ONLINE",
    "VDS_MPS_STANDBY",
    "VDS_MPS_UNKNOWN",
    "VDS_NF_CONTROLLER",
    "VDS_NF_CONTROLLER_ARRIVE",
    "VDS_NF_CONTROLLER_DEPART",
    "VDS_NF_CONTROLLER_MODIFY",
    "VDS_NF_CONTROLLER_REMOVED",
    "VDS_NF_DISK",
    "VDS_NF_DISK_ARRIVE",
    "VDS_NF_DISK_DEPART",
    "VDS_NF_DISK_MODIFY",
    "VDS_NF_DRIVE",
    "VDS_NF_DRIVE_ARRIVE",
    "VDS_NF_DRIVE_DEPART",
    "VDS_NF_DRIVE_LETTER_ASSIGN",
    "VDS_NF_DRIVE_LETTER_FREE",
    "VDS_NF_DRIVE_MODIFY",
    "VDS_NF_DRIVE_REMOVED",
    "VDS_NF_FILE_SYSTEM",
    "VDS_NF_FILE_SYSTEM_FORMAT_PROGRESS",
    "VDS_NF_FILE_SYSTEM_MODIFY",
    "VDS_NF_FILE_SYSTEM_SHRINKING_PROGRESS",
    "VDS_NF_LUN",
    "VDS_NF_LUN_ARRIVE",
    "VDS_NF_LUN_DEPART",
    "VDS_NF_LUN_MODIFY",
    "VDS_NF_MOUNT_POINTS_CHANGE",
    "VDS_NF_PACK",
    "VDS_NF_PACK_ARRIVE",
    "VDS_NF_PACK_DEPART",
    "VDS_NF_PACK_MODIFY",
    "VDS_NF_PARTITION_ARRIVE",
    "VDS_NF_PARTITION_DEPART",
    "VDS_NF_PARTITION_MODIFY",
    "VDS_NF_PORT",
    "VDS_NF_PORTAL_ARRIVE",
    "VDS_NF_PORTAL_DEPART",
    "VDS_NF_PORTAL_GROUP_ARRIVE",
    "VDS_NF_PORTAL_GROUP_DEPART",
    "VDS_NF_PORTAL_GROUP_MODIFY",
    "VDS_NF_PORTAL_MODIFY",
    "VDS_NF_PORT_ARRIVE",
    "VDS_NF_PORT_DEPART",
    "VDS_NF_PORT_MODIFY",
    "VDS_NF_PORT_REMOVED",
    "VDS_NF_SERVICE_OUT_OF_SYNC",
    "VDS_NF_SUB_SYSTEM_ARRIVE",
    "VDS_NF_SUB_SYSTEM_DEPART",
    "VDS_NF_SUB_SYSTEM_MODIFY",
    "VDS_NF_TARGET_ARRIVE",
    "VDS_NF_TARGET_DEPART",
    "VDS_NF_TARGET_MODIFY",
    "VDS_NF_VOLUME_ARRIVE",
    "VDS_NF_VOLUME_DEPART",
    "VDS_NF_VOLUME_MODIFY",
    "VDS_NF_VOLUME_REBUILDING_PROGRESS",
    "VDS_NOTIFICATION",
    "VDS_NOTIFICATION_TARGET_TYPE",
    "VDS_NTT_CONTROLLER",
    "VDS_NTT_DISK",
    "VDS_NTT_DRIVE",
    "VDS_NTT_DRIVE_LETTER",
    "VDS_NTT_FILE_SYSTEM",
    "VDS_NTT_LUN",
    "VDS_NTT_MOUNT_POINT",
    "VDS_NTT_PACK",
    "VDS_NTT_PARTITION",
    "VDS_NTT_PORT",
    "VDS_NTT_PORTAL",
    "VDS_NTT_PORTAL_GROUP",
    "VDS_NTT_SERVICE",
    "VDS_NTT_SUB_SYSTEM",
    "VDS_NTT_TARGET",
    "VDS_NTT_UNKNOWN",
    "VDS_NTT_VOLUME",
    "VDS_OBJECT_TYPE",
    "VDS_OT_ASYNC",
    "VDS_OT_CONTROLLER",
    "VDS_OT_DISK",
    "VDS_OT_DRIVE",
    "VDS_OT_ENUM",
    "VDS_OT_HBAPORT",
    "VDS_OT_INIT_ADAPTER",
    "VDS_OT_INIT_PORTAL",
    "VDS_OT_LUN",
    "VDS_OT_LUN_PLEX",
    "VDS_OT_OPEN_VDISK",
    "VDS_OT_PACK",
    "VDS_OT_PORT",
    "VDS_OT_PORTAL",
    "VDS_OT_PORTAL_GROUP",
    "VDS_OT_PROVIDER",
    "VDS_OT_STORAGE_POOL",
    "VDS_OT_SUB_SYSTEM",
    "VDS_OT_TARGET",
    "VDS_OT_UNKNOWN",
    "VDS_OT_VDISK",
    "VDS_OT_VOLUME",
    "VDS_OT_VOLUME_PLEX",
    "VDS_PACK_NOTIFICATION",
    "VDS_PARTITION_NOTIFICATION",
    "VDS_PATH_ID",
    "VDS_PATH_INFO",
    "VDS_PATH_POLICY",
    "VDS_PATH_STATUS",
    "VDS_PF_DYNAMIC",
    "VDS_PF_INTERNAL_HARDWARE_PROVIDER",
    "VDS_PF_ONE_DISK_ONLY_PER_PACK",
    "VDS_PF_ONE_PACK_ONLINE_ONLY",
    "VDS_PF_SUPPORT_DYNAMIC",
    "VDS_PF_SUPPORT_DYNAMIC_1394",
    "VDS_PF_SUPPORT_FAULT_TOLERANT",
    "VDS_PF_SUPPORT_MIRROR",
    "VDS_PF_SUPPORT_RAID5",
    "VDS_PF_VOLUME_SPACE_MUST_BE_CONTIGUOUS",
    "VDS_POOL_ATTRIBUTES",
    "VDS_POOL_ATTRIB_ACCS_BDW_WT_HINT",
    "VDS_POOL_ATTRIB_ACCS_DIR_HINT",
    "VDS_POOL_ATTRIB_ACCS_LTNCY_HINT",
    "VDS_POOL_ATTRIB_ACCS_RNDM_HINT",
    "VDS_POOL_ATTRIB_ACCS_SIZE_HINT",
    "VDS_POOL_ATTRIB_ALLOW_SPINDOWN",
    "VDS_POOL_ATTRIB_BUSTYPE",
    "VDS_POOL_ATTRIB_CUSTOM_ATTRIB",
    "VDS_POOL_ATTRIB_DATA_AVL_HINT",
    "VDS_POOL_ATTRIB_DATA_RDNCY_DEF",
    "VDS_POOL_ATTRIB_DATA_RDNCY_MAX",
    "VDS_POOL_ATTRIB_DATA_RDNCY_MIN",
    "VDS_POOL_ATTRIB_NO_SINGLE_POF",
    "VDS_POOL_ATTRIB_NUM_CLMNS",
    "VDS_POOL_ATTRIB_NUM_CLMNS_DEF",
    "VDS_POOL_ATTRIB_NUM_CLMNS_MAX",
    "VDS_POOL_ATTRIB_NUM_CLMNS_MIN",
    "VDS_POOL_ATTRIB_PKG_RDNCY_DEF",
    "VDS_POOL_ATTRIB_PKG_RDNCY_MAX",
    "VDS_POOL_ATTRIB_PKG_RDNCY_MIN",
    "VDS_POOL_ATTRIB_RAIDTYPE",
    "VDS_POOL_ATTRIB_STOR_COST_HINT",
    "VDS_POOL_ATTRIB_STOR_EFFCY_HINT",
    "VDS_POOL_ATTRIB_STRIPE_SIZE",
    "VDS_POOL_ATTRIB_STRIPE_SIZE_DEF",
    "VDS_POOL_ATTRIB_STRIPE_SIZE_MAX",
    "VDS_POOL_ATTRIB_STRIPE_SIZE_MIN",
    "VDS_POOL_ATTRIB_THIN_PROVISION",
    "VDS_POOL_CUSTOM_ATTRIBUTES",
    "VDS_PORTAL_GROUP_NOTIFICATION",
    "VDS_PORTAL_NOTIFICATION",
    "VDS_PORT_NOTIFICATION",
    "VDS_PORT_PROP",
    "VDS_PORT_STATUS",
    "VDS_PROVIDER_FLAG",
    "VDS_PROVIDER_LBSUPPORT_FLAG",
    "VDS_PROVIDER_PROP",
    "VDS_PROVIDER_TYPE",
    "VDS_PRS_FAILED",
    "VDS_PRS_NOT_READY",
    "VDS_PRS_OFFLINE",
    "VDS_PRS_ONLINE",
    "VDS_PRS_REMOVED",
    "VDS_PRS_UNKNOWN",
    "VDS_PT_HARDWARE",
    "VDS_PT_MAX",
    "VDS_PT_SOFTWARE",
    "VDS_PT_UNKNOWN",
    "VDS_PT_VIRTUALDISK",
    "VDS_RAID_TYPE",
    "VDS_RA_REFRESH",
    "VDS_RA_RESTART",
    "VDS_RA_UNKNOWN",
    "VDS_REBUILD_PRIORITY_MAX",
    "VDS_REBUILD_PRIORITY_MIN",
    "VDS_RECOVER_ACTION",
    "VDS_RT_RAID0",
    "VDS_RT_RAID01",
    "VDS_RT_RAID03",
    "VDS_RT_RAID05",
    "VDS_RT_RAID1",
    "VDS_RT_RAID10",
    "VDS_RT_RAID15",
    "VDS_RT_RAID2",
    "VDS_RT_RAID3",
    "VDS_RT_RAID30",
    "VDS_RT_RAID4",
    "VDS_RT_RAID5",
    "VDS_RT_RAID50",
    "VDS_RT_RAID51",
    "VDS_RT_RAID53",
    "VDS_RT_RAID6",
    "VDS_RT_RAID60",
    "VDS_RT_RAID61",
    "VDS_RT_UNKNOWN",
    "VDS_SERVICE_NOTIFICATION",
    "VDS_SF_CONSISTENCY_CHECK_CAPABLE",
    "VDS_SF_DRIVE_EXTENT_CAPABLE",
    "VDS_SF_HARDWARE_CHECKSUM_CAPABLE",
    "VDS_SF_LUN_MASKING_CAPABLE",
    "VDS_SF_LUN_PLEXING_CAPABLE",
    "VDS_SF_LUN_REMAPPING_CAPABLE",
    "VDS_SF_MEDIA_SCAN_CAPABLE",
    "VDS_SF_RADIUS_CAPABLE",
    "VDS_SF_READ_BACK_VERIFY_CAPABLE",
    "VDS_SF_READ_CACHING_CAPABLE",
    "VDS_SF_SUPPORTS_AUTH_CHAP",
    "VDS_SF_SUPPORTS_AUTH_MUTUAL_CHAP",
    "VDS_SF_SUPPORTS_FAULT_TOLERANT_LUNS",
    "VDS_SF_SUPPORTS_LUN_NUMBER",
    "VDS_SF_SUPPORTS_MIRRORED_CACHE",
    "VDS_SF_SUPPORTS_MIRROR_LUNS",
    "VDS_SF_SUPPORTS_NON_FAULT_TOLERANT_LUNS",
    "VDS_SF_SUPPORTS_PARITY_LUNS",
    "VDS_SF_SUPPORTS_RAID01_LUNS",
    "VDS_SF_SUPPORTS_RAID03_LUNS",
    "VDS_SF_SUPPORTS_RAID05_LUNS",
    "VDS_SF_SUPPORTS_RAID10_LUNS",
    "VDS_SF_SUPPORTS_RAID15_LUNS",
    "VDS_SF_SUPPORTS_RAID2_LUNS",
    "VDS_SF_SUPPORTS_RAID30_LUNS",
    "VDS_SF_SUPPORTS_RAID3_LUNS",
    "VDS_SF_SUPPORTS_RAID4_LUNS",
    "VDS_SF_SUPPORTS_RAID50_LUNS",
    "VDS_SF_SUPPORTS_RAID51_LUNS",
    "VDS_SF_SUPPORTS_RAID53_LUNS",
    "VDS_SF_SUPPORTS_RAID5_LUNS",
    "VDS_SF_SUPPORTS_RAID60_LUNS",
    "VDS_SF_SUPPORTS_RAID61_LUNS",
    "VDS_SF_SUPPORTS_RAID6_LUNS",
    "VDS_SF_SUPPORTS_SIMPLE_LUNS",
    "VDS_SF_SUPPORTS_SIMPLE_TARGET_CONFIG",
    "VDS_SF_SUPPORTS_SPAN_LUNS",
    "VDS_SF_SUPPORTS_STRIPE_LUNS",
    "VDS_SF_WRITE_CACHING_CAPABLE",
    "VDS_SF_WRITE_THROUGH_CACHING_CAPABLE",
    "VDS_SPS_NOT_READY",
    "VDS_SPS_OFFLINE",
    "VDS_SPS_ONLINE",
    "VDS_SPS_UNKNOWN",
    "VDS_SPT_CONCRETE",
    "VDS_SPT_PRIMORDIAL",
    "VDS_SPT_UNKNOWN",
    "VDS_SSS_FAILED",
    "VDS_SSS_NOT_READY",
    "VDS_SSS_OFFLINE",
    "VDS_SSS_ONLINE",
    "VDS_SSS_PARTIALLY_MANAGED",
    "VDS_SSS_UNKNOWN",
    "VDS_STORAGE_BUS_TYPE",
    "VDS_STORAGE_BUS_TYPE_VDSBusType1394",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeAta",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeAtapi",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeFibre",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeFileBackedVirtual",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeMax",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeMaxReserved",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeMmc",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeNVMe",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeRAID",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeSas",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeSata",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeScm",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeScsi",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeSd",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeSpaces",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeSsa",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeUfs",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeUnknown",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeUsb",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeVirtual",
    "VDS_STORAGE_BUS_TYPE_VDSBusTypeiScsi",
    "VDS_STORAGE_DEVICE_ID_DESCRIPTOR",
    "VDS_STORAGE_IDENTIFIER",
    "VDS_STORAGE_IDENTIFIER_CODE_SET",
    "VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetAscii",
    "VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetBinary",
    "VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetReserved",
    "VDS_STORAGE_IDENTIFIER_CODE_SET_VDSStorageIdCodeSetUtf8",
    "VDS_STORAGE_IDENTIFIER_TYPE",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeEUI64",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeFCPHName",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeLogicalUnitGroup",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeMD5LogicalUnitIdentifier",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypePortRelative",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeScsiNameString",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeTargetPortGroup",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeVendorId",
    "VDS_STORAGE_IDENTIFIER_TYPE_VDSStorageIdTypeVendorSpecific",
    "VDS_STORAGE_POOL_DRIVE_EXTENT",
    "VDS_STORAGE_POOL_PROP",
    "VDS_STORAGE_POOL_STATUS",
    "VDS_STORAGE_POOL_TYPE",
    "VDS_SUB_SYSTEM_FLAG",
    "VDS_SUB_SYSTEM_NOTIFICATION",
    "VDS_SUB_SYSTEM_PROP",
    "VDS_SUB_SYSTEM_PROP2",
    "VDS_SUB_SYSTEM_STATUS",
    "VDS_SUB_SYSTEM_SUPPORTED_RAID_TYPE_FLAG",
    "VDS_S_ACCESS_PATH_NOT_DELETED",
    "VDS_S_ALREADY_EXISTS",
    "VDS_S_BOOT_PARTITION_NUMBER_CHANGE",
    "VDS_S_DEFAULT_PLEX_MEMBER_IDS",
    "VDS_S_DISK_DISMOUNT_FAILED",
    "VDS_S_DISK_IS_MISSING",
    "VDS_S_DISK_MOUNT_FAILED",
    "VDS_S_DISK_PARTIALLY_CLEANED",
    "VDS_S_DISMOUNT_FAILED",
    "VDS_S_EXTEND_FILE_SYSTEM_FAILED",
    "VDS_S_FS_LOCK",
    "VDS_S_GPT_BOOT_MIRRORED_TO_MBR",
    "VDS_S_IA64_BOOT_MIRRORED_TO_MBR",
    "VDS_S_IN_PROGRESS",
    "VDS_S_ISCSI_LOGIN_ALREAD_EXISTS",
    "VDS_S_ISCSI_PERSISTENT_LOGIN_MAY_NOT_BE_REMOVED",
    "VDS_S_ISCSI_SESSION_NOT_FOUND_PERSISTENT_LOGIN_REMOVED",
    "VDS_S_MBR_BOOT_MIRRORED_TO_GPT",
    "VDS_S_NAME_TRUNCATED",
    "VDS_S_NONCONFORMANT_PARTITION_INFO",
    "VDS_S_NO_NOTIFICATION",
    "VDS_S_PLEX_NOT_LOADED_TO_CACHE",
    "VDS_S_PROPERTIES_INCOMPLETE",
    "VDS_S_PROVIDER_ERROR_LOADING_CACHE",
    "VDS_S_REMOUNT_FAILED",
    "VDS_S_RESYNC_NOTIFICATION_TASK_FAILED",
    "VDS_S_STATUSES_INCOMPLETELY_SET",
    "VDS_S_SYSTEM_PARTITION",
    "VDS_S_UNABLE_TO_GET_GPT_ATTRIBUTES",
    "VDS_S_UPDATE_BOOTFILE_FAILED",
    "VDS_S_VOLUME_COMPRESS_FAILED",
    "VDS_S_VSS_FLUSH_AND_HOLD_WRITES",
    "VDS_S_VSS_RELEASE_WRITES",
    "VDS_S_WINPE_BOOTENTRY",
    "VDS_TARGET_NOTIFICATION",
    "VDS_TRANSITION_STATE",
    "VDS_TS_EXTENDING",
    "VDS_TS_RECONFIGING",
    "VDS_TS_RESTRIPING",
    "VDS_TS_SHRINKING",
    "VDS_TS_STABLE",
    "VDS_TS_UNKNOWN",
    "VDS_VERSION_SUPPORT_FLAG",
    "VDS_VOLUME_NOTIFICATION",
    "VDS_VSF_1_0",
    "VDS_VSF_1_1",
    "VDS_VSF_2_0",
    "VDS_VSF_2_1",
    "VDS_VSF_3_0",
    "VDS_WWN",
    "VER_VDS_LUN_INFORMATION",
]
