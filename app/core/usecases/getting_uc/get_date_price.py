import dataclasses
from typing import List

from app.core.entites import Ticker, Currency
from app.core.i_for_uc.currency_db_getter import CurrencyDBGetter
from app.core.usecase import IUseCase


@dataclasses.dataclass
class GetByIntervalDTO:
    ticker: Ticker
    time_from: int
    time_to: int


class GetByIntervalUC(IUseCase):
    def __init__(self, curr_repo: CurrencyDBGetter):
        self.curr_db = curr_repo

    async def execute(self, dto: GetByIntervalDTO) -> List[Currency]:
        result = await self.curr_db.get_by_interval(ticker=dto.ticker, time_from=dto.time_from, time_to=dto.time_to)
        return result
