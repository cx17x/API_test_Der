import dataclasses
from datetime import datetime
from enum import Enum
from typing import Optional


class Ticker(Enum):
    BTC_USDT = 'btc_usdt'
    ETH_USDT = 'eth_usdt'


@dataclasses.dataclass
class Currency:
    ticker: Ticker
    price: float
    timestamp: int
    id: Optional[int] = None
