# CustomerShield

CustomerShield is a machine learning project where I am building a classification model to predict customer churn using the IBM Telco Customer Churn dataset. The goal of this project is to understand customer behavior patterns and develop an AI-based system that can help businesses proactively reduce churn and improve retention strategies.

---

## Problem Statement

Customer churn directly impacts company revenue and growth. Instead of reacting after customers leave, this project focuses on predicting churn in advance using customer demographic and service usage data.

The objective of this project is to:

- Analyze customer behavior and subscription patterns  
- Identify key factors contributing to churn  
- Build machine learning models to classify churn risk  
- Evaluate model performance using proper classification metrics  

---

## Dataset

The project uses the IBM Telco Customer Churn Dataset from Kaggle.

The dataset contains:

- Customer demographic information  
- Service subscription details  
- Contract type and payment method  
- Monthly and total charges  
- Churn label (Yes/No)  

### Dataset Note

The dataset is included inside the `data/` folder for development purposes.

Expected file path:

```
data/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

---

## Project Goals

- Perform data cleaning and preprocessing  
- Conduct exploratory data analysis (EDA)  
- Handle categorical encoding and feature scaling  
- Train machine learning models (Logistic Regression, Random Forest, LightGBM)  
- Evaluate model performance using Accuracy, Precision, Recall, and F1-score  
- Deploy the final model using Streamlit  

---

## Day 1 Progress

- Repository setup  
- Dataset added to data folder  
- Data inspection and type analysis  
- Converted `TotalCharges` to numeric format  
- Missing value analysis  
- Churn distribution analysis  
- Feature relationship visualizations  

---

## Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- LightGBM  
- Matplotlib  
- Seaborn  
- Streamlit (planned deployment)  