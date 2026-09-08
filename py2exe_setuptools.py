# Этот файл используется только при ПОСТРОЕНИИ py2exe.
import os, sys

import logging as log

from setuptools.command import build
from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution
from setuptools.extension import Extension
try:
    # доступно начиная с setuptools v69.0.0
    from setuptools.modified import newer_group
except ImportError:
    from setuptools.dep_util import newer_group
from setuptools.errors import CCompilerError, CompileError, PlatformError, SetupError

from sysconfig import get_platform

class Interpreter(Extension):
    def __init__(self, *args, **kw):
        # Добавьте специальную опцию «target_desc», соответствующую CCompiler
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        if "target_desc" in kw:
            self.target_desc = kw['target_desc']
            del kw['target_desc']
        else:
            self.target_desc = "executable"
        Extension.__init__(self, *args, **kw)


class Dist(Distribution):
    def __init__(self,attrs):
        self.interpreters = None
        Distribution.__init__(self, attrs)

    def has_interpreters(self):
        return self.interpreters and len(self.interpreters) > 0

    def has_extensions(self):
        return self.has_interpreters()

    def has_ext_modules(self):
        return self.has_interpreters()


class BuildInterpreters(build_ext):
    description = "build special python interpreter stubs"

    def finalize_options(self):
        super().finalize_options()
        self.interpreters = self.distribution.interpreters
        self.extensions = [Extension("unused", ["unused.c"])] Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

    def run(self):
        # Скопировано из build_ext.run(), за исключением того, что мы используем
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

        if not self.interpreters:
            return

        super().run()

        # Если мы выполняем кросс-компиляцию, инициализируем компилятор сейчас (если мы не
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        if os.name == 'nt' and self.plat_name != get_platform():
            self.compiler.initialize(self.plat_name)

        # И убедитесь, что все параметры, связанные с компиляцией/связыванием (которые могут
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        # этот объект CCompiler - таким образом, они автоматически применяются к
        # Вся компиляция и компоновка выполняются здесь.
        if self.include_dirs is not None:
            self.compiler.set_include_dirs(self.include_dirs)
        if self.define is not None:
            Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
            for (name, value) in self.define:
                self.compiler.define_macro(name, value)
        if self.undef is not None:
            for macro in self.undef:
                self.compiler.undefine_macro(macro)
        if self.libraries is not None:
            self.compiler.set_libraries(self.libraries)
        if self.library_dirs is not None:
            self.compiler.set_library_dirs(self.library_dirs)
        if self.rpath is not None:
            self.compiler.set_runtime_library_dirs(self.rpath)
        if self.link_objects is not None:
            self.compiler.set_link_objects(self.link_objects)

        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        self.build_interpreters()

    def build_interpreters(self):

        for interp in self.interpreters:
            self.build_interp(interp)

    def build_interp(self, ext):
        sources = ext.sources
        if sources is None or not isinstance(sources, (list, tuple)):
            raise SetupError(
                  "in 'interpreters' option (extension '%s'), "
                  "'sources' must be present and must be "
                  "a list of source filenames" % ext.name)
        sources = list(sources)

        ext_path = self.get_ext_fullpath(ext.name)

        if ext.target_desc == "executable":
            ext_path += ".exe"
        else:
            ext_path += ".dll"

        if 'GCC' in sys.version:
            ext.export_symbols = [s.replace(",", " ") for s in ext.export_symbols]

        depends = sources + ext.depends
        if not (self.force or newer_group(depends, ext_path, 'newer')):
            log.debug("skipping '%s' extension (up-to-date)", ext.name)
            return
        else:
            log.info("building '%s' extension", ext.name)

        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

        # XXX не учитывает 'define_macros' или 'undef_macros' --
        # API CCompiler необходимо изменить, чтобы учесть это, и я
        # хочу делать что-то одно!

        # Два возможных источника дополнительных аргументов компилятора:
        # - 'extra_compile_args' в объекте расширения
        # - переменная среды CFLAGS (не особо
        # элегантно, но люди, похоже, этого ждут, и я
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        # Переменная среды должна иметь приоритет, и
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        extra_compile_args = ext.extra_compile_args or []

        macros = ext.define_macros[:]
        for undef in ext.undef_macros:
            macros.append((undef,))

        objects = self.compiler.compile(sources,
                                         output_dir=self.build_temp,
                                         macros=macros,
                                         include_dirs=ext.include_dirs,
                                         debug=self.debug,
                                         extra_postargs=extra_compile_args,
                                         depends=ext.depends)

        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        #
        # Сценарий setup.py для Python в Unix должен иметь возможность
        # получить этот список, чтобы он мог выполнить всю необходимую очистку
        # избегайте хранения объектных файлов при очистке неудачного
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        # убедитесь, что все промежуточные элементы будут правильно перестроены.
        #
        self._built_objects = objects[:]

        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        if ext.extra_objects:
            objects.extend(ext.extra_objects)
        extra_link_args = ext.extra_link_args or []

        # Определить целевой язык, если он не указан
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        ## runtime_library_dirs=ext.runtime_library_dirs,
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        ##export_symbols=self.get_export_symbols(ext),
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        ## build_temp=self.build_temp,
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

        # Хм, чтобы Python 3.5 мог связать общую библиотеку (вместо exe
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
        # здесь?

        self.compiler.link(ext.target_desc,
                           objects, ext_path,
                           libraries=self.get_libraries(ext),
                           library_dirs=ext.library_dirs,
                           runtime_library_dirs=ext.runtime_library_dirs,
                           export_symbols=ext.export_symbols,
                           extra_postargs=extra_link_args,
                           debug=self.debug)

    def build_extensions(self):
"""Пусто, чтобы пропустить фактическую компиляцию расширения."""


    Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

    def get_ext_filename (self, inter_name):
        ext_path = inter_name.split('.')
        cpython_version_dot = '.' if 'MSC' in sys.version else ''
        if self.debug:
            fnm = os.path.join(*ext_path) + '_d'
        else:
            fnm = os.path.join(*ext_path)
        if ext_path[-1] == "resources":
            return fnm
        return '%s-py%s%s%s-%s' % (fnm, sys.version_info[0], cpython_version_dot, sys.version_info[1], get_platform())


def InstallSubCommands():
"""Добавляет наши собственные подкоманды для сборки и установки."""
    has_interpreters = lambda self: self.distribution.has_interpreters()
    buildCmds = [('build_interpreters', has_interpreters)]
    build.build.sub_commands.extend(buildCmds)

InstallSubCommands()
