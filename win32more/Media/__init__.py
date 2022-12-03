from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Media
import win32more.Media.Multimedia
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
TIMERR_NOERROR = 0
TIMERR_NOCANDO = 97
TIMERR_STRUCT = 129
MAXPNAMELEN = 32
MAXERRORLENGTH = 256
MM_MICROSOFT = 1
MM_MIDI_MAPPER = 1
MM_WAVE_MAPPER = 2
MM_SNDBLST_MIDIOUT = 3
MM_SNDBLST_MIDIIN = 4
MM_SNDBLST_SYNTH = 5
MM_SNDBLST_WAVEOUT = 6
MM_SNDBLST_WAVEIN = 7
MM_ADLIB = 9
MM_MPU401_MIDIOUT = 10
MM_MPU401_MIDIIN = 11
MM_PC_JOYSTICK = 12
TIME_MS = 1
TIME_SAMPLES = 2
TIME_BYTES = 4
TIME_SMPTE = 8
TIME_MIDI = 16
TIME_TICKS = 32
MM_JOY1MOVE = 928
MM_JOY2MOVE = 929
MM_JOY1ZMOVE = 930
MM_JOY2ZMOVE = 931
MM_JOY1BUTTONDOWN = 949
MM_JOY2BUTTONDOWN = 950
MM_JOY1BUTTONUP = 951
MM_JOY2BUTTONUP = 952
MM_MCINOTIFY = 953
MM_WOM_OPEN = 955
MM_WOM_CLOSE = 956
MM_WOM_DONE = 957
MM_WIM_OPEN = 958
MM_WIM_CLOSE = 959
MM_WIM_DATA = 960
MM_MIM_OPEN = 961
MM_MIM_CLOSE = 962
MM_MIM_DATA = 963
MM_MIM_LONGDATA = 964
MM_MIM_ERROR = 965
MM_MIM_LONGERROR = 966
MM_MOM_OPEN = 967
MM_MOM_CLOSE = 968
MM_MOM_DONE = 969
MM_DRVM_OPEN = 976
MM_DRVM_CLOSE = 977
MM_DRVM_DATA = 978
MM_DRVM_ERROR = 979
MM_STREAM_OPEN = 980
MM_STREAM_CLOSE = 981
MM_STREAM_DONE = 982
MM_STREAM_ERROR = 983
MM_MOM_POSITIONCB = 970
MM_MCISIGNAL = 971
MM_MIM_MOREDATA = 972
MM_MIXM_LINE_CHANGE = 976
MM_MIXM_CONTROL_CHANGE = 977
MMSYSERR_BASE = 0
WAVERR_BASE = 32
MIDIERR_BASE = 64
TIMERR_BASE = 96
JOYERR_BASE = 160
MCIERR_BASE = 256
MIXERR_BASE = 1024
MCI_STRING_OFFSET = 512
MCI_VD_OFFSET = 1024
MCI_CD_OFFSET = 1088
MCI_WAVE_OFFSET = 1152
MCI_SEQ_OFFSET = 1216
MMSYSERR_NOERROR = 0
MMSYSERR_ERROR = 1
MMSYSERR_BADDEVICEID = 2
MMSYSERR_NOTENABLED = 3
MMSYSERR_ALLOCATED = 4
MMSYSERR_INVALHANDLE = 5
MMSYSERR_NODRIVER = 6
MMSYSERR_NOMEM = 7
MMSYSERR_NOTSUPPORTED = 8
MMSYSERR_BADERRNUM = 9
MMSYSERR_INVALFLAG = 10
MMSYSERR_INVALPARAM = 11
MMSYSERR_HANDLEBUSY = 12
MMSYSERR_INVALIDALIAS = 13
MMSYSERR_BADDB = 14
MMSYSERR_KEYNOTFOUND = 15
MMSYSERR_READERROR = 16
MMSYSERR_WRITEERROR = 17
MMSYSERR_DELETEERROR = 18
MMSYSERR_VALNOTFOUND = 19
MMSYSERR_NODRIVERCB = 20
MMSYSERR_MOREDATA = 21
MMSYSERR_LASTERROR = 21
TIME_ONESHOT = 0
TIME_PERIODIC = 1
TIME_CALLBACK_FUNCTION = 0
TIME_CALLBACK_EVENT_SET = 16
TIME_CALLBACK_EVENT_PULSE = 32
TIME_KILL_SYNCHRONOUS = 256
def _define_timeGetSystemTime():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Media.MMTIME_head),UInt32)(('timeGetSystemTime', windll['WINMM.dll']), ((1, 'pmmt'),(1, 'cbmmt'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeGetTime():
    try:
        return WINFUNCTYPE(UInt32,)(('timeGetTime', windll['WINMM.dll']), ())
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeGetDevCaps():
    try:
        return WINFUNCTYPE(UInt32,POINTER(win32more.Media.TIMECAPS_head),UInt32)(('timeGetDevCaps', windll['WINMM.dll']), ((1, 'ptc'),(1, 'cbtc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeBeginPeriod():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('timeBeginPeriod', windll['WINMM.dll']), ((1, 'uPeriod'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeEndPeriod():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('timeEndPeriod', windll['WINMM.dll']), ((1, 'uPeriod'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeSetEvent():
    try:
        return WINFUNCTYPE(UInt32,UInt32,UInt32,win32more.Media.LPTIMECALLBACK,UIntPtr,UInt32)(('timeSetEvent', windll['WINMM.dll']), ((1, 'uDelay'),(1, 'uResolution'),(1, 'fptc'),(1, 'dwUser'),(1, 'fuEvent'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_timeKillEvent():
    try:
        return WINFUNCTYPE(UInt32,UInt32)(('timeKillEvent', windll['WINMM.dll']), ((1, 'uTimerID'),))
    except (FileNotFoundError, AttributeError):
        return None
HTASK = IntPtr
def _define_IReferenceClock_head():
    class IReferenceClock(win32more.System.Com.IUnknown_head):
        Guid = Guid('56a86897-0ad4-11ce-b0-3a-00-20-af-0b-a7-70')
    return IReferenceClock
def _define_IReferenceClock():
    IReferenceClock = win32more.Media.IReferenceClock_head
    IReferenceClock.GetTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(3, 'GetTime', ((1, 'pTime'),)))
    IReferenceClock.AdviseTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,Int64,win32more.Foundation.HANDLE,POINTER(UIntPtr))(4, 'AdviseTime', ((1, 'baseTime'),(1, 'streamTime'),(1, 'hEvent'),(1, 'pdwAdviseCookie'),)))
    IReferenceClock.AdvisePeriodic = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64,Int64,win32more.Foundation.HANDLE,POINTER(UIntPtr))(5, 'AdvisePeriodic', ((1, 'startTime'),(1, 'periodTime'),(1, 'hSemaphore'),(1, 'pdwAdviseCookie'),)))
    IReferenceClock.Unadvise = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UIntPtr)(6, 'Unadvise', ((1, 'dwAdviseCookie'),)))
    win32more.System.Com.IUnknown
    return IReferenceClock
def _define_IReferenceClock2_head():
    class IReferenceClock2(win32more.Media.IReferenceClock_head):
        Guid = Guid('36b73885-c2c8-11cf-8b-46-00-80-5f-6c-ef-60')
    return IReferenceClock2
def _define_IReferenceClock2():
    IReferenceClock2 = win32more.Media.IReferenceClock2_head
    win32more.Media.IReferenceClock
    return IReferenceClock2
def _define_IReferenceClockTimerControl_head():
    class IReferenceClockTimerControl(win32more.System.Com.IUnknown_head):
        Guid = Guid('ebec459c-2eca-4d42-a8-af-30-df-55-76-14-b8')
    return IReferenceClockTimerControl
def _define_IReferenceClockTimerControl():
    IReferenceClockTimerControl = win32more.Media.IReferenceClockTimerControl_head
    IReferenceClockTimerControl.SetDefaultTimerResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int64)(3, 'SetDefaultTimerResolution', ((1, 'timerResolution'),)))
    IReferenceClockTimerControl.GetDefaultTimerResolution = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int64))(4, 'GetDefaultTimerResolution', ((1, 'pTimerResolution'),)))
    win32more.System.Com.IUnknown
    return IReferenceClockTimerControl
