# Install Ubuntu Mate

    How to install ubuntu mate
    
## Make sure you have

  * RaspberryPi
  * SD Card
  * Mouse
  * Keyboard
  * HDMI
  * Power Source
  * Download 32-bit operating system (ubuntu mate 16.04.img)
    
## Steps

  2. Connect the sd card to your personal computer
  2. Format the drive (I use SDFormatter)
  2. Write your 32-bit image using Win32diskimager
  2. Insert SD card into your Pi
  2. Connect Pi to your monitor and power up
  2. Go through installation process
  
## Update

  2. Open a terminal
  2. sudo apt-get update
  2. sudo apt-get -y upgrade
  2. python3 -V                     #checks for python version
  2. sudo apt-get install -y python3-pip
  2. (optional) sudo apt-get install build-essential libssl-dev libffi-dev python-dev
  
## Install Chromium

    sudo apt install -y chromium-browser
    
## Install MySQL

    sudo apt-get install mysql-server
    sudo ufw allow mysql                                                            # allow remote access
    systemctl start mysql                                                           # Start MySQL service
    systemctl enable mysql                                                          # Ensure server runs after reboot
    /usr/bin/mysql -u root -p                                                       # Run SQL Shell as root user, should prompt "mysql>"
    
    #The following need to be in mysql:
    UPDATE mysql.user SET Password = PASSWORD('password') WHERE User = 'root';      # Sets root password
    FLUSH PRIVILEGES;                                                               # Make those changes take effect by resetting user info
    SELECT User, Host, authentication_string FROM mysql.user;                       # See what users are allowed on database
    CREATE DATABASE demodb;                                                         # Create a database
    SHOW DATABASES;                                                                 # Shows databases
    
    #These 2 lines add a new database user
    INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject)
    VALUES('demouser','localhost',PASSWORD('demopassword'),'','','');
    FLUSH PRIVILEGES;
    
    GRANT ALL PRIVILEGES ON demodb.* to demouser@localhost;                         # Grant database permissions
    FLUSH PRIVILEGES;
    
    # These 2 lines verify the privilages have been set
    SHOW GRANTS FOR 'demouser'@'localhost';
    2 rows in set (0.00 sec)
    
##### More info at https://support.rackspace.com/how-to/installing-mysql-server-on-ubuntu/ , continue the guide



## Install git

    sudo apt install git

## Upgrade Python to 3.6

    sudo add-apt-repository ppa:deadsnakes/ppa                                      # PPA for deadsnakes, allows to import 3rd party modules
    sudo apt-get update                                                             # update the applied changes
    sudo apt-get install python3.6                                                  # upgrade to pythong 3.6
    pip3 --version                                                                  # see if pip is installed
    sudo -H pip3 install --upgrade pip                                              # upgrade 


	

## Uninstall or install pip/pip3

    python -m pip uninstall pip                                                     # uninstall pip 
    python3 -m pip uninstall pip                                                    # uninstall pip3


    
    
    
    
