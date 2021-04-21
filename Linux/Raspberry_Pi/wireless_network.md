# Wireless Network

    Tools for setting up network
    (wlan0 = wifi adapter)
    
## scan wifi signals in range 

    sudo iwlist wlan0 scan
    
## modify wifi settings

    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    
    standard content:
    
    network={
       ssid="<wifi ssid>"
       psk="<wifi password>"
    }
    
## check adapter to find aquired ip address

    ifconfig wlan0
    
Note: May need to reboot if settings not taking effect

## More info

    https://raspberrypihq.com/how-to-connect-your-raspberry-pi-to-wifi/
    or
    https://learn.adafruit.com/adafruits-raspberry-pi-lesson-3-network-setup/setting-up-wifi-with-occidentalis