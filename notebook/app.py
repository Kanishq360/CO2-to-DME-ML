from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

co2_package = joblib.load("co2_complete_package.joblib")
dme_package = joblib.load("dme_complete_package.joblib")

co2_model = co2_package["pipeline"]
dme_model = dme_package["pipeline"]

features = co2_package["features"]

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    try:
        df = df[features]
    except:
        return {"error": "Feature mismatch"}

    co2 = co2_model.predict(df)[0]
    dme = dme_model.predict(df)[0]

    return {
        "CO2_Conversion": float(co2),
        "DME_Selectivity": float(dme)
    }
