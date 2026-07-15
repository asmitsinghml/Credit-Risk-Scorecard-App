import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from predict import predict_credit_score


# PAGE CONFIG


st.set_page_config(
    page_title="AI Credit Risk Engine",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# LOAD CSS


try:
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# SIDEBAR


with st.sidebar:

    st.title("🤖 AI Engine")

    st.markdown("---")

    st.success("Credit Risk Scorecard")

    st.write("Version : 1.0")

    st.markdown("---")

    st.info("""
### Model Used

- Logistic Regression
- WOE Encoding
- Scorecard
- Probability of Default
- Credit Score
""")

    st.markdown("---")

    st.caption("Developed by Asmit Singh")

# ==========================
# HEADER
# ==========================

st.markdown(
"""
<h1 style='text-align:center;color:#00F5FF;'>
🤖 AI Credit Risk Engine
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<h4 style='text-align:center;'>
Machine Learning Based Credit Score Prediction
</h4>
""",
unsafe_allow_html=True
)

st.markdown("---")

# LAYOUT


left, right = st.columns([1,1])

# LEFT SIDE

with left:

    st.subheader("📋 Customer Details")

    bureau_score = st.slider(
        "Bureau Score",
        100,
        900,
        650
    )

    annual_income = st.number_input(
        "Annual Income",
        min_value=10000,
        value=500000
    )

    cc_util = st.slider(
        "Credit Utilization (%)",
        0,
        100,
        35
    )

    emp_length = st.slider(
        "Employment Length",
        0,
        40,
        6
    )

    num_ccj = st.number_input(
        "Number of CCJ",
        min_value=0,
        value=0
    )

    max_arrears_12m = st.number_input(
        "Maximum Arrears (12 Months)",
        min_value=0,
        value=0
    )

    months_since_recent_cc_delinq = st.slider(
        "Months Since Recent Delinquency",
        0,
        60,
        12
    )

    predict = st.button(
        "🚀 Predict Credit Score",
        use_container_width=True
    )
    
   
# RIGHT SIDE

with right:

    st.subheader("📊 Prediction Result")

    if predict:

        user_data = {
            "bureau_score": bureau_score,
            "num_ccj": num_ccj,
            "max_arrears_12m": max_arrears_12m,
            "cc_util": cc_util,
            "annual_income": annual_income,
            "emp_length": emp_length,
            "months_since_recent_cc_delinq": months_since_recent_cc_delinq
        }

        result = predict_credit_score(user_data)

        
        # Metric Cards
        

        c1, c2 = st.columns(2)

        with c1:
            st.metric(
                "💳 Credit Score",
                result["Credit Score"]
            )

        with c2:
            st.metric(
                "📉 PD",
                f"{result['PD']} %"
            )

        st.progress(result["PD"] / 100)

       
        # Risk Badge
        

        if "Low" in result["Risk"]:
            st.success(result["Risk"])

        elif "Medium" in result["Risk"]:
            st.warning(result["Risk"])

        else:
            st.error(result["Risk"])

        st.info(result["Decision"])

        # Gauge Chart
    

        fig = go.Figure(go.Indicator(

            mode="gauge+number",

            value=result["Credit Score"],

            title={"text":"Credit Score"},

            gauge={

                "axis":{"range":[300,900]},

                "bar":{"color":"cyan"},

                "steps":[

                    {"range":[300,600],"color":"#ff4d4d"},

                    {"range":[600,750],"color":"#ffd633"},

                    {"range":[750,900],"color":"#00cc66"}

                ]

            }

        ))

        fig.update_layout(

            height=350,

            paper_bgcolor="#0d1117",

            font={"color":"white"}

        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    
        # Download Report

        report = pd.DataFrame({

            "Credit Score":[result["Credit Score"]],

            "Probability of Default":[result["PD"]],

            "Risk":[result["Risk"]],

            "Decision":[result["Decision"]]

        })

        st.download_button(

            "📥 Download Report",

            report.to_csv(index=False),

            file_name="credit_score_report.csv",

            mime="text/csv"

        )
        
        
        
        # AI Recommendation

        st.markdown("---")

        st.subheader("🤖 AI Recommendation")

        if "Approved" in result["Decision"]:

            st.success("""
### ✅ Loan Recommendation

✔ Customer has a strong credit profile.

✔ Low probability of default.

✔ Eligible for loan approval.

✔ Suitable for premium banking products.
""")

        elif "Review" in result["Decision"]:

            st.warning("""
### ⚠ Manual Review Required

• Customer has medium risk.

• Verify income documents.

• Review repayment history.

• Additional verification recommended.
""")

        else:

            st.error("""
### ❌ High Credit Risk

• High probability of default.

• Loan approval not recommended.

• Improve bureau score.

• Reduce credit utilization.
""")

        
        # Customer Summary
        

        st.markdown("---")

        st.subheader("📋 Customer Summary")

        summary = pd.DataFrame({

            "Feature":[
                "Bureau Score",
                "Annual Income",
                "Credit Utilization",
                "Employment Length",
                "Number of CCJ",
                "Maximum Arrears",
                "Months Since Delinquency"
            ],

            "Value":[
                bureau_score,
                annual_income,
                f"{cc_util} %",
                f"{emp_length} Years",
                num_ccj,
                max_arrears_12m,
                months_since_recent_cc_delinq
            ]

        })

        st.dataframe(
            summary,
            use_container_width=True
        )

        # Credit Score Status
        

        if result["Credit Score"] >= 750:

            st.success("🟢 Excellent Credit Score")

        elif result["Credit Score"] >= 650:

            st.warning("🟡 Average Credit Score")

        else:

            st.error("🔴 Poor Credit Score")
            
    st.markdown("---")

st.markdown(
"""
<center>

<h4>🤖 AI Credit Risk Engine</h4>

Developed by <b>Asmit Singh</b>

Machine Learning | Credit Risk Analytics | Scorecard Modeling

© 2026

</center>
""",
unsafe_allow_html=True
)