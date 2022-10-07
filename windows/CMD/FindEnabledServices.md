# Find Enabled Services

    This will help you find enabled Windows Services. Server 16
    
## All enabled

    dism /online /get-features /format:table | find “Enabled” | more
    
## All Possible

    dism /online /get-features /format:table | more
    
## All disabled

    dism /online /get-features /format:table | find “Disabled” | more
    
## Telnet Specifically (fill in with whatever)

    dism /online /get-features /format:table | find “Telnet” | more
    
## List details f Telnet

    dism /online /get-featureinfo /featurename:TelnetClient
    
## Enable Telnet

    dism /online /enable-feature /featurename:TelnetClient
    
### Source Link

    http://dalaris.com/how-to-manage-windows-optional-features-using-command-line-and-powershell/