# Redhat Package Manager

    Some usefull Yum commands to reference
    
## yum(Yellowdog Updater Modified) commands

    yum search <search string>          # will search for the desired commands
    yum info <package>                  # display package info
    yum install [-y] <package>          # install package (optional answer yes to questions) (requires root)
    yum remove <package>                # removes package (requires root)
    
## RPM(Redhat Package Manager) commands (download package file and install locally)

    rpm -qa                             # displays installed packages
    rpm -qf <filepath>                  # display what package the file belongs to
    rpm -ql <package>                   # list package files
    rpm -ivh <package>.rpm              # install package
    rpm -e <package>                    # uninstall package