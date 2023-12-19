# Compare Sequencial List  

    This will create a temp table with a sequencial list and then compare it to a sequencial list to find the missing number
    
## Query


    INSERT #test
    VALUES ('<insert any value>')
    GO <insert last number of sequencial values>

    ALTER TABLE #test
    ADD id INT IDENTITY(1,1)
    GO

    SELECT <column filled with sequencial numbers> FROM <table containing that column>
    RIGHT JOIN #test ON #test.id = <table containing that column>.<column filled with sequencial numbers>
    SELECT id FROM #test

    DROP TABLE #test
    
    Now look for the Null value, you could add the #test.id to the select statement instead and full outer join then filter for table.column = NULL