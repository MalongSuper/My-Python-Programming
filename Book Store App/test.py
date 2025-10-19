from sqlalchemy import create_engine
engine = create_engine("sqlite:///user.db")
conn = engine.connect()
result = conn.execute("SELECT * FROM users")
for row in result:
    print(row)
