# Run Spyder Remotely

    Run a remote spyder_kernel on a remote machine and use your Spyder IDE to interact with it
    
## Remote machine

pip3 install spyder-kernels

screen python3 -m spyder_kernels.console — matplotlib=’inline’ — ip=<IDE IP> -f=./remotemachine.json    # this will drop a json for the info you will need to connect

screen -ls                                                                                              # lookup screens

screen -S <screen #> -X quit                                                                            # kill screen when detatched

## Home IDE

spyder

Consoles->"Connect to an existing kernel"

*scp json file from the remote server

Connection file -> Browse (select .json from remote machine)

Select "This is a remote kernel, fill in Hostname and Username

Add password for authentication method

Click ok

(if entered correctly, a new kernel will open)