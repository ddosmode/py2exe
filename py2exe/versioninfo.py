# -*- кодировка: латиница-1 -*-
##
## Copyright (c) 2000–2013 Томас Хеллер
##
## Разрешение настоящим предоставляется бесплатно любому лицу, получившему
## копию этого программного обеспечения и связанных с ним файлов документации (файл
## «Программное обеспечение»), чтобы иметь дело с Программным обеспечением без ограничений, включая
## без ограничений права на использование, копирование, изменение, объединение, публикацию,
## распространять, сублицензировать и/или продавать копии Программного обеспечения, а также
## разрешать лицам, которым предоставлено Программное обеспечение, делать это при условии, что
## следующие условия:
##
## Вышеупомянутое уведомление об авторских правах и настоящее уведомление о разрешении должны быть
## включен во все копии или существенные части Программного обеспечения.
##
## ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ,
## ЯВНЫЕ ИЛИ ПОДРАЗУМЕВАЕМЫЕ, ВКЛЮЧАЯ, НО НЕ ОГРАНИЧИВАЯСЬ, ГАРАНТИИ
## ТОРГОВАЯ ПРИГОДНОСТЬ, ПРИГОДНОСТЬ ДЛЯ ОПРЕДЕЛЕННОЙ ЦЕЛИ И
## НЕНАРУШЕНИЕ ПРАВ. НИ ПРИ КАКИХ ОБСТОЯТЕЛЬСТВАХ АВТОРЫ ИЛИ ОБЛАДАТЕЛИ АВТОРСКИХ ПРАВ НЕ ДОЛЖНЫ БЫТЬ
## ОТВЕТСТВЕННОСТЬ ЗА ЛЮБЫЕ ПРЕТЕНЗИИ, УБЫТКИ ИЛИ ДРУГУЮ ОТВЕТСТВЕННОСТЬ, КАК В ИСКАХ
## КОНТРАКТА, ПРАВИЛЬНОГО ПРАВОНАРУШЕНИЯ ИЛИ ДРУГОГО ПРОИСХОЖДЕНИЯ, ВЫТЕКАЮЩЕГО ИЗ, В СВЯЗИ ИЛИ В СВЯЗИ
## С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ ИЛИ ИСПОЛЬЗОВАНИЕМ ИЛИ ДРУГИМИ ДЕЛАМИ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.
##

import struct

VOS_NT_WINDOWS32 = 0x00040004
VFT_APP = 0x00000001

RT_VERSION = 16

class VersionError(Exception):
    pass

def w32_uc(text):
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
    return text.encode("utf-16-le")

class VS_FIXEDFILEINFO:
    dwSignature = 0xFEEF04BD
    dwStrucVersion = 0x00010000
    dwFileVersionMS = 0x00010000
    dwFileVersionLS = 0x00000001
    dwProductVersionMS = 0x00010000
    dwProductVersionLS = 0x00000001
    dwFileFlagsMask = 0x3F
    dwFileFlags = 0
    dwFileOS = VOS_NT_WINDOWS32
    dwFileType = VFT_APP
    dwFileSubtype = 0
    dwFileDateMS = 0
    dwFileDateLS = 0

    fmt = "13L"

    def __init__(self, version):
        version = version.replace(",", ".")
        fields = (version + '.0.0.0.0').split(".")[:4]
        fields = [f.strip() for f in fields]
        try:
            self.dwFileVersionMS = int(fields[0]) * 65536 + int(fields[1])
            self.dwFileVersionLS = int(fields[2]) * 65536 + int(fields[3])
        except ValueError:
            raise VersionError("could not parse version number '%s'" % version)

    def tobytes(self):
        return struct.pack(self.fmt,
                           self.dwSignature,
                           self.dwStrucVersion,
                           self.dwFileVersionMS,
                           self.dwFileVersionLS,
                           self.dwProductVersionMS,
                           self.dwProductVersionLS,
                           self.dwFileFlagsMask,
                           self.dwFileFlags,
                           self.dwFileOS,
                           self.dwFileType,
                           self.dwFileSubtype,
                           self.dwFileDateMS,
                           self.dwFileDateLS)

def align(data):
    pad = - len(data) % 4
    return data + b'\000' * pad

class VS_STRUCT:
    items = ()

    def tobytes(self):
        szKey = w32_uc(self.name)
        ulen = len(szKey)+2

        value = self.get_value()
        data = struct.pack("h%ss0i" % ulen, self.wType, szKey) + value

        data = align(data)

        for item in self.items:
            data = data + item.tobytes()

        wLength = len(data) + 4 # 4 байта для wLength и wValueLength
        wValueLength = len(value)

        return self.pack("hh", wLength, wValueLength, data)

    def pack(self, fmt, len, vlen, data):
        return struct.pack(fmt, len, vlen) + data

    def get_value(self):
        return b""


