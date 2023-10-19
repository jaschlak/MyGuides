# Powershell Functions

    Functions in powershell
    
## Structure

    function <func_name>()
    {
        // function body/output
    }

    <func_name> input1 input2                               # call function



## Examples

    ### Example 1
    
        function sum()
        {
        param([int]$a,[int]$b)
        $c = $a+$b
        Write-Host $c
        }
        
        sum 5 2
        
    ### Example 2
    
        function checkOS()
        {
            param($OS)                                      # defining parameter (input to function)
            if($OS -eq 'Windows')
            {Write-Host 'Script will execute in Windows'}
            elseif($OS -eq 'Linux')
            {Write-Host 'Script will execute in Linux'}
        }
    
        checkOS Windows
    