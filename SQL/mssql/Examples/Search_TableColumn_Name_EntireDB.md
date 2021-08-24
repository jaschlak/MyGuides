
# List Tables/Columns

    Search all tables and list column names

## Code:

    SELECT      
        t.name AS 'TableName' 
        ,c.name  AS 'ColumnName'  
    FROM        sys.columns c  
    JOIN        sys.tables  t   ON c.object_id = t.object_id  
    WHERE       
        t.name like '\<insert specifier for table\>'
        AND 
        c.name LIKE '%\<insert column name\>%'
    ORDER BY    TableName  
                ,ColumnName;