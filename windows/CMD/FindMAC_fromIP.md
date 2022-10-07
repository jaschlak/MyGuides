#Find MAC with IP

    Find the MAC Address of a connection using an IP address
    Make sure you can ping the IP
    
Code:

    arp -a | findstr <ip address>                       # Search for single ip
    arp -a | findstr /L "<ip#1> <ip#2>"                 # Search for multiple ips