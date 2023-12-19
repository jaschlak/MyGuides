
#Search Column

    Find string in column

## Query 1 (preffered):

    SELECT * FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE TABLE_NAME = '<table_name>'
    AND COLUMN_NAME like '%<partial column name>%'
    
## Query 2:

    SELECT * FROM \<table\> WHERE \<column\> = 'Criteria1' or \<column\> = '\<criteria2\>';  
    SELECT * FROM \<table\> WHERE <column> IN ('\<Criteria1\>','\<Criteria2\>');

```
"_" represent wildcard for single space
```  
