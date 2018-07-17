import requests
import json

from utils.config import *


class Locations:
    @staticmethod
    def get_list():
        return requests.get(LOCATIONS_LIST_URL, headers=HEADERS)

    @staticmethod
    def get_by_id(id):
        response = Locations.get_list()
        response_body = response.json()
        for x in response_body:
            if str(x["id"]) == id:
                return x

    @staticmethod
    def get_all():
        return requests.get(LOCATIONS_URL, headers=HEADERS)

    @staticmethod
    def post(data):
        return requests.post(LOCATIONS_URL, headers=HEADERS, data=json.dumps(data))

    @staticmethod
    def put(data, location_id):
        return requests.put(LOCATIONS_URL + str(location_id), headers=HEADERS, data=json.dumps(data))

    @staticmethod
    def delete(location_id):
        return requests.delete(LOCATIONS_URL + str(location_id), headers=HEADERS)


if __name__ == "__main__":
    pass
