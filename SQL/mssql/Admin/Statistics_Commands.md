# Set Statistics Commands

    Turning on Statistics to validate cost of sql commands
    
    
## Commands

SET STATISTICS <Item1,Item2> ON;
<Normal Query>;
   
   
## IO

SET STATISTICS IO ON;                   -- info on how the query communicated. See how many pages it had to read through
GO

SET STATISTICS IO TIME;                   -- info on cpu time/elapsed time
GO




## Lookup stats for table

    Navigate to table
    Open Statistics folder
    Identify: IX_<something>_id
    DBCC SHOW_STATISTICS('dbo.<tablename>', 'IX_<something>_id')