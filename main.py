from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import CreateMemoItem

app = FastAPI(
    title="Invoice generator backend application",
    description="Invoice generator backend application",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/hello')
async def hello_world():
    return 'Hello, World!!!'

app.include_router(CreateMemoItem.router, prefix="/memo/items", tags=["MemoItems"])