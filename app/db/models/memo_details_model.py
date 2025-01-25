from sqlalchemy.orm import relationship

from app.db.base import Base, engine
from sqlalchemy import Column, Integer, String, Date, Float


class MemoDetails(Base):
    __tablename__ = "MEMO_DETAILS"

    memo_id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(100), nullable=False)
    address = Column(String(200), nullable=False)
    contact = Column(String(50), nullable=False)
    invoice_date = Column(Date, nullable=False)
    bill_amount = Column(Float, nullable=False)

    children = relationship("MemoItem", back_populates="parent", cascade="all, delete-orphan")


# # Create the database tables
# Base.metadata.create_all(bind=engine)