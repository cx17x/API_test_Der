from abc import abstractmethod, ABC
from datetime import datetime
from typing import Optional

from app.core.entites import Currency, Ticker


class IUseCurrDB(ABC):
    @abstractmethod
    async def get_all_info(self, ticker: Ticker) -> Optional[Currency]:
        pass

    @abstractmethod
    async def get_date_price(self, ticker: str, first_date: datetime, last_date: datetime) -> Optional[Currency]:
        pass

    @abstractmethod
    async def get_last_price(self, ticker: str) -> Currency:
        pass
