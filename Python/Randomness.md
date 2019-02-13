#Randomness

    Here are some tips if you need to randomize something
    
## Random number:

    abs(checksum(NewId()) % 10000000)
    
## Random value

    --Create a table:
    Create table RandomNames
    (id int,
     <column 1> varchar(100),
     <column 2> varchar(100)
    )

    insert into RandomNames
    (id, <column 1>,<column 2>)
    select 1,'<value 1>','<value 2>'
    union
    select 2,'<value 3>','<value 4>'
    union
    select 3,'<value 5>','<value 6>'
    union
    select 4,'<value 7>','<value 8>'
    union
    select 5,'<value 9>','<value 10>'
    
    (SELECT <column interest> FROM <table> WHERE id = (SELECT (CAST(RAND()*100 as int) % ((SELECT COUNT(*) FROM <table>)-1)))+1)