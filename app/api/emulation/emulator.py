from random import randint
from fastapi import APIRouter

from app.model.location import Location

router = APIRouter()


@router.post("/get_billing_data")
@router.post("/get_ai_data")
async def get_data_from_billing(data: Location):
    return {
        "count": randint(0, 100),
        "success": True
    }
