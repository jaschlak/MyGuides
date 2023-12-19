# Lock Detection

    Find locks (I think just on tables)
    
## queries

    select cmd,* from sys.sysprocesses
    where blocked > 0