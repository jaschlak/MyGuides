# Cursors

    Using cursors to loop through a table (or something else) and do something,
    very similar to a For loop in everything else
    
## Code:


DECLARE @<variable name> <variable type

DECLARE <cursor name> CURSOR FOR (SELECT <columns> FROM <table>)
	OPEN <cursor name>

	-- Changes first row
	FETCH NEXT FROM <cursor name> INTO @<variable name>
    
    <Do something for the first iteration>

	-- Cycles through and changes all rows
	WHILE @@FETCH_STATUS = 0
	BEGIN

		FETCH NEXT FROM <cursor name> INTO @<variable name>
        
        <Do something until there is nothing left in your cursor>

	END

	CLOSE <cursor name>
DEALLOCATE <cursor name> 


## Example:
-- Declare variables you will be using
DECLARE @<variable 1> INT
DECLARE @<variable 2> varchar(50)
DECLARE @<variable 3> varchar(30)
DECLARE @<variable 4> varchar(30)
DECLARE <cursor name> CURSOR FOR (SELECT ROW_NUMBER() OVER (ORDER BY(SELECT 1)) AS row_num, <column> FROM <table>)
	OPEN <cursor name>

	-- Changes first row
	FETCH NEXT FROM <cursor name> INTO @<variable 1>, @<variable 2>
	SET @<variable 3> = (SELECT first_name FROM <table2> WHERE id = (SELECT (CAST(RAND()*100 as int) % ((SELECT COUNT(*) FROM <table2>)))))
	SET @<variable 4> = (SELECT last_name FROM <table2> WHERE id = (SELECT (CAST(RAND()*100 as int) % ((SELECT COUNT(*) FROM <table2>)))))

	UPDATE vx_pnl
	SET 
	first_name = @<variable 3>,
	last_name = @<variable 4>,
	govt_id_spec = @<variable 1>
	WHERE unid = @<variable 2>

	-- Cycles through and changes all rows
	WHILE @@FETCH_STATUS = 0
	BEGIN

		FETCH NEXT FROM <cursor name> INTO @<variable 1>, @<variable 2>
		SET @<variable 3> = (SELECT first_name FROM <table2> WHERE id = (SELECT (CAST(RAND()*100 as int) % ((SELECT COUNT(*) FROM <table2>)))))
		SET @<variable 4> = (SELECT last_name FROM <table2> WHERE id = (SELECT (CAST(RAND()*100 as int) % ((SELECT COUNT(*) FROM <table2>)))))
		
		UPDATE vx_pnl
		SET 
		first_name = @<variable 3>,
		last_name = @<variable 4>,
		govt_id_spec = @<variable 1>
		WHERE unid = @<variable 2>

	END

	CLOSE <cursor name>
DEALLOCATE <cursor name> 