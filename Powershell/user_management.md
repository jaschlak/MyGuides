# User Management

    User Management from within Powershell

## Active Directory

    Add-ADGroupMember -Identity <groupname> -Members <username>                             # add user to active directory
    Get-ADPrincipalGroupMembership -Identity <username>                                     # check user was added to active directory