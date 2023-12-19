# Use postgres from terminal

    How to use sql from terminal
    
## Get Started (login and create practice db)

    # login-switch to linux user postgres
    sudo -u postgres psql postgres
    
    # run postgresql
    psql
    
    # create db
    
        #-- create database syntax
        CREATE DATABASE <db_name>;
        
        #-- create database example
        CREATE DATABASE restaurants_db;
    
    
    # create table (note: multiline commands can be done on one line)
        
        #-- create table syntax:
        
            CREATE TABLE <table name> (
            <column name> <column type> <optional params>,
            <column name> <column type> <optional params>);
            
        #-- create table example:
        
            CREATE TABLE restaurants (
            id int NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            name varchar(80));
        
    # insert values into table
    
        #-- insert values syntax:
        
            INSERT INTO <table_name> (<columns to populate>)
            VALUES ('<values to populate>');
            
        #-- insert values example:
            
            INSERT INTO restaurants (name)
            VALUES ('Perkins'),('Jimmy Johns'), ('Taco Johns');
            
    # query to obtain database
    
        #-- generic select statement
            SELECT * FROM restaurants;
            
## Setup Intermediate (create restaurant location table and create linking keys)

    # create table for location (note: there is a primary key (location.restaurant_id) linked to (resaurants.id),
                                            # therefore, neither table can delete the row without dropping the key. 
                                            # Also the restaurant_id has to exist in the restaurants table to be valid.
    CREATE TABLE location (
    id int GENERATED ALWAYS AS IDENTITY,
    restaurant_id int,
    address varchar(200),
    city varchar(20),
    state varchar(15),
    zip int,
    country varchar(50),
    PRIMARY KEY(restaurant_id),
    CONSTRAINT fk_restaurant
        FOREIGN KEY(id)
            REFERENCES restaurants(id));
            
            
            
    CREATE TABLE location (id int GENERATED ALWAYS AS IDENTITY, restaurant_id int, address varchar(200), city varchar(20), state varchar(15), zip int, country varchar(50),
    PRIMARY KEY(restaurant_id), CONSTRAINT fk_restaurant FOREIGN KEY(id) REFERENCES restaurants(id));
            
    # Insert into table
    INSERT INTO location (restaurant_id, address, city, state, zip, country)
    VALUES (1, '1111 N Glenstone Ave', 'Des Moines', 'IA', 50266, 'USA');
    
    # SELECT STATEMENTS
        #-- Select only Perkins
        SELECT * FROM restaurants WHERE name = 'Perkins';
        
        #-- Select location information for Perkins also
        SELECT * FROM restaurants
        JOIN location ON restaurants.id = location.restaurant_id;

    
    
    # delete table
    DROP TABLE <tablename>;
    
    # delete database
    
    DROP DATABASE <db_name>;
     
    
    
    