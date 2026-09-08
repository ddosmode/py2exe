Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
# -*- кодировка: utf-8 -*-
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""

import pefile

def decode_bytes_to_string(name):
    try:
        r = name.decode('utf-8')
    except AttributeError:
        r = name
    return r

def find_loaded_dlls(path):

    dllset = set()

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    pe = pefile.PE(path, fast_load=True)
    pe.parse_data_directories(directories=[
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT'],
        pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_EXPORT'],
        ],
        forwarded_exports_only=True,
        import_dllnames_only=True,
        )

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    try:
        imports = pe.DIRECTORY_ENTRY_IMPORT
    except AttributeError:
        imports = []

    for entry in imports:
        dll_str = decode_bytes_to_string(entry.dll)
        dllset.add(dll_str)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    try:
        exports = pe.DIRECTORY_ENTRY_EXPORT
    except AttributeError:
        exports = None

    if exports is not None:
        for symbol in exports.symbols:
            if symbol.forwarder is not None:
                forwarder_str = decode_bytes_to_string(symbol.forwarder)
                basename = forwarder_str.split('.')[0]
                dllname = basename + ".dll"
                dllset.add(dllname)

    pe.close()

    return dllset
