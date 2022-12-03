from ctypes import c_void_p, Structure, Union, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
from win32more.base import MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, COMMETHOD, SUCCEEDED, FAILED
import win32more.Foundation
import win32more.Graphics.Gdi
import win32more.Security
import win32more.Security.Cryptography
import win32more.Storage.Packaging.Opc
import win32more.Storage.Xps
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
def _define_ABORTPROC():
    return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Graphics.Gdi.HDC,Int32)
XPS_E_SIGREQUESTID_DUP = -2142108795
XPS_E_PACKAGE_NOT_OPENED = -2142108794
XPS_E_PACKAGE_ALREADY_OPENED = -2142108793
XPS_E_SIGNATUREID_DUP = -2142108792
XPS_E_MARKUP_COMPATIBILITY_ELEMENTS = -2142108791
XPS_E_OBJECT_DETACHED = -2142108790
XPS_E_INVALID_SIGNATUREBLOCK_MARKUP = -2142108789
XPS_E_INVALID_NUMBER_OF_POINTS_IN_CURVE_SEGMENTS = -2142108160
XPS_E_ABSOLUTE_REFERENCE = -2142108159
XPS_E_INVALID_NUMBER_OF_COLOR_CHANNELS = -2142108158
XPS_E_INVALID_LANGUAGE = -2142109696
XPS_E_INVALID_NAME = -2142109695
XPS_E_INVALID_RESOURCE_KEY = -2142109694
XPS_E_INVALID_PAGE_SIZE = -2142109693
XPS_E_INVALID_BLEED_BOX = -2142109692
XPS_E_INVALID_THUMBNAIL_IMAGE_TYPE = -2142109691
XPS_E_INVALID_LOOKUP_TYPE = -2142109690
XPS_E_INVALID_FLOAT = -2142109689
XPS_E_UNEXPECTED_CONTENT_TYPE = -2142109688
XPS_E_INVALID_FONT_URI = -2142109686
XPS_E_INVALID_CONTENT_BOX = -2142109685
XPS_E_INVALID_MARKUP = -2142109684
XPS_E_INVALID_XML_ENCODING = -2142109683
XPS_E_INVALID_CONTENT_TYPE = -2142109682
XPS_E_INVALID_OBFUSCATED_FONT_URI = -2142109681
XPS_E_UNEXPECTED_RELATIONSHIP_TYPE = -2142109680
XPS_E_UNEXPECTED_RESTRICTED_FONT_RELATIONSHIP = -2142109679
XPS_E_MISSING_NAME = -2142109440
XPS_E_MISSING_LOOKUP = -2142109439
XPS_E_MISSING_GLYPHS = -2142109438
XPS_E_MISSING_SEGMENT_DATA = -2142109437
XPS_E_MISSING_COLORPROFILE = -2142109436
XPS_E_MISSING_RELATIONSHIP_TARGET = -2142109435
XPS_E_MISSING_RESOURCE_RELATIONSHIP = -2142109434
XPS_E_MISSING_FONTURI = -2142109433
XPS_E_MISSING_DOCUMENTSEQUENCE_RELATIONSHIP = -2142109432
XPS_E_MISSING_DOCUMENT = -2142109431
XPS_E_MISSING_REFERRED_DOCUMENT = -2142109430
XPS_E_MISSING_REFERRED_PAGE = -2142109429
XPS_E_MISSING_PAGE_IN_DOCUMENT = -2142109428
XPS_E_MISSING_PAGE_IN_PAGEREFERENCE = -2142109427
XPS_E_MISSING_IMAGE_IN_IMAGEBRUSH = -2142109426
XPS_E_MISSING_RESOURCE_KEY = -2142109425
XPS_E_MISSING_PART_REFERENCE = -2142109424
XPS_E_MISSING_RESTRICTED_FONT_RELATIONSHIP = -2142109423
XPS_E_MISSING_DISCARDCONTROL = -2142109422
XPS_E_MISSING_PART_STREAM = -2142109421
XPS_E_UNAVAILABLE_PACKAGE = -2142109420
XPS_E_DUPLICATE_RESOURCE_KEYS = -2142109184
XPS_E_MULTIPLE_RESOURCES = -2142109183
XPS_E_MULTIPLE_DOCUMENTSEQUENCE_RELATIONSHIPS = -2142109182
XPS_E_MULTIPLE_THUMBNAILS_ON_PAGE = -2142109181
XPS_E_MULTIPLE_THUMBNAILS_ON_PACKAGE = -2142109180
XPS_E_MULTIPLE_PRINTTICKETS_ON_PAGE = -2142109179
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENT = -2142109178
XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENTSEQUENCE = -2142109177
XPS_E_MULTIPLE_REFERENCES_TO_PART = -2142109176
XPS_E_DUPLICATE_NAMES = -2142109175
XPS_E_STRING_TOO_LONG = -2142108928
XPS_E_TOO_MANY_INDICES = -2142108927
XPS_E_MAPPING_OUT_OF_ORDER = -2142108926
XPS_E_MAPPING_OUTSIDE_STRING = -2142108925
XPS_E_MAPPING_OUTSIDE_INDICES = -2142108924
XPS_E_CARET_OUTSIDE_STRING = -2142108923
XPS_E_CARET_OUT_OF_ORDER = -2142108922
XPS_E_ODD_BIDILEVEL = -2142108921
XPS_E_ONE_TO_ONE_MAPPING_EXPECTED = -2142108920
XPS_E_RESTRICTED_FONT_NOT_OBFUSCATED = -2142108919
XPS_E_NEGATIVE_FLOAT = -2142108918
XPS_E_XKEY_ATTR_PRESENT_OUTSIDE_RES_DICT = -2142108672
XPS_E_DICTIONARY_ITEM_NAMED = -2142108671
XPS_E_NESTED_REMOTE_DICTIONARY = -2142108670
XPS_E_INDEX_OUT_OF_RANGE = -2142108416
XPS_E_VISUAL_CIRCULAR_REF = -2142108415
XPS_E_NO_CUSTOM_OBJECTS = -2142108414
XPS_E_ALREADY_OWNED = -2142108413
XPS_E_RESOURCE_NOT_OWNED = -2142108412
XPS_E_UNEXPECTED_COLORPROFILE = -2142108411
XPS_E_COLOR_COMPONENT_OUT_OF_RANGE = -2142108410
XPS_E_BOTH_PATHFIGURE_AND_ABBR_SYNTAX_PRESENT = -2142108409
XPS_E_BOTH_RESOURCE_AND_SOURCEATTR_PRESENT = -2142108408
XPS_E_BLEED_BOX_PAGE_DIMENSIONS_NOT_IN_SYNC = -2142108407
XPS_E_RELATIONSHIP_EXTERNAL = -2142108406
XPS_E_NOT_ENOUGH_GRADIENT_STOPS = -2142108405
XPS_E_PACKAGE_WRITER_NOT_CLOSED = -2142108404
def _define_DeviceCapabilitiesA():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PSTR,win32more.Foundation.PSTR,win32more.Storage.Xps.DEVICE_CAPABILITIES,win32more.Foundation.PSTR,POINTER(win32more.Graphics.Gdi.DEVMODEA_head))(('DeviceCapabilitiesA', windll['winspool.drv']), ((1, 'pDevice'),(1, 'pPort'),(1, 'fwCapability'),(1, 'pOutput'),(1, 'pDevMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_DeviceCapabilitiesW():
    try:
        return WINFUNCTYPE(Int32,win32more.Foundation.PWSTR,win32more.Foundation.PWSTR,win32more.Storage.Xps.DEVICE_CAPABILITIES,win32more.Foundation.PWSTR,POINTER(win32more.Graphics.Gdi.DEVMODEW_head))(('DeviceCapabilitiesW', windll['winspool.drv']), ((1, 'pDevice'),(1, 'pPort'),(1, 'fwCapability'),(1, 'pOutput'),(1, 'pDevMode'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_Escape():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PSTR,c_void_p)(('Escape', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iEscape'),(1, 'cjIn'),(1, 'pvIn'),(1, 'pvOut'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_ExtEscape():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,Int32,Int32,win32more.Foundation.PSTR,Int32,win32more.Foundation.PSTR)(('ExtEscape', windll['GDI32.dll']), ((1, 'hdc'),(1, 'iEscape'),(1, 'cjInput'),(1, 'lpInData'),(1, 'cjOutput'),(1, 'lpOutData'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartDocA():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Storage.Xps.DOCINFOA_head))(('StartDocA', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpdi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartDocW():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,POINTER(win32more.Storage.Xps.DOCINFOW_head))(('StartDocW', windll['GDI32.dll']), ((1, 'hdc'),(1, 'lpdi'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndDoc():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('EndDoc', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_StartPage():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('StartPage', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_EndPage():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('EndPage', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_AbortDoc():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC)(('AbortDoc', windll['GDI32.dll']), ((1, 'hdc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_SetAbortProc():
    try:
        return WINFUNCTYPE(Int32,win32more.Graphics.Gdi.HDC,win32more.Storage.Xps.ABORTPROC)(('SetAbortProc', windll['GDI32.dll']), ((1, 'hdc'),(1, 'proc'),))
    except (FileNotFoundError, AttributeError):
        return None
def _define_PrintWindow():
    try:
        return WINFUNCTYPE(win32more.Foundation.BOOL,win32more.Foundation.HWND,win32more.Graphics.Gdi.HDC,win32more.Storage.Xps.PRINT_WINDOW_FLAGS)(('PrintWindow', windll['USER32.dll']), ((1, 'hwnd'),(1, 'hdcBlt'),(1, 'nFlags'),))
    except (FileNotFoundError, AttributeError):
        return None
DEVICE_CAPABILITIES = UInt16
DC_BINNAMES = 12
DC_BINS = 6
DC_COLLATE = 22
DC_COLORDEVICE = 32
DC_COPIES = 18
DC_DRIVER = 11
DC_DUPLEX = 7
DC_ENUMRESOLUTIONS = 13
DC_EXTRA = 9
DC_FIELDS = 1
DC_FILEDEPENDENCIES = 14
DC_MAXEXTENT = 5
DC_MEDIAREADY = 29
DC_MEDIATYPENAMES = 34
DC_MEDIATYPES = 35
DC_MINEXTENT = 4
DC_ORIENTATION = 17
DC_NUP = 33
DC_PAPERNAMES = 16
DC_PAPERS = 2
DC_PAPERSIZE = 3
DC_PERSONALITY = 25
DC_PRINTERMEM = 28
DC_PRINTRATE = 26
DC_PRINTRATEPPM = 31
DC_PRINTRATEUNIT = 27
DC_SIZE = 8
DC_STAPLE = 30
DC_TRUETYPE = 15
DC_VERSION = 10
def _define_DOCINFOA_head():
    class DOCINFOA(Structure):
        pass
    return DOCINFOA
def _define_DOCINFOA():
    DOCINFOA = win32more.Storage.Xps.DOCINFOA_head
    DOCINFOA._fields_ = [
        ('cbSize', Int32),
        ('lpszDocName', win32more.Foundation.PSTR),
        ('lpszOutput', win32more.Foundation.PSTR),
        ('lpszDatatype', win32more.Foundation.PSTR),
        ('fwType', UInt32),
    ]
    return DOCINFOA
def _define_DOCINFOW_head():
    class DOCINFOW(Structure):
        pass
    return DOCINFOW
def _define_DOCINFOW():
    DOCINFOW = win32more.Storage.Xps.DOCINFOW_head
    DOCINFOW._fields_ = [
        ('cbSize', Int32),
        ('lpszDocName', win32more.Foundation.PWSTR),
        ('lpszOutput', win32more.Foundation.PWSTR),
        ('lpszDatatype', win32more.Foundation.PWSTR),
        ('fwType', UInt32),
    ]
    return DOCINFOW
def _define_DRAWPATRECT_head():
    class DRAWPATRECT(Structure):
        pass
    return DRAWPATRECT
def _define_DRAWPATRECT():
    DRAWPATRECT = win32more.Storage.Xps.DRAWPATRECT_head
    DRAWPATRECT._fields_ = [
        ('ptPosition', win32more.Foundation.POINT),
        ('ptSize', win32more.Foundation.POINT),
        ('wStyle', UInt16),
        ('wPattern', UInt16),
    ]
    return DRAWPATRECT
HPTPROVIDER = IntPtr
def _define_IXpsDocumentPackageTarget_head():
    class IXpsDocumentPackageTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('3b0b6d38-53ad-41da-b2-12-d3-76-37-a6-71-4e')
    return IXpsDocumentPackageTarget
def _define_IXpsDocumentPackageTarget():
    IXpsDocumentPackageTarget = win32more.Storage.Xps.IXpsDocumentPackageTarget_head
    IXpsDocumentPackageTarget.GetXpsOMPackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(3, 'GetXpsOMPackageWriter', ((1, 'documentSequencePartName'),(1, 'discardControlPartName'),(1, 'packageWriter'),)))
    IXpsDocumentPackageTarget.GetXpsOMFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMObjectFactory_head))(4, 'GetXpsOMFactory', ((1, 'xpsFactory'),)))
    IXpsDocumentPackageTarget.GetXpsType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(5, 'GetXpsType', ((1, 'documentType'),)))
    win32more.System.Com.IUnknown
    return IXpsDocumentPackageTarget
def _define_IXpsDocumentPackageTarget3D_head():
    class IXpsDocumentPackageTarget3D(win32more.System.Com.IUnknown_head):
        Guid = Guid('60ba71b8-3101-4984-91-99-f4-ea-77-5f-f0-1d')
    return IXpsDocumentPackageTarget3D
def _define_IXpsDocumentPackageTarget3D():
    IXpsDocumentPackageTarget3D = win32more.Storage.Xps.IXpsDocumentPackageTarget3D_head
    IXpsDocumentPackageTarget3D.GetXpsOMPackageWriter3D = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter3D_head))(3, 'GetXpsOMPackageWriter3D', ((1, 'documentSequencePartName'),(1, 'discardControlPartName'),(1, 'modelPartName'),(1, 'modelData'),(1, 'packageWriter'),)))
    IXpsDocumentPackageTarget3D.GetXpsOMFactory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMObjectFactory_head))(4, 'GetXpsOMFactory', ((1, 'xpsFactory'),)))
    win32more.System.Com.IUnknown
    return IXpsDocumentPackageTarget3D
def _define_IXpsOMBrush_head():
    class IXpsOMBrush(win32more.Storage.Xps.IXpsOMShareable_head):
        Guid = Guid('56a3f80c-ea4c-4187-a5-7b-a2-a4-73-b2-b4-2b')
    return IXpsOMBrush
def _define_IXpsOMBrush():
    IXpsOMBrush = win32more.Storage.Xps.IXpsOMBrush_head
    IXpsOMBrush.GetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(5, 'GetOpacity', ((1, 'opacity'),)))
    IXpsOMBrush.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(6, 'SetOpacity', ((1, 'opacity'),)))
    win32more.Storage.Xps.IXpsOMShareable
    return IXpsOMBrush
def _define_IXpsOMCanvas_head():
    class IXpsOMCanvas(win32more.Storage.Xps.IXpsOMVisual_head):
        Guid = Guid('221d1452-331e-47c6-87-e9-6c-ce-fb-9b-5b-a3')
    return IXpsOMCanvas
def _define_IXpsOMCanvas():
    IXpsOMCanvas = win32more.Storage.Xps.IXpsOMCanvas_head
    IXpsOMCanvas.GetVisuals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMVisualCollection_head))(30, 'GetVisuals', ((1, 'visuals'),)))
    IXpsOMCanvas.GetUseAliasedEdgeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(31, 'GetUseAliasedEdgeMode', ((1, 'useAliasedEdgeMode'),)))
    IXpsOMCanvas.SetUseAliasedEdgeMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(32, 'SetUseAliasedEdgeMode', ((1, 'useAliasedEdgeMode'),)))
    IXpsOMCanvas.GetAccessibilityShortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(33, 'GetAccessibilityShortDescription', ((1, 'shortDescription'),)))
    IXpsOMCanvas.SetAccessibilityShortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(34, 'SetAccessibilityShortDescription', ((1, 'shortDescription'),)))
    IXpsOMCanvas.GetAccessibilityLongDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(35, 'GetAccessibilityLongDescription', ((1, 'longDescription'),)))
    IXpsOMCanvas.SetAccessibilityLongDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(36, 'SetAccessibilityLongDescription', ((1, 'longDescription'),)))
    IXpsOMCanvas.GetDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(37, 'GetDictionary', ((1, 'resourceDictionary'),)))
    IXpsOMCanvas.GetDictionaryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(38, 'GetDictionaryLocal', ((1, 'resourceDictionary'),)))
    IXpsOMCanvas.SetDictionaryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDictionary_head)(39, 'SetDictionaryLocal', ((1, 'resourceDictionary'),)))
    IXpsOMCanvas.GetDictionaryResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(40, 'GetDictionaryResource', ((1, 'remoteDictionaryResource'),)))
    IXpsOMCanvas.SetDictionaryResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)(41, 'SetDictionaryResource', ((1, 'remoteDictionaryResource'),)))
    IXpsOMCanvas.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMCanvas_head))(42, 'Clone', ((1, 'canvas'),)))
    win32more.Storage.Xps.IXpsOMVisual
    return IXpsOMCanvas
def _define_IXpsOMColorProfileResource_head():
    class IXpsOMColorProfileResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('67bd7d69-1eef-4bb1-b5-e7-6f-4f-87-be-8a-be')
    return IXpsOMColorProfileResource
