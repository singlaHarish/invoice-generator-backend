from pydantic import BaseModel


class MemoItemCreate(BaseModel):
    itemType: str
    itemSubType: str
    ratePerItem: float
    quantity: float
    price: float
