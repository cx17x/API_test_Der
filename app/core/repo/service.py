from abc import ABC, abstractmethod

from app.core.entites import Currency


class IServiceCurr(ABC):
    @abstractmethod
    def add_exernal_info(self, tiker: str) -> Currency:
        pass