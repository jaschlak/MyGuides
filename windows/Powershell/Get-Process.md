# Get Process

    This is meant to catelog usefull workflows/examples for Get-Process powershell module
    
## howto

    Get-Process "<process_name_regex>"
    Get-Process "<process_nameToKill_regex>" | Stop-Process
    
## kill adobe Processes

    Get-Process "acro*"
    Get-Process "acro*" | Stop-Process