def _define_IXpsOMColorProfileResource():
    IXpsOMColorProfileResource = win32more.Storage.Xps.IXpsOMColorProfileResource_head
    IXpsOMColorProfileResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(5, 'GetStream', ((1, 'stream'),)))
    IXpsOMColorProfileResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(6, 'SetContent', ((1, 'sourceStream'),(1, 'partName'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMColorProfileResource
def _define_IXpsOMColorProfileResourceCollection_head():
    class IXpsOMColorProfileResourceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('12759630-5fba-4283-8f-7d-cc-a8-49-80-9e-db')
    return IXpsOMColorProfileResourceCollection
def _define_IXpsOMColorProfileResourceCollection():
    IXpsOMColorProfileResourceCollection = win32more.Storage.Xps.IXpsOMColorProfileResourceCollection_head
    IXpsOMColorProfileResourceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMColorProfileResourceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(4, 'GetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMColorProfileResourceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMColorProfileResource_head)(5, 'InsertAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMColorProfileResourceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMColorProfileResourceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMColorProfileResource_head)(7, 'SetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMColorProfileResourceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMColorProfileResource_head)(8, 'Append', ((1, 'object'),)))
    IXpsOMColorProfileResourceCollection.GetByPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(9, 'GetByPartName', ((1, 'partName'),(1, 'part'),)))
    win32more.System.Com.IUnknown
    return IXpsOMColorProfileResourceCollection
def _define_IXpsOMCoreProperties_head():
    class IXpsOMCoreProperties(win32more.Storage.Xps.IXpsOMPart_head):
        Guid = Guid('3340fe8f-4027-4aa1-8f-5f-d3-5a-e4-5f-e5-97')
    return IXpsOMCoreProperties
def _define_IXpsOMCoreProperties():
    IXpsOMCoreProperties = win32more.Storage.Xps.IXpsOMCoreProperties_head
    IXpsOMCoreProperties.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPackage_head))(5, 'GetOwner', ((1, 'package'),)))
    IXpsOMCoreProperties.GetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetCategory', ((1, 'category'),)))
    IXpsOMCoreProperties.SetCategory = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(7, 'SetCategory', ((1, 'category'),)))
    IXpsOMCoreProperties.GetContentStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetContentStatus', ((1, 'contentStatus'),)))
    IXpsOMCoreProperties.SetContentStatus = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'SetContentStatus', ((1, 'contentStatus'),)))
    IXpsOMCoreProperties.GetContentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'GetContentType', ((1, 'contentType'),)))
    IXpsOMCoreProperties.SetContentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'SetContentType', ((1, 'contentType'),)))
    IXpsOMCoreProperties.GetCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(12, 'GetCreated', ((1, 'created'),)))
    IXpsOMCoreProperties.SetCreated = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(13, 'SetCreated', ((1, 'created'),)))
    IXpsOMCoreProperties.GetCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(14, 'GetCreator', ((1, 'creator'),)))
    IXpsOMCoreProperties.SetCreator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(15, 'SetCreator', ((1, 'creator'),)))
    IXpsOMCoreProperties.GetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(16, 'GetDescription', ((1, 'description'),)))
    IXpsOMCoreProperties.SetDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(17, 'SetDescription', ((1, 'description'),)))
    IXpsOMCoreProperties.GetIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(18, 'GetIdentifier', ((1, 'identifier'),)))
    IXpsOMCoreProperties.SetIdentifier = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(19, 'SetIdentifier', ((1, 'identifier'),)))
    IXpsOMCoreProperties.GetKeywords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(20, 'GetKeywords', ((1, 'keywords'),)))
    IXpsOMCoreProperties.SetKeywords = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(21, 'SetKeywords', ((1, 'keywords'),)))
    IXpsOMCoreProperties.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(22, 'GetLanguage', ((1, 'language'),)))
    IXpsOMCoreProperties.SetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(23, 'SetLanguage', ((1, 'language'),)))
    IXpsOMCoreProperties.GetLastModifiedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(24, 'GetLastModifiedBy', ((1, 'lastModifiedBy'),)))
    IXpsOMCoreProperties.SetLastModifiedBy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(25, 'SetLastModifiedBy', ((1, 'lastModifiedBy'),)))
    IXpsOMCoreProperties.GetLastPrinted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(26, 'GetLastPrinted', ((1, 'lastPrinted'),)))
    IXpsOMCoreProperties.SetLastPrinted = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(27, 'SetLastPrinted', ((1, 'lastPrinted'),)))
    IXpsOMCoreProperties.GetModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(28, 'GetModified', ((1, 'modified'),)))
    IXpsOMCoreProperties.SetModified = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.SYSTEMTIME_head))(29, 'SetModified', ((1, 'modified'),)))
    IXpsOMCoreProperties.GetRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(30, 'GetRevision', ((1, 'revision'),)))
    IXpsOMCoreProperties.SetRevision = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(31, 'SetRevision', ((1, 'revision'),)))
    IXpsOMCoreProperties.GetSubject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(32, 'GetSubject', ((1, 'subject'),)))
    IXpsOMCoreProperties.SetSubject = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(33, 'SetSubject', ((1, 'subject'),)))
    IXpsOMCoreProperties.GetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(34, 'GetTitle', ((1, 'title'),)))
    IXpsOMCoreProperties.SetTitle = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(35, 'SetTitle', ((1, 'title'),)))
    IXpsOMCoreProperties.GetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(36, 'GetVersion', ((1, 'version'),)))
    IXpsOMCoreProperties.SetVersion = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(37, 'SetVersion', ((1, 'version'),)))
    IXpsOMCoreProperties.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head))(38, 'Clone', ((1, 'coreProperties'),)))
    win32more.Storage.Xps.IXpsOMPart
    return IXpsOMCoreProperties
def _define_IXpsOMDashCollection_head():
    class IXpsOMDashCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('081613f4-74eb-48f2-83-b3-37-a9-ce-2d-7d-c6')
    return IXpsOMDashCollection
def _define_IXpsOMDashCollection():
    IXpsOMDashCollection = win32more.Storage.Xps.IXpsOMDashCollection_head
    IXpsOMDashCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMDashCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.XPS_DASH_head))(4, 'GetAt', ((1, 'index'),(1, 'dash'),)))
    IXpsOMDashCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.XPS_DASH_head))(5, 'InsertAt', ((1, 'index'),(1, 'dash'),)))
    IXpsOMDashCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMDashCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.XPS_DASH_head))(7, 'SetAt', ((1, 'index'),(1, 'dash'),)))
    IXpsOMDashCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DASH_head))(8, 'Append', ((1, 'dash'),)))
    win32more.System.Com.IUnknown
    return IXpsOMDashCollection
def _define_IXpsOMDictionary_head():
    class IXpsOMDictionary(win32more.System.Com.IUnknown_head):
        Guid = Guid('897c86b8-8eaf-4ae3-bd-de-56-41-9f-cf-42-36')
    return IXpsOMDictionary
def _define_IXpsOMDictionary():
    IXpsOMDictionary = win32more.Storage.Xps.IXpsOMDictionary_head
    IXpsOMDictionary.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetOwner', ((1, 'owner'),)))
    IXpsOMDictionary.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(4, 'GetCount', ((1, 'count'),)))
    IXpsOMDictionary.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR),POINTER(win32more.Storage.Xps.IXpsOMShareable_head))(5, 'GetAt', ((1, 'index'),(1, 'key'),(1, 'entry'),)))
    IXpsOMDictionary.GetByKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.Xps.IXpsOMShareable_head,POINTER(win32more.Storage.Xps.IXpsOMShareable_head))(6, 'GetByKey', ((1, 'key'),(1, 'beforeEntry'),(1, 'entry'),)))
    IXpsOMDictionary.GetIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMShareable_head,POINTER(UInt32))(7, 'GetIndex', ((1, 'entry'),(1, 'index'),)))
    IXpsOMDictionary.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Storage.Xps.IXpsOMShareable_head)(8, 'Append', ((1, 'key'),(1, 'entry'),)))
    IXpsOMDictionary.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Storage.Xps.IXpsOMShareable_head)(9, 'InsertAt', ((1, 'index'),(1, 'key'),(1, 'entry'),)))
    IXpsOMDictionary.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(10, 'RemoveAt', ((1, 'index'),)))
    IXpsOMDictionary.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Foundation.PWSTR,win32more.Storage.Xps.IXpsOMShareable_head)(11, 'SetAt', ((1, 'index'),(1, 'key'),(1, 'entry'),)))
    IXpsOMDictionary.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(12, 'Clone', ((1, 'dictionary'),)))
    win32more.System.Com.IUnknown
    return IXpsOMDictionary
def _define_IXpsOMDocument_head():
    class IXpsOMDocument(win32more.Storage.Xps.IXpsOMPart_head):
        Guid = Guid('2c2c94cb-ac5f-4254-8e-e9-23-94-83-09-d9-f0')
    return IXpsOMDocument
def _define_IXpsOMDocument():
    IXpsOMDocument = win32more.Storage.Xps.IXpsOMDocument_head
    IXpsOMDocument.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head))(5, 'GetOwner', ((1, 'documentSequence'),)))
    IXpsOMDocument.GetPageReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPageReferenceCollection_head))(6, 'GetPageReferences', ((1, 'pageReferences'),)))
    IXpsOMDocument.GetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head))(7, 'GetPrintTicketResource', ((1, 'printTicketResource'),)))
    IXpsOMDocument.SetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPrintTicketResource_head)(8, 'SetPrintTicketResource', ((1, 'printTicketResource'),)))
    IXpsOMDocument.GetDocumentStructureResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocumentStructureResource_head))(9, 'GetDocumentStructureResource', ((1, 'documentStructureResource'),)))
    IXpsOMDocument.SetDocumentStructureResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDocumentStructureResource_head)(10, 'SetDocumentStructureResource', ((1, 'documentStructureResource'),)))
    IXpsOMDocument.GetSignatureBlockResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head))(11, 'GetSignatureBlockResources', ((1, 'signatureBlockResources'),)))
    IXpsOMDocument.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(12, 'Clone', ((1, 'document'),)))
    win32more.Storage.Xps.IXpsOMPart
    return IXpsOMDocument
def _define_IXpsOMDocumentCollection_head():
    class IXpsOMDocumentCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('d1c87f0d-e947-4754-8a-25-97-14-78-f7-e8-3e')
    return IXpsOMDocumentCollection
def _define_IXpsOMDocumentCollection():
    IXpsOMDocumentCollection = win32more.Storage.Xps.IXpsOMDocumentCollection_head
    IXpsOMDocumentCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMDocumentCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(4, 'GetAt', ((1, 'index'),(1, 'document'),)))
    IXpsOMDocumentCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMDocument_head)(5, 'InsertAt', ((1, 'index'),(1, 'document'),)))
    IXpsOMDocumentCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMDocumentCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMDocument_head)(7, 'SetAt', ((1, 'index'),(1, 'document'),)))
    IXpsOMDocumentCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDocument_head)(8, 'Append', ((1, 'document'),)))
    win32more.System.Com.IUnknown
    return IXpsOMDocumentCollection
def _define_IXpsOMDocumentSequence_head():
    class IXpsOMDocumentSequence(win32more.Storage.Xps.IXpsOMPart_head):
        Guid = Guid('56492eb4-d8d5-425e-82-56-4c-2b-64-ad-02-64')
    return IXpsOMDocumentSequence
def _define_IXpsOMDocumentSequence():
    IXpsOMDocumentSequence = win32more.Storage.Xps.IXpsOMDocumentSequence_head
    IXpsOMDocumentSequence.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPackage_head))(5, 'GetOwner', ((1, 'package'),)))
    IXpsOMDocumentSequence.GetDocuments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocumentCollection_head))(6, 'GetDocuments', ((1, 'documents'),)))
    IXpsOMDocumentSequence.GetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head))(7, 'GetPrintTicketResource', ((1, 'printTicketResource'),)))
    IXpsOMDocumentSequence.SetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPrintTicketResource_head)(8, 'SetPrintTicketResource', ((1, 'printTicketResource'),)))
    win32more.Storage.Xps.IXpsOMPart
    return IXpsOMDocumentSequence
def _define_IXpsOMDocumentStructureResource_head():
    class IXpsOMDocumentStructureResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('85febc8a-6b63-48a9-af-07-70-64-e4-ec-ff-30')
    return IXpsOMDocumentStructureResource
def _define_IXpsOMDocumentStructureResource():
    IXpsOMDocumentStructureResource = win32more.Storage.Xps.IXpsOMDocumentStructureResource_head
    IXpsOMDocumentStructureResource.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(5, 'GetOwner', ((1, 'owner'),)))
    IXpsOMDocumentStructureResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(6, 'GetStream', ((1, 'stream'),)))
    IXpsOMDocumentStructureResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(7, 'SetContent', ((1, 'sourceStream'),(1, 'partName'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMDocumentStructureResource
def _define_IXpsOMFontResource_head():
    class IXpsOMFontResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('a8c45708-47d9-4af4-8d-20-33-b4-8c-9b-84-85')
    return IXpsOMFontResource
def _define_IXpsOMFontResource():
    IXpsOMFontResource = win32more.Storage.Xps.IXpsOMFontResource_head
    IXpsOMFontResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(5, 'GetStream', ((1, 'readerStream'),)))
    IXpsOMFontResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Xps.XPS_FONT_EMBEDDING,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(6, 'SetContent', ((1, 'sourceStream'),(1, 'embeddingOption'),(1, 'partName'),)))
    IXpsOMFontResource.GetEmbeddingOption = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_FONT_EMBEDDING))(7, 'GetEmbeddingOption', ((1, 'embeddingOption'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMFontResource
def _define_IXpsOMFontResourceCollection_head():
    class IXpsOMFontResourceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('70b4a6bb-88d4-4fa8-aa-f9-6d-9c-59-6f-db-ad')
    return IXpsOMFontResourceCollection
def _define_IXpsOMFontResourceCollection():
    IXpsOMFontResourceCollection = win32more.Storage.Xps.IXpsOMFontResourceCollection_head
    IXpsOMFontResourceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMFontResourceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMFontResource_head))(4, 'GetAt', ((1, 'index'),(1, 'value'),)))
    IXpsOMFontResourceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMFontResource_head)(5, 'SetAt', ((1, 'index'),(1, 'value'),)))
    IXpsOMFontResourceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMFontResource_head)(6, 'InsertAt', ((1, 'index'),(1, 'value'),)))
    IXpsOMFontResourceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMFontResource_head)(7, 'Append', ((1, 'value'),)))
    IXpsOMFontResourceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(8, 'RemoveAt', ((1, 'index'),)))
    IXpsOMFontResourceCollection.GetByPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMFontResource_head))(9, 'GetByPartName', ((1, 'partName'),(1, 'part'),)))
    win32more.System.Com.IUnknown
    return IXpsOMFontResourceCollection
def _define_IXpsOMGeometry_head():
    class IXpsOMGeometry(win32more.Storage.Xps.IXpsOMShareable_head):
        Guid = Guid('64fcf3d7-4d58-44ba-ad-73-a1-3a-f6-49-20-72')
    return IXpsOMGeometry
def _define_IXpsOMGeometry():
    IXpsOMGeometry = win32more.Storage.Xps.IXpsOMGeometry_head
    IXpsOMGeometry.GetFigures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometryFigureCollection_head))(5, 'GetFigures', ((1, 'figures'),)))
    IXpsOMGeometry.GetFillRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_FILL_RULE))(6, 'GetFillRule', ((1, 'fillRule'),)))
    IXpsOMGeometry.SetFillRule = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_FILL_RULE)(7, 'SetFillRule', ((1, 'fillRule'),)))
    IXpsOMGeometry.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(8, 'GetTransform', ((1, 'transform'),)))
    IXpsOMGeometry.GetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(9, 'GetTransformLocal', ((1, 'transform'),)))
    IXpsOMGeometry.SetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMMatrixTransform_head)(10, 'SetTransformLocal', ((1, 'transform'),)))
    IXpsOMGeometry.GetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetTransformLookup', ((1, 'lookup'),)))
    IXpsOMGeometry.SetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'SetTransformLookup', ((1, 'lookup'),)))
    IXpsOMGeometry.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(13, 'Clone', ((1, 'geometry'),)))
    win32more.Storage.Xps.IXpsOMShareable
    return IXpsOMGeometry
def _define_IXpsOMGeometryFigure_head():
    class IXpsOMGeometryFigure(win32more.System.Com.IUnknown_head):
        Guid = Guid('d410dc83-908c-443e-89-47-b1-79-5d-3c-16-5a')
    return IXpsOMGeometryFigure
def _define_IXpsOMGeometryFigure():
    IXpsOMGeometryFigure = win32more.Storage.Xps.IXpsOMGeometryFigure_head
    IXpsOMGeometryFigure.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(3, 'GetOwner', ((1, 'owner'),)))
    IXpsOMGeometryFigure.GetSegmentData = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(Single))(4, 'GetSegmentData', ((1, 'dataCount'),(1, 'segmentData'),)))
    IXpsOMGeometryFigure.GetSegmentTypes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Storage.Xps.XPS_SEGMENT_TYPE))(5, 'GetSegmentTypes', ((1, 'segmentCount'),(1, 'segmentTypes'),)))
    IXpsOMGeometryFigure.GetSegmentStrokes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Foundation.BOOL))(6, 'GetSegmentStrokes', ((1, 'segmentCount'),(1, 'segmentStrokes'),)))
    IXpsOMGeometryFigure.SetSegments = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,UInt32,POINTER(win32more.Storage.Xps.XPS_SEGMENT_TYPE),POINTER(Single),POINTER(win32more.Foundation.BOOL))(7, 'SetSegments', ((1, 'segmentCount'),(1, 'segmentDataCount'),(1, 'segmentTypes'),(1, 'segmentData'),(1, 'segmentStrokes'),)))
    IXpsOMGeometryFigure.GetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(8, 'GetStartPoint', ((1, 'startPoint'),)))
    IXpsOMGeometryFigure.SetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(9, 'SetStartPoint', ((1, 'startPoint'),)))
    IXpsOMGeometryFigure.GetIsClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(10, 'GetIsClosed', ((1, 'isClosed'),)))
    IXpsOMGeometryFigure.SetIsClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(11, 'SetIsClosed', ((1, 'isClosed'),)))
    IXpsOMGeometryFigure.GetIsFilled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(12, 'GetIsFilled', ((1, 'isFilled'),)))
    IXpsOMGeometryFigure.SetIsFilled = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(13, 'SetIsFilled', ((1, 'isFilled'),)))
    IXpsOMGeometryFigure.GetSegmentCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(14, 'GetSegmentCount', ((1, 'segmentCount'),)))
    IXpsOMGeometryFigure.GetSegmentDataCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'GetSegmentDataCount', ((1, 'segmentDataCount'),)))
    IXpsOMGeometryFigure.GetSegmentStrokePattern = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SEGMENT_STROKE_PATTERN))(16, 'GetSegmentStrokePattern', ((1, 'segmentStrokePattern'),)))
    IXpsOMGeometryFigure.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head))(17, 'Clone', ((1, 'geometryFigure'),)))
    win32more.System.Com.IUnknown
    return IXpsOMGeometryFigure
def _define_IXpsOMGeometryFigureCollection_head():
    class IXpsOMGeometryFigureCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('fd48c3f3-a58e-4b5a-88-26-1d-e5-4a-be-72-b2')
    return IXpsOMGeometryFigureCollection
def _define_IXpsOMGeometryFigureCollection():
    IXpsOMGeometryFigureCollection = win32more.Storage.Xps.IXpsOMGeometryFigureCollection_head
    IXpsOMGeometryFigureCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMGeometryFigureCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head))(4, 'GetAt', ((1, 'index'),(1, 'geometryFigure'),)))
    IXpsOMGeometryFigureCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMGeometryFigure_head)(5, 'InsertAt', ((1, 'index'),(1, 'geometryFigure'),)))
    IXpsOMGeometryFigureCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMGeometryFigureCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMGeometryFigure_head)(7, 'SetAt', ((1, 'index'),(1, 'geometryFigure'),)))
    IXpsOMGeometryFigureCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGeometryFigure_head)(8, 'Append', ((1, 'geometryFigure'),)))
    win32more.System.Com.IUnknown
    return IXpsOMGeometryFigureCollection
def _define_IXpsOMGlyphs_head():
    class IXpsOMGlyphs(win32more.Storage.Xps.IXpsOMVisual_head):
        Guid = Guid('819b3199-0a5a-4b64-be-c7-a9-e1-7e-78-0d-e2')
    return IXpsOMGlyphs
