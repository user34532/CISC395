import json
import os
from models import Destination, TripCollection

FILE_PATH = "data.json"


def load_trips():
    if not os.path.exists(FILE_PATH):
        return TripCollection()

    with open(FILE_PATH, "r") as f:
        data = json.load(f)

    trips = TripCollection()

    for item in data:
        dest = Destination(item["name"], item["country"], item["budget"])
        dest.notes = item.get("notes", [])
        dest.visited = item.get("visited", False)
        trips.add(dest)

    return trips


def save_trips(trips):
    data = []

    for trip in trips.get_all():
        data.append({
            "name": trip.name,
            "country": trip.country,
            "budget": trip.budget,
            "notes": trip.notes,
            "visited": trip.visited
        })

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)