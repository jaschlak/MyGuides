# Assign Computer a Static IP

    Assign your computer a static IP address
    
## Code:

    ipconfig /all           # check your network adapter name, ip address,subnet mask, and default gateway
    
                            # assign ip address using ipconfig values
    netsh interface ip set address name="<network adapter name>" static <new ip address> <new subnet mask> <new Default Gateway>