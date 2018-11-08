# Simple Reply Server

    Run this code in order to wait for a connection
    After connection is established, it will simply
    reply the initial input.
    
    This was taken from Sendex's video: 
    https://www.youtube.com/watch?v=WrtebUkUssc
    
## Code:

    import socket
    import sys
    from _thread import *

    host = ''
    port = 5555
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        s.bind((host,port))
    except socket.error as e:
        print(str(e))


    s.listen(5)
    print('Waiting for a connection.')
    def threaded_client(conn):
        conn.send(str.encode('Welcome, type your info\n'))

        while True:
            data = conn.recv(2048) # buffer rate = 2048
            print(data.decode('utf-8')+'was recieved')
            reply = 'Your server output: ' + data.decode('utf-8')
            if not data:
                break
            conn.sendall(str.encode(reply))
        conn.close()

    while True:

        conn, addr = s.accept()

        print('connected to: '+addr[0]+':'+str(addr[1]))
        print(start_new_thread(threaded_client,(conn,)))
