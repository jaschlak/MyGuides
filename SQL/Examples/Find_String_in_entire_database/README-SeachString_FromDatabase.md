# Find String in Database

This will find the specific string you want in any database you point it at.


## Code  
declare @UNID VARCHAR(255);  
declare @TAB_NAME VARCHAR(255);  
declare @COL_NAME VARCHAR(255);  
declare @SQL NVARCHAR(1024);  
declare @COUNT INT;

DECLARE  MY_CURSOR CURSOR for  
SELECT TABLE_NAME,COLUMN_NAME  
	FROM INFORMATION_SCHEMA.COLUMNS
	
	WHERE TABLE_NAME NOT IN ('vx_flat_evt','vx_evt','vx_aud','vx_dev_ext') 
	
	AND DATA_TYPE IN ('nvarchar','varchar')
	
	AND CHARACTER_MAXIMUM_LENGTH = 24
	
	ORDER BY TABLE_NAME,COLUMN_NAME;

	
SET @UNID = 'DTCU/CciReqwlPwnIqXqWg=='


OPEN MY_CURSOR;

FETCH NEXT FROM MY_CURSOR INTO @TAB_NAME,@COL_NAME;

WHILE @@FETCH_STATUS = 0  

BEGIN  

	--SET @SQL = 'SELECT @CNT = COUNT(*) FROM ' +  @TAB_NAME + ' WHERE ' + @COL_NAME + ' = ''' + @UNID + '''';
	
	SET @SQL = 'SELECT @COUNT=COUNT(*) FROM ' +  @TAB_NAME + ' WHERE ' + @COL_NAME + ' = ''' + @UNID + '''';
	
	--PRINT @SQL
	
	EXEC SP_EXECUTESQL @SQL, N'@COUNT int OUTPUT', @COUNT=@COUNT OUTPUT
	
	--PRINT 'COUNT: ' + CAST(@COUNT AS VARCHAR(10));
	
	
		
	IF @COUNT > 0 
	
	BEGIN
	
		PRINT '--  ' + @TAB_NAME + ' ' +  @COL_NAME  + ' CONTAINS ' + CAST(@COUNT AS VARCHAR(10)) + ' INSTANCES OF ' + @UNID;
		
		PRINT 'SELECT '''+ @TAB_NAME + ''', * FROM ' +  @TAB_NAME + ' WHERE ' + @COL_NAME + ' = ''' + @UNID + '''';
		
	END 
	
FETCH NEXT FROM MY_CURSOR INTO @TAB_NAME,@COL_NAME;

END 


	
CLOSE MY_CURSOR 

DEALLOCATE MY_CURSOR




## Note: you will need to take this code and pass it into another Query.


