import streamlit as st

st.set_page_config(page_title="Late Leaf Spot Prediction", layout="centered")

st.title("🌿 Late Leaf Spot Disease Prediction – Groundnut")

# Input fields
x1 = st.number_input("Max Temperature (°C)", format="%.2f")
x2 = st.number_input("Min Temperature (°C)", format="%.2f")
x3 = st.number_input("Morning RH (%)", format="%.2f")
x4 = st.number_input("Evening RH (%)", format="%.2f")
x5 = st.number_input("Rainfall (mm)", format="%.2f")

model = st.selectbox(
    "Select Prediction Model",
    ["Current Week", "1 Week Before", "2 Weeks Before"]
)

if st.button("Predict Disease"):

    if model == "Current Week":
        Y = -88.94 + 3.39*x1 + 1.16*x2 + 0.368*x3 - 0.0503*x4 - 1.98*x5
    elif model == "1 Week Before":
        Y = -69.84 + 2.86*x1 + 1.20*x2 + 0.294*x3 - 0.0192*x4 + 0.213*x5
    else:
        Y = -76.11 + 3.08*x1 + 1.12*x2 + 0.0873*x3 - 0.0892*x4 + 1.89*x5

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

    st.success(f"Disease Severity: {Y:.2f}%")
    st.warning(f"Risk Level: {risk}")
    st.info(f"Advisory: {advice}")
