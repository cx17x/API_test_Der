from typing import List

import aiohttp
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.UnitOfWork import UnitOfWork
from app.core.entites import Ticker
from app.core.usecases.add_external_info import AddExternalUC, AddExternalDTO
from app.data.database import new_async_session
from app.data.deribit_aiohttp.aiohttp_ses import get_aiohttp_session
from app.data.deribit_aiohttp.gateaway import AiohttpDeribitGateway
from app.data.sql_a.sqlA_curr_gateway import SqlACurrGateway
from app.fastapi_app.views.schemas import ServiceResponse

service_router = APIRouter()


async def add_extention(curr_db: AsyncSession = Depends(new_async_session),
                        aiohttp_session: aiohttp.ClientSession = Depends(get_aiohttp_session)
                        ) -> List[ServiceResponse]:
    deribit_gateway = AiohttpDeribitGateway(aiohttp_session)
    session_db = SqlACurrGateway(curr_db)

    add_extention_uc = AddExternalUC(curr_db=session_db, deribit_gateway=deribit_gateway, uow=curr_db)
    tickers = [Ticker('BTC_USDT'), Ticker('ETH_USDT')]
    dto = AddExternalDTO(ticker=tickers)

    result = await add_extention_uc.execute(dto=dto)

    return result
