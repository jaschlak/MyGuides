# Junos CLI

    Usefuly Junos CLI commands
    
## launch cli

    cli

    # show hostname
    show system host-name

    # show users
    show system users
    show system user <username>
    
    
    
## switch to configuration mode (remember to commit)

    configure
    
    # set hostname
    set system host-name <hostname>
    
    # login
    set system root-authentication plain-text-password
    set system login user <login name> class super-user authentication plain-text-password
    