# Python Service

    How to install python as a Windows Service
    Using tutorial found here https://metallapan.se/post/windows-service-pywin32-pyinstaller/
    
## Create Service File (myservice.py) *** already created in this example *** 

    import time
    import sys

    import win32serviceutil  # ServiceFramework and commandline helper
    import win32service  # Events
    import servicemanager  # Simple setup and logging

    class MyService:
        """Silly little application stub"""
        def stop(self):
            """Stop the service"""
            self.running = False

        def run(self):
            """Main service loop. This is where work is done!"""
            self.running = True
            while self.running:
                time.sleep(10)  # Important work
                servicemanager.LogInfoMsg("Service running...")


    class MyServiceFramework(win32serviceutil.ServiceFramework):

        _svc_name_ = 'MyService'
        _svc_display_name_ = 'My Service display name'

        def SvcStop(self):
            """Stop the service"""
            self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
            self.service_impl.stop()
            self.ReportServiceStatus(win32service.SERVICE_STOPPED)

        def SvcDoRun(self):
            """Start the service; does not return until stopped"""
            self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
            self.service_impl = MyService()
            self.ReportServiceStatus(win32service.SERVICE_RUNNING)
            # Run the service
            self.service_impl.run()


    def init():
        if len(sys.argv) == 1:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(MyServiceFramework)
            servicemanager.StartServiceCtrlDispatcher()
        else:
            win32serviceutil.HandleCommandLine(MyServiceFramework)


    if __name__ == '__main__':
        init()
        
## deploy python file to .exe (builds dependencies and file in "dist" folder) (commands run from CMD)

    pip3 install pywin32 pyinstaller     # install modules for service deployment
    
    pyinstaller.exe --onefile --runtime-tmpdir=. --hidden-import win32timezone <service exe filename>
    or
    pyinstaller.exe --onefile --runtime-tmpdir=. --hidden-import win32timezone myservice.py
    
## install Service (commands run from Admin Permissions CMD)

    dist\myservice.exe install
    or
    dist\<service exe filename> install
    
## Service commands that can be used for testing/debugging

    # Start:
    dist\myservice.exe start

    # Install with autostart:
    dist\myservice.exe --startup delayed install

    # Debug:
    dist\myservice.exe debug

    # Stop:
    dist\myservice.exe stop

    # Uninstall:
    dist\myservice.exe remove