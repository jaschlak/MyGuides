# First Responder Toolkit

    First Responder Toolkit by Brent Ozar. These are helpful ways to find problems with your databases.
    
## Download the toolkit (stored procedures)

    https://www.brentozar.com/first-aid/
    
    or to get notes or even contribute
    https://firstresponderkit.org   (forwards to github repo)
    
## sp_blitz

* checks entire servers general health

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