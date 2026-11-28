
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings


async_engin = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URL
)

async_session_maker = async_sessionmaker(autoflush=False, expire_on_commit=False, bind=async_engin)

async def get_database_session():
    async with async_session_maker() as session:
        yield session