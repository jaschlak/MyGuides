# SQL lite in memory example

    This is example code of an in memory/sqlalchemy usage
    
## code:

    from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
    from sqlalchemy.ext.declarative import declarative_base

    from sqlalchemy.orm import sessionmaker, relationship


    Base = declarative_base()

    class User(Base):
        __tablename__ = "person"
        
        id = Column('id', Integer, primary_key=True)
        username = Column('name', String, unique=True)
        

    # create in memory engine and session
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)

    # instantiate session and add user
    session = Session()
    user = User()
    user.id = 0
    user.username = 'alice'

    session.add(user)
    session.commit()
    session.close()