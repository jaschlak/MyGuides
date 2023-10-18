# Powershell Loop

    How to use loops
    
## Structure
    
### forloop

    for (<initializaiton>; <condition>; <updation>)
    {
        // Loop body (execution)
    }
    
### foreach loop

    foreach (<call_variable> in <array>)
    {
        // Loop body (execution)
    }
    
### while loop (check condition, then execute if true)

    while(<condition>)
    {
        // Loop body (execution)
    }

### do while loop (execute, then check condition to see if still true)

    do
    {
        // Loop body (execution)
    }
    while (<condition>)
    
## Examples
    
    ### Example 1, simple for loop

        for ( $i=0; $i -lt 10; $i++)
            {
                $i
            }
            
    ### Example 2, simple for loop declaring second variable

        for (($i = 0), ($j = 0); $i -lt 10 -and $j -lt 10; $i++, $j++)
        {
            "`$i:$i"
            "`$j:$j"
            Write-Output ""
        }
        
    ### Example 3, iterate list from input file

        $serverlist = Get-Content 'serverlist.txt'
        for ( $i=0; $i -lt $serverlist.COUNT; $i++ )
        {
            Write-Host 'Server $i name is: '$serverlist[$i]
        }
    
    ### Example 4, foreach

        $serverlist = Get-Content 'serverlist.txt'
        foreach ($server in $serverlist)
        {
            Write-Host `Server name is: ` $server
        }
        
    ### Example 5, while loop
    
        // Report until Steam Service has started running
        $STEAM_servicestatus = Get-Service | Where-Object { $_.name -eq 'STEAM' };
        $STEAMstatus = $STEAM_servicestatus.Status;
        while ($STEAMstatus -eq 'Stopped')
        {
            Write-Host 'Status of the STEAM service is stopped';
    }

    ### Example 6, do while loop
    
        $OSObj = Get-ChildItem -Path Env:OS
        $OS = $OSObj.Value
        do
        {
            Write-Output "If you see more than once, this is not a windows machine"
        }
        while ($OS -ne 'Windows_NT')