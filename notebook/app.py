from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

# =========================================
# LOAD ALL MODELS
# =========================================

co2_package = joblib.load("co2_complete_package.joblib")
dme_package = joblib.load("dme_complete_package.joblib")
methanol_package = joblib.load("methanol_complete_package.joblib")
co_package = joblib.load("co_complete_package.joblib")

co2_model = co2_package["pipeline"]
dme_model = dme_package["pipeline"]
methanol_model = methanol_package["pipeline"]
co_model = co_package["pipeline"]

# Use consistent features
features = co2_package["features"]

# =========================================
# HOME
# =========================================

@app.get("/")
def home():
    return {"message": "API Running 🚀"}

# =========================================
# PREDICT
# =========================================

@app.post("/predict")
def predict(data: dict):
    df = pd.DataFrame([data])

    try:
        df = df[features]
    except:
        return {"error": "Feature mismatch"}

    co2 = co2_model.predict(df)[0]
    dme = dme_model.predict(df)[0]
    methanol = methanol_model.predict(df)[0]
    co_val = co_model.predict(df)[0]

    return {
        "CO2_Conversion": float(co2),
        "DME_Selectivity": float(dme),
        "Methanol_Selectivity": float(methanol),
        "CO_Selectivity": float(co_val)
    }
