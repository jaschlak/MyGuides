# Powershell Execution Policy

    Before interacting with powershell, you likely have the restricted default execution policy set.
        Because of this you cannot run powershell scripts (.ps1), you need to modify this setting
        
        Further Reading:
        https://www.linkedin.com/pulse/understanding-powershells-executionpolicy-scope-alan-bonnici/
        https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.4
        
## Execution Policy Permissions

    Restricted                                  # Scripts wont run (Default)
    RemoteSigned                                # Local scripts run, remote signed run if trusted publisher
    AllSigned                                   # Local and Remote must be signed by trusted publisher to run
    Unrestricted                                # All scripts run
    Bypass                                      # Nothing blocked, same as cmd files, no warnings, least restrictive
    Undefined                                   # Default, Restricted Clients, RemoteSigned for WindowsServer
    
## Execution Policy Scope (precedence top to bottom)

    MachinePolicy                               # all users of machine
    UserPolicy                                  # users of specific group policy
    Process                                     # only applies to current process (powershell session)
    CurrentUser                                 # settings for current user
    LocalMachine                                # settings for local machine

## Detect Execution Policy

    Get-ExecutionPolicy
    Get-ExecutionPolicy -List
    
## Set Execution Policy

    Set-ExecutionPolicy <policy setting>
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    