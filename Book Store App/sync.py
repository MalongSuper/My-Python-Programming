# sync_json_to_db.py
import json
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, UserAccount

# File paths
DB_PATH = "users.db"
JSON_PATH = "templates/users_data.json"

# Setup database
engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)

# Step 1: Force recreate the table (drop + create)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# Step 2: Load JSON
if not os.path.exists(JSON_PATH):
    print("users_data.json not found.")
    exit()

with open(JSON_PATH, "r") as file:
    users = json.load(file)

# Step 3: Insert into DB
added = 0
skipped = 0
db = SessionLocal()
for u in users:
    email = u["email"].strip().lower()
    existing = db.query(UserAccount).filter_by(email=email).first()

    if not existing:
        db.add(UserAccount(
            name=u["name"],
            email=email,
            password=u["password"],
            role=u.get("role", "customer")
        ))
        added += 1
        print(f"Added: {email}")
    else:
        skipped += 1
        print(f"Skipped (already exists): {email}")

db.commit()
db.close()

print(f"\nSync complete: {added} added, {skipped} skipped.")

