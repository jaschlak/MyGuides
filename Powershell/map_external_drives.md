# Map External Drives
    
    How to map drives using powershell
    
## Initial mapping of a drive

    net use <drive IE X:> <drive\filepath>                                      # normal file path \\hostname\path
    
## See current drive mapping

    Get-PSDrive <Drive, letter only>
    
## Remove mapping of drive

    net use <drive>: /delete
    
## Map using specific login info

    net use <drive>: <drive\filepath> /user:<username> <password>               # insecure, make sure and delete history if you use this
    net use <drive>: <drive\filepath> /user:<username> *                        # prompts you for password to avoid saving a plain text password in history