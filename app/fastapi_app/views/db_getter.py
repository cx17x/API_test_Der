from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entites import Ticker
from app.core.exceptions import NotFound
from app.core.usecases.getting_uc.get_all_info import GetAllInfoUC, GetAllInfoDTO
from app.core.usecases.getting_uc.get_date_price import GetByIntervalUC, GetByIntervalDTO
from app.core.usecases.getting_uc.get_last_price import GetLastPriceUC, GetLastPriceDTO
from app.data.database import new_async_session
from app.data.sql_a.sqlA_curr_db_getter import SqlACurrencyDBGetter
from app.fastapi_app.views.schemas import ResponseGetByInterval, ResponseGetLastByTicker, ResponseGetListByTicker

db_getter = APIRouter()


@db_getter.get('/interval')
async def get_by_interval(
        ticker: Ticker = Query(),
        time_from: int = Query(),
        time_to: int = Query(),
        curr_db: AsyncSession = Depends(new_async_session)
) -> List[ResponseGetByInterval]:
    session_db = SqlACurrencyDBGetter(curr_db)
    interval_uc = GetByIntervalUC(curr_repo=session_db)
    dto = GetByIntervalDTO(ticker=ticker, time_from=time_from, time_to=time_to)

    try:
        currencies = await interval_uc.execute(dto=dto)
        return [
            ResponseGetByInterval(
                id=currency.id,
                ticker=currency.ticker,
                price=currency.price,
                timestamp=currency.timestamp
            ) for currency in currencies]
    except NotFound:
        raise HTTPException(status_code=404, detail="not found")


@db_getter.get('/last')
async def get_last_by_ticker(
        ticker: Ticker = Query(),
        curr_db: AsyncSession = Depends(new_async_session)
) -> ResponseGetLastByTicker:
    session_db = SqlACurrencyDBGetter(curr_db)
    last_by_ticker_uc = GetLastPriceUC(curr_repo=session_db)
    dto = GetLastPriceDTO(ticker=ticker)

    try:
        currency = await last_by_ticker_uc.execute(dto=dto)
        return ResponseGetLastByTicker(id=currency.id,
                                       ticker=currency.ticker,
                                       price=currency.price,
                                       timestamp=currency.timestamp)

    except NotFound:
        raise HTTPException(status_code=404, detail="Invalid ticker")


@db_getter.get('/list_tickers')
async def get_list_by_ticker(
        ticker: Ticker = Query(),
        curr_db: AsyncSession = Depends(new_async_session)
) -> List[ResponseGetListByTicker]:
    session_db = SqlACurrencyDBGetter(curr_db)
    last_by_ticker_uc = GetAllInfoUC(curr_repo=session_db)
    dto = GetAllInfoDTO(ticker=ticker)

    try:
        currencies = await last_by_ticker_uc.execute(dto=dto)
        return [ResponseGetListByTicker(
            id=currency.id,
            ticker=currency.ticker,
            price=currency.price,
            timestamp=currency.timestamp
        ) for currency in currencies]

    except NotFound:
        raise HTTPException(status_code=404, detail="Invalid ticker")
