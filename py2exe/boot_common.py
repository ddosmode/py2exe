Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
#

import sys
import os
import ctypes

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.

if sys.frozen == "windows_exe":
    class Stderr(object):
        _file = None
        _error = None
        _alert = ctypes.windll.user32.MessageBoxW
        _fname = os.path.join(os.environ["APPDATA"],
                                os.path.splitext(os.path.basename(sys.executable))[0] + '.log')
        def write(self, text):
            if self._file is None and self._error is None:
                import atexit, os, sys
                try:
                    self._file = open(self._fname, 'a')
                except Exception as details:
                    self._error = details
                    atexit.register(self._alert, 0,
                                    "The logfile '%s' could not be opened:\n %s" % \
                                    (self._fname, details),
                                    "Errors in %r" % os.path.basename(sys.executable),
                                    0)
                else:
                    atexit.register(self._alert, 0,
                                    "See the logfile '%s' for details" % self._fname,
                                    "Errors in %r" % os.path.basename(sys.executable),
                                    0)
            if self._file is not None:
                n_written = self._file.write(text)
                self._file.flush()
                return n_written
            else:
                return len(text)
        def flush(self):
            if self._file is not None:
                self._file.flush()
    sys.stderr = Stderr()
    del Stderr

    class Blackhole(object):
        softspace = 0
        def write(self, text):
            return len(text)
        def flush(self):
            pass
    sys.stdout = Blackhole()
    del Blackhole
del sys, ctypes

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
##
Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
