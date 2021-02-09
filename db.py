

from config import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

from sqlalchemy import Column, ForeignKey, Integer, TIMESTAMP, JSON, String, Text
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker;

Base = declarative_base()

class AirtableData(Base):
    __tablename__ = "airtable"

    id = Column(Integer, primary_key=True)
    date = Column(TIMESTAMP)
    data = Column(Text)

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    methods = Column(String)
    photo = Column(String)

db = create_engine(f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')

DBSession = sessionmaker(db)
session = DBSession()

Base.metadata.create_all(db)
