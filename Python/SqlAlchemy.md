# Sql Alchemy

    Snippets for using sql
    
## MySql or MsSql

    import sqlalchemy
    import pyodbc
    import pandas as pd

    class SQL:
        
        def __init__(self):
            
            self.sqluser = os.getenv('username');
            self.sqlpass = os.getenv('password');
            self.ip = <sql_ip>;
            self.port = <sql_port>;
            self.dbname = <db_name>;
            self.sql_driver_name = 'SQL+Server'
            self.statement = ''

        # Sets up connection info for SQL
        def my_engine(self):
            return sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(self.sqluser, self.sqlpass, self.ip, self.dbname))
            
        def ms_engine(self):
            return sqlalchemy.create_engine("mssql+pyodbc://"+self.sqluser+
                                            ":"+self.sqlpass+"@"+self.ip+":"+
                                            self.port+"/"+self.dbname+"?driver="+
                                            self.sql_driver_name);
        
        def get_my_df(self):

            return pd.read_sql(self.statement, self.my_engine().connect())
            
        def get_ms_df(self):

            return pd.read_sql(self.statement, self.ms_engine().connect())

    if __name__ == '__main__':
        
        
        sql = SQL()
        
        sql.statement = <statement>
        
        
        sql.port = '3306'
        results_df = sql.get_my_df()
        
        # or
        
        sql.port = '1433'
        results_df = sql.get_ms_df()