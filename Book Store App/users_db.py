# user_db.py
from db_json import load_users, save_users
from models_db import UserAccount


def find_user_by_email(email, db):
    email = email.strip().lower()
    try:
        user = db.query(UserAccount).filter_by(email=email).first()
        if user:
            return {
                "name": user.name,
                "email": user.email,
                "password": user.password,
                "role": user.role
            }
    except Exception as e:
        print("[DB Error]", e)

    # fallback to JSON
    for u in load_users():
        if u["email"].strip().lower() == email:
            return u
    return None


def add_user(user_dict, db):
    # Step 1: Save to database
    user = UserAccount(
        name=user_dict["name"],
        email=user_dict["email"].strip().lower(),
        password=user_dict["password"],
        role=user_dict.get("role", "customer")
    )
    db.add(user)
    db.commit()

    # Save to JSON
    users = load_users()
    email = user_dict["email"].strip().lower()
    # Avoid duplicate in JSON
    if not any(u["email"].strip().lower() == email for u in users):
        users.append(user_dict)
        save_users(users)
        print(f"[JSON] User added to users_data.json: {email}")


def update_user_password(email, new_password, db):
    email = email.strip().lower()
    user = db.query(UserAccount).filter_by(email=email).first()
    if user:
        user.password = new_password
        db.commit()

    users = load_users()
    for u in users:
        if u["email"].strip().lower() == email:
            u["password"] = new_password
            break
    save_users(users)
