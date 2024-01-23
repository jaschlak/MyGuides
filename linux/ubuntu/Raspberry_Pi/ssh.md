#SSH

    Enabling SSH
    
## Commands (raspi config)

    sudo raspi-config
    Select "Interfacing Options"
    Navigate to and select "SSH"
    Choose "Yes"
    Select "OK"
    Choose "Finish
    
## Commands (systemctl)

    sudo systemctl enable ssh
    sudo systemctl start ssh
    
## Headless

    Create file called "ssh" on boot partition root folder                  # Upon boot, if found ssh will be enabled and file will be deleted
    
## Connect from client machine

    Open CMD or Terminal
    
    ssh <pi username>@<pi ip address>
    
## More info

    https://www.raspberrypi.org/documentation/remote-access/ssh/