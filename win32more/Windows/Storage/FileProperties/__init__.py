from __future__ import annotations
from ctypes import c_void_p, POINTER, CFUNCTYPE, WINFUNCTYPE, cdll, windll
import sys
from typing import Generic, TypeVar
if sys.version_info < (3, 9):
    from typing_extensions import Annotated
else:
    from typing import Annotated
K = TypeVar('K')
T = TypeVar('T')
V = TypeVar('V')
TProgress = TypeVar('TProgress')
TResult = TypeVar('TResult')
TSender = TypeVar('TSender')
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, press, make_head, EasyCastStructure, EasyCastUnion, ComPtr
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.Devices.Geolocation
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
import win32more.Windows.Storage
import win32more.Windows.Storage.FileProperties
import win32more.Windows.Storage.Streams
import sys
_module = sys.modules[__name__]
def __getattr__(name):
    try:
        prototype = globals()[f'{name}_head']
    except KeyError:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'") from None
    setattr(_module, name, press(prototype))
    return getattr(_module, name)
class BasicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IBasicProperties
    _classid_ = 'Windows.Storage.FileProperties.BasicProperties'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.FileProperties.IBasicProperties) -> UInt64: ...
    @winrt_mixinmethod
    def get_DateModified(self: win32more.Windows.Storage.FileProperties.IBasicProperties) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def get_ItemDate(self: win32more.Windows.Storage.FileProperties.IBasicProperties) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    Size = property(get_Size, None)
    DateModified = property(get_DateModified, None)
    ItemDate = property(get_ItemDate, None)
class DocumentProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IDocumentProperties
    _classid_ = 'Windows.Storage.FileProperties.DocumentProperties'
    @winrt_mixinmethod
    def get_Author(self: win32more.Windows.Storage.FileProperties.IDocumentProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.FileProperties.IDocumentProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.FileProperties.IDocumentProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Keywords(self: win32more.Windows.Storage.FileProperties.IDocumentProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Comment(self: win32more.Windows.Storage.FileProperties.IDocumentProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Comment(self: win32more.Windows.Storage.FileProperties.IDocumentProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    Author = property(get_Author, None)
    Title = property(get_Title, put_Title)
    Keywords = property(get_Keywords, None)
    Comment = property(get_Comment, put_Comment)
class GeotagHelper(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.GeotagHelper'
    @winrt_classmethod
    def GetGeotagAsync(cls: win32more.Windows.Storage.FileProperties.IGeotagHelperStatics, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geopoint]: ...
    @winrt_classmethod
    def SetGeotagFromGeolocatorAsync(cls: win32more.Windows.Storage.FileProperties.IGeotagHelperStatics, file: win32more.Windows.Storage.IStorageFile, geolocator: win32more.Windows.Devices.Geolocation.Geolocator) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_classmethod
    def SetGeotagAsync(cls: win32more.Windows.Storage.FileProperties.IGeotagHelperStatics, file: win32more.Windows.Storage.IStorageFile, geopoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncAction: ...
class IBasicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IBasicProperties'
    _iid_ = Guid('{d05d55db-785e-4a66-be02-9beec58aea81}')
    @winrt_commethod(6)
    def get_Size(self) -> UInt64: ...
    @winrt_commethod(7)
    def get_DateModified(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(8)
    def get_ItemDate(self) -> win32more.Windows.Foundation.DateTime: ...
    Size = property(get_Size, None)
    DateModified = property(get_DateModified, None)
    ItemDate = property(get_ItemDate, None)
class IDocumentProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IDocumentProperties'
    _iid_ = Guid('{7eab19bc-1821-4923-b4a9-0aea404d0070}')
    @winrt_commethod(6)
    def get_Author(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(7)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(8)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(9)
    def get_Keywords(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(10)
    def get_Comment(self) -> WinRT_String: ...
    @winrt_commethod(11)
    def put_Comment(self, value: WinRT_String) -> Void: ...
    Author = property(get_Author, None)
    Title = property(get_Title, put_Title)
    Keywords = property(get_Keywords, None)
    Comment = property(get_Comment, put_Comment)
class IGeotagHelperStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IGeotagHelperStatics'
    _iid_ = Guid('{41493244-2524-4655-86a6-ed16f5fc716b}')
    @winrt_commethod(6)
    def GetGeotagAsync(self, file: win32more.Windows.Storage.IStorageFile) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Devices.Geolocation.Geopoint]: ...
    @winrt_commethod(7)
    def SetGeotagFromGeolocatorAsync(self, file: win32more.Windows.Storage.IStorageFile, geolocator: win32more.Windows.Devices.Geolocation.Geolocator) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SetGeotagAsync(self, file: win32more.Windows.Storage.IStorageFile, geopoint: win32more.Windows.Devices.Geolocation.Geopoint) -> win32more.Windows.Foundation.IAsyncAction: ...
class IImageProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IImageProperties'
    _iid_ = Guid('{523c9424-fcff-4275-afee-ecdb9ab47973}')
    @winrt_commethod(6)
    def get_Rating(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_Rating(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_Keywords(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_DateTaken(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(10)
    def put_DateTaken(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(11)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(12)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(13)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Latitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(16)
    def get_Longitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(17)
    def get_CameraManufacturer(self) -> WinRT_String: ...
    @winrt_commethod(18)
    def put_CameraManufacturer(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(19)
    def get_CameraModel(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_CameraModel(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_Orientation(self) -> win32more.Windows.Storage.FileProperties.PhotoOrientation: ...
    @winrt_commethod(22)
    def get_PeopleNames(self) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    Rating = property(get_Rating, put_Rating)
    Keywords = property(get_Keywords, None)
    DateTaken = property(get_DateTaken, put_DateTaken)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Title = property(get_Title, put_Title)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    CameraManufacturer = property(get_CameraManufacturer, put_CameraManufacturer)
    CameraModel = property(get_CameraModel, put_CameraModel)
    Orientation = property(get_Orientation, None)
    PeopleNames = property(get_PeopleNames, None)
class IMusicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IMusicProperties'
    _iid_ = Guid('{bc8aab62-66ec-419a-bc5d-ca65a4cb46da}')
    @winrt_commethod(6)
    def get_Album(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def put_Album(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(8)
    def get_Artist(self) -> WinRT_String: ...
    @winrt_commethod(9)
    def put_Artist(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(10)
    def get_Genre(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(11)
    def get_TrackNumber(self) -> UInt32: ...
    @winrt_commethod(12)
    def put_TrackNumber(self, value: UInt32) -> Void: ...
    @winrt_commethod(13)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(14)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(15)
    def get_Rating(self) -> UInt32: ...
    @winrt_commethod(16)
    def put_Rating(self, value: UInt32) -> Void: ...
    @winrt_commethod(17)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(18)
    def get_Bitrate(self) -> UInt32: ...
    @winrt_commethod(19)
    def get_AlbumArtist(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_AlbumArtist(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_Composers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(22)
    def get_Conductors(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(23)
    def get_Subtitle(self) -> WinRT_String: ...
    @winrt_commethod(24)
    def put_Subtitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(25)
    def get_Producers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(26)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(27)
    def put_Publisher(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(28)
    def get_Writers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(29)
    def get_Year(self) -> UInt32: ...
    @winrt_commethod(30)
    def put_Year(self, value: UInt32) -> Void: ...
    Album = property(get_Album, put_Album)
    Artist = property(get_Artist, put_Artist)
    Genre = property(get_Genre, None)
    TrackNumber = property(get_TrackNumber, put_TrackNumber)
    Title = property(get_Title, put_Title)
    Rating = property(get_Rating, put_Rating)
    Duration = property(get_Duration, None)
    Bitrate = property(get_Bitrate, None)
    AlbumArtist = property(get_AlbumArtist, put_AlbumArtist)
    Composers = property(get_Composers, None)
    Conductors = property(get_Conductors, None)
    Subtitle = property(get_Subtitle, put_Subtitle)
    Producers = property(get_Producers, None)
    Publisher = property(get_Publisher, put_Publisher)
    Writers = property(get_Writers, None)
    Year = property(get_Year, put_Year)
class IStorageItemContentProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IStorageItemContentProperties'
    _iid_ = Guid('{05294bad-bc38-48bf-85d7-770e0e2ae0ba}')
    @winrt_commethod(6)
    def GetMusicPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.MusicProperties]: ...
    @winrt_commethod(7)
    def GetVideoPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.VideoProperties]: ...
    @winrt_commethod(8)
    def GetImagePropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.ImageProperties]: ...
    @winrt_commethod(9)
    def GetDocumentPropertiesAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.DocumentProperties]: ...
class IStorageItemExtraProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IStorageItemExtraProperties'
    _iid_ = Guid('{c54361b2-54cd-432b-bdbc-4b19c4b470d7}')
    @winrt_commethod(6)
    def RetrievePropertiesAsync(self, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_commethod(7)
    def SavePropertiesAsync(self, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(8)
    def SavePropertiesAsyncOverloadDefault(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class IThumbnailProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IThumbnailProperties'
    _iid_ = Guid('{693dd42f-dbe7-49b5-b3b3-2893ac5d3423}')
    @winrt_commethod(6)
    def get_OriginalWidth(self) -> UInt32: ...
    @winrt_commethod(7)
    def get_OriginalHeight(self) -> UInt32: ...
    @winrt_commethod(8)
    def get_ReturnedSmallerCachedSize(self) -> Boolean: ...
    @winrt_commethod(9)
    def get_Type(self) -> win32more.Windows.Storage.FileProperties.ThumbnailType: ...
    OriginalWidth = property(get_OriginalWidth, None)
    OriginalHeight = property(get_OriginalHeight, None)
    ReturnedSmallerCachedSize = property(get_ReturnedSmallerCachedSize, None)
    Type = property(get_Type, None)
class IVideoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.Storage.FileProperties.IVideoProperties'
    _iid_ = Guid('{719ae507-68de-4db8-97de-49998c059f2f}')
    @winrt_commethod(6)
    def get_Rating(self) -> UInt32: ...
    @winrt_commethod(7)
    def put_Rating(self, value: UInt32) -> Void: ...
    @winrt_commethod(8)
    def get_Keywords(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(9)
    def get_Width(self) -> UInt32: ...
    @winrt_commethod(10)
    def get_Height(self) -> UInt32: ...
    @winrt_commethod(11)
    def get_Duration(self) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_commethod(12)
    def get_Latitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(13)
    def get_Longitude(self) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_commethod(14)
    def get_Title(self) -> WinRT_String: ...
    @winrt_commethod(15)
    def put_Title(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(16)
    def get_Subtitle(self) -> WinRT_String: ...
    @winrt_commethod(17)
    def put_Subtitle(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(18)
    def get_Producers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(19)
    def get_Publisher(self) -> WinRT_String: ...
    @winrt_commethod(20)
    def put_Publisher(self, value: WinRT_String) -> Void: ...
    @winrt_commethod(21)
    def get_Writers(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(22)
    def get_Year(self) -> UInt32: ...
    @winrt_commethod(23)
    def put_Year(self, value: UInt32) -> Void: ...
    @winrt_commethod(24)
    def get_Bitrate(self) -> UInt32: ...
    @winrt_commethod(25)
    def get_Directors(self) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_commethod(26)
    def get_Orientation(self) -> win32more.Windows.Storage.FileProperties.VideoOrientation: ...
    Rating = property(get_Rating, put_Rating)
    Keywords = property(get_Keywords, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Duration = property(get_Duration, None)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Title = property(get_Title, put_Title)
    Subtitle = property(get_Subtitle, put_Subtitle)
    Producers = property(get_Producers, None)
    Publisher = property(get_Publisher, put_Publisher)
    Writers = property(get_Writers, None)
    Year = property(get_Year, put_Year)
    Bitrate = property(get_Bitrate, None)
    Directors = property(get_Directors, None)
    Orientation = property(get_Orientation, None)
class ImageProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IImageProperties
    _classid_ = 'Windows.Storage.FileProperties.ImageProperties'
    @winrt_mixinmethod
    def get_Rating(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Rating(self: win32more.Windows.Storage.FileProperties.IImageProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Keywords(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_DateTaken(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_DateTaken(self: win32more.Windows.Storage.FileProperties.IImageProperties, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.FileProperties.IImageProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Latitude(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Longitude(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_CameraManufacturer(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CameraManufacturer(self: win32more.Windows.Storage.FileProperties.IImageProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_CameraModel(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_CameraModel(self: win32more.Windows.Storage.FileProperties.IImageProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Storage.FileProperties.PhotoOrientation: ...
    @winrt_mixinmethod
    def get_PeopleNames(self: win32more.Windows.Storage.FileProperties.IImageProperties) -> win32more.Windows.Foundation.Collections.IVectorView[WinRT_String]: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    Rating = property(get_Rating, put_Rating)
    Keywords = property(get_Keywords, None)
    DateTaken = property(get_DateTaken, put_DateTaken)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Title = property(get_Title, put_Title)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    CameraManufacturer = property(get_CameraManufacturer, put_CameraManufacturer)
    CameraModel = property(get_CameraModel, put_CameraModel)
    Orientation = property(get_Orientation, None)
    PeopleNames = property(get_PeopleNames, None)
class MusicProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IMusicProperties
    _classid_ = 'Windows.Storage.FileProperties.MusicProperties'
    @winrt_mixinmethod
    def get_Album(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Album(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Artist(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Artist(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Genre(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_TrackNumber(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_TrackNumber(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Rating(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Rating(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Bitrate(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_AlbumArtist(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_AlbumArtist(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Composers(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Conductors(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Subtitle(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtitle(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Producers(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Publisher(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Writers(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Year(self: win32more.Windows.Storage.FileProperties.IMusicProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Year(self: win32more.Windows.Storage.FileProperties.IMusicProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    Album = property(get_Album, put_Album)
    Artist = property(get_Artist, put_Artist)
    Genre = property(get_Genre, None)
    TrackNumber = property(get_TrackNumber, put_TrackNumber)
    Title = property(get_Title, put_Title)
    Rating = property(get_Rating, put_Rating)
    Duration = property(get_Duration, None)
    Bitrate = property(get_Bitrate, None)
    AlbumArtist = property(get_AlbumArtist, put_AlbumArtist)
    Composers = property(get_Composers, None)
    Conductors = property(get_Conductors, None)
    Subtitle = property(get_Subtitle, put_Subtitle)
    Producers = property(get_Producers, None)
    Publisher = property(get_Publisher, put_Publisher)
    Writers = property(get_Writers, None)
    Year = property(get_Year, put_Year)
PhotoOrientation = Int32
PhotoOrientation_Unspecified: PhotoOrientation = 0
PhotoOrientation_Normal: PhotoOrientation = 1
PhotoOrientation_FlipHorizontal: PhotoOrientation = 2
PhotoOrientation_Rotate180: PhotoOrientation = 3
PhotoOrientation_FlipVertical: PhotoOrientation = 4
PhotoOrientation_Transpose: PhotoOrientation = 5
PhotoOrientation_Rotate270: PhotoOrientation = 6
PhotoOrientation_Transverse: PhotoOrientation = 7
PhotoOrientation_Rotate90: PhotoOrientation = 8
PropertyPrefetchOptions = UInt32
PropertyPrefetchOptions_None: PropertyPrefetchOptions = 0
PropertyPrefetchOptions_MusicProperties: PropertyPrefetchOptions = 1
PropertyPrefetchOptions_VideoProperties: PropertyPrefetchOptions = 2
PropertyPrefetchOptions_ImageProperties: PropertyPrefetchOptions = 4
PropertyPrefetchOptions_DocumentProperties: PropertyPrefetchOptions = 8
PropertyPrefetchOptions_BasicProperties: PropertyPrefetchOptions = 16
class StorageItemContentProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IStorageItemContentProperties
    _classid_ = 'Windows.Storage.FileProperties.StorageItemContentProperties'
    @winrt_mixinmethod
    def GetMusicPropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemContentProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.MusicProperties]: ...
    @winrt_mixinmethod
    def GetVideoPropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemContentProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.VideoProperties]: ...
    @winrt_mixinmethod
    def GetImagePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemContentProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.ImageProperties]: ...
    @winrt_mixinmethod
    def GetDocumentPropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemContentProperties) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Storage.FileProperties.DocumentProperties]: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
class StorageItemThumbnail(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.Streams.IRandomAccessStreamWithContentType
    _classid_ = 'Windows.Storage.FileProperties.StorageItemThumbnail'
    @winrt_mixinmethod
    def get_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def put_Size(self: win32more.Windows.Storage.Streams.IRandomAccessStream, value: UInt64) -> Void: ...
    @winrt_mixinmethod
    def GetInputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IInputStream: ...
    @winrt_mixinmethod
    def GetOutputStreamAt(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> win32more.Windows.Storage.Streams.IOutputStream: ...
    @winrt_mixinmethod
    def get_Position(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> UInt64: ...
    @winrt_mixinmethod
    def Seek(self: win32more.Windows.Storage.Streams.IRandomAccessStream, position: UInt64) -> Void: ...
    @winrt_mixinmethod
    def CloneStream(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> win32more.Windows.Storage.Streams.IRandomAccessStream: ...
    @winrt_mixinmethod
    def get_CanRead(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def get_CanWrite(self: win32more.Windows.Storage.Streams.IRandomAccessStream) -> Boolean: ...
    @winrt_mixinmethod
    def Close(self: win32more.Windows.Foundation.IClosable) -> Void: ...
    @winrt_mixinmethod
    def ReadAsync(self: win32more.Windows.Storage.Streams.IInputStream, buffer: win32more.Windows.Storage.Streams.IBuffer, count: UInt32, options: win32more.Windows.Storage.Streams.InputStreamOptions) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[win32more.Windows.Storage.Streams.IBuffer, UInt32]: ...
    @winrt_mixinmethod
    def WriteAsync(self: win32more.Windows.Storage.Streams.IOutputStream, buffer: win32more.Windows.Storage.Streams.IBuffer) -> win32more.Windows.Foundation.IAsyncOperationWithProgress[UInt32, UInt32]: ...
    @winrt_mixinmethod
    def FlushAsync(self: win32more.Windows.Storage.Streams.IOutputStream) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_mixinmethod
    def get_ContentType(self: win32more.Windows.Storage.Streams.IContentTypeProvider) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_OriginalWidth(self: win32more.Windows.Storage.FileProperties.IThumbnailProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_OriginalHeight(self: win32more.Windows.Storage.FileProperties.IThumbnailProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_ReturnedSmallerCachedSize(self: win32more.Windows.Storage.FileProperties.IThumbnailProperties) -> Boolean: ...
    @winrt_mixinmethod
    def get_Type(self: win32more.Windows.Storage.FileProperties.IThumbnailProperties) -> win32more.Windows.Storage.FileProperties.ThumbnailType: ...
    Size = property(get_Size, put_Size)
    Position = property(get_Position, None)
    CanRead = property(get_CanRead, None)
    CanWrite = property(get_CanWrite, None)
    ContentType = property(get_ContentType, None)
    OriginalWidth = property(get_OriginalWidth, None)
    OriginalHeight = property(get_OriginalHeight, None)
    ReturnedSmallerCachedSize = property(get_ReturnedSmallerCachedSize, None)
    Type = property(get_Type, None)
ThumbnailMode = Int32
ThumbnailMode_PicturesView: ThumbnailMode = 0
ThumbnailMode_VideosView: ThumbnailMode = 1
ThumbnailMode_MusicView: ThumbnailMode = 2
ThumbnailMode_DocumentsView: ThumbnailMode = 3
ThumbnailMode_ListView: ThumbnailMode = 4
ThumbnailMode_SingleItem: ThumbnailMode = 5
ThumbnailOptions = UInt32
ThumbnailOptions_None: ThumbnailOptions = 0
ThumbnailOptions_ReturnOnlyIfCached: ThumbnailOptions = 1
ThumbnailOptions_ResizeThumbnail: ThumbnailOptions = 2
ThumbnailOptions_UseCurrentScale: ThumbnailOptions = 4
ThumbnailType = Int32
ThumbnailType_Image: ThumbnailType = 0
ThumbnailType_Icon: ThumbnailType = 1
VideoOrientation = Int32
VideoOrientation_Normal: VideoOrientation = 0
VideoOrientation_Rotate90: VideoOrientation = 90
VideoOrientation_Rotate180: VideoOrientation = 180
VideoOrientation_Rotate270: VideoOrientation = 270
class VideoProperties(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.Storage.FileProperties.IVideoProperties
    _classid_ = 'Windows.Storage.FileProperties.VideoProperties'
    @winrt_mixinmethod
    def get_Rating(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Rating(self: win32more.Windows.Storage.FileProperties.IVideoProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Keywords(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Width(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Height(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Duration(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.TimeSpan: ...
    @winrt_mixinmethod
    def get_Latitude(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Longitude(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.IReference[Double]: ...
    @winrt_mixinmethod
    def get_Title(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Title(self: win32more.Windows.Storage.FileProperties.IVideoProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Subtitle(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Subtitle(self: win32more.Windows.Storage.FileProperties.IVideoProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Producers(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Publisher(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> WinRT_String: ...
    @winrt_mixinmethod
    def put_Publisher(self: win32more.Windows.Storage.FileProperties.IVideoProperties, value: WinRT_String) -> Void: ...
    @winrt_mixinmethod
    def get_Writers(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Year(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> UInt32: ...
    @winrt_mixinmethod
    def put_Year(self: win32more.Windows.Storage.FileProperties.IVideoProperties, value: UInt32) -> Void: ...
    @winrt_mixinmethod
    def get_Bitrate(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> UInt32: ...
    @winrt_mixinmethod
    def get_Directors(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Foundation.Collections.IVector[WinRT_String]: ...
    @winrt_mixinmethod
    def get_Orientation(self: win32more.Windows.Storage.FileProperties.IVideoProperties) -> win32more.Windows.Storage.FileProperties.VideoOrientation: ...
    @winrt_mixinmethod
    def RetrievePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToRetrieve: win32more.Windows.Foundation.Collections.IIterable[WinRT_String]) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.Foundation.Collections.IMap[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]: ...
    @winrt_mixinmethod
    def SavePropertiesAsync(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties, propertiesToSave: win32more.Windows.Foundation.Collections.IIterable[win32more.Windows.Foundation.Collections.IKeyValuePair[WinRT_String, win32more.Windows.Win32.System.WinRT.IInspectable_head]]) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def SavePropertiesAsyncOverloadDefault(self: win32more.Windows.Storage.FileProperties.IStorageItemExtraProperties) -> win32more.Windows.Foundation.IAsyncAction: ...
    Rating = property(get_Rating, put_Rating)
    Keywords = property(get_Keywords, None)
    Width = property(get_Width, None)
    Height = property(get_Height, None)
    Duration = property(get_Duration, None)
    Latitude = property(get_Latitude, None)
    Longitude = property(get_Longitude, None)
    Title = property(get_Title, put_Title)
    Subtitle = property(get_Subtitle, put_Subtitle)
    Producers = property(get_Producers, None)
    Publisher = property(get_Publisher, put_Publisher)
    Writers = property(get_Writers, None)
    Year = property(get_Year, put_Year)
    Bitrate = property(get_Bitrate, None)
    Directors = property(get_Directors, None)
    Orientation = property(get_Orientation, None)
make_head(_module, 'BasicProperties')
make_head(_module, 'DocumentProperties')
make_head(_module, 'GeotagHelper')
make_head(_module, 'IBasicProperties')
make_head(_module, 'IDocumentProperties')
make_head(_module, 'IGeotagHelperStatics')
make_head(_module, 'IImageProperties')
make_head(_module, 'IMusicProperties')
make_head(_module, 'IStorageItemContentProperties')
make_head(_module, 'IStorageItemExtraProperties')
make_head(_module, 'IThumbnailProperties')
make_head(_module, 'IVideoProperties')
make_head(_module, 'ImageProperties')
make_head(_module, 'MusicProperties')
make_head(_module, 'StorageItemContentProperties')
make_head(_module, 'StorageItemThumbnail')
make_head(_module, 'VideoProperties')