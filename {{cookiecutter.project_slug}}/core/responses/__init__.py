from dataclasses import dataclass
from typing import Any


@dataclass
class ResponseObject:
    data: Any = None
    meta: Any = None
    code: int = None
