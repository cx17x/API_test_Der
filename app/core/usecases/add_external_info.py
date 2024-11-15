import dataclasses
from typing import List

import asyncio

from app.core.UnitOfWork import UnitOfWork
from app.core.i_for_uc.curr_db_gateway import CurrencyGatewayDB
from app.core.i_for_uc.deribit_gateway import DeribitGateway
from app.core.entites import Ticker
from app.core.usecase import IUseCase
from app.data.database import new_async_session
from app.data.deribit_aiohttp.aiohttp_ses import get_aiohttp_session
from app.data.deribit_aiohttp.gateaway import AiohttpDeribitGateway
from app.data.sql_a.sqlA_curr_gateway import SqlACurrGateway


@dataclasses.dataclass
class AddExternalDTO:
    ticker: List[Ticker]


class AddExternalUC(IUseCase):
    def __init__(self, curr_db: CurrencyGatewayDB, deribit_gateway: DeribitGateway, uow: UnitOfWork):
        self.curr_db = curr_db
        self.deribit_gateway = deribit_gateway
        self.uow = uow

    async def execute(self, dto: AddExternalDTO):
        currencies = [self.deribit_gateway.get_curr(t) for t in dto.ticker]
        results = await asyncio.gather(*currencies)
        await self.curr_db.save_list(results)
        await self.uow.commit()


# async def main():
#     session_gen = get_aiohttp_session()
#     session = await session_gen.__anext__()
#     s1 = await new_async_session().__anext__()
#     curr_db = SqlACurrGateway(s1)
#     deribit_gateway = AiohttpDeribitGateway(session)
#     uow = s1
#
#     add_external_uc = AddExternalUC(curr_db, deribit_gateway, uow)
#
#     tickers = [Ticker('BTC_USDT'), Ticker('ETH_USDT')]
#     dto = AddExternalDTO(ticker=tickers)
#     await add_external_uc.execute(dto)
#
#
# asyncio.run(main())
