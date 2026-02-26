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

##  Day 5 — Model Explainability with SHAP

###  What I Worked On

After tuning and optimizing the LightGBM model, I focused on understanding *why* the model makes certain churn predictions.

Instead of treating the model as a black box, I used SHAP (SHapley Additive exPlanations) to interpret both global feature importance and individual customer predictions.

This step makes the model more transparent and business-friendly.

---

###  Global Feature Interpretation

Using SHAP summary and bar plots, I identified the most influential features driving churn predictions.

Key observations:

- Customers with month-to-month contracts show higher churn risk.
- Lower tenure significantly increases churn probability.
- Higher monthly charges are associated with increased churn likelihood.
- Lack of online security and tech support increases churn risk.

This confirms that contract type, service support, and pricing structure strongly impact customer retention.

---

###  Individual Prediction Explanation

I also generated SHAP waterfall plots to explain individual customer predictions.

This helped visualize:

- Which features pushed the prediction toward churn.
- Which features reduced churn probability.
- How different variables interact to influence final output.

This allows the model to provide not just predictions, but explanations.

---

###  Why This Matters

Model performance is important, but explainability builds trust.

With SHAP analysis, the project now:

- Identifies key churn drivers
- Supports data-driven retention strategies
- Provides interpretable and actionable insights
- Moves beyond prediction into decision support

---

###  Project Progress So Far

By Day 5, the project now includes:

- Baseline Logistic Regression model
- Tuned LightGBM model
- Threshold optimization
- Model comparison using ROC-AUC
- Business-focused recall improvement
- SHAP-based explainability analysis

This transforms the project from a simple classification task into a strategic churn prediction system.

---

###  Business Perspective

In churn prediction:

- Missing a churn customer can result in lost revenue.
- Identifying more at-risk customers enables targeted retention strategies.

Model selection is therefore guided not only by accuracy, but by business impact and recall performance.

---

##  Day 6 — Deployment & Dashboard

###  Focus

Today I moved the project from experimentation to production readiness.

Instead of just training models in notebooks, I packaged the final solution so it can be reused and deployed.

---

###  Final Model

The tuned LightGBM model was selected as the final production model due to its strong churn recall and flexibility through threshold tuning.

---

###  Model Packaging

- Saved trained model using `joblib`
- Saved preprocessing artifacts (feature columns and scaler if used)
- Created a reusable prediction function inside `src/predict.py`

This ensures consistent and reproducible predictions outside the notebook.

---

###  Streamlit Dashboard

Built an interactive Streamlit app where users can:

- Enter customer details  
- Generate churn prediction  
- View churn probability  
- See risk classification  

The dashboard connects directly to the production prediction pipeline.

---

###  Outcome

By Day 6, the project now includes:

- Final optimized model  
- Modular prediction pipeline  
- Interactive web dashboard  
- Clean production-ready structure  

The project has evolved from a notebook-based model into a usable churn prediction product.


##  Day 7 — Final Polishing & Project Completion

###  Focus

Day 7 was dedicated to refining the project, improving presentation quality, and preparing it for final submission.

The goal was not to add more models, but to polish, structure, and present the system professionally.

---

###  Dashboard Refinement

The Streamlit application was improved to provide:

- Clean two-column layout  
- Organized sections (Account Information & Service Details)  
- Clear call-to-action button  
- Risk classification (High / Low)  
- Churn probability display  
- Business-oriented interpretation message  

This transformed the model into a user-friendly churn prediction tool.

---

###  End-to-End Workflow

By Day 7, the project includes:

- Data preprocessing & feature engineering  
- Logistic Regression baseline model  
- Tuned LightGBM model  
- Threshold optimization for business alignment  
- SHAP explainability analysis  
- Production-ready model packaging  
- Modular prediction pipeline  
- Interactive Streamlit dashboard  

The workflow now covers the full ML lifecycle — from data exploration to deployment.

---

###  Repository Cleanup

- Organized folders into a production-ready structure  
- Verified model artifacts are properly stored  
- Cleaned unused files  
- Updated requirements.txt  
- Structured README for clarity  

---

###  Final Outcome

CustomerShield AI is now:

- A complete churn prediction system  
- Optimized for recall and business impact  
- Interpretable using SHAP  
- Packaged for deployment  
- Interactive and demo-ready  

This project demonstrates not just model building, but real-world machine learning implementation and deployment thinking.