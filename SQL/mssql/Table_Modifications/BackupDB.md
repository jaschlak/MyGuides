# Restore a DB using TSQL

    This will backup your database
    (not tested)
    
## Code:

    BACKUP DATABASE <db name> TO DISK = '<path>\<filename>.bak' WITH INIT, COMPRESSION;
    

#### If you want to overwrite existing db's use this:

    BACKUP DATABASE [<old db name>]
    TO  DISK = N'<new path>\<new db name>' 
    WITH NOFORMAT, INIT,  NAME = N'vxdb_811-Full Database Backup', SKIP, NOREWIND, NOUNLOAD,  STATS = 10
    GO
