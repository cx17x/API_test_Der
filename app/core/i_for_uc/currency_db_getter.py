from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional, List

from app.core.entites import Currency, Ticker


class CurrencyDBGetter(ABC):
    @abstractmethod
    async def get_list_by_ticker(self, ticker: Ticker) -> List[Currency]:
        pass

    @abstractmethod
    async def get_by_interval(self, ticker: Ticker, time_from: int, time_to: int) -> List[Currency]:
        pass

    @abstractmethod
    async def get_last_by_ticker(self, ticker: Ticker) -> Currency:
        pass
