# Powershell For Loop

    How to use for loops
    
## Structure

    for (<initializaiton>; <condition>; <updation>)
    {
        // Loop body (execution)
    }
    
## Example 1, simple for loop

    for ( $i=0; $i -lt 10; $i++)
        {
            $i
        }
        
## Example 2, simple for loop declaring second variable

    for (($i = 0), ($j = 0); $i -lt 10 -and $j -lt 10; $i++, $j++)
    {
        "`$i:$i"
        "`$j:$j"
        Write-Output ""
    }
    
## Example 3, iterate list from input file

    $serverlist = Get-Content '<input_file_path>'

    for ( $i=0; $i -lt $serverlist.COUNT; $i++ )
    {
        "Server $i name is: " + $serverlist[$i]
    }