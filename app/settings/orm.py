from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pydantic import MySQLDsn
import os

load_dotenv()
db_config:MySQLDsn = MySQLDsn.build(
    scheme=os.getenv("DB_SCHEME"),
    username=os.getenv("DB_USERNAME"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    path=os.getenv("DB_NAME"),
)
pool_size = int(os.getenv("DB_POOL_SIZE"))
max_overflow = int(os.getenv("DB_MAX_OVERFLOW"))

engine = create_async_engine(db_config.unicode_string(),pool_size=pool_size,max_overflow=max_overflow)

# 创建异步会话工厂
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()