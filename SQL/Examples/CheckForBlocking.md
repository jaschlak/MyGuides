# Checking for blocking

    These help you check for blocking accross DB's
    
## Only check for blocking
    USE Master 
    GO
    SELECT * FROM sys.dm_exec_requests WHERE blocking_session_id <> 0;
    GO

## sp_who2

    EXEC sp_who2
    GO


## filtered sp_who2 into temp table

    CREATE TABLE #sp_who2 
    (
       SPID INT,  
       Status VARCHAR(1000) NULL,  
       Login SYSNAME NULL,  
       HostName SYSNAME NULL,  
       BlkBy SYSNAME NULL,  
       DBName SYSNAME NULL,  
       Command VARCHAR(1000) NULL,  
       CPUTime INT NULL,  
       DiskIO INT NULL,  
       LastBatch VARCHAR(1000) NULL,  
       ProgramName VARCHAR(1000) NULL,  
       SPID2 INT
    ) 
    GO

    INSERT INTO #sp_who2
    EXEC sp_who2
    GO

    SELECT *
    FROM #sp_who2
    WHERE Login = 'bla'
    GO

    DROP