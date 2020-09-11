# Detect Raw Sockets

    It can be critical to catch when a raw socket has been opened to your pc
    
## How to detect

    ss --raw                # like netstat but better, raw parameter (not always best)
    
    sudo lsof | grep RAW    # list of open files, grep for raw