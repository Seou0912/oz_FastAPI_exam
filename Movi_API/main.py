from fastapi import FastAPI
from routers import route

app = FastAPI()

app.include_router(route)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8001, log_level="debug", reload=True)
