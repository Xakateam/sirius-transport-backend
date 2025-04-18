from pydantic import BaseModel

class Bus(BaseModel):
    num: str
    weight: int
    period: int
