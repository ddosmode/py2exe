"""Минимальный сервис Windows для тестирования компиляции py2exe."""
import win32serviceutil
import win32service
import win32event
import servicemanager
import sys
import os

Error 500 (Server Error)!!1500.That’s an error.There was an error. Please try again later.That’s all we know.
_LOG_FILE = os.path.join(os.path.dirname(sys.executable if getattr(sys, "frozen", False) else __file__), "minimal_service.log")


def _log(msg):
    with open(_LOG_FILE, "a") as f:
        f.write(msg + "\n")


class MinimalSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "MinimalTestService"
    _svc_display_name_ = "Minimal Test Service"
    _svc_description_ = "Minimal service to verify py2exe compilation works."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        _log("goodbye")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        _log("hello")
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        # Подождите, пока не поступит сигнал остановки
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == "__main__":
    sys.exit(win32serviceutil.HandleCommandLine(MinimalSvc))
