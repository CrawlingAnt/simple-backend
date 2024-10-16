from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.common.utils import db_url, pool_size, max_overflow

engine = create_async_engine(db_url, pool_size=pool_size, max_overflow=max_overflow)

# 创建异步会话工厂
async_session_factory = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session():
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()
