from pydantic import BaseModel


class MemoItem(BaseModel):
    itemType: str
    itemSubType: str
    pricePerQuantity: float
    quantity: float
    total: float
