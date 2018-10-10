
#DB tables and number of rows

Lists all tables in database and max rows

## Code:

SELECT  
    [TableName] = so.name,  
    [RowCount] = MAX(si.rows)  

FROM  
    sysobjects so,  
    sysindexes si  

WHERE  
    so.xtype = 'U'  
    AND  
    si.id = OBJECT_ID(so.name)  

GROUP BY  
    so.name  

ORDER BY  
    2 DESC  
