# Use postgres from terminal

    How to use sql from terminal
    
## Get Started (login and create practice db)

    # login-switch to linux user postgres
    sudo -u postgres psql postgres
    
    # run postgresql
    psql
    
    # create db
    CREATE DATABASE <db_name>
    
    # create table
        
        #-- create table syntax:
        
            CREATE TABLE <table name> (
            <column name> <column type> <optional params>,
            <column name> <column type> <optional params>;
            
        #-- create table example:
        
            CREATE TABLE names (
            id INT GENERATED ALWAYS AS IDENTITY,
            name nvarchar(80);
        
    # insert values into table
    
        #-- insert values syntax:
        
            INSERT INTO <table_name> (<columns to populate>)
            VALUES ('<values to populate>');
            
        #-- insert values example:
            
            INSERT INTO names (name)
            VALUES ('Perkins'),('Jimmy Johns'), ('Taco Johns');
            
    # query to obtain database
    
        #-- generic select statement
            SELECT * FROM names;
            
## Setup Intermediate (create restaurant location table and create linking keys)

    # create table for location