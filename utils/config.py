import sys

HOST = "http://10.1.4.34:8080"

for arg in sys.argv:
    if "--host" in arg:
        HOST = arg.split("=")[1]

HEADERS = {"Content-Type": "application/json"}

BASE_URL = HOST + "/gdo/api"
LOCATIONS_URL = BASE_URL + "/locations/"
LOCATIONS_LIST_URL = BASE_URL + "/locations/list/"
