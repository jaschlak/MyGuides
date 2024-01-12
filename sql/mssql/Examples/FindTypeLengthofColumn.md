# Find TypeLengthCol

    Find Type and length for a column in the database
    
## Query

    sp_help <tablename>

    SELECT *
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE table_name = '<tablename>'

    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE 
         TABLE_NAME = '<tablename>' AND 
         COLUMN_NAME = '<columnname>'

    SELECT c.name,
           c.max_length,
           c.precision,
           c.scale,
           c.is_nullable,
           t.name
      FROM sys.columns c
      JOIN sys.types   t
        ON c.user_type_id = t.user_type_id
     WHERE c.object_id    = Object_id('<tablename>')