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
    
## sp_blitzFirst

* meant to run as first response to issue
* if no problems found, that will be the second row of results
* provides finding, url to educate you on the topic, and a possible fix (that still needs to be verified by a dba/human)

    ### Normal Use
    * takes two snapshots on tempdb, 5 seconds apart and compares
    ```
    sp_BlitzFirst
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
    
