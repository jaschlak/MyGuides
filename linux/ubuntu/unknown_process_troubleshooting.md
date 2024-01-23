#Unknown Process Troubleshooting

    Troubleshooting a process you can see in your environment but you need more information
    
## find pid

    top
    htop
    
## strace commands

    strace -p <pid>                                         # attach to process and see what is executing
    strace -fp <pid>                                        # follow forks (threads)
    strace -s 80 -fp <pid>                                  # follow forks and print strings (limit 80char)
    
## strace resources

    https://strace.io/
    https://blog.packagecloud.io/eng/2015/11/15/strace-cheat-sheet/