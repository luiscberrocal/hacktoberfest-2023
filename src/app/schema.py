from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class House(BaseModel):
    median_house_value: Optional[float]
    median_income: float
    median_age: int
    tot_rooms: int
    tot_bedrooms: int
    population: int
    households: int
    latitude: float
    longitude: float
    distance_to_coast: float
    distance_to_la: float
    distance_to_sandiego: float
    distance_to_sanjose: float
    distance_to_sanfrancisco: float