def _define_IXpsOMGlyphs():
    IXpsOMGlyphs = win32more.Storage.Xps.IXpsOMGlyphs_head
    IXpsOMGlyphs.GetUnicodeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(30, 'GetUnicodeString', ((1, 'unicodeString'),)))
    IXpsOMGlyphs.GetGlyphIndexCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(31, 'GetGlyphIndexCount', ((1, 'indexCount'),)))
    IXpsOMGlyphs.GetGlyphIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head))(32, 'GetGlyphIndices', ((1, 'indexCount'),(1, 'glyphIndices'),)))
    IXpsOMGlyphs.GetGlyphMappingCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(33, 'GetGlyphMappingCount', ((1, 'glyphMappingCount'),)))
    IXpsOMGlyphs.GetGlyphMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head))(34, 'GetGlyphMappings', ((1, 'glyphMappingCount'),(1, 'glyphMappings'),)))
    IXpsOMGlyphs.GetProhibitedCaretStopCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(35, 'GetProhibitedCaretStopCount', ((1, 'prohibitedCaretStopCount'),)))
    IXpsOMGlyphs.GetProhibitedCaretStops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(36, 'GetProhibitedCaretStops', ((1, 'prohibitedCaretStopCount'),(1, 'prohibitedCaretStops'),)))
    IXpsOMGlyphs.GetBidiLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(37, 'GetBidiLevel', ((1, 'bidiLevel'),)))
    IXpsOMGlyphs.GetIsSideways = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(38, 'GetIsSideways', ((1, 'isSideways'),)))
    IXpsOMGlyphs.GetDeviceFontName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(39, 'GetDeviceFontName', ((1, 'deviceFontName'),)))
    IXpsOMGlyphs.GetStyleSimulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_STYLE_SIMULATION))(40, 'GetStyleSimulations', ((1, 'styleSimulations'),)))
    IXpsOMGlyphs.SetStyleSimulations = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_STYLE_SIMULATION)(41, 'SetStyleSimulations', ((1, 'styleSimulations'),)))
    IXpsOMGlyphs.GetOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(42, 'GetOrigin', ((1, 'origin'),)))
    IXpsOMGlyphs.SetOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(43, 'SetOrigin', ((1, 'origin'),)))
    IXpsOMGlyphs.GetFontRenderingEmSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(44, 'GetFontRenderingEmSize', ((1, 'fontRenderingEmSize'),)))
    IXpsOMGlyphs.SetFontRenderingEmSize = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(45, 'SetFontRenderingEmSize', ((1, 'fontRenderingEmSize'),)))
    IXpsOMGlyphs.GetFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMFontResource_head))(46, 'GetFontResource', ((1, 'fontResource'),)))
    IXpsOMGlyphs.SetFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMFontResource_head)(47, 'SetFontResource', ((1, 'fontResource'),)))
    IXpsOMGlyphs.GetFontFaceIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int16))(48, 'GetFontFaceIndex', ((1, 'fontFaceIndex'),)))
    IXpsOMGlyphs.SetFontFaceIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int16)(49, 'SetFontFaceIndex', ((1, 'fontFaceIndex'),)))
    IXpsOMGlyphs.GetFillBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(50, 'GetFillBrush', ((1, 'fillBrush'),)))
    IXpsOMGlyphs.GetFillBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(51, 'GetFillBrushLocal', ((1, 'fillBrush'),)))
    IXpsOMGlyphs.SetFillBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMBrush_head)(52, 'SetFillBrushLocal', ((1, 'fillBrush'),)))
    IXpsOMGlyphs.GetFillBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(53, 'GetFillBrushLookup', ((1, 'key'),)))
    IXpsOMGlyphs.SetFillBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(54, 'SetFillBrushLookup', ((1, 'key'),)))
    IXpsOMGlyphs.GetGlyphsEditor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGlyphsEditor_head))(55, 'GetGlyphsEditor', ((1, 'editor'),)))
    IXpsOMGlyphs.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGlyphs_head))(56, 'Clone', ((1, 'glyphs'),)))
    win32more.Storage.Xps.IXpsOMVisual
    return IXpsOMGlyphs
def _define_IXpsOMGlyphsEditor_head():
    class IXpsOMGlyphsEditor(win32more.System.Com.IUnknown_head):
        Guid = Guid('a5ab8616-5b16-4b9f-96-29-89-b3-23-ed-79-09')
    return IXpsOMGlyphsEditor
def _define_IXpsOMGlyphsEditor():
    IXpsOMGlyphsEditor = win32more.Storage.Xps.IXpsOMGlyphsEditor_head
    IXpsOMGlyphsEditor.ApplyEdits = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(3, 'ApplyEdits', ()))
    IXpsOMGlyphsEditor.GetUnicodeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(4, 'GetUnicodeString', ((1, 'unicodeString'),)))
    IXpsOMGlyphsEditor.SetUnicodeString = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(5, 'SetUnicodeString', ((1, 'unicodeString'),)))
    IXpsOMGlyphsEditor.GetGlyphIndexCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(6, 'GetGlyphIndexCount', ((1, 'indexCount'),)))
    IXpsOMGlyphsEditor.GetGlyphIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head))(7, 'GetGlyphIndices', ((1, 'indexCount'),(1, 'glyphIndices'),)))
    IXpsOMGlyphsEditor.SetGlyphIndices = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.XPS_GLYPH_INDEX_head))(8, 'SetGlyphIndices', ((1, 'indexCount'),(1, 'glyphIndices'),)))
    IXpsOMGlyphsEditor.GetGlyphMappingCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(9, 'GetGlyphMappingCount', ((1, 'glyphMappingCount'),)))
    IXpsOMGlyphsEditor.GetGlyphMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head))(10, 'GetGlyphMappings', ((1, 'glyphMappingCount'),(1, 'glyphMappings'),)))
    IXpsOMGlyphsEditor.SetGlyphMappings = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.XPS_GLYPH_MAPPING_head))(11, 'SetGlyphMappings', ((1, 'glyphMappingCount'),(1, 'glyphMappings'),)))
    IXpsOMGlyphsEditor.GetProhibitedCaretStopCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(12, 'GetProhibitedCaretStopCount', ((1, 'prohibitedCaretStopCount'),)))
    IXpsOMGlyphsEditor.GetProhibitedCaretStops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32),POINTER(UInt32))(13, 'GetProhibitedCaretStops', ((1, 'count'),(1, 'prohibitedCaretStops'),)))
    IXpsOMGlyphsEditor.SetProhibitedCaretStops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(UInt32))(14, 'SetProhibitedCaretStops', ((1, 'count'),(1, 'prohibitedCaretStops'),)))
    IXpsOMGlyphsEditor.GetBidiLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(15, 'GetBidiLevel', ((1, 'bidiLevel'),)))
    IXpsOMGlyphsEditor.SetBidiLevel = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(16, 'SetBidiLevel', ((1, 'bidiLevel'),)))
    IXpsOMGlyphsEditor.GetIsSideways = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(17, 'GetIsSideways', ((1, 'isSideways'),)))
    IXpsOMGlyphsEditor.SetIsSideways = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(18, 'SetIsSideways', ((1, 'isSideways'),)))
    IXpsOMGlyphsEditor.GetDeviceFontName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(19, 'GetDeviceFontName', ((1, 'deviceFontName'),)))
    IXpsOMGlyphsEditor.SetDeviceFontName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(20, 'SetDeviceFontName', ((1, 'deviceFontName'),)))
    win32more.System.Com.IUnknown
    return IXpsOMGlyphsEditor
def _define_IXpsOMGradientBrush_head():
    class IXpsOMGradientBrush(win32more.Storage.Xps.IXpsOMBrush_head):
        Guid = Guid('edb59622-61a2-42c3-ba-ce-ac-f2-28-6c-06-bf')
    return IXpsOMGradientBrush
def _define_IXpsOMGradientBrush():
    IXpsOMGradientBrush = win32more.Storage.Xps.IXpsOMGradientBrush_head
    IXpsOMGradientBrush.GetGradientStops = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGradientStopCollection_head))(7, 'GetGradientStops', ((1, 'gradientStops'),)))
    IXpsOMGradientBrush.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(8, 'GetTransform', ((1, 'transform'),)))
    IXpsOMGradientBrush.GetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(9, 'GetTransformLocal', ((1, 'transform'),)))
    IXpsOMGradientBrush.SetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMMatrixTransform_head)(10, 'SetTransformLocal', ((1, 'transform'),)))
    IXpsOMGradientBrush.GetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(11, 'GetTransformLookup', ((1, 'key'),)))
    IXpsOMGradientBrush.SetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(12, 'SetTransformLookup', ((1, 'key'),)))
    IXpsOMGradientBrush.GetSpreadMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SPREAD_METHOD))(13, 'GetSpreadMethod', ((1, 'spreadMethod'),)))
    IXpsOMGradientBrush.SetSpreadMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_SPREAD_METHOD)(14, 'SetSpreadMethod', ((1, 'spreadMethod'),)))
    IXpsOMGradientBrush.GetColorInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_INTERPOLATION))(15, 'GetColorInterpolationMode', ((1, 'colorInterpolationMode'),)))
    IXpsOMGradientBrush.SetColorInterpolationMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_COLOR_INTERPOLATION)(16, 'SetColorInterpolationMode', ((1, 'colorInterpolationMode'),)))
    win32more.Storage.Xps.IXpsOMBrush
    return IXpsOMGradientBrush
def _define_IXpsOMGradientStop_head():
    class IXpsOMGradientStop(win32more.System.Com.IUnknown_head):
        Guid = Guid('5cf4f5cc-3969-49b5-a7-0a-55-50-b6-18-fe-49')
    return IXpsOMGradientStop
def _define_IXpsOMGradientStop():
    IXpsOMGradientStop = win32more.Storage.Xps.IXpsOMGradientStop_head
    IXpsOMGradientStop.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGradientBrush_head))(3, 'GetOwner', ((1, 'owner'),)))
    IXpsOMGradientStop.GetOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(4, 'GetOffset', ((1, 'offset'),)))
    IXpsOMGradientStop.SetOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(5, 'SetOffset', ((1, 'offset'),)))
    IXpsOMGradientStop.GetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(6, 'GetColor', ((1, 'color'),(1, 'colorProfile'),)))
    IXpsOMGradientStop.SetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),win32more.Storage.Xps.IXpsOMColorProfileResource_head)(7, 'SetColor', ((1, 'color'),(1, 'colorProfile'),)))
    IXpsOMGradientStop.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head))(8, 'Clone', ((1, 'gradientStop'),)))
    win32more.System.Com.IUnknown
    return IXpsOMGradientStop
def _define_IXpsOMGradientStopCollection_head():
    class IXpsOMGradientStopCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('c9174c3a-3cd3-4319-bd-a4-11-a3-93-92-ce-ef')
    return IXpsOMGradientStopCollection
def _define_IXpsOMGradientStopCollection():
    IXpsOMGradientStopCollection = win32more.Storage.Xps.IXpsOMGradientStopCollection_head
    IXpsOMGradientStopCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMGradientStopCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head))(4, 'GetAt', ((1, 'index'),(1, 'stop'),)))
    IXpsOMGradientStopCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMGradientStop_head)(5, 'InsertAt', ((1, 'index'),(1, 'stop'),)))
    IXpsOMGradientStopCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMGradientStopCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMGradientStop_head)(7, 'SetAt', ((1, 'index'),(1, 'stop'),)))
    IXpsOMGradientStopCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGradientStop_head)(8, 'Append', ((1, 'stop'),)))
    win32more.System.Com.IUnknown
    return IXpsOMGradientStopCollection
def _define_IXpsOMImageBrush_head():
    class IXpsOMImageBrush(win32more.Storage.Xps.IXpsOMTileBrush_head):
        Guid = Guid('3df0b466-d382-49ef-85-50-dd-94-c8-02-42-e4')
    return IXpsOMImageBrush
def _define_IXpsOMImageBrush():
    IXpsOMImageBrush = win32more.Storage.Xps.IXpsOMImageBrush_head
    IXpsOMImageBrush.GetImageResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(18, 'GetImageResource', ((1, 'imageResource'),)))
    IXpsOMImageBrush.SetImageResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(19, 'SetImageResource', ((1, 'imageResource'),)))
    IXpsOMImageBrush.GetColorProfileResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(20, 'GetColorProfileResource', ((1, 'colorProfileResource'),)))
    IXpsOMImageBrush.SetColorProfileResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMColorProfileResource_head)(21, 'SetColorProfileResource', ((1, 'colorProfileResource'),)))
    IXpsOMImageBrush.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMImageBrush_head))(22, 'Clone', ((1, 'imageBrush'),)))
    win32more.Storage.Xps.IXpsOMTileBrush
    return IXpsOMImageBrush
def _define_IXpsOMImageResource_head():
    class IXpsOMImageResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('3db8417d-ae50-485e-9a-44-d7-75-8f-78-a2-3f')
    return IXpsOMImageResource
def _define_IXpsOMImageResource():
    IXpsOMImageResource = win32more.Storage.Xps.IXpsOMImageResource_head
    IXpsOMImageResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(5, 'GetStream', ((1, 'readerStream'),)))
    IXpsOMImageResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Xps.XPS_IMAGE_TYPE,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(6, 'SetContent', ((1, 'sourceStream'),(1, 'imageType'),(1, 'partName'),)))
    IXpsOMImageResource.GetImageType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_IMAGE_TYPE))(7, 'GetImageType', ((1, 'imageType'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMImageResource
def _define_IXpsOMImageResourceCollection_head():
    class IXpsOMImageResourceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('7a4a1a71-9cde-4b71-b3-3f-62-de-84-3e-ab-fe')
    return IXpsOMImageResourceCollection
def _define_IXpsOMImageResourceCollection():
    IXpsOMImageResourceCollection = win32more.Storage.Xps.IXpsOMImageResourceCollection_head
    IXpsOMImageResourceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMImageResourceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(4, 'GetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMImageResourceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMImageResource_head)(5, 'InsertAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMImageResourceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMImageResourceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMImageResource_head)(7, 'SetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMImageResourceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(8, 'Append', ((1, 'object'),)))
    IXpsOMImageResourceCollection.GetByPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(9, 'GetByPartName', ((1, 'partName'),(1, 'part'),)))
    win32more.System.Com.IUnknown
    return IXpsOMImageResourceCollection
def _define_IXpsOMLinearGradientBrush_head():
    class IXpsOMLinearGradientBrush(win32more.Storage.Xps.IXpsOMGradientBrush_head):
        Guid = Guid('005e279f-c30d-40ff-93-ec-19-50-d3-c5-28-db')
    return IXpsOMLinearGradientBrush
def _define_IXpsOMLinearGradientBrush():
    IXpsOMLinearGradientBrush = win32more.Storage.Xps.IXpsOMLinearGradientBrush_head
    IXpsOMLinearGradientBrush.GetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(17, 'GetStartPoint', ((1, 'startPoint'),)))
    IXpsOMLinearGradientBrush.SetStartPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(18, 'SetStartPoint', ((1, 'startPoint'),)))
    IXpsOMLinearGradientBrush.GetEndPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(19, 'GetEndPoint', ((1, 'endPoint'),)))
    IXpsOMLinearGradientBrush.SetEndPoint = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(20, 'SetEndPoint', ((1, 'endPoint'),)))
    IXpsOMLinearGradientBrush.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMLinearGradientBrush_head))(21, 'Clone', ((1, 'linearGradientBrush'),)))
    win32more.Storage.Xps.IXpsOMGradientBrush
    return IXpsOMLinearGradientBrush
def _define_IXpsOMMatrixTransform_head():
    class IXpsOMMatrixTransform(win32more.Storage.Xps.IXpsOMShareable_head):
        Guid = Guid('b77330ff-bb37-4501-a9-3e-f1-b1-e5-0b-fc-46')
    return IXpsOMMatrixTransform
def _define_IXpsOMMatrixTransform():
    IXpsOMMatrixTransform = win32more.Storage.Xps.IXpsOMMatrixTransform_head
    IXpsOMMatrixTransform.GetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_MATRIX_head))(5, 'GetMatrix', ((1, 'matrix'),)))
    IXpsOMMatrixTransform.SetMatrix = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_MATRIX_head))(6, 'SetMatrix', ((1, 'matrix'),)))
    IXpsOMMatrixTransform.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(7, 'Clone', ((1, 'matrixTransform'),)))
    win32more.Storage.Xps.IXpsOMShareable
    return IXpsOMMatrixTransform
def _define_IXpsOMNameCollection_head():
    class IXpsOMNameCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('4bddf8ec-c915-421b-a1-66-d1-73-d2-56-53-d2')
    return IXpsOMNameCollection
def _define_IXpsOMNameCollection():
    IXpsOMNameCollection = win32more.Storage.Xps.IXpsOMNameCollection_head
    IXpsOMNameCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMNameCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Foundation.PWSTR))(4, 'GetAt', ((1, 'index'),(1, 'name'),)))
    win32more.System.Com.IUnknown
    return IXpsOMNameCollection
def _define_IXpsOMObjectFactory_head():
    class IXpsOMObjectFactory(win32more.System.Com.IUnknown_head):
        Guid = Guid('f9b2a685-a50d-4fc2-b7-64-b5-6e-09-3e-a0-ca')
    return IXpsOMObjectFactory
