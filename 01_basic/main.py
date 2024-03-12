from fastapi import FastAPI
from items import router as items_router
from users import router as users_router
from async_sync_test import router as async_sync_test_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)
app.include_router(async_sync_test_router)

# @app.get("/")
# def index():
#     return {"Hello": "World!"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, query: str = None):
#     data = {"item_id": item_id, "query": query}
#     return data


# 실행방법:
# - uvicorn main:app --reload

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", port=8000, log_level="debug", reload=True)
    # python main.py
