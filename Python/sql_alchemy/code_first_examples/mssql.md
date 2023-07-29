# SQL lite in memory example

    This is example code of microsoft_sql/sqlalchemy usage
    
## code:

    from sqlalchemy import create_engine, Column, Integer, String, NVARCHAR, Sequence
    from sqlalchemy import  ForeignKey
    from sqlalchemy.ext.declarative import declarative_base


    from sqlalchemy.orm import sessionmaker, relationship
    from sqlalchemy.orm.util import identity_key

    Base = declarative_base()

    class User(Base):
        
        __tablename__ = "person"
        
        id = Column('id', Integer, Sequence('user_id_seq'), primary_key=True, server_default=Sequence('user_id_seq').next_value())
        username = Column('username', String)
        lastname = Column('lastname', NVARCHAR)
        
        
    class SQL:
        def __init__(self):
            
            #self.engine = create_engine('sqlite:///input/users.db', echo=False)
            
            self.engine = create_engine('mssql+pymssql://<username>:<password>@<hostip>:<port>/<db>', echo=False)
            Base.metadata.create_all(bind=self.engine)
            self.Session = sessionmaker(bind=self.engine)
        
        def add_user(self, username, lastname):
            
            session = self.Session()
            
            user = User()
            #user.id = id
            user.username = username
            user.lastname = lastname
            
            session.add(user)
            session.commit()
            session.close()
            
        def get_users(self):
            
            session = self.Session()
            
            users = session.query(User).all()
            for user in users:
                print(user.id)
                print(user.username)
                print(user.lastname)
            
            session.close()

    if __name__ == '__main__':

        test_sql = SQL()
        
        test_sql.add_user('Chris', 'Pugsly')
        
        test_sql.get_users()