def _define_IXpsOMObjectFactory():
    IXpsOMObjectFactory = win32more.Storage.Xps.IXpsOMObjectFactory_head
    IXpsOMObjectFactory.CreatePackage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPackage_head))(3, 'CreatePackage', ((1, 'package'),)))
    IXpsOMObjectFactory.CreatePackageFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPackage_head))(4, 'CreatePackageFromFile', ((1, 'filename'),(1, 'reuseObjects'),(1, 'package'),)))
    IXpsOMObjectFactory.CreatePackageFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPackage_head))(5, 'CreatePackageFromStream', ((1, 'stream'),(1, 'reuseObjects'),(1, 'package'),)))
    IXpsOMObjectFactory.CreateStoryFragmentsResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head))(6, 'CreateStoryFragmentsResource', ((1, 'acquiredStream'),(1, 'partUri'),(1, 'storyFragmentsResource'),)))
    IXpsOMObjectFactory.CreateDocumentStructureResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMDocumentStructureResource_head))(7, 'CreateDocumentStructureResource', ((1, 'acquiredStream'),(1, 'partUri'),(1, 'documentStructureResource'),)))
    IXpsOMObjectFactory.CreateSignatureBlockResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head))(8, 'CreateSignatureBlockResource', ((1, 'acquiredStream'),(1, 'partUri'),(1, 'signatureBlockResource'),)))
    IXpsOMObjectFactory.CreateRemoteDictionaryResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDictionary_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(9, 'CreateRemoteDictionaryResource', ((1, 'dictionary'),(1, 'partUri'),(1, 'remoteDictionaryResource'),)))
    IXpsOMObjectFactory.CreateRemoteDictionaryResourceFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPartResources_head,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(10, 'CreateRemoteDictionaryResourceFromStream', ((1, 'dictionaryMarkupStream'),(1, 'dictionaryPartUri'),(1, 'resources'),(1, 'dictionaryResource'),)))
    IXpsOMObjectFactory.CreatePartResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPartResources_head))(11, 'CreatePartResources', ((1, 'partResources'),)))
    IXpsOMObjectFactory.CreateDocumentSequence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head))(12, 'CreateDocumentSequence', ((1, 'partUri'),(1, 'documentSequence'),)))
    IXpsOMObjectFactory.CreateDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(13, 'CreateDocument', ((1, 'partUri'),(1, 'document'),)))
    IXpsOMObjectFactory.CreatePageReference = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head),POINTER(win32more.Storage.Xps.IXpsOMPageReference_head))(14, 'CreatePageReference', ((1, 'advisoryPageDimensions'),(1, 'pageReference'),)))
    IXpsOMObjectFactory.CreatePage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head),win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPage_head))(15, 'CreatePage', ((1, 'pageDimensions'),(1, 'language'),(1, 'partUri'),(1, 'page'),)))
    IXpsOMObjectFactory.CreatePageFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPartResources_head,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPage_head))(16, 'CreatePageFromStream', ((1, 'pageMarkupStream'),(1, 'partUri'),(1, 'resources'),(1, 'reuseObjects'),(1, 'page'),)))
    IXpsOMObjectFactory.CreateCanvas = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMCanvas_head))(17, 'CreateCanvas', ((1, 'canvas'),)))
    IXpsOMObjectFactory.CreateGlyphs = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMFontResource_head,POINTER(win32more.Storage.Xps.IXpsOMGlyphs_head))(18, 'CreateGlyphs', ((1, 'fontResource'),(1, 'glyphs'),)))
    IXpsOMObjectFactory.CreatePath = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPath_head))(19, 'CreatePath', ((1, 'path'),)))
    IXpsOMObjectFactory.CreateGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(20, 'CreateGeometry', ((1, 'geometry'),)))
    IXpsOMObjectFactory.CreateGeometryFigure = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head),POINTER(win32more.Storage.Xps.IXpsOMGeometryFigure_head))(21, 'CreateGeometryFigure', ((1, 'startPoint'),(1, 'figure'),)))
    IXpsOMObjectFactory.CreateMatrixTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_MATRIX_head),POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(22, 'CreateMatrixTransform', ((1, 'matrix'),(1, 'transform'),)))
    IXpsOMObjectFactory.CreateSolidColorBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),win32more.Storage.Xps.IXpsOMColorProfileResource_head,POINTER(win32more.Storage.Xps.IXpsOMSolidColorBrush_head))(23, 'CreateSolidColorBrush', ((1, 'color'),(1, 'colorProfile'),(1, 'solidColorBrush'),)))
    IXpsOMObjectFactory.CreateColorProfileResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(24, 'CreateColorProfileResource', ((1, 'acquiredStream'),(1, 'partUri'),(1, 'colorProfileResource'),)))
    IXpsOMObjectFactory.CreateImageBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head,POINTER(win32more.Storage.Xps.XPS_RECT_head),POINTER(win32more.Storage.Xps.XPS_RECT_head),POINTER(win32more.Storage.Xps.IXpsOMImageBrush_head))(25, 'CreateImageBrush', ((1, 'image'),(1, 'viewBox'),(1, 'viewPort'),(1, 'imageBrush'),)))
    IXpsOMObjectFactory.CreateVisualBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head),POINTER(win32more.Storage.Xps.XPS_RECT_head),POINTER(win32more.Storage.Xps.IXpsOMVisualBrush_head))(26, 'CreateVisualBrush', ((1, 'viewBox'),(1, 'viewPort'),(1, 'visualBrush'),)))
    IXpsOMObjectFactory.CreateImageResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Xps.XPS_IMAGE_TYPE,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(27, 'CreateImageResource', ((1, 'acquiredStream'),(1, 'contentType'),(1, 'partUri'),(1, 'imageResource'),)))
    IXpsOMObjectFactory.CreatePrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head))(28, 'CreatePrintTicketResource', ((1, 'acquiredStream'),(1, 'partUri'),(1, 'printTicketResource'),)))
    IXpsOMObjectFactory.CreateFontResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Xps.XPS_FONT_EMBEDDING,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMFontResource_head))(29, 'CreateFontResource', ((1, 'acquiredStream'),(1, 'fontEmbedding'),(1, 'partUri'),(1, 'isObfSourceStream'),(1, 'fontResource'),)))
    IXpsOMObjectFactory.CreateGradientStop = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),win32more.Storage.Xps.IXpsOMColorProfileResource_head,Single,POINTER(win32more.Storage.Xps.IXpsOMGradientStop_head))(30, 'CreateGradientStop', ((1, 'color'),(1, 'colorProfile'),(1, 'offset'),(1, 'gradientStop'),)))
    IXpsOMObjectFactory.CreateLinearGradientBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGradientStop_head,win32more.Storage.Xps.IXpsOMGradientStop_head,POINTER(win32more.Storage.Xps.XPS_POINT_head),POINTER(win32more.Storage.Xps.XPS_POINT_head),POINTER(win32more.Storage.Xps.IXpsOMLinearGradientBrush_head))(31, 'CreateLinearGradientBrush', ((1, 'gradStop1'),(1, 'gradStop2'),(1, 'startPoint'),(1, 'endPoint'),(1, 'linearGradientBrush'),)))
    IXpsOMObjectFactory.CreateRadialGradientBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGradientStop_head,win32more.Storage.Xps.IXpsOMGradientStop_head,POINTER(win32more.Storage.Xps.XPS_POINT_head),POINTER(win32more.Storage.Xps.XPS_POINT_head),POINTER(win32more.Storage.Xps.XPS_SIZE_head),POINTER(win32more.Storage.Xps.IXpsOMRadialGradientBrush_head))(32, 'CreateRadialGradientBrush', ((1, 'gradStop1'),(1, 'gradStop2'),(1, 'centerPoint'),(1, 'gradientOrigin'),(1, 'radiiSizes'),(1, 'radialGradientBrush'),)))
    IXpsOMObjectFactory.CreateCoreProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head))(33, 'CreateCoreProperties', ((1, 'partUri'),(1, 'coreProperties'),)))
    IXpsOMObjectFactory.CreateDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(34, 'CreateDictionary', ((1, 'dictionary'),)))
    IXpsOMObjectFactory.CreatePartUriCollection = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPartUriCollection_head))(35, 'CreatePartUriCollection', ((1, 'partUriCollection'),)))
    IXpsOMObjectFactory.CreatePackageWriterOnFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_INTERLEAVING,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMCoreProperties_head,win32more.Storage.Xps.IXpsOMImageResource_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(36, 'CreatePackageWriterOnFile', ((1, 'fileName'),(1, 'securityAttributes'),(1, 'flagsAndAttributes'),(1, 'optimizeMarkupSize'),(1, 'interleaving'),(1, 'documentSequencePartName'),(1, 'coreProperties'),(1, 'packageThumbnail'),(1, 'documentSequencePrintTicket'),(1, 'discardControlPartName'),(1, 'packageWriter'),)))
    IXpsOMObjectFactory.CreatePackageWriterOnStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_INTERLEAVING,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMCoreProperties_head,win32more.Storage.Xps.IXpsOMImageResource_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(37, 'CreatePackageWriterOnStream', ((1, 'outputStream'),(1, 'optimizeMarkupSize'),(1, 'interleaving'),(1, 'documentSequencePartName'),(1, 'coreProperties'),(1, 'packageThumbnail'),(1, 'documentSequencePrintTicket'),(1, 'discardControlPartName'),(1, 'packageWriter'),)))
    IXpsOMObjectFactory.CreatePartUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(38, 'CreatePartUri', ((1, 'uri'),(1, 'partUri'),)))
    IXpsOMObjectFactory.CreateReadOnlyStreamOnFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.System.Com.IStream_head))(39, 'CreateReadOnlyStreamOnFile', ((1, 'filename'),(1, 'stream'),)))
    win32more.System.Com.IUnknown
    return IXpsOMObjectFactory
def _define_IXpsOMObjectFactory1_head():
    class IXpsOMObjectFactory1(win32more.Storage.Xps.IXpsOMObjectFactory_head):
        Guid = Guid('0a91b617-d612-4181-bf-7c-be-58-24-e9-cc-8f')
    return IXpsOMObjectFactory1
def _define_IXpsOMObjectFactory1():
    IXpsOMObjectFactory1 = win32more.Storage.Xps.IXpsOMObjectFactory1_head
    IXpsOMObjectFactory1.GetDocumentTypeFromFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(40, 'GetDocumentTypeFromFile', ((1, 'filename'),(1, 'documentType'),)))
    IXpsOMObjectFactory1.GetDocumentTypeFromStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(41, 'GetDocumentTypeFromStream', ((1, 'xpsDocumentStream'),(1, 'documentType'),)))
    IXpsOMObjectFactory1.ConvertHDPhotoToJpegXR = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(42, 'ConvertHDPhotoToJpegXR', ((1, 'imageResource'),)))
    IXpsOMObjectFactory1.ConvertJpegXRToHDPhoto = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(43, 'ConvertJpegXRToHDPhoto', ((1, 'imageResource'),)))
    IXpsOMObjectFactory1.CreatePackageWriterOnFile1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_INTERLEAVING,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMCoreProperties_head,win32more.Storage.Xps.IXpsOMImageResource_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.XPS_DOCUMENT_TYPE,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(44, 'CreatePackageWriterOnFile1', ((1, 'fileName'),(1, 'securityAttributes'),(1, 'flagsAndAttributes'),(1, 'optimizeMarkupSize'),(1, 'interleaving'),(1, 'documentSequencePartName'),(1, 'coreProperties'),(1, 'packageThumbnail'),(1, 'documentSequencePrintTicket'),(1, 'discardControlPartName'),(1, 'documentType'),(1, 'packageWriter'),)))
    IXpsOMObjectFactory1.CreatePackageWriterOnStream1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_INTERLEAVING,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMCoreProperties_head,win32more.Storage.Xps.IXpsOMImageResource_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.XPS_DOCUMENT_TYPE,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(45, 'CreatePackageWriterOnStream1', ((1, 'outputStream'),(1, 'optimizeMarkupSize'),(1, 'interleaving'),(1, 'documentSequencePartName'),(1, 'coreProperties'),(1, 'packageThumbnail'),(1, 'documentSequencePrintTicket'),(1, 'discardControlPartName'),(1, 'documentType'),(1, 'packageWriter'),)))
    IXpsOMObjectFactory1.CreatePackage1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPackage1_head))(46, 'CreatePackage1', ((1, 'package'),)))
    IXpsOMObjectFactory1.CreatePackageFromStream1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPackage1_head))(47, 'CreatePackageFromStream1', ((1, 'stream'),(1, 'reuseObjects'),(1, 'package'),)))
    IXpsOMObjectFactory1.CreatePackageFromFile1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPackage1_head))(48, 'CreatePackageFromFile1', ((1, 'filename'),(1, 'reuseObjects'),(1, 'package'),)))
    IXpsOMObjectFactory1.CreatePage1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head),win32more.Foundation.PWSTR,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPage1_head))(49, 'CreatePage1', ((1, 'pageDimensions'),(1, 'language'),(1, 'partUri'),(1, 'page'),)))
    IXpsOMObjectFactory1.CreatePageFromStream1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPartResources_head,win32more.Foundation.BOOL,POINTER(win32more.Storage.Xps.IXpsOMPage1_head))(50, 'CreatePageFromStream1', ((1, 'pageMarkupStream'),(1, 'partUri'),(1, 'resources'),(1, 'reuseObjects'),(1, 'page'),)))
    IXpsOMObjectFactory1.CreateRemoteDictionaryResourceFromStream1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPartResources_head,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(51, 'CreateRemoteDictionaryResourceFromStream1', ((1, 'dictionaryMarkupStream'),(1, 'partUri'),(1, 'resources'),(1, 'dictionaryResource'),)))
    win32more.Storage.Xps.IXpsOMObjectFactory
    return IXpsOMObjectFactory1
def _define_IXpsOMPackage_head():
    class IXpsOMPackage(win32more.System.Com.IUnknown_head):
        Guid = Guid('18c3df65-81e1-4674-91-dc-fc-45-2f-5a-41-6f')
    return IXpsOMPackage
def _define_IXpsOMPackage():
    IXpsOMPackage = win32more.Storage.Xps.IXpsOMPackage_head
    IXpsOMPackage.GetDocumentSequence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocumentSequence_head))(3, 'GetDocumentSequence', ((1, 'documentSequence'),)))
    IXpsOMPackage.SetDocumentSequence = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDocumentSequence_head)(4, 'SetDocumentSequence', ((1, 'documentSequence'),)))
    IXpsOMPackage.GetCoreProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMCoreProperties_head))(5, 'GetCoreProperties', ((1, 'coreProperties'),)))
    IXpsOMPackage.SetCoreProperties = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMCoreProperties_head)(6, 'SetCoreProperties', ((1, 'coreProperties'),)))
    IXpsOMPackage.GetDiscardControlPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(7, 'GetDiscardControlPartName', ((1, 'discardControlPartUri'),)))
    IXpsOMPackage.SetDiscardControlPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(8, 'SetDiscardControlPartName', ((1, 'discardControlPartUri'),)))
    IXpsOMPackage.GetThumbnailResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(9, 'GetThumbnailResource', ((1, 'imageResource'),)))
    IXpsOMPackage.SetThumbnailResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(10, 'SetThumbnailResource', ((1, 'imageResource'),)))
    IXpsOMPackage.WriteToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.Foundation.BOOL)(11, 'WriteToFile', ((1, 'fileName'),(1, 'securityAttributes'),(1, 'flagsAndAttributes'),(1, 'optimizeMarkupSize'),)))
    IXpsOMPackage.WriteToStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL)(12, 'WriteToStream', ((1, 'stream'),(1, 'optimizeMarkupSize'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPackage
def _define_IXpsOMPackage1_head():
    class IXpsOMPackage1(win32more.Storage.Xps.IXpsOMPackage_head):
        Guid = Guid('95a9435e-12bb-461b-8e-7f-c6-ad-b0-4c-d9-6a')
    return IXpsOMPackage1
def _define_IXpsOMPackage1():
    IXpsOMPackage1 = win32more.Storage.Xps.IXpsOMPackage1_head
    IXpsOMPackage1.GetDocumentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(13, 'GetDocumentType', ((1, 'documentType'),)))
    IXpsOMPackage1.WriteToFile1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_DOCUMENT_TYPE)(14, 'WriteToFile1', ((1, 'fileName'),(1, 'securityAttributes'),(1, 'flagsAndAttributes'),(1, 'optimizeMarkupSize'),(1, 'documentType'),)))
    IXpsOMPackage1.WriteToStream1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_DOCUMENT_TYPE)(15, 'WriteToStream1', ((1, 'outputStream'),(1, 'optimizeMarkupSize'),(1, 'documentType'),)))
    win32more.Storage.Xps.IXpsOMPackage
    return IXpsOMPackage1
def _define_IXpsOMPackageTarget_head():
    class IXpsOMPackageTarget(win32more.System.Com.IUnknown_head):
        Guid = Guid('219a9db0-4959-47d0-80-34-b1-ce-84-f4-1a-4d')
    return IXpsOMPackageTarget
def _define_IXpsOMPackageTarget():
    IXpsOMPackageTarget = win32more.Storage.Xps.IXpsOMPackageTarget_head
    IXpsOMPackageTarget.CreateXpsOMPackageWriter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMPackageWriter_head))(3, 'CreateXpsOMPackageWriter', ((1, 'documentSequencePartName'),(1, 'documentSequencePrintTicket'),(1, 'discardControlPartName'),(1, 'packageWriter'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPackageTarget
def _define_IXpsOMPackageWriter_head():
    class IXpsOMPackageWriter(win32more.System.Com.IUnknown_head):
        Guid = Guid('4e2aa182-a443-42c6-b4-1b-4f-8e-9d-e7-3f-f9')
    return IXpsOMPackageWriter
def _define_IXpsOMPackageWriter():
    IXpsOMPackageWriter = win32more.Storage.Xps.IXpsOMPackageWriter_head
    IXpsOMPackageWriter.StartNewDocument = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Xps.IXpsOMDocumentStructureResource_head,win32more.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head,win32more.Storage.Xps.IXpsOMPartUriCollection_head)(3, 'StartNewDocument', ((1, 'documentPartName'),(1, 'documentPrintTicket'),(1, 'documentStructure'),(1, 'signatureBlockResources'),(1, 'restrictedFonts'),)))
    IXpsOMPackageWriter.AddPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPage_head,POINTER(win32more.Storage.Xps.XPS_SIZE_head),win32more.Storage.Xps.IXpsOMPartUriCollection_head,win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head,win32more.Storage.Xps.IXpsOMPrintTicketResource_head,win32more.Storage.Xps.IXpsOMImageResource_head)(4, 'AddPage', ((1, 'page'),(1, 'advisoryPageDimensions'),(1, 'discardableResourceParts'),(1, 'storyFragments'),(1, 'pagePrintTicket'),(1, 'pageThumbnail'),)))
    IXpsOMPackageWriter.AddResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMResource_head)(5, 'AddResource', ((1, 'resource'),)))
    IXpsOMPackageWriter.Close = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'Close', ()))
    IXpsOMPackageWriter.IsClosed = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'IsClosed', ((1, 'isClosed'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPackageWriter
def _define_IXpsOMPackageWriter3D_head():
    class IXpsOMPackageWriter3D(win32more.Storage.Xps.IXpsOMPackageWriter_head):
        Guid = Guid('e8a45033-640e-43fa-9b-df-fd-de-aa-31-c6-a0')
    return IXpsOMPackageWriter3D
def _define_IXpsOMPackageWriter3D():
    IXpsOMPackageWriter3D = win32more.Storage.Xps.IXpsOMPackageWriter3D_head
    IXpsOMPackageWriter3D.AddModelTexture = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.System.Com.IStream_head)(8, 'AddModelTexture', ((1, 'texturePartName'),(1, 'textureData'),)))
    IXpsOMPackageWriter3D.SetModelPrintTicket = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,win32more.System.Com.IStream_head)(9, 'SetModelPrintTicket', ((1, 'printTicketPartName'),(1, 'printTicketData'),)))
    win32more.Storage.Xps.IXpsOMPackageWriter
    return IXpsOMPackageWriter3D
def _define_IXpsOMPage_head():
    class IXpsOMPage(win32more.Storage.Xps.IXpsOMPart_head):
        Guid = Guid('d3e18888-f120-4fee-8c-68-35-29-6e-ae-91-d4')
    return IXpsOMPage
def _define_IXpsOMPage():
    IXpsOMPage = win32more.Storage.Xps.IXpsOMPage_head
    IXpsOMPage.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPageReference_head))(5, 'GetOwner', ((1, 'pageReference'),)))
    IXpsOMPage.GetVisuals = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMVisualCollection_head))(6, 'GetVisuals', ((1, 'visuals'),)))
    IXpsOMPage.GetPageDimensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(7, 'GetPageDimensions', ((1, 'pageDimensions'),)))
    IXpsOMPage.SetPageDimensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(8, 'SetPageDimensions', ((1, 'pageDimensions'),)))
    IXpsOMPage.GetContentBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(9, 'GetContentBox', ((1, 'contentBox'),)))
    IXpsOMPage.SetContentBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(10, 'SetContentBox', ((1, 'contentBox'),)))
    IXpsOMPage.GetBleedBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(11, 'GetBleedBox', ((1, 'bleedBox'),)))
    IXpsOMPage.SetBleedBox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(12, 'SetBleedBox', ((1, 'bleedBox'),)))
    IXpsOMPage.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetLanguage', ((1, 'language'),)))
    IXpsOMPage.SetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(14, 'SetLanguage', ((1, 'language'),)))
    IXpsOMPage.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(15, 'GetName', ((1, 'name'),)))
    IXpsOMPage.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(16, 'SetName', ((1, 'name'),)))
    IXpsOMPage.GetIsHyperlinkTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(17, 'GetIsHyperlinkTarget', ((1, 'isHyperlinkTarget'),)))
    IXpsOMPage.SetIsHyperlinkTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(18, 'SetIsHyperlinkTarget', ((1, 'isHyperlinkTarget'),)))
    IXpsOMPage.GetDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(19, 'GetDictionary', ((1, 'resourceDictionary'),)))
    IXpsOMPage.GetDictionaryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(20, 'GetDictionaryLocal', ((1, 'resourceDictionary'),)))
    IXpsOMPage.SetDictionaryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDictionary_head)(21, 'SetDictionaryLocal', ((1, 'resourceDictionary'),)))
    IXpsOMPage.GetDictionaryResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(22, 'GetDictionaryResource', ((1, 'remoteDictionaryResource'),)))
    IXpsOMPage.SetDictionaryResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)(23, 'SetDictionaryResource', ((1, 'remoteDictionaryResource'),)))
    IXpsOMPage.Write = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL)(24, 'Write', ((1, 'stream'),(1, 'optimizeMarkupSize'),)))
    IXpsOMPage.GenerateUnusedLookupKey = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_OBJECT_TYPE,POINTER(win32more.Foundation.PWSTR))(25, 'GenerateUnusedLookupKey', ((1, 'type'),(1, 'key'),)))
    IXpsOMPage.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPage_head))(26, 'Clone', ((1, 'page'),)))
    win32more.Storage.Xps.IXpsOMPart
    return IXpsOMPage
