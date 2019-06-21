# Connection Info

    Gives information about connections being made to the SQL Server
    
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