# First Responder Toolkit

    First Responder Toolkit by Brent Ozar. These are helpful ways to find problems with your databases.
    
## Download the toolkit (stored procedures)

    https://www.brentozar.com/first-aid/
    
    or to get notes or even contribute
    https://firstresponderkit.org   (forwards to github repo)
    
    optional getting started references provided on the site:
    https://www.brentozar.com/archive/2015/10/how-to-download-the-stack-overflow-database-via-bittorrent/
    https://www.brentozar.com/archive/2016/08/dell-dba-days-prep-using-stackexchange-queries-generate-workloads/
    
## sp_blitz

* checks entire servers general health
* meant to be run as a routine, not first response to issue

    ### Normal Use
    ```
    sp_Blitz @CheckServerInfo = 1;
    ```
    
    ### Save Output to it's own db/table
    *Make sure you have created the DBName you are using
    *Saving Output adds ServerName and CheckDate (Unions results every time run)
    
    ```
    sp_Blitz @CheckServerInfo = 1,
    @CheckUserDatabaseObjects = 1,
    @OutputDatabaseName = 'DBAtools',
    @OutputSchemaName = 'dbo',
    @OutputTableName = 'Blitz';
    ```
    
    
    #### Notes: 
    * Priority Level 1-50 are important for possible data loss
    * If your application doesn't control users don't run CheckUserDatabaseObjects -> @CheckUserDatabaseObjects = 0;
    * Can add markdown print type with "@OutputType = 'markdown';"
    * Add stored procedure to Master db for best practice to avoid digging in db's for it
    
## sp_BlitzFirst

* meant to run as first response to issue
* if no problems found, that will be the second row of results
* provides finding, url to educate you on the topic, and a possible fix (that still needs to be verified by a dba/human)

    ### Normal Use (dif)
    * takes two snapshots on tempdb, 5 seconds apart and compares
    ```
    sp_BlitzFirst
    ```
    
    ### Top 10
    * Gets the top 10 Waits    
    ```
    sp_BlitzFirst @SinceStartup = 1, @OutputType = 'Top10';
    ```

        
    ### More detail
    * can take several seconds to run
    ```
    sp_BlitzFirst @ExpertMode = 1;
    ```
        #### Results
        * running queries info
        * headline from normal stored procedure
        * Wait Stats
        * Storage
        * perfmon counters
        
    ### More params
        
        ```
        * Check Server info (CPU speed and cores)
        @CheckServerInfo = 1,
        ```
        
    ### Cron process
    
    * Recommends running every 15 minutes so stats can be seen historically during troubleshooting
    
    
    ```
    Exec sp_BlitzFirst
	@OutputDatabaseName = 'DBAtools',
	@OutputSchemaName = 'dbo',
	@OutputTableName = 'BlitzFirst',
	@OutputTableNameFileStats = 'BlitzFirst_FileStats',
	@OutputTableNameTableNamePerfmonStats = 'BlitzFirst_PerfmonStats',
	@OutputTableNameWaitStats = 'BlitzFirst_WaitStats',
	@OutputTableNameBlitzCache = 'BlitzCache',
	@OutputType = 'None'
    ```
    
        #### query output
        * Get output for Wait Stat Deltas by wait type
        ```
        SELECT * FROM DBAtools.dbo.BlitzFirst_WaitStats_Deltas
        Order BY wait_time_minutes_delta DESC
        ```

## sp_BlitzWho
* see all active queries
* typically run multiple times to see things that run briefly

```
sp_BlitzWho
GO 20
```

## sp_BlitzCache
* see top resource intensive queries
* Note: can't catch if we keep resetting our own plan cache or option recompile are on

```
EXEC sp_BlitzCache
GO
EXEC sp_BlitzCache @SortOrder = 'reads';
```

    # Sort Order
    CXPACKET, CXCONSUMER, LATCH_EX: Sort by CPU and by READS. Queries going parallel to read a lot of data or do a lot of CPU work. 
    LCK%: locking. Sort by DURATION, and look for the warning of “Long Running, Low CPU.” That’s probably a query being blocked.
    PAGEIOLATCH:  Sort by READS. reading data pages that aren’t cached in RAM.
    RESOURCE_SEMAPHORE: Sort by MEMORY GRANT, although that isn’t available in older versions of SQL. queries can’t get enough workspace memory to start running. 
    SOS_SCHEDULER_YIELD: Sort by CPU. CPU pressure, so 
    WRITELOG: Sort by WRITES. writing to the transaction log for delete/update/insert (DUI) work. 
    
    
    # More params
    
    @SortOrder = '<Category>'           # Common sort categories: 'CPU' 'WRITES' 'READS' 'DURATION' 'MEMORY GRANT' 'AVG CPU' 'AVG READS' 'EXECUTIONS' 'XPM' (executions per minute)
    @MinutesBack = <minutex>            # Only see queries that have run that many minutes back
    @StoredProcName = '<stored proc>'   # Sort by stored procedure
    @DatabaseName = '<db_name>'         # Filteres to only info on your db
    @OnlyQueryHashes = '<query_hash>'   # Query hash can be found by right clicking query plan, click properties, observe in Properties "QueryHash", can be comma delimited
    @ExportToExcel                      # Puts results in XML format to copy and paste away
    
    ## Output to TABLE
    @OutputDatabaseName = 'DBATools'
    @OutputSchemaName = 'dbo'
    @OutputTableName = 'BlitzCache'
    
## sp_BlitzIndex

```
sp_BlitzIndex
```

    ### More params
    @GetAllDatabases = 1                # Get info on all databases in server
    @BringThePain = 1                   # Required for getting more than 50 db's info, not intense just slow. Can run for more than a couple minutes
    @Mode = 0                           # Default mode is 0, 2 gets all indexes that exist on a db for inventory, Mode 3 finds missing indexes
    @SortOrder                          # 'ROWS' 'SIZE'
    
    ### Output
    
    Details column: often gives benefits per day, Brent advises <1,000,000 is not worth making a change
    Usage column: uses = how many times sql detected usage, Impact = how much sql thinks indexing might be able to improve performance, Avg query cost = Sql bucks spent on each execution
    More Info column: query to get more info on this issue

    
## Mess with People
* Make an empty db

```
CREATE DATABASE [ ];        -- move to db after
CREATE SCHEMA [ ];
CREATE TABLE [ ].[ ]([ ] INT IDENTITY(1,1));
```
    
## Workflow

    EXEC sp_BlitzFirst @SinceStartup = 1, @OutputType = 'Top10';
    GO
    -- Figure out what you need to sort by (see BlitzCache Sort Order)