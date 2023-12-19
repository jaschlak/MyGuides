#Defrag

    Defrag the database
    
Code:

    INSERT INTO archive..defraghist
               ([db],[objectid]
               ,[indexid]
               ,[idxname]
               ,[partitionnum]
               ,[frag],[runat])
         SELECT
       d.name as dbname , object_name(ps.object_id) AS objectid,
        ps.index_id AS indexid,
                  i.name as idxname,
        partition_number AS partitionnum,
        avg_fragmentation_in_percent AS frag, getdate()
    from sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL , NULL, 'LIMITED')ps 
    join sys.indexes i on
    i.object_id=ps.object_id and
    ps.index_id=i.index_id
    join sys.databases d on
    d.database_id = ps.database_id
    --Arguments 1(Database_ID,object_Id,Index_ID,partition,mode
    WHERE avg_fragmentation_in_percent >=19.0 AND ps.index_id> 0  and index_type_desc not like '%columnstore%';

    go





    Defrag - 
    SET QUOTED_IDENTIFIER ON
    declare @frag_Temp as Table
    (
        ID int identity(1,1),
           [objectid][int] NULL,
           [indexid][int] NULL,
           [partitionnum][int] NULL,
           [frag] [float] NULL
    )

    Declare @Count int;
    Declare @i tinyint=1;
    DECLARE @schemaname sysname;
    DECLARE @objectname sysname;
    DECLARE @indexname sysname;
    DECLARE @objectid int;
    DECLARE @indexid int;
    DECLARE @partitionnum bigint;
    DECLARE @partitioncount bigint;
    DECLARE @SQLCommand as Nvarchar(3000);
    insert into @frag_Temp
    SELECT
        object_id AS objectid,
        index_id AS indexid,
        partition_number AS partitionnum,
        avg_fragmentation_in_percent AS frag
    FROM sys.dm_db_index_physical_stats (DB_ID(), NULL, NULL , NULL, 'LIMITED')
    --Arguments 1(Database_ID,object_Id,Index_ID,partition,mode
    WHERE avg_fragmentation_in_percent >=19.0 AND index_id> 0  and object_id not in (682693730,778694072,1020738889,1529824562) and index_type_desc not like '%columnstore%';

    select @Count=Count(*) from @frag_Temp --Get Total Count
           While(@i<=@Count)
              Begin
                 select @objectid=objectid,@indexid=indexid,@partitionnum=partitionnum
                    from @frag_Temp where ID=@i

                  --Get tableName and its schema
                     select @objectname=o.name,@schemaname=c.name from
                     sys.objects o
                     inner join  sys.schemas c on o.schema_ID=c.schema_ID
                     where o.object_id=@objectid
                   --Get Index Name
                         select @indexname=name
                         from sys.indexes
                         where index_id=@indexid and object_id=@objectid
                   --Get Partition Count
                   select @partitioncount=count(*) from sys.partitions
                         where object_id=@objectid and index_id=@indexid
          
                    SELECT @SQLCommand= 'Alter Index ' + @indexname + ' ON ' +                                          @schemaname + '.' + @objectname + ' REBUILD WITH (ONLINE = ON,MAXDOP=1,sort_in_tempdb = on)'  
                          IF(@partitioncount>1)
                         SELECT @SQLCommand=@SQLCommand +  ' PARTITION=' +                                              convert(Char,@partitionnum);
                         
                       EXEC(@SQLCommand);

                   --Increment Count
                   set @i=@i+1

              End

