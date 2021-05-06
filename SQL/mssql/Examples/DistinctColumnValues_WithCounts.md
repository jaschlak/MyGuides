#Distinct Column Values With Counts

    Use this format to find all unique values for a column and give the counts of each
    
## query:

    select distinct columnName, count(columnName) as CountOf from tableName group by columnName