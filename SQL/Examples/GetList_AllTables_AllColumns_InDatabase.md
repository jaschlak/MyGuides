
#List Tables/Columns

Search all tables and list column names

## Code:

SELECT      c.name  AS 'ColumnName'  
            ,t.name AS 'TableName'  
FROM        sys.columns c  
JOIN        sys.tables  t   ON c.object_id = t.object_id  
WHERE       c.name LIKE '%\<insert column name\>%' AND t.name like '\<insert specifier for table\>';  
ORDER BY    TableName  
            ,ColumnName;  
			