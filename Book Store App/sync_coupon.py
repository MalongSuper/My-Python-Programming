import json
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Paths
DB_PATH = "coupon.db"
JSON_PATH = "coupon.json"

# SQLAlchemy setup
Base = declarative_base()

class CouponAccount(Base):
    __tablename__ = "coupons"
    user_email = Column(String, primary_key=True)
    code = Column(String, primary_key=True)
    discount_percent = Column(Float)
    expiry_date = Column(Date)

# Connect to database
engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

# Drop and recreate table
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Load coupons from JSON
if not os.path.exists(JSON_PATH):
    print("coupon.json not found.")
    exit()

with open(JSON_PATH, "r") as f:
    coupons = json.load(f)

# Sync data
db = SessionLocal()
added = 0
for c in coupons:
    try:
        expiry = datetime.strptime(c["expiry_date"], "%Y-%m-%d").date()
        db.add(CouponAccount(
            user_email=c["user_email"],
            code=c["code"],
            discount_percent=c["discount_percent"],
            expiry_date=expiry
        ))
        added += 1
        print(f"Synced coupon for {c['user_email']}: {c['code']}")
    except Exception as e:
        print(f"Error syncing coupon for {c.get('user_email')}: {e}")

db.commit()
db.close()
print(f"\nSync complete: {added} coupons added.")