def _define_IXpsOMPage1_head():
    class IXpsOMPage1(win32more.Storage.Xps.IXpsOMPage_head):
        Guid = Guid('305b60ef-6892-4dda-9c-bb-3a-a6-59-74-50-8a')
    return IXpsOMPage1
def _define_IXpsOMPage1():
    IXpsOMPage1 = win32more.Storage.Xps.IXpsOMPage1_head
    IXpsOMPage1.GetDocumentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(27, 'GetDocumentType', ((1, 'documentType'),)))
    IXpsOMPage1.Write1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Foundation.BOOL,win32more.Storage.Xps.XPS_DOCUMENT_TYPE)(28, 'Write1', ((1, 'stream'),(1, 'optimizeMarkupSize'),(1, 'documentType'),)))
    win32more.Storage.Xps.IXpsOMPage
    return IXpsOMPage1
def _define_IXpsOMPageReference_head():
    class IXpsOMPageReference(win32more.System.Com.IUnknown_head):
        Guid = Guid('ed360180-6f92-4998-89-0d-2f-20-85-31-a0-a0')
    return IXpsOMPageReference
def _define_IXpsOMPageReference():
    IXpsOMPageReference = win32more.Storage.Xps.IXpsOMPageReference_head
    IXpsOMPageReference.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(3, 'GetOwner', ((1, 'document'),)))
    IXpsOMPageReference.GetPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPage_head))(4, 'GetPage', ((1, 'page'),)))
    IXpsOMPageReference.SetPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPage_head)(5, 'SetPage', ((1, 'page'),)))
    IXpsOMPageReference.DiscardPage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,)(6, 'DiscardPage', ()))
    IXpsOMPageReference.IsPageLoaded = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(7, 'IsPageLoaded', ((1, 'isPageLoaded'),)))
    IXpsOMPageReference.GetAdvisoryPageDimensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(8, 'GetAdvisoryPageDimensions', ((1, 'pageDimensions'),)))
    IXpsOMPageReference.SetAdvisoryPageDimensions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(9, 'SetAdvisoryPageDimensions', ((1, 'pageDimensions'),)))
    IXpsOMPageReference.GetStoryFragmentsResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head))(10, 'GetStoryFragmentsResource', ((1, 'storyFragmentsResource'),)))
    IXpsOMPageReference.SetStoryFragmentsResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head)(11, 'SetStoryFragmentsResource', ((1, 'storyFragmentsResource'),)))
    IXpsOMPageReference.GetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPrintTicketResource_head))(12, 'GetPrintTicketResource', ((1, 'printTicketResource'),)))
    IXpsOMPageReference.SetPrintTicketResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPrintTicketResource_head)(13, 'SetPrintTicketResource', ((1, 'printTicketResource'),)))
    IXpsOMPageReference.GetThumbnailResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(14, 'GetThumbnailResource', ((1, 'imageResource'),)))
    IXpsOMPageReference.SetThumbnailResource = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMImageResource_head)(15, 'SetThumbnailResource', ((1, 'imageResource'),)))
    IXpsOMPageReference.CollectLinkTargets = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMNameCollection_head))(16, 'CollectLinkTargets', ((1, 'linkTargets'),)))
    IXpsOMPageReference.CollectPartResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPartResources_head))(17, 'CollectPartResources', ((1, 'partResources'),)))
    IXpsOMPageReference.HasRestrictedFonts = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(18, 'HasRestrictedFonts', ((1, 'restrictedFonts'),)))
    IXpsOMPageReference.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPageReference_head))(19, 'Clone', ((1, 'pageReference'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPageReference
def _define_IXpsOMPageReferenceCollection_head():
    class IXpsOMPageReferenceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('ca16ba4d-e7b9-45c5-95-8b-f9-80-22-47-37-45')
    return IXpsOMPageReferenceCollection
def _define_IXpsOMPageReferenceCollection():
    IXpsOMPageReferenceCollection = win32more.Storage.Xps.IXpsOMPageReferenceCollection_head
    IXpsOMPageReferenceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMPageReferenceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMPageReference_head))(4, 'GetAt', ((1, 'index'),(1, 'pageReference'),)))
    IXpsOMPageReferenceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMPageReference_head)(5, 'InsertAt', ((1, 'index'),(1, 'pageReference'),)))
    IXpsOMPageReferenceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMPageReferenceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMPageReference_head)(7, 'SetAt', ((1, 'index'),(1, 'pageReference'),)))
    IXpsOMPageReferenceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPageReference_head)(8, 'Append', ((1, 'pageReference'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPageReferenceCollection
def _define_IXpsOMPart_head():
    class IXpsOMPart(win32more.System.Com.IUnknown_head):
        Guid = Guid('74eb2f0b-a91e-4486-af-ac-0f-ab-ec-a3-df-c6')
    return IXpsOMPart
def _define_IXpsOMPart():
    IXpsOMPart = win32more.Storage.Xps.IXpsOMPart_head
    IXpsOMPart.GetPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(3, 'GetPartName', ((1, 'partUri'),)))
    IXpsOMPart.SetPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(4, 'SetPartName', ((1, 'partUri'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPart
def _define_IXpsOMPartResources_head():
    class IXpsOMPartResources(win32more.System.Com.IUnknown_head):
        Guid = Guid('f4cf7729-4864-4275-99-b3-a8-71-71-63-ec-af')
    return IXpsOMPartResources
def _define_IXpsOMPartResources():
    IXpsOMPartResources = win32more.Storage.Xps.IXpsOMPartResources_head
    IXpsOMPartResources.GetFontResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMFontResourceCollection_head))(3, 'GetFontResources', ((1, 'fontResources'),)))
    IXpsOMPartResources.GetImageResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMImageResourceCollection_head))(4, 'GetImageResources', ((1, 'imageResources'),)))
    IXpsOMPartResources.GetColorProfileResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMColorProfileResourceCollection_head))(5, 'GetColorProfileResources', ((1, 'colorProfileResources'),)))
    IXpsOMPartResources.GetRemoteDictionaryResources = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResourceCollection_head))(6, 'GetRemoteDictionaryResources', ((1, 'dictionaryResources'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPartResources
def _define_IXpsOMPartUriCollection_head():
    class IXpsOMPartUriCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('57c650d4-067c-4893-8c-33-f6-2a-06-33-73-0f')
    return IXpsOMPartUriCollection
def _define_IXpsOMPartUriCollection():
    IXpsOMPartUriCollection = win32more.Storage.Xps.IXpsOMPartUriCollection_head
    IXpsOMPartUriCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMPartUriCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(4, 'GetAt', ((1, 'index'),(1, 'partUri'),)))
    IXpsOMPartUriCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(5, 'InsertAt', ((1, 'index'),(1, 'partUri'),)))
    IXpsOMPartUriCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMPartUriCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(7, 'SetAt', ((1, 'index'),(1, 'partUri'),)))
    IXpsOMPartUriCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(8, 'Append', ((1, 'partUri'),)))
    win32more.System.Com.IUnknown
    return IXpsOMPartUriCollection
def _define_IXpsOMPath_head():
    class IXpsOMPath(win32more.Storage.Xps.IXpsOMVisual_head):
        Guid = Guid('37d38bb6-3ee9-4110-93-12-14-b1-94-16-33-37')
    return IXpsOMPath
def _define_IXpsOMPath():
    IXpsOMPath = win32more.Storage.Xps.IXpsOMPath_head
    IXpsOMPath.GetGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(30, 'GetGeometry', ((1, 'geometry'),)))
    IXpsOMPath.GetGeometryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(31, 'GetGeometryLocal', ((1, 'geometry'),)))
    IXpsOMPath.SetGeometryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGeometry_head)(32, 'SetGeometryLocal', ((1, 'geometry'),)))
    IXpsOMPath.GetGeometryLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(33, 'GetGeometryLookup', ((1, 'lookup'),)))
    IXpsOMPath.SetGeometryLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(34, 'SetGeometryLookup', ((1, 'lookup'),)))
    IXpsOMPath.GetAccessibilityShortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(35, 'GetAccessibilityShortDescription', ((1, 'shortDescription'),)))
    IXpsOMPath.SetAccessibilityShortDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(36, 'SetAccessibilityShortDescription', ((1, 'shortDescription'),)))
    IXpsOMPath.GetAccessibilityLongDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(37, 'GetAccessibilityLongDescription', ((1, 'longDescription'),)))
    IXpsOMPath.SetAccessibilityLongDescription = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(38, 'SetAccessibilityLongDescription', ((1, 'longDescription'),)))
    IXpsOMPath.GetSnapsToPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(39, 'GetSnapsToPixels', ((1, 'snapsToPixels'),)))
    IXpsOMPath.SetSnapsToPixels = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(40, 'SetSnapsToPixels', ((1, 'snapsToPixels'),)))
    IXpsOMPath.GetStrokeBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(41, 'GetStrokeBrush', ((1, 'brush'),)))
    IXpsOMPath.GetStrokeBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(42, 'GetStrokeBrushLocal', ((1, 'brush'),)))
    IXpsOMPath.SetStrokeBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMBrush_head)(43, 'SetStrokeBrushLocal', ((1, 'brush'),)))
    IXpsOMPath.GetStrokeBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(44, 'GetStrokeBrushLookup', ((1, 'lookup'),)))
    IXpsOMPath.SetStrokeBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(45, 'SetStrokeBrushLookup', ((1, 'lookup'),)))
    IXpsOMPath.GetStrokeDashes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDashCollection_head))(46, 'GetStrokeDashes', ((1, 'strokeDashes'),)))
    IXpsOMPath.GetStrokeDashCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DASH_CAP))(47, 'GetStrokeDashCap', ((1, 'strokeDashCap'),)))
    IXpsOMPath.SetStrokeDashCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_DASH_CAP)(48, 'SetStrokeDashCap', ((1, 'strokeDashCap'),)))
    IXpsOMPath.GetStrokeDashOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(49, 'GetStrokeDashOffset', ((1, 'strokeDashOffset'),)))
    IXpsOMPath.SetStrokeDashOffset = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(50, 'SetStrokeDashOffset', ((1, 'strokeDashOffset'),)))
    IXpsOMPath.GetStrokeStartLineCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_LINE_CAP))(51, 'GetStrokeStartLineCap', ((1, 'strokeStartLineCap'),)))
    IXpsOMPath.SetStrokeStartLineCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_LINE_CAP)(52, 'SetStrokeStartLineCap', ((1, 'strokeStartLineCap'),)))
    IXpsOMPath.GetStrokeEndLineCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_LINE_CAP))(53, 'GetStrokeEndLineCap', ((1, 'strokeEndLineCap'),)))
    IXpsOMPath.SetStrokeEndLineCap = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_LINE_CAP)(54, 'SetStrokeEndLineCap', ((1, 'strokeEndLineCap'),)))
    IXpsOMPath.GetStrokeLineJoin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_LINE_JOIN))(55, 'GetStrokeLineJoin', ((1, 'strokeLineJoin'),)))
    IXpsOMPath.SetStrokeLineJoin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_LINE_JOIN)(56, 'SetStrokeLineJoin', ((1, 'strokeLineJoin'),)))
    IXpsOMPath.GetStrokeMiterLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(57, 'GetStrokeMiterLimit', ((1, 'strokeMiterLimit'),)))
    IXpsOMPath.SetStrokeMiterLimit = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(58, 'SetStrokeMiterLimit', ((1, 'strokeMiterLimit'),)))
    IXpsOMPath.GetStrokeThickness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(59, 'GetStrokeThickness', ((1, 'strokeThickness'),)))
    IXpsOMPath.SetStrokeThickness = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(60, 'SetStrokeThickness', ((1, 'strokeThickness'),)))
    IXpsOMPath.GetFillBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(61, 'GetFillBrush', ((1, 'brush'),)))
    IXpsOMPath.GetFillBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(62, 'GetFillBrushLocal', ((1, 'brush'),)))
    IXpsOMPath.SetFillBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMBrush_head)(63, 'SetFillBrushLocal', ((1, 'brush'),)))
    IXpsOMPath.GetFillBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(64, 'GetFillBrushLookup', ((1, 'lookup'),)))
    IXpsOMPath.SetFillBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(65, 'SetFillBrushLookup', ((1, 'lookup'),)))
    IXpsOMPath.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPath_head))(66, 'Clone', ((1, 'path'),)))
    win32more.Storage.Xps.IXpsOMVisual
    return IXpsOMPath
def _define_IXpsOMPrintTicketResource_head():
    class IXpsOMPrintTicketResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('e7ff32d2-34aa-499b-bb-e9-9c-d4-ee-6c-59-f7')
    return IXpsOMPrintTicketResource
def _define_IXpsOMPrintTicketResource():
    IXpsOMPrintTicketResource = win32more.Storage.Xps.IXpsOMPrintTicketResource_head
    IXpsOMPrintTicketResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(5, 'GetStream', ((1, 'stream'),)))
    IXpsOMPrintTicketResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(6, 'SetContent', ((1, 'sourceStream'),(1, 'partName'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMPrintTicketResource
def _define_IXpsOMRadialGradientBrush_head():
    class IXpsOMRadialGradientBrush(win32more.Storage.Xps.IXpsOMGradientBrush_head):
        Guid = Guid('75f207e5-08bf-413c-96-b1-b8-2b-40-64-17-6b')
    return IXpsOMRadialGradientBrush
def _define_IXpsOMRadialGradientBrush():
    IXpsOMRadialGradientBrush = win32more.Storage.Xps.IXpsOMRadialGradientBrush_head
    IXpsOMRadialGradientBrush.GetCenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(17, 'GetCenter', ((1, 'center'),)))
    IXpsOMRadialGradientBrush.SetCenter = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(18, 'SetCenter', ((1, 'center'),)))
    IXpsOMRadialGradientBrush.GetRadiiSizes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(19, 'GetRadiiSizes', ((1, 'radiiSizes'),)))
    IXpsOMRadialGradientBrush.SetRadiiSizes = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIZE_head))(20, 'SetRadiiSizes', ((1, 'radiiSizes'),)))
    IXpsOMRadialGradientBrush.GetGradientOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(21, 'GetGradientOrigin', ((1, 'origin'),)))
    IXpsOMRadialGradientBrush.SetGradientOrigin = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_POINT_head))(22, 'SetGradientOrigin', ((1, 'origin'),)))
    IXpsOMRadialGradientBrush.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMRadialGradientBrush_head))(23, 'Clone', ((1, 'radialGradientBrush'),)))
    win32more.Storage.Xps.IXpsOMGradientBrush
    return IXpsOMRadialGradientBrush
def _define_IXpsOMRemoteDictionaryResource_head():
    class IXpsOMRemoteDictionaryResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('c9bd7cd4-e16a-4bf8-8c-84-c9-50-af-7a-30-61')
    return IXpsOMRemoteDictionaryResource
def _define_IXpsOMRemoteDictionaryResource():
    IXpsOMRemoteDictionaryResource = win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head
    IXpsOMRemoteDictionaryResource.GetDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDictionary_head))(5, 'GetDictionary', ((1, 'dictionary'),)))
    IXpsOMRemoteDictionaryResource.SetDictionary = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMDictionary_head)(6, 'SetDictionary', ((1, 'dictionary'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMRemoteDictionaryResource
def _define_IXpsOMRemoteDictionaryResource1_head():
    class IXpsOMRemoteDictionaryResource1(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head):
        Guid = Guid('bf8fc1d4-9d46-4141-ba-5f-94-bb-92-50-d0-41')
    return IXpsOMRemoteDictionaryResource1
def _define_IXpsOMRemoteDictionaryResource1():
    IXpsOMRemoteDictionaryResource1 = win32more.Storage.Xps.IXpsOMRemoteDictionaryResource1_head
    IXpsOMRemoteDictionaryResource1.GetDocumentType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_DOCUMENT_TYPE))(7, 'GetDocumentType', ((1, 'documentType'),)))
    IXpsOMRemoteDictionaryResource1.Write1 = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.ISequentialStream_head,win32more.Storage.Xps.XPS_DOCUMENT_TYPE)(8, 'Write1', ((1, 'stream'),(1, 'documentType'),)))
    win32more.Storage.Xps.IXpsOMRemoteDictionaryResource
    return IXpsOMRemoteDictionaryResource1
def _define_IXpsOMRemoteDictionaryResourceCollection_head():
    class IXpsOMRemoteDictionaryResourceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('5c38db61-7fec-464a-87-bd-41-e3-be-f0-18-be')
    return IXpsOMRemoteDictionaryResourceCollection
def _define_IXpsOMRemoteDictionaryResourceCollection():
    IXpsOMRemoteDictionaryResourceCollection = win32more.Storage.Xps.IXpsOMRemoteDictionaryResourceCollection_head
    IXpsOMRemoteDictionaryResourceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMRemoteDictionaryResourceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(4, 'GetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMRemoteDictionaryResourceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)(5, 'InsertAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMRemoteDictionaryResourceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMRemoteDictionaryResourceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)(7, 'SetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMRemoteDictionaryResourceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head)(8, 'Append', ((1, 'object'),)))
    IXpsOMRemoteDictionaryResourceCollection.GetByPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMRemoteDictionaryResource_head))(9, 'GetByPartName', ((1, 'partName'),(1, 'remoteDictionaryResource'),)))
    win32more.System.Com.IUnknown
    return IXpsOMRemoteDictionaryResourceCollection
def _define_IXpsOMResource_head():
    class IXpsOMResource(win32more.Storage.Xps.IXpsOMPart_head):
        Guid = Guid('da2ac0a2-73a2-4975-ad-14-74-09-7c-3f-f3-a5')
    return IXpsOMResource
def _define_IXpsOMResource():
    IXpsOMResource = win32more.Storage.Xps.IXpsOMResource_head
    win32more.Storage.Xps.IXpsOMPart
    return IXpsOMResource
def _define_IXpsOMShareable_head():
    class IXpsOMShareable(win32more.System.Com.IUnknown_head):
        Guid = Guid('7137398f-2fc1-454d-8c-6a-2c-31-15-a1-6e-ce')
    return IXpsOMShareable
def _define_IXpsOMShareable():
    IXpsOMShareable = win32more.Storage.Xps.IXpsOMShareable_head
    IXpsOMShareable.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUnknown_head))(3, 'GetOwner', ((1, 'owner'),)))
    IXpsOMShareable.GetType = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_OBJECT_TYPE))(4, 'GetType', ((1, 'type'),)))
    win32more.System.Com.IUnknown
    return IXpsOMShareable
def _define_IXpsOMSignatureBlockResource_head():
    class IXpsOMSignatureBlockResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('4776ad35-2e04-4357-87-43-eb-f6-c1-71-a9-05')
    return IXpsOMSignatureBlockResource
