import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Currency:
    ticker: str
    price: float
    timestamp: datetime  ## думаю будет foreign key
