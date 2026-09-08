"""Некоторые функции API Windows, типы данных и константы."""
from ctypes import *

_kernel32 = WinDLL("kernel32")
_imagehlp = WinDLL("imagehlp")

def BOOL_errcheck(result, func, args):
    if result:
        return result
    raise WinError()

## если __debug__:
## из импорта ctypeslib.dynamic_module включает
## #0x0502: Windows XP SP2
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
##     включать("""\
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
## #define NO_STRICT
## #define WINVER 0x0502
## #define _WIN32_WINNT 0x0502
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
##     """,
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

WSTRING = c_wchar_p
STRING = c_char_p
UINT = c_uint
WCHAR = c_wchar
LPWSTR = WSTRING
GetWindowsDirectoryW = _kernel32.GetWindowsDirectoryW
GetWindowsDirectoryW.restype = UINT
GetWindowsDirectoryW.argtypes = [LPWSTR, UINT]
GetSystemDirectoryW = _kernel32.GetSystemDirectoryW
GetSystemDirectoryW.restype = UINT
GetSystemDirectoryW.argtypes = [LPWSTR, UINT]
DWORD = c_ulong
PVOID = c_void_p
HANDLE = PVOID
HINSTANCE = HANDLE
HMODULE = HINSTANCE
GetModuleFileNameW = _kernel32.GetModuleFileNameW
GetModuleFileNameW.restype = DWORD
GetModuleFileNameW.argtypes = [HMODULE, LPWSTR, DWORD]
BOOL = c_int

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
BindOutOfMemory = 0
BindRvaToVaFailed = 1
BindNoRoomInImage = 2
BindImportModuleFailed = 3
BindImportProcedureFailed = 4
BindImportModule = 5
BindImportProcedure = 6
BindForwarder = 7
BindForwarderNOT = 8
BindImageModified = 9
BindExpandFileHeaders = 10
BindImageComplete = 11
BindMismatchedSymbols = 12
BindSymbolsNotUpdated = 13
BindImportProcedure32 = 14
BindImportProcedure64 = 15
BindForwarder32 = 16
BindForwarder64 = 17
BindForwarderNOT32 = 18
BindForwarderNOT64 = 19
_IMAGEHLP_STATUS_REASON = c_int Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
CHAR = c_char
PIMAGEHLP_STATUS_ROUTINE = WINFUNCTYPE(BOOL, _IMAGEHLP_STATUS_REASON, STRING, STRING, c_ulong, c_ulong)
PSTR = STRING
BindImageEx = _imagehlp.BindImageEx
BindImageEx.restype = BOOL
BindImageEx.argtypes = [DWORD, PSTR, PSTR, PSTR, PIMAGEHLP_STATUS_ROUTINE]
BindImageEx.errcheck = BOOL_errcheck
BIND_ALL_IMAGES = 4 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
BIND_CACHE_IMPORT_DLLS = 8 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
BIND_NO_UPDATE = 2 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
LPCWSTR = WSTRING
SearchPathW = _kernel32.SearchPathW
SearchPathW.restype = DWORD
SearchPathW.argtypes = [LPCWSTR, LPCWSTR, LPCWSTR, DWORD, LPWSTR, POINTER(LPWSTR)]
BeginUpdateResourceW = _kernel32.BeginUpdateResourceW
BeginUpdateResourceW.restype = HANDLE
BeginUpdateResourceW.argtypes = [LPCWSTR, BOOL]
WORD = c_ushort
LPVOID = c_void_p
UpdateResourceW = _kernel32.UpdateResourceW
UpdateResourceW.restype = BOOL
UpdateResourceW.argtypes = [HANDLE, LPCWSTR, LPCWSTR, WORD, LPVOID, DWORD]
UpdateResourceW.errcheck = BOOL_errcheck
EndUpdateResourceW = _kernel32.EndUpdateResourceW
EndUpdateResourceW.restype = BOOL
EndUpdateResourceW.argtypes = [HANDLE, BOOL]
EndUpdateResourceW.errcheck = BOOL_errcheck
LPCSTR = STRING
UpdateResourceA = _kernel32.UpdateResourceA
UpdateResourceA.restype = BOOL
UpdateResourceA.argtypes = [HANDLE, LPCSTR, LPCSTR, WORD, LPVOID, DWORD]
UpdateResourceA.errcheck = BOOL_errcheck
RT_STRING = 6 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
RT_VERSION = 16 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
class tagVS_FIXEDFILEINFO(Structure):
    pass
VS_FIXEDFILEINFO = tagVS_FIXEDFILEINFO
tagVS_FIXEDFILEINFO._fields_ = [
    ('dwSignature', DWORD),
    ('dwStrucVersion', DWORD),
    ('dwFileVersionMS', DWORD),
    ('dwFileVersionLS', DWORD),
    ('dwProductVersionMS', DWORD),
    ('dwProductVersionLS', DWORD),
    ('dwFileFlagsMask', DWORD),
    ('dwFileFlags', DWORD),
    ('dwFileOS', DWORD),
    ('dwFileType', DWORD),
    ('dwFileSubtype', DWORD),
    ('dwFileDateMS', DWORD),
    ('dwFileDateLS', DWORD),
]
VFT_APP = 1 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
VOS_NT_WINDOWS32 = 262148 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
BYTE = c_ubyte
RT_ICON = 3 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
RT_GROUP_ICON = 14 Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
