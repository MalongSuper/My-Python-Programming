from sqlalchemy import Column, String, Float, Date, Table
from db_setup import Base

class CouponDB(Base):
    __tablename__ = "coupons"
    user_email = Column(String, primary_key=True)
    code = Column(String, primary_key=True)
    discount_percent = Column(Float)
    expiry_date = Column(Date)
