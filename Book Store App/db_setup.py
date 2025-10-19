# db_setup.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models_db import Base

engine = create_engine("sqlite:///users.db")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)
