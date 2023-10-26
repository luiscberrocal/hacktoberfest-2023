import pickle
from pathlib import Path

import pandas as pd
from fastapi import FastAPI

from src.app.schema import House

app = FastAPI()
model_file = Path(__file__).parent.parent / 'data' / 'regression_model.pickle'
with open(model_file, "rb") as f:
    REGRESSION_MODEL = pickle.load(f)


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
def predict_house_price(house: House) -> float:
    X_to_predict = pd.DataFrame.from_records([house.dict(exclude={"median_house_value"})])
    y_pred_pickled = REGRESSION_MODEL.predict(X_to_predict)
    return y_pred_pickled[0]
