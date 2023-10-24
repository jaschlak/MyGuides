# Powershell Credential Management

    How to handle credentials used for powershell commands
    
## Commands

    whami                                                                           # see current user
    Get-Credential                                                                  # powershell credential popup window
    $<cred_var_name> = Get-Credential                                               # save credential as variable (cred object)
    <command> -Credential <cred_var_name>                                           # pass credential to command (takes cred object input)
                                            
    (Get-Credential).Password                                                       # output the password type (SecureString)
    (Get-Credential).Password | Convert-From-SecureString                           # output in encrypted format
                    
    $<pass_var> = Get-Content <pass_file> | ConvertTo-SecureString                  # convert encrypted file password back to secure string
    New-0bject System.Management.Automation.PSCredential("<appuser>",$<pass_var>)   # create credential object from encrypted password file
    
    
## AES key workflow

    $Key = New-Object Byte[] 32
    [Security.Cryptography.RNGCryptoServiceProvider]::Create().GetBytes($Key)
    $Key | out-file <key_path>.key
    
    $temp_cred = Get-Credential
    $temp_cred.Password | ConvertFrom-SecureString -Key (Get-Content <key_path>.key) | Set-Content <pass_filepath>.txt
    
    $password = Get-Content <pass_filepath>.txt | ConvertTo-SecureString -Key (Get-Content <key_path>.key)
    $credential = New-Object System.Management.Automation.PSCredential($temp_cred.UserName,$password)
    
    Get-WmiObject -Class Win32_operatingsystem -ComputerName <computername> -Credential $credential
    
    