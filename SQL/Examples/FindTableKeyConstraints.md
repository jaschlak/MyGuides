# Find Key Constraints

    This will help find what your table is connected to
    
## Code:

    DECLARE @item varchar(100) = '<insert desired table>'

    SELECT RC.CONSTRAINT_NAME FK_Name
    , KF.TABLE_SCHEMA FK_Schema
    , KF.TABLE_NAME FK_Table
    , KF.COLUMN_NAME FK_Column
    , RC.UNIQUE_CONSTRAINT_NAME PK_Name
    , KP.TABLE_SCHEMA PK_Schema
    , KP.TABLE_NAME PK_Table
    , KP.COLUMN_NAME PK_Column
    , RC.MATCH_OPTION MatchOption
    FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS RC
    JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KF ON RC.CONSTRAINT_NAME = KF.CONSTRAINT_NAME
    JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE KP ON RC.UNIQUE_CONSTRAINT_NAME = KP.CONSTRAINT_NAME

    WHERE KP.TABLE_NAME = @item
    OR KF.TABLE_NAME = @item


## Alternative Code:

    select constraintColumns.* from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE as constraintColumns
    inner join INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS as constraints on constraintColumns.CONSTRAINT_NAME = constraints.CONSTRAINT_NAME
    inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as keys on constraints.UNIQUE_CONSTRAINT_NAME = keys.CONSTRAINT_NAME
    where keys.TABLE_NAME = '<insert table name>';
    
## Alternative, find in following results

    sp_help '\<insert table name\>'


    