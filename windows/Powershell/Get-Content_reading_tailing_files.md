# Tail Log

    Get the last few lines that are new with a refresh rate through powershell
    
## Command

    Get-Content -Path <path>
    Get-Content <insert log> -Tail 2 –Wait
    Get-Content -Path <path> -First 2
    Get-Content -Path <path>\* -Include '*.txt'
    
    
    Get-Content -Path <path> -Tail 5 | Where-Object {$_ -like '*Fail*'}