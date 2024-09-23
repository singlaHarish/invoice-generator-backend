from typing import List

from pydantic import BaseModel
from datetime import date

from app.models.MemoItem import MemoItem


class MemoDetails(BaseModel):
    invoiceId: int
    customerName: str
    invoiceDate: date
    memoItems: List[MemoItem]
    totalBill: float
