# Table query activity

    Shows which tables are recieving the most queries
    
    https://social.msdn.microsoft.com/Forums/sqlserver/en-US/43ba1d03-1fb4-46ce-b109-913ab3181e59/find-tables-with-the-most-activity-using-tsql-was-need-query-?forum=transactsql
    
## Which tables had the most query activity

    Select Object_Name(ix.[object_id]) as objectName 
            , Sum(ddius.user_seeks) As 'table_seeks' 
            , Sum(ddius.user_scans) As 'table_scans' 
            , Sum(ddius.user_lookups) As 'table_lookups' 
            , Sum(ddius.user_updates) As 'table_updates' 
            , Sum(ddius.user_seeks + ddius.user_scans) As 'query_activity' 
    From sys.indexes As ix 
    Left Join sys.dm_db_index_usage_stats ddius 
        On ix.object_id = ddius.object_id 
            And ix.index_id = ddius.index_id 
    Where ddius.database_id = DB_ID() 
    Group By Object_Name(ix.[object_id]) 
    Order By query_activity Desc; 
    
## Modified query to show individual transactions and show how the above code works

    SELECT * FROM sys.indexes 
	Left Join sys.dm_db_index_usage_stats ddius 
        On sys.indexes.object_id = ddius.object_id 
		And indexes.index_id = ddius.index_id