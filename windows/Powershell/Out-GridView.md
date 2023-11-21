# Powershell Out-Gridview

    This transforms the text table data into a UI table like you would see in taskmanager or resmon
    
## Command

    Out-Gridview
    
## Example

    # get running processes, filtered columns, sorted
    Get-Process | Select-Object - Property Name, WorkingSet, PeakWorkingSet | 
        Sort-Object -Property WorkingSet -Descending | Out-GridView
        
    # see all files in powershell home directory
    ($A = Get-ChildItem -Path $PSHOME -Recurse) | Out-GridView
    
    # see services running on remote machine
    Invoke-Command -ComuterName <hostname> -ScriptBlock {Get-Service} | Out-GridView