"""
Late Leaf Spot Disease Prediction – Groundnut
---------------------------------------------
Developed by: Kishor Kumar
Year: 2026
Description:
This web application predicts Late Leaf Spot disease severity
in groundnut crops using weather parameters and regression models.

Copyright (c) 2026 Kishor Kumar
All rights reserved.
"""

import streamlit as st

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Late Leaf Spot Prediction",
    page_icon="🌿",
    layout="centered"
)

# -------------------------------
# TITLE
# -------------------------------
st.title("🌿 Late Leaf Spot Disease Prediction – Groundnut")

st.markdown(
"""
This application predicts disease severity using weather parameters.
Enter the required data below and select the prediction model.
"""
)

# -------------------------------
# INPUT SECTION
# -------------------------------
st.subheader("Enter Weather Parameters")

x1 = st.number_input("Max Temperature (°C)", min_value=0.0)
x2 = st.number_input("Min Temperature (°C)", min_value=0.0)
x3 = st.number_input("Morning Relative Humidity (%)", min_value=0.0)
x4 = st.number_input("Evening Relative Humidity (%)", min_value=0.0)
x5 = st.number_input("Rainfall (mm)", min_value=0.0)

model = st.selectbox(
    "Select Prediction Model",
    ["Current Week", "1 Week Before", "2 Weeks Before"]
)

# -------------------------------
# PREDICTION FUNCTION
# -------------------------------
def predict_disease(x1, x2, x3, x4, x5, model):

    if model == "Current Week":
        Y = -88.94 + 3.39*x1 + 1.16*x2 + 0.368*x3 - 0.0503*x4 - 1.98*x5
    elif model == "1 Week Before":
        Y = -69.84 + 2.86*x1 + 1.20*x2 + 0.294*x3 - 0.0192*x4 + 0.213*x5
    else:
        Y = -76.11 + 3.08*x1 + 1.12*x2 + 0.0873*x3 - 0.0892*x4 + 1.89*x5

    # Risk classification
    if Y < 20:
        risk = "Low Risk"
        advice = "No spray needed."
    elif Y < 40:
        risk = "Moderate Risk"
        advice = "Monitor crop condition."
    elif Y < 60:
        risk = "High Risk"
        advice = "Preventive fungicide spray recommended."
    else:
        risk = "Severe Risk"
        advice = "Immediate fungicide spray required!"

    return Y, risk, advice

# -------------------------------
# PREDICT BUTTON
# -------------------------------
if st.button("Predict Disease"):

    Y, risk, advice = predict_disease(x1, x2, x3, x4, x5, model)

    st.success(f"Disease Severity: {Y:.2f}%")
    st.info(f"Risk Level: {risk}")
    st.warning(f"Advisory: {advice}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("© 2026 Kishor Kumar. All Rights Reserved.")
