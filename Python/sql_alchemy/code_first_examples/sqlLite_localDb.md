# SQL lite in memory example

    This is example code of local db/sqlalchemy usage
    
## code:

    from sqlalchemy import create_engine, Column, Integer, String, NVARCHAR, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base

    from sqlalchemy.orm import sessionmaker, relationship


    Base = declarative_base()

    class User(Base):
        
        __tablename__ = "person"
        
        id = Column('id', Integer, primary_key=True)
        username = Column('name', String, unique=True)
        lastname = Column('lastname', NVARCHAR)
        
        
    class SQL:
        def __init__(self):
            
            self.engine = create_engine('sqlite:///input/users.db', echo=False)
            Base.metadata.create_all(bind=self.engine)
            self.Session = sessionmaker(bind=self.engine)
        
        def add_user(self, id, username, lastname):
            
            session = self.Session()
            
            user = User()
            user.id = id
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
        
        test_sql.add_user(1,'Chris', 'Pugsly')
        
        test_sql.get_users()