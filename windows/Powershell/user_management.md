# User Management

    User Management from within Powershell

## Active Directory

    Get-ADUser -Filter {displayname -like "*<partialname>"}                                 # lookup ad user by display name

    Add-ADGroupMember -Identity <groupname> -Members <username>                             # add user to active directory
    Get-ADPrincipalGroupMembership -Identity <username>                                     # check user was added to active directory