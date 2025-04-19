from fastapi import APIRouter

from app.api.navigation.routes import router as routes_router
from app.api.emulation.emulator import router as emulation_router

router = APIRouter()

router.include_router(routes_router, prefix="/navigation")
router.include_router(emulation_router, prefix="/emulation")