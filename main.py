from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

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

@app.options("/{path:path}")
async def preflight_handler(path: str):
    return

@app.middleware("http")
async def ensure_https(request: Request, call_next):
    # If request is HTTP, redirect to HTTPS
    if not request.url.scheme == "https":
        url = request.url.replace(scheme="https")
        return RedirectResponse(url=url)
    response = await call_next(request)
    return response

@app.get('/hello')
async def hello_world():
    return 'Hello, World!!!'


app.include_router(CreateMemoItem.router, prefix="/memo/items", tags=["MemoItems"])