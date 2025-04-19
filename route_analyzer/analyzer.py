def check_route_is_pedestrian(route):
    is_pedestrian = False
    for r in route:
        if r["pedestrian"]:
            is_pedestrian = True

    return is_pedestrian


def get_route_stops(route):
    stops = []

    for r in route:
        for i in range(len(r["movements"])):
            movement = r["movements"][i]

            if movement["type"] != "passage":
                continue

            geometry = r["movements"][i - 1]["alternatives"][0]["geometry"]
            location = geometry[len(geometry) - 1]["selection"].split(" ")[-2:]
            location = list(reversed([float(loc.replace(")", "")) for loc in location]))

            stops.append({
                "name": movement["waypoint"]["name"],
                "location": location,
                "buses": [rt["names"] for rt in movement["routes"]]
            })

    return stops
