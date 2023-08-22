# Dockerfile

    Example docker file for a simple python flask app
    
## dockerfile contents

    # start by pulling the python image
    FROM python:3.9.1

    # copy the requirements file into the image
    COPY ./requirements.txt /app/requirements.txt
    COPY ./app/ /app/
    COPY <local_file> <docker_filepath>

    # switch working directory
    WORKDIR /app

    # install the dependencies and packages in the requirements file
    RUN pip install -r requirements.txt

    # declare persistant volume (persistant db or other file)
    VOLUME /data

    # expose port outside container
    EXPOSE <port>

    # configure the container to run in an executed manner (python dev)
    #ENTRYPOINT [ "python" ]
    CMD ["python","main.py"]