import asyncio

from app.core.entites import Ticker
from app.core.usecases.add_external_info import AddExternalUC, AddExternalDTO
from app.data.database import new_async_session
from app.data.deribit_aiohttp.aiohttp_ses import get_aiohttp_session
from app.data.deribit_aiohttp.gateaway import AiohttpDeribitGateway
from app.data.sql_a.sqlA_curr_gateway import SqlACurrGateway


async def scheduled_add_extention():
    while True:

        session_gen = get_aiohttp_session()
        aiohttp_session = await session_gen.__anext__()  # Получаем aiohttp-сессию
        db_session_gen = new_async_session()
        async_db_session = await db_session_gen.__anext__()  # Получаем сессию базы данных

        try:

            curr_db = SqlACurrGateway(async_db_session)
            deribit_gateway = AiohttpDeribitGateway(aiohttp_session)
            uow = async_db_session

            add_external_uc = AddExternalUC(curr_db, deribit_gateway, uow)
            tickers = [Ticker('BTC_USDT'), Ticker('ETH_USDT')]
            dto = AddExternalDTO(ticker=tickers)

            result = await add_external_uc.execute(dto)
            print("Scheduled Task Result:", result)

        except Exception as e:
            print(f"Error in scheduled task: {e}")

        finally:

            await session_gen.aclose()
            await db_session_gen.aclose()

        await asyncio.sleep(10)
