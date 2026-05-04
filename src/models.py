from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Trip:
    name: str
    notes: list = field(default_factory=list)


@dataclass
class Destination:
    name: str
    country: str
    budget: float
    notes: list = field(default_factory=list)
    date_added: str = ""

    def __post_init__(self):
        if not self.date_added:
            self.date_added = datetime.now().strftime("%Y-%m-%d")

    def add_note(self, note):
        self.notes.append(note)


class TripCollection:
    def __init__(self):
        self.trips = []

    def add(self, trip):
        self.trips.append(trip)

    def get_trips(self):
        return self.trips

    def get_all(self):
        return self.trips

    def get_by_index(self, index):
        return self.trips[index]

    def search_by_country(self, country):   # ✅ FINAL METHOD
        return [t for t in self.trips if t.country.lower() == country.lower()]

    def __len__(self):
        return len(self.trips)
