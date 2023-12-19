# SQL/Python Shell

## Initial for both versions

    There are several ways to connect to pyodbc, I prefer to make a new ODBC connection to make life easier.

    win+s, ODBC
    User DSN -> Add -> whatever your ODBC Driver is ->
    Enter the name you want to use, description of the use, and pick your SQL server
    Make note of the Driver you picked

# sqlalchemy version

## Build Connection:
    
    import sqlalchemy
    import pandas as pd;
    
## import db to dataframe

    engine = sqlalchemy.create_engine("mssql+pyodbc://<SQL username>:<SQL pass>@localhost:1433/<table>?driver=<ODBC+driver+name>");
    df = pd.read_sql('vx_dev', con=engine)
    
## write to database

    
    engine = sqlalchemy.create_engine("mssql+pyodbc://<SQL username>:<SQL pass>@localhost:1433/<table>?driver=<ODBC+driver+name>");
    df.to_sql('<new table name (can't exist)>', engine, index=False)


## Create database

    engine = sqlalchemy.create_engine("mssql+pyodbc://<SQL username>:<SQL pass>@localhost:1433/<table>?driver=<ODBC+driver+name>");
    con = engine.connect();
    con.execute("create database <new db name>");
    
    
# pyodbc version:
    

    
## Build Connection:

    import pyodbc;
    con = pyodbc.connect('DRIVER={<Driver Name>};SERVER=<YourIP or localhost>;PORT=1433;DATABASE=<table you want to use>;UID=<SQL username>;PWD=<SQL password>');
    
## Query results to a dataframe

    cur = con.cursor();
    df=pd.read_sql_query('<T-SQL statement>', con)
    
## Query results to list of tuples

    cur = con.cursor();
    table = '<table>';
    cur.columns(table);
    columns = [column[0] for column in cur.description]
    rows = cur.execute("SELECT * FROM "+table).fetchall();
    columns = columns = [column[0] for column in cur.description]
    
## Create table

    cur = con.cursor();
    querystring = 'CREATE TABLE <table name> (<col name> <col type>,<col name> <col type>,...ect);';
    cur.execute(querystring);
    con.commit();
    
## Insert values into table from tuple

    values = [];
    for i in range(0,len(variable1)):
        values.append(variable1[i], variable2[i], ect...)                           # make list of tuples for sql input
    Make a tuple following the same convention as table
    cur.executemany("insert into <table name> values (?,?,?,?,?,?,?,?)", values)
    con.commit();