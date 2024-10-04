import uvicorn
from api import router as api_router
from fastapi import FastAPI
from core.config import settings

app = FastAPI()
app.router.include_router(
    api_router,
    prefix=settings.api.prefix,
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)