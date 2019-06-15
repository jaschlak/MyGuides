# Real VNC Installation for Raspberry Pi Ubuntu Mate

    There was some difficulty in making RealVNC server work on Ubunut Mate. Run the Client as normal on Windows 10 but on Ubuntu use this guide
    
## Download Server Files from here:

    https://raspberrypi.stackexchange.com/questions/69780/how-to-install-realvnc-server-on-ubuntu-mate-16-04-lts
    
## Install downloaded files

    sudo dpkg --install <deb_filename>
    
## Run Server with

    systemctl start vncserver-x11-serviced.service
    
## Start Server with every boot

    systemctl enable vncserver-x11-serviced.service
    
## More documentaiton

    https://www.realvnc.com/en/connect/docs/unix-start-stop.html
    
## Get ssh working Ubunut Mate 18.04 Raspberry Pi

    keys not generated use the following:
    sudo dpkg-reconfigure openssh-server
    
    login using this method:
    ssh jstar@motionpi