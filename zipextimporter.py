"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
import sys
import zipimport

from importlib import machinery
from importlib import util

# _memimporter is a module built into the py2exe runstubs.
import _memimporter

class ZipExtensionImporter(zipimport.zipimporter):
    _suffixes = machinery.EXTENSION_SUFFIXES

    def find_loader(self, fullname, path=None):
"""Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know."""
        loader, portions = super().find_loader(fullname, path)
        if loader is None:
            pathname = fullname.replace(".", "\\")
            for s in self._suffixes:
                if (pathname + s) in self._files:
                    return self, []
            return None, []
        return loader, portions

    def find_module(self, fullname, path=None):
        result = zipimport.zipimporter.find_module(self, fullname, path)
        if result:
            return result
        fullname = fullname.replace(".", "\\")
        for s in self._suffixes:
            if (fullname + s) in self._files:
                return self
        return None

    def find_spec(self, name, path=None):
        module = self.find_module(name, path)
        if module is not None:
            return util.spec_from_loader(name, module)
        else:
            return None

    def load_module(self, fullname):
        verbose = _memimporter.get_verbose_flag()

        if fullname in sys.modules:
            mod = sys.modules[fullname]
            if verbose:
                sys.stderr.write(
                    "import %s # previously loaded from zipfile %s\n"
                    % (fullname, self.archive))
            return mod
        try:
            return zipimport.zipimporter.load_module(self, fullname)
        except ImportError as err:
            if verbose:
                sys.stderr.write("error loading %s: %s\n"% (fullname, err))

            if sys.version_info >= (3, 0):
                # name of initfunction
                initname = "PyInit_" + fullname.split(".")[-1]
            else:
                # name of initfunction
                initname = "init" + fullname.split(".")[-1]
            filename = fullname.replace(".", "\\")
            if filename in ("pywintypes", "pythoncom"):
                filename = filename + "%d%d" % sys.version_info[:2]
                suffixes = ('.dll',)
            else:
                suffixes = self._suffixes
            for s in suffixes:
                path = filename + s
                if path in self._files:
                    if verbose > 1:
                        sys.stderr.write("# found %s in zipfile %s\n"
                                         % (path, self.archive))
                    spec = util.find_spec(fullname, path)
                    mod = _memimporter.import_module(fullname, path,
                                                     initname,
                                                     self.get_data, spec)
                    mod.__file__ = "%s\\%s" % (self.archive, path)
                    mod.__loader__ = self
                    mod.__memimported__ = True
                    sys.modules[fullname] = mod
                    if verbose:
                        sys.stderr.write("import %s # loaded from zipfile %s\n"
                                         % (fullname, mod.__file__))
                    return mod
            raise zipimport.ZipImportError("can't find module %s" % fullname) from err

    if sys.version_info >= (3, 10):
        def create_module(self, spec):
            mod =  super().create_module(spec)
            if mod is None:
                verbose = _memimporter.get_verbose_flag()
                fullname = spec.name

                filename = fullname.replace(".", "\\")
                suffixes = self._suffixes
                initname = "PyInit_" + fullname.split(".")[-1]

                for s in suffixes:
                    path = filename + s
                    if path in self._files:
                        if verbose > 1:
                            sys.stderr.write("# found %s in zipfile %s\n"
                                            % (path, self.archive))
                        mod = _memimporter.import_module(fullname, path,
                                                        initname,
                                                        self.get_data, spec)
                        mod.__file__ = "%s\\%s" % (self.archive, path)
                        mod.__loader__ = self
                        mod.__memimported__ = True
                        if verbose:
                            sys.stderr.write("import %s # loaded from zipfile %s\n"
                                            % (fullname, mod.__file__))
                        return mod
                # raise zipimport.ZipImportError("can't find module %s" % fullname)

    if sys.version_info >= (3, 10):
        def exec_module(self, module):
            if hasattr(module, '__memimported__'):
                pass
            else:
                super().exec_module(module)

    def __repr__(self):
        return "<%s object %r>" % (self.__class__.__name__, self.archive)

def install():
    "Install the zipextimporter"
    sys.path_hooks.insert(0, ZipExtensionImporter)
    # Not sure if this is needed...
    sys.path_importer_cache.clear()
    ## # Not sure if this is needed...
    ## import importlib
    ## importlib.invalidate_caches()
