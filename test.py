from route_analyzer.analyzer import *
from gis_api.client import GisAPIClient

gis_api = GisAPIClient()

# 43.402440, 39.963147
# 43.411328, 39.947022
# print(get_route_stops(gis_api.get_route([43.402440, 39.963147], [43.411328, 39.947022])))
print(get_rating(gis_api.get_route([43.402440, 39.963147], [43.411328, 39.947022])))
