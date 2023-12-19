#Return long entries in text

    Result cells only go up to about 60k characters if you need longer results use this query. Return value is text, not grid
    
## Query

    declare @len int
    declare @af varchar(max)
    declare @curlen int = 1

    SELECT @len = len(<column name>), @af = <column name> FROM <tablename>
    WHERE <search criteria to find certain row>

    while @curlen < @len
    begin
        print substring(@af, @curlen, 5000)
        set @curlen = @curlen + 5000
    end