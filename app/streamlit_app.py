import streamlit as st
from src.predict import predict_churn
import pandas as pd

st.set_page_config(page_title="CustomerShield AI", layout="wide")

st.title("📊 CustomerShield AI")
st.subheader("Customer Churn Prediction Dashboard")

st.write("Enter customer details to predict churn probability.")

tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
online_security = st.selectbox("Online Security", ["Yes", "No"])
tech_support = st.selectbox("Tech Support", ["Yes", "No"])

if st.button("Predict Churn"):

    input_data = {
        "tenure": tenure,
        "MonthlyCharges": monthly_charges,
        # include encoded values depending on your training structure
    }

    prediction, probability = predict_churn(input_data)
    
    st.write("### Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Churn")
    else:
        st.success("✅ Low Risk of Churn")

    st.metric("Churn Probability", f"{probability:.2f}")
    if probability > 0.7:
        st.warning("Very high churn risk. Immediate retention action recommended.")
    elif probability > 0.4:
        st.info("Moderate churn risk. Consider targeted offer.")

