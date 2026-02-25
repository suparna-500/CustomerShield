import joblib
import pandas as pd

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "model", "lightgbm_churn_model.pkl"))
columns = joblib.load(os.path.join(BASE_DIR, "model", "feature_columns.pkl"))

THRESHOLD = 0.4

def predict_churn(input_data: dict):
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=columns, fill_value=0)

    probability = model.predict_proba(df)[:,1][0]
    prediction = int(probability >= THRESHOLD)

    return prediction, probability