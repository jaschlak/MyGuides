import time
import sys

import win32serviceutil  # ServiceFramework and commandline helper
import win32service  # Events
import servicemanager  # Simple setup and logging

from myloggerprogram import write_to_logs

class LoggerTestService:
    """Silly little application stub"""
    def stop(self):
        """Stop the service"""
        self.running = False

    def run(self):
        """Main service loop. This is where work is done!"""
        write_to_logs()
        self.running = True
        while self.running:
            time.sleep(10)  # Important work
            servicemanager.LogInfoMsg("Service running...")


class LoggerTestServiceFramework(win32serviceutil.ServiceFramework):

    _svc_name_ = 'MyLoggerService'
    _svc_display_name_ = 'MyLoggerService'
    _svc_description_ = 'Log Test with Python Service'

    def SvcStop(self):
        """Stop the service"""
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.service_impl.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)

    def SvcDoRun(self):
        """Start the service; does not return until stopped"""
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.service_impl = LoggerTestService()
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        # Run the service
        self.service_impl.run()


def init():
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(LoggerTestServiceFramework)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(LoggerTestServiceFramework)


if __name__ == '__main__':
    init()