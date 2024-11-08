from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.data.config import settings

Base = declarative_base()


def create_async_session_maker():
    db_uri = settings.DATABASE_URL

    if not db_uri:
        raise ValueError("DB_URI env variable is not set")

    async_engine = create_async_engine(db_uri)

    asinc_engine = async_sessionmaker(
        async_engine,
        expire_on_commit=False,
        class_=AsyncSession,
        autocommit=False,
        autoflush=False
    )
    return asinc_engine


async def new_async_session() -> AsyncSession:
    session_maker = create_async_session_maker()
    async with session_maker() as session:
        yield session

