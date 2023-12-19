# Postgress Linux Install

    How to Install Postgres SQL on Linux Terminal
    
## Commands for installation workflow

    # install
    sudo apt-get -y install postgresql postgresql-contrib pgadmin3
    
    # Test by connecting to postgres server, login as user and database "postgres"
    sudo -u postgres psql postgres
    
    # change postgres user password
    \password postgres 
    
    # quit connection
    ctrl + d
    
    # login as postgres user
    sudo su - postgres
    
    # run postgresql client
    psql
    
    # validate connection info
    \conninfo
    

    
    
    
    
## Commands to create new users (

    # Create new superuser
    sudo -u postgres createuser --superuser <username>  sudo -u postgres psql 
    
    # Create a new database
    sudo -u postgres createdb <dbname>
    
## Run Client Program

    # Open postgresql client
    pgadmin3
    
    
## References

    https://garywoodfine.com/install-postgres-sql-ubuntu/