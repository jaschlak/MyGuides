# Ways of querying a file

## See file contents (like cat)

    powershell.exe get-content <filepath>
    
## See file contents live

    powershell.exe get-content <filepath> -tail 2 -wait
    
## See lines that contain a select word within file
    
    powershell.exe get-content <filepath> | find "<string to find>"
    
## See number of lines that contain a select word within file

    powershell.exe get-content <filepath> | find "<string to find>" /c
    
## Replace Part of a file

    powershell.exe (<source filepath> gc hibernate.properties) -replace '<original string>', '<replacement string>' | powershell.exe Set-Content <destination filepath>
    
## Replace part of a file with Regex (note the space after $2 needs to be dealt with at some point)

    powershell.exe (powershell.exe gc <source filepath>) -replace '(<regex to keep>)<regex to replace>(regex2 to keep)<regex to delete>', '$1<replacement string>$2 <replacement string>' | powershell.exe Set-Content <output filepath>