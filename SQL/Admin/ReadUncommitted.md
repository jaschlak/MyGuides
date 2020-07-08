# Snapshot Isolation Checks

    Working with Snapshot Isolation
    
## Check if read uncommitted is on for DB:

    SELECT is_read_committed_snapshot_on FROM sys.databases 
    WHERE name= '<INSERT DB NAME>'
    
## Turn on read uncommitted for DB

    ALTER DATABASE <INSERT DB NAME> SET READ_COMMITTED_SNAPSHOT ON;
    GO
    
