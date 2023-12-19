# User Management

	Common references for user management in Ubuntu/Debian based flavors
	
## user creation

	#create new user
	adduser <username>
    adduser -m <username>                   # creates home directory also
    adduser -m -d <path> <username>         # set user default shell
    adduser <username> <groupname>          # create user and group
	
	#create sudo user
	adduser -G sudo <username>
    
    #set user to /bin/bash
    sudo chsh -s /bin/bash username
	
## create group

    sudo groupadd <groupname>
    
## ssh

	#login
	ssh <username>@<hostname>
	
	#login as different user
	runuser <username>
	
	#login as root
	sudo su
	
## changing privs

	#change file permissions
	#convention is binary summation (421) for read write execute (rwx) in the order of user group other (ugo)
	chmod 550 <filename> 		            # gives read and execute permision to user and group but not other
	
	#change owner of file
	chown <username> <filename>
	
	#change group of file
	chgrp <groupname> <filename>
    
    #change default shell
    usermod --shell <shell path> <username>
    chsh --shell <shell path> <username>
    nano /etc/passwd                        # modify the last arguement to <shell path>
    
    #group modification
    usermod -a -G <groupname> <username>    # add user to group
    usermod -g <groupname> <username>       # change users primary group
    
    #set system permissions
    visudo
    nano /etc/sudoers
    
## find user

    users                                   # display your current username
    cat /etc/passwd | grep <username>       # format of output---> username:enc_password:UID:GID:GECOS:home_directory:login_shell
    ls /home/ | grep <username>
    
## find groups

    groups                                  # list groups associated with user
    cat /etc/group | grep <groupname>       # format of output---> group name:password:GID:list of users
    groups <username>                       # find all groups a user is in
    find / -group <name of group>           # find files group is associated with
	
