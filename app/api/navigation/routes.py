from fastapi import APIRouter

from app.model.route import Route
from route_analyzer.analyzer import get_rating
from gis_api.client import GisAPIClient

router = APIRouter()

gis_api = GisAPIClient()


@router.post("/get")
async def get_route(route: Route):
    response = get_rating(gis_api.get_route(route.geo_from, route.geo_to))

    return {
        "data": response
    }
