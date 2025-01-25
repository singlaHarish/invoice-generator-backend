import logging
import sys

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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)


@app.options("/{path:path}")
async def preflight_handler(path: str):
    return

@app.get('/hello')
async def hello_world():
    return 'Hello, World!!!'


app.include_router(CreateMemoItem.router, prefix="/memo", tags=["MemoItems"])