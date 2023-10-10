#Powershell Modules

    Managing Powershell Modules
    
## Commands

    Get-Module                                                                                      # see installed powershell modules
    Get-Module -Name "<module_name>"                                                                # look up module explicitly, name IE: "Microsoft.PowerApps.PowerShell"
    Get-Module -ListAvailable                                                                       # list all available modules
    Get-Module <partial_module_string>* -ListAvailable                                              # list all avaliable moduled, filtered with wildcard
    
    Update-Module                                                                                   # update all installed modules
    Update-Module -Name "<module_name>"                                                             # update module explicityl, name IE: "Microsoft.PowerApps.PowerShell"