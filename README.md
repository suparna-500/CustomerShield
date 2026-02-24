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


## Day 2 Progress — Data Preprocessing & Baseline Model

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


##  Day 3 Progress — Advanced Modeling with LightGBM


###  Class Imbalance Handling
The dataset contains a lower proportion of churn customers compared to non-churn customers, creating class imbalance.

To improve churn detection:
- Calculated imbalance ratio
- Applied class weighting 
- Prioritized improving recall for churn class

---

###  LightGBM Model Training
- Trained a LightGBM classifier on the preprocessed dataset
- Compared performance with baseline Logistic Regression
- Evaluated using Accuracy, Recall, F1-score, and ROC-AUC

---

###  Key Observations
- LightGBM improved detection of churn customers compared to the baseline model.
- The model demonstrated better sensitivity toward minority class predictions.
- Trade-offs between overall accuracy and churn recall were analyzed.


---

###  Project Evolution
With LightGBM integration, the project now includes:
- Baseline model comparison
- Class imbalance handling
- Boosting-based learning approach
- Business-aligned evaluation strategy

##  Day 4 Progress— Model Optimization & Threshold Strategy

###  Objective
Refine the LightGBM model through hyperparameter tuning and align predictions with business priorities using decision threshold optimization.

---

###  Hyperparameter Tuning

LightGBM hyperparameters were optimized using GridSearchCV with ROC-AUC as the evaluation metric.  

After tuning:
- The model maintained strong ranking performance.
- ROC-AUC remained comparable to the baseline Logistic Regression model.
- The tuned model provided more flexibility in handling churn detection trade-offs.

---

###  Threshold Optimization

Instead of relying on the default 0.5 decision threshold, I analyzed the precision–recall tradeoff across different threshold values.

This allowed me to:

- Increase recall for churn customers
- Adjust the balance between precision and recall
- Align model predictions with business goals

By lowering the threshold, the model was able to identify a significantly higher proportion of churn customers.

---

###  Key Insight

Both Logistic Regression and LightGBM achieved very similar ROC-AUC scores, indicating comparable ranking ability.

However, LightGBM allowed stronger control over churn recall through threshold adjustment.  
This makes it more suitable when the primary goal is minimizing revenue loss by identifying high-risk customers.

---

###  Business Perspective

In churn prediction:

- Missing a churn customer can result in lost revenue.
- Identifying more at-risk customers enables targeted retention strategies.

Model selection is therefore guided not only by accuracy, but by business impact and recall performance.

---

