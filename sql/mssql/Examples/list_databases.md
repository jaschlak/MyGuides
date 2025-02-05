# List Databases

    This is meant to be queries that iterate database names and gather information
    from an entire sql instance
    
## Examples

    -- get list of all databases, extact the unique strings between the first and second underscores

    SELECT DISTINCT 
        CASE 
            WHEN CHARINDEX('_', name) > 0 
                 AND CHARINDEX('_', name, CHARINDEX('_', name) + 1) > 0 
            THEN SUBSTRING(name, 
                           CHARINDEX('_', name) + 1, 
                           CHARINDEX('_', name, CHARINDEX('_', name) + 1) - CHARINDEX('_', name) - 1)
            ELSE NULL  -- Avoids errors for names without two underscores
        END AS ExtractedString
    FROM sys.databases
    WHERE name LIKE '%_%_%'  -- Ensures at least two underscores exist
    AND state_desc = 'ONLINE';  -- Filters out inaccessible databases

    