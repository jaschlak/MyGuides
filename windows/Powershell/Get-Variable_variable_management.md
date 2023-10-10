# Environmental Variables

    Environmental variable commands
    
## Create Environmental Variable

    $Env:<variableName> = <variableValue>
    
## Create Environmental Variable for Machine

    [System.Environment]::SetEnvironmentVariable(‘<variableName>’,’<variableValue>’,[System.EnvironmentVariableTarget]::Machine)
    
## Create Environmental Variable for user

    [System.Environment]::SetEnvironmentVariable(‘<variableName>’,’<variableValue>’,[System.EnvironmentVariableTarget]::User)
    
## Remove Environmental Variable

    Remove-Item Env:\<variableName>
    
## Print Environmental Variable
    
    $Env:<variableName>
    or 
    Get-Item Env:<variableName>
    
## Print all Environmental Variables

    Get-Variable