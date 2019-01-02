# Restore a DB using TSQL

    This will restore your database and overwrite the old one
    
## Code:

    RESTORE DATABASE <db name>
    FROM DISK = 'path\filename.bak'
    WITH REPLACE