# Usefull Commands

    Consolidated list of usefull commands
    
## Find current Path

    echo $Path
    
## Path to aliased commands
    
    which <command>
    which <command spelled backwards>                       # gives path in reverse order
    
## help/man

    <command> -h
    <command> --help
    man <command>
    man -k <search term>                                    # not sure which command you are looking for
    
## run command in background

    <command> &
    
## Working directory

    pwd                                                     # Parent Working Directory
    echo $OLDPWD                                            # Cotton Eye Joe
    
## List Directories

    ls -F                                                   # types of files /Dir, @Link, *Exec
    ls -t                                                   # list by time
    ls -r                                                   # reverse time
    ls -R                                                   # recursive
    ls --color                                              # color code directories
    tree -d                                                 # list directories only
    tree -C                                                 # color code directories
    
    ls -l                                                   # permissions symbols, -=regular file, d=directory, l=symbolic link, r=read, w=write, x=execute
    
## change directories

    cd -                                                    # takes you to last directory
    
## make/remove directory

    mkdir -p <directory>                                    # recursive create
    rmdir -p <directory>                                    # recursive delete empty directories
    rm -rf <directory>                                      # recursively force delete files and folders
    
## boot

    shutdown <time>                                         # shutdown
    telinit 0                                               # shutdown
    systemctl isolate poweroff.<target>                     # shutdown
    poweroff                                                # shutdown
    
## display currently running processes

    ps
    ps -x                                                   # all processes owned by you
    ps -fU <user>                                           # display users proces by username
    ps -fu <pid number>                                     # display process by pid
    ps -U root -u root                                      # diplay all process run by root
    ps -fG <group name or session type>                     # processes run by groupname
    ps -fG <group number>                                   # process by group number
    https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/ #More commangs
    
    
    
