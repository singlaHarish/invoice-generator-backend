from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from mysql.connector import Error
from sqlalchemy.orm import Session

from app.schemas.memo_details_schema import MemoDetailsCreate
from app.db.base import get_db
from app.db.models.memo_details_model import MemoDetails as MemoDetailsModel
from app.db.models.memo_item_model import MemoItem as MemoItemModel

router = APIRouter()


@router.post("/items")
async def create_memo(requestItem: MemoDetailsCreate, db: Session = Depends(get_db)):
    try:
        print("MemoDetailsModel type:", type(MemoDetailsModel))
        date_str = requestItem.invoiceDate
        date_obj = datetime.strptime(date_str, "%m/%d/%Y").date()
        memo_details = MemoDetailsModel(customer_name=requestItem.customerName,
                                        address=requestItem.address,
                                        contact=requestItem.contact,
                                        invoice_date=date_obj,
                                        bill_amount=requestItem.billAmount)

        for memoItem in requestItem.memoItems:
            memo_item = MemoItemModel(item_type=memoItem.itemType, item_subtype=memoItem.itemSubType,
                                      rate_per_item=memoItem.ratePerItem, quantity=memoItem.quantity,
                                      price=memoItem.price)
            memo_details.children.append(memo_item)

        db.add(memo_details)
        db.commit()
        db.refresh(memo_details)
        return {"message": "Data added successfully", "memo_id": memo_details.memo_id}
    except Error as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
