Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
import errno
import os
import shutil
import sys
import tempfile
import unittest

##импорт модуля поиска
import py2exe.mf310 as modulefinder

TEST_DIR = 'synthetic'
TEST_PATH = [TEST_DIR]Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

print("TEST_PATH is", TEST_PATH)

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

maybe_test = [
    "a.module",
    ["a", "a.module", "sys",
     "b"],
    ["c"], ["b.something"],
    """\
a/__init__.py
a/module.py
                                from b import something
                                from c import something
b/__init__.py
                                from sys import *
"""]

maybe_test_new = [
    "a.module",
    ["a", "a.module", "sys",
     "b", "__future__"],
    ["c"], ["b.something"],
    """\
a/__init__.py
a/module.py
                                from b import something
                                from c import something
b/__init__.py
                                from __future__ import absolute_import
                                from sys import *
"""]

package_test = [
    "a.module",
    ["a", "a.b", "a.c", "a.module", "mymodule", "sys"],
    ["blahblah", "c"], [],
    """\
mymodule.py
a/__init__.py
                                import blahblah
                                from a import b
                                import c
a/module.py
                                import sys
                                from a import b as x
                                from a.c import sillyname
a/b.py
a/c.py
                                from a.module import x
                                import mymodule as sillyname
                                from sys import version_info
"""]

namespace_package_test = [
    "a.module",
    ["a", "a.b", "a.c", "a.module", "sys", "q", "q.pkg"],
    ["blahblah", "z"], [],
    """\
a/__init__.py
                                from a import b
a/module.py
                                import sys
                                from a import b as x
                                from a.c import sillyname
                                from q import pkg
                                import blahblah
a/b.py
a/c.py
                                from a.module import x
                                from sys import version_info
q/pkg.py
                                import z
"""]

absolute_import_test = [
    "a.module",
    ["a", "a.module",
     "b", "b.x", "b.y", "b.z",
     "__future__", "sys", "gc"],
    ["blahblah", "z"], [],
    """\
mymodule.py
a/__init__.py
a/module.py
                                from __future__ import absolute_import
                                import sys # sys
                                import blahblah # fails
                                import z # fails
                                import gc # gc
                                import b.x # b.x
                                from b import y # b.y
                                from b.z import * # b.z.*
a/gc.py
a/sys.py
                                import mymodule
b/__init__.py
                                from . import z
b/unused.py
b/x.py
b/y.py
b/z.py
"""]

relative_import_test = [
    "a.module",
    ["__future__",
     "a", "a.module",
     "a.b", "a.b.y", "a.b.z",
     "a.b.c", "a.b.c.moduleC",
     "a.b.c.d", "a.b.c.e",
     "a.b.x",
     "gc"],
    [], [],
    """\
mymodule.py
a/__init__.py
                                from .b import y, z # a.b.y, a.b.z
a/module.py
                                from __future__ import absolute_import # __future__
                                import gc # gc
a/gc.py
a/sys.py
a/b/__init__.py
                                from ..b import x # a.b.x
                                #from a.b.c import moduleC
                                from .c import moduleC # a.b.moduleC
a/b/x.py
a/b/y.py
a/b/z.py
a/b/g.py
a/b/c/__init__.py
                                from ..c import e # a.b.c.e
a/b/c/moduleC.py
                                from ..c import d # a.b.c.d
a/b/c/d.py
a/b/c/e.py
a/b/c/x.py
"""]

relative_import_test_2 = [
    "a.module",
    ["a", "a.module",
     "a.sys",
     "a.b", "a.b.y", "a.b.z",
     "a.b.c", "a.b.c.d",
     "a.b.c.e",
     "a.b.c.moduleC",
     "a.b.c.f",
     "a.b.x",
     "a.another"],
    [], [],
    """\
mymodule.py
a/__init__.py
                                from . import sys # a.sys
a/another.py
a/module.py
                                from .b import y, z # a.b.y, a.b.z
a/gc.py
a/sys.py
a/b/__init__.py
                                from .c import moduleC # a.b.c.moduleC
                                from .c import d # a.b.c.d
a/b/x.py
a/b/y.py
a/b/z.py
a/b/c/__init__.py
                                from . import e # a.b.c.e
a/b/c/moduleC.py
                                #
                                from . import f   # a.b.c.f
                                from .. import x  # a.b.x
                                from ... import another # a.another
a/b/c/d.py
a/b/c/e.py
a/b/c/f.py
"""]

relative_import_test_3 = [
    "a.module",
    ["a", "a.module"],
    ["a.bar"],
    [],
    """\
a/__init__.py
                                def foo(): pass
a/module.py
                                from . import foo
                                from . import bar
"""]


def open_file(path):
    dirname = os.path.dirname(path)
    try:
        os.makedirs(dirname)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return open(path, "w")


def create_package(source):
    ofi = None
    try:
        for line in source.splitlines():
            if line.startswith(" ") or line.startswith("\t"):
                ofi.write(line.strip() + "\n")
            else:
                if ofi:
                    ofi.close()
                ofi = open_file(os.path.join(TEST_DIR, line.strip()))
    finally:
        if ofi:
            ofi.close()


class ModuleFinderTest(unittest.TestCase):
    def _do_test(self, info, report=False):
        import_this, modules, missing, maybe_missing, source = info
        create_package(source)
        sys_path = sys.path[:]
        sys.path.insert(0, TEST_DIR)
        try:
            mf = modulefinder.ModuleFinder()Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            mf.import_hook(import_this)
            if report:
                mf.report()
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
## opath = sys.path[:]
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            modules = sorted(set(modules))
            found = sorted(mf.modules)
            Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            self.assertEqual(found, modules)

            Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            bad, maybe = mf.any_missing_maybe()
            bad = sorted(bad)
            maybe = sorted(maybe)
            self.assertEqual(bad, missing)
            self.assertEqual(maybe, maybe_missing)
        finally:
            sys.path = sys_path
            shutil.rmtree(TEST_DIR)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_package(self):
        self._do_test(package_test)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_namespace_package(self):
        self._do_test(namespace_package_test)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_maybe(self):
        self._do_test(maybe_test)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_maybe_new(self):
        self._do_test(maybe_test_new)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_absolute_imports(self):
        self._do_test(absolute_import_test)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_relative_imports(self):
        self._do_test(relative_import_test)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_relative_imports_2(self):
        self._do_test(relative_import_test_2)

    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
    def test_relative_imports_3(self):
        self._do_test(relative_import_test_3)


Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

if __name__ == "__main__":
    unittest.main()
