# DB Table Storage Query

    This gives a better view of how much storage space is being used by each table than the standard SQL report
    
## Query

    SELECT sch.[name], obj.[name], ISNULL(obj.[type_desc], N'TOTAL:') AS [type_desc],
           COUNT(*) AS [ReservedPages],
           (COUNT(*) * 8) AS [ReservedKB],
           (COUNT(*) * 8) / 1024.0 AS [ReservedMB],
           (COUNT(*) * 8) / 1024.0 / 1024.0 AS [ReservedGB]
    FROM sys.dm_db_database_page_allocations(DB_ID(), NULL, NULL, NULL, DEFAULT) pa
    INNER JOIN sys.all_objects obj
            ON obj.[object_id] = pa.[object_id]
    INNER JOIN sys.schemas sch
            ON sch.[schema_id] = obj.[schema_id]
    GROUP BY GROUPING SETS ((sch.[name], obj.[name], obj.[type_desc]), ())
    ORDER BY [ReservedPages] DESC;