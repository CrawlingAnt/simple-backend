from sqlmodel import create_engine,SQLModel,Session
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

engine = create_async_engine("mysql+aiomysql://root:a198man204@127.0.0.1:3306/study_system",pool_size=10,max_overflow=20)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# 创建异步会话工厂
async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session():
    async with async_session_factory() as session:
        yield session
