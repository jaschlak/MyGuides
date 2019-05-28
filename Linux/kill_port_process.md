#Kill Port Process

    Search for a process on a port and kill it
    
## Find PID for anything running on a speficic port

    fuser 8080/tcp
    
## kill the processes running on that port
    
    fuser -k 8080/tcp