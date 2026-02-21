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


#  Day 2 Progress — Data Preprocessing & Baseline Model

##  Data Cleaning
- Cleaned column names
- Removed hidden spaces in categorical values
- Converted `TotalCharges` to numeric format
- Handled missing values using median imputation

##  Feature Engineering
- Encoded target variable (`Churn`) into binary format
- Applied One-Hot Encoding to categorical variables
- Dropped unnecessary column (`customerID`)

##  Data Preparation
- Created stratified train-test split (80-20)
- Applied feature scaling using StandardScaler

##  Baseline Model
- Trained Logistic Regression classifier

##  Model Evaluation
Evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Score

Baseline performance:
- Accuracy: ~78–82%
- ROC-AUC: ~0.82–0.85

---

##  Key Observations
- Dataset shows class imbalance (~26% churn)
- Contract type, tenure, and monthly charges strongly influence churn
- Logistic Regression provides a solid baseline but struggles slightly with recall for churn class

---
