from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:db@localhost/fastapi'

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# print(SQLALCHEMY_DATABASE_URL)  #postgresql://postgres:db@localhost:5432/fastapi

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False , bind= engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# import time
# import psycopg2
# from psycopg2.extras import RealDictCursor
# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="db", cursor_factory= RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connected sucessfully!")
#         break
#     except Exception as error:
#         print("Connection to database was failed. Error: ", error)
#         time.sleep(2)