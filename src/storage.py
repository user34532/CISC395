import json
import os
from typing import List
from dataclasses import asdict
from src.models import Destination, TripCollection

DATA_FILE = "data/trips.json"


def load_trips() -> TripCollection:
    collection = TripCollection()

    if not os.path.exists(DATA_FILE):
        return collection

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    for item in data:
        destination = Destination(
            name=item["name"],
            country=item["country"],
            budget=item["budget"],
            notes=item.get("notes", []),
            date_added=item.get("date_added", "")
        )
        collection.add(destination)

    return collection


def save_trips(collection: TripCollection) -> None:
    os.makedirs("data", exist_ok=True)

    data = [asdict(trip) for trip in collection.get_all()]

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)