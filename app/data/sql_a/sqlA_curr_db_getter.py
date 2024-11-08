import asyncio
from typing import List

from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.entites import Currency, Ticker
from app.core.i_for_uc.currency_db_getter import CurrencyDBGetter
from app.data.database import new_async_session
from app.data.model import CurrencyModel


class SqlACurrencyDBGetter(CurrencyDBGetter):
    def __init__(self, db_session: AsyncSession):
        self.db = db_session

    def entity_to_model(self, currency: Currency):
        return CurrencyModel(
            id=currency.id,
            ticker=currency.ticker.value,
            price=currency.price,
            timestamp=currency.timestamp
        )

    def model_to_entity(self, currence_model: CurrencyModel):
        return Currency(
            id=currence_model.id,
            ticker=Ticker(currence_model.ticker),
            price=currence_model.price,
            timestamp=currence_model.timestamp
        )

    async def get_by_interval(self, ticker: Ticker, time_from: int, time_to: int) -> List[Currency]:
        query = select(CurrencyModel).where(
            (CurrencyModel.ticker == ticker.value) &
            (CurrencyModel.timestamp >= time_from) &
            (CurrencyModel.timestamp <= time_to))
        result = await self.db.execute(query)
        currency_models = result.scalars().all()
        return [self.model_to_entity(currency_model) for currency_model in currency_models]

    async def get_last_by_ticker(self, ticker: Ticker) -> Currency:
        query = select(CurrencyModel).where(CurrencyModel.ticker == ticker.value).order_by(
            desc(CurrencyModel.timestamp)).limit(1)
        result = await self.db.execute(query)
        currency_model = result.scalar_one_or_none()
        return self.model_to_entity(currency_model) if currency_model else None

    async def get_list_by_ticker(self, ticker: Ticker) -> List[Currency]:
        query = select(CurrencyModel).where(CurrencyModel.ticker == ticker.value)
        result = await self.db.execute(query)
        currency_models = result.scalars().all()
        return [self.model_to_entity(currency_model) for currency_model in currency_models]


async def main():
    async for s1 in new_async_session():
        repo = SqlACurrencyDBGetter(s1)
        ticker = Ticker('BTC_USDT')
        # currencies = await repo.get_list_by_ticker(ticker=ticker)
        # currencies = await repo.get_last_by_ticker(ticker=ticker)
        # currencies = await repo.get_by_interval(ticker=ticker, time_from=1730308000000, time_to=2730318646329,)
        # print(currencies)


asyncio.run(main())
