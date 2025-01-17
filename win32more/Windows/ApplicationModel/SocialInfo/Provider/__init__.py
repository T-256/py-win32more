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
from win32more import ARCH, MissingType, c_char_p_no, c_wchar_p_no, Byte, SByte, Char, Int16, UInt16, Int32, UInt32, Int64, UInt64, IntPtr, UIntPtr, Single, Double, String, Boolean, Void, Guid, SUCCEEDED, FAILED, cfunctype, winfunctype, commethod, cfunctype_pointer, winfunctype_pointer, EasyCastStructure, EasyCastUnion, ComPtr, make_ready
from win32more._winrt import SZArray, WinRT_String, winrt_commethod, winrt_mixinmethod, winrt_classmethod, winrt_factorymethod, winrt_activatemethod, MulticastDelegate
import win32more.Windows.Win32.System.WinRT
import win32more.Windows.ApplicationModel.SocialInfo
import win32more.Windows.ApplicationModel.SocialInfo.Provider
import win32more.Windows.Foundation
import win32more.Windows.Foundation.Collections
class ISocialDashboardItemUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater'
    _iid_ = Guid('{3cde9dc9-4800-46cd-869b-1973ec685bde}')
    @winrt_commethod(6)
    def get_OwnerRemoteId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Content(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_commethod(8)
    def get_Timestamp(self) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_commethod(9)
    def put_Timestamp(self, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_commethod(10)
    def put_Thumbnail(self, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_commethod(11)
    def get_Thumbnail(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_commethod(12)
    def CommitAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_commethod(13)
    def get_TargetUri(self) -> win32more.Windows.Foundation.Uri: ...
    @winrt_commethod(14)
    def put_TargetUri(self, value: win32more.Windows.Foundation.Uri) -> Void: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TargetUri = property(get_TargetUri, put_TargetUri)
class ISocialFeedUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater'
    _iid_ = Guid('{7a0c0aa7-ed89-4bd5-a8d9-15f4d9861c10}')
    @winrt_commethod(6)
    def get_OwnerRemoteId(self) -> WinRT_String: ...
    @winrt_commethod(7)
    def get_Kind(self) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind: ...
    @winrt_commethod(8)
    def get_Items(self) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItem]: ...
    @winrt_commethod(9)
    def CommitAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Kind = property(get_Kind, None)
    Items = property(get_Items, None)
class ISocialInfoProviderManagerStatics(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics'
    _iid_ = Guid('{1b88e52b-7787-48d6-aa12-d8e8f47ab85a}')
    @winrt_commethod(6)
    def CreateSocialFeedUpdaterAsync(self, kind: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind, mode: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedUpdateMode, ownerRemoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater]: ...
    @winrt_commethod(7)
    def CreateDashboardItemUpdaterAsync(self, ownerRemoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater]: ...
    @winrt_commethod(8)
    def UpdateBadgeCountValue(self, itemRemoteId: WinRT_String, newCount: Int32) -> Void: ...
    @winrt_commethod(9)
    def ReportNewContentAvailable(self, contactRemoteId: WinRT_String, kind: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind) -> Void: ...
    @winrt_commethod(10)
    def ProvisionAsync(self) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_commethod(11)
    def DeprovisionAsync(self) -> win32more.Windows.Foundation.IAsyncAction: ...
class SocialDashboardItemUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater'
    @winrt_mixinmethod
    def get_OwnerRemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Content(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedContent: ...
    @winrt_mixinmethod
    def get_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> win32more.Windows.Foundation.DateTime: ...
    @winrt_mixinmethod
    def put_Timestamp(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: win32more.Windows.Foundation.DateTime) -> Void: ...
    @winrt_mixinmethod
    def put_Thumbnail(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail) -> Void: ...
    @winrt_mixinmethod
    def get_Thumbnail(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> win32more.Windows.ApplicationModel.SocialInfo.SocialItemThumbnail: ...
    @winrt_mixinmethod
    def CommitAsync(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> win32more.Windows.Foundation.IAsyncAction: ...
    @winrt_mixinmethod
    def get_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater) -> win32more.Windows.Foundation.Uri: ...
    @winrt_mixinmethod
    def put_TargetUri(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialDashboardItemUpdater, value: win32more.Windows.Foundation.Uri) -> Void: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Content = property(get_Content, None)
    Timestamp = property(get_Timestamp, put_Timestamp)
    Thumbnail = property(get_Thumbnail, put_Thumbnail)
    TargetUri = property(get_TargetUri, put_TargetUri)
class SocialFeedUpdater(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    default_interface: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater'
    @winrt_mixinmethod
    def get_OwnerRemoteId(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> WinRT_String: ...
    @winrt_mixinmethod
    def get_Kind(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind: ...
    @winrt_mixinmethod
    def get_Items(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> win32more.Windows.Foundation.Collections.IVector[win32more.Windows.ApplicationModel.SocialInfo.SocialFeedItem]: ...
    @winrt_mixinmethod
    def CommitAsync(self: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialFeedUpdater) -> win32more.Windows.Foundation.IAsyncAction: ...
    OwnerRemoteId = property(get_OwnerRemoteId, None)
    Kind = property(get_Kind, None)
    Items = property(get_Items, None)
class SocialInfoProviderManager(ComPtr):
    extends: win32more.Windows.Win32.System.WinRT.IInspectable
    _classid_ = 'Windows.ApplicationModel.SocialInfo.Provider.SocialInfoProviderManager'
    @winrt_classmethod
    def CreateSocialFeedUpdaterAsync(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, kind: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind, mode: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedUpdateMode, ownerRemoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.SocialInfo.Provider.SocialFeedUpdater]: ...
    @winrt_classmethod
    def CreateDashboardItemUpdaterAsync(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, ownerRemoteId: WinRT_String) -> win32more.Windows.Foundation.IAsyncOperation[win32more.Windows.ApplicationModel.SocialInfo.Provider.SocialDashboardItemUpdater]: ...
    @winrt_classmethod
    def UpdateBadgeCountValue(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, itemRemoteId: WinRT_String, newCount: Int32) -> Void: ...
    @winrt_classmethod
    def ReportNewContentAvailable(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics, contactRemoteId: WinRT_String, kind: win32more.Windows.ApplicationModel.SocialInfo.SocialFeedKind) -> Void: ...
    @winrt_classmethod
    def ProvisionAsync(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> win32more.Windows.Foundation.IAsyncOperation[Boolean]: ...
    @winrt_classmethod
    def DeprovisionAsync(cls: win32more.Windows.ApplicationModel.SocialInfo.Provider.ISocialInfoProviderManagerStatics) -> win32more.Windows.Foundation.IAsyncAction: ...
make_ready(__name__)
