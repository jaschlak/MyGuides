# Last Queries Run On Server

    See the last queries that were run on a SQL Server by date
    
## Query

    SELECT deqs.last_execution_time AS [Time], dest.text AS [Query]
    FROM sys.dm_exec_query_stats AS deqs
    CROSS APPLY sys.dm_exec_sql_text(deqs.sql_handle) AS dest
    WHERE deqs.last_execution_time > '2019-08-26 12:12:00.000'
    ORDER BY deqs.last_execution_time DESC