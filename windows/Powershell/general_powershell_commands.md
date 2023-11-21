# General Powershell Commands

    This is a list of general powershell commands that might allow for this document to be more of a one stop shop for powershell general use
    
## Resources

    https://www.udemy.com/course/powershell-stairway-to-automation/learn
    
## General Commands

    Get-Help <command>

    Show-Command                        # show powershell command forms window
    Show-Command '<command>'            # get info on specific command  (forms window)  
    
    <command> | Grid-OUTVIEW            # get output in a UI grid view like resmon
    
    <var_name> = <value>                # assign variable
    [<var_type>]<var_name> = <value>    # assign variable with explicit type
    <var_name>.GetType()                # check variable type
    <var_name> = <val1>,<val2>,<val3>   # assign array values
    <var_name> = @(<val1>,<val2>)       # assign array values (standard notation)
    <array_var_name>[<index>]           # call array value by index
    <array_var_name>.COUNT              # get count of values in array
    <array_var_name>.Get-Type()         # get array type
    
    Get-Content
    Get-Content -Path <path> -Tail 5 | Where-Object {$_ -like '*Fail*'}
    
    Get-ChildItem -Path <path> -Recurse -Include '*.txt'
    Get-ChildItem -Path <path> | Select Name,FullName,LastAccessTime,LastWriteTime,Length
    
    Clear-content <filepath>
    Import-CSV <filepath>
    Out-File -FilePath <filepath>       # -Append -Force
    Export-CSV -Path <filepath>         # -Delimeter
    
## General Structure

    ### Loops
    
    #### forloop

        for (<initializaiton>; <condition>; <updation>)
        {
            # Loop body (execution)
        }
        
    #### foreach loop

        foreach (<call_variable> in <array>)
        {
            # Loop body (execution)
        }
    
    #### while loop (check condition, then execute if true)

        while(<condition>)
        {
            # Loop body (execution)
        }

    #### do while loop (execute, then check condition to see if still true)

        do
        {
            # Loop body (execution)
        }
        while (<condition>)
        
    ### Statements
    
        #### if, else if, else

            if (<condition>){
                # execution
            } elseif (<condition>) {
                // execution
            } else {
                # execution
            }
        
    
    ### functions
    
        function <func_name>()
        {
            # function body/output
        }

        <func_name> input1 input2           # call function
    
    
## Networking

    Test-Connection -ComputerName <hostname> -Count <int of how many results to show>
    
## Running saved Commands

    Invoke-Item <filepath>              # run commands in File
    
## Health Investigation

    Get-Service                         # get name/status of services
    Get-Process                         # get info on processes currently Running
    
## Tricks

    # Variable assignment and filtering
        $output = Get-Service                                                                                                   # assign variable
        $output | Where-Object {$_.Status -eq 'Running'}                                                                        # filter to Services that are running
                                                                            
    # Changing default object return attributes                                                                 
        #<command> | Get-Member                                                                                                 # get attributes available to select
        #<command> | Select-Object <select attributes>                                                                          # select specific attributes (comma separated)
        #<command> | Select-Object <select attributes> | Where-Object {$_.<attribute> -eq '<chosen attribute>'                  # also filter by object attribute
        #<command> | Select-Object <select attributes> | Where-Object {$_.<attribute> -eq '<chosen attribute>' | Stop-Service   # can even stop service after filtering results
        