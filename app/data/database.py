from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from app.data.config import settings

Base = declarative_base()


def create_session_maker():
    db_uri = settings.DATABASE_URL

    if not db_uri:
        raise ValueError("DB_URI env variable is not set")

    engine = create_engine(
        db_uri,
        echo=True
    )
    return sessionmaker(engine, autoflush=False, expire_on_commit=False)


def new_session() -> Session:
    session_maker = create_session_maker()
    with session_maker() as session:
        yield session