def _define_LPDRVCALLBACK():
    return WINFUNCTYPE(Void,win32more.Media.Multimedia.HDRVR,UInt32,UIntPtr,UIntPtr,UIntPtr)
def _define_LPTIMECALLBACK():
    return WINFUNCTYPE(Void,UInt32,UInt32,UIntPtr,UIntPtr,UIntPtr)
def _define_MMTIME_head():
    class MMTIME(Structure):
        pass
    return MMTIME
def _define_MMTIME():
    MMTIME = win32more.Media.MMTIME_head
    class MMTIME__u_e__Union(Union):
        pass
    class MMTIME__u_e__Union__smpte_e__Struct(Structure):
        pass
    MMTIME__u_e__Union__smpte_e__Struct._fields_ = [
        ('hour', Byte),
        ('min', Byte),
        ('sec', Byte),
        ('frame', Byte),
        ('fps', Byte),
        ('dummy', Byte),
        ('pad', Byte * 2),
    ]
    class MMTIME__u_e__Union__midi_e__Struct(Structure):
        pass
    MMTIME__u_e__Union__midi_e__Struct._pack_ = 1
    MMTIME__u_e__Union__midi_e__Struct._fields_ = [
        ('songptrpos', UInt32),
    ]
    MMTIME__u_e__Union._pack_ = 1
    MMTIME__u_e__Union._fields_ = [
        ('ms', UInt32),
        ('sample', UInt32),
        ('cb', UInt32),
        ('ticks', UInt32),
        ('smpte', MMTIME__u_e__Union__smpte_e__Struct),
        ('midi', MMTIME__u_e__Union__midi_e__Struct),
    ]
    MMTIME._pack_ = 1
    MMTIME._fields_ = [
        ('wType', UInt32),
        ('u', MMTIME__u_e__Union),
    ]
    return MMTIME
