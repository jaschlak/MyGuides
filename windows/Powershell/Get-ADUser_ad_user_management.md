# User Management

    User Management from within Powershell

## Active Directory

    Get-ADUser -Filter {displayname -like "*<partialname>"}                                                                 # lookup ad user by display name
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"}                                                                 # search for group by partial name
                                    
                                    
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"} | Get-ADGroupMember                                             # get users within AD Group    
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"} | Get-ADGroupMember | Select-Object distinguishedName,name      # get users within AD Group (filtered)
    

    Add-ADGroupMember -Identity <groupname> -Members <username>                                                             # add user to active directory
    Get-ADPrincipalGroupMembership -Identity <username>                                                                     # check user was added to active directory