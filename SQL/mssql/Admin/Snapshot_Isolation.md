# Snapshot Isolation Checks

    Working with Snapshot Isolation
    
## Check if snapshot islation is on for DB:

    SELECT snapshot_isolation_state_desc from sys.databases 
    where name='<INSERT DB NAME>'
    
## Turn on Snapshot Isolation for DB

    ALTER DATABASE <INSERT DB NAME> SET snapshot_isolation_state_desc ON;
    GO
    
## Check if snapshot Snapshot Isolation is on for a single DB using GUI

    Right Click DB from MSMM and select Properties
    Choose Options tab
    Check "Allow Snapshot Isolation" Field
    
    
    