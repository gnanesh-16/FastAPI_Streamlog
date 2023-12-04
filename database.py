from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Url string to our postgresDatabase
DB_USER = 'root'
DB_PASSWORD = 'user123'
DB_HOST = 'localhost'  # or your PostgreSQL server IP address
DB_PORT = '3306'  # default PostgreSQL port
DB_NAME = 'blogapplication'

URL_DATABASE = f'mysql+pymysql://root:user123@localhost:3306/blogapplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
