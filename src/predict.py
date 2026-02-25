import joblib
import pandas as pd

model = joblib.load("model/lightgbm_churn_model.pkl")
columns = joblib.load("model/feature_columns.pkl")

THRESHOLD = 0.4

def predict_churn(input_data: dict):
    df = pd.DataFrame([input_data])
    df = df.reindex(columns=columns, fill_value=0)

    probability = model.predict_proba(df)[:,1][0]
    prediction = int(probability >= THRESHOLD)

    return prediction, probability