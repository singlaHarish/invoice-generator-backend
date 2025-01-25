from fastapi import Depends
from sqlalchemy.orm import Session

from app.config.logConfig import logger
from app.config.routerConfig import router
from app.db.base import get_db

from app.db.models.memo_details_model import MemoDetails as MemoDetailsModel

@router.get("/items")
def run_query(db: Session = Depends(get_db)):
    db_items = db.query(MemoDetailsModel).all()
    logger.info(f"Memo items are: {len(db_items)}")
    return db_items