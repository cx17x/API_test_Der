from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.i_for_uc.curr_db_gateway import CurrencyGatewayDB
from app.core.entites import Currency
from app.data.model import CurrencyModel


class SqlACurrGateway(CurrencyGatewayDB):

    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    async def save(self, currency: Currency) -> None:
        currency_model = CurrencyModel(ticker=currency.ticker, price=currency.price,
                                       datetime=currency.timestamp)
        self.db.add(currency_model)

    async def save_list(self, list_currency: List[Currency]) -> None:
        currency_models = [
            CurrencyModel(ticker=currency.ticker, price=int(currency.price), timestamp=currency.timestamp)
            for currency in list_currency
        ]
        self.db.add_all(currency_models)
