# General Powershell Commands

    This is a list of general powershell commands that might allow for this document to be more of a one stop shop for powershell general use
    
## Resources

    https://www.udemy.com/course/powershell-stairway-to-automation/learn
    
## General Commands

    Show-Command                        # show powershell command forms window
    Show-Command '<command>'            # get info on specific command  (forms window)  
    Get-Service                         # get name/status of services
    <var_name> = <value>                # assign variable
    [<var_type>]<var_name> = <value>    # assign variable with explicit type
    <var_name>.GetType()                # check variable type
    <var_name> = <val1>,<val2>,<val3>   # assign array values
    <var_name> = @(<val1>,<val2>)       # assign array values (standard notation)
    <array_var_name>[<index>]           # call array value by index
    <array_var_name>.COUNT              # get count of values in array
    <array_var_name>.Get-Type()         # get array type
    
## General Structure

    ### Loops
    
    #### forloop

        for (<initializaiton>; <condition>; <updation>)
        {
            // Loop body (execution)
        }
        
    #### foreach loop

        foreach (<call_variable> in <array>)
        {
            // Loop body (execution)
        }
    
    
## Tricks

    # Variable assignment and filtering
        $output = Get-Service                               # assign variable
        $output | Where-Object {$_.Status -eq 'Running'}    # filter to Services that are running
        
        