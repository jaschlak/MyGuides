
# Create Tables

    Creates and modifies tables
    Populate Tables
    Join Tables
    
    (This page includes troubleshooting)
    
## Code:

    -- Create my tables
    USE Jordan_Test

    /*
    -- Creates the Stock Ticker Table
    CREATE TABLE Stock_Ticker
    (
     unid	INTEGER PRIMARY KEY,
     ticker	TEXT

    );


    -- Modifies Stock Ticker Table
    ALTER TABLE Stock_Ticker
    ADD	GoodIdea	TEXT;
    ADD	TYPE	TEXT;


    -- Creates Stock_Company Table
    CREATE TABLE Stock_Company
    (
     unid	INTEGER PRIMARY KEY,
     Company	TEXT
    );


    -- Creates Stock_Company Type
    CREATE TABLE Stock_Type
    (
     unid	INTEGER PRIMARY KEY,
     Stock_Type	TEXT
    );

    CREATE TABLE Stock_News
    (
     unid	INTEGER PRIMARY KEY,
     News	TEXT
    );
    
    
   
    -- Populating Stock_Ticker
    INSERT INTO Stock_Ticker
    VALUES 
    (123456, 'TSLA', 'No', 'Tech');

    INSERT INTO Stock_Ticker
    VALUES 
    (123457, 'FB', 'Yes', 'Tech');

    INSERT INTO Stock_Ticker
    VALUES 
    (123458, 'DCIX', 'Yes', 'Trans');

    INSERT INTO Stock_Ticker
    VALUES 
    (123459, 'CRON', 'Yes', 'Weed');



    -- Populating Stock_Company
    INSERT INTO Stock_Company
    VALUES
    ((SELECT unid FROM Stock_Ticker
    WHERE ticker LIKE 'TSLA'), 'TESLA');


    INSERT INTO Stock_Company
    VALUES
    ((SELECT unid FROM Stock_Ticker
    WHERE ticker LIKE 'FB'), 'FACEBOOK');

    INSERT INTO Stock_Company
    VALUES
    ((SELECT unid FROM Stock_Ticker
    WHERE ticker LIKE 'DCIX'), 'DIANA_CONT');

    INSERT INTO Stock_Company
    VALUES
    ((SELECT unid FROM Stock_Ticker
    WHERE ticker LIKE 'CRON'), 'CRONOS');



    -- Stock_News

    -- Populating Stock News
    INSERT INTO Stock_NEWS
    VALUES
    (111111, 'GOOD');

    INSERT INTO Stock_NEWS
    VALUES
    (000000, 'BAD');


    -- SELECT * FROM Stock_News

    -- Populating Stock Type
    INSERT INTO Stock_Type
    VALUES
    (6543, (SELECT TYPE FROM Stock_Ticker
    WHERE ticker LIKE 'CRON'));

    INSERT INTO Stock_Type
    VALUES
    (6542, (SELECT TYPE FROM Stock_Ticker
    WHERE ticker LIKE 'DCIX'));

    INSERT INTO Stock_Type
    VALUES
    (6541, (SELECT TYPE FROM Stock_Ticker
    WHERE ticker LIKE 'TSLA'));


    -- unid of Stock_News, BAD was taken to integer state of 0 instead of 000000
    -- Replace value with 222222


    UPDATE Stock_News
    SET unid = 222222
    WHERE News LIKE 'BAD';




    -- Adding column to ticker with unid of News info

    ALTER TABLE Stock_Ticker
    ADD News TEXT;

    -- Messed up and made NEWS type 'TEXT', should be INTEGER
    ALTER TABLE Stock_Ticker
    ALTER COLUMN News INTEGER;
    -- Got the following Error: Cannot alter column 'News' to be data type int. Just Delete it

    ALTER TABLE Stock_Ticker DROP COLUMN News;

    -- Adding column to ticker with unid of News info

    ALTER TABLE Stock_Ticker
    ADD News INTEGER;
    -- Turns out you still have to replace null values instead of adding a new row to a column



    -- Adding column to ticker with unid of News info -- Finally
    UPDATE Stock_Ticker
    SET News = (SELECT unid FROM Stock_News WHERE News LIKE 'Good')
    WHERE ticker LIKE 'TSLA';

    UPDATE Stock_Ticker
    SET News = (SELECT unid FROM Stock_News WHERE News LIKE 'Bad')
    WHERE ticker LIKE 'FB';

    UPDATE Stock_Ticker
    SET News = (SELECT unid FROM Stock_News WHERE News LIKE 'Good')
    WHERE ticker LIKE 'DCIX';

    UPDATE Stock_Ticker
    SET News = (SELECT unid FROM Stock_News WHERE News LIKE 'Bad')
    WHERE ticker LIKE 'Cron';




    SELECT * FROM Stock_Ticker;
    SELECT * FROM Stock_Company;
    SELECT * FROM Stock_News;
    SELECT * FROM Stock_Type;




    -- Now the goal is to Join all useful info onto one table


    SELECT Stock_Ticker.unid, ticker, Company, Stock_Type, GoodIdea, Stock_Ticker.News AS ticker_unid FROM Stock_Ticker

    FULL OUTER JOIN Stock_Company
    ON Stock_Ticker.unid = Stock_Company.unid

    FULL OUTER JOIN Stock_News
    ON Stock_Ticker.News = Stock_News.unid

    FULL OUTER JOIN Stock_Type
    ON Stock_Ticker.[TYPE] LIKE Stock_Type.Stock_Type


    -- Woohoo!
    */


