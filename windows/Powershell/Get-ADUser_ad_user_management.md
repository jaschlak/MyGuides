# User Management

    User Management from within Powershell

## Active Directory

    Get-ADUser -Filter {displayname -like "*<partialname>*"}                                                                 # lookup ad user by display name
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"}                                                                 # search for group by partial name
                                    
                                    
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"} | Get-ADGroupMember                                             # get users within AD Group    
    Get-ADGroup -Filter {name -like "*<partialgroupname>*"} | Get-ADGroupMember | Select-Object distinguishedName,name      # get users within AD Group (filtered)
    

    Add-ADGroupMember -Identity <groupname> -Members <username>                                                             # add user to active directory
    Get-ADPrincipalGroupMembership -Identity <username>                                                                     # check user was added to active directory
    
    
    
## Workflow

    # find username
    Get-ADUser -Filter {displayname -like "*<partialname>*"} | Select-Object GivenName, Surname,@{name="AD Username";Expression={$_.SamAccountName}},UserPrincipalName
    
    # find ad groups
    Get-ADPrincipalGroupMembership -Identity <ad_username> | Select-Object @{name="ADGroups";Expression={$_.name}}
    
    # find all users within group
    Get-ADGroup -Filter {name -like "<groupname>"} | Get-ADGroupMember | Select-Object name,@{name="AD Username";Expression={$_.SamAccountName}},UserPrincipalName