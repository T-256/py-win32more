from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Networking.WinHttp
import win32more.Networking.WinSock
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
WINHTTP_FLAG_ASYNC = 268435456
WINHTTP_FLAG_SECURE_DEFAULTS = 805306368
SECURITY_FLAG_IGNORE_UNKNOWN_CA = 256
SECURITY_FLAG_IGNORE_CERT_DATE_INVALID = 8192
SECURITY_FLAG_IGNORE_CERT_CN_INVALID = 4096
SECURITY_FLAG_IGNORE_CERT_WRONG_USAGE = 512
WINHTTP_AUTOPROXY_AUTO_DETECT = 1
WINHTTP_AUTOPROXY_CONFIG_URL = 2
WINHTTP_AUTOPROXY_HOST_KEEPCASE = 4
WINHTTP_AUTOPROXY_HOST_LOWERCASE = 8
WINHTTP_AUTOPROXY_ALLOW_AUTOCONFIG = 256
WINHTTP_AUTOPROXY_ALLOW_STATIC = 512
WINHTTP_AUTOPROXY_ALLOW_CM = 1024
WINHTTP_AUTOPROXY_RUN_INPROCESS = 65536
WINHTTP_AUTOPROXY_RUN_OUTPROCESS_ONLY = 131072
WINHTTP_AUTOPROXY_NO_DIRECTACCESS = 262144
WINHTTP_AUTOPROXY_NO_CACHE_CLIENT = 524288
WINHTTP_AUTOPROXY_NO_CACHE_SVC = 1048576
WINHTTP_AUTOPROXY_SORT_RESULTS = 4194304
WINHTTP_AUTO_DETECT_TYPE_DHCP = 1
WINHTTP_AUTO_DETECT_TYPE_DNS_A = 2
NETWORKING_KEY_BUFSIZE = 128
WINHTTP_PROXY_TYPE_DIRECT = 1
WINHTTP_PROXY_TYPE_PROXY = 2
WINHTTP_PROXY_TYPE_AUTO_PROXY_URL = 4
WINHTTP_PROXY_TYPE_AUTO_DETECT = 8
WINHTTP_REQUEST_STAT_FLAG_TCP_FAST_OPEN = 1
WINHTTP_REQUEST_STAT_FLAG_TLS_SESSION_RESUMPTION = 2
WINHTTP_REQUEST_STAT_FLAG_TLS_FALSE_START = 4
WINHTTP_REQUEST_STAT_FLAG_PROXY_TLS_SESSION_RESUMPTION = 8
WINHTTP_REQUEST_STAT_FLAG_PROXY_TLS_FALSE_START = 16
WINHTTP_REQUEST_STAT_FLAG_FIRST_REQUEST = 32
WINHTTP_MATCH_CONNECTION_GUID_FLAG_REQUIRE_MARKED_CONNECTION = 1
WINHTTP_MATCH_CONNECTION_GUID_FLAGS_MASK = 1
WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_SOFT_LIMIT = 1
WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_BYPASS_CACHE = 2
WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_USE_DNS_TTL = 4
WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_CONN_USE_TTL = 8
WINHTTP_TIME_FORMAT_BUFSIZE = 62
WINHTTP_OPTION_CALLBACK = 1
WINHTTP_OPTION_RESOLVE_TIMEOUT = 2
WINHTTP_OPTION_CONNECT_TIMEOUT = 3
WINHTTP_OPTION_CONNECT_RETRIES = 4
WINHTTP_OPTION_SEND_TIMEOUT = 5
WINHTTP_OPTION_RECEIVE_TIMEOUT = 6
WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT = 7
WINHTTP_OPTION_HANDLE_TYPE = 9
WINHTTP_OPTION_READ_BUFFER_SIZE = 12
WINHTTP_OPTION_WRITE_BUFFER_SIZE = 13
WINHTTP_OPTION_PARENT_HANDLE = 21
WINHTTP_OPTION_EXTENDED_ERROR = 24
WINHTTP_OPTION_SECURITY_FLAGS = 31
WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT = 32
WINHTTP_OPTION_URL = 34
WINHTTP_OPTION_SECURITY_KEY_BITNESS = 36
WINHTTP_OPTION_PROXY = 38
WINHTTP_OPTION_PROXY_RESULT_ENTRY = 39
WINHTTP_OPTION_USER_AGENT = 41
WINHTTP_OPTION_CONTEXT_VALUE = 45
WINHTTP_OPTION_CLIENT_CERT_CONTEXT = 47
WINHTTP_OPTION_REQUEST_PRIORITY = 58
WINHTTP_OPTION_HTTP_VERSION = 59
WINHTTP_OPTION_DISABLE_FEATURE = 63
WINHTTP_OPTION_CODEPAGE = 68
WINHTTP_OPTION_MAX_CONNS_PER_SERVER = 73
WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER = 74
WINHTTP_OPTION_AUTOLOGON_POLICY = 77
WINHTTP_OPTION_SERVER_CERT_CONTEXT = 78
WINHTTP_OPTION_ENABLE_FEATURE = 79
WINHTTP_OPTION_WORKER_THREAD_COUNT = 80
WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT = 81
WINHTTP_OPTION_PASSPORT_COBRANDING_URL = 82
WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH = 83
WINHTTP_OPTION_SECURE_PROTOCOLS = 84
WINHTTP_OPTION_ENABLETRACING = 85
WINHTTP_OPTION_PASSPORT_SIGN_OUT = 86
WINHTTP_OPTION_PASSPORT_RETURN_URL = 87
WINHTTP_OPTION_REDIRECT_POLICY = 88
WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS = 89
WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE = 90
WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE = 91
WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE = 92
WINHTTP_OPTION_CONNECTION_INFO = 93
WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST = 94
WINHTTP_OPTION_SPN = 96
WINHTTP_OPTION_GLOBAL_PROXY_CREDS = 97
WINHTTP_OPTION_GLOBAL_SERVER_CREDS = 98
WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT = 99
WINHTTP_OPTION_REJECT_USERPWD_IN_URL = 100
WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS = 101
WINHTTP_OPTION_RECEIVE_PROXY_CONNECT_RESPONSE = 103
WINHTTP_OPTION_IS_PROXY_CONNECT_RESPONSE = 104
WINHTTP_OPTION_SERVER_SPN_USED = 106
WINHTTP_OPTION_PROXY_SPN_USED = 107
WINHTTP_OPTION_SERVER_CBT = 108
WINHTTP_OPTION_UNSAFE_HEADER_PARSING = 110
WINHTTP_OPTION_ASSURED_NON_BLOCKING_CALLBACKS = 111
WINHTTP_OPTION_UPGRADE_TO_WEB_SOCKET = 114
WINHTTP_OPTION_WEB_SOCKET_CLOSE_TIMEOUT = 115
WINHTTP_OPTION_WEB_SOCKET_KEEPALIVE_INTERVAL = 116
WINHTTP_OPTION_DECOMPRESSION = 118
WINHTTP_OPTION_WEB_SOCKET_RECEIVE_BUFFER_SIZE = 122
WINHTTP_OPTION_WEB_SOCKET_SEND_BUFFER_SIZE = 123
WINHTTP_OPTION_TCP_PRIORITY_HINT = 128
WINHTTP_OPTION_CONNECTION_FILTER = 131
WINHTTP_OPTION_ENABLE_HTTP_PROTOCOL = 133
WINHTTP_OPTION_HTTP_PROTOCOL_USED = 134
WINHTTP_OPTION_KDC_PROXY_SETTINGS = 136
WINHTTP_OPTION_PROXY_DISABLE_SERVICE_CALLS = 137
WINHTTP_OPTION_ENCODE_EXTRA = 138
WINHTTP_OPTION_DISABLE_STREAM_QUEUE = 139
WINHTTP_OPTION_IPV6_FAST_FALLBACK = 140
WINHTTP_OPTION_CONNECTION_STATS_V0 = 141
WINHTTP_OPTION_REQUEST_TIMES = 142
WINHTTP_OPTION_EXPIRE_CONNECTION = 143
WINHTTP_OPTION_DISABLE_SECURE_PROTOCOL_FALLBACK = 144
WINHTTP_OPTION_HTTP_PROTOCOL_REQUIRED = 145
WINHTTP_OPTION_REQUEST_STATS = 146
WINHTTP_OPTION_SERVER_CERT_CHAIN_CONTEXT = 147
WINHTTP_OPTION_CONNECTION_STATS_V1 = 150
WINHTTP_OPTION_SECURITY_INFO = 151
WINHTTP_OPTION_TCP_KEEPALIVE = 152
WINHTTP_OPTION_TCP_FAST_OPEN = 153
WINHTTP_OPTION_TLS_FALSE_START = 154
WINHTTP_OPTION_IGNORE_CERT_REVOCATION_OFFLINE = 155
WINHTTP_OPTION_SOURCE_ADDRESS = 156
WINHTTP_OPTION_HEAP_EXTENSION = 157
WINHTTP_OPTION_TLS_PROTOCOL_INSECURE_FALLBACK = 158
WINHTTP_OPTION_STREAM_ERROR_CODE = 159
WINHTTP_OPTION_REQUIRE_STREAM_END = 160
WINHTTP_OPTION_ENABLE_HTTP2_PLUS_CLIENT_CERT = 161
WINHTTP_OPTION_FAILED_CONNECTION_RETRIES = 162
WINHTTP_OPTION_SET_GLOBAL_CALLBACK = 163
WINHTTP_OPTION_HTTP2_KEEPALIVE = 164
WINHTTP_OPTION_RESOLUTION_HOSTNAME = 165
WINHTTP_OPTION_SET_TOKEN_BINDING = 166
WINHTTP_OPTION_TOKEN_BINDING_PUBLIC_KEY = 167
WINHTTP_OPTION_REFERER_TOKEN_BINDING_HOSTNAME = 168
WINHTTP_OPTION_HTTP2_PLUS_TRANSFER_ENCODING = 169
WINHTTP_OPTION_RESOLVER_CACHE_CONFIG = 170
WINHTTP_OPTION_DISABLE_CERT_CHAIN_BUILDING = 171
WINHTTP_OPTION_BACKGROUND_CONNECTIONS = 172
WINHTTP_OPTION_FIRST_AVAILABLE_CONNECTION = 173
WINHTTP_OPTION_ENABLE_TEST_SIGNING = 174
WINHTTP_OPTION_NTSERVICE_FLAG_TEST = 175
WINHTTP_OPTION_DISABLE_PROXY_LINK_LOCAL_NAME_RESOLUTION = 176
WINHTTP_OPTION_TCP_PRIORITY_STATUS = 177
WINHTTP_OPTION_CONNECTION_GUID = 178
WINHTTP_OPTION_MATCH_CONNECTION_GUID = 179
WINHTTP_OPTION_PROXY_CONFIG_INFO = 180
WINHTTP_OPTION_AGGREGATE_PROXY_CONFIG = 181
WINHTTP_OPTION_SELECTED_PROXY_CONFIG_INFO = 182
WINHTTP_OPTION_HTTP2_RECEIVE_WINDOW = 183
WINHTTP_LAST_OPTION = 183
WINHTTP_OPTION_USERNAME = 4096
WINHTTP_OPTION_PASSWORD = 4097
WINHTTP_OPTION_PROXY_USERNAME = 4098
WINHTTP_OPTION_PROXY_PASSWORD = 4099
WINHTTP_CONNS_PER_SERVER_UNLIMITED = 4294967295
WINHTTP_CONNECTION_RETRY_CONDITION_408 = 1
WINHTTP_CONNECTION_RETRY_CONDITION_SSL_HANDSHAKE = 2
WINHTTP_CONNECTION_RETRY_CONDITION_STALE_CONNECTION = 4
WINHTTP_DECOMPRESSION_FLAG_GZIP = 1
WINHTTP_DECOMPRESSION_FLAG_DEFLATE = 2
WINHTTP_PROTOCOL_FLAG_HTTP2 = 1
WINHTTP_PROTOCOL_FLAG_HTTP3 = 2
WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM = 0
WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW = 1
WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH = 2
WINHTTP_AUTOLOGON_SECURITY_LEVEL_DEFAULT = 0
WINHTTP_OPTION_REDIRECT_POLICY_NEVER = 0
WINHTTP_OPTION_REDIRECT_POLICY_DISALLOW_HTTPS_TO_HTTP = 1
WINHTTP_OPTION_REDIRECT_POLICY_ALWAYS = 2
WINHTTP_OPTION_REDIRECT_POLICY_LAST = 2
WINHTTP_OPTION_REDIRECT_POLICY_DEFAULT = 1
WINHTTP_DISABLE_PASSPORT_AUTH = 0
WINHTTP_ENABLE_PASSPORT_AUTH = 268435456
WINHTTP_DISABLE_PASSPORT_KEYRING = 536870912
WINHTTP_ENABLE_PASSPORT_KEYRING = 1073741824
WINHTTP_DISABLE_COOKIES = 1
WINHTTP_DISABLE_REDIRECTS = 2
WINHTTP_DISABLE_AUTHENTICATION = 4
WINHTTP_DISABLE_KEEP_ALIVE = 8
WINHTTP_ENABLE_SSL_REVOCATION = 1
WINHTTP_ENABLE_SSL_REVERT_IMPERSONATION = 2
WINHTTP_DISABLE_SPN_SERVER_PORT = 0
WINHTTP_ENABLE_SPN_SERVER_PORT = 1
WINHTTP_OPTION_SPN_MASK = 1
WINHTTP_HANDLE_TYPE_SESSION = 1
WINHTTP_HANDLE_TYPE_CONNECT = 2
WINHTTP_HANDLE_TYPE_REQUEST = 3
WINHTTP_AUTH_SCHEME_PASSPORT = 4
WINHTTP_AUTH_SCHEME_DIGEST = 8
WINHTTP_AUTH_TARGET_SERVER = 0
WINHTTP_AUTH_TARGET_PROXY = 1
SECURITY_FLAG_SECURE = 1
SECURITY_FLAG_STRENGTH_WEAK = 268435456
SECURITY_FLAG_STRENGTH_MEDIUM = 1073741824
SECURITY_FLAG_STRENGTH_STRONG = 536870912
WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED = 1
WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CERT = 2
WINHTTP_CALLBACK_STATUS_FLAG_CERT_REVOKED = 4
WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA = 8
WINHTTP_CALLBACK_STATUS_FLAG_CERT_CN_INVALID = 16
WINHTTP_CALLBACK_STATUS_FLAG_CERT_DATE_INVALID = 32
WINHTTP_CALLBACK_STATUS_FLAG_CERT_WRONG_USAGE = 64
WINHTTP_CALLBACK_STATUS_FLAG_SECURITY_CHANNEL_ERROR = 2147483648
WINHTTP_FLAG_SECURE_PROTOCOL_SSL2 = 8
WINHTTP_FLAG_SECURE_PROTOCOL_SSL3 = 32
WINHTTP_FLAG_SECURE_PROTOCOL_TLS1 = 128
WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_1 = 512
WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2 = 2048
WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3 = 8192
WINHTTP_CALLBACK_STATUS_RESOLVING_NAME = 1
WINHTTP_CALLBACK_STATUS_NAME_RESOLVED = 2
WINHTTP_CALLBACK_STATUS_CONNECTING_TO_SERVER = 4
WINHTTP_CALLBACK_STATUS_CONNECTED_TO_SERVER = 8
WINHTTP_CALLBACK_STATUS_SENDING_REQUEST = 16
WINHTTP_CALLBACK_STATUS_REQUEST_SENT = 32
WINHTTP_CALLBACK_STATUS_RECEIVING_RESPONSE = 64
WINHTTP_CALLBACK_STATUS_RESPONSE_RECEIVED = 128
WINHTTP_CALLBACK_STATUS_CLOSING_CONNECTION = 256
WINHTTP_CALLBACK_STATUS_CONNECTION_CLOSED = 512
WINHTTP_CALLBACK_STATUS_HANDLE_CREATED = 1024
WINHTTP_CALLBACK_STATUS_HANDLE_CLOSING = 2048
WINHTTP_CALLBACK_STATUS_DETECTING_PROXY = 4096
WINHTTP_CALLBACK_STATUS_REDIRECT = 16384
WINHTTP_CALLBACK_STATUS_INTERMEDIATE_RESPONSE = 32768
WINHTTP_CALLBACK_STATUS_SECURE_FAILURE = 65536
WINHTTP_CALLBACK_STATUS_HEADERS_AVAILABLE = 131072
WINHTTP_CALLBACK_STATUS_DATA_AVAILABLE = 262144
WINHTTP_CALLBACK_STATUS_READ_COMPLETE = 524288
WINHTTP_CALLBACK_STATUS_WRITE_COMPLETE = 1048576
WINHTTP_CALLBACK_STATUS_REQUEST_ERROR = 2097152
WINHTTP_CALLBACK_STATUS_SENDREQUEST_COMPLETE = 4194304
WINHTTP_CALLBACK_STATUS_GETPROXYFORURL_COMPLETE = 16777216
WINHTTP_CALLBACK_STATUS_CLOSE_COMPLETE = 33554432
WINHTTP_CALLBACK_STATUS_SHUTDOWN_COMPLETE = 67108864
WINHTTP_CALLBACK_STATUS_SETTINGS_WRITE_COMPLETE = 268435456
WINHTTP_CALLBACK_STATUS_SETTINGS_READ_COMPLETE = 536870912
API_RECEIVE_RESPONSE = 1
API_QUERY_DATA_AVAILABLE = 2
API_READ_DATA = 3
API_WRITE_DATA = 4
API_SEND_REQUEST = 5
API_GET_PROXY_FOR_URL = 6
WINHTTP_CALLBACK_FLAG_DETECTING_PROXY = 4096
WINHTTP_CALLBACK_FLAG_REDIRECT = 16384
WINHTTP_CALLBACK_FLAG_INTERMEDIATE_RESPONSE = 32768
WINHTTP_CALLBACK_FLAG_SECURE_FAILURE = 65536
WINHTTP_CALLBACK_FLAG_SENDREQUEST_COMPLETE = 4194304
WINHTTP_CALLBACK_FLAG_HEADERS_AVAILABLE = 131072
WINHTTP_CALLBACK_FLAG_DATA_AVAILABLE = 262144
WINHTTP_CALLBACK_FLAG_READ_COMPLETE = 524288
WINHTTP_CALLBACK_FLAG_WRITE_COMPLETE = 1048576
WINHTTP_CALLBACK_FLAG_REQUEST_ERROR = 2097152
WINHTTP_CALLBACK_FLAG_GETPROXYFORURL_COMPLETE = 16777216
WINHTTP_CALLBACK_FLAG_ALL_NOTIFICATIONS = 4294967295
WINHTTP_QUERY_MIME_VERSION = 0
WINHTTP_QUERY_CONTENT_TYPE = 1
WINHTTP_QUERY_CONTENT_TRANSFER_ENCODING = 2
WINHTTP_QUERY_CONTENT_ID = 3
WINHTTP_QUERY_CONTENT_DESCRIPTION = 4
WINHTTP_QUERY_CONTENT_LENGTH = 5
WINHTTP_QUERY_CONTENT_LANGUAGE = 6
WINHTTP_QUERY_ALLOW = 7
WINHTTP_QUERY_PUBLIC = 8
WINHTTP_QUERY_DATE = 9
WINHTTP_QUERY_EXPIRES = 10
WINHTTP_QUERY_LAST_MODIFIED = 11
WINHTTP_QUERY_MESSAGE_ID = 12
WINHTTP_QUERY_URI = 13
WINHTTP_QUERY_DERIVED_FROM = 14
WINHTTP_QUERY_COST = 15
WINHTTP_QUERY_LINK = 16
WINHTTP_QUERY_PRAGMA = 17
WINHTTP_QUERY_VERSION = 18
WINHTTP_QUERY_STATUS_CODE = 19
WINHTTP_QUERY_STATUS_TEXT = 20
WINHTTP_QUERY_RAW_HEADERS = 21
WINHTTP_QUERY_RAW_HEADERS_CRLF = 22
WINHTTP_QUERY_CONNECTION = 23
WINHTTP_QUERY_ACCEPT = 24
WINHTTP_QUERY_ACCEPT_CHARSET = 25
WINHTTP_QUERY_ACCEPT_ENCODING = 26
WINHTTP_QUERY_ACCEPT_LANGUAGE = 27
WINHTTP_QUERY_AUTHORIZATION = 28
WINHTTP_QUERY_CONTENT_ENCODING = 29
WINHTTP_QUERY_FORWARDED = 30
WINHTTP_QUERY_FROM = 31
WINHTTP_QUERY_IF_MODIFIED_SINCE = 32
WINHTTP_QUERY_LOCATION = 33
WINHTTP_QUERY_ORIG_URI = 34
WINHTTP_QUERY_REFERER = 35
WINHTTP_QUERY_RETRY_AFTER = 36
WINHTTP_QUERY_SERVER = 37
WINHTTP_QUERY_TITLE = 38
WINHTTP_QUERY_USER_AGENT = 39
WINHTTP_QUERY_WWW_AUTHENTICATE = 40
WINHTTP_QUERY_PROXY_AUTHENTICATE = 41
WINHTTP_QUERY_ACCEPT_RANGES = 42
WINHTTP_QUERY_SET_COOKIE = 43
WINHTTP_QUERY_COOKIE = 44
WINHTTP_QUERY_REQUEST_METHOD = 45
WINHTTP_QUERY_REFRESH = 46
WINHTTP_QUERY_CONTENT_DISPOSITION = 47
WINHTTP_QUERY_AGE = 48
WINHTTP_QUERY_CACHE_CONTROL = 49
WINHTTP_QUERY_CONTENT_BASE = 50
WINHTTP_QUERY_CONTENT_LOCATION = 51
WINHTTP_QUERY_CONTENT_MD5 = 52
WINHTTP_QUERY_CONTENT_RANGE = 53
WINHTTP_QUERY_ETAG = 54
WINHTTP_QUERY_HOST = 55
WINHTTP_QUERY_IF_MATCH = 56
WINHTTP_QUERY_IF_NONE_MATCH = 57
WINHTTP_QUERY_IF_RANGE = 58
WINHTTP_QUERY_IF_UNMODIFIED_SINCE = 59
WINHTTP_QUERY_MAX_FORWARDS = 60
WINHTTP_QUERY_PROXY_AUTHORIZATION = 61
WINHTTP_QUERY_RANGE = 62
WINHTTP_QUERY_TRANSFER_ENCODING = 63
WINHTTP_QUERY_UPGRADE = 64
WINHTTP_QUERY_VARY = 65
WINHTTP_QUERY_VIA = 66
WINHTTP_QUERY_WARNING = 67
WINHTTP_QUERY_EXPECT = 68
WINHTTP_QUERY_PROXY_CONNECTION = 69
WINHTTP_QUERY_UNLESS_MODIFIED_SINCE = 70
WINHTTP_QUERY_PROXY_SUPPORT = 75
WINHTTP_QUERY_AUTHENTICATION_INFO = 76
WINHTTP_QUERY_PASSPORT_URLS = 77
WINHTTP_QUERY_PASSPORT_CONFIG = 78
WINHTTP_QUERY_MAX = 78
WINHTTP_QUERY_EX_ALL_HEADERS = 21
WINHTTP_QUERY_CUSTOM = 65535
WINHTTP_QUERY_FLAG_REQUEST_HEADERS = 2147483648
WINHTTP_QUERY_FLAG_SYSTEMTIME = 1073741824
WINHTTP_QUERY_FLAG_NUMBER = 536870912
WINHTTP_QUERY_FLAG_NUMBER64 = 134217728
WINHTTP_QUERY_FLAG_TRAILERS = 33554432
WINHTTP_QUERY_FLAG_WIRE_ENCODING = 16777216
HTTP_STATUS_CONTINUE = 100
HTTP_STATUS_SWITCH_PROTOCOLS = 101
HTTP_STATUS_OK = 200
HTTP_STATUS_CREATED = 201
HTTP_STATUS_ACCEPTED = 202
HTTP_STATUS_PARTIAL = 203
HTTP_STATUS_NO_CONTENT = 204
HTTP_STATUS_RESET_CONTENT = 205
HTTP_STATUS_PARTIAL_CONTENT = 206
HTTP_STATUS_WEBDAV_MULTI_STATUS = 207
HTTP_STATUS_AMBIGUOUS = 300
HTTP_STATUS_MOVED = 301
HTTP_STATUS_REDIRECT = 302
HTTP_STATUS_REDIRECT_METHOD = 303
HTTP_STATUS_NOT_MODIFIED = 304
HTTP_STATUS_USE_PROXY = 305
HTTP_STATUS_REDIRECT_KEEP_VERB = 307
HTTP_STATUS_PERMANENT_REDIRECT = 308
HTTP_STATUS_BAD_REQUEST = 400
HTTP_STATUS_DENIED = 401
HTTP_STATUS_PAYMENT_REQ = 402
HTTP_STATUS_FORBIDDEN = 403
HTTP_STATUS_NOT_FOUND = 404
HTTP_STATUS_BAD_METHOD = 405
HTTP_STATUS_NONE_ACCEPTABLE = 406
HTTP_STATUS_PROXY_AUTH_REQ = 407
HTTP_STATUS_REQUEST_TIMEOUT = 408
HTTP_STATUS_CONFLICT = 409
HTTP_STATUS_GONE = 410
HTTP_STATUS_LENGTH_REQUIRED = 411
HTTP_STATUS_PRECOND_FAILED = 412
HTTP_STATUS_REQUEST_TOO_LARGE = 413
HTTP_STATUS_URI_TOO_LONG = 414
HTTP_STATUS_UNSUPPORTED_MEDIA = 415
HTTP_STATUS_RETRY_WITH = 449
HTTP_STATUS_SERVER_ERROR = 500
HTTP_STATUS_NOT_SUPPORTED = 501
HTTP_STATUS_BAD_GATEWAY = 502
HTTP_STATUS_SERVICE_UNAVAIL = 503
HTTP_STATUS_GATEWAY_TIMEOUT = 504
HTTP_STATUS_VERSION_NOT_SUP = 505
HTTP_STATUS_FIRST = 100
HTTP_STATUS_LAST = 505
ICU_NO_ENCODE = 536870912
ICU_NO_META = 134217728
ICU_ENCODE_SPACES_ONLY = 67108864
ICU_BROWSER_MODE = 33554432
ICU_ENCODE_PERCENT = 4096
ICU_ESCAPE_AUTHORITY = 8192
WINHTTP_ADDREQ_INDEX_MASK = 65535
WINHTTP_ADDREQ_FLAGS_MASK = 4294901760
WINHTTP_ADDREQ_FLAG_ADD_IF_NEW = 268435456
WINHTTP_ADDREQ_FLAG_ADD = 536870912
WINHTTP_ADDREQ_FLAG_COALESCE_WITH_COMMA = 1073741824
WINHTTP_ADDREQ_FLAG_COALESCE_WITH_SEMICOLON = 16777216
WINHTTP_ADDREQ_FLAG_COALESCE = 1073741824
WINHTTP_ADDREQ_FLAG_REPLACE = 2147483648
WINHTTP_EXTENDED_HEADER_FLAG_UNICODE = 1
WINHTTP_IGNORE_REQUEST_TOTAL_LENGTH = 0
WINHTTP_ERROR_BASE = 12000
ERROR_WINHTTP_OUT_OF_HANDLES = 12001
ERROR_WINHTTP_TIMEOUT = 12002
ERROR_WINHTTP_INTERNAL_ERROR = 12004
ERROR_WINHTTP_INVALID_URL = 12005
ERROR_WINHTTP_UNRECOGNIZED_SCHEME = 12006
ERROR_WINHTTP_NAME_NOT_RESOLVED = 12007
ERROR_WINHTTP_INVALID_OPTION = 12009
ERROR_WINHTTP_OPTION_NOT_SETTABLE = 12011
ERROR_WINHTTP_SHUTDOWN = 12012
ERROR_WINHTTP_LOGIN_FAILURE = 12015
ERROR_WINHTTP_OPERATION_CANCELLED = 12017
ERROR_WINHTTP_INCORRECT_HANDLE_TYPE = 12018
ERROR_WINHTTP_INCORRECT_HANDLE_STATE = 12019
ERROR_WINHTTP_CANNOT_CONNECT = 12029
ERROR_WINHTTP_CONNECTION_ERROR = 12030
ERROR_WINHTTP_RESEND_REQUEST = 12032
ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED = 12044
ERROR_WINHTTP_CANNOT_CALL_BEFORE_OPEN = 12100
ERROR_WINHTTP_CANNOT_CALL_BEFORE_SEND = 12101
ERROR_WINHTTP_CANNOT_CALL_AFTER_SEND = 12102
ERROR_WINHTTP_CANNOT_CALL_AFTER_OPEN = 12103
ERROR_WINHTTP_HEADER_NOT_FOUND = 12150
ERROR_WINHTTP_INVALID_SERVER_RESPONSE = 12152
ERROR_WINHTTP_INVALID_HEADER = 12153
ERROR_WINHTTP_INVALID_QUERY_REQUEST = 12154
ERROR_WINHTTP_HEADER_ALREADY_EXISTS = 12155
ERROR_WINHTTP_REDIRECT_FAILED = 12156
ERROR_WINHTTP_AUTO_PROXY_SERVICE_ERROR = 12178
ERROR_WINHTTP_BAD_AUTO_PROXY_SCRIPT = 12166
ERROR_WINHTTP_UNABLE_TO_DOWNLOAD_SCRIPT = 12167
ERROR_WINHTTP_UNHANDLED_SCRIPT_TYPE = 12176
ERROR_WINHTTP_SCRIPT_EXECUTION_ERROR = 12177
ERROR_WINHTTP_NOT_INITIALIZED = 12172
ERROR_WINHTTP_SECURE_FAILURE = 12175
ERROR_WINHTTP_SECURE_CERT_DATE_INVALID = 12037
ERROR_WINHTTP_SECURE_CERT_CN_INVALID = 12038
ERROR_WINHTTP_SECURE_INVALID_CA = 12045
ERROR_WINHTTP_SECURE_CERT_REV_FAILED = 12057
ERROR_WINHTTP_SECURE_CHANNEL_ERROR = 12157
ERROR_WINHTTP_SECURE_INVALID_CERT = 12169
ERROR_WINHTTP_SECURE_CERT_REVOKED = 12170
ERROR_WINHTTP_SECURE_CERT_WRONG_USAGE = 12179
ERROR_WINHTTP_AUTODETECTION_FAILED = 12180
ERROR_WINHTTP_HEADER_COUNT_EXCEEDED = 12181
ERROR_WINHTTP_HEADER_SIZE_OVERFLOW = 12182
ERROR_WINHTTP_CHUNKED_ENCODING_HEADER_SIZE_OVERFLOW = 12183
ERROR_WINHTTP_RESPONSE_DRAIN_OVERFLOW = 12184
ERROR_WINHTTP_CLIENT_CERT_NO_PRIVATE_KEY = 12185
ERROR_WINHTTP_CLIENT_CERT_NO_ACCESS_PRIVATE_KEY = 12186
ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED_PROXY = 12187
ERROR_WINHTTP_SECURE_FAILURE_PROXY = 12188
ERROR_WINHTTP_RESERVED_189 = 12189
ERROR_WINHTTP_HTTP_PROTOCOL_MISMATCH = 12190
ERROR_WINHTTP_GLOBAL_CALLBACK_FAILED = 12191
ERROR_WINHTTP_FEATURE_DISABLED = 12192
WINHTTP_ERROR_LAST = 12192
WINHTTP_RESET_STATE = 1
WINHTTP_RESET_SWPAD_CURRENT_NETWORK = 2
WINHTTP_RESET_SWPAD_ALL = 4
WINHTTP_RESET_SCRIPT_CACHE = 8
WINHTTP_RESET_ALL = 65535
WINHTTP_RESET_NOTIFY_NETWORK_CHANGED = 65536
WINHTTP_RESET_OUT_OF_PROC = 131072
WINHTTP_RESET_DISCARD_RESOLVERS = 262144
WINHTTP_WEB_SOCKET_MAX_CLOSE_REASON_LENGTH = 123
WINHTTP_WEB_SOCKET_MIN_KEEPALIVE_VALUE = 15000
def _define_WinHttpSetStatusCallback():
    try:
        return WINFUNCTYPE(win32more.Networking.WinHttp.WINHTTP_STATUS_CALLBACK,c_void_p,win32more.Networking.WinHttp.WINHTTP_STATUS_CALLBACK,UInt32,UIntPtr)(('WinHttpSetStatusCallback', windll['WINHTTP.dll']), ((1, 'hInternet'),(1, 'lpfnInternetCallback'),(1, 'dwNotificationFlags'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpTimeFromSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Foundation.SYSTEMTIME_head),win32more.Foundation.PWSTR)(('WinHttpTimeFromSystemTime', windll['WINHTTP.dll']), ((1, 'pst'),(1, 'pwszTime'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpTimeToSystemTime():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.SYSTEMTIME_head))(('WinHttpTimeToSystemTime', windll['WINHTTP.dll']), ((1, 'pwszTime'),(1, 'pst'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpCrackUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.PWSTR,UInt32,UInt32,POINTER(win32more.Networking.WinHttp.URL_COMPONENTS_head))(('WinHttpCrackUrl', windll['WINHTTP.dll']), ((1, 'pwszUrl'),(1, 'dwUrlLength'),(1, 'dwFlags'),(1, 'lpUrlComponents'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpCreateUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Networking.WinHttp.URL_COMPONENTS_head),win32more.Networking.WinHttp.WIN_HTTP_CREATE_URL_FLAGS,win32more.Foundation.PWSTR,POINTER(UInt32))(('WinHttpCreateUrl', windll['WINHTTP.dll']), ((1, 'lpUrlComponents'),(1, 'dwFlags'),(1, 'pwszUrl'),(1, 'pdwUrlLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpCheckPlatform():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,)(('WinHttpCheckPlatform', windll['WINHTTP.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetDefaultProxyConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_INFO_head))(('WinHttpGetDefaultProxyConfiguration', windll['WINHTTP.dll']), ((1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSetDefaultProxyConfiguration():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_INFO_head))(('WinHttpSetDefaultProxyConfiguration', windll['WINHTTP.dll']), ((1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpOpen():
    try:
        return WINFUNCTYPE(c_void_p,win32more.Foundation.PWSTR,win32more.Networking.WinHttp.WINHTTP_ACCESS_TYPE,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,UInt32)(('WinHttpOpen', windll['WINHTTP.dll']), ((1, 'pszAgentW'),(1, 'dwAccessType'),(1, 'pszProxyW'),(1, 'pszProxyBypassW'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpCloseHandle():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p)(('WinHttpCloseHandle', windll['WINHTTP.dll']), ((1, 'hInternet'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpConnect():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.PWSTR,win32more.Networking.WinHttp.INTERNET_PORT,UInt32)(('WinHttpConnect', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'pswzServerName'),(1, 'nServerPort'),(1, 'dwReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpReadData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p,UInt32,POINTER(UInt32))(('WinHttpReadData', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpBuffer'),(1, 'dwNumberOfBytesToRead'),(1, 'lpdwNumberOfBytesRead'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpReadDataEx():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UInt32,POINTER(UInt32),UInt64,UInt32,c_void_p)(('WinHttpReadDataEx', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpBuffer'),(1, 'dwNumberOfBytesToRead'),(1, 'lpdwNumberOfBytesRead'),(1, 'ullFlags'),(1, 'cbProperty'),(1, 'pvProperty'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWriteData():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p,UInt32,POINTER(UInt32))(('WinHttpWriteData', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpBuffer'),(1, 'dwNumberOfBytesToWrite'),(1, 'lpdwNumberOfBytesWritten'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryDataAvailable():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(UInt32))(('WinHttpQueryDataAvailable', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpdwNumberOfBytesAvailable'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,c_void_p,POINTER(UInt32))(('WinHttpQueryOption', windll['WINHTTP.dll']), ((1, 'hInternet'),(1, 'dwOption'),(1, 'lpBuffer'),(1, 'lpdwBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSetOption():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,c_void_p,UInt32)(('WinHttpSetOption', windll['WINHTTP.dll']), ((1, 'hInternet'),(1, 'dwOption'),(1, 'lpBuffer'),(1, 'dwBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSetTimeouts():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,Int32,Int32,Int32,Int32)(('WinHttpSetTimeouts', windll['WINHTTP.dll']), ((1, 'hInternet'),(1, 'nResolveTimeout'),(1, 'nConnectTimeout'),(1, 'nSendTimeout'),(1, 'nReceiveTimeout'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpOpenRequest():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,POINTER(win32more.Foundation.PWSTR),win32more.Networking.WinHttp.WINHTTP_OPEN_REQUEST_FLAGS)(('WinHttpOpenRequest', windll['WINHTTP.dll']), ((1, 'hConnect'),(1, 'pwszVerb'),(1, 'pwszObjectName'),(1, 'pwszVersion'),(1, 'pwszReferrer'),(1, 'ppwszAcceptTypes'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpAddRequestHeaders():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR,UInt32,UInt32)(('WinHttpAddRequestHeaders', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpszHeaders'),(1, 'dwHeadersLength'),(1, 'dwModifiers'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpAddRequestHeadersEx():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt64,UInt64,UInt32,POINTER(win32more.Networking.WinHttp.WINHTTP_EXTENDED_HEADER_head))(('WinHttpAddRequestHeadersEx', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'dwModifiers'),(1, 'ullFlags'),(1, 'ullExtra'),(1, 'cHeaders'),(1, 'pHeaders'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSendRequest():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR,UInt32,c_void_p,UInt32,UInt32,UIntPtr)(('WinHttpSendRequest', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpszHeaders'),(1, 'dwHeadersLength'),(1, 'lpOptional'),(1, 'dwOptionalLength'),(1, 'dwTotalLength'),(1, 'dwContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSetCredentials():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,UInt32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,c_void_p)(('WinHttpSetCredentials', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'AuthTargets'),(1, 'AuthScheme'),(1, 'pwszUserName'),(1, 'pwszPassword'),(1, 'pAuthParams'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryAuthSchemes():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,POINTER(UInt32),POINTER(UInt32),POINTER(UInt32))(('WinHttpQueryAuthSchemes', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpdwSupportedSchemes'),(1, 'lpdwFirstScheme'),(1, 'pdwAuthTarget'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpReceiveResponse():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,c_void_p)(('WinHttpReceiveResponse', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'lpReserved'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryHeaders():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,UInt32,win32more.Foundation.PWSTR,c_void_p,POINTER(UInt32),POINTER(UInt32))(('WinHttpQueryHeaders', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'dwInfoLevel'),(1, 'pwszName'),(1, 'lpBuffer'),(1, 'lpdwBufferLength'),(1, 'lpdwIndex'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryHeadersEx():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32,UInt64,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WinHttp.WINHTTP_HEADER_NAME_head),c_void_p,POINTER(UInt32),POINTER(POINTER(win32more.Networking.WinHttp.WINHTTP_EXTENDED_HEADER_head)),POINTER(UInt32))(('WinHttpQueryHeadersEx', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'dwInfoLevel'),(1, 'ullFlags'),(1, 'uiCodePage'),(1, 'pdwIndex'),(1, 'pHeaderName'),(1, 'pBuffer'),(1, 'pdwBufferLength'),(1, 'ppHeaders'),(1, 'pdwHeadersCount'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpQueryConnectionGroup():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(Guid),UInt64,POINTER(POINTER(win32more.Networking.WinHttp.WINHTTP_QUERY_CONNECTION_GROUP_RESULT_head)))(('WinHttpQueryConnectionGroup', windll['WINHTTP.dll']), ((1, 'hInternet'),(1, 'pGuidConnection'),(1, 'ullFlags'),(1, 'ppResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpFreeQueryConnectionGroupResult():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WinHttp.WINHTTP_QUERY_CONNECTION_GROUP_RESULT_head))(('WinHttpFreeQueryConnectionGroupResult', windll['WINHTTP.dll']), ((1, 'pResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpDetectAutoProxyConfigUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,UInt32,POINTER(win32more.Foundation.PWSTR))(('WinHttpDetectAutoProxyConfigUrl', windll['WINHTTP.dll']), ((1, 'dwAutoDetectFlags'),(1, 'ppwstrAutoConfigUrl'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxyForUrl():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinHttp.WINHTTP_AUTOPROXY_OPTIONS_head),POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_INFO_head))(('WinHttpGetProxyForUrl', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'lpcwszUrl'),(1, 'pAutoProxyOptions'),(1, 'pProxyInfo'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpCreateProxyResolver():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(c_void_p))(('WinHttpCreateProxyResolver', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'phResolver'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxyForUrlEx():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinHttp.WINHTTP_AUTOPROXY_OPTIONS_head),UIntPtr)(('WinHttpGetProxyForUrlEx', windll['WINHTTP.dll']), ((1, 'hResolver'),(1, 'pcwszUrl'),(1, 'pAutoProxyOptions'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxyForUrlEx2():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.Foundation.PWSTR,POINTER(win32more.Networking.WinHttp.WINHTTP_AUTOPROXY_OPTIONS_head),UInt32,c_char_p_no,UIntPtr)(('WinHttpGetProxyForUrlEx2', windll['WINHTTP.dll']), ((1, 'hResolver'),(1, 'pcwszUrl'),(1, 'pAutoProxyOptions'),(1, 'cbInterfaceSelectionContext'),(1, 'pInterfaceSelectionContext'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxyResult():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_head))(('WinHttpGetProxyResult', windll['WINHTTP.dll']), ((1, 'hResolver'),(1, 'pProxyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxyResultEx():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_EX_head))(('WinHttpGetProxyResultEx', windll['WINHTTP.dll']), ((1, 'hResolver'),(1, 'pProxyResultEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpFreeProxyResult():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_head))(('WinHttpFreeProxyResult', windll['WINHTTP.dll']), ((1, 'pProxyResult'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpFreeProxyResultEx():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_EX_head))(('WinHttpFreeProxyResultEx', windll['WINHTTP.dll']), ((1, 'pProxyResultEx'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpResetAutoProxy():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt32)(('WinHttpResetAutoProxy', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'dwFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetIEProxyConfigForCurrentUser():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,POINTER(win32more.Networking.WinHttp.WINHTTP_CURRENT_USER_IE_PROXY_CONFIG_head))(('WinHttpGetIEProxyConfigForCurrentUser', windll['WINHTTP.dll']), ((1, 'pProxyConfig'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWriteProxySettings():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.Foundation.BOOL,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_SETTINGS_head))(('WinHttpWriteProxySettings', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'fForceUpdate'),(1, 'pWinHttpProxySettings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpReadProxySettings():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,win32more.Foundation.BOOL,POINTER(UInt32),POINTER(win32more.Foundation.BOOL),POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_SETTINGS_head))(('WinHttpReadProxySettings', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'pcwszConnectionName'),(1, 'fFallBackToDefaultSettings'),(1, 'fSetAutoDiscoverForDefaultSettings'),(1, 'pdwSettingsVersion'),(1, 'pfDefaultSettingsAreReturned'),(1, 'pWinHttpProxySettings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpFreeProxySettings():
    try:
        return WINFUNCTYPE(Void,POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_SETTINGS_head))(('WinHttpFreeProxySettings', windll['WINHTTP.dll']), ((1, 'pWinHttpProxySettings'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpGetProxySettingsVersion():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(UInt32))(('WinHttpGetProxySettingsVersion', windll['WINHTTP.dll']), ((1, 'hSession'),(1, 'pdwProxySettingsVersion'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpSetProxySettingsPerUser():
    try:
        return WINFUNCTYPE(UInt32,win32more.Foundation.BOOL)(('WinHttpSetProxySettingsPerUser', windll['WINHTTP.dll']), ((1, 'fProxySettingsPerUser'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketCompleteUpgrade():
    try:
        return WINFUNCTYPE(c_void_p,c_void_p,UIntPtr)(('WinHttpWebSocketCompleteUpgrade', windll['WINHTTP.dll']), ((1, 'hRequest'),(1, 'pContext'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketSend():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_BUFFER_TYPE,c_void_p,UInt32)(('WinHttpWebSocketSend', windll['WINHTTP.dll']), ((1, 'hWebSocket'),(1, 'eBufferType'),(1, 'pvBuffer'),(1, 'dwBufferLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketReceive():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,c_void_p,UInt32,POINTER(UInt32),POINTER(win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_BUFFER_TYPE))(('WinHttpWebSocketReceive', windll['WINHTTP.dll']), ((1, 'hWebSocket'),(1, 'pvBuffer'),(1, 'dwBufferLength'),(1, 'pdwBytesRead'),(1, 'peBufferType'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketShutdown():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt16,c_void_p,UInt32)(('WinHttpWebSocketShutdown', windll['WINHTTP.dll']), ((1, 'hWebSocket'),(1, 'usStatus'),(1, 'pvReason'),(1, 'dwReasonLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketClose():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,UInt16,c_void_p,UInt32)(('WinHttpWebSocketClose', windll['WINHTTP.dll']), ((1, 'hWebSocket'),(1, 'usStatus'),(1, 'pvReason'),(1, 'dwReasonLength'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_WinHttpWebSocketQueryCloseStatus():
    try:
        return WINFUNCTYPE(UInt32,c_void_p,POINTER(UInt16),c_void_p,UInt32,POINTER(UInt32))(('WinHttpWebSocketQueryCloseStatus', windll['WINHTTP.dll']), ((1, 'hWebSocket'),(1, 'pusStatus'),(1, 'pvReason'),(1, 'dwReasonLength'),(1, 'pdwReasonLengthConsumed'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_HTTP_VERSION_INFO_head():
    class HTTP_VERSION_INFO(Structure):
        pass
    return HTTP_VERSION_INFO
def _define_HTTP_VERSION_INFO():
    HTTP_VERSION_INFO = win32more.Networking.WinHttp.HTTP_VERSION_INFO_head
    HTTP_VERSION_INFO._fields_ = [
        ('dwMajorVersion', UInt32),
        ('dwMinorVersion', UInt32),
    ]
    return HTTP_VERSION_INFO
INTERNET_PORT = UInt32
INTERNET_DEFAULT_HTTP_PORT = 80
INTERNET_DEFAULT_HTTPS_PORT = 443
INTERNET_DEFAULT_PORT = 0
def _define_URL_COMPONENTS_head():
    class URL_COMPONENTS(Structure):
        pass
    return URL_COMPONENTS
def _define_URL_COMPONENTS():
    URL_COMPONENTS = win32more.Networking.WinHttp.URL_COMPONENTS_head
    URL_COMPONENTS._fields_ = [
        ('dwStructSize', UInt32),
        ('lpszScheme', win32more.Foundation.PWSTR),
        ('dwSchemeLength', UInt32),
        ('nScheme', win32more.Networking.WinHttp.WINHTTP_INTERNET_SCHEME),
        ('lpszHostName', win32more.Foundation.PWSTR),
        ('dwHostNameLength', UInt32),
        ('nPort', UInt16),
        ('lpszUserName', win32more.Foundation.PWSTR),
        ('dwUserNameLength', UInt32),
        ('lpszPassword', win32more.Foundation.PWSTR),
        ('dwPasswordLength', UInt32),
        ('lpszUrlPath', win32more.Foundation.PWSTR),
        ('dwUrlPathLength', UInt32),
        ('lpszExtraInfo', win32more.Foundation.PWSTR),
        ('dwExtraInfoLength', UInt32),
    ]
    return URL_COMPONENTS
WIN_HTTP_CREATE_URL_FLAGS = UInt32
ICU_ESCAPE = 2147483648
ICU_REJECT_USERPWD = 16384
ICU_DECODE = 268435456
WINHTTP_ACCESS_TYPE = UInt32
WINHTTP_ACCESS_TYPE_NO_PROXY = 1
WINHTTP_ACCESS_TYPE_DEFAULT_PROXY = 0
WINHTTP_ACCESS_TYPE_NAMED_PROXY = 3
WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY = 4
def _define_WINHTTP_ASYNC_RESULT_head():
    class WINHTTP_ASYNC_RESULT(Structure):
        pass
    return WINHTTP_ASYNC_RESULT
def _define_WINHTTP_ASYNC_RESULT():
    WINHTTP_ASYNC_RESULT = win32more.Networking.WinHttp.WINHTTP_ASYNC_RESULT_head
    WINHTTP_ASYNC_RESULT._fields_ = [
        ('dwResult', UIntPtr),
        ('dwError', UInt32),
    ]
    return WINHTTP_ASYNC_RESULT
def _define_WINHTTP_AUTOPROXY_OPTIONS_head():
    class WINHTTP_AUTOPROXY_OPTIONS(Structure):
        pass
    return WINHTTP_AUTOPROXY_OPTIONS
def _define_WINHTTP_AUTOPROXY_OPTIONS():
    WINHTTP_AUTOPROXY_OPTIONS = win32more.Networking.WinHttp.WINHTTP_AUTOPROXY_OPTIONS_head
    WINHTTP_AUTOPROXY_OPTIONS._fields_ = [
        ('dwFlags', UInt32),
        ('dwAutoDetectFlags', UInt32),
        ('lpszAutoConfigUrl', win32more.Foundation.PWSTR),
        ('lpvReserved', c_void_p),
        ('dwReserved', UInt32),
        ('fAutoLogonIfChallenged', win32more.Foundation.BOOL),
    ]
    return WINHTTP_AUTOPROXY_OPTIONS
def _define_WINHTTP_CERTIFICATE_INFO_head():
    class WINHTTP_CERTIFICATE_INFO(Structure):
        pass
    return WINHTTP_CERTIFICATE_INFO
def _define_WINHTTP_CERTIFICATE_INFO():
    WINHTTP_CERTIFICATE_INFO = win32more.Networking.WinHttp.WINHTTP_CERTIFICATE_INFO_head
    WINHTTP_CERTIFICATE_INFO._fields_ = [
        ('ftExpiry', win32more.Foundation.FILETIME),
        ('ftStart', win32more.Foundation.FILETIME),
        ('lpszSubjectInfo', win32more.Foundation.PWSTR),
        ('lpszIssuerInfo', win32more.Foundation.PWSTR),
        ('lpszProtocolName', win32more.Foundation.PWSTR),
        ('lpszSignatureAlgName', win32more.Foundation.PWSTR),
        ('lpszEncryptionAlgName', win32more.Foundation.PWSTR),
        ('dwKeySize', UInt32),
    ]
    return WINHTTP_CERTIFICATE_INFO
def _define_WINHTTP_CONNECTION_GROUP_head():
    class WINHTTP_CONNECTION_GROUP(Structure):
        pass
    return WINHTTP_CONNECTION_GROUP
def _define_WINHTTP_CONNECTION_GROUP():
    WINHTTP_CONNECTION_GROUP = win32more.Networking.WinHttp.WINHTTP_CONNECTION_GROUP_head
    WINHTTP_CONNECTION_GROUP._fields_ = [
        ('cConnections', UInt32),
        ('guidGroup', Guid),
    ]
    return WINHTTP_CONNECTION_GROUP
def _define_WINHTTP_CONNECTION_INFO_head():
    class WINHTTP_CONNECTION_INFO(Structure):
        pass
    return WINHTTP_CONNECTION_INFO
def _define_WINHTTP_CONNECTION_INFO():
    WINHTTP_CONNECTION_INFO = win32more.Networking.WinHttp.WINHTTP_CONNECTION_INFO_head
    WINHTTP_CONNECTION_INFO._fields_ = [
        ('cbSize', UInt32),
        ('LocalAddress', win32more.Networking.WinSock.SOCKADDR_STORAGE),
        ('RemoteAddress', win32more.Networking.WinSock.SOCKADDR_STORAGE),
    ]
    return WINHTTP_CONNECTION_INFO
def _define_WINHTTP_CREDS_head():
    class WINHTTP_CREDS(Structure):
        pass
    return WINHTTP_CREDS
def _define_WINHTTP_CREDS():
    WINHTTP_CREDS = win32more.Networking.WinHttp.WINHTTP_CREDS_head
    WINHTTP_CREDS._fields_ = [
        ('lpszUserName', win32more.Foundation.PSTR),
        ('lpszPassword', win32more.Foundation.PSTR),
        ('lpszRealm', win32more.Foundation.PSTR),
        ('dwAuthScheme', win32more.Networking.WinHttp.WINHTTP_CREDS_AUTHSCHEME),
        ('lpszHostName', win32more.Foundation.PSTR),
        ('dwPort', UInt32),
    ]
    return WINHTTP_CREDS
WINHTTP_CREDS_AUTHSCHEME = UInt32
WINHTTP_AUTH_SCHEME_BASIC = 1
WINHTTP_AUTH_SCHEME_NTLM = 2
WINHTTP_AUTH_SCHEME_NEGOTIATE = 16
def _define_WINHTTP_CREDS_EX_head():
    class WINHTTP_CREDS_EX(Structure):
        pass
    return WINHTTP_CREDS_EX
def _define_WINHTTP_CREDS_EX():
    WINHTTP_CREDS_EX = win32more.Networking.WinHttp.WINHTTP_CREDS_EX_head
    WINHTTP_CREDS_EX._fields_ = [
        ('lpszUserName', win32more.Foundation.PSTR),
        ('lpszPassword', win32more.Foundation.PSTR),
        ('lpszRealm', win32more.Foundation.PSTR),
        ('dwAuthScheme', win32more.Networking.WinHttp.WINHTTP_CREDS_AUTHSCHEME),
        ('lpszHostName', win32more.Foundation.PSTR),
        ('dwPort', UInt32),
        ('lpszUrl', win32more.Foundation.PSTR),
    ]
    return WINHTTP_CREDS_EX
def _define_WINHTTP_CURRENT_USER_IE_PROXY_CONFIG_head():
    class WINHTTP_CURRENT_USER_IE_PROXY_CONFIG(Structure):
        pass
    return WINHTTP_CURRENT_USER_IE_PROXY_CONFIG
def _define_WINHTTP_CURRENT_USER_IE_PROXY_CONFIG():
    WINHTTP_CURRENT_USER_IE_PROXY_CONFIG = win32more.Networking.WinHttp.WINHTTP_CURRENT_USER_IE_PROXY_CONFIG_head
    WINHTTP_CURRENT_USER_IE_PROXY_CONFIG._fields_ = [
        ('fAutoDetect', win32more.Foundation.BOOL),
        ('lpszAutoConfigUrl', win32more.Foundation.PWSTR),
        ('lpszProxy', win32more.Foundation.PWSTR),
        ('lpszProxyBypass', win32more.Foundation.PWSTR),
    ]
    return WINHTTP_CURRENT_USER_IE_PROXY_CONFIG
def _define_WINHTTP_EXTENDED_HEADER_head():
    class WINHTTP_EXTENDED_HEADER(Structure):
        pass
    return WINHTTP_EXTENDED_HEADER
def _define_WINHTTP_EXTENDED_HEADER():
    WINHTTP_EXTENDED_HEADER = win32more.Networking.WinHttp.WINHTTP_EXTENDED_HEADER_head
    class WINHTTP_EXTENDED_HEADER__Anonymous1_e__Union(Union):
        pass
    WINHTTP_EXTENDED_HEADER__Anonymous1_e__Union._fields_ = [
        ('pwszName', win32more.Foundation.PWSTR),
        ('pszName', win32more.Foundation.PSTR),
    ]
    class WINHTTP_EXTENDED_HEADER__Anonymous2_e__Union(Union):
        pass
    WINHTTP_EXTENDED_HEADER__Anonymous2_e__Union._fields_ = [
        ('pwszValue', win32more.Foundation.PWSTR),
        ('pszValue', win32more.Foundation.PSTR),
    ]
    WINHTTP_EXTENDED_HEADER._anonymous_ = [
        'Anonymous1',
        'Anonymous2',
    ]
    WINHTTP_EXTENDED_HEADER._fields_ = [
        ('Anonymous1', WINHTTP_EXTENDED_HEADER__Anonymous1_e__Union),
        ('Anonymous2', WINHTTP_EXTENDED_HEADER__Anonymous2_e__Union),
    ]
    return WINHTTP_EXTENDED_HEADER
def _define_WINHTTP_FAILED_CONNECTION_RETRIES_head():
    class WINHTTP_FAILED_CONNECTION_RETRIES(Structure):
        pass
    return WINHTTP_FAILED_CONNECTION_RETRIES
def _define_WINHTTP_FAILED_CONNECTION_RETRIES():
    WINHTTP_FAILED_CONNECTION_RETRIES = win32more.Networking.WinHttp.WINHTTP_FAILED_CONNECTION_RETRIES_head
    WINHTTP_FAILED_CONNECTION_RETRIES._fields_ = [
        ('dwMaxRetries', UInt32),
        ('dwAllowedRetryConditions', UInt32),
    ]
    return WINHTTP_FAILED_CONNECTION_RETRIES
def _define_WINHTTP_HEADER_NAME_head():
    class WINHTTP_HEADER_NAME(Union):
        pass
    return WINHTTP_HEADER_NAME
def _define_WINHTTP_HEADER_NAME():
    WINHTTP_HEADER_NAME = win32more.Networking.WinHttp.WINHTTP_HEADER_NAME_head
    WINHTTP_HEADER_NAME._fields_ = [
        ('pwszName', win32more.Foundation.PWSTR),
        ('pszName', win32more.Foundation.PSTR),
    ]
    return WINHTTP_HEADER_NAME
def _define_WINHTTP_HOST_CONNECTION_GROUP_head():
    class WINHTTP_HOST_CONNECTION_GROUP(Structure):
        pass
    return WINHTTP_HOST_CONNECTION_GROUP
def _define_WINHTTP_HOST_CONNECTION_GROUP():
    WINHTTP_HOST_CONNECTION_GROUP = win32more.Networking.WinHttp.WINHTTP_HOST_CONNECTION_GROUP_head
    WINHTTP_HOST_CONNECTION_GROUP._fields_ = [
        ('pwszHost', win32more.Foundation.PWSTR),
        ('cConnectionGroups', UInt32),
        ('pConnectionGroups', POINTER(win32more.Networking.WinHttp.WINHTTP_CONNECTION_GROUP_head)),
    ]
    return WINHTTP_HOST_CONNECTION_GROUP
def _define_WINHTTP_HTTP2_RECEIVE_WINDOW_head():
    class WINHTTP_HTTP2_RECEIVE_WINDOW(Structure):
        pass
    return WINHTTP_HTTP2_RECEIVE_WINDOW
def _define_WINHTTP_HTTP2_RECEIVE_WINDOW():
    WINHTTP_HTTP2_RECEIVE_WINDOW = win32more.Networking.WinHttp.WINHTTP_HTTP2_RECEIVE_WINDOW_head
    WINHTTP_HTTP2_RECEIVE_WINDOW._fields_ = [
        ('ulStreamWindow', UInt32),
        ('ulStreamWindowUpdateDelta', UInt32),
    ]
    return WINHTTP_HTTP2_RECEIVE_WINDOW
WINHTTP_INTERNET_SCHEME = UInt32
WINHTTP_INTERNET_SCHEME_HTTP = 1
WINHTTP_INTERNET_SCHEME_HTTPS = 2
WINHTTP_INTERNET_SCHEME_FTP = 3
WINHTTP_INTERNET_SCHEME_SOCKS = 4
def _define_WINHTTP_MATCH_CONNECTION_GUID_head():
    class WINHTTP_MATCH_CONNECTION_GUID(Structure):
        pass
    return WINHTTP_MATCH_CONNECTION_GUID
def _define_WINHTTP_MATCH_CONNECTION_GUID():
    WINHTTP_MATCH_CONNECTION_GUID = win32more.Networking.WinHttp.WINHTTP_MATCH_CONNECTION_GUID_head
    WINHTTP_MATCH_CONNECTION_GUID._fields_ = [
        ('ConnectionGuid', Guid),
        ('ullFlags', UInt64),
    ]
    return WINHTTP_MATCH_CONNECTION_GUID
WINHTTP_OPEN_REQUEST_FLAGS = UInt32
WINHTTP_FLAG_BYPASS_PROXY_CACHE = 256
WINHTTP_FLAG_ESCAPE_DISABLE = 64
WINHTTP_FLAG_ESCAPE_DISABLE_QUERY = 128
WINHTTP_FLAG_ESCAPE_PERCENT = 4
WINHTTP_FLAG_NULL_CODEPAGE = 8
WINHTTP_FLAG_REFRESH = 256
WINHTTP_FLAG_SECURE = 8388608
def _define_WINHTTP_PROXY_INFO_head():
    class WINHTTP_PROXY_INFO(Structure):
        pass
    return WINHTTP_PROXY_INFO
def _define_WINHTTP_PROXY_INFO():
    WINHTTP_PROXY_INFO = win32more.Networking.WinHttp.WINHTTP_PROXY_INFO_head
    WINHTTP_PROXY_INFO._fields_ = [
        ('dwAccessType', win32more.Networking.WinHttp.WINHTTP_ACCESS_TYPE),
        ('lpszProxy', win32more.Foundation.PWSTR),
        ('lpszProxyBypass', win32more.Foundation.PWSTR),
    ]
    return WINHTTP_PROXY_INFO
def _define_WINHTTP_PROXY_NETWORKING_KEY_head():
    class WINHTTP_PROXY_NETWORKING_KEY(Structure):
        pass
    return WINHTTP_PROXY_NETWORKING_KEY
def _define_WINHTTP_PROXY_NETWORKING_KEY():
    WINHTTP_PROXY_NETWORKING_KEY = win32more.Networking.WinHttp.WINHTTP_PROXY_NETWORKING_KEY_head
    WINHTTP_PROXY_NETWORKING_KEY._fields_ = [
        ('pbBuffer', Byte * 128),
    ]
    return WINHTTP_PROXY_NETWORKING_KEY
def _define_WINHTTP_PROXY_RESULT_head():
    class WINHTTP_PROXY_RESULT(Structure):
        pass
    return WINHTTP_PROXY_RESULT
def _define_WINHTTP_PROXY_RESULT():
    WINHTTP_PROXY_RESULT = win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_head
    WINHTTP_PROXY_RESULT._fields_ = [
        ('cEntries', UInt32),
        ('pEntries', POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_ENTRY_head)),
    ]
    return WINHTTP_PROXY_RESULT
def _define_WINHTTP_PROXY_RESULT_ENTRY_head():
    class WINHTTP_PROXY_RESULT_ENTRY(Structure):
        pass
    return WINHTTP_PROXY_RESULT_ENTRY
def _define_WINHTTP_PROXY_RESULT_ENTRY():
    WINHTTP_PROXY_RESULT_ENTRY = win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_ENTRY_head
    WINHTTP_PROXY_RESULT_ENTRY._fields_ = [
        ('fProxy', win32more.Foundation.BOOL),
        ('fBypass', win32more.Foundation.BOOL),
        ('ProxyScheme', win32more.Networking.WinHttp.WINHTTP_INTERNET_SCHEME),
        ('pwszProxy', win32more.Foundation.PWSTR),
        ('ProxyPort', UInt16),
    ]
    return WINHTTP_PROXY_RESULT_ENTRY
def _define_WINHTTP_PROXY_RESULT_EX_head():
    class WINHTTP_PROXY_RESULT_EX(Structure):
        pass
    return WINHTTP_PROXY_RESULT_EX
def _define_WINHTTP_PROXY_RESULT_EX():
    WINHTTP_PROXY_RESULT_EX = win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_EX_head
    WINHTTP_PROXY_RESULT_EX._fields_ = [
        ('cEntries', UInt32),
        ('pEntries', POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_RESULT_ENTRY_head)),
        ('hProxyDetectionHandle', win32more.Foundation.HANDLE),
        ('dwProxyInterfaceAffinity', UInt32),
    ]
    return WINHTTP_PROXY_RESULT_EX
def _define_WINHTTP_PROXY_SETTINGS_head():
    class WINHTTP_PROXY_SETTINGS(Structure):
        pass
    return WINHTTP_PROXY_SETTINGS
def _define_WINHTTP_PROXY_SETTINGS():
    WINHTTP_PROXY_SETTINGS = win32more.Networking.WinHttp.WINHTTP_PROXY_SETTINGS_head
    WINHTTP_PROXY_SETTINGS._fields_ = [
        ('dwStructSize', UInt32),
        ('dwFlags', UInt32),
        ('dwCurrentSettingsVersion', UInt32),
        ('pwszConnectionName', win32more.Foundation.PWSTR),
        ('pwszProxy', win32more.Foundation.PWSTR),
        ('pwszProxyBypass', win32more.Foundation.PWSTR),
        ('pwszAutoconfigUrl', win32more.Foundation.PWSTR),
        ('pwszAutoconfigSecondaryUrl', win32more.Foundation.PWSTR),
        ('dwAutoDiscoveryFlags', UInt32),
        ('pwszLastKnownGoodAutoConfigUrl', win32more.Foundation.PWSTR),
        ('dwAutoconfigReloadDelayMins', UInt32),
        ('ftLastKnownDetectTime', win32more.Foundation.FILETIME),
        ('dwDetectedInterfaceIpCount', UInt32),
        ('pdwDetectedInterfaceIp', POINTER(UInt32)),
        ('cNetworkKeys', UInt32),
        ('pNetworkKeys', POINTER(win32more.Networking.WinHttp.WINHTTP_PROXY_NETWORKING_KEY_head)),
    ]
    return WINHTTP_PROXY_SETTINGS
def _define_WINHTTP_QUERY_CONNECTION_GROUP_RESULT_head():
    class WINHTTP_QUERY_CONNECTION_GROUP_RESULT(Structure):
        pass
    return WINHTTP_QUERY_CONNECTION_GROUP_RESULT
def _define_WINHTTP_QUERY_CONNECTION_GROUP_RESULT():
    WINHTTP_QUERY_CONNECTION_GROUP_RESULT = win32more.Networking.WinHttp.WINHTTP_QUERY_CONNECTION_GROUP_RESULT_head
    WINHTTP_QUERY_CONNECTION_GROUP_RESULT._fields_ = [
        ('cHosts', UInt32),
        ('pHostConnectionGroups', POINTER(win32more.Networking.WinHttp.WINHTTP_HOST_CONNECTION_GROUP_head)),
    ]
    return WINHTTP_QUERY_CONNECTION_GROUP_RESULT
WINHTTP_REQUEST_STAT_ENTRY = Int32
WINHTTP_REQUEST_STAT_ENTRY_WinHttpConnectFailureCount = 0
WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyFailureCount = 1
WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeClientLeg1Size = 2
WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeServerLeg1Size = 3
WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeClientLeg2Size = 4
WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeServerLeg2Size = 5
WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestHeadersSize = 6
WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestHeadersCompressedSize = 7
WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseHeadersSize = 8
WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseHeadersCompressedSize = 9
WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseBodySize = 10
WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseBodyCompressedSize = 11
WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeClientLeg1Size = 12
WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeServerLeg1Size = 13
WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeClientLeg2Size = 14
WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeServerLeg2Size = 15
WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestStatLast = 16
WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestStatMax = 32
def _define_WINHTTP_REQUEST_STATS_head():
    class WINHTTP_REQUEST_STATS(Structure):
        pass
    return WINHTTP_REQUEST_STATS
def _define_WINHTTP_REQUEST_STATS():
    WINHTTP_REQUEST_STATS = win32more.Networking.WinHttp.WINHTTP_REQUEST_STATS_head
    WINHTTP_REQUEST_STATS._fields_ = [
        ('ullFlags', UInt64),
        ('ulIndex', UInt32),
        ('cStats', UInt32),
        ('rgullStats', UInt64 * 32),
    ]
    return WINHTTP_REQUEST_STATS
WINHTTP_REQUEST_TIME_ENTRY = Int32
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyDetectionStart = 0
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyDetectionEnd = 1
WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireStart = 2
WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireWaitEnd = 3
WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireEnd = 4
WINHTTP_REQUEST_TIME_ENTRY_WinHttpNameResolutionStart = 5
WINHTTP_REQUEST_TIME_ENTRY_WinHttpNameResolutionEnd = 6
WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionEstablishmentStart = 7
WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionEstablishmentEnd = 8
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg1Start = 9
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg1End = 10
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg2Start = 11
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg2End = 12
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg3Start = 13
WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg3End = 14
WINHTTP_REQUEST_TIME_ENTRY_WinHttpStreamWaitStart = 15
WINHTTP_REQUEST_TIME_ENTRY_WinHttpStreamWaitEnd = 16
WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestStart = 17
WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersCompressionStart = 18
WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersCompressionEnd = 19
WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersEnd = 20
WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestEnd = 21
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseStart = 22
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersDecompressionStart = 23
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersDecompressionEnd = 24
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersEnd = 25
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseBodyDecompressionDelta = 26
WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseEnd = 27
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTunnelStart = 28
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTunnelEnd = 29
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg1Start = 30
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg1End = 31
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg2Start = 32
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg2End = 33
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg3Start = 34
WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg3End = 35
WINHTTP_REQUEST_TIME_ENTRY_WinHttpRequestTimeLast = 36
WINHTTP_REQUEST_TIME_ENTRY_WinHttpRequestTimeMax = 64
def _define_WINHTTP_REQUEST_TIMES_head():
    class WINHTTP_REQUEST_TIMES(Structure):
        pass
    return WINHTTP_REQUEST_TIMES
def _define_WINHTTP_REQUEST_TIMES():
    WINHTTP_REQUEST_TIMES = win32more.Networking.WinHttp.WINHTTP_REQUEST_TIMES_head
    WINHTTP_REQUEST_TIMES._fields_ = [
        ('cTimes', UInt32),
        ('rgullTimes', UInt64 * 64),
    ]
    return WINHTTP_REQUEST_TIMES
def _define_WINHTTP_RESOLVER_CACHE_CONFIG_head():
    class WINHTTP_RESOLVER_CACHE_CONFIG(Structure):
        pass
    return WINHTTP_RESOLVER_CACHE_CONFIG
def _define_WINHTTP_RESOLVER_CACHE_CONFIG():
    WINHTTP_RESOLVER_CACHE_CONFIG = win32more.Networking.WinHttp.WINHTTP_RESOLVER_CACHE_CONFIG_head
    WINHTTP_RESOLVER_CACHE_CONFIG._fields_ = [
        ('ulMaxResolverCacheEntries', UInt32),
        ('ulMaxCacheEntryAge', UInt32),
        ('ulMinCacheEntryTtl', UInt32),
        ('SecureDnsSetting', win32more.Networking.WinHttp.WINHTTP_SECURE_DNS_SETTING),
        ('ullConnResolutionWaitTime', UInt64),
        ('ullFlags', UInt64),
    ]
    return WINHTTP_RESOLVER_CACHE_CONFIG
WINHTTP_SECURE_DNS_SETTING = Int32
WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingDefault = 0
WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingForcePlaintext = 1
WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingRequireEncryption = 2
WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingTryEncryptionWithFallback = 3
WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingMax = 4
def _define_WINHTTP_STATUS_CALLBACK():
    return WINFUNCTYPE(Void,c_void_p,UIntPtr,UInt32,c_void_p,UInt32)
def _define_WINHTTP_WEB_SOCKET_ASYNC_RESULT_head():
    class WINHTTP_WEB_SOCKET_ASYNC_RESULT(Structure):
        pass
    return WINHTTP_WEB_SOCKET_ASYNC_RESULT
def _define_WINHTTP_WEB_SOCKET_ASYNC_RESULT():
    WINHTTP_WEB_SOCKET_ASYNC_RESULT = win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_ASYNC_RESULT_head
    WINHTTP_WEB_SOCKET_ASYNC_RESULT._fields_ = [
        ('AsyncResult', win32more.Networking.WinHttp.WINHTTP_ASYNC_RESULT),
        ('Operation', win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_OPERATION),
    ]
    return WINHTTP_WEB_SOCKET_ASYNC_RESULT
WINHTTP_WEB_SOCKET_BUFFER_TYPE = Int32
WINHTTP_WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE = 0
WINHTTP_WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE = 1
WINHTTP_WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE = 2
WINHTTP_WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE = 3
WINHTTP_WEB_SOCKET_CLOSE_BUFFER_TYPE = 4
WINHTTP_WEB_SOCKET_CLOSE_STATUS = Int32
WINHTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS = 1000
WINHTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS = 1001
WINHTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS = 1002
WINHTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS = 1003
WINHTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS = 1005
WINHTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS = 1006
WINHTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS = 1007
WINHTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS = 1008
WINHTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS = 1009
WINHTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS = 1010
WINHTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS = 1011
WINHTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS = 1015
WINHTTP_WEB_SOCKET_OPERATION = Int32
WINHTTP_WEB_SOCKET_SEND_OPERATION = 0
WINHTTP_WEB_SOCKET_RECEIVE_OPERATION = 1
WINHTTP_WEB_SOCKET_CLOSE_OPERATION = 2
WINHTTP_WEB_SOCKET_SHUTDOWN_OPERATION = 3
def _define_WINHTTP_WEB_SOCKET_STATUS_head():
    class WINHTTP_WEB_SOCKET_STATUS(Structure):
        pass
    return WINHTTP_WEB_SOCKET_STATUS
def _define_WINHTTP_WEB_SOCKET_STATUS():
    WINHTTP_WEB_SOCKET_STATUS = win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_STATUS_head
    WINHTTP_WEB_SOCKET_STATUS._fields_ = [
        ('dwBytesTransferred', UInt32),
        ('eBufferType', win32more.Networking.WinHttp.WINHTTP_WEB_SOCKET_BUFFER_TYPE),
    ]
    return WINHTTP_WEB_SOCKET_STATUS
__all__ = [
    "API_GET_PROXY_FOR_URL",
    "API_QUERY_DATA_AVAILABLE",
    "API_READ_DATA",
    "API_RECEIVE_RESPONSE",
    "API_SEND_REQUEST",
    "API_WRITE_DATA",
    "ERROR_WINHTTP_AUTODETECTION_FAILED",
    "ERROR_WINHTTP_AUTO_PROXY_SERVICE_ERROR",
    "ERROR_WINHTTP_BAD_AUTO_PROXY_SCRIPT",
    "ERROR_WINHTTP_CANNOT_CALL_AFTER_OPEN",
    "ERROR_WINHTTP_CANNOT_CALL_AFTER_SEND",
    "ERROR_WINHTTP_CANNOT_CALL_BEFORE_OPEN",
    "ERROR_WINHTTP_CANNOT_CALL_BEFORE_SEND",
    "ERROR_WINHTTP_CANNOT_CONNECT",
    "ERROR_WINHTTP_CHUNKED_ENCODING_HEADER_SIZE_OVERFLOW",
    "ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED",
    "ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED_PROXY",
    "ERROR_WINHTTP_CLIENT_CERT_NO_ACCESS_PRIVATE_KEY",
    "ERROR_WINHTTP_CLIENT_CERT_NO_PRIVATE_KEY",
    "ERROR_WINHTTP_CONNECTION_ERROR",
    "ERROR_WINHTTP_FEATURE_DISABLED",
    "ERROR_WINHTTP_GLOBAL_CALLBACK_FAILED",
    "ERROR_WINHTTP_HEADER_ALREADY_EXISTS",
    "ERROR_WINHTTP_HEADER_COUNT_EXCEEDED",
    "ERROR_WINHTTP_HEADER_NOT_FOUND",
    "ERROR_WINHTTP_HEADER_SIZE_OVERFLOW",
    "ERROR_WINHTTP_HTTP_PROTOCOL_MISMATCH",
    "ERROR_WINHTTP_INCORRECT_HANDLE_STATE",
    "ERROR_WINHTTP_INCORRECT_HANDLE_TYPE",
    "ERROR_WINHTTP_INTERNAL_ERROR",
    "ERROR_WINHTTP_INVALID_HEADER",
    "ERROR_WINHTTP_INVALID_OPTION",
    "ERROR_WINHTTP_INVALID_QUERY_REQUEST",
    "ERROR_WINHTTP_INVALID_SERVER_RESPONSE",
    "ERROR_WINHTTP_INVALID_URL",
    "ERROR_WINHTTP_LOGIN_FAILURE",
    "ERROR_WINHTTP_NAME_NOT_RESOLVED",
    "ERROR_WINHTTP_NOT_INITIALIZED",
    "ERROR_WINHTTP_OPERATION_CANCELLED",
    "ERROR_WINHTTP_OPTION_NOT_SETTABLE",
    "ERROR_WINHTTP_OUT_OF_HANDLES",
    "ERROR_WINHTTP_REDIRECT_FAILED",
    "ERROR_WINHTTP_RESEND_REQUEST",
    "ERROR_WINHTTP_RESERVED_189",
    "ERROR_WINHTTP_RESPONSE_DRAIN_OVERFLOW",
    "ERROR_WINHTTP_SCRIPT_EXECUTION_ERROR",
    "ERROR_WINHTTP_SECURE_CERT_CN_INVALID",
    "ERROR_WINHTTP_SECURE_CERT_DATE_INVALID",
    "ERROR_WINHTTP_SECURE_CERT_REVOKED",
    "ERROR_WINHTTP_SECURE_CERT_REV_FAILED",
    "ERROR_WINHTTP_SECURE_CERT_WRONG_USAGE",
    "ERROR_WINHTTP_SECURE_CHANNEL_ERROR",
    "ERROR_WINHTTP_SECURE_FAILURE",
    "ERROR_WINHTTP_SECURE_FAILURE_PROXY",
    "ERROR_WINHTTP_SECURE_INVALID_CA",
    "ERROR_WINHTTP_SECURE_INVALID_CERT",
    "ERROR_WINHTTP_SHUTDOWN",
    "ERROR_WINHTTP_TIMEOUT",
    "ERROR_WINHTTP_UNABLE_TO_DOWNLOAD_SCRIPT",
    "ERROR_WINHTTP_UNHANDLED_SCRIPT_TYPE",
    "ERROR_WINHTTP_UNRECOGNIZED_SCHEME",
    "HTTP_STATUS_ACCEPTED",
    "HTTP_STATUS_AMBIGUOUS",
    "HTTP_STATUS_BAD_GATEWAY",
    "HTTP_STATUS_BAD_METHOD",
    "HTTP_STATUS_BAD_REQUEST",
    "HTTP_STATUS_CONFLICT",
    "HTTP_STATUS_CONTINUE",
    "HTTP_STATUS_CREATED",
    "HTTP_STATUS_DENIED",
    "HTTP_STATUS_FIRST",
    "HTTP_STATUS_FORBIDDEN",
    "HTTP_STATUS_GATEWAY_TIMEOUT",
    "HTTP_STATUS_GONE",
    "HTTP_STATUS_LAST",
    "HTTP_STATUS_LENGTH_REQUIRED",
    "HTTP_STATUS_MOVED",
    "HTTP_STATUS_NONE_ACCEPTABLE",
    "HTTP_STATUS_NOT_FOUND",
    "HTTP_STATUS_NOT_MODIFIED",
    "HTTP_STATUS_NOT_SUPPORTED",
    "HTTP_STATUS_NO_CONTENT",
    "HTTP_STATUS_OK",
    "HTTP_STATUS_PARTIAL",
    "HTTP_STATUS_PARTIAL_CONTENT",
    "HTTP_STATUS_PAYMENT_REQ",
    "HTTP_STATUS_PERMANENT_REDIRECT",
    "HTTP_STATUS_PRECOND_FAILED",
    "HTTP_STATUS_PROXY_AUTH_REQ",
    "HTTP_STATUS_REDIRECT",
    "HTTP_STATUS_REDIRECT_KEEP_VERB",
    "HTTP_STATUS_REDIRECT_METHOD",
    "HTTP_STATUS_REQUEST_TIMEOUT",
    "HTTP_STATUS_REQUEST_TOO_LARGE",
    "HTTP_STATUS_RESET_CONTENT",
    "HTTP_STATUS_RETRY_WITH",
    "HTTP_STATUS_SERVER_ERROR",
    "HTTP_STATUS_SERVICE_UNAVAIL",
    "HTTP_STATUS_SWITCH_PROTOCOLS",
    "HTTP_STATUS_UNSUPPORTED_MEDIA",
    "HTTP_STATUS_URI_TOO_LONG",
    "HTTP_STATUS_USE_PROXY",
    "HTTP_STATUS_VERSION_NOT_SUP",
    "HTTP_STATUS_WEBDAV_MULTI_STATUS",
    "HTTP_VERSION_INFO",
    "ICU_BROWSER_MODE",
    "ICU_DECODE",
    "ICU_ENCODE_PERCENT",
    "ICU_ENCODE_SPACES_ONLY",
    "ICU_ESCAPE",
    "ICU_ESCAPE_AUTHORITY",
    "ICU_NO_ENCODE",
    "ICU_NO_META",
    "ICU_REJECT_USERPWD",
    "INTERNET_DEFAULT_HTTPS_PORT",
    "INTERNET_DEFAULT_HTTP_PORT",
    "INTERNET_DEFAULT_PORT",
    "INTERNET_PORT",
    "NETWORKING_KEY_BUFSIZE",
    "SECURITY_FLAG_IGNORE_CERT_CN_INVALID",
    "SECURITY_FLAG_IGNORE_CERT_DATE_INVALID",
    "SECURITY_FLAG_IGNORE_CERT_WRONG_USAGE",
    "SECURITY_FLAG_IGNORE_UNKNOWN_CA",
    "SECURITY_FLAG_SECURE",
    "SECURITY_FLAG_STRENGTH_MEDIUM",
    "SECURITY_FLAG_STRENGTH_STRONG",
    "SECURITY_FLAG_STRENGTH_WEAK",
    "URL_COMPONENTS",
    "WINHTTP_ACCESS_TYPE",
    "WINHTTP_ACCESS_TYPE_AUTOMATIC_PROXY",
    "WINHTTP_ACCESS_TYPE_DEFAULT_PROXY",
    "WINHTTP_ACCESS_TYPE_NAMED_PROXY",
    "WINHTTP_ACCESS_TYPE_NO_PROXY",
    "WINHTTP_ADDREQ_FLAGS_MASK",
    "WINHTTP_ADDREQ_FLAG_ADD",
    "WINHTTP_ADDREQ_FLAG_ADD_IF_NEW",
    "WINHTTP_ADDREQ_FLAG_COALESCE",
    "WINHTTP_ADDREQ_FLAG_COALESCE_WITH_COMMA",
    "WINHTTP_ADDREQ_FLAG_COALESCE_WITH_SEMICOLON",
    "WINHTTP_ADDREQ_FLAG_REPLACE",
    "WINHTTP_ADDREQ_INDEX_MASK",
    "WINHTTP_ASYNC_RESULT",
    "WINHTTP_AUTH_SCHEME_BASIC",
    "WINHTTP_AUTH_SCHEME_DIGEST",
    "WINHTTP_AUTH_SCHEME_NEGOTIATE",
    "WINHTTP_AUTH_SCHEME_NTLM",
    "WINHTTP_AUTH_SCHEME_PASSPORT",
    "WINHTTP_AUTH_TARGET_PROXY",
    "WINHTTP_AUTH_TARGET_SERVER",
    "WINHTTP_AUTOLOGON_SECURITY_LEVEL_DEFAULT",
    "WINHTTP_AUTOLOGON_SECURITY_LEVEL_HIGH",
    "WINHTTP_AUTOLOGON_SECURITY_LEVEL_LOW",
    "WINHTTP_AUTOLOGON_SECURITY_LEVEL_MEDIUM",
    "WINHTTP_AUTOPROXY_ALLOW_AUTOCONFIG",
    "WINHTTP_AUTOPROXY_ALLOW_CM",
    "WINHTTP_AUTOPROXY_ALLOW_STATIC",
    "WINHTTP_AUTOPROXY_AUTO_DETECT",
    "WINHTTP_AUTOPROXY_CONFIG_URL",
    "WINHTTP_AUTOPROXY_HOST_KEEPCASE",
    "WINHTTP_AUTOPROXY_HOST_LOWERCASE",
    "WINHTTP_AUTOPROXY_NO_CACHE_CLIENT",
    "WINHTTP_AUTOPROXY_NO_CACHE_SVC",
    "WINHTTP_AUTOPROXY_NO_DIRECTACCESS",
    "WINHTTP_AUTOPROXY_OPTIONS",
    "WINHTTP_AUTOPROXY_RUN_INPROCESS",
    "WINHTTP_AUTOPROXY_RUN_OUTPROCESS_ONLY",
    "WINHTTP_AUTOPROXY_SORT_RESULTS",
    "WINHTTP_AUTO_DETECT_TYPE_DHCP",
    "WINHTTP_AUTO_DETECT_TYPE_DNS_A",
    "WINHTTP_CALLBACK_FLAG_ALL_NOTIFICATIONS",
    "WINHTTP_CALLBACK_FLAG_DATA_AVAILABLE",
    "WINHTTP_CALLBACK_FLAG_DETECTING_PROXY",
    "WINHTTP_CALLBACK_FLAG_GETPROXYFORURL_COMPLETE",
    "WINHTTP_CALLBACK_FLAG_HEADERS_AVAILABLE",
    "WINHTTP_CALLBACK_FLAG_INTERMEDIATE_RESPONSE",
    "WINHTTP_CALLBACK_FLAG_READ_COMPLETE",
    "WINHTTP_CALLBACK_FLAG_REDIRECT",
    "WINHTTP_CALLBACK_FLAG_REQUEST_ERROR",
    "WINHTTP_CALLBACK_FLAG_SECURE_FAILURE",
    "WINHTTP_CALLBACK_FLAG_SENDREQUEST_COMPLETE",
    "WINHTTP_CALLBACK_FLAG_WRITE_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_CLOSE_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_CLOSING_CONNECTION",
    "WINHTTP_CALLBACK_STATUS_CONNECTED_TO_SERVER",
    "WINHTTP_CALLBACK_STATUS_CONNECTING_TO_SERVER",
    "WINHTTP_CALLBACK_STATUS_CONNECTION_CLOSED",
    "WINHTTP_CALLBACK_STATUS_DATA_AVAILABLE",
    "WINHTTP_CALLBACK_STATUS_DETECTING_PROXY",
    "WINHTTP_CALLBACK_STATUS_FLAG_CERT_CN_INVALID",
    "WINHTTP_CALLBACK_STATUS_FLAG_CERT_DATE_INVALID",
    "WINHTTP_CALLBACK_STATUS_FLAG_CERT_REVOKED",
    "WINHTTP_CALLBACK_STATUS_FLAG_CERT_REV_FAILED",
    "WINHTTP_CALLBACK_STATUS_FLAG_CERT_WRONG_USAGE",
    "WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CA",
    "WINHTTP_CALLBACK_STATUS_FLAG_INVALID_CERT",
    "WINHTTP_CALLBACK_STATUS_FLAG_SECURITY_CHANNEL_ERROR",
    "WINHTTP_CALLBACK_STATUS_GETPROXYFORURL_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_HANDLE_CLOSING",
    "WINHTTP_CALLBACK_STATUS_HANDLE_CREATED",
    "WINHTTP_CALLBACK_STATUS_HEADERS_AVAILABLE",
    "WINHTTP_CALLBACK_STATUS_INTERMEDIATE_RESPONSE",
    "WINHTTP_CALLBACK_STATUS_NAME_RESOLVED",
    "WINHTTP_CALLBACK_STATUS_READ_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_RECEIVING_RESPONSE",
    "WINHTTP_CALLBACK_STATUS_REDIRECT",
    "WINHTTP_CALLBACK_STATUS_REQUEST_ERROR",
    "WINHTTP_CALLBACK_STATUS_REQUEST_SENT",
    "WINHTTP_CALLBACK_STATUS_RESOLVING_NAME",
    "WINHTTP_CALLBACK_STATUS_RESPONSE_RECEIVED",
    "WINHTTP_CALLBACK_STATUS_SECURE_FAILURE",
    "WINHTTP_CALLBACK_STATUS_SENDING_REQUEST",
    "WINHTTP_CALLBACK_STATUS_SENDREQUEST_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_SETTINGS_READ_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_SETTINGS_WRITE_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_SHUTDOWN_COMPLETE",
    "WINHTTP_CALLBACK_STATUS_WRITE_COMPLETE",
    "WINHTTP_CERTIFICATE_INFO",
    "WINHTTP_CONNECTION_GROUP",
    "WINHTTP_CONNECTION_INFO",
    "WINHTTP_CONNECTION_RETRY_CONDITION_408",
    "WINHTTP_CONNECTION_RETRY_CONDITION_SSL_HANDSHAKE",
    "WINHTTP_CONNECTION_RETRY_CONDITION_STALE_CONNECTION",
    "WINHTTP_CONNS_PER_SERVER_UNLIMITED",
    "WINHTTP_CREDS",
    "WINHTTP_CREDS_AUTHSCHEME",
    "WINHTTP_CREDS_EX",
    "WINHTTP_CURRENT_USER_IE_PROXY_CONFIG",
    "WINHTTP_DECOMPRESSION_FLAG_DEFLATE",
    "WINHTTP_DECOMPRESSION_FLAG_GZIP",
    "WINHTTP_DISABLE_AUTHENTICATION",
    "WINHTTP_DISABLE_COOKIES",
    "WINHTTP_DISABLE_KEEP_ALIVE",
    "WINHTTP_DISABLE_PASSPORT_AUTH",
    "WINHTTP_DISABLE_PASSPORT_KEYRING",
    "WINHTTP_DISABLE_REDIRECTS",
    "WINHTTP_DISABLE_SPN_SERVER_PORT",
    "WINHTTP_ENABLE_PASSPORT_AUTH",
    "WINHTTP_ENABLE_PASSPORT_KEYRING",
    "WINHTTP_ENABLE_SPN_SERVER_PORT",
    "WINHTTP_ENABLE_SSL_REVERT_IMPERSONATION",
    "WINHTTP_ENABLE_SSL_REVOCATION",
    "WINHTTP_ERROR_BASE",
    "WINHTTP_ERROR_LAST",
    "WINHTTP_EXTENDED_HEADER",
    "WINHTTP_EXTENDED_HEADER_FLAG_UNICODE",
    "WINHTTP_FAILED_CONNECTION_RETRIES",
    "WINHTTP_FLAG_ASYNC",
    "WINHTTP_FLAG_BYPASS_PROXY_CACHE",
    "WINHTTP_FLAG_ESCAPE_DISABLE",
    "WINHTTP_FLAG_ESCAPE_DISABLE_QUERY",
    "WINHTTP_FLAG_ESCAPE_PERCENT",
    "WINHTTP_FLAG_NULL_CODEPAGE",
    "WINHTTP_FLAG_REFRESH",
    "WINHTTP_FLAG_SECURE",
    "WINHTTP_FLAG_SECURE_DEFAULTS",
    "WINHTTP_FLAG_SECURE_PROTOCOL_SSL2",
    "WINHTTP_FLAG_SECURE_PROTOCOL_SSL3",
    "WINHTTP_FLAG_SECURE_PROTOCOL_TLS1",
    "WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_1",
    "WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_2",
    "WINHTTP_FLAG_SECURE_PROTOCOL_TLS1_3",
    "WINHTTP_HANDLE_TYPE_CONNECT",
    "WINHTTP_HANDLE_TYPE_REQUEST",
    "WINHTTP_HANDLE_TYPE_SESSION",
    "WINHTTP_HEADER_NAME",
    "WINHTTP_HOST_CONNECTION_GROUP",
    "WINHTTP_HTTP2_RECEIVE_WINDOW",
    "WINHTTP_IGNORE_REQUEST_TOTAL_LENGTH",
    "WINHTTP_INTERNET_SCHEME",
    "WINHTTP_INTERNET_SCHEME_FTP",
    "WINHTTP_INTERNET_SCHEME_HTTP",
    "WINHTTP_INTERNET_SCHEME_HTTPS",
    "WINHTTP_INTERNET_SCHEME_SOCKS",
    "WINHTTP_LAST_OPTION",
    "WINHTTP_MATCH_CONNECTION_GUID",
    "WINHTTP_MATCH_CONNECTION_GUID_FLAGS_MASK",
    "WINHTTP_MATCH_CONNECTION_GUID_FLAG_REQUIRE_MARKED_CONNECTION",
    "WINHTTP_OPEN_REQUEST_FLAGS",
    "WINHTTP_OPTION_AGGREGATE_PROXY_CONFIG",
    "WINHTTP_OPTION_ASSURED_NON_BLOCKING_CALLBACKS",
    "WINHTTP_OPTION_AUTOLOGON_POLICY",
    "WINHTTP_OPTION_BACKGROUND_CONNECTIONS",
    "WINHTTP_OPTION_CALLBACK",
    "WINHTTP_OPTION_CLIENT_CERT_CONTEXT",
    "WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST",
    "WINHTTP_OPTION_CODEPAGE",
    "WINHTTP_OPTION_CONFIGURE_PASSPORT_AUTH",
    "WINHTTP_OPTION_CONNECTION_FILTER",
    "WINHTTP_OPTION_CONNECTION_GUID",
    "WINHTTP_OPTION_CONNECTION_INFO",
    "WINHTTP_OPTION_CONNECTION_STATS_V0",
    "WINHTTP_OPTION_CONNECTION_STATS_V1",
    "WINHTTP_OPTION_CONNECT_RETRIES",
    "WINHTTP_OPTION_CONNECT_TIMEOUT",
    "WINHTTP_OPTION_CONTEXT_VALUE",
    "WINHTTP_OPTION_DECOMPRESSION",
    "WINHTTP_OPTION_DISABLE_CERT_CHAIN_BUILDING",
    "WINHTTP_OPTION_DISABLE_FEATURE",
    "WINHTTP_OPTION_DISABLE_PROXY_LINK_LOCAL_NAME_RESOLUTION",
    "WINHTTP_OPTION_DISABLE_SECURE_PROTOCOL_FALLBACK",
    "WINHTTP_OPTION_DISABLE_STREAM_QUEUE",
    "WINHTTP_OPTION_ENABLETRACING",
    "WINHTTP_OPTION_ENABLE_FEATURE",
    "WINHTTP_OPTION_ENABLE_HTTP2_PLUS_CLIENT_CERT",
    "WINHTTP_OPTION_ENABLE_HTTP_PROTOCOL",
    "WINHTTP_OPTION_ENABLE_TEST_SIGNING",
    "WINHTTP_OPTION_ENCODE_EXTRA",
    "WINHTTP_OPTION_EXPIRE_CONNECTION",
    "WINHTTP_OPTION_EXTENDED_ERROR",
    "WINHTTP_OPTION_FAILED_CONNECTION_RETRIES",
    "WINHTTP_OPTION_FIRST_AVAILABLE_CONNECTION",
    "WINHTTP_OPTION_GLOBAL_PROXY_CREDS",
    "WINHTTP_OPTION_GLOBAL_SERVER_CREDS",
    "WINHTTP_OPTION_HANDLE_TYPE",
    "WINHTTP_OPTION_HEAP_EXTENSION",
    "WINHTTP_OPTION_HTTP2_KEEPALIVE",
    "WINHTTP_OPTION_HTTP2_PLUS_TRANSFER_ENCODING",
    "WINHTTP_OPTION_HTTP2_RECEIVE_WINDOW",
    "WINHTTP_OPTION_HTTP_PROTOCOL_REQUIRED",
    "WINHTTP_OPTION_HTTP_PROTOCOL_USED",
    "WINHTTP_OPTION_HTTP_VERSION",
    "WINHTTP_OPTION_IGNORE_CERT_REVOCATION_OFFLINE",
    "WINHTTP_OPTION_IPV6_FAST_FALLBACK",
    "WINHTTP_OPTION_IS_PROXY_CONNECT_RESPONSE",
    "WINHTTP_OPTION_KDC_PROXY_SETTINGS",
    "WINHTTP_OPTION_MATCH_CONNECTION_GUID",
    "WINHTTP_OPTION_MAX_CONNS_PER_1_0_SERVER",
    "WINHTTP_OPTION_MAX_CONNS_PER_SERVER",
    "WINHTTP_OPTION_MAX_HTTP_AUTOMATIC_REDIRECTS",
    "WINHTTP_OPTION_MAX_HTTP_STATUS_CONTINUE",
    "WINHTTP_OPTION_MAX_RESPONSE_DRAIN_SIZE",
    "WINHTTP_OPTION_MAX_RESPONSE_HEADER_SIZE",
    "WINHTTP_OPTION_NTSERVICE_FLAG_TEST",
    "WINHTTP_OPTION_PARENT_HANDLE",
    "WINHTTP_OPTION_PASSPORT_COBRANDING_TEXT",
    "WINHTTP_OPTION_PASSPORT_COBRANDING_URL",
    "WINHTTP_OPTION_PASSPORT_RETURN_URL",
    "WINHTTP_OPTION_PASSPORT_SIGN_OUT",
    "WINHTTP_OPTION_PASSWORD",
    "WINHTTP_OPTION_PROXY",
    "WINHTTP_OPTION_PROXY_CONFIG_INFO",
    "WINHTTP_OPTION_PROXY_DISABLE_SERVICE_CALLS",
    "WINHTTP_OPTION_PROXY_PASSWORD",
    "WINHTTP_OPTION_PROXY_RESULT_ENTRY",
    "WINHTTP_OPTION_PROXY_SPN_USED",
    "WINHTTP_OPTION_PROXY_USERNAME",
    "WINHTTP_OPTION_READ_BUFFER_SIZE",
    "WINHTTP_OPTION_RECEIVE_PROXY_CONNECT_RESPONSE",
    "WINHTTP_OPTION_RECEIVE_RESPONSE_TIMEOUT",
    "WINHTTP_OPTION_RECEIVE_TIMEOUT",
    "WINHTTP_OPTION_REDIRECT_POLICY",
    "WINHTTP_OPTION_REDIRECT_POLICY_ALWAYS",
    "WINHTTP_OPTION_REDIRECT_POLICY_DEFAULT",
    "WINHTTP_OPTION_REDIRECT_POLICY_DISALLOW_HTTPS_TO_HTTP",
    "WINHTTP_OPTION_REDIRECT_POLICY_LAST",
    "WINHTTP_OPTION_REDIRECT_POLICY_NEVER",
    "WINHTTP_OPTION_REFERER_TOKEN_BINDING_HOSTNAME",
    "WINHTTP_OPTION_REJECT_USERPWD_IN_URL",
    "WINHTTP_OPTION_REQUEST_PRIORITY",
    "WINHTTP_OPTION_REQUEST_STATS",
    "WINHTTP_OPTION_REQUEST_TIMES",
    "WINHTTP_OPTION_REQUIRE_STREAM_END",
    "WINHTTP_OPTION_RESOLUTION_HOSTNAME",
    "WINHTTP_OPTION_RESOLVER_CACHE_CONFIG",
    "WINHTTP_OPTION_RESOLVE_TIMEOUT",
    "WINHTTP_OPTION_SECURE_PROTOCOLS",
    "WINHTTP_OPTION_SECURITY_CERTIFICATE_STRUCT",
    "WINHTTP_OPTION_SECURITY_FLAGS",
    "WINHTTP_OPTION_SECURITY_INFO",
    "WINHTTP_OPTION_SECURITY_KEY_BITNESS",
    "WINHTTP_OPTION_SELECTED_PROXY_CONFIG_INFO",
    "WINHTTP_OPTION_SEND_TIMEOUT",
    "WINHTTP_OPTION_SERVER_CBT",
    "WINHTTP_OPTION_SERVER_CERT_CHAIN_CONTEXT",
    "WINHTTP_OPTION_SERVER_CERT_CONTEXT",
    "WINHTTP_OPTION_SERVER_SPN_USED",
    "WINHTTP_OPTION_SET_GLOBAL_CALLBACK",
    "WINHTTP_OPTION_SET_TOKEN_BINDING",
    "WINHTTP_OPTION_SOURCE_ADDRESS",
    "WINHTTP_OPTION_SPN",
    "WINHTTP_OPTION_SPN_MASK",
    "WINHTTP_OPTION_STREAM_ERROR_CODE",
    "WINHTTP_OPTION_TCP_FAST_OPEN",
    "WINHTTP_OPTION_TCP_KEEPALIVE",
    "WINHTTP_OPTION_TCP_PRIORITY_HINT",
    "WINHTTP_OPTION_TCP_PRIORITY_STATUS",
    "WINHTTP_OPTION_TLS_FALSE_START",
    "WINHTTP_OPTION_TLS_PROTOCOL_INSECURE_FALLBACK",
    "WINHTTP_OPTION_TOKEN_BINDING_PUBLIC_KEY",
    "WINHTTP_OPTION_UNLOAD_NOTIFY_EVENT",
    "WINHTTP_OPTION_UNSAFE_HEADER_PARSING",
    "WINHTTP_OPTION_UPGRADE_TO_WEB_SOCKET",
    "WINHTTP_OPTION_URL",
    "WINHTTP_OPTION_USERNAME",
    "WINHTTP_OPTION_USER_AGENT",
    "WINHTTP_OPTION_USE_GLOBAL_SERVER_CREDENTIALS",
    "WINHTTP_OPTION_WEB_SOCKET_CLOSE_TIMEOUT",
    "WINHTTP_OPTION_WEB_SOCKET_KEEPALIVE_INTERVAL",
    "WINHTTP_OPTION_WEB_SOCKET_RECEIVE_BUFFER_SIZE",
    "WINHTTP_OPTION_WEB_SOCKET_SEND_BUFFER_SIZE",
    "WINHTTP_OPTION_WORKER_THREAD_COUNT",
    "WINHTTP_OPTION_WRITE_BUFFER_SIZE",
    "WINHTTP_PROTOCOL_FLAG_HTTP2",
    "WINHTTP_PROTOCOL_FLAG_HTTP3",
    "WINHTTP_PROXY_INFO",
    "WINHTTP_PROXY_NETWORKING_KEY",
    "WINHTTP_PROXY_RESULT",
    "WINHTTP_PROXY_RESULT_ENTRY",
    "WINHTTP_PROXY_RESULT_EX",
    "WINHTTP_PROXY_SETTINGS",
    "WINHTTP_PROXY_TYPE_AUTO_DETECT",
    "WINHTTP_PROXY_TYPE_AUTO_PROXY_URL",
    "WINHTTP_PROXY_TYPE_DIRECT",
    "WINHTTP_PROXY_TYPE_PROXY",
    "WINHTTP_QUERY_ACCEPT",
    "WINHTTP_QUERY_ACCEPT_CHARSET",
    "WINHTTP_QUERY_ACCEPT_ENCODING",
    "WINHTTP_QUERY_ACCEPT_LANGUAGE",
    "WINHTTP_QUERY_ACCEPT_RANGES",
    "WINHTTP_QUERY_AGE",
    "WINHTTP_QUERY_ALLOW",
    "WINHTTP_QUERY_AUTHENTICATION_INFO",
    "WINHTTP_QUERY_AUTHORIZATION",
    "WINHTTP_QUERY_CACHE_CONTROL",
    "WINHTTP_QUERY_CONNECTION",
    "WINHTTP_QUERY_CONNECTION_GROUP_RESULT",
    "WINHTTP_QUERY_CONTENT_BASE",
    "WINHTTP_QUERY_CONTENT_DESCRIPTION",
    "WINHTTP_QUERY_CONTENT_DISPOSITION",
    "WINHTTP_QUERY_CONTENT_ENCODING",
    "WINHTTP_QUERY_CONTENT_ID",
    "WINHTTP_QUERY_CONTENT_LANGUAGE",
    "WINHTTP_QUERY_CONTENT_LENGTH",
    "WINHTTP_QUERY_CONTENT_LOCATION",
    "WINHTTP_QUERY_CONTENT_MD5",
    "WINHTTP_QUERY_CONTENT_RANGE",
    "WINHTTP_QUERY_CONTENT_TRANSFER_ENCODING",
    "WINHTTP_QUERY_CONTENT_TYPE",
    "WINHTTP_QUERY_COOKIE",
    "WINHTTP_QUERY_COST",
    "WINHTTP_QUERY_CUSTOM",
    "WINHTTP_QUERY_DATE",
    "WINHTTP_QUERY_DERIVED_FROM",
    "WINHTTP_QUERY_ETAG",
    "WINHTTP_QUERY_EXPECT",
    "WINHTTP_QUERY_EXPIRES",
    "WINHTTP_QUERY_EX_ALL_HEADERS",
    "WINHTTP_QUERY_FLAG_NUMBER",
    "WINHTTP_QUERY_FLAG_NUMBER64",
    "WINHTTP_QUERY_FLAG_REQUEST_HEADERS",
    "WINHTTP_QUERY_FLAG_SYSTEMTIME",
    "WINHTTP_QUERY_FLAG_TRAILERS",
    "WINHTTP_QUERY_FLAG_WIRE_ENCODING",
    "WINHTTP_QUERY_FORWARDED",
    "WINHTTP_QUERY_FROM",
    "WINHTTP_QUERY_HOST",
    "WINHTTP_QUERY_IF_MATCH",
    "WINHTTP_QUERY_IF_MODIFIED_SINCE",
    "WINHTTP_QUERY_IF_NONE_MATCH",
    "WINHTTP_QUERY_IF_RANGE",
    "WINHTTP_QUERY_IF_UNMODIFIED_SINCE",
    "WINHTTP_QUERY_LAST_MODIFIED",
    "WINHTTP_QUERY_LINK",
    "WINHTTP_QUERY_LOCATION",
    "WINHTTP_QUERY_MAX",
    "WINHTTP_QUERY_MAX_FORWARDS",
    "WINHTTP_QUERY_MESSAGE_ID",
    "WINHTTP_QUERY_MIME_VERSION",
    "WINHTTP_QUERY_ORIG_URI",
    "WINHTTP_QUERY_PASSPORT_CONFIG",
    "WINHTTP_QUERY_PASSPORT_URLS",
    "WINHTTP_QUERY_PRAGMA",
    "WINHTTP_QUERY_PROXY_AUTHENTICATE",
    "WINHTTP_QUERY_PROXY_AUTHORIZATION",
    "WINHTTP_QUERY_PROXY_CONNECTION",
    "WINHTTP_QUERY_PROXY_SUPPORT",
    "WINHTTP_QUERY_PUBLIC",
    "WINHTTP_QUERY_RANGE",
    "WINHTTP_QUERY_RAW_HEADERS",
    "WINHTTP_QUERY_RAW_HEADERS_CRLF",
    "WINHTTP_QUERY_REFERER",
    "WINHTTP_QUERY_REFRESH",
    "WINHTTP_QUERY_REQUEST_METHOD",
    "WINHTTP_QUERY_RETRY_AFTER",
    "WINHTTP_QUERY_SERVER",
    "WINHTTP_QUERY_SET_COOKIE",
    "WINHTTP_QUERY_STATUS_CODE",
    "WINHTTP_QUERY_STATUS_TEXT",
    "WINHTTP_QUERY_TITLE",
    "WINHTTP_QUERY_TRANSFER_ENCODING",
    "WINHTTP_QUERY_UNLESS_MODIFIED_SINCE",
    "WINHTTP_QUERY_UPGRADE",
    "WINHTTP_QUERY_URI",
    "WINHTTP_QUERY_USER_AGENT",
    "WINHTTP_QUERY_VARY",
    "WINHTTP_QUERY_VERSION",
    "WINHTTP_QUERY_VIA",
    "WINHTTP_QUERY_WARNING",
    "WINHTTP_QUERY_WWW_AUTHENTICATE",
    "WINHTTP_REQUEST_STATS",
    "WINHTTP_REQUEST_STAT_ENTRY",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpConnectFailureCount",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyFailureCount",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeClientLeg1Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeClientLeg2Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeServerLeg1Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpProxyTlsHandshakeServerLeg2Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestHeadersCompressedSize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestHeadersSize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestStatLast",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpRequestStatMax",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseBodyCompressedSize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseBodySize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseHeadersCompressedSize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpResponseHeadersSize",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeClientLeg1Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeClientLeg2Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeServerLeg1Size",
    "WINHTTP_REQUEST_STAT_ENTRY_WinHttpTlsHandshakeServerLeg2Size",
    "WINHTTP_REQUEST_STAT_FLAG_FIRST_REQUEST",
    "WINHTTP_REQUEST_STAT_FLAG_PROXY_TLS_FALSE_START",
    "WINHTTP_REQUEST_STAT_FLAG_PROXY_TLS_SESSION_RESUMPTION",
    "WINHTTP_REQUEST_STAT_FLAG_TCP_FAST_OPEN",
    "WINHTTP_REQUEST_STAT_FLAG_TLS_FALSE_START",
    "WINHTTP_REQUEST_STAT_FLAG_TLS_SESSION_RESUMPTION",
    "WINHTTP_REQUEST_TIMES",
    "WINHTTP_REQUEST_TIME_ENTRY",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionAcquireWaitEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionEstablishmentEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpConnectionEstablishmentStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpNameResolutionEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpNameResolutionStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyDetectionEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyDetectionStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg1End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg1Start",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg2End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg2Start",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg3End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTlsHandshakeClientLeg3Start",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTunnelEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpProxyTunnelStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseBodyDecompressionDelta",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersDecompressionEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersDecompressionStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseHeadersEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpReceiveResponseStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpRequestTimeLast",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpRequestTimeMax",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersCompressionEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersCompressionStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestHeadersEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpSendRequestStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpStreamWaitEnd",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpStreamWaitStart",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg1End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg1Start",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg2End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg2Start",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg3End",
    "WINHTTP_REQUEST_TIME_ENTRY_WinHttpTlsHandshakeClientLeg3Start",
    "WINHTTP_RESET_ALL",
    "WINHTTP_RESET_DISCARD_RESOLVERS",
    "WINHTTP_RESET_NOTIFY_NETWORK_CHANGED",
    "WINHTTP_RESET_OUT_OF_PROC",
    "WINHTTP_RESET_SCRIPT_CACHE",
    "WINHTTP_RESET_STATE",
    "WINHTTP_RESET_SWPAD_ALL",
    "WINHTTP_RESET_SWPAD_CURRENT_NETWORK",
    "WINHTTP_RESOLVER_CACHE_CONFIG",
    "WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_BYPASS_CACHE",
    "WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_CONN_USE_TTL",
    "WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_SOFT_LIMIT",
    "WINHTTP_RESOLVER_CACHE_CONFIG_FLAG_USE_DNS_TTL",
    "WINHTTP_SECURE_DNS_SETTING",
    "WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingDefault",
    "WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingForcePlaintext",
    "WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingMax",
    "WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingRequireEncryption",
    "WINHTTP_SECURE_DNS_SETTING_WinHttpSecureDnsSettingTryEncryptionWithFallback",
    "WINHTTP_STATUS_CALLBACK",
    "WINHTTP_TIME_FORMAT_BUFSIZE",
    "WINHTTP_WEB_SOCKET_ABORTED_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_ASYNC_RESULT",
    "WINHTTP_WEB_SOCKET_BINARY_FRAGMENT_BUFFER_TYPE",
    "WINHTTP_WEB_SOCKET_BINARY_MESSAGE_BUFFER_TYPE",
    "WINHTTP_WEB_SOCKET_BUFFER_TYPE",
    "WINHTTP_WEB_SOCKET_CLOSE_BUFFER_TYPE",
    "WINHTTP_WEB_SOCKET_CLOSE_OPERATION",
    "WINHTTP_WEB_SOCKET_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_EMPTY_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_ENDPOINT_TERMINATED_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_INVALID_DATA_TYPE_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_INVALID_PAYLOAD_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_MAX_CLOSE_REASON_LENGTH",
    "WINHTTP_WEB_SOCKET_MESSAGE_TOO_BIG_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_MIN_KEEPALIVE_VALUE",
    "WINHTTP_WEB_SOCKET_OPERATION",
    "WINHTTP_WEB_SOCKET_POLICY_VIOLATION_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_PROTOCOL_ERROR_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_RECEIVE_OPERATION",
    "WINHTTP_WEB_SOCKET_SECURE_HANDSHAKE_ERROR_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_SEND_OPERATION",
    "WINHTTP_WEB_SOCKET_SERVER_ERROR_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_SHUTDOWN_OPERATION",
    "WINHTTP_WEB_SOCKET_STATUS",
    "WINHTTP_WEB_SOCKET_SUCCESS_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_UNSUPPORTED_EXTENSIONS_CLOSE_STATUS",
    "WINHTTP_WEB_SOCKET_UTF8_FRAGMENT_BUFFER_TYPE",
    "WINHTTP_WEB_SOCKET_UTF8_MESSAGE_BUFFER_TYPE",
    "WIN_HTTP_CREATE_URL_FLAGS",
    "WinHttpAddRequestHeaders",
    "WinHttpAddRequestHeadersEx",
    "WinHttpCheckPlatform",
    "WinHttpCloseHandle",
    "WinHttpConnect",
    "WinHttpCrackUrl",
    "WinHttpCreateProxyResolver",
    "WinHttpCreateUrl",
    "WinHttpDetectAutoProxyConfigUrl",
    "WinHttpFreeProxyResult",
    "WinHttpFreeProxyResultEx",
    "WinHttpFreeProxySettings",
    "WinHttpFreeQueryConnectionGroupResult",
    "WinHttpGetDefaultProxyConfiguration",
    "WinHttpGetIEProxyConfigForCurrentUser",
    "WinHttpGetProxyForUrl",
    "WinHttpGetProxyForUrlEx",
    "WinHttpGetProxyForUrlEx2",
    "WinHttpGetProxyResult",
    "WinHttpGetProxyResultEx",
    "WinHttpGetProxySettingsVersion",
    "WinHttpOpen",
    "WinHttpOpenRequest",
    "WinHttpQueryAuthSchemes",
    "WinHttpQueryConnectionGroup",
    "WinHttpQueryDataAvailable",
    "WinHttpQueryHeaders",
    "WinHttpQueryHeadersEx",
    "WinHttpQueryOption",
    "WinHttpReadData",
    "WinHttpReadDataEx",
    "WinHttpReadProxySettings",
    "WinHttpReceiveResponse",
    "WinHttpResetAutoProxy",
    "WinHttpSendRequest",
    "WinHttpSetCredentials",
    "WinHttpSetDefaultProxyConfiguration",
    "WinHttpSetOption",
    "WinHttpSetProxySettingsPerUser",
    "WinHttpSetStatusCallback",
    "WinHttpSetTimeouts",
    "WinHttpTimeFromSystemTime",
    "WinHttpTimeToSystemTime",
    "WinHttpWebSocketClose",
    "WinHttpWebSocketCompleteUpgrade",
    "WinHttpWebSocketQueryCloseStatus",
    "WinHttpWebSocketReceive",
    "WinHttpWebSocketSend",
    "WinHttpWebSocketShutdown",
    "WinHttpWriteData",
    "WinHttpWriteProxySettings",
]