def _define_TIMECAPS_head():
    class TIMECAPS(Structure):
        pass
    return TIMECAPS
def _define_TIMECAPS():
    TIMECAPS = win32more.Media.TIMECAPS_head
    TIMECAPS._fields_ = [
        ('wPeriodMin', UInt32),
        ('wPeriodMax', UInt32),
    ]
    return TIMECAPS
def _define_TIMECODE_head():
    class TIMECODE(Union):
        pass
    return TIMECODE
def _define_TIMECODE():
    TIMECODE = win32more.Media.TIMECODE_head
    class TIMECODE__Anonymous_e__Struct(Structure):
        pass
    TIMECODE__Anonymous_e__Struct._fields_ = [
        ('wFrameRate', UInt16),
        ('wFrameFract', UInt16),
        ('dwFrames', UInt32),
    ]
    TIMECODE._anonymous_ = [
        'Anonymous',
    ]
    TIMECODE._fields_ = [
        ('Anonymous', TIMECODE__Anonymous_e__Struct),
        ('qw', UInt64),
    ]
    return TIMECODE
def _define_TIMECODE_SAMPLE_head():
    class TIMECODE_SAMPLE(Structure):
        pass
    return TIMECODE_SAMPLE
def _define_TIMECODE_SAMPLE():
    TIMECODE_SAMPLE = win32more.Media.TIMECODE_SAMPLE_head
    TIMECODE_SAMPLE._fields_ = [
        ('qwTick', Int64),
        ('timecode', win32more.Media.TIMECODE),
        ('dwUser', UInt32),
        ('dwFlags', win32more.Media.TIMECODE_SAMPLE_FLAGS),
    ]
    return TIMECODE_SAMPLE
