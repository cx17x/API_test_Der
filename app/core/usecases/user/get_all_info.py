import asyncio
import dataclasses
from abc import ABC
from typing import List

from app.core.entites import Ticker, Currency
from app.core.i_for_uc.use_db import IUseCurrDB
from app.core.usecase import IUseCase


@dataclasses.dataclass
class GetAllInfoDTO:
    ticker: Ticker


class GetAllInfoUC(IUseCase):
    def __init__(self, curr_repo: IUseCurrDB):
        self.curr_db = curr_repo

    async def execute(self, dto: GetAllInfoDTO) -> List[Currency]:
        currencies = [self.curr_db.get_all_info(ticket) for ticket in dto.ticker]
        results = await asyncio.gather(*currencies)
        return results
