# SQL Query Statistical Info

    Gives a bar graph of SQL historical info
    
## Code:

    import sqlalchemy;
    import pandas as pd;
    import matplotlib.pyplot as plt;


    class SQL_commands:
        # Sets up connection info for SQL
        def my_engine(sqluser = '', sqlpass = '', ip = '', port = '', dbname = '', sql_driver_name = ''):
            return sqlalchemy.create_engine("mssql+pyodbc://"+sqluser+":"+sqlpass+"@"+ip+":"+port+"/"+dbname+"?driver="+sql_driver_name);


    #%% Creating SQL connection to use

    sqluser = 'entreuser';
    sqlpass = '3ntr3';
    ip = '10.3.3.118';
    port = '1433';
    dbname = 'vxdb_820';
    sql_driver_name = 'SQL+Server'

    engine = SQL_commands.my_engine(sqluser, sqlpass, ip, port, dbname, sql_driver_name);

    con = engine.connect();

    statement = "SELECT deqs.last_execution_time AS [Time], dest.TEXT AS [Query], dest.dbid FROM sys.dm_exec_query_stats AS deqs CROSS APPLY sys.dm_exec_sql_text(deqs.sql_handle) AS dest ORDER BY deqs.last_execution_time DESC"


    results_df = pd.read_sql(statement, con)




    results_df['Time'] = list(map(lambda x: str(x)[0:16], results_df['Time']))

    x = [];
    y = [];
    for i,item in enumerate(results_df['Time'].unique()):
        x.append(i);
        y.append(len(results_df[results_df['Time']==item]));

        
    plt.bar(x, y);
    plt.show();