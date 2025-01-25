from sqlalchemy.orm import relationship

from app.db.base import Base, engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class MemoItem(Base):
    __tablename__ = "MEMO_ITEM"

    memo_item_id = Column(Integer, primary_key=True, index=True)
    item_type = Column(String(200), nullable=False)
    item_subtype = Column(String(200), nullable=False)
    rate_per_item = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False)
    fk_memo_details_id = Column(Integer, ForeignKey("MEMO_DETAILS.memo_id", ondelete="CASCADE"), nullable=False)

    parent = relationship("MemoDetails", back_populates="children")


# # Create the database tables
# Base.metadata.create_all(bind=engine)