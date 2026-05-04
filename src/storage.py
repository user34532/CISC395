import json
import os

DATA_PATH = "data/trips.json"

def load_trips():
    if not os.path.exists(DATA_PATH):
        return []

    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_trips(trips):
    with open(DATA_PATH, "w") as f:
        json.dump(trips, f, indent=2)
