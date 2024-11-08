import asyncio
import dataclasses
from abc import ABC
from typing import List

from app.core.entites import Ticker, Currency
from app.core.i_for_uc.currency_db_getter import CurrencyDBGetter
from app.core.usecase import IUseCase


@dataclasses.dataclass
class GetAllInfoDTO:
    ticker: Ticker


class GetAllInfoUC(IUseCase):
    def __init__(self, curr_repo: CurrencyDBGetter):
        self.curr_db = curr_repo

    async def execute(self, dto: GetAllInfoDTO) -> List[Currency]:
        result = await self.curr_db.get_list_by_ticker(dto.ticker)
        return result
