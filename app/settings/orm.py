from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


engine = create_async_engine("mysql+aiomysql://root:a198man204@127.0.0.1:3306/study_system",pool_size=10,max_overflow=20)


# 创建异步会话工厂
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with async_session_factory() as session:
        try:
            yield session
        finally:
            await session.close()