from typing import List

from pydantic import BaseModel

from app.core.entites import Currency, Ticker


class ServiceResponse(BaseModel):
    ticker: Ticker
    price: float
    timestamp: int


class ResponseGetByInterval(BaseModel):
    ticker: Ticker
    price: float
    timestamp: int


class ResponseGetLastByTicker(BaseModel):
    ticker: Ticker
    price: float
    timestamp: int


class ResponseGetListByTicker(BaseModel):
    ticker: Ticker
    price: float
    timestamp: int
