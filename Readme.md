# Credit Risk Scorecard Application

## Project Overview

This project implements an End-to-End Credit Risk Scorecard Model using Logistic Regression and Weight of Evidence (WOE) transformation techniques. The application predicts customer creditworthiness by estimating the Probability of Default (PD), generating a Credit Score, and classifying applicants based on their risk profile.

The model follows the industry-standard Credit Risk Modelling workflow used in Banking and Financial Institutions for retail lending decisions.

---

## Features

- Credit Risk Assessment
- Probability of Default (PD) Prediction
- WOE Based Feature Transformation
- Logistic Regression Scorecard Model
- Credit Score Generation
- Risk Classification
- Interactive Streamlit Application
- Real-Time Prediction Pipeline

---

## Project Workflow

```
Raw Customer Data
        ↓
Data Preprocessing
        ↓
WOE Transformation
        ↓
Logistic Regression Model
        ↓
Probability of Default (PD)
        ↓
Score Scaling
        ↓
Credit Score Generation
        ↓
Risk Classification
        ↓
Final Credit Decision
```

---

## Credit Risk Modelling Process

The scorecard model follows the standard Credit Risk Modelling framework:

- Data Preparation
- Segmentation
- Weight of Evidence (WOE) Transformation
- Logistic Regression Modelling
- Probability of Default Estimation
- Score Scaling
- Scorecard Development
- Credit Score Calculation
- Risk Classification
- Final Prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Logistic Regression
- Credit Risk Modelling
- WOE Transformation
- Scorecard Development
- Pickle Serialization

---

## Project Structure

```
scorecard_app/

│── app.py
│── predict.py
│
│── model.pkl
│── scorecard.pkl
│── coef_df.pkl
│── config.pkl
│── woe_transformers.pkl
│
│── requirements.txt
│── style.css
│── README.md
```

---

## Model Components

| Component | Description |
|----------|-------------|
| model.pkl | Trained Logistic Regression Model |
| scorecard.pkl | Final Scorecard Mapping |
| config.pkl | Score Scaling Configuration |
| coef_df.pkl | Model Coefficients |
| woe_transformers.pkl | WOE Transformation Objects |
| predict.py | Prediction Pipeline |
| app.py | Streamlit Application |

---

## Installation

Clone the repository

```bash
git clone YOUR_REPOSITORY_LINK
```

Move inside the project directory

```bash
cd Credit-Risk-Scorecard-App
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Model Output

The application provides:

- Probability of Default (PD)
- Credit Score
- Credit Status Prediction
- Risk Classification
- Customer Summary Report

---

## Business Use Case

This project can be used for:

- Credit Approval Decisions
- Retail Lending
- Consumer Loan Assessment
- Customer Risk Profiling
- Financial Risk Management
- Banking Scorecard Modelling

---

## Future Improvements

- KS Statistics Analysis
- ROC-AUC Visualization
- Score Distribution Analysis
- Decile Analysis
- Basel Framework Integration
- IFRS-9 Implementation
- Expected Credit Loss (ECL) Modelling

---

## Author

### Asmit Singh

- B.Tech (CSE)
- Credit Risk Modelling Enthusiast
- Machine Learning & Data Science
