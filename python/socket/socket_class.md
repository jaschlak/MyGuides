# Socket

    This is a basic class that will do easy general stuff you might want socket to do
    
    
## Example including port ping

    import socket

    class MySocket:
        
        def __init__(self):
            
            self.remote_host = None
            self.remote_port = None
            
        def port_ping(self):
        
            self.port = int(self.remote_port)
            
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            
            try:
                result = sock.connect_ex((self.remote_host, self.remote_port))
                
                if result:
                    print('port: {} is open on host: {}'.format(self.remote_port,self.remote_host))
                else:
                    print('port: {} is closed on host: {}'.format(self.remote_port,self.remote_host))
            except Exception as e:
                'There was an error accessing port: {} is closed on host: {}. Error: {}'.format(self.remote_port,self.remote_host, e)
                
                
    if __name__ == '__main__':
        
        mysocket = MySocket()
        
        mysocket.remote_host = 'localhost'
        mysocket.remote_port = 443
        
        
        mysocket.port_ping()