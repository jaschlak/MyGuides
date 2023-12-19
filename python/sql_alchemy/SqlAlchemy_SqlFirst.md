# Sql Alchemy

    Snippets for using sql
    
## MySql or MsSql

    import sqlalchemy
    import pandas as pd
    import os

    from support.config import get_configuration
    from support.log import LogClass

    class SQL:
        
        def __init__(self):
            
            self.config = get_configuration()['db_info']
            
            self.trusted_connection = None #'False'
            self.sqluser            = None #os.getenv(sql_user)              # can hardcode if you have to
            self.sqlpass            = None #os.getenv(sql_pass)              # can hardcode if you have to
            self.server_type        = None #'MSSQL'
            self.host               = None #'<ip_address or host name>'
            self.port               = None #'1433'
            self.dbname             = None #'<db_name>'
            self.driver             = None #'SQL+SERVER'
            self.connector          = None #'pymssql'
            self.instance           = 'single'
            
            
            if os.name == 'nt':
                self.sql_driver_name = 'SQL+Server'
            elif os.name == 'posix':
                self.sql_driver_name = self.get_linux_driver()
                
            self.statement = None
            
        def load_config(self, db_name):
            self.trusted_connection = self.config[db_name]['integrated']
            self.sqluser            = self.config[db_name]['user']
            self.sqlpassword        = self.config[db_name]['password']
            self.host               = self.config[db_name]['host']
            self.port               = self.config[db_name]['port']
            self.server_type        = self.config[db_name]['server_type']
            self.dbname             = db_name
            
            if 'instance' in self.config[db_name].keys():
                self.instance       = self.config[db_name]['instance']
                
            if 'driver' in self.config[db_name].keys():
                self.driver         = self.config[db_name]['driver']
            
        def build_connection_string(self):
            
            '''
                ## Build connection string based on connection strategy

                sqlalchemy connection string example
                # non-integrated
                "{db_type}+{db_connector}://{login}:{password}@{host}:{port}/{dbname}?driver={driver+type}"
                
                # integrated
                '{db_type}+{db_connector}://{host}:{port}/{dbname}?driver={driver+type}?TrustedConnection=yes'
        
            '''                       
            
            # microsoft sql 
            if self.server_type == 'mssql':
            
                # load defaults
                if self.connector == None:
                    import pyodbc
                    self.connector = 'pyodbc'
                elif self.connector == 'pyodbc':
                    import pyodbc
                    
                if self.driver == None:
                    self.driver = 'SQL+SERVER'
                
                # integrated connection
                if self.trusted_connection == True:
                    
                    # single instance
                    if self.instance =='single':
                        self.con_string = '{}+{}://{}:{}/{}?driver={}?TrustedConnection=yes'.format(
                            self.server_type,
                            self.connector,
                            self.host,
                            self.port,
                            self.dbname,
                            self.driver
                            )
                    # multiple instance
                    else:
                        self.con_string = '{}+{}://{}/{}:{}/{}?driver={}?TrustedConnection=yes'.format(
                            self.server_type,
                            self.connector,
                            self.host,
                            self.instance,
                            self.port,
                            self.dbname,
                            self.driver
                            )
                # not integrated
                else:
                    
                    # single instance
                    if self.instance =='single':
                        self.con_string = '{}+{}://{}:{}@{}:{}/{}?driver={}'.format(
                            self.server_type,
                            self.connector,
                            self.sqluser,
                            self.sqlpassword,
                            self.host,
                            self.port,
                            self.dbname,
                            self.driver
                            )
                    # multiple instance
                    else:
                        self.con_string = '{}+{}://{}:{}@{}/{}:{}/{}?driver={}'.format(
                            self.server_type,
                            self.connector,
                            self.sqluser,
                            self.sqlpassword,
                            self.host,
                            self.instance,
                            self.port,
                            self.dbname,
                            self.driver
                            )
                            
            ## MYSQL (sql logins only, can add trusted, clean up on next use)
            elif self.self.server_type == 'mysql':
                import pymysql
                self.con_string = 'mysql+pymysql://{}:{}@{}/{}'.format(
                    self.sqluser, 
                    self.sqlpass, 
                    self.ip, 
                    self.dbname
                    )

            ## SQLEXPRESS (clean up on next use)
            # if using sql express and trusted connection
            if self.server_type  == 'sqlexpress' and self.trusted_connection:
                self.con_string = '{}+{}://{}\SQLEXPRESS/{}?trusted_connection=yes&driver={}'.format(
                    self.server_type,
                    self.connector,
                    self.ip, 
                    self.dbname, 
                    self.trusted_connection, 
                    self.sql_driver_name
                )
            
            elif self.server_type == 'sqlexpress' and !self.trusted_connection:
                self.con_string ='{}+{}://{}:{}@{}\SQLEXPRESS/{}?driver=no'.format(
                    self.server_type,
                    self.connector,
                    self.sqluser, 
                    self.sqlpass, 
                    self.ip, 
                    self.dbname, 
                    self.sql_driver_name
                    )
            
                return sqlalchemy.create_engine(const)

        def create_engine(self):
            self.engine = sqlalchemy.create_engine(self.con_string)
            
        def load_engine(self, db_name):
            self.config = get_configuration()['db_info']
            self.load_config(db_name)
            self.build_connection_string()
            self.create_engine()
            
        def get_df(self):
            
            connection = self.engine.connect()
            return pd.read_sql(self.statement, connection)
            
        def execute_only(self):
            
            conn = self.get_engine().connect()
            conn.execute(self.statement)
            # Note a rollback strategy can be accomplished using sessions: https://docs.sqlalchemy.org/en/13/orm/session_basics.html
                        
                        
	if __name__ == '__main__':
		
		import os
		os.chdir(os.path.dirname(os.getcwd()))
		
		from support.config import get_configuration  

		sql = SQL()
		
		db_name = '<db_name>'
		sql.load_engine(db_name)
		
		
		
		sql.statement = 'SELECT GETDATE() AS dates'
		this = sql.get_df()
		
		
		'''
			# Test write db
			sql.statement = '' '
			CREATE TABLE test_table (
			id int,
			[name] nvarchar(60))
			'' '
			# sql.execute_only()
		'''
		