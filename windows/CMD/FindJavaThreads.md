# Java Thread Locator

    This finds info on threads that are actively running on your computer
    
## Use JStack (must own the computer, simply being an admin is not enough, JDK must be isntalled)

    cd \                                                            # Go to root directory
    dir .\*jstack.exe* /s /b /a-d                                   # look for jstack exe file
    cd <path to jstack.exe>                                         # Change directories to jstack folder
    Jstack -l <PID>                                                 # Find threads ID number via Task Manager/ Resource Monitor
    
    returns a thread dump of the thread
    

## Another option from the same directory

    jcmd -l                                                         # Lists all threads using JDK
    jcmd <PID> Thread.print                                         # Prints thread
    jcmd <PID> VM.uptime                                            # Duration thread has been open for
    
### More commands for jcmd (https://www.javacodegeeks.com/2016/03/jcmd-one-jdk-command-line-tool-rule.html): 

    JFR.stop
    JFR.start
    JFR.dump
    JFR.check
    VM.native_memory
    VM.check_commercial_features
    VM.unlock_commercial_features
    ManagementAgent.stop
    ManagementAgent.start_local
    ManagementAgent.start
    GC.rotate_log
    GC.class_stats
    GC.class_histogram
    GC.heap_dump
    GC.run_finalization
    GC.run
    Thread.print
    VM.uptime
    VM.flags
    VM.system_properties
    VM.command_line
    VM.version
    help
        
    