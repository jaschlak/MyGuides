# Moving Temp DBs

    Script for moving TempDB, works for .mdf, .ldf, and .ndf files
    
## Queries

    ALTER DATABASE <db_name> MODIFY FILE (NAME = '<tempdb logical name>',  FILENAME = '<file path>')

## Example

    ALTER DATABASE tempdb MODIFY FILE (NAME = 'temp4',  FILENAME = 'd:\tempdb_mssql_4.ndf')