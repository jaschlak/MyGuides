# Schedulted Task

    This will create a scheduled task similar to a CRON job
    
## Create a file holding the command you want

    #Kill a task (keep path to file handy)
    taskkill /IM "<Name of Process from resmon>" /F
    
## Open cmd
    
    #/SC (DAILY), /TN (Name of this process), /ST (HH:MM)
    SCHTASKS /CREATE /SC <frequency> /TN "<your scheduled process name>" /TR "<path to file that holds the command>" /ST <Time>