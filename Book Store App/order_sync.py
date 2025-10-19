from db_setup import Base, engine, SessionLocal
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class OrderDB(Base):
    __tablename__ = 'orders'
    id = Column(String, primary_key=True)
    customer_email = Column(String)
    total = Column(Float)
    payment_status = Column(String)
    payment_method = Column(String)
    payment_id = Column(String)
    date_created = Column(DateTime, default=datetime.now)

class OrderItemDB(Base):
    __tablename__ = 'order_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(String, ForeignKey("orders.id"))
    title = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

def save_order_to_db(order):
    db = SessionLocal()
    db_order = OrderDB(
        id=order.id,
        customer_email=order.customer.email,
        total=order.total_amount,
        payment_status=order.payment_status,
        payment_method=order.payment.method,
        payment_id=order.payment.payment_id,
        date_created=order.date_created
    )
    db.add(db_order)
    db.commit()

    for item in order.order_items:
        db_item = OrderItemDB(
            order_id=order.id,
            title=item.book.title,
            price=item.book.price,
            quantity=item.quantity
        )
        db.add(db_item)

    db.commit()
    db.close()
