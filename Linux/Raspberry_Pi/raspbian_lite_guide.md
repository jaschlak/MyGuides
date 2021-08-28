# Raspbian Lite Guide

    Setup Guide to get started. Using Raspbian Lite because Linux Ubuntu Mate has been troublesome with the Pi3b
    and Raspbian Full is way to large for a small project and comes with bloat
    
    Note: the process is almost the same no matter which image you use, the download site of the image would only need to change
    
## Supplies needed

    raspberry pi
    sd card
    mouse
    keyboard
    external computer (for writing to sd card)
    internet (or images predownloaded)
    monitor (optional)
    hdmi cable (optional)
    
## Guide

### Step 1: Download Image

    * Get on external computer 
    * Download Raspbian lite Image
        - this can be found https://www.raspberrypi.org/software/operating-systems/ # make sure you download "Raspberry Pi OS Lite"
 
### Step 2: Write Image to SD Card

    * clean sd card (optionial)
        - follow instructions via Windows Command Prompt on https://github.com/jaschlak/MyGuides/blob/master/CMD/DiskPartition.md
    * open Win32DiskImager
        - under "Image File" click the folder icon
        - navigate to the raspbian lite image you just downloaded and click "Open"
        - under "Device" make sure you select the letter assigned to your formatted sd card
        - press the "Write" button
        
### Step 3: Optional Features

    Add Wifi Settings:
    
        - navigate to your sd card and open /boot/
        - create file titled "wpa_supplicant.conf"
        - add the following contents to "wpa_supplicant.conf"
        
            country=US
            ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
            update_config=1
            network={
             ssid="<wifi ssid>"
             scan_ssid=1
             psk="<wifi password>"
             key_mgmt=WPA-PSK
            }
            
    Enable SSH
    
        - navigate to your sd card and open /boot/
        - create empty file called "ssh"

### Step 4: Boot Up Pi

    * remove sd card from computer and insert into raspberry pi
    * Connect all peripheral devices (ensure hdmi is connected before power)
    * power on raspberry pi
    
### Step 5: Update Pi (linux)

    * enter the following commands, agree to all questions
        - sudo apt-get update
        - sudo apt-get upgrade
        
### Step 6: Change root password and make operational user (optional) Coming Soon
    