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

    chmod g-w myfile.exe                                    # take away write ability from group for myfile.exe
    chmod u+rwx, g-x test.txt                               # multiple permissions at once
    chmod o=                                                # give no permissions to other
    
## umask (changes the mask or the default template for file creation)

    umask -S                                                # switch from octal mode to symbolic mode

    umask follows the oposite values
          Dir     File
          Perms  Perms    
          
    oct Bin Str  Str 
    0   0   rwx  rw-
    1   1   rw-  rw-
    2   10  r-x  r--
    3   11  r--  r--
    4   100 -wx  -w-
    5   101 w-w  -w-
    6   110 --x  ---
    7   111 ---  ---
    
## Special modes

    setuid
    setgid
    sticky