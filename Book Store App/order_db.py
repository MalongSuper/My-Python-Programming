from sqlalchemy import Column, String, Float, Integer, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()
DB_PATH = "order.db"

class OrderDB(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True)
    user_email = Column(String)
    book_title = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    total = Column(Float)
    payment_method = Column(String)
    payment_status = Column(String)
    coupon_code = Column(String, nullable=True)
    discount_percent = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

engine = create_engine(f"sqlite:///{DB_PATH}")
SessionLocal = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)

def save_order_to_db(order):
    db = SessionLocal()

    coupon_code = None
    discount_percent = None
    if order.order_coupons:
        coupon = order.order_coupons[0]._OrderCoupon__coupon
        coupon_code = coupon.get_code()
        discount_percent = int(coupon.discount)

    for item in order.order_items:
        db_entry = OrderDB(
            id=order.id,
            user_email=order.customer.email,
            book_title=item.book.title,
            quantity=item.quantity,
            price=item.book.price,
            total=order.total_amount,
            payment_method=order.payment.method if order.payment else "Unknown",
            payment_status=order.payment.status if order.payment else "Pending",
            coupon_code=coupon_code,
            discount_percent=discount_percent,
            created_at=order.date_created
        )
        db.add(db_entry)

    db.commit()
    db.close()



