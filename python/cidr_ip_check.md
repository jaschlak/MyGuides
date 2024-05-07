# CIDR IP checks

    This is meant to show you how to work with netaddr module so you can do what you need. Examples given below
    
## Examples

### Check if ips are in subnet

    # pip3 install netaddr

    from netaddr import IPNetwork, IPAddress

    subnet = '<CIDR>'
    ip1 = '<ip>'
    ip2 = '<ip>'

    subnet_range = IPNetwork(subnet)

    if IPAddress(ip1) in IPNetwork(subnet):
        print('ip1 found')
    else:
        print('ip1 not found')
        
    if IPAddress(ip2) in IPNetwork(subnet):
        print('ip2 found')
    else:
        print('ip2 not found')
        
    print('first ip in range: {}'.format(subnet_range.network))
        
    print('last ip in range: {}'.format(subnet_range.broadcast))
    