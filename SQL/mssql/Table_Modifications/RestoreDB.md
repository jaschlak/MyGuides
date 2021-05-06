# Restore a DB using TSQL

    This will restore your database and overwrite the old one
    
## Code:

    RESTORE DATABASE <db name>
    FROM DISK = '<path\filename.bak>'
    WITH REPLACE
    
#### Error: The backup set holds a backup of a database other than the existing 'dbname' database.?, Use this:

    USE [master]
    RESTORE DATABASE [<dbname>] 
    FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL11.ENTREMAIN\MSSQL\Backup\vxdb811' WITH  FILE = 1,  
    MOVE N'<old mdf name without ext>' TO N'<path to mdfs>\<new mdf name>.mdf',  
    MOVE N'old ldf name without ext' TO N'<likely same path>\<new mdf name>.ldf',  NOUNLOAD,  STATS = 5, REPLACE

    GO
