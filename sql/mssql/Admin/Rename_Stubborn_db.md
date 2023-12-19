# Rename Stubborn DB

    Sometimes a service is constantly pointing at a database, rather than taking down those connections it is easiest to use single user mode
    
## query

    use master
    ALTER DATABASE <old_db_name> SET SINGLE_USER WITH ROLLBACK IMMEDIATE    
    ALTER DATABASE <old_db_name> MODIFY NAME = [new_db_name]
    ALTER DATABASE <new_db_name> SET MULTI_USER