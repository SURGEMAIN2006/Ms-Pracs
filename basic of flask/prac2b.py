
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

water_data = []

class WaterIntake(BaseModel):
    date: str
    amount_liters: float

@app.post("/water/")
def add_water(record: WaterIntake):
    water_data.append(record)
    return {"message": "Water intake saved"}

@app.get("/water/", response_model=List[WaterIntake])
def get_water():
    return water_data
