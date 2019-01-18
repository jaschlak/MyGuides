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
    
