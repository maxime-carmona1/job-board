from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+pymysql://data:root@localhost/BD_job-advertisments") #?charset=utf8mb4"


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()