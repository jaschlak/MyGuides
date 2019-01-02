# Java Thread Locator

    This finds info on threads that are actively running on your computer
    
## Use JStack (must own the computer, simply being an admin is not enough, JDK must be isntalled)

    cd \                                                            # Go to root directory
    dir .\*jstack.exe* / /b /a-d                                    # look for jstack exe file
    cd <path to jstack.exe>                                         # Change directories to jstack folder
    Jstack -l <PID>                                                 # Find threads ID number via Task Manager/ Resource Monitor
    
    returns a thread dump of the thread
    
