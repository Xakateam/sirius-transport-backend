from pydantic import BaseModel


# TODO: Check model correctness
class Bus(BaseModel):
    num: str
    weight: int
    period: int
