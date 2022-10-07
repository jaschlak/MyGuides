# Assign Computer a Static IP

    Assign your computer a static IP address
    source: https://pureinfotech.com/set-static-ip-address-windows-10/
    
## Code:

    ipconfig /all           # check your network adapter name, ip address,subnet mask, default gateway, and DNS server address
    
                            # assign ip address using ipconfig values
    netsh interface ip set address name="<adapter name>" static <ip address> <subnet mask> <Default Gateway>
    
                            # assign DNS server address
    netsh interface ip set dns name = "<network adapter name> static <DNS server address>
    
                            # assign second DNS server address
    netsh interface ip add dns name="<second DNS address>" index=2