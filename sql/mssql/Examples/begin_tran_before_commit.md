# BEGIN TRAN before commit

  > Begin tran saves whatever commands are performed locally so you can check on things before pushing the changes to the actual sql server.  
  > This eats up memory and blocks tables so don't leave in TRAN state too long
  
  ## Example
  
  `BEGIN TRAN`  
  DELETE FROM <table>
  WHERE ID = <id>  
  
  `ROLLBACK`  
  --    `COMMIT`  
  
  `BEGIN TRAN`  
  UPDATE <table_name>  
  SET <column1> = <value>, <column2> = <value>  
  WHERE ID = <id>  
  
  ROLLBACK  
  --     `COMMIT`  
  
  ## Check how many TRANS are currently running
  
  `SELECT @@TRANCOUNT`