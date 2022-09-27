# vlf

    Virtual Log Files, chunks of log files. New vlf are created when active log files already exist and new ones need to be created.
    More Info: https://www.sqlshack.com/what-is-sql-server-virtual-log-file-and-how-to-monitor-it/
    
## Detect

    # see how many vlf's exist and how much space they takeup on the server, segmented by database
    SELECT [name] AS 'Database Name',
    COUNT(li.database_id) AS 'VLF Count',
    SUM(li.vlf_size_mb) AS 'VLF Size (MB)',
    SUM(CAST(li.vlf_active AS INT)) AS 'Active VLF',
    SUM(li.vlf_active*li.vlf_size_mb) AS 'Active VLF Size (MB)',
    COUNT(li.database_id)-SUM(CAST(li.vlf_active AS INT)) AS 'Inactive VLF',
    SUM(li.vlf_size_mb)-SUM(li.vlf_active*li.vlf_size_mb) AS 'Inactive VLF Size (MB)'
    FROM sys.databases s
    CROSS APPLY sys.dm_db_log_info(s.database_id) li
    GROUP BY [name]
    ORDER BY COUNT(li.database_id) DESC;
    
## Fix

    Go to database that has excessive vlf's
        Confirm there has been a recent full backup
        Shrink the database log files
        Confirm vlf size/count has been handled (Detect section)