# Permissions

    Usefull permissions commands
    
## lookup file permissions

    ls -l                                                   # permissions symbols, -=regular file, d=directory, l=symbolic link, r=read, w=write, x=execute
    
## change permissions

    chmod                                                   # change mode command
    
    Mode Options: rwx(read write execute) ugoa (user group other) +-=
    
    Values:
    r w x
    0 0 0 off
    1 1 1 on
    4 2 1 = values to enter for all on (Bin2B10)
    
    oct Bin Str
    0   0   ---
    1   1   --x
    2   10  -w-
    3   11  -wx
    4   100 r--
    5   101 r-x
    6   110 rw-
    7   111 rwx
    
## example

    chmod g-w myfile.exe   # tage write ability from group for myfile.exe
    chmod g
    
    