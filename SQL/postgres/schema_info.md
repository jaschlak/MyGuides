#Schema Info

    These are commands to be run in T-SQL to get information about the schema of the databases
    
## Queries

    \l                              # list all databases
    \c <db_name>                    # connect to database
    \dt                             # list tables within database
    \d *.*                          # list all tables
    \d <schema_name>.*              # list tables within schema
    
    
    
## Information Schema Queries

    SELECT * FROM information_schema.tables;                                        # see schema info from all tables
    SELECT * FROM information_schema.tables WHERE table_schema = 'schema_name';     # show schema info for table within schema
    