from sqlalchemy.orm import Session

from app.core.entites import Currency
from app.core.repo.service import IServiceCurr
from app.data.model import CurrencyModel


class ServiceRepoBD(IServiceCurr):
    def __init__(self, db_session: Session):
        self.db = db_session

    def to_entyty(self, currency: CurrencyModel):
        return Currency(
            ticker=currency.ticker,
            price=currency.price,
            timestamp=currency.timestamp
        )

    def to_model(self, currency_entity: Currency):
        return CurrencyModel(
            ticker=currency_entity.ticker,
            price=currency_entity.price,
            timestamp=currency_entity.timestamp
        )

    def add_exernal_info(self, tiker: str) -> Currency:
        pass