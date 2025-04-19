from random import randint
from fastapi import APIRouter
import requests
import os

from app.model.location import Location

router = APIRouter()


@router.post("/get_ai_data")
async def get_data_from_ai(data: Location):
    url = os.environ.get("AI_BASE_URL", "http://127.0.0.1/")
    res = requests.post(url, files={
        "media": open("photo.jpg", "rb")
    })
    return res.json()


@router.post("/get_billing_data")
async def get_data_from_billing(data: Location):
    return {
        "count": randint(0, 50),
        "success": True
    }
