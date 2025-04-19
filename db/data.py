import json


def load_file(path):
    with open("./db/data/" + path) as f:
        data = json.load(f)

    return data


class Data:
    def __init__(self):
        self.paths = {
            "buses": "buses.json",
        }

        self.data = {}

        self.load()

    def load(self):
        for p in self.paths:
            self.data[p] = load_file(self.paths[p])
