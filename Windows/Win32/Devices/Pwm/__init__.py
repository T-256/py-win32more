from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.Devices.Pwm
import Windows.Win32.Foundation
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
GUID_DEVINTERFACE_PWM_CONTROLLER: Guid = Guid('60824b4c-eed1-4c9c-b4-9c-1b-96-14-61-a8-19')
GUID_DEVINTERFACE_PWM_CONTROLLER_WSZ: String = '{60824B4C-EED1-4C9C-B49C-1B961461A819}'
IOCTL_PWM_CONTROLLER_GET_INFO: UInt32 = 262144
IOCTL_PWM_CONTROLLER_GET_ACTUAL_PERIOD: UInt32 = 262148
IOCTL_PWM_CONTROLLER_SET_DESIRED_PERIOD: UInt32 = 294920
IOCTL_PWM_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE: UInt32 = 262544
IOCTL_PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE: UInt32 = 295316
IOCTL_PWM_PIN_GET_POLARITY: UInt32 = 262552
IOCTL_PWM_PIN_SET_POLARITY: UInt32 = 295324
IOCTL_PWM_PIN_START: UInt32 = 295331
IOCTL_PWM_PIN_STOP: UInt32 = 295335
IOCTL_PWM_PIN_IS_STARTED: UInt32 = 262568
PWM_IOCTL_ID_CONTROLLER_GET_INFO: Int32 = 0
PWM_IOCTL_ID_CONTROLLER_GET_ACTUAL_PERIOD: Int32 = 1
PWM_IOCTL_ID_CONTROLLER_SET_DESIRED_PERIOD: Int32 = 2
PWM_IOCTL_ID_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE: Int32 = 100
PWM_IOCTL_ID_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE: Int32 = 101
PWM_IOCTL_ID_PIN_GET_POLARITY: Int32 = 102
PWM_IOCTL_ID_PIN_SET_POLARITY: Int32 = 103
PWM_IOCTL_ID_PIN_START: Int32 = 104
PWM_IOCTL_ID_PIN_STOP: Int32 = 105
PWM_IOCTL_ID_PIN_IS_STARTED: Int32 = 106
class PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT(EasyCastStructure):
    ActualPeriod: UInt64
class PWM_CONTROLLER_INFO(EasyCastStructure):
    Size: UIntPtr
    PinCount: UInt32
    MinimumPeriod: UInt64
    MaximumPeriod: UInt64
class PWM_CONTROLLER_SET_DESIRED_PERIOD_INPUT(EasyCastStructure):
    DesiredPeriod: UInt64
class PWM_CONTROLLER_SET_DESIRED_PERIOD_OUTPUT(EasyCastStructure):
    ActualPeriod: UInt64
class PWM_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE_OUTPUT(EasyCastStructure):
    Percentage: UInt64
class PWM_PIN_GET_POLARITY_OUTPUT(EasyCastStructure):
    Polarity: Windows.Win32.Devices.Pwm.PWM_POLARITY
class PWM_PIN_IS_STARTED_OUTPUT(EasyCastStructure):
    IsStarted: Windows.Win32.Foundation.BOOLEAN
class PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT(EasyCastStructure):
    Percentage: UInt64
class PWM_PIN_SET_POLARITY_INPUT(EasyCastStructure):
    Polarity: Windows.Win32.Devices.Pwm.PWM_POLARITY
PWM_POLARITY = Int32
PWM_ACTIVE_HIGH: PWM_POLARITY = 0
PWM_ACTIVE_LOW: PWM_POLARITY = 1
make_head(_module, 'PWM_CONTROLLER_GET_ACTUAL_PERIOD_OUTPUT')
make_head(_module, 'PWM_CONTROLLER_INFO')
make_head(_module, 'PWM_CONTROLLER_SET_DESIRED_PERIOD_INPUT')
make_head(_module, 'PWM_CONTROLLER_SET_DESIRED_PERIOD_OUTPUT')
make_head(_module, 'PWM_PIN_GET_ACTIVE_DUTY_CYCLE_PERCENTAGE_OUTPUT')
make_head(_module, 'PWM_PIN_GET_POLARITY_OUTPUT')
make_head(_module, 'PWM_PIN_IS_STARTED_OUTPUT')
make_head(_module, 'PWM_PIN_SET_ACTIVE_DUTY_CYCLE_PERCENTAGE_INPUT')
make_head(_module, 'PWM_PIN_SET_POLARITY_INPUT')
