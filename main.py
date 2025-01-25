from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers import CreateMemoItem, GetMemoItems
from app.db.base import Base, engine

app = FastAPI(
    title="Invoice generator backend application",
    description="Invoice generator backend application",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables on app start
Base.metadata.create_all(bind=engine)  # This creates the tables before any requests are processed


@app.options("/{path:path}")
async def preflight_handler(path: str):
    return

@app.get('/hello')
async def hello_world():
    return 'Hello, World!!!'


app.include_router(CreateMemoItem.router, prefix="/memo", tags=["MemoItems"])
app.include_router(GetMemoItems.router, prefix="/memo", tags=["MemoItems"])