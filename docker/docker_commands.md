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
    
    # run existing docker container
    docker run -it --name <container_instance_name> -p <host_port>:<container_port> -v <host_path>:<container_path> <import_container> <shell_type>
    
        host_path, current directory = ${PWD} (linux), %cd% (windows)
        shell_type = bash (linux), cmd.exe (windows)
    
    
##  Examples

    # run "mypython1" container with -it (interactive) python 3.7 module (official from docker hub) with linux bash using host:container (ports)
    #   mapping PWD (parent working directory) to the python app (container) so the container can read/write in this directory
    #   note: in windows %cd% instead of ${pwd}
    docker run -it --name mypython1 -p 5000:5000 -v ${PWD}:/app python:3.7 bash
    
    # start "mypython1" container again -i interactive, -a attach
    docker start -ia mypython1
    
    # attach to running docker container
    docker attach <docker container>
    
    # remove "mypython1" container
    docker rm mypython1
    
    # build (create, to push), with tag, tag notation: <dockerhub_username>/<image_name>/<version_number>
    docker build -t <tag name> .
    
    # scan build for issues/vulnerabilities
    docker scout quickview
    
    # get cve info for image, image notation: <dockerhub_username>/<image_name>
    docker scout cves <image_name>
    
    # get recommendations for image, image notation: <dockerhub_username>/<image_name>
    docker scout recommendations <image_name>
    
    # push to dockerhub, tag notation: <dockerhub_username>/<image_name>/<version_number>
    docker push <tag name>
    
    # run docker image w tag, tag notation: <dockerhub_username>/<image_name>/<version_number>
    docker run -p 5000:5000 <tag_name>