from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript
import win32more.Windows.Win32.System.Js
import win32more.Windows.Win32.System.Variant
JS_SOURCE_CONTEXT_NONE: UInt64 = 18446744073709551615
if ARCH in 'X64,ARM64':
    @winfunctype('chakra.dll')
    def JsCreateContext(runtime: VoidPtr, debugApplication: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64, newContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X64,ARM64':
    @winfunctype('chakra.dll')
    def JsStartDebugging(debugApplication: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication64) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateRuntime(attributes: win32more.Windows.Win32.System.Js.JsRuntimeAttributes, runtimeVersion: win32more.Windows.Win32.System.Js.JsRuntimeVersion, threadService: win32more.Windows.Win32.System.Js.JsThreadServiceCallback, runtime: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCollectGarbage(runtime: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDisposeRuntime(runtime: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntimeMemoryUsage(runtime: VoidPtr, memoryUsage: POINTER(UIntPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntimeMemoryLimit(runtime: VoidPtr, memoryLimit: POINTER(UIntPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeMemoryLimit(runtime: VoidPtr, memoryLimit: UIntPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeMemoryAllocationCallback(runtime: VoidPtr, callbackState: VoidPtr, allocationCallback: win32more.Windows.Win32.System.Js.JsMemoryAllocationCallback) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetRuntimeBeforeCollectCallback(runtime: VoidPtr, callbackState: VoidPtr, beforeCollectCallback: win32more.Windows.Win32.System.Js.JsBeforeCollectCallback) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsAddRef(ref: VoidPtr, count: POINTER(UInt32)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRelease(ref: VoidPtr, count: POINTER(UInt32)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X86':
    @winfunctype('chakra.dll')
    def JsCreateContext(runtime: VoidPtr, debugApplication: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32, newContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetCurrentContext(currentContext: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetCurrentContext(context: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetRuntime(context: VoidPtr, runtime: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
if ARCH in 'X86':
    @winfunctype('chakra.dll')
    def JsStartDebugging(debugApplication: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IDebugApplication32) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIdle(nextIdleTick: POINTER(UInt32)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsParseScript(script: win32more.Windows.Win32.Foundation.PWSTR, sourceContext: UIntPtr, sourceUrl: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRunScript(script: win32more.Windows.Win32.Foundation.PWSTR, sourceContext: UIntPtr, sourceUrl: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSerializeScript(script: win32more.Windows.Win32.Foundation.PWSTR, buffer: POINTER(Byte), bufferSize: POINTER(UInt32)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsParseSerializedScript(script: win32more.Windows.Win32.Foundation.PWSTR, buffer: POINTER(Byte), sourceContext: UIntPtr, sourceUrl: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsRunSerializedScript(script: win32more.Windows.Win32.Foundation.PWSTR, buffer: POINTER(Byte), sourceContext: UIntPtr, sourceUrl: win32more.Windows.Win32.Foundation.PWSTR, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPropertyIdFromName(name: win32more.Windows.Win32.Foundation.PWSTR, propertyId: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPropertyNameFromId(propertyId: VoidPtr, name: POINTER(POINTER(UInt16))) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetUndefinedValue(undefinedValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetNullValue(nullValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetTrueValue(trueValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetFalseValue(falseValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsBoolToBoolean(value: Byte, booleanValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsBooleanToBool(value: VoidPtr, boolValue: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToBoolean(value: VoidPtr, booleanValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetValueType(value: VoidPtr, type: POINTER(win32more.Windows.Win32.System.Js.JsValueType)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDoubleToNumber(doubleValue: Double, value: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIntToNumber(intValue: Int32, value: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsNumberToDouble(value: VoidPtr, doubleValue: POINTER(Double)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToNumber(value: VoidPtr, numberValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetStringLength(stringValue: VoidPtr, length: POINTER(Int32)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsPointerToString(stringValue: win32more.Windows.Win32.Foundation.PWSTR, stringLength: UIntPtr, value: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStringToPointer(value: VoidPtr, stringValue: POINTER(POINTER(UInt16)), stringLength: POINTER(UIntPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToString(value: VoidPtr, stringValue: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsVariantToValue(variant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT), value: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsValueToVariant(object: VoidPtr, variant: POINTER(win32more.Windows.Win32.System.Variant.VARIANT)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetGlobalObject(globalObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateObject(object: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateExternalObject(data: VoidPtr, finalizeCallback: win32more.Windows.Win32.System.Js.JsFinalizeCallback, object: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConvertValueToObject(value: VoidPtr, object: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetPrototype(object: VoidPtr, prototypeObject: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetPrototype(object: VoidPtr, prototypeObject: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetExtensionAllowed(object: VoidPtr, value: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsPreventExtension(object: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetProperty(object: VoidPtr, propertyId: VoidPtr, value: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetOwnPropertyDescriptor(object: VoidPtr, propertyId: VoidPtr, propertyDescriptor: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetOwnPropertyNames(object: VoidPtr, propertyNames: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetProperty(object: VoidPtr, propertyId: VoidPtr, value: VoidPtr, useStrictRules: Byte) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasProperty(object: VoidPtr, propertyId: VoidPtr, hasProperty: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDeleteProperty(object: VoidPtr, propertyId: VoidPtr, useStrictRules: Byte, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDefineProperty(object: VoidPtr, propertyId: VoidPtr, propertyDescriptor: VoidPtr, result: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasIndexedProperty(object: VoidPtr, index: VoidPtr, result: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetIndexedProperty(object: VoidPtr, index: VoidPtr, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetIndexedProperty(object: VoidPtr, index: VoidPtr, value: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDeleteIndexedProperty(object: VoidPtr, index: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEquals(object1: VoidPtr, object2: VoidPtr, result: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStrictEquals(object1: VoidPtr, object2: VoidPtr, result: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasExternalData(object: VoidPtr, value: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetExternalData(object: VoidPtr, externalData: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetExternalData(object: VoidPtr, externalData: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateArray(length: UInt32, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCallFunction(function: VoidPtr, arguments: POINTER(VoidPtr), argumentCount: UInt16, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsConstructObject(function: VoidPtr, arguments: POINTER(VoidPtr), argumentCount: UInt16, result: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateFunction(nativeFunction: win32more.Windows.Win32.System.Js.JsNativeFunction, callbackState: VoidPtr, function: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateRangeError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateReferenceError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateSyntaxError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateTypeError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsCreateURIError(message: VoidPtr, error: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsHasException(hasException: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsGetAndClearException(exception: POINTER(VoidPtr)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsSetException(exception: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsDisableRuntimeExecution(runtime: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEnableRuntimeExecution(runtime: VoidPtr) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIsRuntimeExecutionDisabled(runtime: VoidPtr, isDisabled: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStartProfiling(callback: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerCallback, eventMask: win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.PROFILER_EVENT_MASK, context: UInt32) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsStopProfiling(reason: win32more.Windows.Win32.Foundation.HRESULT) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsEnumerateHeap(enumerator: POINTER(win32more.Windows.Win32.System.Diagnostics.Debug.ActiveScript.IActiveScriptProfilerHeapEnum)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype('chakra.dll')
def JsIsEnumeratingHeap(isEnumeratingHeap: POINTER(Boolean)) -> win32more.Windows.Win32.System.Js.JsErrorCode: ...
@winfunctype_pointer
def JsBackgroundWorkItemCallback(callbackState: VoidPtr) -> Void: ...
@winfunctype_pointer
def JsBeforeCollectCallback(callbackState: VoidPtr) -> Void: ...
JsErrorCode = UInt32
JsErrorCode_JsNoError: win32more.Windows.Win32.System.Js.JsErrorCode = 0
JsErrorCode_JsErrorCategoryUsage: win32more.Windows.Win32.System.Js.JsErrorCode = 65536
JsErrorCode_JsErrorInvalidArgument: win32more.Windows.Win32.System.Js.JsErrorCode = 65537
JsErrorCode_JsErrorNullArgument: win32more.Windows.Win32.System.Js.JsErrorCode = 65538
JsErrorCode_JsErrorNoCurrentContext: win32more.Windows.Win32.System.Js.JsErrorCode = 65539
JsErrorCode_JsErrorInExceptionState: win32more.Windows.Win32.System.Js.JsErrorCode = 65540
JsErrorCode_JsErrorNotImplemented: win32more.Windows.Win32.System.Js.JsErrorCode = 65541
JsErrorCode_JsErrorWrongThread: win32more.Windows.Win32.System.Js.JsErrorCode = 65542
JsErrorCode_JsErrorRuntimeInUse: win32more.Windows.Win32.System.Js.JsErrorCode = 65543
JsErrorCode_JsErrorBadSerializedScript: win32more.Windows.Win32.System.Js.JsErrorCode = 65544
JsErrorCode_JsErrorInDisabledState: win32more.Windows.Win32.System.Js.JsErrorCode = 65545
JsErrorCode_JsErrorCannotDisableExecution: win32more.Windows.Win32.System.Js.JsErrorCode = 65546
JsErrorCode_JsErrorHeapEnumInProgress: win32more.Windows.Win32.System.Js.JsErrorCode = 65547
JsErrorCode_JsErrorArgumentNotObject: win32more.Windows.Win32.System.Js.JsErrorCode = 65548
JsErrorCode_JsErrorInProfileCallback: win32more.Windows.Win32.System.Js.JsErrorCode = 65549
JsErrorCode_JsErrorInThreadServiceCallback: win32more.Windows.Win32.System.Js.JsErrorCode = 65550
JsErrorCode_JsErrorCannotSerializeDebugScript: win32more.Windows.Win32.System.Js.JsErrorCode = 65551
JsErrorCode_JsErrorAlreadyDebuggingContext: win32more.Windows.Win32.System.Js.JsErrorCode = 65552
JsErrorCode_JsErrorAlreadyProfilingContext: win32more.Windows.Win32.System.Js.JsErrorCode = 65553
JsErrorCode_JsErrorIdleNotEnabled: win32more.Windows.Win32.System.Js.JsErrorCode = 65554
JsErrorCode_JsErrorCategoryEngine: win32more.Windows.Win32.System.Js.JsErrorCode = 131072
JsErrorCode_JsErrorOutOfMemory: win32more.Windows.Win32.System.Js.JsErrorCode = 131073
JsErrorCode_JsErrorCategoryScript: win32more.Windows.Win32.System.Js.JsErrorCode = 196608
JsErrorCode_JsErrorScriptException: win32more.Windows.Win32.System.Js.JsErrorCode = 196609
JsErrorCode_JsErrorScriptCompile: win32more.Windows.Win32.System.Js.JsErrorCode = 196610
JsErrorCode_JsErrorScriptTerminated: win32more.Windows.Win32.System.Js.JsErrorCode = 196611
JsErrorCode_JsErrorScriptEvalDisabled: win32more.Windows.Win32.System.Js.JsErrorCode = 196612
JsErrorCode_JsErrorCategoryFatal: win32more.Windows.Win32.System.Js.JsErrorCode = 262144
JsErrorCode_JsErrorFatal: win32more.Windows.Win32.System.Js.JsErrorCode = 262145
@winfunctype_pointer
def JsFinalizeCallback(data: VoidPtr) -> Void: ...
@winfunctype_pointer
def JsMemoryAllocationCallback(callbackState: VoidPtr, allocationEvent: win32more.Windows.Win32.System.Js.JsMemoryEventType, allocationSize: UIntPtr) -> Boolean: ...
JsMemoryEventType = Int32
JsMemoryEventType_JsMemoryAllocate: win32more.Windows.Win32.System.Js.JsMemoryEventType = 0
JsMemoryEventType_JsMemoryFree: win32more.Windows.Win32.System.Js.JsMemoryEventType = 1
JsMemoryEventType_JsMemoryFailure: win32more.Windows.Win32.System.Js.JsMemoryEventType = 2
@winfunctype_pointer
def JsNativeFunction(callee: VoidPtr, isConstructCall: Boolean, arguments: POINTER(VoidPtr), argumentCount: UInt16, callbackState: VoidPtr) -> VoidPtr: ...
JsRuntimeAttributes = Int32
JsRuntimeAttributes_JsRuntimeAttributeNone: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 0
JsRuntimeAttributes_JsRuntimeAttributeDisableBackgroundWork: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 1
JsRuntimeAttributes_JsRuntimeAttributeAllowScriptInterrupt: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 2
JsRuntimeAttributes_JsRuntimeAttributeEnableIdleProcessing: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 4
JsRuntimeAttributes_JsRuntimeAttributeDisableNativeCodeGeneration: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 8
JsRuntimeAttributes_JsRuntimeAttributeDisableEval: win32more.Windows.Win32.System.Js.JsRuntimeAttributes = 16
JsRuntimeVersion = Int32
JsRuntimeVersion_JsRuntimeVersion10: win32more.Windows.Win32.System.Js.JsRuntimeVersion = 0
JsRuntimeVersion_JsRuntimeVersion11: win32more.Windows.Win32.System.Js.JsRuntimeVersion = 1
JsRuntimeVersion_JsRuntimeVersionEdge: win32more.Windows.Win32.System.Js.JsRuntimeVersion = -1
@winfunctype_pointer
def JsThreadServiceCallback(callback: win32more.Windows.Win32.System.Js.JsBackgroundWorkItemCallback, callbackState: VoidPtr) -> Boolean: ...
JsValueType = Int32
JsValueType_JsUndefined: win32more.Windows.Win32.System.Js.JsValueType = 0
JsValueType_JsNull: win32more.Windows.Win32.System.Js.JsValueType = 1
JsValueType_JsNumber: win32more.Windows.Win32.System.Js.JsValueType = 2
JsValueType_JsString: win32more.Windows.Win32.System.Js.JsValueType = 3
JsValueType_JsBoolean: win32more.Windows.Win32.System.Js.JsValueType = 4
JsValueType_JsObject: win32more.Windows.Win32.System.Js.JsValueType = 5
JsValueType_JsFunction: win32more.Windows.Win32.System.Js.JsValueType = 6
JsValueType_JsError: win32more.Windows.Win32.System.Js.JsValueType = 7
JsValueType_JsArray: win32more.Windows.Win32.System.Js.JsValueType = 8


make_ready(__name__)
