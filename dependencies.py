from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        try:
            yield db
        finally:
            db.close()


# 비동기용 의존성
from database import AsyncSession


async def get_async_db():
    async with AsyncSession() as session:
        yield session
