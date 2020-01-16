# Add shortcut to CMD

    Add notepad++ to a shortcut PATH
    
## Show current PATH Content 

    echo %PATH%                                                     # big chunk
    echo %PATH:;=&echo.%                                            # Line by line
    
## Add to PATH

    set PATH=%PATH%;C:\Program Files (x86)\Notepad++                # Temperary for session
    setx path "%PATH%;C:\Program Files (x86)\Notepad++"             # Permanent for user
    setx /M path "%PATH%;C:\Program Files (x86)\Notepad++"          # Permanent for all users
    
## Backup current PATH directories

    DOSKEY /MACROS                                                  # Display current aliases created
    DOSKEY /MACROS:ALL                                              # Display all aliased executables
    echo %PATH% > C:\path-backup.txt
    
## Alias

    doskey npp=notepad++.exe $*