#Find PIDs 

    You found pid's doing weird stuff in resmon didn't you? Well use one of these methods to find out where it was launched from.
    Might send output to a file and scan the output
    
    source: https://superuser.com/questions/768984/show-exe-file-path-of-running-processes-on-the-command-line-in-windows
    
## powershell

    gwmi win32_process | select Handle, name, CommandLine | format-list                         # dislplay all pid's, process name, and commandline path
    gwmi win32_process | select name
    gwmi win32_process | select CommandLine
    
# cmd

    wmic process get ProcessID,name,ExecutablePath                                              # results for all pid's    
    wmic process where "name='<processname>'" get ProcessID, ExecutablePath                     # search by process name
    wmic process where "name='<processname>'" get ProcessID, name, ExecutablePath /FORMAT:LIST  # search by process name and get id,name,path in a list