from typing import List

from pydantic import BaseModel

from app.model.bus import Bus


class Stop(BaseModel):
    lat: float
    lon: float
    weight: int
    name: str
    reverse: bool
    buses: List[Bus]
