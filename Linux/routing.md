# Routing

    Routing setup/issues
    
## Setup Example

link: https://linuxconfig.org/how-to-add-static-route-with-netplan-on-ubuntu-20-04-focal-fossa-linux

network:
    ethernets:
        enp0s3:
            dhcp4: false
            addresses: [192.168.1.202/24]
            gateway4: 192.168.1.1
            nameservers:
                addresses: [8.8.8.8,8.8.8.4,192.168.1.1]
            routes:
              - to: 172.16.0.0./24
                via: 192.168.1.100
                
## Identify route issues

    traceroute <test ip>                        # confirm the route is in use
    
    sudo ip route show                          # check for routing conflict
    
## Remove routing conflict

    sudo ip route del <entire row from sudo ip route show>