# User Management

    This is a shortcut for looking up and managing (eventually) user creds in Windows via Command Prompt
    
## Local

    NET USER <username> <password> /add                                                 # create user
    NET LOCALGROUP <groupname> <username> /add                                          # add user to local group
    NET USER <groupname> /active:yes                                                    # enable user in group
    NET USER <groupname> /active:no                                                     # disable user in group
    
## Domain

    NET USER                                                                            # see all users that exists
    NET USER <username>                                                                 # find group memberships for user (even wo admin, can see if user does not exist)
    NET GROUP                                                                           # see all groups that exist
    NET GROUP <groupname>                                                               # find users associated with group
    