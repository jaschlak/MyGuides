# Tasklist

    This gives a list of tasks running and what they are associated with
    
## display filtered tasks by process name

    tasklist | find "<process name>"
    tasklist | finstr "PID <PID number>"                                            # PID shows table header
    
## display all tasks running

    tasklist
    tasklist /V                                                                     # Table format
    
## display tasks and modules they depend on

    tasklist /M
    tasklist /M <process name (no decimal)>*                                        # all isntances of chrome running
    
## display tasks and service they are connected to

    tasklist /SVC
    
## further filtering

    tasklist /fi "imagename eq <process name"
    tasklist /fi "memusage gt 500000" /fo table"                                    # tasks that are using more than 500MB of RAM
    tasklist /fi "pid eq <insert pid>"
    
## run on remote system

    tasklist /S <ip address>
    tasklist /U <domain name>\<username> /S <ip address>
    
## futher documentation

    tasklist /?