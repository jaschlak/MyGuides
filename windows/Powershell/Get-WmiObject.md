# Powershell Get-WmiObject

    Get instances of Windows Management Instrumentation Objects. Usefull for getting objects, using methods on outputs, and granular control of output attribute names
    
## Examples

    # General lookup
    Get-WmiObject -Class Win32_Operatingsystem 
    
    # Get Members (see attributes and methods)
    Get-WmiObject -Class Win32_Operatingsystem | Get-Member

    # utilize Contert To Datetime Operation and output with control of column/attribute names
    Get-WmiObject -Class Win32_Operatingsystem -ComputerName <hostname> | Select-Object @{'Name'='ServerName';'Expression'={$_.PSComputerName}}, @{'Name'='Last Restart Time';'Expression'={$_.ConvertToDateTime($_.LastBootUpTime)}}