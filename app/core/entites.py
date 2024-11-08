import dataclasses
from datetime import datetime
from enum import Enum
from typing import Optional


class Ticker(Enum):
    BTC_USDT = 'BTC_USDT'
    ETH_USDT = 'ETH_USDT'


@dataclasses.dataclass
class Currency:
    ticker: Ticker
    price: float
    timestamp: int
    id: Optional[int] = None
