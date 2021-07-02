# Wireshark Filters

    Common searches for wireshark filters
    
## capture filters

    # filter to mac
    eth.addr == xx:xx:xx:xx:xx:xx
    
    # filter 2 way to address
    net <ip address>
    src <ip address>
    dst <ip address>
    
    # filter to port
    port <port>
    
## post capture searches

    ip.addr == <ip address>
    ip.dst == <ip address>
    tcp.port == <port number>
    udp.port == <port number>
    
    # search for specific content
    data.data contains "<enter text>"