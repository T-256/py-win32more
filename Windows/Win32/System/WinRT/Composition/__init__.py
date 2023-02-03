from __future__ import annotations
from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from Windows.base import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head
import Windows.Win32.Foundation
import Windows.Win32.System.Com
import Windows.Win32.System.WinRT
import Windows.Win32.System.WinRT.Composition
import Windows.Win32.UI.Input.Pointer
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        if name in _arch_optional:
            return None
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
def __dir__():
    return __all__
class ICompositionCapabilitiesInteropFactory(c_void_p):
    extends: Windows.Win32.System.WinRT.IInspectable
    Guid = Guid('2c9db356-e70d-4642-82-98-bc-4a-a5-b4-86-5c')
    @commethod(6)
    def GetForWindow(hwnd: Windows.Win32.Foundation.HWND, result: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
class ICompositionDrawingSurfaceInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('fd04e6e3-fe0c-4c3c-ab-19-a0-76-01-a5-76-ee')
    @commethod(3)
    def BeginDraw(updateRect: POINTER(Windows.Win32.Foundation.RECT_head), iid: POINTER(Guid), updateObject: POINTER(c_void_p), updateOffset: POINTER(Windows.Win32.Foundation.POINT_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EndDraw() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def Resize(sizePixels: Windows.Win32.Foundation.SIZE) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(6)
    def Scroll(scrollRect: POINTER(Windows.Win32.Foundation.RECT_head), clipRect: POINTER(Windows.Win32.Foundation.RECT_head), offsetX: Int32, offsetY: Int32) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(7)
    def ResumeDraw() -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(8)
    def SuspendDraw() -> Windows.Win32.Foundation.HRESULT: ...
class ICompositionDrawingSurfaceInterop2(c_void_p):
    extends: Windows.Win32.System.WinRT.Composition.ICompositionDrawingSurfaceInterop
    Guid = Guid('41e64aae-98c0-4239-8e-95-a3-30-dd-6a-a1-8b')
    @commethod(9)
    def CopySurface(destinationResource: Windows.Win32.System.Com.IUnknown_head, destinationOffsetX: Int32, destinationOffsetY: Int32, sourceRectangle: POINTER(Windows.Win32.Foundation.RECT_head)) -> Windows.Win32.Foundation.HRESULT: ...
class ICompositionGraphicsDeviceInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('a116ff71-f8bf-4c8a-9c-98-70-77-9a-32-a9-c8')
    @commethod(3)
    def GetRenderingDevice(value: POINTER(Windows.Win32.System.Com.IUnknown_head)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def SetRenderingDevice(value: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class ICompositorDesktopInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('29e691fa-4567-4dca-b3-19-d0-f2-07-eb-68-07')
    @commethod(3)
    def CreateDesktopWindowTarget(hwndTarget: Windows.Win32.Foundation.HWND, isTopmost: Windows.Win32.Foundation.BOOL, result: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def EnsureOnThread(threadId: UInt32) -> Windows.Win32.Foundation.HRESULT: ...
class ICompositorInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('25297d5c-3ad4-4c9c-b5-cf-e3-6a-38-51-23-30')
    @commethod(3)
    def CreateCompositionSurfaceForHandle(swapChain: Windows.Win32.Foundation.HANDLE, result: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(4)
    def CreateCompositionSurfaceForSwapChain(swapChain: Windows.Win32.System.Com.IUnknown_head, result: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
    @commethod(5)
    def CreateGraphicsDevice(renderingDevice: Windows.Win32.System.Com.IUnknown_head, result: POINTER(MissingType)) -> Windows.Win32.Foundation.HRESULT: ...
class IDesktopWindowTargetInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('35dbf59e-e3f9-45b0-81-e7-fe-75-f4-14-5d-c9')
    @commethod(3)
    def get_Hwnd(value: POINTER(Windows.Win32.Foundation.HWND)) -> Windows.Win32.Foundation.HRESULT: ...
class ISwapChainInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('26f496a0-7f38-45fb-88-f7-fa-aa-be-67-dd-59')
    @commethod(3)
    def SetSwapChain(swapChain: Windows.Win32.System.Com.IUnknown_head) -> Windows.Win32.Foundation.HRESULT: ...
class IVisualInteractionSourceInterop(c_void_p):
    extends: Windows.Win32.System.Com.IUnknown
    Guid = Guid('11f62cd1-2f9d-42d3-b0-5f-d6-79-0d-9e-9f-8e')
    @commethod(3)
    def TryRedirectForManipulation(pointerInfo: POINTER(Windows.Win32.UI.Input.Pointer.POINTER_INFO_head)) -> Windows.Win32.Foundation.HRESULT: ...
make_head(_module, 'ICompositionCapabilitiesInteropFactory')
make_head(_module, 'ICompositionDrawingSurfaceInterop')
make_head(_module, 'ICompositionDrawingSurfaceInterop2')
make_head(_module, 'ICompositionGraphicsDeviceInterop')
make_head(_module, 'ICompositorDesktopInterop')
make_head(_module, 'ICompositorInterop')
make_head(_module, 'IDesktopWindowTargetInterop')
make_head(_module, 'ISwapChainInterop')
make_head(_module, 'IVisualInteractionSourceInterop')
__all__ = [
    "ICompositionCapabilitiesInteropFactory",
    "ICompositionDrawingSurfaceInterop",
    "ICompositionDrawingSurfaceInterop2",
    "ICompositionGraphicsDeviceInterop",
    "ICompositorDesktopInterop",
    "ICompositorInterop",
    "IDesktopWindowTargetInterop",
    "ISwapChainInterop",
    "IVisualInteractionSourceInterop",
]
_arch_optional = [
]