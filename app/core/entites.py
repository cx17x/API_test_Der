import dataclasses
from datetime import datetime
from typing import Optional


@dataclasses.dataclass
class Currency:
    ticker: str
    price: float
    timestamp: datetime  ## думаю будет foreign key
