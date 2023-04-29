from __future__ import annotations
from ctypes import c_void_p, c_char_p, c_wchar_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows import ARCH, MissingType, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
import Windows.Win32.System.Search.Common
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
CONDITION_OPERATION = Int32
COP_IMPLICIT: CONDITION_OPERATION = 0
COP_EQUAL: CONDITION_OPERATION = 1
COP_NOTEQUAL: CONDITION_OPERATION = 2
COP_LESSTHAN: CONDITION_OPERATION = 3
COP_GREATERTHAN: CONDITION_OPERATION = 4
COP_LESSTHANOREQUAL: CONDITION_OPERATION = 5
COP_GREATERTHANOREQUAL: CONDITION_OPERATION = 6
COP_VALUE_STARTSWITH: CONDITION_OPERATION = 7
COP_VALUE_ENDSWITH: CONDITION_OPERATION = 8
COP_VALUE_CONTAINS: CONDITION_OPERATION = 9
COP_VALUE_NOTCONTAINS: CONDITION_OPERATION = 10
COP_DOSWILDCARDS: CONDITION_OPERATION = 11
COP_WORD_EQUAL: CONDITION_OPERATION = 12
COP_WORD_STARTSWITH: CONDITION_OPERATION = 13
COP_APPLICATION_SPECIFIC: CONDITION_OPERATION = 14
CONDITION_TYPE = Int32
CT_AND_CONDITION: CONDITION_TYPE = 0
CT_OR_CONDITION: CONDITION_TYPE = 1
CT_NOT_CONDITION: CONDITION_TYPE = 2
CT_LEAF_CONDITION: CONDITION_TYPE = 3
