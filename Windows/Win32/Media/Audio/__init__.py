from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Foundation
import Windows.Win32.Media
import Windows.Win32.Media.Audio
import Windows.Win32.Media.Multimedia
import Windows.Win32.System.Com
import Windows.Win32.System.Com.StructuredStorage
import Windows.Win32.UI.Shell.PropertiesSystem
import Windows.Win32.UI.WindowsAndMessaging
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class ACMDRIVERDETAILSA(EasyCastStructure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    wMid: UInt16
    wPid: UInt16
    vdwACM: UInt32
    vdwDriver: UInt32
    fdwSupport: UInt32
    cFormatTags: UInt32
    cFilterTags: UInt32
    hicon: Windows.Win32.UI.WindowsAndMessaging.HICON
    szShortName: Windows.Win32.Foundation.CHAR * 32
    szLongName: Windows.Win32.Foundation.CHAR * 128
    szCopyright: Windows.Win32.Foundation.CHAR * 80
    szLicensing: Windows.Win32.Foundation.CHAR * 128
    szFeatures: Windows.Win32.Foundation.CHAR * 512
    _pack_ = 1
class ACMDRIVERDETAILSW(EasyCastStructure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    wMid: UInt16
    wPid: UInt16
    vdwACM: UInt32
    vdwDriver: UInt32
    fdwSupport: UInt32
    cFormatTags: UInt32
    cFilterTags: UInt32
    hicon: Windows.Win32.UI.WindowsAndMessaging.HICON
    szShortName: Char * 32
    szLongName: Char * 128
    szCopyright: Char * 80
    szLicensing: Char * 128
    szFeatures: Char * 512
    _pack_ = 1
@winfunctype_pointer
def ACMDRIVERENUMCB(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class ACMDRVFORMATSUGGEST(EasyCastStructure):
    cbStruct: UInt32
    fdwSuggest: UInt32
    pwfxSrc: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfxSrc: UInt32
    pwfxDst: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfxDst: UInt32
    _pack_ = 1
class ACMDRVOPENDESCA(EasyCastStructure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    dwError: UInt32
    pszSectionName: Windows.Win32.Foundation.PSTR
    pszAliasName: Windows.Win32.Foundation.PSTR
    dnDevNode: UInt32
    _pack_ = 1
class ACMDRVOPENDESCW(EasyCastStructure):
    cbStruct: UInt32
    fccType: UInt32
    fccComp: UInt32
    dwVersion: UInt32
    dwFlags: UInt32
    dwError: UInt32
    pszSectionName: Windows.Win32.Foundation.PWSTR
    pszAliasName: Windows.Win32.Foundation.PWSTR
    dnDevNode: UInt32
    _pack_ = 1
class ACMDRVSTREAMHEADER(EasyCastStructure):
    cbStruct: UInt32
    fdwStatus: UInt32
    dwUser: UIntPtr
    pbSrc: POINTER(Byte)
    cbSrcLength: UInt32
    cbSrcLengthUsed: UInt32
    dwSrcUser: UIntPtr
    pbDst: POINTER(Byte)
    cbDstLength: UInt32
    cbDstLengthUsed: UInt32
    dwDstUser: UIntPtr
    fdwConvert: UInt32
    padshNext: POINTER(Windows.Win32.Media.Audio.ACMDRVSTREAMHEADER_head)
    fdwDriver: UInt32
    dwDriver: UIntPtr
    fdwPrepared: UInt32
    dwPrepared: UIntPtr
    pbPreparedSrc: POINTER(Byte)
    cbPreparedSrcLength: UInt32
    pbPreparedDst: POINTER(Byte)
    cbPreparedDstLength: UInt32
    _pack_ = 1
class ACMDRVSTREAMINSTANCE(EasyCastStructure):
    cbStruct: UInt32
    pwfxSrc: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    pwfxDst: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    dwCallback: UIntPtr
    dwInstance: UIntPtr
    fdwOpen: UInt32
    fdwDriver: UInt32
    dwDriver: UIntPtr
    has: Windows.Win32.Media.Audio.HACMSTREAM
    _pack_ = 1
class ACMDRVSTREAMSIZE(EasyCastStructure):
    cbStruct: UInt32
    fdwSize: UInt32
    cbSrcLength: UInt32
    cbDstLength: UInt32
    _pack_ = 1
class ACMFILTERCHOOSEA(EasyCastStructure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    cbwfltr: UInt32
    pszTitle: Windows.Win32.Foundation.PSTR
    szFilterTag: Windows.Win32.Foundation.CHAR * 48
    szFilter: Windows.Win32.Foundation.CHAR * 128
    pszName: Windows.Win32.Foundation.PSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfltrEnum: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    hInstance: Windows.Win32.Foundation.HMODULE
    pszTemplateName: Windows.Win32.Foundation.PSTR
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Media.Audio.ACMFILTERCHOOSEHOOKPROCA
    _pack_ = 1
@winfunctype_pointer
def ACMFILTERCHOOSEHOOKPROCA(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def ACMFILTERCHOOSEHOOKPROCW(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
class ACMFILTERCHOOSEW(EasyCastStructure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    cbwfltr: UInt32
    pszTitle: Windows.Win32.Foundation.PWSTR
    szFilterTag: Char * 48
    szFilter: Char * 128
    pszName: Windows.Win32.Foundation.PWSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfltrEnum: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    hInstance: Windows.Win32.Foundation.HMODULE
    pszTemplateName: Windows.Win32.Foundation.PWSTR
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Media.Audio.ACMFILTERCHOOSEHOOKPROCW
    _pack_ = 1
class ACMFILTERDETAILSA(EasyCastStructure):
    cbStruct: UInt32
    dwFilterIndex: UInt32
    dwFilterTag: UInt32
    fdwSupport: UInt32
    pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    cbwfltr: UInt32
    szFilter: Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
class ACMFILTERDETAILSW(EasyCastStructure):
    cbStruct: UInt32
    dwFilterIndex: UInt32
    dwFilterTag: UInt32
    fdwSupport: UInt32
    pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head)
    cbwfltr: UInt32
    szFilter: Char * 128
    _pack_ = 1
@winfunctype_pointer
def ACMFILTERENUMCBA(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSA_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFILTERENUMCBW(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSW_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class ACMFILTERTAGDETAILSA(EasyCastStructure):
    cbStruct: UInt32
    dwFilterTagIndex: UInt32
    dwFilterTag: UInt32
    cbFilterSize: UInt32
    fdwSupport: UInt32
    cStandardFilters: UInt32
    szFilterTag: Windows.Win32.Foundation.CHAR * 48
    _pack_ = 1
class ACMFILTERTAGDETAILSW(EasyCastStructure):
    cbStruct: UInt32
    dwFilterTagIndex: UInt32
    dwFilterTag: UInt32
    cbFilterSize: UInt32
    fdwSupport: UInt32
    cStandardFilters: UInt32
    szFilterTag: Char * 48
    _pack_ = 1
@winfunctype_pointer
def ACMFILTERTAGENUMCBA(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFILTERTAGENUMCBW(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class ACMFORMATCHOOSEA(EasyCastStructure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfx: UInt32
    pszTitle: Windows.Win32.Foundation.PSTR
    szFormatTag: Windows.Win32.Foundation.CHAR * 48
    szFormat: Windows.Win32.Foundation.CHAR * 128
    pszName: Windows.Win32.Foundation.PSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfxEnum: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    hInstance: Windows.Win32.Foundation.HMODULE
    pszTemplateName: Windows.Win32.Foundation.PSTR
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Media.Audio.ACMFORMATCHOOSEHOOKPROCA
    _pack_ = 1
@winfunctype_pointer
def ACMFORMATCHOOSEHOOKPROCA(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype_pointer
def ACMFORMATCHOOSEHOOKPROCW(hwnd: Windows.Win32.Foundation.HWND, uMsg: UInt32, wParam: Windows.Win32.Foundation.WPARAM, lParam: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
class ACMFORMATCHOOSEW(EasyCastStructure):
    cbStruct: UInt32
    fdwStyle: UInt32
    hwndOwner: Windows.Win32.Foundation.HWND
    pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfx: UInt32
    pszTitle: Windows.Win32.Foundation.PWSTR
    szFormatTag: Char * 48
    szFormat: Char * 128
    pszName: Windows.Win32.Foundation.PWSTR
    cchName: UInt32
    fdwEnum: UInt32
    pwfxEnum: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    hInstance: Windows.Win32.Foundation.HMODULE
    pszTemplateName: Windows.Win32.Foundation.PWSTR
    lCustData: Windows.Win32.Foundation.LPARAM
    pfnHook: Windows.Win32.Media.Audio.ACMFORMATCHOOSEHOOKPROCW
    _pack_ = 1
class ACMFORMATDETAILSA(EasyCastStructure):
    cbStruct: UInt32
    dwFormatIndex: UInt32
    dwFormatTag: UInt32
    fdwSupport: UInt32
    pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfx: UInt32
    szFormat: Windows.Win32.Foundation.CHAR * 128
    _pack_ = 1
@winfunctype_pointer
def ACMFORMATENUMCBA(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(Windows.Win32.Media.Audio.ACMFORMATDETAILSA_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFORMATENUMCBW(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, pafd: POINTER(Windows.Win32.Media.Audio.tACMFORMATDETAILSW_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
class ACMFORMATTAGDETAILSA(EasyCastStructure):
    cbStruct: UInt32
    dwFormatTagIndex: UInt32
    dwFormatTag: UInt32
    cbFormatSize: UInt32
    fdwSupport: UInt32
    cStandardFormats: UInt32
    szFormatTag: Windows.Win32.Foundation.CHAR * 48
    _pack_ = 1
class ACMFORMATTAGDETAILSW(EasyCastStructure):
    cbStruct: UInt32
    dwFormatTagIndex: UInt32
    dwFormatTag: UInt32
    cbFormatSize: UInt32
    fdwSupport: UInt32
    cStandardFormats: UInt32
    szFormatTag: Char * 48
    _pack_ = 1
@winfunctype_pointer
def ACMFORMATTAGENUMCBA(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ACMFORMATTAGENUMCBW(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW_head), dwInstance: UIntPtr, fdwSupport: UInt32) -> Windows.Win32.Foundation.BOOL: ...
if ARCH in 'X64,ARM64':
    class ACMSTREAMHEADER(EasyCastStructure):
        cbStruct: UInt32
        fdwStatus: UInt32
        dwUser: UIntPtr
        pbSrc: POINTER(Byte)
        cbSrcLength: UInt32
        cbSrcLengthUsed: UInt32
        dwSrcUser: UIntPtr
        pbDst: POINTER(Byte)
        cbDstLength: UInt32
        cbDstLengthUsed: UInt32
        dwDstUser: UIntPtr
        dwReservedDriver: UInt32 * 15
        _pack_ = 1
if ARCH in 'X86':
    class ACMSTREAMHEADER(EasyCastStructure):
        cbStruct: UInt32
        fdwStatus: UInt32
        dwUser: UIntPtr
        pbSrc: POINTER(Byte)
        cbSrcLength: UInt32
        cbSrcLengthUsed: UInt32
        dwSrcUser: UIntPtr
        pbDst: POINTER(Byte)
        cbDstLength: UInt32
        cbDstLengthUsed: UInt32
        dwDstUser: UIntPtr
        dwReservedDriver: UInt32 * 10
        _pack_ = 1
AMBISONICS_CHANNEL_ORDERING = Int32
AMBISONICS_CHANNEL_ORDERING_ACN: AMBISONICS_CHANNEL_ORDERING = 0
AMBISONICS_NORMALIZATION = Int32
AMBISONICS_NORMALIZATION_SN3D: AMBISONICS_NORMALIZATION = 0
AMBISONICS_NORMALIZATION_N3D: AMBISONICS_NORMALIZATION = 1
class AMBISONICS_PARAMS(EasyCastStructure):
    u32Size: UInt32
    u32Version: UInt32
    u32Type: Windows.Win32.Media.Audio.AMBISONICS_TYPE
    u32ChannelOrdering: Windows.Win32.Media.Audio.AMBISONICS_CHANNEL_ORDERING
    u32Normalization: Windows.Win32.Media.Audio.AMBISONICS_NORMALIZATION
    u32Order: UInt32
    u32NumChannels: UInt32
    pu32ChannelMap: POINTER(UInt32)
AMBISONICS_TYPE = Int32
AMBISONICS_TYPE_FULL3D: AMBISONICS_TYPE = 0
AUDCLNT_SHAREMODE = Int32
AUDCLNT_SHAREMODE_SHARED: AUDCLNT_SHAREMODE = 0
AUDCLNT_SHAREMODE_EXCLUSIVE: AUDCLNT_SHAREMODE = 1
AUDCLNT_STREAMOPTIONS = Int32
AUDCLNT_STREAMOPTIONS_NONE: AUDCLNT_STREAMOPTIONS = 0
AUDCLNT_STREAMOPTIONS_RAW: AUDCLNT_STREAMOPTIONS = 1
AUDCLNT_STREAMOPTIONS_MATCH_FORMAT: AUDCLNT_STREAMOPTIONS = 2
AUDCLNT_STREAMOPTIONS_AMBISONICS: AUDCLNT_STREAMOPTIONS = 4
class AUDIOCLIENT_ACTIVATION_PARAMS(EasyCastStructure):
    ActivationType: Windows.Win32.Media.Audio.AUDIOCLIENT_ACTIVATION_TYPE
    Anonymous: _Anonymous_e__Union
    class _Anonymous_e__Union(EasyCastUnion):
        ProcessLoopbackParams: Windows.Win32.Media.Audio.AUDIOCLIENT_PROCESS_LOOPBACK_PARAMS
AUDIOCLIENT_ACTIVATION_TYPE = Int32
AUDIOCLIENT_ACTIVATION_TYPE_DEFAULT: AUDIOCLIENT_ACTIVATION_TYPE = 0
AUDIOCLIENT_ACTIVATION_TYPE_PROCESS_LOOPBACK: AUDIOCLIENT_ACTIVATION_TYPE = 1
class AUDIOCLIENT_PROCESS_LOOPBACK_PARAMS(EasyCastStructure):
    TargetProcessId: UInt32
    ProcessLoopbackMode: Windows.Win32.Media.Audio.PROCESS_LOOPBACK_MODE
AUDIO_DUCKING_OPTIONS = Int32
AUDIO_DUCKING_OPTIONS_DEFAULT: AUDIO_DUCKING_OPTIONS = 0
AUDIO_DUCKING_OPTIONS_DO_NOT_DUCK_OTHER_STREAMS: AUDIO_DUCKING_OPTIONS = 1
class AUDIO_EFFECT(EasyCastStructure):
    id: Guid
    canSetState: Windows.Win32.Foundation.BOOL
    state: Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE
AUDIO_EFFECT_STATE = Int32
AUDIO_EFFECT_STATE_OFF: AUDIO_EFFECT_STATE = 0
AUDIO_EFFECT_STATE_ON: AUDIO_EFFECT_STATE = 1
AUDIO_STREAM_CATEGORY = Int32
AudioCategory_Other: AUDIO_STREAM_CATEGORY = 0
AudioCategory_ForegroundOnlyMedia: AUDIO_STREAM_CATEGORY = 1
AudioCategory_Communications: AUDIO_STREAM_CATEGORY = 3
AudioCategory_Alerts: AUDIO_STREAM_CATEGORY = 4
AudioCategory_SoundEffects: AUDIO_STREAM_CATEGORY = 5
AudioCategory_GameEffects: AUDIO_STREAM_CATEGORY = 6
AudioCategory_GameMedia: AUDIO_STREAM_CATEGORY = 7
AudioCategory_GameChat: AUDIO_STREAM_CATEGORY = 8
AudioCategory_Speech: AUDIO_STREAM_CATEGORY = 9
AudioCategory_Movie: AUDIO_STREAM_CATEGORY = 10
AudioCategory_Media: AUDIO_STREAM_CATEGORY = 11
AudioCategory_FarFieldSpeech: AUDIO_STREAM_CATEGORY = 12
AudioCategory_UniformSpeech: AUDIO_STREAM_CATEGORY = 13
AudioCategory_VoiceTyping: AUDIO_STREAM_CATEGORY = 14
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = Int32
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_DEFAULT: AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 0
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_USER: AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 1
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_VOLATILE: AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 2
AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE_ENUM_COUNT: AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE = 3
class AUDIO_VOLUME_NOTIFICATION_DATA(EasyCastStructure):
    guidEventContext: Guid
    bMuted: Windows.Win32.Foundation.BOOL
    fMasterVolume: Single
    nChannels: UInt32
    afChannelVolumes: Single * 1
class AUXCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class AUXCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class AUXCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
class AUXCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
MIXERCONTROL_CONTROLTYPE_CUSTOM: UInt32 = 0
MIXERCONTROL_CONTROLTYPE_BOOLEANMETER: UInt32 = 268500992
MIXERCONTROL_CONTROLTYPE_SIGNEDMETER: UInt32 = 268566528
MIXERCONTROL_CONTROLTYPE_PEAKMETER: UInt32 = 268566529
MIXERCONTROL_CONTROLTYPE_UNSIGNEDMETER: UInt32 = 268632064
MIXERCONTROL_CONTROLTYPE_BOOLEAN: UInt32 = 536936448
MIXERCONTROL_CONTROLTYPE_ONOFF: UInt32 = 536936449
MIXERCONTROL_CONTROLTYPE_MUTE: UInt32 = 536936450
MIXERCONTROL_CONTROLTYPE_MONO: UInt32 = 536936451
MIXERCONTROL_CONTROLTYPE_LOUDNESS: UInt32 = 536936452
MIXERCONTROL_CONTROLTYPE_STEREOENH: UInt32 = 536936453
MIXERCONTROL_CONTROLTYPE_BASS_BOOST: UInt32 = 536945271
MIXERCONTROL_CONTROLTYPE_BUTTON: UInt32 = 553713664
MIXERCONTROL_CONTROLTYPE_DECIBELS: UInt32 = 805568512
MIXERCONTROL_CONTROLTYPE_SIGNED: UInt32 = 805437440
MIXERCONTROL_CONTROLTYPE_UNSIGNED: UInt32 = 805502976
MIXERCONTROL_CONTROLTYPE_PERCENT: UInt32 = 805634048
MIXERCONTROL_CONTROLTYPE_SLIDER: UInt32 = 1073872896
MIXERCONTROL_CONTROLTYPE_PAN: UInt32 = 1073872897
MIXERCONTROL_CONTROLTYPE_QSOUNDPAN: UInt32 = 1073872898
MIXERCONTROL_CONTROLTYPE_FADER: UInt32 = 1342373888
MIXERCONTROL_CONTROLTYPE_VOLUME: UInt32 = 1342373889
MIXERCONTROL_CONTROLTYPE_BASS: UInt32 = 1342373890
MIXERCONTROL_CONTROLTYPE_TREBLE: UInt32 = 1342373891
MIXERCONTROL_CONTROLTYPE_EQUALIZER: UInt32 = 1342373892
MIXERCONTROL_CONTROLTYPE_SINGLESELECT: UInt32 = 1879113728
MIXERCONTROL_CONTROLTYPE_MUX: UInt32 = 1879113729
MIXERCONTROL_CONTROLTYPE_MULTIPLESELECT: UInt32 = 1895890944
MIXERCONTROL_CONTROLTYPE_MIXER: UInt32 = 1895890945
MIXERCONTROL_CONTROLTYPE_MICROTIME: UInt32 = 1610809344
MIXERCONTROL_CONTROLTYPE_MILLITIME: UInt32 = 1627586560
WAVE_MAPPER: UInt32 = 4294967295
ENDPOINT_FORMAT_RESET_MIX_ONLY: UInt32 = 1
ENDPOINT_HARDWARE_SUPPORT_VOLUME: UInt32 = 1
ENDPOINT_HARDWARE_SUPPORT_MUTE: UInt32 = 2
ENDPOINT_HARDWARE_SUPPORT_METER: UInt32 = 4
AUDIOCLOCK_CHARACTERISTIC_FIXED_FREQ: UInt32 = 1
AMBISONICS_PARAM_VERSION_1: UInt32 = 1
AUDCLNT_E_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2004287487
AUDCLNT_E_ALREADY_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2004287486
AUDCLNT_E_WRONG_ENDPOINT_TYPE: Windows.Win32.Foundation.HRESULT = -2004287485
AUDCLNT_E_DEVICE_INVALIDATED: Windows.Win32.Foundation.HRESULT = -2004287484
AUDCLNT_E_NOT_STOPPED: Windows.Win32.Foundation.HRESULT = -2004287483
AUDCLNT_E_BUFFER_TOO_LARGE: Windows.Win32.Foundation.HRESULT = -2004287482
AUDCLNT_E_OUT_OF_ORDER: Windows.Win32.Foundation.HRESULT = -2004287481
AUDCLNT_E_UNSUPPORTED_FORMAT: Windows.Win32.Foundation.HRESULT = -2004287480
AUDCLNT_E_INVALID_SIZE: Windows.Win32.Foundation.HRESULT = -2004287479
AUDCLNT_E_DEVICE_IN_USE: Windows.Win32.Foundation.HRESULT = -2004287478
AUDCLNT_E_BUFFER_OPERATION_PENDING: Windows.Win32.Foundation.HRESULT = -2004287477
AUDCLNT_E_THREAD_NOT_REGISTERED: Windows.Win32.Foundation.HRESULT = -2004287476
AUDCLNT_E_EXCLUSIVE_MODE_NOT_ALLOWED: Windows.Win32.Foundation.HRESULT = -2004287474
AUDCLNT_E_ENDPOINT_CREATE_FAILED: Windows.Win32.Foundation.HRESULT = -2004287473
AUDCLNT_E_SERVICE_NOT_RUNNING: Windows.Win32.Foundation.HRESULT = -2004287472
AUDCLNT_E_EVENTHANDLE_NOT_EXPECTED: Windows.Win32.Foundation.HRESULT = -2004287471
AUDCLNT_E_EXCLUSIVE_MODE_ONLY: Windows.Win32.Foundation.HRESULT = -2004287470
AUDCLNT_E_BUFDURATION_PERIOD_NOT_EQUAL: Windows.Win32.Foundation.HRESULT = -2004287469
AUDCLNT_E_EVENTHANDLE_NOT_SET: Windows.Win32.Foundation.HRESULT = -2004287468
AUDCLNT_E_INCORRECT_BUFFER_SIZE: Windows.Win32.Foundation.HRESULT = -2004287467
AUDCLNT_E_BUFFER_SIZE_ERROR: Windows.Win32.Foundation.HRESULT = -2004287466
AUDCLNT_E_CPUUSAGE_EXCEEDED: Windows.Win32.Foundation.HRESULT = -2004287465
AUDCLNT_E_BUFFER_ERROR: Windows.Win32.Foundation.HRESULT = -2004287464
AUDCLNT_E_BUFFER_SIZE_NOT_ALIGNED: Windows.Win32.Foundation.HRESULT = -2004287463
AUDCLNT_E_INVALID_DEVICE_PERIOD: Windows.Win32.Foundation.HRESULT = -2004287456
AUDCLNT_E_INVALID_STREAM_FLAG: Windows.Win32.Foundation.HRESULT = -2004287455
AUDCLNT_E_ENDPOINT_OFFLOAD_NOT_CAPABLE: Windows.Win32.Foundation.HRESULT = -2004287454
AUDCLNT_E_OUT_OF_OFFLOAD_RESOURCES: Windows.Win32.Foundation.HRESULT = -2004287453
AUDCLNT_E_OFFLOAD_MODE_ONLY: Windows.Win32.Foundation.HRESULT = -2004287452
AUDCLNT_E_NONOFFLOAD_MODE_ONLY: Windows.Win32.Foundation.HRESULT = -2004287451
AUDCLNT_E_RESOURCES_INVALIDATED: Windows.Win32.Foundation.HRESULT = -2004287450
AUDCLNT_E_RAW_MODE_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -2004287449
AUDCLNT_E_ENGINE_PERIODICITY_LOCKED: Windows.Win32.Foundation.HRESULT = -2004287448
AUDCLNT_E_ENGINE_FORMAT_LOCKED: Windows.Win32.Foundation.HRESULT = -2004287447
AUDCLNT_E_HEADTRACKING_ENABLED: Windows.Win32.Foundation.HRESULT = -2004287440
AUDCLNT_E_HEADTRACKING_UNSUPPORTED: Windows.Win32.Foundation.HRESULT = -2004287424
AUDCLNT_E_EFFECT_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2004287423
AUDCLNT_E_EFFECT_STATE_READ_ONLY: Windows.Win32.Foundation.HRESULT = -2004287422
AUDCLNT_S_BUFFER_EMPTY: Windows.Win32.Foundation.HRESULT = 143196161
AUDCLNT_S_THREAD_ALREADY_REGISTERED: Windows.Win32.Foundation.HRESULT = 143196162
AUDCLNT_S_POSITION_STALLED: Windows.Win32.Foundation.HRESULT = 143196163
AUDCLNT_STREAMFLAGS_CROSSPROCESS: UInt32 = 65536
AUDCLNT_STREAMFLAGS_LOOPBACK: UInt32 = 131072
AUDCLNT_STREAMFLAGS_EVENTCALLBACK: UInt32 = 262144
AUDCLNT_STREAMFLAGS_NOPERSIST: UInt32 = 524288
AUDCLNT_STREAMFLAGS_RATEADJUST: UInt32 = 1048576
AUDCLNT_STREAMFLAGS_SRC_DEFAULT_QUALITY: UInt32 = 134217728
AUDCLNT_STREAMFLAGS_AUTOCONVERTPCM: UInt32 = 2147483648
AUDCLNT_SESSIONFLAGS_EXPIREWHENUNOWNED: UInt32 = 268435456
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDE: UInt32 = 536870912
AUDCLNT_SESSIONFLAGS_DISPLAY_HIDEWHENEXPIRED: UInt32 = 1073741824
SPTLAUDCLNT_E_DESTROYED: Windows.Win32.Foundation.HRESULT = -2004287232
SPTLAUDCLNT_E_OUT_OF_ORDER: Windows.Win32.Foundation.HRESULT = -2004287231
SPTLAUDCLNT_E_RESOURCES_INVALIDATED: Windows.Win32.Foundation.HRESULT = -2004287230
SPTLAUDCLNT_E_NO_MORE_OBJECTS: Windows.Win32.Foundation.HRESULT = -2004287229
SPTLAUDCLNT_E_PROPERTY_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2004287228
SPTLAUDCLNT_E_ERRORS_IN_OBJECT_CALLS: Windows.Win32.Foundation.HRESULT = -2004287227
SPTLAUDCLNT_E_METADATA_FORMAT_NOT_SUPPORTED: Windows.Win32.Foundation.HRESULT = -2004287226
SPTLAUDCLNT_E_STREAM_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2004287225
SPTLAUDCLNT_E_INVALID_LICENSE: Windows.Win32.Foundation.HRESULT = -2004287224
SPTLAUDCLNT_E_STREAM_NOT_STOPPED: Windows.Win32.Foundation.HRESULT = -2004287222
SPTLAUDCLNT_E_STATIC_OBJECT_NOT_AVAILABLE: Windows.Win32.Foundation.HRESULT = -2004287221
SPTLAUDCLNT_E_OBJECT_ALREADY_ACTIVE: Windows.Win32.Foundation.HRESULT = -2004287220
SPTLAUDCLNT_E_INTERNAL: Windows.Win32.Foundation.HRESULT = -2004287219
DEVICE_STATE_ACTIVE: UInt32 = 1
DEVICE_STATE_DISABLED: UInt32 = 2
DEVICE_STATE_NOTPRESENT: UInt32 = 4
DEVICE_STATE_UNPLUGGED: UInt32 = 8
DEVICE_STATEMASK_ALL: UInt32 = 15
def PKEY_AudioEndpoint_FormFactor():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=0)
def PKEY_AudioEndpoint_ControlPanelPageProvider():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=1)
def PKEY_AudioEndpoint_Association():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=2)
def PKEY_AudioEndpoint_PhysicalSpeakers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=3)
def PKEY_AudioEndpoint_GUID():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=4)
def PKEY_AudioEndpoint_Disable_SysFx():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=5)
ENDPOINT_SYSFX_ENABLED: UInt32 = 0
ENDPOINT_SYSFX_DISABLED: UInt32 = 1
def PKEY_AudioEndpoint_FullRangeSpeakers():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=6)
def PKEY_AudioEndpoint_Supports_EventDriven_Mode():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=7)
def PKEY_AudioEndpoint_JackSubType():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=8)
def PKEY_AudioEndpoint_Default_VolumeInDb():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('1da5d803-d492-4edd-8c-23-e0-c0-ff-ee-7f-0e'), pid=9)
def PKEY_AudioEngine_DeviceFormat():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f19f064d-082c-4e27-bc-73-68-82-a1-bb-8e-4c'), pid=0)
def PKEY_AudioEngine_OEMFormat():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('e4870e26-3cc5-4cd2-ba-46-ca-0a-9a-70-ed-04'), pid=3)
def PKEY_AudioEndpointLogo_IconEffects():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f1ab780d-2010-4ed3-a3-a6-8b-87-f0-f0-c4-76'), pid=0)
def PKEY_AudioEndpointLogo_IconPath():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('f1ab780d-2010-4ed3-a3-a6-8b-87-f0-f0-c4-76'), pid=1)
def PKEY_AudioEndpointSettings_MenuText():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14242002-0320-4de4-95-55-a7-d8-2b-73-c2-86'), pid=0)
def PKEY_AudioEndpointSettings_LaunchContract():
    return Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY(fmtid=Guid('14242002-0320-4de4-95-55-a7-d8-2b-73-c2-86'), pid=1)
DEVINTERFACE_AUDIO_RENDER: Guid = Guid('e6327cad-dcec-4949-ae-8a-99-1e-97-6a-79-d2')
DEVINTERFACE_AUDIO_CAPTURE: Guid = Guid('2eef81be-33fa-4800-96-70-1c-d4-74-97-2c-3f')
DEVINTERFACE_MIDI_OUTPUT: Guid = Guid('6dc23320-ab33-4ce4-80-d4-bb-b3-eb-bf-28-14')
DEVINTERFACE_MIDI_INPUT: Guid = Guid('504be32c-ccf6-4d2c-b7-3f-6f-8b-37-47-e2-2b')
EVENTCONTEXT_VOLUMESLIDER: Guid = Guid('e2c2e9de-09b1-4b04-84-e5-07-93-12-25-ee-04')
SPATIAL_AUDIO_STANDARD_COMMANDS_START: UInt32 = 200
SPATIAL_AUDIO_POSITION: UInt32 = 200
SPTLAUD_MD_CLNT_E_COMMAND_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2004286976
SPTLAUD_MD_CLNT_E_OBJECT_NOT_INITIALIZED: Windows.Win32.Foundation.HRESULT = -2004286975
SPTLAUD_MD_CLNT_E_INVALID_ARGS: Windows.Win32.Foundation.HRESULT = -2004286974
SPTLAUD_MD_CLNT_E_METADATA_FORMAT_NOT_FOUND: Windows.Win32.Foundation.HRESULT = -2004286973
SPTLAUD_MD_CLNT_E_VALUE_BUFFER_INCORRECT_SIZE: Windows.Win32.Foundation.HRESULT = -2004286972
SPTLAUD_MD_CLNT_E_MEMORY_BOUNDS: Windows.Win32.Foundation.HRESULT = -2004286971
SPTLAUD_MD_CLNT_E_NO_MORE_COMMANDS: Windows.Win32.Foundation.HRESULT = -2004286970
SPTLAUD_MD_CLNT_E_BUFFER_ALREADY_ATTACHED: Windows.Win32.Foundation.HRESULT = -2004286969
SPTLAUD_MD_CLNT_E_BUFFER_NOT_ATTACHED: Windows.Win32.Foundation.HRESULT = -2004286968
SPTLAUD_MD_CLNT_E_FRAMECOUNT_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -2004286967
SPTLAUD_MD_CLNT_E_NO_ITEMS_FOUND: Windows.Win32.Foundation.HRESULT = -2004286960
SPTLAUD_MD_CLNT_E_ITEM_COPY_OVERFLOW: Windows.Win32.Foundation.HRESULT = -2004286959
SPTLAUD_MD_CLNT_E_NO_ITEMS_OPEN: Windows.Win32.Foundation.HRESULT = -2004286958
SPTLAUD_MD_CLNT_E_ITEMS_ALREADY_OPEN: Windows.Win32.Foundation.HRESULT = -2004286957
SPTLAUD_MD_CLNT_E_ATTACH_FAILED_INTERNAL_BUFFER: Windows.Win32.Foundation.HRESULT = -2004286956
SPTLAUD_MD_CLNT_E_DETACH_FAILED_INTERNAL_BUFFER: Windows.Win32.Foundation.HRESULT = -2004286955
SPTLAUD_MD_CLNT_E_NO_BUFFER_ATTACHED: Windows.Win32.Foundation.HRESULT = -2004286954
SPTLAUD_MD_CLNT_E_NO_MORE_ITEMS: Windows.Win32.Foundation.HRESULT = -2004286953
SPTLAUD_MD_CLNT_E_FRAMEOFFSET_OUT_OF_RANGE: Windows.Win32.Foundation.HRESULT = -2004286952
SPTLAUD_MD_CLNT_E_ITEM_MUST_HAVE_COMMANDS: Windows.Win32.Foundation.HRESULT = -2004286951
SPTLAUD_MD_CLNT_E_NO_ITEMOFFSET_WRITTEN: Windows.Win32.Foundation.HRESULT = -2004286944
SPTLAUD_MD_CLNT_E_NO_ITEMS_WRITTEN: Windows.Win32.Foundation.HRESULT = -2004286943
SPTLAUD_MD_CLNT_E_COMMAND_ALREADY_WRITTEN: Windows.Win32.Foundation.HRESULT = -2004286942
SPTLAUD_MD_CLNT_E_FORMAT_MISMATCH: Windows.Win32.Foundation.HRESULT = -2004286941
SPTLAUD_MD_CLNT_E_BUFFER_STILL_ATTACHED: Windows.Win32.Foundation.HRESULT = -2004286940
SPTLAUD_MD_CLNT_E_ITEMS_LOCKED_FOR_WRITING: Windows.Win32.Foundation.HRESULT = -2004286939
VIRTUAL_AUDIO_DEVICE_PROCESS_LOOPBACK: String = 'VAD\\Process_Loopback'
WAVERR_BADFORMAT: UInt32 = 32
WAVERR_STILLPLAYING: UInt32 = 33
WAVERR_UNPREPARED: UInt32 = 34
WAVERR_SYNC: UInt32 = 35
WAVERR_LASTERROR: UInt32 = 35
WHDR_DONE: UInt32 = 1
WHDR_PREPARED: UInt32 = 2
WHDR_BEGINLOOP: UInt32 = 4
WHDR_ENDLOOP: UInt32 = 8
WHDR_INQUEUE: UInt32 = 16
WAVECAPS_PITCH: UInt32 = 1
WAVECAPS_PLAYBACKRATE: UInt32 = 2
WAVECAPS_VOLUME: UInt32 = 4
WAVECAPS_LRVOLUME: UInt32 = 8
WAVECAPS_SYNC: UInt32 = 16
WAVECAPS_SAMPLEACCURATE: UInt32 = 32
WAVE_INVALIDFORMAT: UInt32 = 0
WAVE_FORMAT_1M08: UInt32 = 1
WAVE_FORMAT_1S08: UInt32 = 2
WAVE_FORMAT_1M16: UInt32 = 4
WAVE_FORMAT_1S16: UInt32 = 8
WAVE_FORMAT_2M08: UInt32 = 16
WAVE_FORMAT_2S08: UInt32 = 32
WAVE_FORMAT_2M16: UInt32 = 64
WAVE_FORMAT_2S16: UInt32 = 128
WAVE_FORMAT_4M08: UInt32 = 256
WAVE_FORMAT_4S08: UInt32 = 512
WAVE_FORMAT_4M16: UInt32 = 1024
WAVE_FORMAT_4S16: UInt32 = 2048
WAVE_FORMAT_44M08: UInt32 = 256
WAVE_FORMAT_44S08: UInt32 = 512
WAVE_FORMAT_44M16: UInt32 = 1024
WAVE_FORMAT_44S16: UInt32 = 2048
WAVE_FORMAT_48M08: UInt32 = 4096
WAVE_FORMAT_48S08: UInt32 = 8192
WAVE_FORMAT_48M16: UInt32 = 16384
WAVE_FORMAT_48S16: UInt32 = 32768
WAVE_FORMAT_96M08: UInt32 = 65536
WAVE_FORMAT_96S08: UInt32 = 131072
WAVE_FORMAT_96M16: UInt32 = 262144
WAVE_FORMAT_96S16: UInt32 = 524288
WAVE_FORMAT_PCM: UInt32 = 1
MIDIERR_UNPREPARED: UInt32 = 64
MIDIERR_STILLPLAYING: UInt32 = 65
MIDIERR_NOMAP: UInt32 = 66
MIDIERR_NOTREADY: UInt32 = 67
MIDIERR_NODEVICE: UInt32 = 68
MIDIERR_INVALIDSETUP: UInt32 = 69
MIDIERR_BADOPENMODE: UInt32 = 70
MIDIERR_DONT_CONTINUE: UInt32 = 71
MIDIERR_LASTERROR: UInt32 = 71
MIDIPATCHSIZE: UInt32 = 128
MIDI_CACHE_ALL: UInt32 = 1
MIDI_CACHE_BESTFIT: UInt32 = 2
MIDI_CACHE_QUERY: UInt32 = 3
MIDI_UNCACHE: UInt32 = 4
MOD_MIDIPORT: UInt32 = 1
MOD_SYNTH: UInt32 = 2
MOD_SQSYNTH: UInt32 = 3
MOD_FMSYNTH: UInt32 = 4
MOD_MAPPER: UInt32 = 5
MOD_WAVETABLE: UInt32 = 6
MOD_SWSYNTH: UInt32 = 7
MIDICAPS_VOLUME: UInt32 = 1
MIDICAPS_LRVOLUME: UInt32 = 2
MIDICAPS_CACHE: UInt32 = 4
MIDICAPS_STREAM: UInt32 = 8
MHDR_DONE: UInt32 = 1
MHDR_PREPARED: UInt32 = 2
MHDR_INQUEUE: UInt32 = 4
MHDR_ISSTRM: UInt32 = 8
MEVT_F_SHORT: Int32 = 0
MEVT_F_LONG: Int32 = -2147483648
MEVT_F_CALLBACK: Int32 = 1073741824
MIDISTRM_ERROR: Int32 = -2
MIDIPROP_SET: Int32 = -2147483648
MIDIPROP_GET: Int32 = 1073741824
MIDIPROP_TIMEDIV: Int32 = 1
MIDIPROP_TEMPO: Int32 = 2
AUXCAPS_CDAUDIO: UInt32 = 1
AUXCAPS_AUXIN: UInt32 = 2
AUXCAPS_VOLUME: UInt32 = 1
AUXCAPS_LRVOLUME: UInt32 = 2
MIXER_SHORT_NAME_CHARS: UInt32 = 16
MIXER_LONG_NAME_CHARS: UInt32 = 64
MIXERR_INVALLINE: UInt32 = 1024
MIXERR_INVALCONTROL: UInt32 = 1025
MIXERR_INVALVALUE: UInt32 = 1026
MIXERR_LASTERROR: UInt32 = 1026
MIXER_OBJECTF_HANDLE: Int32 = -2147483648
MIXER_OBJECTF_MIXER: Int32 = 0
MIXER_OBJECTF_WAVEOUT: Int32 = 268435456
MIXER_OBJECTF_WAVEIN: Int32 = 536870912
MIXER_OBJECTF_MIDIOUT: Int32 = 805306368
MIXER_OBJECTF_MIDIIN: Int32 = 1073741824
MIXER_OBJECTF_AUX: Int32 = 1342177280
MIXERLINE_LINEF_ACTIVE: Int32 = 1
MIXERLINE_LINEF_DISCONNECTED: Int32 = 32768
MIXERLINE_LINEF_SOURCE: Int32 = -2147483648
MIXERLINE_COMPONENTTYPE_DST_FIRST: Int32 = 0
MIXERLINE_COMPONENTTYPE_DST_LAST: UInt32 = 8
MIXERLINE_COMPONENTTYPE_SRC_FIRST: Int32 = 4096
MIXERLINE_COMPONENTTYPE_SRC_LAST: UInt32 = 4106
MIXERLINE_TARGETTYPE_UNDEFINED: UInt32 = 0
MIXERLINE_TARGETTYPE_WAVEOUT: UInt32 = 1
MIXERLINE_TARGETTYPE_WAVEIN: UInt32 = 2
MIXERLINE_TARGETTYPE_MIDIOUT: UInt32 = 3
MIXERLINE_TARGETTYPE_MIDIIN: UInt32 = 4
MIXERLINE_TARGETTYPE_AUX: UInt32 = 5
MIXER_GETLINEINFOF_DESTINATION: Int32 = 0
MIXER_GETLINEINFOF_SOURCE: Int32 = 1
MIXER_GETLINEINFOF_LINEID: Int32 = 2
MIXER_GETLINEINFOF_COMPONENTTYPE: Int32 = 3
MIXER_GETLINEINFOF_TARGETTYPE: Int32 = 4
MIXER_GETLINEINFOF_QUERYMASK: Int32 = 15
MIXERCONTROL_CONTROLF_UNIFORM: Int32 = 1
MIXERCONTROL_CONTROLF_MULTIPLE: Int32 = 2
MIXERCONTROL_CONTROLF_DISABLED: Int32 = -2147483648
MIXERCONTROL_CT_CLASS_MASK: Int32 = -268435456
MIXERCONTROL_CT_CLASS_CUSTOM: Int32 = 0
MIXERCONTROL_CT_CLASS_METER: Int32 = 268435456
MIXERCONTROL_CT_CLASS_SWITCH: Int32 = 536870912
MIXERCONTROL_CT_CLASS_NUMBER: Int32 = 805306368
MIXERCONTROL_CT_CLASS_SLIDER: Int32 = 1073741824
MIXERCONTROL_CT_CLASS_FADER: Int32 = 1342177280
MIXERCONTROL_CT_CLASS_TIME: Int32 = 1610612736
MIXERCONTROL_CT_CLASS_LIST: Int32 = 1879048192
MIXERCONTROL_CT_SUBCLASS_MASK: Int32 = 251658240
MIXERCONTROL_CT_SC_SWITCH_BOOLEAN: Int32 = 0
MIXERCONTROL_CT_SC_SWITCH_BUTTON: Int32 = 16777216
MIXERCONTROL_CT_SC_METER_POLLED: Int32 = 0
MIXERCONTROL_CT_SC_TIME_MICROSECS: Int32 = 0
MIXERCONTROL_CT_SC_TIME_MILLISECS: Int32 = 16777216
MIXERCONTROL_CT_SC_LIST_SINGLE: Int32 = 0
MIXERCONTROL_CT_SC_LIST_MULTIPLE: Int32 = 16777216
MIXERCONTROL_CT_UNITS_MASK: Int32 = 16711680
MIXERCONTROL_CT_UNITS_CUSTOM: Int32 = 0
MIXERCONTROL_CT_UNITS_BOOLEAN: Int32 = 65536
MIXERCONTROL_CT_UNITS_SIGNED: Int32 = 131072
MIXERCONTROL_CT_UNITS_UNSIGNED: Int32 = 196608
MIXERCONTROL_CT_UNITS_DECIBELS: Int32 = 262144
MIXERCONTROL_CT_UNITS_PERCENT: Int32 = 327680
MIXER_GETLINECONTROLSF_ALL: Int32 = 0
MIXER_GETLINECONTROLSF_ONEBYID: Int32 = 1
MIXER_GETLINECONTROLSF_ONEBYTYPE: Int32 = 2
MIXER_GETLINECONTROLSF_QUERYMASK: Int32 = 15
MIXER_GETCONTROLDETAILSF_VALUE: Int32 = 0
MIXER_GETCONTROLDETAILSF_LISTTEXT: Int32 = 1
MIXER_GETCONTROLDETAILSF_QUERYMASK: Int32 = 15
MIXER_SETCONTROLDETAILSF_VALUE: Int32 = 0
MIXER_SETCONTROLDETAILSF_CUSTOM: Int32 = 1
MIXER_SETCONTROLDETAILSF_QUERYMASK: Int32 = 15
DRV_MAPPER_PREFERRED_INPUT_GET: UInt32 = 16384
DRV_MAPPER_PREFERRED_OUTPUT_GET: UInt32 = 16386
DRVM_MAPPER: UInt32 = 8192
DRVM_MAPPER_STATUS: UInt32 = 8192
WIDM_MAPPER_STATUS: UInt32 = 8192
WAVEIN_MAPPER_STATUS_DEVICE: UInt32 = 0
WAVEIN_MAPPER_STATUS_MAPPED: UInt32 = 1
WAVEIN_MAPPER_STATUS_FORMAT: UInt32 = 2
WODM_MAPPER_STATUS: UInt32 = 8192
WAVEOUT_MAPPER_STATUS_DEVICE: UInt32 = 0
WAVEOUT_MAPPER_STATUS_MAPPED: UInt32 = 1
WAVEOUT_MAPPER_STATUS_FORMAT: UInt32 = 2
ACMERR_BASE: UInt32 = 512
ACMERR_NOTPOSSIBLE: UInt32 = 512
ACMERR_BUSY: UInt32 = 513
ACMERR_UNPREPARED: UInt32 = 514
ACMERR_CANCELED: UInt32 = 515
ACM_METRIC_COUNT_DRIVERS: UInt32 = 1
ACM_METRIC_COUNT_CODECS: UInt32 = 2
ACM_METRIC_COUNT_CONVERTERS: UInt32 = 3
ACM_METRIC_COUNT_FILTERS: UInt32 = 4
ACM_METRIC_COUNT_DISABLED: UInt32 = 5
ACM_METRIC_COUNT_HARDWARE: UInt32 = 6
ACM_METRIC_COUNT_LOCAL_DRIVERS: UInt32 = 20
ACM_METRIC_COUNT_LOCAL_CODECS: UInt32 = 21
ACM_METRIC_COUNT_LOCAL_CONVERTERS: UInt32 = 22
ACM_METRIC_COUNT_LOCAL_FILTERS: UInt32 = 23
ACM_METRIC_COUNT_LOCAL_DISABLED: UInt32 = 24
ACM_METRIC_HARDWARE_WAVE_INPUT: UInt32 = 30
ACM_METRIC_HARDWARE_WAVE_OUTPUT: UInt32 = 31
ACM_METRIC_MAX_SIZE_FORMAT: UInt32 = 50
ACM_METRIC_MAX_SIZE_FILTER: UInt32 = 51
ACM_METRIC_DRIVER_SUPPORT: UInt32 = 100
ACM_METRIC_DRIVER_PRIORITY: UInt32 = 101
ACM_DRIVERENUMF_NOLOCAL: Int32 = 1073741824
ACM_DRIVERENUMF_DISABLED: Int32 = -2147483648
ACM_DRIVERADDF_NAME: Int32 = 1
ACM_DRIVERADDF_FUNCTION: Int32 = 3
ACM_DRIVERADDF_NOTIFYHWND: Int32 = 4
ACM_DRIVERADDF_TYPEMASK: Int32 = 7
ACM_DRIVERADDF_LOCAL: Int32 = 0
ACM_DRIVERADDF_GLOBAL: Int32 = 8
ACMDM_USER: UInt32 = 16384
ACMDM_RESERVED_LOW: UInt32 = 24576
ACMDM_RESERVED_HIGH: UInt32 = 28671
ACMDM_DRIVER_ABOUT: UInt32 = 24587
ACM_DRIVERPRIORITYF_ENABLE: Int32 = 1
ACM_DRIVERPRIORITYF_DISABLE: Int32 = 2
ACM_DRIVERPRIORITYF_ABLEMASK: Int32 = 3
ACM_DRIVERPRIORITYF_BEGIN: Int32 = 65536
ACM_DRIVERPRIORITYF_END: Int32 = 131072
ACM_DRIVERPRIORITYF_DEFERMASK: Int32 = 196608
ACMDRIVERDETAILS_SHORTNAME_CHARS: UInt32 = 32
ACMDRIVERDETAILS_LONGNAME_CHARS: UInt32 = 128
ACMDRIVERDETAILS_COPYRIGHT_CHARS: UInt32 = 80
ACMDRIVERDETAILS_LICENSING_CHARS: UInt32 = 128
ACMDRIVERDETAILS_FEATURES_CHARS: UInt32 = 512
ACMDRIVERDETAILS_SUPPORTF_CODEC: Int32 = 1
ACMDRIVERDETAILS_SUPPORTF_CONVERTER: Int32 = 2
ACMDRIVERDETAILS_SUPPORTF_FILTER: Int32 = 4
ACMDRIVERDETAILS_SUPPORTF_HARDWARE: Int32 = 8
ACMDRIVERDETAILS_SUPPORTF_ASYNC: Int32 = 16
ACMDRIVERDETAILS_SUPPORTF_LOCAL: Int32 = 1073741824
ACMDRIVERDETAILS_SUPPORTF_DISABLED: Int32 = -2147483648
ACMFORMATTAGDETAILS_FORMATTAG_CHARS: UInt32 = 48
ACM_FORMATTAGDETAILSF_INDEX: Int32 = 0
ACM_FORMATTAGDETAILSF_FORMATTAG: Int32 = 1
ACM_FORMATTAGDETAILSF_LARGESTSIZE: Int32 = 2
ACM_FORMATTAGDETAILSF_QUERYMASK: Int32 = 15
ACMFORMATDETAILS_FORMAT_CHARS: UInt32 = 128
ACM_FORMATDETAILSF_INDEX: Int32 = 0
ACM_FORMATDETAILSF_FORMAT: Int32 = 1
ACM_FORMATDETAILSF_QUERYMASK: Int32 = 15
ACM_FORMATENUMF_WFORMATTAG: Int32 = 65536
ACM_FORMATENUMF_NCHANNELS: Int32 = 131072
ACM_FORMATENUMF_NSAMPLESPERSEC: Int32 = 262144
ACM_FORMATENUMF_WBITSPERSAMPLE: Int32 = 524288
ACM_FORMATENUMF_CONVERT: Int32 = 1048576
ACM_FORMATENUMF_SUGGEST: Int32 = 2097152
ACM_FORMATENUMF_HARDWARE: Int32 = 4194304
ACM_FORMATENUMF_INPUT: Int32 = 8388608
ACM_FORMATENUMF_OUTPUT: Int32 = 16777216
ACM_FORMATSUGGESTF_WFORMATTAG: Int32 = 65536
ACM_FORMATSUGGESTF_NCHANNELS: Int32 = 131072
ACM_FORMATSUGGESTF_NSAMPLESPERSEC: Int32 = 262144
ACM_FORMATSUGGESTF_WBITSPERSAMPLE: Int32 = 524288
ACM_FORMATSUGGESTF_TYPEMASK: Int32 = 16711680
ACMHELPMSGSTRINGA: String = 'acmchoose_help'
ACMHELPMSGSTRINGW: String = 'acmchoose_help'
ACMHELPMSGCONTEXTMENUA: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTMENUW: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTHELPA: String = 'acmchoose_contexthelp'
ACMHELPMSGCONTEXTHELPW: String = 'acmchoose_contexthelp'
ACMHELPMSGSTRING: String = 'acmchoose_help'
ACMHELPMSGCONTEXTMENU: String = 'acmchoose_contextmenu'
ACMHELPMSGCONTEXTHELP: String = 'acmchoose_contexthelp'
MM_ACM_FORMATCHOOSE: UInt32 = 32768
FORMATCHOOSE_MESSAGE: UInt32 = 0
FORMATCHOOSE_FORMATTAG_VERIFY: UInt32 = 0
FORMATCHOOSE_FORMAT_VERIFY: UInt32 = 1
FORMATCHOOSE_CUSTOM_VERIFY: UInt32 = 2
ACMFORMATCHOOSE_STYLEF_SHOWHELP: Int32 = 4
ACMFORMATCHOOSE_STYLEF_ENABLEHOOK: Int32 = 8
ACMFORMATCHOOSE_STYLEF_ENABLETEMPLATE: Int32 = 16
ACMFORMATCHOOSE_STYLEF_ENABLETEMPLATEHANDLE: Int32 = 32
ACMFORMATCHOOSE_STYLEF_INITTOWFXSTRUCT: Int32 = 64
ACMFORMATCHOOSE_STYLEF_CONTEXTHELP: Int32 = 128
ACMFILTERTAGDETAILS_FILTERTAG_CHARS: UInt32 = 48
ACM_FILTERTAGDETAILSF_INDEX: Int32 = 0
ACM_FILTERTAGDETAILSF_FILTERTAG: Int32 = 1
ACM_FILTERTAGDETAILSF_LARGESTSIZE: Int32 = 2
ACM_FILTERTAGDETAILSF_QUERYMASK: Int32 = 15
ACMFILTERDETAILS_FILTER_CHARS: UInt32 = 128
ACM_FILTERDETAILSF_INDEX: Int32 = 0
ACM_FILTERDETAILSF_FILTER: Int32 = 1
ACM_FILTERDETAILSF_QUERYMASK: Int32 = 15
ACM_FILTERENUMF_DWFILTERTAG: Int32 = 65536
MM_ACM_FILTERCHOOSE: UInt32 = 32768
FILTERCHOOSE_MESSAGE: UInt32 = 0
FILTERCHOOSE_FILTERTAG_VERIFY: UInt32 = 0
FILTERCHOOSE_FILTER_VERIFY: UInt32 = 1
FILTERCHOOSE_CUSTOM_VERIFY: UInt32 = 2
ACMFILTERCHOOSE_STYLEF_SHOWHELP: Int32 = 4
ACMFILTERCHOOSE_STYLEF_ENABLEHOOK: Int32 = 8
ACMFILTERCHOOSE_STYLEF_ENABLETEMPLATE: Int32 = 16
ACMFILTERCHOOSE_STYLEF_ENABLETEMPLATEHANDLE: Int32 = 32
ACMFILTERCHOOSE_STYLEF_INITTOFILTERSTRUCT: Int32 = 64
ACMFILTERCHOOSE_STYLEF_CONTEXTHELP: Int32 = 128
ACMSTREAMHEADER_STATUSF_DONE: Int32 = 65536
ACMSTREAMHEADER_STATUSF_PREPARED: Int32 = 131072
ACMSTREAMHEADER_STATUSF_INQUEUE: Int32 = 1048576
ACM_STREAMOPENF_QUERY: UInt32 = 1
ACM_STREAMOPENF_ASYNC: UInt32 = 2
ACM_STREAMOPENF_NONREALTIME: UInt32 = 4
ACM_STREAMSIZEF_SOURCE: Int32 = 0
ACM_STREAMSIZEF_DESTINATION: Int32 = 1
ACM_STREAMSIZEF_QUERYMASK: Int32 = 15
ACM_STREAMCONVERTF_BLOCKALIGN: UInt32 = 4
ACM_STREAMCONVERTF_START: UInt32 = 16
ACM_STREAMCONVERTF_END: UInt32 = 32
SND_RING: Int32 = 1048576
SND_ALIAS_START: UInt32 = 0
ACMDM_DRIVER_NOTIFY: UInt32 = 24577
ACMDM_DRIVER_DETAILS: UInt32 = 24586
ACMDM_HARDWARE_WAVE_CAPS_INPUT: UInt32 = 24596
ACMDM_HARDWARE_WAVE_CAPS_OUTPUT: UInt32 = 24597
ACMDM_FORMATTAG_DETAILS: UInt32 = 24601
ACMDM_FORMAT_DETAILS: UInt32 = 24602
ACMDM_FORMAT_SUGGEST: UInt32 = 24603
ACMDM_FILTERTAG_DETAILS: UInt32 = 24626
ACMDM_FILTER_DETAILS: UInt32 = 24627
ACMDM_STREAM_OPEN: UInt32 = 24652
ACMDM_STREAM_CLOSE: UInt32 = 24653
ACMDM_STREAM_SIZE: UInt32 = 24654
ACMDM_STREAM_CONVERT: UInt32 = 24655
ACMDM_STREAM_RESET: UInt32 = 24656
ACMDM_STREAM_PREPARE: UInt32 = 24657
ACMDM_STREAM_UNPREPARE: UInt32 = 24658
ACMDM_STREAM_UPDATE: UInt32 = 24659
@winfunctype('OLE32.dll')
def CoRegisterMessageFilter(lpMessageFilter: Windows.Win32.Media.Audio.IMessageFilter_head, lplpMessageFilter: POINTER(Windows.Win32.Media.Audio.IMessageFilter_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('WINMM.dll')
def sndPlaySoundA(pszSound: Windows.Win32.Foundation.PSTR, fuSound: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def sndPlaySoundW(pszSound: Windows.Win32.Foundation.PWSTR, fuSound: UInt32) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def PlaySoundA(pszSound: Windows.Win32.Foundation.PSTR, hmod: Windows.Win32.Foundation.HMODULE, fdwSound: Windows.Win32.Media.Audio.SND_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def PlaySoundW(pszSound: Windows.Win32.Foundation.PWSTR, hmod: Windows.Win32.Foundation.HMODULE, fdwSound: Windows.Win32.Media.Audio.SND_FLAGS) -> Windows.Win32.Foundation.BOOL: ...
@winfunctype('WINMM.dll')
def waveOutGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetDevCapsA(uDeviceID: UIntPtr, pwoc: POINTER(Windows.Win32.Media.Audio.WAVEOUTCAPSA_head), cbwoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetDevCapsW(uDeviceID: UIntPtr, pwoc: POINTER(Windows.Win32.Media.Audio.WAVEOUTCAPSW_head), cbwoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetVolume(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetVolume(hwo: Windows.Win32.Media.Audio.HWAVEOUT, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetErrorTextA(mmrError: UInt32, pszText: Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetErrorTextW(mmrError: UInt32, pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutOpen(phwo: POINTER(Windows.Win32.Media.Audio.HWAVEOUT), uDeviceID: UInt32, pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutClose(hwo: Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutPrepareHeader(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutUnprepareHeader(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutWrite(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutPause(hwo: Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutRestart(hwo: Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutReset(hwo: Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutBreakLoop(hwo: Windows.Win32.Media.Audio.HWAVEOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPosition(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pmmt: POINTER(Windows.Win32.Media.MMTIME_head), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPitch(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pdwPitch: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetPitch(hwo: Windows.Win32.Media.Audio.HWAVEOUT, dwPitch: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetPlaybackRate(hwo: Windows.Win32.Media.Audio.HWAVEOUT, pdwRate: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutSetPlaybackRate(hwo: Windows.Win32.Media.Audio.HWAVEOUT, dwRate: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutGetID(hwo: Windows.Win32.Media.Audio.HWAVEOUT, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveOutMessage(hwo: Windows.Win32.Media.Audio.HWAVEOUT, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetDevCapsA(uDeviceID: UIntPtr, pwic: POINTER(Windows.Win32.Media.Audio.WAVEINCAPSA_head), cbwic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetDevCapsW(uDeviceID: UIntPtr, pwic: POINTER(Windows.Win32.Media.Audio.WAVEINCAPSW_head), cbwic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetErrorTextA(mmrError: UInt32, pszText: Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetErrorTextW(mmrError: UInt32, pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInOpen(phwi: POINTER(Windows.Win32.Media.Audio.HWAVEIN), uDeviceID: UInt32, pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInClose(hwi: Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInPrepareHeader(hwi: Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInUnprepareHeader(hwi: Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInAddBuffer(hwi: Windows.Win32.Media.Audio.HWAVEIN, pwh: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head), cbwh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInStart(hwi: Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInStop(hwi: Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInReset(hwi: Windows.Win32.Media.Audio.HWAVEIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetPosition(hwi: Windows.Win32.Media.Audio.HWAVEIN, pmmt: POINTER(Windows.Win32.Media.MMTIME_head), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInGetID(hwi: Windows.Win32.Media.Audio.HWAVEIN, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def waveInMessage(hwi: Windows.Win32.Media.Audio.HWAVEIN, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamOpen(phms: POINTER(Windows.Win32.Media.Audio.HMIDISTRM), puDeviceID: POINTER(UInt32), cMidi: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamClose(hms: Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamProperty(hms: Windows.Win32.Media.Audio.HMIDISTRM, lppropdata: POINTER(Byte), dwProperty: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamPosition(hms: Windows.Win32.Media.Audio.HMIDISTRM, lpmmt: POINTER(Windows.Win32.Media.MMTIME_head), cbmmt: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamOut(hms: Windows.Win32.Media.Audio.HMIDISTRM, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamPause(hms: Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamRestart(hms: Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiStreamStop(hms: Windows.Win32.Media.Audio.HMIDISTRM) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiConnect(hmi: Windows.Win32.Media.Audio.HMIDI, hmo: Windows.Win32.Media.Audio.HMIDIOUT, pReserved: c_void_p) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiDisconnect(hmi: Windows.Win32.Media.Audio.HMIDI, hmo: Windows.Win32.Media.Audio.HMIDIOUT, pReserved: c_void_p) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetDevCapsA(uDeviceID: UIntPtr, pmoc: POINTER(Windows.Win32.Media.Audio.MIDIOUTCAPSA_head), cbmoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetDevCapsW(uDeviceID: UIntPtr, pmoc: POINTER(Windows.Win32.Media.Audio.MIDIOUTCAPSW_head), cbmoc: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetVolume(hmo: Windows.Win32.Media.Audio.HMIDIOUT, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutSetVolume(hmo: Windows.Win32.Media.Audio.HMIDIOUT, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetErrorTextA(mmrError: UInt32, pszText: Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetErrorTextW(mmrError: UInt32, pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutOpen(phmo: POINTER(Windows.Win32.Media.Audio.HMIDIOUT), uDeviceID: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutClose(hmo: Windows.Win32.Media.Audio.HMIDIOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutPrepareHeader(hmo: Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutUnprepareHeader(hmo: Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutShortMsg(hmo: Windows.Win32.Media.Audio.HMIDIOUT, dwMsg: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutLongMsg(hmo: Windows.Win32.Media.Audio.HMIDIOUT, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutReset(hmo: Windows.Win32.Media.Audio.HMIDIOUT) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutCachePatches(hmo: Windows.Win32.Media.Audio.HMIDIOUT, uBank: UInt32, pwpa: POINTER(UInt16), fuCache: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutCacheDrumPatches(hmo: Windows.Win32.Media.Audio.HMIDIOUT, uPatch: UInt32, pwkya: POINTER(UInt16), fuCache: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutGetID(hmo: Windows.Win32.Media.Audio.HMIDIOUT, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiOutMessage(hmo: Windows.Win32.Media.Audio.HMIDIOUT, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetDevCapsA(uDeviceID: UIntPtr, pmic: POINTER(Windows.Win32.Media.Audio.MIDIINCAPSA_head), cbmic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetDevCapsW(uDeviceID: UIntPtr, pmic: POINTER(Windows.Win32.Media.Audio.MIDIINCAPSW_head), cbmic: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetErrorTextA(mmrError: UInt32, pszText: Windows.Win32.Foundation.PSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetErrorTextW(mmrError: UInt32, pszText: Windows.Win32.Foundation.PWSTR, cchText: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInOpen(phmi: POINTER(Windows.Win32.Media.Audio.HMIDIIN), uDeviceID: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: Windows.Win32.Media.Audio.MIDI_WAVE_OPEN_TYPE) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInClose(hmi: Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInPrepareHeader(hmi: Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInUnprepareHeader(hmi: Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInAddBuffer(hmi: Windows.Win32.Media.Audio.HMIDIIN, pmh: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head), cbmh: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInStart(hmi: Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInStop(hmi: Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInReset(hmi: Windows.Win32.Media.Audio.HMIDIIN) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInGetID(hmi: Windows.Win32.Media.Audio.HMIDIIN, puDeviceID: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def midiInMessage(hmi: Windows.Win32.Media.Audio.HMIDIIN, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetDevCapsA(uDeviceID: UIntPtr, pac: POINTER(Windows.Win32.Media.Audio.AUXCAPSA_head), cbac: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetDevCapsW(uDeviceID: UIntPtr, pac: POINTER(Windows.Win32.Media.Audio.AUXCAPSW_head), cbac: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxSetVolume(uDeviceID: UInt32, dwVolume: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxGetVolume(uDeviceID: UInt32, pdwVolume: POINTER(UInt32)) -> UInt32: ...
@winfunctype('WINMM.dll')
def auxOutMessage(uDeviceID: UInt32, uMsg: UInt32, dw1: UIntPtr, dw2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetNumDevs() -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetDevCapsA(uMxId: UIntPtr, pmxcaps: POINTER(Windows.Win32.Media.Audio.MIXERCAPSA_head), cbmxcaps: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetDevCapsW(uMxId: UIntPtr, pmxcaps: POINTER(Windows.Win32.Media.Audio.MIXERCAPSW_head), cbmxcaps: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerOpen(phmx: POINTER(Windows.Win32.Media.Audio.HMIXER), uMxId: UInt32, dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerClose(hmx: Windows.Win32.Media.Audio.HMIXER) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerMessage(hmx: Windows.Win32.Media.Audio.HMIXER, uMsg: UInt32, dwParam1: UIntPtr, dwParam2: UIntPtr) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineInfoA(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxl: POINTER(Windows.Win32.Media.Audio.MIXERLINEA_head), fdwInfo: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineInfoW(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxl: POINTER(Windows.Win32.Media.Audio.MIXERLINEW_head), fdwInfo: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetID(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, puMxId: POINTER(UInt32), fdwId: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineControlsA(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxlc: POINTER(Windows.Win32.Media.Audio.MIXERLINECONTROLSA_head), fdwControls: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetLineControlsW(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxlc: POINTER(Windows.Win32.Media.Audio.MIXERLINECONTROLSW_head), fdwControls: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetControlDetailsA(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(Windows.Win32.Media.Audio.MIXERCONTROLDETAILS_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerGetControlDetailsW(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(Windows.Win32.Media.Audio.MIXERCONTROLDETAILS_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('WINMM.dll')
def mixerSetControlDetails(hmxobj: Windows.Win32.Media.Audio.HMIXEROBJ, pmxcd: POINTER(Windows.Win32.Media.Audio.MIXERCONTROLDETAILS_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MMDevAPI.dll')
def ActivateAudioInterfaceAsync(deviceInterfacePath: Windows.Win32.Foundation.PWSTR, riid: POINTER(Guid), activationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), completionHandler: Windows.Win32.Media.Audio.IActivateAudioInterfaceCompletionHandler_head, activationOperation: POINTER(Windows.Win32.Media.Audio.IActivateAudioInterfaceAsyncOperation_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitor(audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategory(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategoryAndDeviceRole(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, role: Windows.Win32.Media.Audio.ERole, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateRenderAudioStateMonitorForCategoryAndDeviceId(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, deviceId: Windows.Win32.Foundation.PWSTR, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitor(audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategory(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategoryAndDeviceRole(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, role: Windows.Win32.Media.Audio.ERole, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('Windows.Media.MediaControl.dll')
def CreateCaptureAudioStateMonitorForCategoryAndDeviceId(category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, deviceId: Windows.Win32.Foundation.PWSTR, audioStateMonitor: POINTER(Windows.Win32.Media.Audio.IAudioStateMonitor_head)) -> Windows.Win32.Foundation.HRESULT: ...
@winfunctype('MSACM32.dll')
def acmGetVersion() -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmMetrics(hao: Windows.Win32.Media.Audio.HACMOBJ, uMetric: UInt32, pMetric: c_void_p) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverEnum(fnCallback: Windows.Win32.Media.Audio.ACMDRIVERENUMCB, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverID(hao: Windows.Win32.Media.Audio.HACMOBJ, phadid: POINTER(Windows.Win32.Media.Audio.HACMDRIVERID), fdwDriverID: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverAddA(phadid: POINTER(Windows.Win32.Media.Audio.HACMDRIVERID), hinstModule: Windows.Win32.Foundation.HMODULE, lParam: Windows.Win32.Foundation.LPARAM, dwPriority: UInt32, fdwAdd: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverAddW(phadid: POINTER(Windows.Win32.Media.Audio.HACMDRIVERID), hinstModule: Windows.Win32.Foundation.HMODULE, lParam: Windows.Win32.Foundation.LPARAM, dwPriority: UInt32, fdwAdd: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverRemove(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, fdwRemove: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverOpen(phad: POINTER(Windows.Win32.Media.Audio.HACMDRIVER), hadid: Windows.Win32.Media.Audio.HACMDRIVERID, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverClose(had: Windows.Win32.Media.Audio.HACMDRIVER, fdwClose: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverMessage(had: Windows.Win32.Media.Audio.HACMDRIVER, uMsg: UInt32, lParam1: Windows.Win32.Foundation.LPARAM, lParam2: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype('MSACM32.dll')
def acmDriverPriority(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, dwPriority: UInt32, fdwPriority: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverDetailsA(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, padd: POINTER(Windows.Win32.Media.Audio.ACMDRIVERDETAILSA_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmDriverDetailsW(hadid: Windows.Win32.Media.Audio.HACMDRIVERID, padd: POINTER(Windows.Win32.Media.Audio.ACMDRIVERDETAILSW_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagDetailsA(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagDetailsW(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagEnumA(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSA_head), fnCallback: Windows.Win32.Media.Audio.ACMFORMATTAGENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatTagEnumW(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFORMATTAGDETAILSW_head), fnCallback: Windows.Win32.Media.Audio.ACMFORMATTAGENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatDetailsA(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFORMATDETAILSA_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatDetailsW(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.tACMFORMATDETAILSW_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatEnumA(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFORMATDETAILSA_head), fnCallback: Windows.Win32.Media.Audio.ACMFORMATENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatEnumW(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.tACMFORMATDETAILSW_head), fnCallback: Windows.Win32.Media.Audio.ACMFORMATENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatSuggest(had: Windows.Win32.Media.Audio.HACMDRIVER, pwfxSrc: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pwfxDst: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), cbwfxDst: UInt32, fdwSuggest: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatChooseA(pafmtc: POINTER(Windows.Win32.Media.Audio.ACMFORMATCHOOSEA_head)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFormatChooseW(pafmtc: POINTER(Windows.Win32.Media.Audio.ACMFORMATCHOOSEW_head)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagDetailsA(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagDetailsW(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagEnumA(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSA_head), fnCallback: Windows.Win32.Media.Audio.ACMFILTERTAGENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterTagEnumW(had: Windows.Win32.Media.Audio.HACMDRIVER, paftd: POINTER(Windows.Win32.Media.Audio.ACMFILTERTAGDETAILSW_head), fnCallback: Windows.Win32.Media.Audio.ACMFILTERTAGENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterDetailsA(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSA_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterDetailsW(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSW_head), fdwDetails: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterEnumA(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSA_head), fnCallback: Windows.Win32.Media.Audio.ACMFILTERENUMCBA, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterEnumW(had: Windows.Win32.Media.Audio.HACMDRIVER, pafd: POINTER(Windows.Win32.Media.Audio.ACMFILTERDETAILSW_head), fnCallback: Windows.Win32.Media.Audio.ACMFILTERENUMCBW, dwInstance: UIntPtr, fdwEnum: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterChooseA(pafltrc: POINTER(Windows.Win32.Media.Audio.ACMFILTERCHOOSEA_head)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmFilterChooseW(pafltrc: POINTER(Windows.Win32.Media.Audio.ACMFILTERCHOOSEW_head)) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamOpen(phas: POINTER(Windows.Win32.Media.Audio.HACMSTREAM), had: Windows.Win32.Media.Audio.HACMDRIVER, pwfxSrc: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pwfxDst: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pwfltr: POINTER(Windows.Win32.Media.Audio.WAVEFILTER_head), dwCallback: UIntPtr, dwInstance: UIntPtr, fdwOpen: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamClose(has: Windows.Win32.Media.Audio.HACMSTREAM, fdwClose: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamSize(has: Windows.Win32.Media.Audio.HACMSTREAM, cbInput: UInt32, pdwOutputBytes: POINTER(UInt32), fdwSize: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamReset(has: Windows.Win32.Media.Audio.HACMSTREAM, fdwReset: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamMessage(has: Windows.Win32.Media.Audio.HACMSTREAM, uMsg: UInt32, lParam1: Windows.Win32.Foundation.LPARAM, lParam2: Windows.Win32.Foundation.LPARAM) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamConvert(has: Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(Windows.Win32.Media.Audio.ACMSTREAMHEADER_head), fdwConvert: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamPrepareHeader(has: Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(Windows.Win32.Media.Audio.ACMSTREAMHEADER_head), fdwPrepare: UInt32) -> UInt32: ...
@winfunctype('MSACM32.dll')
def acmStreamUnprepareHeader(has: Windows.Win32.Media.Audio.HACMSTREAM, pash: POINTER(Windows.Win32.Media.Audio.ACMSTREAMHEADER_head), fdwUnprepare: UInt32) -> UInt32: ...
class AudioClient3ActivationParams(EasyCastStructure):
    tracingContextId: Guid
class AudioClientProperties(EasyCastStructure):
    cbSize: UInt32
    bIsOffload: Windows.Win32.Foundation.BOOL
    eCategory: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    Options: Windows.Win32.Media.Audio.AUDCLNT_STREAMOPTIONS
class AudioExtensionParams(EasyCastStructure):
    AddPageParam: Windows.Win32.Foundation.LPARAM
    pEndpoint: Windows.Win32.Media.Audio.IMMDevice_head
    pPnpInterface: Windows.Win32.Media.Audio.IMMDevice_head
    pPnpDevnode: Windows.Win32.Media.Audio.IMMDevice_head
AudioObjectType = Int32
AudioObjectType_None: AudioObjectType = 0
AudioObjectType_Dynamic: AudioObjectType = 1
AudioObjectType_FrontLeft: AudioObjectType = 2
AudioObjectType_FrontRight: AudioObjectType = 4
AudioObjectType_FrontCenter: AudioObjectType = 8
AudioObjectType_LowFrequency: AudioObjectType = 16
AudioObjectType_SideLeft: AudioObjectType = 32
AudioObjectType_SideRight: AudioObjectType = 64
AudioObjectType_BackLeft: AudioObjectType = 128
AudioObjectType_BackRight: AudioObjectType = 256
AudioObjectType_TopFrontLeft: AudioObjectType = 512
AudioObjectType_TopFrontRight: AudioObjectType = 1024
AudioObjectType_TopBackLeft: AudioObjectType = 2048
AudioObjectType_TopBackRight: AudioObjectType = 4096
AudioObjectType_BottomFrontLeft: AudioObjectType = 8192
AudioObjectType_BottomFrontRight: AudioObjectType = 16384
AudioObjectType_BottomBackLeft: AudioObjectType = 32768
AudioObjectType_BottomBackRight: AudioObjectType = 65536
AudioObjectType_BackCenter: AudioObjectType = 131072
AudioSessionDisconnectReason = Int32
AudioSessionDisconnectReason_DisconnectReasonDeviceRemoval: AudioSessionDisconnectReason = 0
AudioSessionDisconnectReason_DisconnectReasonServerShutdown: AudioSessionDisconnectReason = 1
AudioSessionDisconnectReason_DisconnectReasonFormatChanged: AudioSessionDisconnectReason = 2
AudioSessionDisconnectReason_DisconnectReasonSessionLogoff: AudioSessionDisconnectReason = 3
AudioSessionDisconnectReason_DisconnectReasonSessionDisconnected: AudioSessionDisconnectReason = 4
AudioSessionDisconnectReason_DisconnectReasonExclusiveModeOverride: AudioSessionDisconnectReason = 5
AudioSessionState = Int32
AudioSessionState_AudioSessionStateInactive: AudioSessionState = 0
AudioSessionState_AudioSessionStateActive: AudioSessionState = 1
AudioSessionState_AudioSessionStateExpired: AudioSessionState = 2
AudioStateMonitorSoundLevel = Int32
AudioStateMonitorSoundLevel_Muted: AudioStateMonitorSoundLevel = 0
AudioStateMonitorSoundLevel_Low: AudioStateMonitorSoundLevel = 1
AudioStateMonitorSoundLevel_Full: AudioStateMonitorSoundLevel = 2
ConnectorType = Int32
ConnectorType_Unknown_Connector: ConnectorType = 0
ConnectorType_Physical_Internal: ConnectorType = 1
ConnectorType_Physical_External: ConnectorType = 2
ConnectorType_Software_IO: ConnectorType = 3
ConnectorType_Software_Fixed: ConnectorType = 4
ConnectorType_Network: ConnectorType = 5
class DIRECTX_AUDIO_ACTIVATION_PARAMS(EasyCastStructure):
    cbDirectXAudioActivationParams: UInt32
    guidAudioSession: Guid
    dwAudioStreamFlags: UInt32
DataFlow = Int32
DataFlow_In: DataFlow = 0
DataFlow_Out: DataFlow = 1
DeviceTopology = Guid('1df639d0-5ec1-47aa-93-79-82-8d-c1-aa-8c-59')
class ECHOWAVEFILTER(EasyCastStructure):
    wfltr: Windows.Win32.Media.Audio.WAVEFILTER
    dwVolume: UInt32
    dwDelay: UInt32
    _pack_ = 1
EDataFlow = Int32
EDataFlow_eRender: EDataFlow = 0
EDataFlow_eCapture: EDataFlow = 1
EDataFlow_eAll: EDataFlow = 2
EDataFlow_EDataFlow_enum_count: EDataFlow = 3
ERole = Int32
ERole_eConsole: ERole = 0
ERole_eMultimedia: ERole = 1
ERole_eCommunications: ERole = 2
ERole_ERole_enum_count: ERole = 3
EndpointFormFactor = Int32
EndpointFormFactor_RemoteNetworkDevice: EndpointFormFactor = 0
EndpointFormFactor_Speakers: EndpointFormFactor = 1
EndpointFormFactor_LineLevel: EndpointFormFactor = 2
EndpointFormFactor_Headphones: EndpointFormFactor = 3
EndpointFormFactor_Microphone: EndpointFormFactor = 4
EndpointFormFactor_Headset: EndpointFormFactor = 5
EndpointFormFactor_Handset: EndpointFormFactor = 6
EndpointFormFactor_UnknownDigitalPassthrough: EndpointFormFactor = 7
EndpointFormFactor_SPDIF: EndpointFormFactor = 8
EndpointFormFactor_DigitalAudioDisplayDevice: EndpointFormFactor = 9
EndpointFormFactor_UnknownFormFactor: EndpointFormFactor = 10
EndpointFormFactor_EndpointFormFactor_enum_count: EndpointFormFactor = 11
HACMDRIVER = IntPtr
HACMDRIVERID = IntPtr
HACMOBJ = IntPtr
HACMSTREAM = IntPtr
HMIDI = IntPtr
HMIDIIN = IntPtr
HMIDIOUT = IntPtr
HMIDISTRM = IntPtr
HMIXER = IntPtr
HMIXEROBJ = IntPtr
HWAVE = IntPtr
HWAVEIN = IntPtr
HWAVEOUT = IntPtr
class IAcousticEchoCancellationControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f4ae25b5-aaa3-437d-b6-b3-db-be-2d-0e-95-49')
    @commethod(3)
    def SetEchoCancellationRenderEndpoint(self, endpointId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IActivateAudioInterfaceAsyncOperation(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('72a22d78-cde4-431d-b8-cc-84-3a-71-19-9b-6d')
    @commethod(3)
    def GetActivateResult(self, activateResult: POINTER(Windows.Win32.Foundation.HRESULT), activatedInterface: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IActivateAudioInterfaceCompletionHandler(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('41d949ab-9862-444a-80-f6-c2-61-33-4d-a5-eb')
    @commethod(3)
    def ActivateCompleted(self, activateOperation: Windows.Win32.Media.Audio.IActivateAudioInterfaceAsyncOperation_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioAmbisonicsControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('28724c91-df35-4856-9f-76-d6-a2-64-13-f3-df')
    @commethod(3)
    def SetData(self, pAmbisonicsParams: POINTER(Windows.Win32.Media.Audio.AMBISONICS_PARAMS_head), cbAmbisonicsParams: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetHeadTracking(self, bEnableHeadTracking: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetHeadTracking(self, pbEnableHeadTracking: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetRotation(self, X: Single, Y: Single, Z: Single, W: Single) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioAutoGainControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('85401fd4-6de4-4b9d-98-69-2d-67-53-a8-2f-3c')
    @commethod(3)
    def GetEnabled(self, pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEnabled(self, bEnable: Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioBass(ComPtr):
    extends: Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('a2b1a1d9-4db3-425d-a2-b2-bd-33-5c-b3-e2-e5')
class IAudioCaptureClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c8adbd64-e71e-48a0-a4-de-18-5c-39-5c-d3-17')
    @commethod(3)
    def GetBuffer(self, ppData: POINTER(POINTER(Byte)), pNumFramesToRead: POINTER(UInt32), pdwFlags: POINTER(UInt32), pu64DevicePosition: POINTER(UInt64), pu64QPCPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseBuffer(self, NumFramesRead: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetNextPacketSize(self, pNumFramesInNextPacket: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioChannelConfig(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bb11c46f-ec28-493c-b8-8a-5d-b8-80-62-ce-98')
    @commethod(3)
    def SetChannelConfig(self, dwConfig: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetChannelConfig(self, pdwConfig: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1cb9ad4c-dbfa-4c32-b1-78-c2-f5-68-a7-03-b2')
    @commethod(3)
    def Initialize(self, ShareMode: Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE, StreamFlags: UInt32, hnsBufferDuration: Int64, hnsPeriodicity: Int64, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), AudioSessionGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetBufferSize(self, pNumBufferFrames: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetStreamLatency(self, phnsLatency: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetCurrentPadding(self, pNumPaddingFrames: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsFormatSupported(self, ShareMode: Windows.Win32.Media.Audio.AUDCLNT_SHAREMODE, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), ppClosestMatch: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetMixFormat(self, ppDeviceFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetDevicePeriod(self, phnsDefaultDevicePeriod: POINTER(Int64), phnsMinimumDevicePeriod: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def SetEventHandle(self, eventHandle: Windows.Win32.Foundation.HANDLE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetService(self, riid: POINTER(Guid), ppv: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClient2(ComPtr):
    extends: Windows.Win32.Media.Audio.IAudioClient
    _iid_ = Guid('726778cd-f60a-4eda-82-de-e4-76-10-cd-78-aa')
    @commethod(15)
    def IsOffloadCapable(self, Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, pbOffloadCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetClientProperties(self, pProperties: POINTER(Windows.Win32.Media.Audio.AudioClientProperties_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(17)
    def GetBufferSizeLimits(self, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), bEventDriven: Windows.Win32.Foundation.BOOL, phnsMinBufferDuration: POINTER(Int64), phnsMaxBufferDuration: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClient3(ComPtr):
    extends: Windows.Win32.Media.Audio.IAudioClient2
    _iid_ = Guid('7ed4ee07-8e67-4cd4-8c-1a-2b-7a-59-87-ad-42')
    @commethod(18)
    def GetSharedModeEnginePeriod(self, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), pDefaultPeriodInFrames: POINTER(UInt32), pFundamentalPeriodInFrames: POINTER(UInt32), pMinPeriodInFrames: POINTER(UInt32), pMaxPeriodInFrames: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(19)
    def GetCurrentSharedModeEnginePeriod(self, ppFormat: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)), pCurrentPeriodInFrames: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(20)
    def InitializeSharedAudioStream(self, StreamFlags: UInt32, PeriodInFrames: UInt32, pFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), AudioSessionGuid: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClientDuckingControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c789d381-a28c-4168-b2-8f-d3-a8-37-92-4d-c3')
    @commethod(3)
    def SetDuckingOptionsForCurrentStream(self, options: Windows.Win32.Media.Audio.AUDIO_DUCKING_OPTIONS) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClock(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('cd63314f-3fba-4a1b-81-2c-ef-96-35-87-28-e7')
    @commethod(3)
    def GetFrequency(self, pu64Frequency: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPosition(self, pu64Position: POINTER(UInt64), pu64QPCPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetCharacteristics(self, pdwCharacteristics: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClock2(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6f49ff73-6727-49ac-a0-08-d9-8c-f5-e7-00-48')
    @commethod(3)
    def GetDevicePosition(self, DevicePosition: POINTER(UInt64), QPCPosition: POINTER(UInt64)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioClockAdjustment(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f6e4c0a0-46d9-4fb8-be-21-57-a3-ef-2b-62-6c')
    @commethod(3)
    def SetSampleRate(self, flSampleRate: Single) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEffectsChangedNotificationClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a5ded44f-3c5d-4b2b-bd-1e-5d-c1-ee-20-bb-f6')
    @commethod(3)
    def OnAudioEffectsChanged(self) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioEffectsManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('4460b3ae-4b44-4527-86-76-75-48-a8-ac-d2-60')
    @commethod(3)
    def RegisterAudioEffectsChangedNotificationCallback(self, client: Windows.Win32.Media.Audio.IAudioEffectsChangedNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterAudioEffectsChangedNotificationCallback(self, client: Windows.Win32.Media.Audio.IAudioEffectsChangedNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetAudioEffects(self, effects: POINTER(POINTER(Windows.Win32.Media.Audio.AUDIO_EFFECT_head)), numEffects: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAudioEffectState(self, effectId: Guid, state: Windows.Win32.Media.Audio.AUDIO_EFFECT_STATE) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioFormatEnumerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('dcdaa858-895a-4a22-a5-eb-67-bd-a5-06-09-6d')
    @commethod(3)
    def GetCount(self, count: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetFormat(self, index: UInt32, format: POINTER(POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head))) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioInputSelector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('4f03dc02-5e6e-4653-8f-72-a0-30-c1-23-d5-98')
    @commethod(3)
    def GetSelection(self, pnIdSelected: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSelection(self, nIdSelect: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioLoudness(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('7d8b1437-dd53-4350-9c-1b-1e-e2-89-0b-d9-38')
    @commethod(3)
    def GetEnabled(self, pbEnabled: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEnabled(self, bEnable: Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioMidrange(ComPtr):
    extends: Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('5e54b6d7-b44b-40d9-9a-9e-e6-91-d9-ce-6e-df')
class IAudioMute(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('df45aeea-b74a-4b6b-af-ad-23-66-b6-aa-01-2e')
    @commethod(3)
    def SetMute(self, bMuted: Windows.Win32.Foundation.BOOL, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMute(self, pbMuted: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioOutputSelector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bb515f69-94a7-429e-8b-9c-27-1b-3f-11-a3-ab')
    @commethod(3)
    def GetSelection(self, pnIdSelected: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetSelection(self, nIdSelect: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioPeakMeter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('dd79923c-0599-45e0-b8-b6-c8-df-7d-b6-e7-96')
    @commethod(3)
    def GetChannelCount(self, pcChannels: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLevel(self, nChannel: UInt32, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioRenderClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f294acfc-3146-4483-a7-bf-ad-dc-a7-c2-60-e2')
    @commethod(3)
    def GetBuffer(self, NumFramesRequested: UInt32, ppData: POINTER(POINTER(Byte))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReleaseBuffer(self, NumFramesWritten: UInt32, dwFlags: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionControl(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('f4b1a599-7266-4319-a8-ca-e7-0a-cb-11-e8-cd')
    @commethod(3)
    def GetState(self, pRetVal: POINTER(Windows.Win32.Media.Audio.AudioSessionState)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDisplayName(self, pRetVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetDisplayName(self, Value: Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetIconPath(self, pRetVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetIconPath(self, Value: Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetGroupingParam(self, pRetVal: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetGroupingParam(self, Override: POINTER(Guid), EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def RegisterAudioSessionNotification(self, NewNotifications: Windows.Win32.Media.Audio.IAudioSessionEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def UnregisterAudioSessionNotification(self, NewNotifications: Windows.Win32.Media.Audio.IAudioSessionEvents_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionControl2(ComPtr):
    extends: Windows.Win32.Media.Audio.IAudioSessionControl
    _iid_ = Guid('bfb7ff88-7239-4fc9-8f-a2-07-c9-50-be-9c-6d')
    @commethod(12)
    def GetSessionIdentifier(self, pRetVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def GetSessionInstanceIdentifier(self, pRetVal: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def GetProcessId(self, pRetVal: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def IsSystemSoundsSession(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(16)
    def SetDuckingPreference(self, optOut: Windows.Win32.Foundation.BOOL) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionEnumerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('e2f5bb11-0570-40ca-ac-dd-3a-a0-12-77-de-e8')
    @commethod(3)
    def GetCount(self, SessionCount: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSession(self, SessionCount: Int32, Session: POINTER(Windows.Win32.Media.Audio.IAudioSessionControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionEvents(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('24918acc-64b3-37c1-8c-a9-74-a6-6e-99-57-a8')
    @commethod(3)
    def OnDisplayNameChanged(self, NewDisplayName: Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnIconPathChanged(self, NewIconPath: Windows.Win32.Foundation.PWSTR, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnSimpleVolumeChanged(self, NewVolume: Single, NewMute: Windows.Win32.Foundation.BOOL, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnChannelVolumeChanged(self, ChannelCount: UInt32, NewChannelVolumeArray: POINTER(Single), ChangedChannel: UInt32, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnGroupingParamChanged(self, NewGroupingParam: POINTER(Guid), EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def OnStateChanged(self, NewState: Windows.Win32.Media.Audio.AudioSessionState) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def OnSessionDisconnected(self, DisconnectReason: Windows.Win32.Media.Audio.AudioSessionDisconnectReason) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionManager(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bfa971f1-4d5e-40bb-93-5e-96-70-39-bf-be-e4')
    @commethod(3)
    def GetAudioSessionControl(self, AudioSessionGuid: POINTER(Guid), StreamFlags: UInt32, SessionControl: POINTER(Windows.Win32.Media.Audio.IAudioSessionControl_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSimpleAudioVolume(self, AudioSessionGuid: POINTER(Guid), StreamFlags: UInt32, AudioVolume: POINTER(Windows.Win32.Media.Audio.ISimpleAudioVolume_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionManager2(ComPtr):
    extends: Windows.Win32.Media.Audio.IAudioSessionManager
    _iid_ = Guid('77aa99a0-1bd6-484f-8b-c7-2c-65-4c-9a-9b-6f')
    @commethod(5)
    def GetSessionEnumerator(self, SessionEnum: POINTER(Windows.Win32.Media.Audio.IAudioSessionEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterSessionNotification(self, SessionNotification: Windows.Win32.Media.Audio.IAudioSessionNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterSessionNotification(self, SessionNotification: Windows.Win32.Media.Audio.IAudioSessionNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterDuckNotification(self, sessionID: Windows.Win32.Foundation.PWSTR, duckNotification: Windows.Win32.Media.Audio.IAudioVolumeDuckNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterDuckNotification(self, duckNotification: Windows.Win32.Media.Audio.IAudioVolumeDuckNotification_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSessionNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('641dd20b-4d41-49cc-ab-a3-17-4b-94-77-bb-08')
    @commethod(3)
    def OnSessionCreated(self, NewSession: Windows.Win32.Media.Audio.IAudioSessionControl_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioStateMonitor(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('63bd8738-e30d-4c77-bf-5c-83-4e-87-c6-57-e2')
    @commethod(3)
    def RegisterCallback(self, callback: Windows.Win32.Media.Audio.PAudioStateMonitorCallback, context: c_void_p, registration: POINTER(Int64)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def UnregisterCallback(self, registration: Int64) -> Void: ...
    @commethod(5)
    def GetSoundLevel(self) -> Windows.Win32.Media.Audio.AudioStateMonitorSoundLevel: ...
class IAudioStreamVolume(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('93014887-242d-4068-8a-15-cf-5e-93-b9-0f-e3')
    @commethod(3)
    def GetChannelCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolume(self, dwIndex: UInt32, fLevel: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolume(self, dwIndex: UInt32, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsPropertyChangeNotificationClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('20049d40-56d5-400e-a2-ef-38-55-99-fe-ed-49')
    @commethod(3)
    def OnPropertyChanged(self, type: Windows.Win32.Media.Audio.AUDIO_SYSTEMEFFECTS_PROPERTYSTORE_TYPE, key: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioSystemEffectsPropertyStore(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('302ae7f9-d7e0-43e4-97-1b-1f-82-93-61-3d-2a')
    @commethod(3)
    def OpenDefaultPropertyStore(self, stgmAccess: UInt32, propStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenUserPropertyStore(self, stgmAccess: UInt32, propStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OpenVolatilePropertyStore(self, stgmAccess: UInt32, propStore: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ResetUserPropertyStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResetVolatilePropertyStore(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def RegisterPropertyChangeNotification(self, callback: Windows.Win32.Media.Audio.IAudioSystemEffectsPropertyChangeNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def UnregisterPropertyChangeNotification(self, callback: Windows.Win32.Media.Audio.IAudioSystemEffectsPropertyChangeNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioTreble(ComPtr):
    extends: Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('0a717812-694e-4907-b7-4b-ba-fa-5c-fd-ca-7b')
class IAudioViewManagerService(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a7a7ef10-1f49-45e0-ad-35-61-20-57-cc-8f-74')
    @commethod(3)
    def SetAudioStreamWindow(self, hwnd: Windows.Win32.Foundation.HWND) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioVolumeDuckNotification(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c3b284d4-6d39-4359-b3-cf-b5-6d-db-3b-b3-9c')
    @commethod(3)
    def OnVolumeDuckNotification(self, sessionID: Windows.Win32.Foundation.PWSTR, countCommunicationSessions: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnVolumeUnduckNotification(self, sessionID: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
class IAudioVolumeLevel(ComPtr):
    extends: Windows.Win32.Media.Audio.IPerChannelDbLevel
    _iid_ = Guid('7fb7b48f-531d-44a2-bc-b3-5a-d5-a1-34-b3-dc')
class IChannelAudioVolume(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1c158861-b533-4b30-b1-cf-e8-53-e5-1c-59-b8')
    @commethod(3)
    def GetChannelCount(self, pdwCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetChannelVolume(self, dwIndex: UInt32, fLevel: Single, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetChannelVolume(self, dwIndex: UInt32, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single), EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetAllVolumes(self, dwCount: UInt32, pfVolumes: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
class IConnector(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('9c2c4058-23f5-41de-87-7a-df-3a-f2-36-a0-9e')
    @commethod(3)
    def GetType(self, pType: POINTER(Windows.Win32.Media.Audio.ConnectorType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDataFlow(self, pFlow: POINTER(Windows.Win32.Media.Audio.DataFlow)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ConnectTo(self, pConnectTo: Windows.Win32.Media.Audio.IConnector_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Disconnect(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def IsConnected(self, pbConnected: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetConnectedTo(self, ppConTo: POINTER(Windows.Win32.Media.Audio.IConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetConnectorIdConnectedTo(self, ppwstrConnectorId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def GetDeviceIdConnectedTo(self, ppwstrDeviceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
class IControlChangeNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a09513ed-c709-4d21-bd-7b-5f-34-c4-7f-39-47')
    @commethod(3)
    def OnNotify(self, dwSenderProcessId: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IControlInterface(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('45d37c3f-5140-444a-ae-24-40-07-89-f3-cb-f3')
    @commethod(3)
    def GetName(self, ppwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetIID(self, pIID: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeviceSpecificProperty(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('3b22bcbf-2586-4af0-85-83-20-5d-39-1b-80-7c')
    @commethod(3)
    def GetType(self, pVType: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetValue(self, pvValue: c_void_p, pcbValue: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetValue(self, pvValue: c_void_p, cbValue: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Get4BRange(self, plMin: POINTER(Int32), plMax: POINTER(Int32), plStepping: POINTER(Int32)) -> Windows.Win32.Foundation.HRESULT: ...
class IDeviceTopology(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('2a07407e-6497-4a18-97-87-32-f7-9b-d0-d9-8f')
    @commethod(3)
    def GetConnectorCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetConnector(self, nIndex: UInt32, ppConnector: POINTER(Windows.Win32.Media.Audio.IConnector_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetSubunitCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSubunit(self, nIndex: UInt32, ppSubunit: POINTER(Windows.Win32.Media.Audio.ISubunit_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetPartById(self, nId: UInt32, ppPart: POINTER(Windows.Win32.Media.Audio.IPart_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetDeviceId(self, ppwstrDeviceId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetSignalPath(self, pIPartFrom: Windows.Win32.Media.Audio.IPart_head, pIPartTo: Windows.Win32.Media.Audio.IPart_head, bRejectMixedPaths: Windows.Win32.Foundation.BOOL, ppParts: POINTER(Windows.Win32.Media.Audio.IPartsList_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMMDevice(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d666063f-1587-4e43-81-f1-b9-48-e8-07-36-3f')
    @commethod(3)
    def Activate(self, iid: POINTER(Guid), dwClsCtx: Windows.Win32.System.Com.CLSCTX, pActivationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppInterface: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OpenPropertyStore(self, stgmAccess: Windows.Win32.System.Com.STGM, ppProperties: POINTER(Windows.Win32.UI.Shell.PropertiesSystem.IPropertyStore_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetId(self, ppstrId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetState(self, pdwState: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceActivator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('3b0d0ea4-d0a9-4b0e-93-5b-09-51-67-46-fa-c0')
    @commethod(3)
    def Activate(self, iid: POINTER(Guid), pDevice: Windows.Win32.Media.Audio.IMMDevice_head, pActivationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), ppInterface: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceCollection(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('0bd7a1be-7a1a-44db-83-97-cc-53-92-38-7b-5e')
    @commethod(3)
    def GetCount(self, pcDevices: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def Item(self, nDevice: UInt32, ppDevice: POINTER(Windows.Win32.Media.Audio.IMMDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IMMDeviceEnumerator(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('a95664d2-9614-4f35-a7-46-de-8d-b6-36-17-e6')
    @commethod(3)
    def EnumAudioEndpoints(self, dataFlow: Windows.Win32.Media.Audio.EDataFlow, dwStateMask: UInt32, ppDevices: POINTER(Windows.Win32.Media.Audio.IMMDeviceCollection_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetDefaultAudioEndpoint(self, dataFlow: Windows.Win32.Media.Audio.EDataFlow, role: Windows.Win32.Media.Audio.ERole, ppEndpoint: POINTER(Windows.Win32.Media.Audio.IMMDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetDevice(self, pwstrId: Windows.Win32.Foundation.PWSTR, ppDevice: POINTER(Windows.Win32.Media.Audio.IMMDevice_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def RegisterEndpointNotificationCallback(self, pClient: Windows.Win32.Media.Audio.IMMNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def UnregisterEndpointNotificationCallback(self, pClient: Windows.Win32.Media.Audio.IMMNotificationClient_head) -> Windows.Win32.Foundation.HRESULT: ...
class IMMEndpoint(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1be09788-6894-4089-85-86-9a-2a-6c-26-5a-c5')
    @commethod(3)
    def GetDataFlow(self, pDataFlow: POINTER(Windows.Win32.Media.Audio.EDataFlow)) -> Windows.Win32.Foundation.HRESULT: ...
class IMMNotificationClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('7991eec9-7e89-4d85-83-90-6c-70-3c-ec-60-c0')
    @commethod(3)
    def OnDeviceStateChanged(self, pwstrDeviceId: Windows.Win32.Foundation.PWSTR, dwNewState: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def OnDeviceAdded(self, pwstrDeviceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def OnDeviceRemoved(self, pwstrDeviceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def OnDefaultDeviceChanged(self, flow: Windows.Win32.Media.Audio.EDataFlow, role: Windows.Win32.Media.Audio.ERole, pwstrDefaultDeviceId: Windows.Win32.Foundation.PWSTR) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def OnPropertyValueChanged(self, pwstrDeviceId: Windows.Win32.Foundation.PWSTR, key: Windows.Win32.UI.Shell.PropertiesSystem.PROPERTYKEY) -> Windows.Win32.Foundation.HRESULT: ...
class IMessageFilter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('00000016-0000-0000-c0-00-00-00-00-00-00-46')
    @commethod(3)
    def HandleInComingCall(self, dwCallType: UInt32, htaskCaller: Windows.Win32.Media.HTASK, dwTickCount: UInt32, lpInterfaceInfo: POINTER(Windows.Win32.System.Com.INTERFACEINFO_head)) -> UInt32: ...
    @commethod(4)
    def RetryRejectedCall(self, htaskCallee: Windows.Win32.Media.HTASK, dwTickCount: UInt32, dwRejectType: UInt32) -> UInt32: ...
    @commethod(5)
    def MessagePending(self, htaskCallee: Windows.Win32.Media.HTASK, dwTickCount: UInt32, dwPendingType: UInt32) -> UInt32: ...
class IPart(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('ae2de0e4-5bca-4f2d-aa-46-5d-13-f8-fd-b3-a9')
    @commethod(3)
    def GetName(self, ppwstrName: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLocalId(self, pnId: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetGlobalId(self, ppwstrGlobalId: POINTER(Windows.Win32.Foundation.PWSTR)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetPartType(self, pPartType: POINTER(Windows.Win32.Media.Audio.PartType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetSubType(self, pSubType: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def GetControlInterfaceCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def GetControlInterface(self, nIndex: UInt32, ppInterfaceDesc: POINTER(Windows.Win32.Media.Audio.IControlInterface_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def EnumPartsIncoming(self, ppParts: POINTER(Windows.Win32.Media.Audio.IPartsList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def EnumPartsOutgoing(self, ppParts: POINTER(Windows.Win32.Media.Audio.IPartsList_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetTopologyObject(self, ppTopology: POINTER(Windows.Win32.Media.Audio.IDeviceTopology_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(13)
    def Activate(self, dwClsContext: UInt32, refiid: POINTER(Guid), ppvObject: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(14)
    def RegisterControlChangeCallback(self, riid: POINTER(Guid), pNotify: Windows.Win32.Media.Audio.IControlChangeNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(15)
    def UnregisterControlChangeCallback(self, pNotify: Windows.Win32.Media.Audio.IControlChangeNotify_head) -> Windows.Win32.Foundation.HRESULT: ...
class IPartsList(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('6daa848c-5eb0-45cc-ae-a5-99-8a-2c-da-1f-fb')
    @commethod(3)
    def GetCount(self, pCount: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetPart(self, nIndex: UInt32, ppPart: POINTER(Windows.Win32.Media.Audio.IPart_head)) -> Windows.Win32.Foundation.HRESULT: ...
class IPerChannelDbLevel(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('c2f8e001-f205-4bc9-99-bc-c1-3b-1e-04-8c-cb')
    @commethod(3)
    def GetChannelCount(self, pcChannels: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetLevelRange(self, nChannel: UInt32, pfMinLevelDB: POINTER(Single), pfMaxLevelDB: POINTER(Single), pfStepping: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetLevel(self, nChannel: UInt32, pfLevelDB: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def SetLevel(self, nChannel: UInt32, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def SetLevelUniform(self, fLevelDB: Single, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetLevelAllChannels(self, aLevelsDB: POINTER(Single), cChannels: UInt32, pguidEventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
class ISimpleAudioVolume(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('87ce5498-68d6-44e5-92-15-6d-a4-7e-f8-83-d8')
    @commethod(3)
    def SetMasterVolume(self, fLevel: Single, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetMasterVolume(self, pfLevel: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def SetMute(self, bMute: Windows.Win32.Foundation.BOOL, EventContext: POINTER(Guid)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMute(self, pbMute: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bbf8e066-aaaa-49be-9a-4d-fd-2a-85-8e-a2-7f')
    @commethod(3)
    def GetStaticObjectPosition(self, type: Windows.Win32.Media.Audio.AudioObjectType, x: POINTER(Single), y: POINTER(Single), z: POINTER(Single)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetNativeStaticObjectTypeMask(self, mask: POINTER(Windows.Win32.Media.Audio.AudioObjectType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxDynamicObjectCount(self, value: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetSupportedAudioObjectFormatEnumerator(self, enumerator: POINTER(Windows.Win32.Media.Audio.IAudioFormatEnumerator_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetMaxFrameCount(self, objectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), frameCountPerBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def IsAudioObjectFormatSupported(self, objectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def IsSpatialAudioStreamAvailable(self, streamUuid: POINTER(Guid), auxiliaryInfo: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def ActivateSpatialAudioStream(self, activationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head), riid: POINTER(Guid), stream: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioClient2(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioClient
    _iid_ = Guid('caabe452-a66a-4bee-a9-3e-e3-20-46-3f-6a-53')
    @commethod(11)
    def IsOffloadCapable(self, category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, isOffloadCapable: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def GetMaxFrameCountForCategory(self, category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY, offloadEnabled: Windows.Win32.Foundation.BOOL, objectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head), frameCountPerBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataClient(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('777d4a3b-f6ff-4a26-85-dc-68-d7-cd-ed-a1-d4')
    @commethod(3)
    def ActivateSpatialAudioMetadataItems(self, maxItemCount: UInt16, frameCount: UInt16, metadataItemsBuffer: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataItemsBuffer_head), metadataItems: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetSpatialAudioMetadataItemsBufferLength(self, maxItemCount: UInt16, bufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ActivateSpatialAudioMetadataWriter(self, overflowMode: Windows.Win32.Media.Audio.SpatialAudioMetadataWriterOverflowMode, metadataWriter: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataWriter_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def ActivateSpatialAudioMetadataCopier(self, metadataCopier: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataCopier_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ActivateSpatialAudioMetadataReader(self, metadataReader: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataReader_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataCopier(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('d224b233-e251-4fd0-9c-a2-d5-ec-f9-a6-84-04')
    @commethod(3)
    def Open(self, metadataItems: Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CopyMetadataForFrames(self, copyFrameCount: UInt16, copyMode: Windows.Win32.Media.Audio.SpatialAudioMetadataCopyMode, dstMetadataItems: Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head, itemsCopied: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataItems(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('bcd7c78f-3098-4f22-b5-47-a2-f2-5a-38-12-69')
    @commethod(3)
    def GetFrameCount(self, frameCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetItemCount(self, itemCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def GetMaxItemCount(self, maxItemCount: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetMaxValueBufferLength(self, maxValueBufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def GetInfo(self, info: POINTER(Windows.Win32.Media.Audio.SpatialAudioMetadataItemsInfo_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataItemsBuffer(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('42640a16-e1bd-42d9-9f-f6-03-1a-b7-1a-2d-ba')
    @commethod(3)
    def AttachToBuffer(self, buffer: POINTER(Byte), bufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def AttachToPopulatedBuffer(self, buffer: POINTER(Byte), bufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def DetachBuffer(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataReader(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('b78e86a2-31d9-4c32-94-d2-7d-f4-0f-c7-eb-ec')
    @commethod(3)
    def Open(self, metadataItems: Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def ReadNextItem(self, commandCount: POINTER(Byte), frameOffset: POINTER(UInt16)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def ReadNextItemCommand(self, commandID: POINTER(Byte), valueBuffer: c_void_p, maxValueBufferLength: UInt32, valueBufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioMetadataWriter(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('1b17ca01-2955-444d-a4-30-53-7d-c5-89-a8-44')
    @commethod(3)
    def Open(self, metadataItems: Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def WriteNextItem(self, frameOffset: UInt16) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def WriteNextItemCommand(self, commandID: Byte, valueBuffer: c_void_p, valueBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Close(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObject(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('dde28967-521b-46e5-8f-00-bd-6f-2b-c8-ab-1d')
    @commethod(7)
    def SetPosition(self, x: Single, y: Single, z: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetVolume(self, volume: Single) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectBase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('cce0b8f2-8d4d-4efb-a8-cf-3d-6e-cf-1c-30-e0')
    @commethod(3)
    def GetBuffer(self, buffer: POINTER(POINTER(Byte)), bufferLength: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetEndOfStream(self, frameCount: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def IsActive(self, isActive: POINTER(Windows.Win32.Foundation.BOOL)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def GetAudioObjectType(self, audioObjectType: POINTER(Windows.Win32.Media.Audio.AudioObjectType)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForHrtf(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('d7436ade-1978-4e14-ab-a0-55-5b-d8-eb-83-b4')
    @commethod(7)
    def SetPosition(self, x: Single, y: Single, z: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SetGain(self, gain: Single) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def SetOrientation(self, orientation: POINTER(POINTER(Single))) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(10)
    def SetEnvironment(self, environment: Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def SetDistanceDecay(self, distanceDecay: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(12)
    def SetDirectivity(self, directivity: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForMetadataCommands(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('0df2c94b-f5f9-472d-af-6b-c4-6e-0a-c9-cd-05')
    @commethod(7)
    def WriteNextMetadataCommand(self, commandID: Byte, valueBuffer: c_void_p, valueBufferLength: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectForMetadataItems(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectBase
    _iid_ = Guid('ddea49ff-3bc0-4377-8a-ad-9f-bc-fd-80-85-66')
    @commethod(7)
    def GetSpatialAudioMetadataItems(self, metadataItems: POINTER(Windows.Win32.Media.Audio.ISpatialAudioMetadataItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStream(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('bab5f473-b423-477b-85-f5-b5-a3-32-a0-41-53')
    @commethod(10)
    def ActivateSpatialAudioObject(self, type: Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(Windows.Win32.Media.Audio.ISpatialAudioObject_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamBase(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('feaaf403-c1d8-450d-aa-05-e0-cc-ee-75-02-a8')
    @commethod(3)
    def GetAvailableDynamicObjectCount(self, value: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def GetService(self, riid: POINTER(Guid), service: POINTER(c_void_p)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Start(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Stop(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def Reset(self) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def BeginUpdatingAudioObjects(self, availableDynamicObjectCount: POINTER(UInt32), frameCountPerBuffer: POINTER(UInt32)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(9)
    def EndUpdatingAudioObjects(self) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamForHrtf(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('e08deef9-5363-406e-9f-dc-08-0e-e2-47-bb-e0')
    @commethod(10)
    def ActivateSpatialAudioObjectForHrtf(self, type: Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(Windows.Win32.Media.Audio.ISpatialAudioObjectForHrtf_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamForMetadata(ComPtr):
    extends: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase
    _iid_ = Guid('bbc9c907-48d5-4a2e-a0-c7-f7-f0-d6-7c-1f-b1')
    @commethod(10)
    def ActivateSpatialAudioObjectForMetadataCommands(self, type: Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(Windows.Win32.Media.Audio.ISpatialAudioObjectForMetadataCommands_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(11)
    def ActivateSpatialAudioObjectForMetadataItems(self, type: Windows.Win32.Media.Audio.AudioObjectType, audioObject: POINTER(Windows.Win32.Media.Audio.ISpatialAudioObjectForMetadataItems_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ISpatialAudioObjectRenderStreamNotify(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('dddf83e6-68d7-4c70-88-3f-a1-83-6a-fb-4a-50')
    @commethod(3)
    def OnAvailableDynamicObjectCountChange(self, sender: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamBase_head, hnsComplianceDeadlineTime: Int64, availableDynamicObjectCountChange: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ISubunit(ComPtr):
    extends: Windows.Win32.System.Com.IUnknown
    _iid_ = Guid('82149a85-dba6-4487-86-bb-ea-8f-7f-ef-cc-71')
@winfunctype_pointer
def LPACMDRIVERPROC(param0: UIntPtr, param1: Windows.Win32.Media.Audio.HACMDRIVERID, param2: UInt32, param3: Windows.Win32.Foundation.LPARAM, param4: Windows.Win32.Foundation.LPARAM) -> Windows.Win32.Foundation.LRESULT: ...
@winfunctype_pointer
def LPMIDICALLBACK(hdrvr: Windows.Win32.Media.Multimedia.HDRVR, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
@winfunctype_pointer
def LPWAVECALLBACK(hdrvr: Windows.Win32.Media.Multimedia.HDRVR, uMsg: UInt32, dwUser: UIntPtr, dw1: UIntPtr, dw2: UIntPtr) -> Void: ...
class MIDIEVENT(EasyCastStructure):
    dwDeltaTime: UInt32
    dwStreamID: UInt32
    dwEvent: UInt32
    dwParms: UInt32 * 1
    _pack_ = 1
class MIDIHDR(EasyCastStructure):
    lpData: Windows.Win32.Foundation.PSTR
    dwBufferLength: UInt32
    dwBytesRecorded: UInt32
    dwUser: UIntPtr
    dwFlags: UInt32
    lpNext: POINTER(Windows.Win32.Media.Audio.MIDIHDR_head)
    reserved: UIntPtr
    dwOffset: UInt32
    dwReserved: UIntPtr * 8
    _pack_ = 1
class MIDIINCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIINCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIINCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwSupport: UInt32
    _pack_ = 1
class MIDIINCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwSupport: UInt32
    _pack_ = 1
class MIDIOUTCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIOUTCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIDIOUTCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    _pack_ = 1
class MIDIOUTCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    wTechnology: UInt16
    wVoices: UInt16
    wNotes: UInt16
    wChannelMask: UInt16
    dwSupport: UInt32
    _pack_ = 1
class MIDIPROPTEMPO(EasyCastStructure):
    cbStruct: UInt32
    dwTempo: UInt32
    _pack_ = 1
class MIDIPROPTIMEDIV(EasyCastStructure):
    cbStruct: UInt32
    dwTimeDiv: UInt32
    _pack_ = 1
class MIDISTRMBUFFVER(EasyCastStructure):
    dwVersion: UInt32
    dwMid: UInt32
    dwOEMVersion: UInt32
    _pack_ = 1
MIDI_WAVE_OPEN_TYPE = UInt32
CALLBACK_TYPEMASK: MIDI_WAVE_OPEN_TYPE = 458752
CALLBACK_NULL: MIDI_WAVE_OPEN_TYPE = 0
CALLBACK_WINDOW: MIDI_WAVE_OPEN_TYPE = 65536
CALLBACK_TASK: MIDI_WAVE_OPEN_TYPE = 131072
CALLBACK_FUNCTION: MIDI_WAVE_OPEN_TYPE = 196608
CALLBACK_THREAD: MIDI_WAVE_OPEN_TYPE = 131072
CALLBACK_EVENT: MIDI_WAVE_OPEN_TYPE = 327680
WAVE_FORMAT_QUERY: MIDI_WAVE_OPEN_TYPE = 1
WAVE_ALLOWSYNC: MIDI_WAVE_OPEN_TYPE = 2
WAVE_MAPPED: MIDI_WAVE_OPEN_TYPE = 4
WAVE_FORMAT_DIRECT: MIDI_WAVE_OPEN_TYPE = 8
WAVE_FORMAT_DIRECT_QUERY: MIDI_WAVE_OPEN_TYPE = 9
WAVE_MAPPED_DEFAULT_COMMUNICATION_DEVICE: MIDI_WAVE_OPEN_TYPE = 16
MIDI_IO_STATUS: MIDI_WAVE_OPEN_TYPE = 32
class MIXERCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIXERCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class MIXERCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    _pack_ = 1
class MIXERCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    fdwSupport: UInt32
    cDestinations: UInt32
    _pack_ = 1
class MIXERCONTROLA(EasyCastStructure):
    cbStruct: UInt32
    dwControlID: UInt32
    dwControlType: UInt32
    fdwControl: UInt32
    cMultipleItems: UInt32
    szShortName: Windows.Win32.Foundation.CHAR * 16
    szName: Windows.Win32.Foundation.CHAR * 64
    Bounds: _Bounds_e__Union
    Metrics: _Metrics_e__Union
    _pack_ = 1
    class _Bounds_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        dwReserved: UInt32 * 6
        _pack_ = 1
        class _Anonymous1_e__Struct(EasyCastStructure):
            lMinimum: Int32
            lMaximum: Int32
            _pack_ = 1
        class _Anonymous2_e__Struct(EasyCastStructure):
            dwMinimum: UInt32
            dwMaximum: UInt32
            _pack_ = 1
    class _Metrics_e__Union(EasyCastUnion):
        cSteps: UInt32
        cbCustomData: UInt32
        dwReserved: UInt32 * 6
        _pack_ = 1
class MIXERCONTROLDETAILS(EasyCastStructure):
    cbStruct: UInt32
    dwControlID: UInt32
    cChannels: UInt32
    Anonymous: _Anonymous_e__Union
    cbDetails: UInt32
    paDetails: c_void_p
    _pack_ = 1
    class _Anonymous_e__Union(EasyCastUnion):
        hwndOwner: Windows.Win32.Foundation.HWND
        cMultipleItems: UInt32
        _pack_ = 1
class MIXERCONTROLDETAILS_BOOLEAN(EasyCastStructure):
    fValue: Int32
    _pack_ = 1
class MIXERCONTROLDETAILS_LISTTEXTA(EasyCastStructure):
    dwParam1: UInt32
    dwParam2: UInt32
    szName: Windows.Win32.Foundation.CHAR * 64
    _pack_ = 1
class MIXERCONTROLDETAILS_LISTTEXTW(EasyCastStructure):
    dwParam1: UInt32
    dwParam2: UInt32
    szName: Char * 64
    _pack_ = 1
class MIXERCONTROLDETAILS_SIGNED(EasyCastStructure):
    lValue: Int32
    _pack_ = 1
class MIXERCONTROLDETAILS_UNSIGNED(EasyCastStructure):
    dwValue: UInt32
    _pack_ = 1
class MIXERCONTROLW(EasyCastStructure):
    cbStruct: UInt32
    dwControlID: UInt32
    dwControlType: UInt32
    fdwControl: UInt32
    cMultipleItems: UInt32
    szShortName: Char * 16
    szName: Char * 64
    Bounds: _Bounds_e__Union
    Metrics: _Metrics_e__Union
    _pack_ = 1
    class _Bounds_e__Union(EasyCastUnion):
        Anonymous1: _Anonymous1_e__Struct
        Anonymous2: _Anonymous2_e__Struct
        dwReserved: UInt32 * 6
        _pack_ = 1
        class _Anonymous1_e__Struct(EasyCastStructure):
            lMinimum: Int32
            lMaximum: Int32
            _pack_ = 1
        class _Anonymous2_e__Struct(EasyCastStructure):
            dwMinimum: UInt32
            dwMaximum: UInt32
            _pack_ = 1
    class _Metrics_e__Union(EasyCastUnion):
        cSteps: UInt32
        cbCustomData: UInt32
        dwReserved: UInt32 * 6
        _pack_ = 1
class MIXERLINEA(EasyCastStructure):
    cbStruct: UInt32
    dwDestination: UInt32
    dwSource: UInt32
    dwLineID: UInt32
    fdwLine: UInt32
    dwUser: UIntPtr
    dwComponentType: Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE
    cChannels: UInt32
    cConnections: UInt32
    cControls: UInt32
    szShortName: Windows.Win32.Foundation.CHAR * 16
    szName: Windows.Win32.Foundation.CHAR * 64
    Target: _Target_e__Struct
    _pack_ = 1
    class _Target_e__Struct(EasyCastStructure):
        dwType: UInt32
        dwDeviceID: UInt32
        wMid: UInt16
        wPid: UInt16
        vDriverVersion: UInt32
        szPname: Windows.Win32.Foundation.CHAR * 32
        _pack_ = 1
class MIXERLINECONTROLSA(EasyCastStructure):
    cbStruct: UInt32
    dwLineID: UInt32
    Anonymous: _Anonymous_e__Union
    cControls: UInt32
    cbmxctrl: UInt32
    pamxctrl: POINTER(Windows.Win32.Media.Audio.MIXERCONTROLA_head)
    _pack_ = 1
    class _Anonymous_e__Union(EasyCastUnion):
        dwControlID: UInt32
        dwControlType: UInt32
        _pack_ = 1
class MIXERLINECONTROLSW(EasyCastStructure):
    cbStruct: UInt32
    dwLineID: UInt32
    Anonymous: _Anonymous_e__Union
    cControls: UInt32
    cbmxctrl: UInt32
    pamxctrl: POINTER(Windows.Win32.Media.Audio.MIXERCONTROLW_head)
    _pack_ = 1
    class _Anonymous_e__Union(EasyCastUnion):
        dwControlID: UInt32
        dwControlType: UInt32
        _pack_ = 1
class MIXERLINEW(EasyCastStructure):
    cbStruct: UInt32
    dwDestination: UInt32
    dwSource: UInt32
    dwLineID: UInt32
    fdwLine: UInt32
    dwUser: UIntPtr
    dwComponentType: Windows.Win32.Media.Audio.MIXERLINE_COMPONENTTYPE
    cChannels: UInt32
    cConnections: UInt32
    cControls: UInt32
    szShortName: Char * 16
    szName: Char * 64
    Target: _Target_e__Struct
    _pack_ = 1
    class _Target_e__Struct(EasyCastStructure):
        dwType: UInt32
        dwDeviceID: UInt32
        wMid: UInt16
        wPid: UInt16
        vDriverVersion: UInt32
        szPname: Char * 32
        _pack_ = 1
MIXERLINE_COMPONENTTYPE = UInt32
MIXERLINE_COMPONENTTYPE_DST_DIGITAL: MIXERLINE_COMPONENTTYPE = 1
MIXERLINE_COMPONENTTYPE_DST_HEADPHONES: MIXERLINE_COMPONENTTYPE = 5
MIXERLINE_COMPONENTTYPE_DST_LINE: MIXERLINE_COMPONENTTYPE = 2
MIXERLINE_COMPONENTTYPE_DST_MONITOR: MIXERLINE_COMPONENTTYPE = 3
MIXERLINE_COMPONENTTYPE_DST_SPEAKERS: MIXERLINE_COMPONENTTYPE = 4
MIXERLINE_COMPONENTTYPE_DST_TELEPHONE: MIXERLINE_COMPONENTTYPE = 6
MIXERLINE_COMPONENTTYPE_DST_UNDEFINED: MIXERLINE_COMPONENTTYPE = 0
MIXERLINE_COMPONENTTYPE_DST_VOICEIN: MIXERLINE_COMPONENTTYPE = 8
MIXERLINE_COMPONENTTYPE_DST_WAVEIN: MIXERLINE_COMPONENTTYPE = 7
MIXERLINE_COMPONENTTYPE_SRC_ANALOG: MIXERLINE_COMPONENTTYPE = 4106
MIXERLINE_COMPONENTTYPE_SRC_AUXILIARY: MIXERLINE_COMPONENTTYPE = 4105
MIXERLINE_COMPONENTTYPE_SRC_COMPACTDISC: MIXERLINE_COMPONENTTYPE = 4101
MIXERLINE_COMPONENTTYPE_SRC_DIGITAL: MIXERLINE_COMPONENTTYPE = 4097
MIXERLINE_COMPONENTTYPE_SRC_LINE: MIXERLINE_COMPONENTTYPE = 4098
MIXERLINE_COMPONENTTYPE_SRC_MICROPHONE: MIXERLINE_COMPONENTTYPE = 4099
MIXERLINE_COMPONENTTYPE_SRC_PCSPEAKER: MIXERLINE_COMPONENTTYPE = 4103
MIXERLINE_COMPONENTTYPE_SRC_SYNTHESIZER: MIXERLINE_COMPONENTTYPE = 4100
MIXERLINE_COMPONENTTYPE_SRC_TELEPHONE: MIXERLINE_COMPONENTTYPE = 4102
MIXERLINE_COMPONENTTYPE_SRC_UNDEFINED: MIXERLINE_COMPONENTTYPE = 4096
MIXERLINE_COMPONENTTYPE_SRC_WAVEOUT: MIXERLINE_COMPONENTTYPE = 4104
MMDeviceEnumerator = Guid('bcde0395-e52f-467c-8e-3d-c4-57-92-91-69-2e')
@winfunctype_pointer
def PAudioStateMonitorCallback(audioStateMonitor: Windows.Win32.Media.Audio.IAudioStateMonitor_head, context: c_void_p) -> Void: ...
class PCMWAVEFORMAT(EasyCastStructure):
    wf: Windows.Win32.Media.Audio.WAVEFORMAT
    wBitsPerSample: UInt16
    _pack_ = 1
PROCESS_LOOPBACK_MODE = Int32
PROCESS_LOOPBACK_MODE_INCLUDE_TARGET_PROCESS_TREE: PROCESS_LOOPBACK_MODE = 0
PROCESS_LOOPBACK_MODE_EXCLUDE_TARGET_PROCESS_TREE: PROCESS_LOOPBACK_MODE = 1
PartType = Int32
PartType_Connector: PartType = 0
PartType_Subunit: PartType = 1
SND_FLAGS = UInt32
SND_APPLICATION: SND_FLAGS = 128
SND_ALIAS: SND_FLAGS = 65536
SND_ALIAS_ID: SND_FLAGS = 1114112
SND_FILENAME: SND_FLAGS = 131072
SND_RESOURCE: SND_FLAGS = 262148
SND_ASYNC: SND_FLAGS = 1
SND_NODEFAULT: SND_FLAGS = 2
SND_LOOP: SND_FLAGS = 8
SND_MEMORY: SND_FLAGS = 4
SND_NOSTOP: SND_FLAGS = 16
SND_NOWAIT: SND_FLAGS = 8192
SND_PURGE: SND_FLAGS = 64
SND_SENTRY: SND_FLAGS = 524288
SND_SYNC: SND_FLAGS = 0
SND_SYSTEM: SND_FLAGS = 2097152
SPATIAL_AUDIO_STREAM_OPTIONS = Int32
SPATIAL_AUDIO_STREAM_OPTIONS_NONE: SPATIAL_AUDIO_STREAM_OPTIONS = 0
SPATIAL_AUDIO_STREAM_OPTIONS_OFFLOAD: SPATIAL_AUDIO_STREAM_OPTIONS = 1
class SpatialAudioClientActivationParams(EasyCastStructure):
    tracingContextId: Guid
    appId: Guid
    majorVersion: Int32
    minorVersion1: Int32
    minorVersion2: Int32
    minorVersion3: Int32
class SpatialAudioHrtfActivationParams(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    DistanceDecay: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay_head)
    Directivity: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion_head)
    Environment: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType)
    Orientation: POINTER(Single)
    _pack_ = 1
class SpatialAudioHrtfActivationParams2(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    DistanceDecay: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecay_head)
    Directivity: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityUnion_head)
    Environment: POINTER(Windows.Win32.Media.Audio.SpatialAudioHrtfEnvironmentType)
    Orientation: POINTER(Single)
    Options: Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class SpatialAudioHrtfDirectivity(EasyCastStructure):
    Type: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityType
    Scaling: Single
    _pack_ = 1
class SpatialAudioHrtfDirectivityCardioid(EasyCastStructure):
    directivity: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
    Order: Single
    _pack_ = 1
class SpatialAudioHrtfDirectivityCone(EasyCastStructure):
    directivity: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
    InnerAngle: Single
    OuterAngle: Single
    _pack_ = 1
SpatialAudioHrtfDirectivityType = Int32
SpatialAudioHrtfDirectivity_OmniDirectional: SpatialAudioHrtfDirectivityType = 0
SpatialAudioHrtfDirectivity_Cardioid: SpatialAudioHrtfDirectivityType = 1
SpatialAudioHrtfDirectivity_Cone: SpatialAudioHrtfDirectivityType = 2
class SpatialAudioHrtfDirectivityUnion(EasyCastUnion):
    Cone: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityCone
    Cardiod: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivityCardioid
    Omni: Windows.Win32.Media.Audio.SpatialAudioHrtfDirectivity
class SpatialAudioHrtfDistanceDecay(EasyCastStructure):
    Type: Windows.Win32.Media.Audio.SpatialAudioHrtfDistanceDecayType
    MaxGain: Single
    MinGain: Single
    UnityGainDistance: Single
    CutoffDistance: Single
    _pack_ = 1
SpatialAudioHrtfDistanceDecayType = Int32
SpatialAudioHrtfDistanceDecay_NaturalDecay: SpatialAudioHrtfDistanceDecayType = 0
SpatialAudioHrtfDistanceDecay_CustomDecay: SpatialAudioHrtfDistanceDecayType = 1
SpatialAudioHrtfEnvironmentType = Int32
SpatialAudioHrtfEnvironment_Small: SpatialAudioHrtfEnvironmentType = 0
SpatialAudioHrtfEnvironment_Medium: SpatialAudioHrtfEnvironmentType = 1
SpatialAudioHrtfEnvironment_Large: SpatialAudioHrtfEnvironmentType = 2
SpatialAudioHrtfEnvironment_Outdoors: SpatialAudioHrtfEnvironmentType = 3
SpatialAudioHrtfEnvironment_Average: SpatialAudioHrtfEnvironmentType = 4
SpatialAudioMetadataCopyMode = Int32
SpatialAudioMetadataCopy_Overwrite: SpatialAudioMetadataCopyMode = 0
SpatialAudioMetadataCopy_Append: SpatialAudioMetadataCopyMode = 1
SpatialAudioMetadataCopy_AppendMergeWithLast: SpatialAudioMetadataCopyMode = 2
SpatialAudioMetadataCopy_AppendMergeWithFirst: SpatialAudioMetadataCopyMode = 3
class SpatialAudioMetadataItemsInfo(EasyCastStructure):
    FrameCount: UInt16
    ItemCount: UInt16
    MaxItemCount: UInt16
    MaxValueBufferLength: UInt32
    _pack_ = 1
SpatialAudioMetadataWriterOverflowMode = Int32
SpatialAudioMetadataWriterOverflow_Fail: SpatialAudioMetadataWriterOverflowMode = 0
SpatialAudioMetadataWriterOverflow_MergeWithNew: SpatialAudioMetadataWriterOverflowMode = 1
SpatialAudioMetadataWriterOverflow_MergeWithLast: SpatialAudioMetadataWriterOverflowMode = 2
class SpatialAudioObjectRenderStreamActivationParams(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    _pack_ = 1
class SpatialAudioObjectRenderStreamActivationParams2(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    Options: Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class SpatialAudioObjectRenderStreamForMetadataActivationParams(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    MetadataFormatId: Guid
    MaxMetadataItemCount: UInt16
    MetadataActivationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    _pack_ = 1
class SpatialAudioObjectRenderStreamForMetadataActivationParams2(EasyCastStructure):
    ObjectFormat: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    StaticObjectTypeMask: Windows.Win32.Media.Audio.AudioObjectType
    MinDynamicObjectCount: UInt32
    MaxDynamicObjectCount: UInt32
    Category: Windows.Win32.Media.Audio.AUDIO_STREAM_CATEGORY
    EventHandle: Windows.Win32.Foundation.HANDLE
    MetadataFormatId: Guid
    MaxMetadataItemCount: UInt32
    MetadataActivationParams: POINTER(Windows.Win32.System.Com.StructuredStorage.PROPVARIANT_head)
    NotifyObject: Windows.Win32.Media.Audio.ISpatialAudioObjectRenderStreamNotify_head
    Options: Windows.Win32.Media.Audio.SPATIAL_AUDIO_STREAM_OPTIONS
    _pack_ = 1
class VOLUMEWAVEFILTER(EasyCastStructure):
    wfltr: Windows.Win32.Media.Audio.WAVEFILTER
    dwVolume: UInt32
    _pack_ = 1
class WAVEFILTER(EasyCastStructure):
    cbStruct: UInt32
    dwFilterTag: UInt32
    fdwFilter: UInt32
    dwReserved: UInt32 * 5
    _pack_ = 1
class WAVEFORMAT(EasyCastStructure):
    wFormatTag: UInt16
    nChannels: UInt16
    nSamplesPerSec: UInt32
    nAvgBytesPerSec: UInt32
    nBlockAlign: UInt16
    _pack_ = 1
class WAVEFORMATEX(EasyCastStructure):
    wFormatTag: UInt16
    nChannels: UInt16
    nSamplesPerSec: UInt32
    nAvgBytesPerSec: UInt32
    nBlockAlign: UInt16
    wBitsPerSample: UInt16
    cbSize: UInt16
    _pack_ = 1
class WAVEFORMATEXTENSIBLE(EasyCastStructure):
    Format: Windows.Win32.Media.Audio.WAVEFORMATEX
    Samples: _Samples_e__Union
    dwChannelMask: UInt32
    SubFormat: Guid
    _pack_ = 1
    class _Samples_e__Union(EasyCastUnion):
        wValidBitsPerSample: UInt16
        wSamplesPerBlock: UInt16
        wReserved: UInt16
        _pack_ = 1
class WAVEHDR(EasyCastStructure):
    lpData: Windows.Win32.Foundation.PSTR
    dwBufferLength: UInt32
    dwBytesRecorded: UInt32
    dwUser: UIntPtr
    dwFlags: UInt32
    dwLoops: UInt32
    lpNext: POINTER(Windows.Win32.Media.Audio.WAVEHDR_head)
    reserved: UIntPtr
    _pack_ = 1
class WAVEINCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEINCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEINCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    _pack_ = 1
class WAVEINCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    _pack_ = 1
class WAVEOUTCAPS2A(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEOUTCAPS2W(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    ManufacturerGuid: Guid
    ProductGuid: Guid
    NameGuid: Guid
    _pack_ = 1
class WAVEOUTCAPSA(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Windows.Win32.Foundation.CHAR * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
class WAVEOUTCAPSW(EasyCastStructure):
    wMid: UInt16
    wPid: UInt16
    vDriverVersion: UInt32
    szPname: Char * 32
    dwFormats: UInt32
    wChannels: UInt16
    wReserved1: UInt16
    dwSupport: UInt32
    _pack_ = 1
_AUDCLNT_BUFFERFLAGS = Int32
AUDCLNT_BUFFERFLAGS_DATA_DISCONTINUITY: _AUDCLNT_BUFFERFLAGS = 1
AUDCLNT_BUFFERFLAGS_SILENT: _AUDCLNT_BUFFERFLAGS = 2
AUDCLNT_BUFFERFLAGS_TIMESTAMP_ERROR: _AUDCLNT_BUFFERFLAGS = 4
class tACMFORMATDETAILSW(EasyCastStructure):
    cbStruct: UInt32
    dwFormatIndex: UInt32
    dwFormatTag: UInt32
    fdwSupport: UInt32
    pwfx: POINTER(Windows.Win32.Media.Audio.WAVEFORMATEX_head)
    cbwfx: UInt32
    szFormat: Char * 128
    _pack_ = 1
make_head(_module, 'ACMDRIVERDETAILSA')
make_head(_module, 'ACMDRIVERDETAILSW')
make_head(_module, 'ACMDRIVERENUMCB')
make_head(_module, 'ACMDRVFORMATSUGGEST')
make_head(_module, 'ACMDRVOPENDESCA')
make_head(_module, 'ACMDRVOPENDESCW')
make_head(_module, 'ACMDRVSTREAMHEADER')
make_head(_module, 'ACMDRVSTREAMINSTANCE')
make_head(_module, 'ACMDRVSTREAMSIZE')
make_head(_module, 'ACMFILTERCHOOSEA')
make_head(_module, 'ACMFILTERCHOOSEHOOKPROCA')
make_head(_module, 'ACMFILTERCHOOSEHOOKPROCW')
make_head(_module, 'ACMFILTERCHOOSEW')
make_head(_module, 'ACMFILTERDETAILSA')
make_head(_module, 'ACMFILTERDETAILSW')
make_head(_module, 'ACMFILTERENUMCBA')
make_head(_module, 'ACMFILTERENUMCBW')
make_head(_module, 'ACMFILTERTAGDETAILSA')
make_head(_module, 'ACMFILTERTAGDETAILSW')
make_head(_module, 'ACMFILTERTAGENUMCBA')
make_head(_module, 'ACMFILTERTAGENUMCBW')
make_head(_module, 'ACMFORMATCHOOSEA')
make_head(_module, 'ACMFORMATCHOOSEHOOKPROCA')
make_head(_module, 'ACMFORMATCHOOSEHOOKPROCW')
make_head(_module, 'ACMFORMATCHOOSEW')
make_head(_module, 'ACMFORMATDETAILSA')
make_head(_module, 'ACMFORMATENUMCBA')
make_head(_module, 'ACMFORMATENUMCBW')
make_head(_module, 'ACMFORMATTAGDETAILSA')
make_head(_module, 'ACMFORMATTAGDETAILSW')
make_head(_module, 'ACMFORMATTAGENUMCBA')
make_head(_module, 'ACMFORMATTAGENUMCBW')
if ARCH in 'X64,ARM64':
    make_head(_module, 'ACMSTREAMHEADER')
if ARCH in 'X86':
    make_head(_module, 'ACMSTREAMHEADER')
make_head(_module, 'AMBISONICS_PARAMS')
make_head(_module, 'AUDIOCLIENT_ACTIVATION_PARAMS')
make_head(_module, 'AUDIOCLIENT_PROCESS_LOOPBACK_PARAMS')
make_head(_module, 'AUDIO_EFFECT')
make_head(_module, 'AUDIO_VOLUME_NOTIFICATION_DATA')
make_head(_module, 'AUXCAPS2A')
make_head(_module, 'AUXCAPS2W')
make_head(_module, 'AUXCAPSA')
make_head(_module, 'AUXCAPSW')
make_head(_module, 'PKEY_AudioEndpoint_FormFactor')
make_head(_module, 'PKEY_AudioEndpoint_ControlPanelPageProvider')
make_head(_module, 'PKEY_AudioEndpoint_Association')
make_head(_module, 'PKEY_AudioEndpoint_PhysicalSpeakers')
make_head(_module, 'PKEY_AudioEndpoint_GUID')
make_head(_module, 'PKEY_AudioEndpoint_Disable_SysFx')
make_head(_module, 'PKEY_AudioEndpoint_FullRangeSpeakers')
make_head(_module, 'PKEY_AudioEndpoint_Supports_EventDriven_Mode')
make_head(_module, 'PKEY_AudioEndpoint_JackSubType')
make_head(_module, 'PKEY_AudioEndpoint_Default_VolumeInDb')
make_head(_module, 'PKEY_AudioEngine_DeviceFormat')
make_head(_module, 'PKEY_AudioEngine_OEMFormat')
make_head(_module, 'PKEY_AudioEndpointLogo_IconEffects')
make_head(_module, 'PKEY_AudioEndpointLogo_IconPath')
make_head(_module, 'PKEY_AudioEndpointSettings_MenuText')
make_head(_module, 'PKEY_AudioEndpointSettings_LaunchContract')
make_head(_module, 'AudioClient3ActivationParams')
make_head(_module, 'AudioClientProperties')
make_head(_module, 'AudioExtensionParams')
make_head(_module, 'DIRECTX_AUDIO_ACTIVATION_PARAMS')
make_head(_module, 'ECHOWAVEFILTER')
make_head(_module, 'IAcousticEchoCancellationControl')
make_head(_module, 'IActivateAudioInterfaceAsyncOperation')
make_head(_module, 'IActivateAudioInterfaceCompletionHandler')
make_head(_module, 'IAudioAmbisonicsControl')
make_head(_module, 'IAudioAutoGainControl')
make_head(_module, 'IAudioBass')
make_head(_module, 'IAudioCaptureClient')
make_head(_module, 'IAudioChannelConfig')
make_head(_module, 'IAudioClient')
make_head(_module, 'IAudioClient2')
make_head(_module, 'IAudioClient3')
make_head(_module, 'IAudioClientDuckingControl')
make_head(_module, 'IAudioClock')
make_head(_module, 'IAudioClock2')
make_head(_module, 'IAudioClockAdjustment')
make_head(_module, 'IAudioEffectsChangedNotificationClient')
make_head(_module, 'IAudioEffectsManager')
make_head(_module, 'IAudioFormatEnumerator')
make_head(_module, 'IAudioInputSelector')
make_head(_module, 'IAudioLoudness')
make_head(_module, 'IAudioMidrange')
make_head(_module, 'IAudioMute')
make_head(_module, 'IAudioOutputSelector')
make_head(_module, 'IAudioPeakMeter')
make_head(_module, 'IAudioRenderClient')
make_head(_module, 'IAudioSessionControl')
make_head(_module, 'IAudioSessionControl2')
make_head(_module, 'IAudioSessionEnumerator')
make_head(_module, 'IAudioSessionEvents')
make_head(_module, 'IAudioSessionManager')
make_head(_module, 'IAudioSessionManager2')
make_head(_module, 'IAudioSessionNotification')
make_head(_module, 'IAudioStateMonitor')
make_head(_module, 'IAudioStreamVolume')
make_head(_module, 'IAudioSystemEffectsPropertyChangeNotificationClient')
make_head(_module, 'IAudioSystemEffectsPropertyStore')
make_head(_module, 'IAudioTreble')
make_head(_module, 'IAudioViewManagerService')
make_head(_module, 'IAudioVolumeDuckNotification')
make_head(_module, 'IAudioVolumeLevel')
make_head(_module, 'IChannelAudioVolume')
make_head(_module, 'IConnector')
make_head(_module, 'IControlChangeNotify')
make_head(_module, 'IControlInterface')
make_head(_module, 'IDeviceSpecificProperty')
make_head(_module, 'IDeviceTopology')
make_head(_module, 'IMMDevice')
make_head(_module, 'IMMDeviceActivator')
make_head(_module, 'IMMDeviceCollection')
make_head(_module, 'IMMDeviceEnumerator')
make_head(_module, 'IMMEndpoint')
make_head(_module, 'IMMNotificationClient')
make_head(_module, 'IMessageFilter')
make_head(_module, 'IPart')
make_head(_module, 'IPartsList')
make_head(_module, 'IPerChannelDbLevel')
make_head(_module, 'ISimpleAudioVolume')
make_head(_module, 'ISpatialAudioClient')
make_head(_module, 'ISpatialAudioClient2')
make_head(_module, 'ISpatialAudioMetadataClient')
make_head(_module, 'ISpatialAudioMetadataCopier')
make_head(_module, 'ISpatialAudioMetadataItems')
make_head(_module, 'ISpatialAudioMetadataItemsBuffer')
make_head(_module, 'ISpatialAudioMetadataReader')
make_head(_module, 'ISpatialAudioMetadataWriter')
make_head(_module, 'ISpatialAudioObject')
make_head(_module, 'ISpatialAudioObjectBase')
make_head(_module, 'ISpatialAudioObjectForHrtf')
make_head(_module, 'ISpatialAudioObjectForMetadataCommands')
make_head(_module, 'ISpatialAudioObjectForMetadataItems')
make_head(_module, 'ISpatialAudioObjectRenderStream')
make_head(_module, 'ISpatialAudioObjectRenderStreamBase')
make_head(_module, 'ISpatialAudioObjectRenderStreamForHrtf')
make_head(_module, 'ISpatialAudioObjectRenderStreamForMetadata')
make_head(_module, 'ISpatialAudioObjectRenderStreamNotify')
make_head(_module, 'ISubunit')
make_head(_module, 'LPACMDRIVERPROC')
make_head(_module, 'LPMIDICALLBACK')
make_head(_module, 'LPWAVECALLBACK')
make_head(_module, 'MIDIEVENT')
make_head(_module, 'MIDIHDR')
make_head(_module, 'MIDIINCAPS2A')
make_head(_module, 'MIDIINCAPS2W')
make_head(_module, 'MIDIINCAPSA')
make_head(_module, 'MIDIINCAPSW')
make_head(_module, 'MIDIOUTCAPS2A')
make_head(_module, 'MIDIOUTCAPS2W')
make_head(_module, 'MIDIOUTCAPSA')
make_head(_module, 'MIDIOUTCAPSW')
make_head(_module, 'MIDIPROPTEMPO')
make_head(_module, 'MIDIPROPTIMEDIV')
make_head(_module, 'MIDISTRMBUFFVER')
make_head(_module, 'MIXERCAPS2A')
make_head(_module, 'MIXERCAPS2W')
make_head(_module, 'MIXERCAPSA')
make_head(_module, 'MIXERCAPSW')
make_head(_module, 'MIXERCONTROLA')
make_head(_module, 'MIXERCONTROLDETAILS')
make_head(_module, 'MIXERCONTROLDETAILS_BOOLEAN')
make_head(_module, 'MIXERCONTROLDETAILS_LISTTEXTA')
make_head(_module, 'MIXERCONTROLDETAILS_LISTTEXTW')
make_head(_module, 'MIXERCONTROLDETAILS_SIGNED')
make_head(_module, 'MIXERCONTROLDETAILS_UNSIGNED')
make_head(_module, 'MIXERCONTROLW')
make_head(_module, 'MIXERLINEA')
make_head(_module, 'MIXERLINECONTROLSA')
make_head(_module, 'MIXERLINECONTROLSW')
make_head(_module, 'MIXERLINEW')
make_head(_module, 'PAudioStateMonitorCallback')
make_head(_module, 'PCMWAVEFORMAT')
make_head(_module, 'SpatialAudioClientActivationParams')
make_head(_module, 'SpatialAudioHrtfActivationParams')
make_head(_module, 'SpatialAudioHrtfActivationParams2')
make_head(_module, 'SpatialAudioHrtfDirectivity')
make_head(_module, 'SpatialAudioHrtfDirectivityCardioid')
make_head(_module, 'SpatialAudioHrtfDirectivityCone')
make_head(_module, 'SpatialAudioHrtfDirectivityUnion')
make_head(_module, 'SpatialAudioHrtfDistanceDecay')
make_head(_module, 'SpatialAudioMetadataItemsInfo')
make_head(_module, 'SpatialAudioObjectRenderStreamActivationParams')
make_head(_module, 'SpatialAudioObjectRenderStreamActivationParams2')
make_head(_module, 'SpatialAudioObjectRenderStreamForMetadataActivationParams')
make_head(_module, 'SpatialAudioObjectRenderStreamForMetadataActivationParams2')
make_head(_module, 'VOLUMEWAVEFILTER')
make_head(_module, 'WAVEFILTER')
make_head(_module, 'WAVEFORMAT')
make_head(_module, 'WAVEFORMATEX')
make_head(_module, 'WAVEFORMATEXTENSIBLE')
make_head(_module, 'WAVEHDR')
make_head(_module, 'WAVEINCAPS2A')
make_head(_module, 'WAVEINCAPS2W')
make_head(_module, 'WAVEINCAPSA')
make_head(_module, 'WAVEINCAPSW')
make_head(_module, 'WAVEOUTCAPS2A')
make_head(_module, 'WAVEOUTCAPS2W')
make_head(_module, 'WAVEOUTCAPSA')
make_head(_module, 'WAVEOUTCAPSW')
make_head(_module, 'tACMFORMATDETAILSW')
