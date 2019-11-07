# TCP common commands

    This is a list of common commands/programs you can use for TCP connections
    
## Telnet

    sudo apt-get telnet
    
    telnet <ip> <port>                              # This will send a message to an ip that is listening
    <message>
    
## Setup Temp Response Port

    echo '<string to respond with>' | nc -l -p <port>