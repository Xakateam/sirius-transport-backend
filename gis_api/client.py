import os
import requests


class GisAPIClient:
    def __init__(self):
        # 115a9176-502d-412d-ab6d-0e6c9d02a968
        self.api_key = os.environ.get("GIS_API_KEY")
        if not self.api_key:
            print("No 2GIS API key specified")

            raise KeyError

        self.base_url = os.environ.get("GIS_API_BASE_URL", "https://routing.api.2gis.com/")

    def get_route(self, source, target):
        response = self.call("public_transport/2.0", {
            "locale": "ru",
            "source":
                {
                    "name": "dot_a",
                    "point":
                        {
                            "lat": source[0],
                            "lon": source[1]
                        }
                },
            "target":
                {
                    "name": "dot_b",
                    "point":
                        {
                            "lat": target[0],
                            "lon": target[1]
                        }
                },
            "transport": ["bus"]
        })

        return response

    def call(self, method, params):
        request = requests.post(self.base_url + method + "?key=" + self.api_key, json=params)

        return request.json()
