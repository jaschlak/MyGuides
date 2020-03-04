# Run SQL commands through CMD

    This will allow you to run a SQL command through CMD
    
## Create the file

    Create a text file in a folder you would like to store the query in
    Change the file extention from .txt to .sql
    
## Write the script

    Open the .sql file and create your query, here is an example of a possible structure
    
    USE <db name>;  
    GO  
    SELECT * from <tablename>;  
    GO
    
    
## Test the connection using Computer or Computer and instance name
    
    Open CMD and run
    sqlcmd -S ComputerA  
    sqlcmd -S ComputerA\instanceB  
    
## Test the connection using IP or IP and instance name

    Open CMD and run
    sqlcmd -S 127.0.0.1  
    sqlcmd -S 127.0.0.1\instanceB  
    
## Connect to the Database Engine by specifying the TCP\IP port number:

    Open CMD and run
    sqlcmd -S ComputerA,1433  
    sqlcmd -S ComputerA,1691  
    sqlcmd -S 127.0.0.1,1433  
    sqlcmd -S 127.0.0.1,1691  
    
## For more info on testing the connection

    https://docs.microsoft.com/en-us/sql/ssms/scripting/sqlcmd-connect-to-the-database-engine?view=sql-server-2017
    
## Params

    /S = the servername/instance name. Example: Pete's Laptop/SQLSERV
    /d = the database name. Example: Botlek1
    -E = Windows authentication.
    -U = SQL Server authentication/user. Example: Pete
    -P = password that belongs to the user. Example: 1234
    
## Run Query
    
    Open CMD, navigate to .sql file and run
    sqlcmd -S myServer\instanceName -i C:\myScript.sql -o C:\EmpAdds.txt
    
    or 
    
    sqlcmd -S <SQL ip/domain> /d <database name> -U <username> -P <password> -i <path to sql command file> -o <path to output>
    