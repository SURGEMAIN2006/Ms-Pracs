from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Data Prediction Service")

class PredictionInput(BaseModel):
    amount: float
    transaction_count: int

@app.get("/")
def home():
    return {
        "message": "AI Data Service is running"
    }

@app.post("/predict")
def predict(data: PredictionInput):

    score = (data.amount * 0.01) + (data.transaction_count * 5)

    if score >= 50:
        prediction = "High"
    else:
        prediction = "Low"

    return {
        "prediction": prediction,
        "score": round(score, 2)
    }