def _define_IXpsOMSignatureBlockResource():
    IXpsOMSignatureBlockResource = win32more.Storage.Xps.IXpsOMSignatureBlockResource_head
    IXpsOMSignatureBlockResource.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMDocument_head))(5, 'GetOwner', ((1, 'owner'),)))
    IXpsOMSignatureBlockResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(6, 'GetStream', ((1, 'stream'),)))
    IXpsOMSignatureBlockResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(7, 'SetContent', ((1, 'sourceStream'),(1, 'partName'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMSignatureBlockResource
def _define_IXpsOMSignatureBlockResourceCollection_head():
    class IXpsOMSignatureBlockResourceCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('ab8f5d8e-351b-4d33-aa-ed-fa-56-f0-02-29-31')
    return IXpsOMSignatureBlockResourceCollection
def _define_IXpsOMSignatureBlockResourceCollection():
    IXpsOMSignatureBlockResourceCollection = win32more.Storage.Xps.IXpsOMSignatureBlockResourceCollection_head
    IXpsOMSignatureBlockResourceCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMSignatureBlockResourceCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head))(4, 'GetAt', ((1, 'index'),(1, 'signatureBlockResource'),)))
    IXpsOMSignatureBlockResourceCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)(5, 'InsertAt', ((1, 'index'),(1, 'signatureBlockResource'),)))
    IXpsOMSignatureBlockResourceCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMSignatureBlockResourceCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)(7, 'SetAt', ((1, 'index'),(1, 'signatureBlockResource'),)))
    IXpsOMSignatureBlockResourceCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMSignatureBlockResource_head)(8, 'Append', ((1, 'signatureBlockResource'),)))
    IXpsOMSignatureBlockResourceCollection.GetByPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMSignatureBlockResource_head))(9, 'GetByPartName', ((1, 'partName'),(1, 'signatureBlockResource'),)))
    win32more.System.Com.IUnknown
    return IXpsOMSignatureBlockResourceCollection
def _define_IXpsOMSolidColorBrush_head():
    class IXpsOMSolidColorBrush(win32more.Storage.Xps.IXpsOMBrush_head):
        Guid = Guid('a06f9f05-3be9-4763-98-a8-09-4f-c6-72-e4-88')
    return IXpsOMSolidColorBrush
def _define_IXpsOMSolidColorBrush():
    IXpsOMSolidColorBrush = win32more.Storage.Xps.IXpsOMSolidColorBrush_head
    IXpsOMSolidColorBrush.GetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),POINTER(win32more.Storage.Xps.IXpsOMColorProfileResource_head))(7, 'GetColor', ((1, 'color'),(1, 'colorProfile'),)))
    IXpsOMSolidColorBrush.SetColor = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_COLOR_head),win32more.Storage.Xps.IXpsOMColorProfileResource_head)(8, 'SetColor', ((1, 'color'),(1, 'colorProfile'),)))
    IXpsOMSolidColorBrush.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMSolidColorBrush_head))(9, 'Clone', ((1, 'solidColorBrush'),)))
    win32more.Storage.Xps.IXpsOMBrush
    return IXpsOMSolidColorBrush
def _define_IXpsOMStoryFragmentsResource_head():
    class IXpsOMStoryFragmentsResource(win32more.Storage.Xps.IXpsOMResource_head):
        Guid = Guid('c2b3ca09-0473-4282-87-ae-17-80-86-32-23-f0')
    return IXpsOMStoryFragmentsResource
def _define_IXpsOMStoryFragmentsResource():
    IXpsOMStoryFragmentsResource = win32more.Storage.Xps.IXpsOMStoryFragmentsResource_head
    IXpsOMStoryFragmentsResource.GetOwner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMPageReference_head))(5, 'GetOwner', ((1, 'owner'),)))
    IXpsOMStoryFragmentsResource.GetStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IStream_head))(6, 'GetStream', ((1, 'stream'),)))
    IXpsOMStoryFragmentsResource.SetContent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(7, 'SetContent', ((1, 'sourceStream'),(1, 'partName'),)))
    win32more.Storage.Xps.IXpsOMResource
    return IXpsOMStoryFragmentsResource
def _define_IXpsOMThumbnailGenerator_head():
    class IXpsOMThumbnailGenerator(win32more.System.Com.IUnknown_head):
        Guid = Guid('15b873d5-1971-41e8-83-a3-65-78-40-30-64-c7')
    return IXpsOMThumbnailGenerator
def _define_IXpsOMThumbnailGenerator():
    IXpsOMThumbnailGenerator = win32more.Storage.Xps.IXpsOMThumbnailGenerator_head
    IXpsOMThumbnailGenerator.GenerateThumbnail = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMPage_head,win32more.Storage.Xps.XPS_IMAGE_TYPE,win32more.Storage.Xps.XPS_THUMBNAIL_SIZE,win32more.Storage.Packaging.Opc.IOpcPartUri_head,POINTER(win32more.Storage.Xps.IXpsOMImageResource_head))(3, 'GenerateThumbnail', ((1, 'page'),(1, 'thumbnailType'),(1, 'thumbnailSize'),(1, 'imageResourcePartName'),(1, 'imageResource'),)))
    win32more.System.Com.IUnknown
    return IXpsOMThumbnailGenerator
def _define_IXpsOMTileBrush_head():
    class IXpsOMTileBrush(win32more.Storage.Xps.IXpsOMBrush_head):
        Guid = Guid('0fc2328d-d722-4a54-b2-ec-be-90-21-8a-78-9e')
    return IXpsOMTileBrush
def _define_IXpsOMTileBrush():
    IXpsOMTileBrush = win32more.Storage.Xps.IXpsOMTileBrush_head
    IXpsOMTileBrush.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(7, 'GetTransform', ((1, 'transform'),)))
    IXpsOMTileBrush.GetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(8, 'GetTransformLocal', ((1, 'transform'),)))
    IXpsOMTileBrush.SetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMMatrixTransform_head)(9, 'SetTransformLocal', ((1, 'transform'),)))
    IXpsOMTileBrush.GetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(10, 'GetTransformLookup', ((1, 'key'),)))
    IXpsOMTileBrush.SetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(11, 'SetTransformLookup', ((1, 'key'),)))
    IXpsOMTileBrush.GetViewbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(12, 'GetViewbox', ((1, 'viewbox'),)))
    IXpsOMTileBrush.SetViewbox = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(13, 'SetViewbox', ((1, 'viewbox'),)))
    IXpsOMTileBrush.GetViewport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(14, 'GetViewport', ((1, 'viewport'),)))
    IXpsOMTileBrush.SetViewport = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_RECT_head))(15, 'SetViewport', ((1, 'viewport'),)))
    IXpsOMTileBrush.GetTileMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_TILE_MODE))(16, 'GetTileMode', ((1, 'tileMode'),)))
    IXpsOMTileBrush.SetTileMode = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_TILE_MODE)(17, 'SetTileMode', ((1, 'tileMode'),)))
    win32more.Storage.Xps.IXpsOMBrush
    return IXpsOMTileBrush
def _define_IXpsOMVisual_head():
    class IXpsOMVisual(win32more.Storage.Xps.IXpsOMShareable_head):
        Guid = Guid('bc3e7333-fb0b-4af3-a8-19-0b-4e-aa-d0-d2-fd')
    return IXpsOMVisual
def _define_IXpsOMVisual():
    IXpsOMVisual = win32more.Storage.Xps.IXpsOMVisual_head
    IXpsOMVisual.GetTransform = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(5, 'GetTransform', ((1, 'matrixTransform'),)))
    IXpsOMVisual.GetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMMatrixTransform_head))(6, 'GetTransformLocal', ((1, 'matrixTransform'),)))
    IXpsOMVisual.SetTransformLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMMatrixTransform_head)(7, 'SetTransformLocal', ((1, 'matrixTransform'),)))
    IXpsOMVisual.GetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(8, 'GetTransformLookup', ((1, 'key'),)))
    IXpsOMVisual.SetTransformLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(9, 'SetTransformLookup', ((1, 'key'),)))
    IXpsOMVisual.GetClipGeometry = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(10, 'GetClipGeometry', ((1, 'clipGeometry'),)))
    IXpsOMVisual.GetClipGeometryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMGeometry_head))(11, 'GetClipGeometryLocal', ((1, 'clipGeometry'),)))
    IXpsOMVisual.SetClipGeometryLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMGeometry_head)(12, 'SetClipGeometryLocal', ((1, 'clipGeometry'),)))
    IXpsOMVisual.GetClipGeometryLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetClipGeometryLookup', ((1, 'key'),)))
    IXpsOMVisual.SetClipGeometryLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(14, 'SetClipGeometryLookup', ((1, 'key'),)))
    IXpsOMVisual.GetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Single))(15, 'GetOpacity', ((1, 'opacity'),)))
    IXpsOMVisual.SetOpacity = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Single)(16, 'SetOpacity', ((1, 'opacity'),)))
    IXpsOMVisual.GetOpacityMaskBrush = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(17, 'GetOpacityMaskBrush', ((1, 'opacityMaskBrush'),)))
    IXpsOMVisual.GetOpacityMaskBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMBrush_head))(18, 'GetOpacityMaskBrushLocal', ((1, 'opacityMaskBrush'),)))
    IXpsOMVisual.SetOpacityMaskBrushLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMBrush_head)(19, 'SetOpacityMaskBrushLocal', ((1, 'opacityMaskBrush'),)))
    IXpsOMVisual.GetOpacityMaskBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(20, 'GetOpacityMaskBrushLookup', ((1, 'key'),)))
    IXpsOMVisual.SetOpacityMaskBrushLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(21, 'SetOpacityMaskBrushLookup', ((1, 'key'),)))
    IXpsOMVisual.GetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(22, 'GetName', ((1, 'name'),)))
    IXpsOMVisual.SetName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(23, 'SetName', ((1, 'name'),)))
    IXpsOMVisual.GetIsHyperlinkTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.BOOL))(24, 'GetIsHyperlinkTarget', ((1, 'isHyperlink'),)))
    IXpsOMVisual.SetIsHyperlinkTarget = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.BOOL)(25, 'SetIsHyperlinkTarget', ((1, 'isHyperlink'),)))
    IXpsOMVisual.GetHyperlinkNavigateUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.System.Com.IUri_head))(26, 'GetHyperlinkNavigateUri', ((1, 'hyperlinkUri'),)))
    IXpsOMVisual.SetHyperlinkNavigateUri = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IUri_head)(27, 'SetHyperlinkNavigateUri', ((1, 'hyperlinkUri'),)))
    IXpsOMVisual.GetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(28, 'GetLanguage', ((1, 'language'),)))
    IXpsOMVisual.SetLanguage = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(29, 'SetLanguage', ((1, 'language'),)))
    win32more.Storage.Xps.IXpsOMShareable
    return IXpsOMVisual
def _define_IXpsOMVisualBrush_head():
    class IXpsOMVisualBrush(win32more.Storage.Xps.IXpsOMTileBrush_head):
        Guid = Guid('97e294af-5b37-46b4-80-57-87-4d-2f-64-11-9b')
    return IXpsOMVisualBrush
def _define_IXpsOMVisualBrush():
    IXpsOMVisualBrush = win32more.Storage.Xps.IXpsOMVisualBrush_head
    IXpsOMVisualBrush.GetVisual = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMVisual_head))(18, 'GetVisual', ((1, 'visual'),)))
    IXpsOMVisualBrush.GetVisualLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMVisual_head))(19, 'GetVisualLocal', ((1, 'visual'),)))
    IXpsOMVisualBrush.SetVisualLocal = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMVisual_head)(20, 'SetVisualLocal', ((1, 'visual'),)))
    IXpsOMVisualBrush.GetVisualLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(21, 'GetVisualLookup', ((1, 'lookup'),)))
    IXpsOMVisualBrush.SetVisualLookup = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(22, 'SetVisualLookup', ((1, 'lookup'),)))
    IXpsOMVisualBrush.Clone = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsOMVisualBrush_head))(23, 'Clone', ((1, 'visualBrush'),)))
    win32more.Storage.Xps.IXpsOMTileBrush
    return IXpsOMVisualBrush
def _define_IXpsOMVisualCollection_head():
    class IXpsOMVisualCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('94d8abde-ab91-46a8-82-b7-f5-b0-5e-f0-1a-96')
    return IXpsOMVisualCollection
def _define_IXpsOMVisualCollection():
    IXpsOMVisualCollection = win32more.Storage.Xps.IXpsOMVisualCollection_head
    IXpsOMVisualCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsOMVisualCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsOMVisual_head))(4, 'GetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMVisualCollection.InsertAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMVisual_head)(5, 'InsertAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMVisualCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(6, 'RemoveAt', ((1, 'index'),)))
    IXpsOMVisualCollection.SetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,win32more.Storage.Xps.IXpsOMVisual_head)(7, 'SetAt', ((1, 'index'),(1, 'object'),)))
    IXpsOMVisualCollection.Append = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsOMVisual_head)(8, 'Append', ((1, 'object'),)))
    win32more.System.Com.IUnknown
    return IXpsOMVisualCollection
def _define_IXpsSignature_head():
    class IXpsSignature(win32more.System.Com.IUnknown_head):
        Guid = Guid('6ae4c93e-1ade-42fb-89-8b-3a-56-58-28-48-57')
    return IXpsSignature
def _define_IXpsSignature():
    IXpsSignature = win32more.Storage.Xps.IXpsSignature_head
    IXpsSignature.GetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetSignatureId', ((1, 'sigId'),)))
    IXpsSignature.GetSignatureValue = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(4, 'GetSignatureValue', ((1, 'signatureHashValue'),(1, 'count'),)))
    IXpsSignature.GetCertificateEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateEnumerator_head))(5, 'GetCertificateEnumerator', ((1, 'certificateEnumerator'),)))
    IXpsSignature.GetSigningTime = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(6, 'GetSigningTime', ((1, 'sigDateTimeString'),)))
    IXpsSignature.GetSigningTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT))(7, 'GetSigningTimeFormat', ((1, 'timeFormat'),)))
    IXpsSignature.GetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(8, 'GetSignaturePartName', ((1, 'signaturePartName'),)))
    IXpsSignature.Verify = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Storage.Xps.XPS_SIGNATURE_STATUS))(9, 'Verify', ((1, 'x509Certificate'),(1, 'sigStatus'),)))
    IXpsSignature.GetPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIGN_POLICY))(10, 'GetPolicy', ((1, 'policy'),)))
    IXpsSignature.GetCustomObjectEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectEnumerator_head))(11, 'GetCustomObjectEnumerator', ((1, 'customObjectEnumerator'),)))
    IXpsSignature.GetCustomReferenceEnumerator = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceEnumerator_head))(12, 'GetCustomReferenceEnumerator', ((1, 'customReferenceEnumerator'),)))
    IXpsSignature.GetSignatureXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(c_char_p_no),POINTER(UInt32))(13, 'GetSignatureXml', ((1, 'signatureXml'),(1, 'count'),)))
    IXpsSignature.SetSignatureXml = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,c_char_p_no,UInt32)(14, 'SetSignatureXml', ((1, 'signatureXml'),(1, 'count'),)))
    win32more.System.Com.IUnknown
    return IXpsSignature
def _define_IXpsSignatureBlock_head():
    class IXpsSignatureBlock(win32more.System.Com.IUnknown_head):
        Guid = Guid('151fac09-0b97-4ac6-a3-23-5e-42-97-d4-32-2b')
    return IXpsSignatureBlock
def _define_IXpsSignatureBlock():
    IXpsSignatureBlock = win32more.Storage.Xps.IXpsSignatureBlock_head
    IXpsSignatureBlock.GetRequests = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsSignatureRequestCollection_head))(3, 'GetRequests', ((1, 'requests'),)))
    IXpsSignatureBlock.GetPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(4, 'GetPartName', ((1, 'partName'),)))
    IXpsSignatureBlock.GetDocumentIndex = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(5, 'GetDocumentIndex', ((1, 'fixedDocumentIndex'),)))
    IXpsSignatureBlock.GetDocumentName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(6, 'GetDocumentName', ((1, 'fixedDocumentName'),)))
    IXpsSignatureBlock.CreateRequest = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Storage.Xps.IXpsSignatureRequest_head))(7, 'CreateRequest', ((1, 'requestId'),(1, 'signatureRequest'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureBlock
def _define_IXpsSignatureBlockCollection_head():
    class IXpsSignatureBlockCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('23397050-fe99-467a-8d-ce-92-37-f0-74-ff-e4')
    return IXpsSignatureBlockCollection
def _define_IXpsSignatureBlockCollection():
    IXpsSignatureBlockCollection = win32more.Storage.Xps.IXpsSignatureBlockCollection_head
    IXpsSignatureBlockCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsSignatureBlockCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsSignatureBlock_head))(4, 'GetAt', ((1, 'index'),(1, 'signatureBlock'),)))
    IXpsSignatureBlockCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'RemoveAt', ((1, 'index'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureBlockCollection
def _define_IXpsSignatureCollection_head():
    class IXpsSignatureCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('a2d1d95d-add2-4dff-ab-27-6b-9c-64-5f-f3-22')
    return IXpsSignatureCollection
def _define_IXpsSignatureCollection():
    IXpsSignatureCollection = win32more.Storage.Xps.IXpsSignatureCollection_head
    IXpsSignatureCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsSignatureCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsSignature_head))(4, 'GetAt', ((1, 'index'),(1, 'signature'),)))
    IXpsSignatureCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'RemoveAt', ((1, 'index'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureCollection
def _define_IXpsSignatureManager_head():
    class IXpsSignatureManager(win32more.System.Com.IUnknown_head):
        Guid = Guid('d3e8d338-fdc4-4afc-80-b5-d5-32-a1-78-2e-e1')
    return IXpsSignatureManager
def _define_IXpsSignatureManager():
    IXpsSignatureManager = win32more.Storage.Xps.IXpsSignatureManager_head
    IXpsSignatureManager.LoadPackageFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(3, 'LoadPackageFile', ((1, 'fileName'),)))
    IXpsSignatureManager.LoadPackageStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(4, 'LoadPackageStream', ((1, 'stream'),)))
    IXpsSignatureManager.Sign = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.IXpsSigningOptions_head,POINTER(win32more.Security.Cryptography.CERT_CONTEXT_head),POINTER(win32more.Storage.Xps.IXpsSignature_head))(5, 'Sign', ((1, 'signOptions'),(1, 'x509Certificate'),(1, 'signature'),)))
    IXpsSignatureManager.GetSignatureOriginPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(6, 'GetSignatureOriginPartName', ((1, 'signatureOriginPartName'),)))
    IXpsSignatureManager.SetSignatureOriginPartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(7, 'SetSignatureOriginPartName', ((1, 'signatureOriginPartName'),)))
    IXpsSignatureManager.GetSignatures = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsSignatureCollection_head))(8, 'GetSignatures', ((1, 'signatures'),)))
    IXpsSignatureManager.AddSignatureBlock = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head,UInt32,POINTER(win32more.Storage.Xps.IXpsSignatureBlock_head))(9, 'AddSignatureBlock', ((1, 'partName'),(1, 'fixedDocumentIndex'),(1, 'signatureBlock'),)))
    IXpsSignatureManager.GetSignatureBlocks = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsSignatureBlockCollection_head))(10, 'GetSignatureBlocks', ((1, 'signatureBlocks'),)))
    IXpsSignatureManager.CreateSigningOptions = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsSigningOptions_head))(11, 'CreateSigningOptions', ((1, 'signingOptions'),)))
    IXpsSignatureManager.SavePackageToFile = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR,POINTER(win32more.Security.SECURITY_ATTRIBUTES_head),UInt32)(12, 'SavePackageToFile', ((1, 'fileName'),(1, 'securityAttributes'),(1, 'flagsAndAttributes'),)))
    IXpsSignatureManager.SavePackageToStream = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.System.Com.IStream_head)(13, 'SavePackageToStream', ((1, 'stream'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureManager
def _define_IXpsSignatureRequest_head():
    class IXpsSignatureRequest(win32more.System.Com.IUnknown_head):
        Guid = Guid('ac58950b-7208-4b2d-b2-c4-95-10-83-d3-b8-eb')
    return IXpsSignatureRequest
def _define_IXpsSignatureRequest():
    IXpsSignatureRequest = win32more.Storage.Xps.IXpsSignatureRequest_head
    IXpsSignatureRequest.GetIntent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetIntent', ((1, 'intent'),)))
    IXpsSignatureRequest.SetIntent = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'SetIntent', ((1, 'intent'),)))
    IXpsSignatureRequest.GetRequestedSigner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetRequestedSigner', ((1, 'signerName'),)))
    IXpsSignatureRequest.SetRequestedSigner = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'SetRequestedSigner', ((1, 'signerName'),)))
    IXpsSignatureRequest.GetRequestSignByDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetRequestSignByDate', ((1, 'dateString'),)))
    IXpsSignatureRequest.SetRequestSignByDate = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'SetRequestSignByDate', ((1, 'dateString'),)))
    IXpsSignatureRequest.GetSigningLocale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(9, 'GetSigningLocale', ((1, 'place'),)))
    IXpsSignatureRequest.SetSigningLocale = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(10, 'SetSigningLocale', ((1, 'place'),)))
    IXpsSignatureRequest.GetSpotLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(Int32),POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head),POINTER(Single),POINTER(Single))(11, 'GetSpotLocation', ((1, 'pageIndex'),(1, 'pagePartName'),(1, 'x'),(1, 'y'),)))
    IXpsSignatureRequest.SetSpotLocation = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,Int32,Single,Single)(12, 'SetSpotLocation', ((1, 'pageIndex'),(1, 'x'),(1, 'y'),)))
    IXpsSignatureRequest.GetRequestId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(13, 'GetRequestId', ((1, 'requestId'),)))
    IXpsSignatureRequest.GetSignature = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.IXpsSignature_head))(14, 'GetSignature', ((1, 'signature'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureRequest
def _define_IXpsSignatureRequestCollection_head():
    class IXpsSignatureRequestCollection(win32more.System.Com.IUnknown_head):
        Guid = Guid('f0253e68-9f19-412e-9b-4f-54-d3-b0-ac-6c-d9')
    return IXpsSignatureRequestCollection
def _define_IXpsSignatureRequestCollection():
    IXpsSignatureRequestCollection = win32more.Storage.Xps.IXpsSignatureRequestCollection_head
    IXpsSignatureRequestCollection.GetCount = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(UInt32))(3, 'GetCount', ((1, 'count'),)))
    IXpsSignatureRequestCollection.GetAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32,POINTER(win32more.Storage.Xps.IXpsSignatureRequest_head))(4, 'GetAt', ((1, 'index'),(1, 'signatureRequest'),)))
    IXpsSignatureRequestCollection.RemoveAt = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,UInt32)(5, 'RemoveAt', ((1, 'index'),)))
    win32more.System.Com.IUnknown
    return IXpsSignatureRequestCollection
