# Alter indexes with constraints

    This will alter indexes even when there are more indexes and changing filegroups is not allowed
    
## Code:

    CREATE UNIQUE CLUSTERED INDEX <index name>
    ON dbo.<tablename>(<key if applicable>)
    WITH (DROP_EXISTING=ON,ONLINE=ON) ON <New File Group>