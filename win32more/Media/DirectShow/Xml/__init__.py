from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Data.Xml.MsXml
import win32more.Foundation
import win32more.Media.DirectShow
import win32more.Media.DirectShow.Xml
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
def _define_CLSID_XMLGraphBuilder():
    return Guid('1bb05961-5fbf-11d2-a5-21-44-df-07-c1-00-00')
def _define_IXMLGraphBuilder_head():
    class IXMLGraphBuilder(win32more.System.Com.IUnknown_head):
        Guid = Guid('1bb05960-5fbf-11d2-a5-21-44-df-07-c1-00-00')
    return IXMLGraphBuilder
def _define_IXMLGraphBuilder():
    IXMLGraphBuilder = win32more.Media.DirectShow.Xml.IXMLGraphBuilder_head
    IXMLGraphBuilder.BuildFromXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DirectShow.IGraphBuilder_head,win32more.Data.Xml.MsXml.IXMLElement_head)(3, 'BuildFromXML', ((1, 'pGraph'),(1, 'pxml'),)))
    IXMLGraphBuilder.SaveToXML = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DirectShow.IGraphBuilder_head,POINTER(win32more.Foundation.BSTR))(4, 'SaveToXML', ((1, 'pGraph'),(1, 'pbstrxml'),)))
    IXMLGraphBuilder.BuildFromXMLFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Media.DirectShow.IGraphBuilder_head,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR)(5, 'BuildFromXMLFile', ((1, 'pGraph'),(1, 'wszFileName'),(1, 'wszBaseURL'),)))
    win32more.System.Com.IUnknown
    return IXMLGraphBuilder
__all__ = [
    "CLSID_XMLGraphBuilder",
    "IXMLGraphBuilder",
]