def _define_IXpsSigningOptions_head():
    class IXpsSigningOptions(win32more.System.Com.IUnknown_head):
        Guid = Guid('7718eae4-3215-49be-af-5b-59-4f-ef-7f-cf-a6')
    return IXpsSigningOptions
def _define_IXpsSigningOptions():
    IXpsSigningOptions = win32more.Storage.Xps.IXpsSigningOptions_head
    IXpsSigningOptions.GetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(3, 'GetSignatureId', ((1, 'signatureId'),)))
    IXpsSigningOptions.SetSignatureId = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(4, 'SetSignatureId', ((1, 'signatureId'),)))
    IXpsSigningOptions.GetSignatureMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(5, 'GetSignatureMethod', ((1, 'signatureMethod'),)))
    IXpsSigningOptions.SetSignatureMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(6, 'SetSignatureMethod', ((1, 'signatureMethod'),)))
    IXpsSigningOptions.GetDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Foundation.PWSTR))(7, 'GetDigestMethod', ((1, 'digestMethod'),)))
    IXpsSigningOptions.SetDigestMethod = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Foundation.PWSTR)(8, 'SetDigestMethod', ((1, 'digestMethod'),)))
    IXpsSigningOptions.GetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcPartUri_head))(9, 'GetSignaturePartName', ((1, 'signaturePartName'),)))
    IXpsSigningOptions.SetSignaturePartName = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.IOpcPartUri_head)(10, 'SetSignaturePartName', ((1, 'signaturePartName'),)))
    IXpsSigningOptions.GetPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIGN_POLICY))(11, 'GetPolicy', ((1, 'policy'),)))
    IXpsSigningOptions.SetPolicy = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_SIGN_POLICY)(12, 'SetPolicy', ((1, 'policy'),)))
    IXpsSigningOptions.GetSigningTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT))(13, 'GetSigningTimeFormat', ((1, 'timeFormat'),)))
    IXpsSigningOptions.SetSigningTimeFormat = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Packaging.Opc.OPC_SIGNATURE_TIME_FORMAT)(14, 'SetSigningTimeFormat', ((1, 'timeFormat'),)))
    IXpsSigningOptions.GetCustomObjects = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureCustomObjectSet_head))(15, 'GetCustomObjects', ((1, 'customObjectSet'),)))
    IXpsSigningOptions.GetCustomReferences = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcSignatureReferenceSet_head))(16, 'GetCustomReferences', ((1, 'customReferenceSet'),)))
    IXpsSigningOptions.GetCertificateSet = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Packaging.Opc.IOpcCertificateSet_head))(17, 'GetCertificateSet', ((1, 'certificateSet'),)))
    IXpsSigningOptions.GetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,POINTER(win32more.Storage.Xps.XPS_SIGN_FLAGS))(18, 'GetFlags', ((1, 'flags'),)))
    IXpsSigningOptions.SetFlags = COMMETHOD(WINFUNCTYPE(win32more.Foundation.HRESULT,win32more.Storage.Xps.XPS_SIGN_FLAGS)(19, 'SetFlags', ((1, 'flags'),)))
    win32more.System.Com.IUnknown
    return IXpsSigningOptions
PRINT_WINDOW_FLAGS = UInt32
PW_CLIENTONLY = 1
def _define_PSFEATURE_CUSTPAPER_head():
    class PSFEATURE_CUSTPAPER(Structure):
        pass
    return PSFEATURE_CUSTPAPER
def _define_PSFEATURE_CUSTPAPER():
    PSFEATURE_CUSTPAPER = win32more.Storage.Xps.PSFEATURE_CUSTPAPER_head
    PSFEATURE_CUSTPAPER._fields_ = [
        ('lOrientation', Int32),
        ('lWidth', Int32),
        ('lHeight', Int32),
        ('lWidthOffset', Int32),
        ('lHeightOffset', Int32),
    ]
    return PSFEATURE_CUSTPAPER
def _define_PSFEATURE_OUTPUT_head():
    class PSFEATURE_OUTPUT(Structure):
        pass
    return PSFEATURE_OUTPUT
def _define_PSFEATURE_OUTPUT():
    PSFEATURE_OUTPUT = win32more.Storage.Xps.PSFEATURE_OUTPUT_head
    PSFEATURE_OUTPUT._fields_ = [
        ('bPageIndependent', win32more.Foundation.BOOL),
        ('bSetPageDevice', win32more.Foundation.BOOL),
    ]
    return PSFEATURE_OUTPUT
PSINJECT_POINT = UInt16
PSINJECT_BEGINSTREAM = 1
PSINJECT_PSADOBE = 2
PSINJECT_PAGESATEND = 3
PSINJECT_PAGES = 4
PSINJECT_DOCNEEDEDRES = 5
PSINJECT_DOCSUPPLIEDRES = 6
PSINJECT_PAGEORDER = 7
PSINJECT_ORIENTATION = 8
PSINJECT_BOUNDINGBOX = 9
PSINJECT_DOCUMENTPROCESSCOLORS = 10
PSINJECT_COMMENTS = 11
PSINJECT_BEGINDEFAULTS = 12
PSINJECT_ENDDEFAULTS = 13
PSINJECT_BEGINPROLOG = 14
PSINJECT_ENDPROLOG = 15
PSINJECT_BEGINSETUP = 16
PSINJECT_ENDSETUP = 17
PSINJECT_TRAILER = 18
PSINJECT_EOF = 19
PSINJECT_ENDSTREAM = 20
PSINJECT_DOCUMENTPROCESSCOLORSATEND = 21
PSINJECT_PAGENUMBER = 100
PSINJECT_BEGINPAGESETUP = 101
PSINJECT_ENDPAGESETUP = 102
PSINJECT_PAGETRAILER = 103
PSINJECT_PLATECOLOR = 104
PSINJECT_SHOWPAGE = 105
PSINJECT_PAGEBBOX = 106
PSINJECT_ENDPAGECOMMENTS = 107
PSINJECT_VMSAVE = 200
PSINJECT_VMRESTORE = 201
def _define_PSINJECTDATA_head():
    class PSINJECTDATA(Structure):
        pass
    return PSINJECTDATA
def _define_PSINJECTDATA():
    PSINJECTDATA = win32more.Storage.Xps.PSINJECTDATA_head
    PSINJECTDATA._fields_ = [
        ('DataBytes', UInt32),
        ('InjectionPoint', win32more.Storage.Xps.PSINJECT_POINT),
        ('PageNumber', UInt16),
    ]
    return PSINJECTDATA
def _define_XPS_COLOR_head():
    class XPS_COLOR(Structure):
        pass
    return XPS_COLOR
def _define_XPS_COLOR():
    XPS_COLOR = win32more.Storage.Xps.XPS_COLOR_head
    class XPS_COLOR_XPS_COLOR_VALUE(Union):
        pass
    class XPS_COLOR_XPS_COLOR_VALUE__sRGB_e__Struct(Structure):
        pass
    XPS_COLOR_XPS_COLOR_VALUE__sRGB_e__Struct._fields_ = [
        ('alpha', Byte),
        ('red', Byte),
        ('green', Byte),
        ('blue', Byte),
    ]
    class XPS_COLOR_XPS_COLOR_VALUE__scRGB_e__Struct(Structure):
        pass
    XPS_COLOR_XPS_COLOR_VALUE__scRGB_e__Struct._fields_ = [
        ('alpha', Single),
        ('red', Single),
        ('green', Single),
        ('blue', Single),
    ]
    class XPS_COLOR_XPS_COLOR_VALUE__context_e__Struct(Structure):
        pass
    XPS_COLOR_XPS_COLOR_VALUE__context_e__Struct._fields_ = [
        ('channelCount', Byte),
        ('channels', Single * 9),
    ]
    XPS_COLOR_XPS_COLOR_VALUE._fields_ = [
        ('sRGB', XPS_COLOR_XPS_COLOR_VALUE__sRGB_e__Struct),
        ('scRGB', XPS_COLOR_XPS_COLOR_VALUE__scRGB_e__Struct),
        ('context', XPS_COLOR_XPS_COLOR_VALUE__context_e__Struct),
    ]
    XPS_COLOR._fields_ = [
        ('colorType', win32more.Storage.Xps.XPS_COLOR_TYPE),
        ('value', XPS_COLOR_XPS_COLOR_VALUE),
    ]
    return XPS_COLOR
XPS_COLOR_INTERPOLATION = Int32
XPS_COLOR_INTERPOLATION_SCRGBLINEAR = 1
XPS_COLOR_INTERPOLATION_SRGBLINEAR = 2
XPS_COLOR_TYPE = Int32
XPS_COLOR_TYPE_SRGB = 1
XPS_COLOR_TYPE_SCRGB = 2
XPS_COLOR_TYPE_CONTEXT = 3
def _define_XPS_DASH_head():
    class XPS_DASH(Structure):
        pass
    return XPS_DASH
def _define_XPS_DASH():
    XPS_DASH = win32more.Storage.Xps.XPS_DASH_head
    XPS_DASH._fields_ = [
        ('length', Single),
        ('gap', Single),
    ]
    return XPS_DASH
XPS_DASH_CAP = Int32
XPS_DASH_CAP_FLAT = 1
XPS_DASH_CAP_ROUND = 2
XPS_DASH_CAP_SQUARE = 3
XPS_DASH_CAP_TRIANGLE = 4
XPS_DOCUMENT_TYPE = Int32
XPS_DOCUMENT_TYPE_UNSPECIFIED = 1
XPS_DOCUMENT_TYPE_XPS = 2
XPS_DOCUMENT_TYPE_OPENXPS = 3
XPS_FILL_RULE = Int32
XPS_FILL_RULE_EVENODD = 1
XPS_FILL_RULE_NONZERO = 2
XPS_FONT_EMBEDDING = Int32
XPS_FONT_EMBEDDING_NORMAL = 1
XPS_FONT_EMBEDDING_OBFUSCATED = 2
XPS_FONT_EMBEDDING_RESTRICTED = 3
XPS_FONT_EMBEDDING_RESTRICTED_UNOBFUSCATED = 4
def _define_XPS_GLYPH_INDEX_head():
    class XPS_GLYPH_INDEX(Structure):
        pass
    return XPS_GLYPH_INDEX
def _define_XPS_GLYPH_INDEX():
    XPS_GLYPH_INDEX = win32more.Storage.Xps.XPS_GLYPH_INDEX_head
    XPS_GLYPH_INDEX._fields_ = [
        ('index', Int32),
        ('advanceWidth', Single),
        ('horizontalOffset', Single),
        ('verticalOffset', Single),
    ]
    return XPS_GLYPH_INDEX
def _define_XPS_GLYPH_MAPPING_head():
    class XPS_GLYPH_MAPPING(Structure):
        pass
    return XPS_GLYPH_MAPPING
def _define_XPS_GLYPH_MAPPING():
    XPS_GLYPH_MAPPING = win32more.Storage.Xps.XPS_GLYPH_MAPPING_head
    XPS_GLYPH_MAPPING._fields_ = [
        ('unicodeStringStart', UInt32),
        ('unicodeStringLength', UInt16),
        ('glyphIndicesStart', UInt32),
        ('glyphIndicesLength', UInt16),
    ]
    return XPS_GLYPH_MAPPING
XPS_IMAGE_TYPE = Int32
XPS_IMAGE_TYPE_JPEG = 1
XPS_IMAGE_TYPE_PNG = 2
XPS_IMAGE_TYPE_TIFF = 3
XPS_IMAGE_TYPE_WDP = 4
XPS_IMAGE_TYPE_JXR = 5
XPS_INTERLEAVING = Int32
XPS_INTERLEAVING_OFF = 1
XPS_INTERLEAVING_ON = 2
XPS_LINE_CAP = Int32
XPS_LINE_CAP_FLAT = 1
XPS_LINE_CAP_ROUND = 2
XPS_LINE_CAP_SQUARE = 3
XPS_LINE_CAP_TRIANGLE = 4
XPS_LINE_JOIN = Int32
XPS_LINE_JOIN_MITER = 1
XPS_LINE_JOIN_BEVEL = 2
XPS_LINE_JOIN_ROUND = 3
def _define_XPS_MATRIX_head():
    class XPS_MATRIX(Structure):
        pass
    return XPS_MATRIX
def _define_XPS_MATRIX():
    XPS_MATRIX = win32more.Storage.Xps.XPS_MATRIX_head
    XPS_MATRIX._fields_ = [
        ('m11', Single),
        ('m12', Single),
        ('m21', Single),
        ('m22', Single),
        ('m31', Single),
        ('m32', Single),
    ]
    return XPS_MATRIX
XPS_OBJECT_TYPE = Int32
XPS_OBJECT_TYPE_CANVAS = 1
XPS_OBJECT_TYPE_GLYPHS = 2
XPS_OBJECT_TYPE_PATH = 3
XPS_OBJECT_TYPE_MATRIX_TRANSFORM = 4
XPS_OBJECT_TYPE_GEOMETRY = 5
XPS_OBJECT_TYPE_SOLID_COLOR_BRUSH = 6
XPS_OBJECT_TYPE_IMAGE_BRUSH = 7
XPS_OBJECT_TYPE_LINEAR_GRADIENT_BRUSH = 8
XPS_OBJECT_TYPE_RADIAL_GRADIENT_BRUSH = 9
XPS_OBJECT_TYPE_VISUAL_BRUSH = 10
def _define_XPS_POINT_head():
    class XPS_POINT(Structure):
        pass
    return XPS_POINT
def _define_XPS_POINT():
    XPS_POINT = win32more.Storage.Xps.XPS_POINT_head
    XPS_POINT._fields_ = [
        ('x', Single),
        ('y', Single),
    ]
    return XPS_POINT
def _define_XPS_RECT_head():
    class XPS_RECT(Structure):
        pass
    return XPS_RECT
def _define_XPS_RECT():
    XPS_RECT = win32more.Storage.Xps.XPS_RECT_head
    XPS_RECT._fields_ = [
        ('x', Single),
        ('y', Single),
        ('width', Single),
        ('height', Single),
    ]
    return XPS_RECT
XPS_SEGMENT_STROKE_PATTERN = Int32
XPS_SEGMENT_STROKE_PATTERN_ALL = 1
XPS_SEGMENT_STROKE_PATTERN_NONE = 2
XPS_SEGMENT_STROKE_PATTERN_MIXED = 3
XPS_SEGMENT_TYPE = Int32
XPS_SEGMENT_TYPE_ARC_LARGE_CLOCKWISE = 1
XPS_SEGMENT_TYPE_ARC_LARGE_COUNTERCLOCKWISE = 2
XPS_SEGMENT_TYPE_ARC_SMALL_CLOCKWISE = 3
XPS_SEGMENT_TYPE_ARC_SMALL_COUNTERCLOCKWISE = 4
XPS_SEGMENT_TYPE_BEZIER = 5
XPS_SEGMENT_TYPE_LINE = 6
XPS_SEGMENT_TYPE_QUADRATIC_BEZIER = 7
XPS_SIGN_FLAGS = Int32
XPS_SIGN_FLAGS_NONE = 0
XPS_SIGN_FLAGS_IGNORE_MARKUP_COMPATIBILITY = 1
XPS_SIGN_POLICY = Int32
XPS_SIGN_POLICY_NONE = 0
XPS_SIGN_POLICY_CORE_PROPERTIES = 1
XPS_SIGN_POLICY_SIGNATURE_RELATIONSHIPS = 2
XPS_SIGN_POLICY_PRINT_TICKET = 4
XPS_SIGN_POLICY_DISCARD_CONTROL = 8
XPS_SIGN_POLICY_ALL = 15
XPS_SIGNATURE_STATUS = Int32
XPS_SIGNATURE_STATUS_INCOMPLIANT = 1
XPS_SIGNATURE_STATUS_INCOMPLETE = 2
XPS_SIGNATURE_STATUS_BROKEN = 3
XPS_SIGNATURE_STATUS_QUESTIONABLE = 4
XPS_SIGNATURE_STATUS_VALID = 5
def _define_XPS_SIZE_head():
    class XPS_SIZE(Structure):
        pass
    return XPS_SIZE
def _define_XPS_SIZE():
    XPS_SIZE = win32more.Storage.Xps.XPS_SIZE_head
    XPS_SIZE._fields_ = [
        ('width', Single),
        ('height', Single),
    ]
    return XPS_SIZE
