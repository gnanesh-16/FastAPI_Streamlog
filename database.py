from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Url string to our postgresDatabase
DB_USER = 'root'
DB_PASSWORD = 'user_password'
DB_HOST = 'localhost'  # or your PostgreSQL server IP address
DB_PORT = 'port_user'  # default PostgreSQL port
DB_NAME = 'blogapplication'

URL_DATABASE = f'mysql+pymysql://root:user_password@localhost:Port_user/blogapplication'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()
