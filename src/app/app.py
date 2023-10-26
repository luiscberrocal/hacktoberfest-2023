from fastapi import FastAPI

from src.app.schema import House

app = FastAPI()


@app.get("/")
def main_end_point() -> House:
    house_data = {
        "median_income": 3.87,
        "median_age": 28.6,
        "tot_rooms": 5,
        "tot_bedrooms": 3,
        "population": 1425,
        "households": 500,
        "latitude": 35.6,
        "longitude": -119.56,
        "distance_to_coast": 40_509.3,
        "distance_to_la": 269_422,
        "distance_to_sandiego": 398_000,
        "distance_to_sanjose": 34_000.0,
        "distance_to_sanfrancisco": 346_000.0
    }
    house = House(**house_data)
    return house


@app.post("/predict")
def predict_house_price(house: House) -> House:
    return house
