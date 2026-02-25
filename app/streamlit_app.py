import streamlit as st
from src.predict import predict_churn
import pandas as pd

st.set_page_config(page_title="CustomerShield AI", layout="wide")

st.title("📊 CustomerShield AI")
st.subheader("Customer Churn Prediction Dashboard")

st.write("Enter customer details to predict churn probability.")