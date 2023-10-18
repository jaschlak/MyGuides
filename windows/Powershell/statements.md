#Statements

    How to use statements
    
## Structure

    ### if, else if, else

        if (<condition>){
            // execution
        } elseif (<condition>) {
            // execution
        } else {
            // execution
        }
    
## Examples

    ### Example 1 if, else if, else
    
        $var = 5
            
        if ($var -lt 7){
            Write-Output "I guess it is less than 7"
        } elseif ($var -lt 9) {
            Write-Output "Oh wait, it is more than 7 but less than 9"
        } else {
            Write-Output "Shoot it could be anything!"
        }