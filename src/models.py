from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class Destination:
    name: str
    country: str
    budget: float
    notes: List[str] = field(default_factory=list)
    date_added: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    visited: bool = False

    def add_note(self, note: str):
        self.notes.append(note)


class TripCollection:
    def __init__(self):
        self._trips: List[Destination] = []

    def add(self, destination: Destination):
        self._trips.append(destination)

    def get_all(self) -> List[Destination]:
        return self._trips

    def search_by_country(self, country: str) -> List[Destination]:
        return [trip for trip in self._trips if trip.country.lower() == country.lower()]

    def get_by_index(self, index: int) -> Destination:
        return self._trips[index]

    def __len__(self):
        return len(self._trips)

    def get_wishlist(self):
        return [trip for trip in self._trips if not trip.visited]

    def get_visited(self):
        return [trip for trip in self._trips if trip.visited]

    def mark_visited(self, index: int):
        self._trips[index].visited = True