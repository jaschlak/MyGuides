# Schedulted Task

    This will create a scheduled task similar to a CRON job
    
## Create a file holding the command you want (Optional)

    #Kill a task (keep path to file handy)
    taskkill /IM "<Name of Process from resmon>" /F
    
## Open cmd
    
    #/SC (DAILY), /TN (Name of this process), /ST (HH:MM)
    SCHTASKS /CREATE /SC <frequency> /TN "<scheduled process name>" /TR "<command or path to batch>" /ST <Time>
    
    #Creates a scheduled task "report" on remote machine "ABC" to run notepad.exe every week.
    SCHTASKS /Create /S <remote server> /U <executor user> /P <executor password> /RU <remote user> /RP <remote password> /SC <scheduled process name> /TN <name of task> /TR "<command or path to batch>" /ST <Time>
    
## Example
    # Kill Chrome Every Minute
    SCHTASKS /CREATE /SC MINUTE /TN "LogOffYourComputer" /TR "taskkill /IM chrome.exe /F"