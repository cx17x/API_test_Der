from abc import abstractmethod, ABC
from datetime import datetime

from app.core.entites import Currency


class IUserCurr(ABC):
    @abstractmethod
    def get_all_info(self, ticker: str) -> Currency:
        pass

    @abstractmethod
    def get_date_price(self, ticker: str, first_date:datetime, last_date: datetime) -> Currency:
        pass

    @abstractmethod
    def get_last_price(self, ticker: str) -> Currency:
        pass
