from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLAKCHEMY_DATABASE_URL = "postgresql://calories_api:calories_api@localhost:5432/calories_db"
engine = create_engine(SQLAKCHEMY_DATABASE_URL)
SessionLocal1 = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
