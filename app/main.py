import uvicorn
from fastapi import FastAPI

from infrastructure.routers.router import Router

app = FastAPI()

router = Router()
app.include_router(router.get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
