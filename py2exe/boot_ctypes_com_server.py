Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

import sys
import _ctypes

if 1:
    ################################################################
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    import ctypes
    class LOGGER:
        def __init__(self):
            self.softspace = None
        def write(self, text):
            if isinstance(text, str):
                ctypes.windll.kernel32.OutputDebugStringW(text)
            else:
                ctypes.windll.kernel32.OutputDebugStringA(text)
    sys.stderr = sys.stdout = LOGGER()
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

################################################################
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

if not hasattr(sys, "frozen"):
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    sys.frozen = _ctypes.frozen = 1
else:
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    _ctypes.frozen = sys.frozen

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#...

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
try:
    com_module_names
except NameError:
    print("This script is designed to be run from inside py2exe % s" % str(details))
    sys.exit(1)

com_modules = []
for name in com_module_names:
    __import__(name)
    com_modules.append(sys.modules[name])

def get_classes(module):
    return [ob
            for ob in module.__dict__.values()
            if hasattr(ob, "_reg_progid_") and ob._reg_progid_ is not None
            ]

def build_class_map():
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    #
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    classmap = {}
    for mod in com_modules:
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        for cls in get_classes(mod):
            classmap[cls._reg_clsid_] = cls
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    import comtypes.server.inprocserver
    comtypes.server.inprocserver._clsid_to_class = classmap
build_class_map()
del build_class_map

def DllRegisterServer():
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    from comtypes.server.register import register
    for mod in com_modules:
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        for cls in get_classes(mod):
            register(cls)


def DllUnregisterServer():
    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    from comtypes.server.register import unregister
    for mod in com_modules:
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        for cls in get_classes(mod):
            unregister(cls)
