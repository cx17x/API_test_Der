from abc import ABC, abstractmethod
from typing import List

from app.core.entites import Currency


class CurDBGateway(ABC):
    @abstractmethod
    async def save(self, currency: Currency) -> None:
        pass

    @abstractmethod
    async def save_list(self, list_currency: List[Currency]) -> None:
        pass
