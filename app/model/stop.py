from pydantic import BaseModel



# TODO: Check model correctness
class Stop(BaseModel):
    uuid: str
    lat: float
    lon: float
    weight: int
    name: str
    reverse: bool
