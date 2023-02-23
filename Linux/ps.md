#ps

    Process Status command
    
## Most Used

    ps aux | grep <pid>
    
## Examples

    ps
    ps aux                                                  # extra output
    ps -x                                                   # all processes owned by you
    ps -fU <user>                                           # display users proces by username
    ps -fu <pid number>                                     # display process by pid
    ps -U root -u root                                      # diplay all process run by root
    ps -fG <group name or session type>                     # processes run by groupname
    ps -fG <group number>                                   # process by group number
    https://www.tecmint.com/ps-command-examples-for-linux-process-monitoring/ #More commangs
    
