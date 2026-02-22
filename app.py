import pickle
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import logging

# logging for production
logging.basicConfig(level=logging.INFO)

# load model
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    logging.info("Model loaded successfully")
except Exception as e:
    logging.error("Model loading failed")
    raise e

app = FastAPI(
    title="🏭 CO2 Emission Prediction API",
    description="Predict CO2 emissions from engine size and cylinders",
    version="1.0"
)

# input validation
class InputData(BaseModel):
    engine_size: float = Field(..., gt=0, description="Engine size must be > 0")
    cylinders: int = Field(..., gt=0, description="Cylinders must be > 0")


@app.get("/")
def home():
    return {"status": "API running", "model": "CO2 predictor"}


@app.get("/health")
def health():
    return {"health": "ok"}


@app.post("/predict")
def predict(data: InputData):

    try:
        input_df = pd.DataFrame(
            [[data.engine_size, data.cylinders]],
            columns=["ENGINE SIZE", "CYLINDERS"]
        )

        prediction = model.predict(input_df)[0]

        return {
            "Predicted_CO2": round(prediction, 2)
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))