XPS_SPREAD_METHOD = Int32
XPS_SPREAD_METHOD_PAD = 1
XPS_SPREAD_METHOD_REFLECT = 2
XPS_SPREAD_METHOD_REPEAT = 3
XPS_STYLE_SIMULATION = Int32
XPS_STYLE_SIMULATION_NONE = 1
XPS_STYLE_SIMULATION_ITALIC = 2
XPS_STYLE_SIMULATION_BOLD = 3
XPS_STYLE_SIMULATION_BOLDITALIC = 4
XPS_THUMBNAIL_SIZE = Int32
XPS_THUMBNAIL_SIZE_VERYSMALL = 1
XPS_THUMBNAIL_SIZE_SMALL = 2
XPS_THUMBNAIL_SIZE_MEDIUM = 3
XPS_THUMBNAIL_SIZE_LARGE = 4
XPS_TILE_MODE = Int32
XPS_TILE_MODE_NONE = 1
XPS_TILE_MODE_TILE = 2
XPS_TILE_MODE_FLIPX = 3
XPS_TILE_MODE_FLIPY = 4
XPS_TILE_MODE_FLIPXY = 5
XpsOMObjectFactory = Guid('e974d26d-3d9b-4d47-88-cc-38-72-f2-dc-35-85')
XpsOMThumbnailGenerator = Guid('7e4a23e2-b969-4761-be-35-1a-8c-ed-58-e3-23')
XpsSignatureManager = Guid('b0c43320-2315-44a2-b7-0a-09-43-a1-40-a8-ee')
__all__ = [
    "ABORTPROC",
    "AbortDoc",
    "DC_BINNAMES",
    "DC_BINS",
    "DC_COLLATE",
    "DC_COLORDEVICE",
    "DC_COPIES",
    "DC_DRIVER",
    "DC_DUPLEX",
    "DC_ENUMRESOLUTIONS",
    "DC_EXTRA",
    "DC_FIELDS",
    "DC_FILEDEPENDENCIES",
    "DC_MAXEXTENT",
    "DC_MEDIAREADY",
    "DC_MEDIATYPENAMES",
    "DC_MEDIATYPES",
    "DC_MINEXTENT",
    "DC_NUP",
    "DC_ORIENTATION",
    "DC_PAPERNAMES",
    "DC_PAPERS",
    "DC_PAPERSIZE",
    "DC_PERSONALITY",
    "DC_PRINTERMEM",
    "DC_PRINTRATE",
    "DC_PRINTRATEPPM",
    "DC_PRINTRATEUNIT",
    "DC_SIZE",
    "DC_STAPLE",
    "DC_TRUETYPE",
    "DC_VERSION",
    "DEVICE_CAPABILITIES",
    "DOCINFOA",
    "DOCINFOW",
    "DRAWPATRECT",
    "DeviceCapabilitiesA",
    "DeviceCapabilitiesW",
    "EndDoc",
    "EndPage",
    "Escape",
    "ExtEscape",
    "HPTPROVIDER",
    "IXpsDocumentPackageTarget",
    "IXpsDocumentPackageTarget3D",
    "IXpsOMBrush",
    "IXpsOMCanvas",
    "IXpsOMColorProfileResource",
    "IXpsOMColorProfileResourceCollection",
    "IXpsOMCoreProperties",
    "IXpsOMDashCollection",
    "IXpsOMDictionary",
    "IXpsOMDocument",
    "IXpsOMDocumentCollection",
    "IXpsOMDocumentSequence",
    "IXpsOMDocumentStructureResource",
    "IXpsOMFontResource",
    "IXpsOMFontResourceCollection",
    "IXpsOMGeometry",
    "IXpsOMGeometryFigure",
    "IXpsOMGeometryFigureCollection",
    "IXpsOMGlyphs",
    "IXpsOMGlyphsEditor",
    "IXpsOMGradientBrush",
    "IXpsOMGradientStop",
    "IXpsOMGradientStopCollection",
    "IXpsOMImageBrush",
    "IXpsOMImageResource",
    "IXpsOMImageResourceCollection",
    "IXpsOMLinearGradientBrush",
    "IXpsOMMatrixTransform",
    "IXpsOMNameCollection",
    "IXpsOMObjectFactory",
    "IXpsOMObjectFactory1",
    "IXpsOMPackage",
    "IXpsOMPackage1",
    "IXpsOMPackageTarget",
    "IXpsOMPackageWriter",
    "IXpsOMPackageWriter3D",
    "IXpsOMPage",
    "IXpsOMPage1",
    "IXpsOMPageReference",
    "IXpsOMPageReferenceCollection",
    "IXpsOMPart",
    "IXpsOMPartResources",
    "IXpsOMPartUriCollection",
    "IXpsOMPath",
    "IXpsOMPrintTicketResource",
    "IXpsOMRadialGradientBrush",
    "IXpsOMRemoteDictionaryResource",
    "IXpsOMRemoteDictionaryResource1",
    "IXpsOMRemoteDictionaryResourceCollection",
    "IXpsOMResource",
    "IXpsOMShareable",
    "IXpsOMSignatureBlockResource",
    "IXpsOMSignatureBlockResourceCollection",
    "IXpsOMSolidColorBrush",
    "IXpsOMStoryFragmentsResource",
    "IXpsOMThumbnailGenerator",
    "IXpsOMTileBrush",
    "IXpsOMVisual",
    "IXpsOMVisualBrush",
    "IXpsOMVisualCollection",
    "IXpsSignature",
    "IXpsSignatureBlock",
    "IXpsSignatureBlockCollection",
    "IXpsSignatureCollection",
    "IXpsSignatureManager",
    "IXpsSignatureRequest",
    "IXpsSignatureRequestCollection",
    "IXpsSigningOptions",
    "PRINT_WINDOW_FLAGS",
    "PSFEATURE_CUSTPAPER",
    "PSFEATURE_OUTPUT",
    "PSINJECTDATA",
    "PSINJECT_BEGINDEFAULTS",
    "PSINJECT_BEGINPAGESETUP",
    "PSINJECT_BEGINPROLOG",
    "PSINJECT_BEGINSETUP",
    "PSINJECT_BEGINSTREAM",
    "PSINJECT_BOUNDINGBOX",
    "PSINJECT_COMMENTS",
    "PSINJECT_DOCNEEDEDRES",
    "PSINJECT_DOCSUPPLIEDRES",
    "PSINJECT_DOCUMENTPROCESSCOLORS",
    "PSINJECT_DOCUMENTPROCESSCOLORSATEND",
    "PSINJECT_ENDDEFAULTS",
    "PSINJECT_ENDPAGECOMMENTS",
    "PSINJECT_ENDPAGESETUP",
    "PSINJECT_ENDPROLOG",
    "PSINJECT_ENDSETUP",
    "PSINJECT_ENDSTREAM",
    "PSINJECT_EOF",
    "PSINJECT_ORIENTATION",
    "PSINJECT_PAGEBBOX",
    "PSINJECT_PAGENUMBER",
    "PSINJECT_PAGEORDER",
    "PSINJECT_PAGES",
    "PSINJECT_PAGESATEND",
    "PSINJECT_PAGETRAILER",
    "PSINJECT_PLATECOLOR",
    "PSINJECT_POINT",
    "PSINJECT_PSADOBE",
    "PSINJECT_SHOWPAGE",
    "PSINJECT_TRAILER",
    "PSINJECT_VMRESTORE",
    "PSINJECT_VMSAVE",
    "PW_CLIENTONLY",
    "PrintWindow",
    "SetAbortProc",
    "StartDocA",
    "StartDocW",
    "StartPage",
    "XPS_COLOR",
    "XPS_COLOR_INTERPOLATION",
    "XPS_COLOR_INTERPOLATION_SCRGBLINEAR",
    "XPS_COLOR_INTERPOLATION_SRGBLINEAR",
    "XPS_COLOR_TYPE",
    "XPS_COLOR_TYPE_CONTEXT",
    "XPS_COLOR_TYPE_SCRGB",
    "XPS_COLOR_TYPE_SRGB",
    "XPS_DASH",
    "XPS_DASH_CAP",
    "XPS_DASH_CAP_FLAT",
    "XPS_DASH_CAP_ROUND",
    "XPS_DASH_CAP_SQUARE",
    "XPS_DASH_CAP_TRIANGLE",
    "XPS_DOCUMENT_TYPE",
    "XPS_DOCUMENT_TYPE_OPENXPS",
    "XPS_DOCUMENT_TYPE_UNSPECIFIED",
    "XPS_DOCUMENT_TYPE_XPS",
    "XPS_E_ABSOLUTE_REFERENCE",
    "XPS_E_ALREADY_OWNED",
    "XPS_E_BLEED_BOX_PAGE_DIMENSIONS_NOT_IN_SYNC",
    "XPS_E_BOTH_PATHFIGURE_AND_ABBR_SYNTAX_PRESENT",
    "XPS_E_BOTH_RESOURCE_AND_SOURCEATTR_PRESENT",
    "XPS_E_CARET_OUTSIDE_STRING",
    "XPS_E_CARET_OUT_OF_ORDER",
    "XPS_E_COLOR_COMPONENT_OUT_OF_RANGE",
    "XPS_E_DICTIONARY_ITEM_NAMED",
    "XPS_E_DUPLICATE_NAMES",
    "XPS_E_DUPLICATE_RESOURCE_KEYS",
    "XPS_E_INDEX_OUT_OF_RANGE",
    "XPS_E_INVALID_BLEED_BOX",
    "XPS_E_INVALID_CONTENT_BOX",
    "XPS_E_INVALID_CONTENT_TYPE",
    "XPS_E_INVALID_FLOAT",
    "XPS_E_INVALID_FONT_URI",
    "XPS_E_INVALID_LANGUAGE",
    "XPS_E_INVALID_LOOKUP_TYPE",
    "XPS_E_INVALID_MARKUP",
    "XPS_E_INVALID_NAME",
    "XPS_E_INVALID_NUMBER_OF_COLOR_CHANNELS",
    "XPS_E_INVALID_NUMBER_OF_POINTS_IN_CURVE_SEGMENTS",
    "XPS_E_INVALID_OBFUSCATED_FONT_URI",
    "XPS_E_INVALID_PAGE_SIZE",
    "XPS_E_INVALID_RESOURCE_KEY",
    "XPS_E_INVALID_SIGNATUREBLOCK_MARKUP",
    "XPS_E_INVALID_THUMBNAIL_IMAGE_TYPE",
    "XPS_E_INVALID_XML_ENCODING",
    "XPS_E_MAPPING_OUTSIDE_INDICES",
    "XPS_E_MAPPING_OUTSIDE_STRING",
    "XPS_E_MAPPING_OUT_OF_ORDER",
    "XPS_E_MARKUP_COMPATIBILITY_ELEMENTS",
    "XPS_E_MISSING_COLORPROFILE",
    "XPS_E_MISSING_DISCARDCONTROL",
    "XPS_E_MISSING_DOCUMENT",
    "XPS_E_MISSING_DOCUMENTSEQUENCE_RELATIONSHIP",
    "XPS_E_MISSING_FONTURI",
    "XPS_E_MISSING_GLYPHS",
    "XPS_E_MISSING_IMAGE_IN_IMAGEBRUSH",
    "XPS_E_MISSING_LOOKUP",
    "XPS_E_MISSING_NAME",
    "XPS_E_MISSING_PAGE_IN_DOCUMENT",
    "XPS_E_MISSING_PAGE_IN_PAGEREFERENCE",
    "XPS_E_MISSING_PART_REFERENCE",
    "XPS_E_MISSING_PART_STREAM",
    "XPS_E_MISSING_REFERRED_DOCUMENT",
    "XPS_E_MISSING_REFERRED_PAGE",
    "XPS_E_MISSING_RELATIONSHIP_TARGET",
    "XPS_E_MISSING_RESOURCE_KEY",
    "XPS_E_MISSING_RESOURCE_RELATIONSHIP",
    "XPS_E_MISSING_RESTRICTED_FONT_RELATIONSHIP",
    "XPS_E_MISSING_SEGMENT_DATA",
    "XPS_E_MULTIPLE_DOCUMENTSEQUENCE_RELATIONSHIPS",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENT",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_DOCUMENTSEQUENCE",
    "XPS_E_MULTIPLE_PRINTTICKETS_ON_PAGE",
    "XPS_E_MULTIPLE_REFERENCES_TO_PART",
    "XPS_E_MULTIPLE_RESOURCES",
    "XPS_E_MULTIPLE_THUMBNAILS_ON_PACKAGE",
    "XPS_E_MULTIPLE_THUMBNAILS_ON_PAGE",
    "XPS_E_NEGATIVE_FLOAT",
    "XPS_E_NESTED_REMOTE_DICTIONARY",
    "XPS_E_NOT_ENOUGH_GRADIENT_STOPS",
    "XPS_E_NO_CUSTOM_OBJECTS",
    "XPS_E_OBJECT_DETACHED",
    "XPS_E_ODD_BIDILEVEL",
    "XPS_E_ONE_TO_ONE_MAPPING_EXPECTED",
    "XPS_E_PACKAGE_ALREADY_OPENED",
    "XPS_E_PACKAGE_NOT_OPENED",
    "XPS_E_PACKAGE_WRITER_NOT_CLOSED",
    "XPS_E_RELATIONSHIP_EXTERNAL",
    "XPS_E_RESOURCE_NOT_OWNED",
    "XPS_E_RESTRICTED_FONT_NOT_OBFUSCATED",
    "XPS_E_SIGNATUREID_DUP",
    "XPS_E_SIGREQUESTID_DUP",
    "XPS_E_STRING_TOO_LONG",
    "XPS_E_TOO_MANY_INDICES",
    "XPS_E_UNAVAILABLE_PACKAGE",
    "XPS_E_UNEXPECTED_COLORPROFILE",
    "XPS_E_UNEXPECTED_CONTENT_TYPE",
    "XPS_E_UNEXPECTED_RELATIONSHIP_TYPE",
    "XPS_E_UNEXPECTED_RESTRICTED_FONT_RELATIONSHIP",
    "XPS_E_VISUAL_CIRCULAR_REF",
    "XPS_E_XKEY_ATTR_PRESENT_OUTSIDE_RES_DICT",
    "XPS_FILL_RULE",
    "XPS_FILL_RULE_EVENODD",
    "XPS_FILL_RULE_NONZERO",
    "XPS_FONT_EMBEDDING",
    "XPS_FONT_EMBEDDING_NORMAL",
    "XPS_FONT_EMBEDDING_OBFUSCATED",
    "XPS_FONT_EMBEDDING_RESTRICTED",
    "XPS_FONT_EMBEDDING_RESTRICTED_UNOBFUSCATED",
    "XPS_GLYPH_INDEX",
    "XPS_GLYPH_MAPPING",
    "XPS_IMAGE_TYPE",
    "XPS_IMAGE_TYPE_JPEG",
    "XPS_IMAGE_TYPE_JXR",
    "XPS_IMAGE_TYPE_PNG",
    "XPS_IMAGE_TYPE_TIFF",
    "XPS_IMAGE_TYPE_WDP",
    "XPS_INTERLEAVING",
    "XPS_INTERLEAVING_OFF",
    "XPS_INTERLEAVING_ON",
    "XPS_LINE_CAP",
    "XPS_LINE_CAP_FLAT",
    "XPS_LINE_CAP_ROUND",
    "XPS_LINE_CAP_SQUARE",
    "XPS_LINE_CAP_TRIANGLE",
    "XPS_LINE_JOIN",
    "XPS_LINE_JOIN_BEVEL",
    "XPS_LINE_JOIN_MITER",
    "XPS_LINE_JOIN_ROUND",
    "XPS_MATRIX",
    "XPS_OBJECT_TYPE",
    "XPS_OBJECT_TYPE_CANVAS",
    "XPS_OBJECT_TYPE_GEOMETRY",
    "XPS_OBJECT_TYPE_GLYPHS",
    "XPS_OBJECT_TYPE_IMAGE_BRUSH",
    "XPS_OBJECT_TYPE_LINEAR_GRADIENT_BRUSH",
    "XPS_OBJECT_TYPE_MATRIX_TRANSFORM",
    "XPS_OBJECT_TYPE_PATH",
    "XPS_OBJECT_TYPE_RADIAL_GRADIENT_BRUSH",
    "XPS_OBJECT_TYPE_SOLID_COLOR_BRUSH",
    "XPS_OBJECT_TYPE_VISUAL_BRUSH",
    "XPS_POINT",
    "XPS_RECT",
    "XPS_SEGMENT_STROKE_PATTERN",
    "XPS_SEGMENT_STROKE_PATTERN_ALL",
    "XPS_SEGMENT_STROKE_PATTERN_MIXED",
    "XPS_SEGMENT_STROKE_PATTERN_NONE",
    "XPS_SEGMENT_TYPE",
    "XPS_SEGMENT_TYPE_ARC_LARGE_CLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_LARGE_COUNTERCLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_SMALL_CLOCKWISE",
    "XPS_SEGMENT_TYPE_ARC_SMALL_COUNTERCLOCKWISE",
    "XPS_SEGMENT_TYPE_BEZIER",
    "XPS_SEGMENT_TYPE_LINE",
    "XPS_SEGMENT_TYPE_QUADRATIC_BEZIER",
    "XPS_SIGNATURE_STATUS",
    "XPS_SIGNATURE_STATUS_BROKEN",
    "XPS_SIGNATURE_STATUS_INCOMPLETE",
    "XPS_SIGNATURE_STATUS_INCOMPLIANT",
    "XPS_SIGNATURE_STATUS_QUESTIONABLE",
    "XPS_SIGNATURE_STATUS_VALID",
    "XPS_SIGN_FLAGS",
    "XPS_SIGN_FLAGS_IGNORE_MARKUP_COMPATIBILITY",
    "XPS_SIGN_FLAGS_NONE",
    "XPS_SIGN_POLICY",
    "XPS_SIGN_POLICY_ALL",
    "XPS_SIGN_POLICY_CORE_PROPERTIES",
    "XPS_SIGN_POLICY_DISCARD_CONTROL",
    "XPS_SIGN_POLICY_NONE",
    "XPS_SIGN_POLICY_PRINT_TICKET",
    "XPS_SIGN_POLICY_SIGNATURE_RELATIONSHIPS",
    "XPS_SIZE",
    "XPS_SPREAD_METHOD",
    "XPS_SPREAD_METHOD_PAD",
    "XPS_SPREAD_METHOD_REFLECT",
    "XPS_SPREAD_METHOD_REPEAT",
    "XPS_STYLE_SIMULATION",
    "XPS_STYLE_SIMULATION_BOLD",
    "XPS_STYLE_SIMULATION_BOLDITALIC",
    "XPS_STYLE_SIMULATION_ITALIC",
    "XPS_STYLE_SIMULATION_NONE",
    "XPS_THUMBNAIL_SIZE",
    "XPS_THUMBNAIL_SIZE_LARGE",
    "XPS_THUMBNAIL_SIZE_MEDIUM",
    "XPS_THUMBNAIL_SIZE_SMALL",
    "XPS_THUMBNAIL_SIZE_VERYSMALL",
    "XPS_TILE_MODE",
    "XPS_TILE_MODE_FLIPX",
    "XPS_TILE_MODE_FLIPXY",
    "XPS_TILE_MODE_FLIPY",
    "XPS_TILE_MODE_NONE",
    "XPS_TILE_MODE_TILE",
    "XpsOMObjectFactory",
    "XpsOMThumbnailGenerator",
    "XpsSignatureManager",
]
