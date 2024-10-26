import dataclasses
from datetime import datetime

from app.core.UnitOfWork import UnitOfWork
from app.core.usecase import IUseCase
from app.core.usecases.repo.service import IServiceCurr


@dataclasses.dataclass
class AddExternalDTO:
    ticker: str
    price: float
    timestamp: datetime


class AddExternalUC(IUseCase):
    def __init__(self, curr_repo: IServiceCurr, uow: UnitOfWork):
        self.curr_repo = curr_repo
        self.uow = uow

    def execute(self, dto: AddExternalDTO):
        new_currency = self.curr_repo.add_exernal_info(dto)
        self.uow.commit()
        return new_currency
