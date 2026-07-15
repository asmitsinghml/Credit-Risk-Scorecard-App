import joblib
import pandas as pd
import numpy as np

# Load Saved Files

model = joblib.load("model.pkl")
woe_transformers = joblib.load("woe_transformers.pkl")
coef_df = joblib.load("coef_df.pkl")
config = joblib.load("config.pkl")

factor = config["factor"]
base_points = config["base_points"]

# BUSINESS RULES

APPROVE_SCORE = 750
REVIEW_SCORE = 650

APPROVE_PD = 0.05
REVIEW_PD = 0.10


# Prediction Function

def predict_credit_score(user_input):

    # Convert user input into DataFrame
    df = pd.DataFrame([user_input])

   
    # WOE Transformation
    X_woe = pd.DataFrame()

    for feature in df.columns:
        X_woe[feature] = woe_transformers[feature].transform(
            df[feature],
            metric="woe"
        )

    # Probability of Default
    pd_value = model.predict_proba(X_woe)[0][1]

    # Credit Score Calculation
    score_df = X_woe.copy()

    for feature in coef_df["Feature"]:

        coef = coef_df.loc[
            coef_df["Feature"] == feature,
            "Coefficient"
        ].values[0]

        score_df[feature] = (
            -score_df[feature]
            * coef
            * factor
        )

    credit_score = score_df.sum(axis=1).iloc[0] + base_points


    
    # HYBRID DECISION ENGINE
    

    if credit_score >= APPROVE_SCORE:

        if pd_value <= APPROVE_PD:

            risk = "Low Risk"
            decision = "Approved"

        else:

            risk = "Medium Risk"
            decision = "Review Required"


    elif credit_score >= REVIEW_SCORE:

        if pd_value <= REVIEW_PD:

            risk = "Medium Risk"
            decision = "Review Required"

        else:

            risk = "High Risk"
            decision = "Rejected"


    else:

        risk = "High Risk"
        decision = "Rejected"


    
    # RETURN OUTPUT
    

    return {

        "Credit Score": round(credit_score),

        "PD": round(pd_value * 100, 2),

        "Risk": risk,

        "Decision": decision

    }


# Test (Run only if this file is executed directly)


if __name__ == "__main__":

    sample = {
        "bureau_score": 650,
        "num_ccj": 0,
        "max_arrears_12m": 0,
        "cc_util": 35,
        "annual_income": 500000,
        "emp_length": 6,
        "months_since_recent_cc_delinq": 12
    }

    result = predict_credit_score(sample)

    print(result)