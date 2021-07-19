# Sql Alchemy

    Snippets for using sql
    
## MySql or MsSql

    import sqlalchemy
    import pyodbc
    import pandas as pd

    class SQL:
        
        def __init__(self):
            
            self.sqluser = os.getenv(sql_user)              # can hardcode if you have to
            self.sqlpass = os.getenv(sql_pass)              # can hardcode if you have to
            self.trusted_connection = 'no'
            self.server_edition = 'SQLEXPRESS'
            self.ip = '<ip_address or host name>'
            self.port = ''
            self.dbname = '<db_name>'
            self.sql_driver_name = 'SQL+Server'
            self.statement = ''
            
        def auto_config(self):
            
            if self.server_edition.lower() == 'sqlexpress':
                self.sql_driver_name = 'SQL+Server+Native+Client+11.0'
                self.port = 1433
            elif self.server_edition.THIS.lower() == 'mssql':
                self.sql_driver_name = 'SQL+Server'
                self.port = 1433
            elif self.server_edition.lower() == 'mysql':
                self.port = 3306
            
            if self.trusted_connection.lower() == 'yes':
                self.sqluser = ''
                self.sqlpass = ''
                
        def get_engine(self):
            
            ## SQLEXPRESS
            # if using sql express and trusted connection
            if self.server_edition.lower() == 'sqlexpress' and self.trusted_connection.lower() == 'yes':
                const = 'mssql+pyodbc://{0}\SQLEXPRESS/{1}?trusted_connection={2}&driver={3}' \
                .format(self.ip, self.dbname, self.trusted_connection, self.sql_driver_name)

                return sqlalchemy.create_engine(const)
            
            elif self.server_edition.lower() == 'sqlexpress' and self.trusted_connection.lower() == 'no':
                const = constr = 'mssql+pyodbc://{0}:{1}@{2}\SQLEXPRESS/{3}?driver={4}' \
                    .format(self.sqluser, self.sqlpass, self.ip, self.dbname, self.sql_driver_name)
            
                return sqlalchemy.create_engine(const)
            
            
            ## MSSQL (sql logins only, can add trusted users later)
            elif self.server_edition.lower() == 'mssql':
                const = 'mssql+pyodbc//{0}:{1}@{2}:{3}/{4}?driver={5}' \
                    .format(self.sqluser, self.sqlpass, self.ip, self.port, self.dbname, self.sql_driver_name)
                    
                return sqlalchemy.create_engine(const)
                    
            ## MYSQL (sql logins only, can add trusted users later)
            elif self.server_edition.lower() == 'mysql':
                import pymysql
                const = 'mysql+pymysql://{0}:{1}@{2}/{3}' \
                    .format(self.sqluser, self.sqlpass, self.ip, self.dbname)
                    
                return sqlalchemy.create_engine(const)
            
                
            
        def get_df(self):
            
            engine = self.get_engine()
            return pd.read_sql(self.statement, engine.connect())

        def execute_only(self):
            
            conn = self.get_engine().connect()
            conn.execute(self.statement)
            # Note a rollback strategy can be accomplished using sessions: https://docs.sqlalchemy.org/en/13/orm/session_basics.html

    if __name__ == '__main__':
        
        # get dataframe from database
        sql = SQL()
        sql.statement = <statement>
        results_df = sql.get_df()

        # Test write db
        sql.statement = 'CREATE TABLE test_table (' \
            'id int,' \
            '[name] nvarchar(60))'
        sql.execute_only()