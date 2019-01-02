# Restore a DB using TSQL

    This will backup your database
    (not tested)
    
## Code:

    BACKUP DATABASE <db name> TO DISK = '<path>\<filename>.bak' WITH INIT, COMPRESSION;