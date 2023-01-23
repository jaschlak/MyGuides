# Docker Commands

    Useful docker commands for reference
    
## Commands

    // build docker image (dockerfile must be present)
    docker image build -t <app_name>:<app_version> .
    
    // run docker image, publish [host port]
    docker run -it -p <host_port>:<container_port> --rm --name <container_name> -d <app_name>:<app_version>
    
        --rm        removes container when stopped
        -i          keeps STDIN open and allows piping
        -t          psudo-tty (allows keyboard)
        -d          detatch shell
        <app_version>   example: v1
        
    // print docker processes running
    docker ps
    
    
    // copy file from local directory to container
    docker cp <local_file_name> <container_id>:<container_filepath>
    