import aiohttp
import app.data.deribit_aiohttp.urls as urls
from app.core.i_for_uc.deribit_gateway import DeribitGateway
from app.core.entites import Ticker, Currency


class AiohttpDeribitGateway(DeribitGateway):
    def __init__(self, http_sess: aiohttp.ClientSession):
        self.http_session = http_sess

    async def get_curr(self, ticker: Ticker) -> Currency:
        url = urls.BASE_URL + urls.GET_TICKET + f'?instrument_name={ticker.name}'
        async with self.http_session.get(url) as response:
            data = await response.json()
            print(data)

        return Currency(ticker=data["result"]["instrument_name"],
                        price=data["result"]["index_price"],
                        timestamp=data["result"]["timestamp"])


# print(urls.BASE_URL + urls.GET_TICKET + f'?instrument_name=ETH_USDT')
