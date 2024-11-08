from pydantic import BaseModel


class MemoItemCreate(BaseModel):
    itemType: str
    itemSubType: str
    ratePerItem: str
    quantity: str
    price: str
