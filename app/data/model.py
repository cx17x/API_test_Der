from sqlalchemy import Column, Integer, String, DateTime

from app.data.database import Base


class CurrencyModel(Base):
    __tablename__ = 'currency'
    # id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    timestamp = Column(DateTime, primary_key=True)
