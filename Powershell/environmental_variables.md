# Environmental Variables

    Environmental variable commands
    
## Create Environmental Variable

    $Env:<variableName> = <variableValue>
    
## Remove Environmental Variable

    Remove-Item Env:\<variableName>
    
## Print Environmental Variable
    
    $Env:<variableName>
    or 
    Get-Item Env:<variableName>
    
## Print all Environmental Variables

    Get-Variable