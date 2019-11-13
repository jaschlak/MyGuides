# Ways of querying a file

## See file contents (like cat)

    powershell.exe get-content <filepath>
    
## See file contents live

    powershell.exe get-content <filepath> -tail 2 -wait
    
## See lines that contain a select word within file
    
    powershell.exe get-content <filepath> | find "<string to find>"
    
## See number of lines that contain a select word within file

    powershell.exe get-content <filepath> | find "<string to find>" /c