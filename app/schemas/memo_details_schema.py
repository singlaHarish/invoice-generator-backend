from typing import List

from pydantic import BaseModel
from datetime import date

from app.schemas.memo_item_schema import MemoItemCreate


class MemoDetailsCreate(BaseModel):
    customerName: str
    address: str
    contact: str
    invoiceDate: date
    memoItems: List[MemoItemCreate]
    billAmount: float
