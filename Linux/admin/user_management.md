# User Management

	Common references for user management in Ubuntu/Debian based flavors
	
## user creation

	create new user
	adduser <username>
	
	create sudo user
	adduser -G sudo <username>
	
## ssh

	login
	ssh <username>@<hostname>
	
	login as different user
	runuser <username>
	
	login as root
	sudo su
	
## privs

	change file permissions
	convention is binary summation (421) for read write execute (rwx) in the order of user group other (ugo)
	chmod 550 <filename> 		# gives read and execute permision to user and group but not other
	
	change owner of file
	chown <username> <filename>
	
	change group of file
	chgrp <groupname> <filename>
	