TIMECODE_SAMPLE_FLAGS = UInt32
ED_DEVCAP_TIMECODE_READ = 4121
ED_DEVCAP_ATN_READ = 5047
ED_DEVCAP_RTC_READ = 5050
__all__ = [
    "ED_DEVCAP_ATN_READ",
    "ED_DEVCAP_RTC_READ",
    "ED_DEVCAP_TIMECODE_READ",
    "HTASK",
    "IReferenceClock",
    "IReferenceClock2",
    "IReferenceClockTimerControl",
    "JOYERR_BASE",
    "LPDRVCALLBACK",
    "LPTIMECALLBACK",
    "MAXERRORLENGTH",
    "MAXPNAMELEN",
    "MCIERR_BASE",
    "MCI_CD_OFFSET",
    "MCI_SEQ_OFFSET",
    "MCI_STRING_OFFSET",
    "MCI_VD_OFFSET",
    "MCI_WAVE_OFFSET",
    "MIDIERR_BASE",
    "MIXERR_BASE",
    "MMSYSERR_ALLOCATED",
    "MMSYSERR_BADDB",
    "MMSYSERR_BADDEVICEID",
    "MMSYSERR_BADERRNUM",
    "MMSYSERR_BASE",
    "MMSYSERR_DELETEERROR",
    "MMSYSERR_ERROR",
    "MMSYSERR_HANDLEBUSY",
    "MMSYSERR_INVALFLAG",
    "MMSYSERR_INVALHANDLE",
    "MMSYSERR_INVALIDALIAS",
    "MMSYSERR_INVALPARAM",
    "MMSYSERR_KEYNOTFOUND",
    "MMSYSERR_LASTERROR",
    "MMSYSERR_MOREDATA",
    "MMSYSERR_NODRIVER",
    "MMSYSERR_NODRIVERCB",
    "MMSYSERR_NOERROR",
    "MMSYSERR_NOMEM",
    "MMSYSERR_NOTENABLED",
    "MMSYSERR_NOTSUPPORTED",
    "MMSYSERR_READERROR",
    "MMSYSERR_VALNOTFOUND",
    "MMSYSERR_WRITEERROR",
    "MMTIME",
    "MM_ADLIB",
    "MM_DRVM_CLOSE",
    "MM_DRVM_DATA",
    "MM_DRVM_ERROR",
    "MM_DRVM_OPEN",
    "MM_JOY1BUTTONDOWN",
    "MM_JOY1BUTTONUP",
    "MM_JOY1MOVE",
    "MM_JOY1ZMOVE",
    "MM_JOY2BUTTONDOWN",
    "MM_JOY2BUTTONUP",
    "MM_JOY2MOVE",
    "MM_JOY2ZMOVE",
    "MM_MCINOTIFY",
    "MM_MCISIGNAL",
    "MM_MICROSOFT",
    "MM_MIDI_MAPPER",
    "MM_MIM_CLOSE",
    "MM_MIM_DATA",
    "MM_MIM_ERROR",
    "MM_MIM_LONGDATA",
    "MM_MIM_LONGERROR",
    "MM_MIM_MOREDATA",
    "MM_MIM_OPEN",
    "MM_MIXM_CONTROL_CHANGE",
    "MM_MIXM_LINE_CHANGE",
    "MM_MOM_CLOSE",
    "MM_MOM_DONE",
    "MM_MOM_OPEN",
    "MM_MOM_POSITIONCB",
    "MM_MPU401_MIDIIN",
    "MM_MPU401_MIDIOUT",
    "MM_PC_JOYSTICK",
    "MM_SNDBLST_MIDIIN",
    "MM_SNDBLST_MIDIOUT",
    "MM_SNDBLST_SYNTH",
    "MM_SNDBLST_WAVEIN",
    "MM_SNDBLST_WAVEOUT",
    "MM_STREAM_CLOSE",
    "MM_STREAM_DONE",
    "MM_STREAM_ERROR",
    "MM_STREAM_OPEN",
    "MM_WAVE_MAPPER",
    "MM_WIM_CLOSE",
    "MM_WIM_DATA",
    "MM_WIM_OPEN",
    "MM_WOM_CLOSE",
    "MM_WOM_DONE",
    "MM_WOM_OPEN",
    "TIMECAPS",
    "TIMECODE",
    "TIMECODE_SAMPLE",
    "TIMECODE_SAMPLE_FLAGS",
    "TIMERR_BASE",
    "TIMERR_NOCANDO",
    "TIMERR_NOERROR",
    "TIMERR_STRUCT",
    "TIME_BYTES",
    "TIME_CALLBACK_EVENT_PULSE",
    "TIME_CALLBACK_EVENT_SET",
    "TIME_CALLBACK_FUNCTION",
    "TIME_KILL_SYNCHRONOUS",
    "TIME_MIDI",
    "TIME_MS",
    "TIME_ONESHOT",
    "TIME_PERIODIC",
    "TIME_SAMPLES",
    "TIME_SMPTE",
    "TIME_TICKS",
    "WAVERR_BASE",
    "timeBeginPeriod",
    "timeEndPeriod",
    "timeGetDevCaps",
    "timeGetSystemTime",
    "timeGetTime",
    "timeKillEvent",
    "timeSetEvent",
]
