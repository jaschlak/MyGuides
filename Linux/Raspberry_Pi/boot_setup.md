# Boot Setup

    Things to setup after writing the image (still on other computer)
    
## Steps

    move to boot folder of the sd card
    
    create a file called "ssh" no extention
    
    create a file called "wpa__supplicant.conf"
    
    Add the following contents
    
    country=US
    update_config=1
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev

    network={
     scan_ssid=1
     ssid="<WiFi Name>"
     psk="<password>"
     key_mgmt=WPA-PSK
    }