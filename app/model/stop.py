from typing import List

from pydantic import BaseModel

from app.model.bus import Bus


# TODO: Check model correctness
class Stop(BaseModel):
    uuid: str
    lat: float
    lon: float
    weight: int
    name: str
    reverse: bool
