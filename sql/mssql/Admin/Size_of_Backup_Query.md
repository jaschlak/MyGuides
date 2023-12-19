# Backup Size Query

    Find out the size of a DB backup
    
## Query for entire backup (shows (database size, unallocated space))

    <Enter backup query or obtain it from the gui>
    exec sp_spaceused
    
## Query for single table or multiple tables (shows(rows, reserved, data, index_size, unused))

    <Enter backup query or obtain it from the gui>
    exec sp_spaceused