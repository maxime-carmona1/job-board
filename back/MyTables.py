import datetime
from sqlite3 import Date
from sqlalchemy  import DATE, INTEGER, Boolean, Column, ForeignKey, Integer,VARCHAR
from sqlalchemy.orm import relationship
#from sqlalchemy.ext.declarative import declarative_base
from .mainDb import base
#Base = declarative_base()

class User(base):
    __tablename__ = "TAB_user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR, unique=True, index=True)
    first_name= Column(VARCHAR, default=None)
    last_name = Column(VARCHAR, default=True)
    user_description = Column(VARCHAR, default=True)
    mail_adress = Column(VARCHAR, default=True)
    phone = Column(Integer, default=True)
    mdp = Column(VARCHAR, default= True)

    advertisments = relationship("advertisments", back_populates="users")
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

class advertisments(base):
    __tablename__ = "TAB_advertisments"

    id = Column(Integer, primary_key=True, index=True)
    entreprise = Column(VARCHAR, unique=True, index=True)
    job_title = Column(VARCHAR, default=None)
    job_description = Column(VARCHAR, default=True)
    online_date = Column(DATE, default=True)
    contratType = Column(VARCHAR, default=True)
    salaire = Column(Integer, default=True)
    user = Column(VARCHAR,ForeignKey(User.id),default= True)

    users = relationship("User", back_populates="advertisments")
    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}



