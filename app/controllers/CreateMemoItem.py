from app.models.MemoDetails import MemoDetails
from main import app


@app.post('/memo/items', response_model=MemoDetails)
async def hello_world(memodetails: MemoDetails):
    return memodetails
