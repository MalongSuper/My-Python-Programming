# models_db.py
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class UserAccount(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True)
    name = Column(String)
    password = Column(String)
    role = Column(String)  # 'customer' or 'admin'