class String(VS_STRUCT):
    wType = 1
    items = ()

    def __init__(self, name_value):
        (name, value) = name_value
        self.name = name
        if value:
            self.value = value + '\000' # строки должны заканчиваться нулем
        else:
            self.value = value

    def pack(self, fmt, len, vlen, data):
        # ValueLength измеряется в СЛОВАХ, а не в БАЙТАХ!
        return struct.pack(fmt, len, vlen//2) + data

    def get_value(self):
        return w32_uc(self.value)


class StringTable(VS_STRUCT):
    wType = 1

    def __init__(self, name, strings):
        self.name = name
        self.items = map(String, strings)


class StringFileInfo(VS_STRUCT):
    wType = 1
    name = "StringFileInfo"

    def __init__(self, name, strings):
        self.items = [StringTable(name, strings)]

class Var(VS_STRUCT):
    # MSDN говорит:
    # Если вы используете структуру Var для перечисления языков,
    # поддержка приложений или DLL вместо использования нескольких версий
    # ресурсов, используйте элемент Value для хранения массива DWORD
    # значения, указывающие комбинации языка и кодовой страницы
    # поддерживается этим файлом. Младшее слово каждого DWORD должно
    # содержат идентификатор языка Microsoft и слово старшего порядка
    # должен содержать номер кодовой страницы IBM. Либо высшего порядка, либо
    # младшее слово может быть нулевым, что указывает на то, что файл является языковым
    # или независимо от кодовой страницы. Если структура Var опущена,
    # файл будет интерпретироваться как язык, так и кодовая страница
    # независимый.
    wType = 0
    name = "Translation"

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return struct.pack("l", self.value)

class VarFileInfo(VS_STRUCT):
    wType = 1
    name = "VarFileInfo"

    def __init__(self, *names):
        self.items = map(Var, names)

    def get_value(self):
        return b""

class VS_VERSIONINFO(VS_STRUCT):
    wType = 0 # 0: двоичные данные, 1: текстовые данные
    name = "VS_VERSION_INFO"

    def __init__(self, version, items):
        self.value = VS_FIXEDFILEINFO(version)
        self.items = items

    def get_value(self):
        return self.value.tobytes()

class Version(object):
    def __init__(self, version_info):
        version = version_info.version
        comments = version_info.comments
        company_name = version_info.company_name
        file_description = version_info.file_description
        internal_name = version_info.internal_name
        legal_copyright = version_info.legal_copyright
        legal_trademarks = version_info.legal_trademarks
        original_filename = version_info.original_filename
        private_build = version_info.private_build
        product_name = version_info.product_name
        product_version = version_info.product_version
        special_build = version_info.special_build

        self.version = version

        strings = []
        if comments is not None:
            strings.append(("Comments", comments))
        if company_name is not None:
            strings.append(("CompanyName", company_name))
        if file_description is not None:
            strings.append(("FileDescription", file_description))
        strings.append(("FileVersion", version))
        if internal_name is not None:
            strings.append(("InternalName", internal_name))
        if legal_copyright is not None:
            strings.append(("LegalCopyright", legal_copyright))
        if legal_trademarks is not None:
            strings.append(("LegalTrademarks", legal_trademarks))
        if original_filename is not None:
            strings.append(("OriginalFilename", original_filename))
        if private_build is not None:
            strings.append(("PrivateBuild", private_build))
        if product_name is not None:
            strings.append(("ProductName", product_name))
        strings.append(("ProductVersion", product_version or version))
        if special_build is not None:
            strings.append(("SpecialBuild", special_build))
        from . import __version__
        strings.append(("Creator", "py2exe %s" % __version__))
        self.strings = strings

    def resource_bytes(self):
        vs = VS_VERSIONINFO(self.version,
                            [StringFileInfo("040904B0",
                                            self.strings),
                             VarFileInfo(0x04B00409)])
        return vs.tobytes()

def test():
    import sys
    from argparse import Namespace
    sys.path.append("c:/tmp")
    version_info = Namespace(
                      version = "1, 0, 0, 1",
                      comments = "Ümläut comments",
                      company_name = "No Company",
                      file_description = "silly application",
                      internal_name = "silly",
                      legal_copyright = u"Copyright © 2003",
                      legal_trademarks = None,
                      original_filename = "silly.exe",
                      private_build = "test build",
                      product_name = "silly product",
                      product_version = None,
                      special_build = None,
                    )
    version = Version(version_info)
    print(version.resource_bytes())

if __name__ == '__main__':
    test()
