from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

from app.data.config import settings

Base = declarative_base()


def create_async_session_maker():
    db_uri = settings.DATABASE_URL

    if not db_uri:
        raise ValueError("DB_URI env variable is not set")

    asinc_engine = create_async_engine(
        db_uri,
        echo=True
    )
    return async_sessionmaker(asinc_engine, autoflush=False, expire_on_commit=False)


async def new_async_session() -> AsyncSession:
    session_maker = create_async_session_maker()
    async with session_maker() as session:
        yield session
