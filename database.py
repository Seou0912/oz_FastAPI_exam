from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import sessionmaker

# 동기용 데이터베이스 설정
SQLALCHEMY_DATABASE_URL = "mysql+pymysql: //root:oz-password@localhost/oz-fastapi"

engie = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engie)

# (1) 비동기식 방식 -Starlette
# (2) 데이터 검증 - pydantic

# 비동기용 데잍 베이스 설정 -> aiomysql
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

ASYNC_SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://root:oz-passwd@localhost/oz-fastapi"
async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(bind=async_engine, class_=AsyncSession)

Base = declarative_base()
