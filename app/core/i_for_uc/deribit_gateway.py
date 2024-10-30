from abc import ABC, abstractmethod

from app.core.entites import Currency, Ticker


class DeribitGateway(ABC):
    @abstractmethod
    async def get_curr(self, ticker: Ticker) -> Currency:
        pass

