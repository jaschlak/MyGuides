# Find Key Constraints

    This will help find what your table is connected to
    
## Code:

    select constraintColumns.* from INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE as constraintColumns
    inner join INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS as constraints on constraintColumns.CONSTRAINT_NAME = constraints.CONSTRAINT_NAME
    inner join INFORMATION_SCHEMA.KEY_COLUMN_USAGE as keys on constraints.UNIQUE_CONSTRAINT_NAME = keys.CONSTRAINT_NAME
    where keys.TABLE_NAME = '<insert table name>';
    
## Alternative, find in following results

    sp_help '\<insert table name\>'


    