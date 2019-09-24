# Find TypeLengthCol

    Find Type and length for a column in the database
    
## Query

    SELECT * FROM vx_prop
    WHERE prop_key = 'schema.version'

    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE 
         TABLE_NAME = '<insert tablename>' AND 
         COLUMN_NAME = '<insert column name>'

    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE 
         TABLE_NAME = '<insert tablename>' AND 
         COLUMN_NAME = '<insert column name>'
