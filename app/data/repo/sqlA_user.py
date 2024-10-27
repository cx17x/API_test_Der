from datetime import datetime

from sqlalchemy.orm import Session
from app.data.model import CurrencyModel
from app.core.entites import Currency
from app.core.repo.user import IUserCurr


class UserRepoBD(IUserCurr):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_info(self, ticker: str) -> Currency:
        pass

    def get_date_price(self, ticker: str, first_date:datetime, last_date: datetime) -> Currency:
        pass

    def get_last_price(self, ticker: str) -> Currency:
        pass