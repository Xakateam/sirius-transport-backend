from random import randint

import requests

from route_analyzer.sources import sources as data_sources


def check_route_is_pedestrian(route):
    is_pedestrian = False
    for r in route:
        if r["pedestrian"]:
            is_pedestrian = True

    return is_pedestrian


def get_route_stops(route):
    stops = []

    for i in range(len(route)):
        for z in range(len(route[i]["movements"])):
            movement = route[i]["movements"][z]

            if movement["type"] != "passage":
                continue

            geometry = route[i]["movements"][z - 1]["alternatives"][0]["geometry"]
            location = geometry[len(geometry) - 1]["selection"].split(" ")[-2:]
            location = list(reversed([float(loc.replace(")", "")) for loc in location]))

            platform_positions = [
                                     reverse_list(list(map(
                                         float,
                                         pos["geometry"].replace("POINT(", "").replace(")", "").split(" ")))
                                     )
                                     for pos in movement["alternatives"][0]["platforms"]
                                 ][1:-1]

            stops.append({
                "route_id": i,
                "name": movement["waypoint"]["name"],
                "location": location,
                "stops": movement["platforms"]["names"],
                "stops_positions": platform_positions,
                "buses": [rt["names"] for rt in movement["routes"]]
            })

    return stops


def reverse_list(lst):
    return list(reversed(lst))


def get_rating(routes):
    if check_route_is_pedestrian(routes):
        return []

    route_stops = get_route_stops(routes)
    print(route_stops)

    for i in range(len(route_stops)):
        route_stops[i]["busy_rate"] = sum([get_load(loc) for loc in route_stops[i]["stops_positions"]])
    # Assign rating to each stop, and sort DESCENT
    # Check all files for PEP + write documentation
    # Try to connect front + back => make schema for responses (2gis)

    return route_stops


def get_load(location):
    return randint(0, 50)

    # request_pool = [requests.post(u, json={
    #     "location": location
    # }) for u in data_sources]
    #
    # responses = []
    #
    # for u in data_sources:
    #     res = requests.post(u, json={
    #         "location": location
    #     })
    #
    #     responses.append(res.json())
    # return [d["count"] for d in responses][0]
