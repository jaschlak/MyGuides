# Connection Info

    Gives information about connections being made to the SQL Server
    
## New Method

    CREATE TABLE #sp_who2 (SPID INT,Status VARCHAR(255),
          Login  VARCHAR(255),HostName  VARCHAR(255),
          BlkBy  VARCHAR(255),DBName  VARCHAR(255),
          Command VARCHAR(255),CPUTime INT,
          DiskIO INT,LastBatch VARCHAR(255),
          ProgramName VARCHAR(255),SPID2 INT,
          REQUESTID INT)
    INSERT INTO #sp_who2 EXEC sp_who2
    SELECT      *
    FROM        #sp_who2
    -- Add any filtering of the results here :
    --WHERE       Login = 'jschlak'
    -- Add any sorting of the results here :
    WHERE DBName = 'vxdb_850f_AOB'
    --AND HOSTNAME = 'NOCAPPSERVER '
    ORDER BY    CPUTime DESC
     
    DROP TABLE #sp_who2
    
    dbcc inputbuffer(<insertnumber from query above>)
    
    
## List info for all sessions running, filter down db, login, hostname, sessions status, command type

    -- List all Sessions into temp table for probing
    CREATE TABLE #sessTemp
    (spid smallint, ecid smallint, [status] nchar(30), loginame nchar(128), hostname nchar(128), blocking char(5), dbname nchar(128), command nchar(16), request_id int )

    INSERT INTO #sessTemp
    EXEC sp_who

    SELECT * FROM #sessTemp
    --WHERE 
    --status = -- 'sleeping' 'AWAITING COMMAND' 'SELECT' 'EXECUTE' '
    --AND
    --dbname = -- 'vxdb_830_500pnl'            
    --AND           
    --command = --'AWAITING COMMAND' 'SELECT' 'EXECUTE' '
    --AND
    --hostname = --
    --AND
    --spid = 1

    DROP TABLE #sessTemp
    
    
## Method 2 gives database names

    SELECT COUNT(*) num_connections,db_name(dbid) [db_name], loginame FROM sys.sysprocesses
    GROUP BY db_name(dbid),loginame
    
## Find Orphan Connections

    -- Find Oprhan (indefinitely waiting) connections
    select * FROM syslockinfo WHERE req_spid=-2