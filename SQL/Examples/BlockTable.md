# Table Blocking

    Block a table in SQL for a time period, roll back transaction
    
## Query:
    BEGIN TRANSACTION
    SELECT * FROM Panels WITH (TABLOCKX,HOLDLOCK)
    WAITFOR DELAY '00:00:10'
    ROLLBACK TRANSACTION 