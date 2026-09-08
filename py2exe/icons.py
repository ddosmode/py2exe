Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
# -*- кодировка: utf-8 -*-
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
import itertools

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
from . import _wapi

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
class ICONDIRENTRY(_wapi.Structure):
    _pack_ = 2
    _fields_ = [("bWidth", _wapi.BYTE),
                ("bHeight", _wapi.BYTE),
                ("bColorCount", _wapi.BYTE),
                ("bReserved", _wapi.BYTE),
                ("wPlanes", _wapi.WORD),
                ("wBitCount", _wapi.WORD),
                ("dwBytesInRes", _wapi.DWORD),
                ("dwImageOffset", _wapi.DWORD)]


Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
class ICONDIRHEADER(_wapi.Structure):
    _pack_ = 2
    _fields_ = [("idReserved", _wapi.WORD), Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
                ("idType", _wapi.WORD), Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
                ("idCount", _wapi.WORD), Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
                ]

    @classmethod
    def readfrom(cls, fileobj):
        header = cls()
        fileobj.readinto(header)
        header.idEntries = []
        for i in range(header.idCount):
            entry = ICONDIRENTRY()
            fileobj.readinto(entry)
            header.idEntries.append(entry)

        header.iconimages = []
        for entry in header.idEntries:
            fileobj.seek(entry.dwImageOffset)
            image = fileobj.read(entry.dwBytesInRes)
            header.iconimages.append(image)
        return header

################################################################

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

class GRPICONDIRENTRY(_wapi.Structure):
    _pack_ = 2
    _fields_ = [("bWidth", _wapi.BYTE),
                ("bHeight", _wapi.BYTE),
                ("bColorCount", _wapi.BYTE),
                ("bReserved", _wapi.BYTE),
                ("wPlanes", _wapi.WORD),
                ("wBitCount", _wapi.WORD),
                ("dwBytesInRes", _wapi.DWORD),
                Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
                ("nID", _wapi.WORD)]


def CreateGrpIconDirHeader(iconheader, id_generator):
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    class GRPICONDIRHEADER(_wapi.Structure):
        _pack_ = 2
        _fields_ = [("idReserved", _wapi.WORD),
                    ("idType", _wapi.WORD),
                    ("idCount", _wapi.WORD),
                    ("idEntries", GRPICONDIRENTRY * iconheader.idCount)]
        def tobytes(self):
            return memoryview(self).tobytes()
    grpheader = GRPICONDIRHEADER(
        idReserved = iconheader.idReserved,
        idType = iconheader.idType,
        idCount = iconheader.idCount)
    for i in range(iconheader.idCount):
        dst = grpheader.idEntries[i]
        src = iconheader.idEntries[i]
        dst.bWidth = src.bWidth
        dst.bHeight = src.bHeight
        dst.bColorCount = src.bColorCount
        dst.bReserved = src.bReserved
        dst.wPlanes = src.wPlanes
        dst.wBitCount = src.wBitCount
        dst.dwBytesInRes = src.dwBytesInRes
        dst.nID = next(id_generator)
        if dst.nID > 32767:
            raise ValueError("Invalid resource id %s" % dst.nID)
    return grpheader

################################################################

def BuildIcons(icon_resources):
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
    result = []

    id_generator = itertools.count(10)

    for resource_id, iconpath in icon_resources:
        with open(iconpath, "rb") as iconfile:
            header = ICONDIRHEADER.readfrom(iconfile)

        grp_header = CreateGrpIconDirHeader(header, id_generator)

        for i, entry in enumerate(grp_header.idEntries):
            Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            result.append((_wapi.RT_ICON, entry.nID, header.iconimages[i]))

        result.append((_wapi.RT_GROUP_ICON, resource_id, grp_header.tobytes()))

    return result

################################################################

if __name__ == "__main__":
    with open("128.ico", "rb") as ifi:
        hdr = ICONDIRHEADER.readfrom(ifi)

        print(hdr.iconimages)

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        print(hdr.idType, hdr.idCount)

        for entry in hdr.idEntries:
            print("ENTRY", entry.bWidth, entry.bHeight, entry.bColorCount,
                  entry.wPlanes, entry.wBitCount,
                  entry.dwBytesInRes,
                  entry.dwImageOffset)

            ifi.seek(entry.dwImageOffset)
            iconimage = ifi.read(entry.dwBytesInRes)
            assert len(iconimage) == entry.dwBytesInRes

        print(ifi.tell())

"""
    /* Each RT_ICON resource in an image file (containing the icon for one
       specific resolution and number of colors) must have a unique id, and
       the id must be in the GRPICONDIRHEADER's nID member.

       So, we use a *static* variable rt_icon_id which is incremented for each
       RT_ICON resource and written into the GRPICONDIRHEADER's nID member.

       XXX Do we need a way to reset the rt_icon_id variable to zero?  If we
       are building a lot of images in one setup script? 
    */
    for (i = 0; i < pidh->idCount; ++i) {
	    pgidh->idEntries[i].nID = rt_icon_id++;
    }
"""
"""
    if (!pfn_UpdateResource(hUpdate,
			    (Py_UNICODE *)MAKEINTRESOURCE(RT_GROUP_ICON),
			    (Py_UNICODE *)MAKEINTRESOURCE(icoid),
			    MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL),
			    pgidh,
			    gidh_size)) {
	SystemError(GetLastError(), "UpdateResource");
	goto failed;
    }
    for (i = 0; i < pidh->idCount; ++i) {
        char *cp = &icodata[pidh->idEntries[i].dwImageOffset];
        int cBytes = pidh->idEntries[i].dwBytesInRes;
        if (!pfn_UpdateResource(hUpdate,
				(Py_UNICODE *)MAKEINTRESOURCE(RT_ICON),
				(Py_UNICODE *)MAKEINTRESOURCE(pgidh->idEntries[i].nID),
				MAKELANGID(LANG_NEUTRAL, SUBLANG_NEUTRAL),
				cp,
				cBytes)) {
            SystemError(GetLastError(), "UpdateResource");
            goto failed;
        }
    }
"""
