from datetime import datetime

from sqlalchemy.orm import Session
from app.data.model import CurrencyModel
from app.core.entites import Currency
from app.core.i_for_uc.use_db import IUseCurrDB


class UserRepoBD(IUseCurrDB):
    def __init__(self, db_session: Session):
        self.db = db_session

    async def get_all_info(self, ticker: str) -> Currency:
        pass

    async def get_date_price(self, ticker: str, first_date: datetime, last_date: datetime) -> Currency:
        pass

    async def get_last_price(self, ticker: str) -> Currency:
        product_model = self.db.query(CurrencyModel).get(ticker)
        if product_model is not None:
            return self._model_to_entity(product_model)
        raise NotFound