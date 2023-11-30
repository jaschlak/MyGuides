# Powershell Network

    These are network specific powershell commands. This document is being added so I don't have to dig into other modules 
        when I need to be quick with network probing. I am sure I will expand the content later.
        
## Networking

    Test-Connection -ComputerName <hostname> -Count <int of how many results to show>
    Test-NetConnection -ComputerName <hostname> -Port <port>                                            # port ping