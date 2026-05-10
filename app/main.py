from fastapi import FastAPI
import joblib
import numpy as np

from app.schemas import StudentInput

model = joblib.load("model/model.pkl")

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ML Prediction API is running"}


@app.post("/predict")
def predict(data: StudentInput):

    input_data = np.array([[data.hours_studied]])

    prediction = model.predict(input_data)

    return {
        "hours_studied": data.hours_studied,
        "predicted_marks": round(prediction[0], 2)
    }