"""
Late Leaf Spot Disease Prediction System
------------------------------------------
Developed by: Kishor Kumar
Year: 2026

This application predicts Late Leaf Spot disease severity in groundnut
using weather-based regression models and provides advisory guidance.
"""

import streamlit as st

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Late Leaf Spot Prediction",
    page_icon="🌿",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS DESIGN
# ---------------------------------------------------
st.markdown("""
<style>
.main-title {
    font-size:40px;
    color:#2E8B57;
    font-weight:bold;
}
.section-title {
    font-size:28px;
    color:#006400;
    margin-top:20px;
}
.footer {
    text-align:center;
    font-size:14px;
    color:gray;
    margin-top:50px;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Disease Prediction", "Disease Information", "About Developer"]
)

# ===================================================
# PAGE 1 – HOME
# ===================================================
if page == "Home":

    st.markdown('<p class="main-title">🌿 Late Leaf Spot Disease Prediction</p>', unsafe_allow_html=True)

    st.write("""
    This web-based decision support system helps farmers predict
    Late Leaf Spot disease severity in groundnut crops using
    weather parameters such as temperature, humidity, and rainfall.
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/5/58/Arachis_hypogaea_peanuts.jpg", use_container_width=True)

    st.success("Navigate to 'Disease Prediction' page to start prediction.")

# ===================================================
# PAGE 2 – DISEASE PREDICTION
# ===================================================
elif page == "Disease Prediction":

    st.markdown('<p class="section-title">Weather Parameters Input</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        x1 = st.number_input("Max Temperature (°C)", min_value=0.0, value=32.0)
        x2 = st.number_input("Min Temperature (°C)", min_value=0.0, value=22.0)
        x3 = st.number_input("Morning Relative Humidity (%)", min_value=0.0, value=85.0)

    with col2:
        x4 = st.number_input("Evening Relative Humidity (%)", min_value=0.0, value=70.0)
        x5 = st.number_input("Rainfall (mm)", min_value=0.0, value=5.0)

    model = st.selectbox(
        "Select Prediction Model",
        ["Current Week", "1 Week Before", "2 Weeks Before"]
    )

    def predict_disease(x1, x2, x3, x4, x5, model):

        if model == "Current Week":
            Y = -88.94 + 3.39*x1 + 1.16*x2 + 0.368*x3 - 0.0503*x4 - 1.98*x5
        elif model == "1 Week Before":
            Y = -69.84 + 2.86*x1 + 1.20*x2 + 0.294*x3 - 0.0192*x4 + 0.213*x5
        else:
            Y = -76.11 + 3.08*x1 + 1.12*x2 + 0.0873*x3 - 0.0892*x4 + 1.89*x5

        # Limit prediction between 0 and 100
        Y = max(0, min(Y, 100))

        # Risk Classification
        if Y < 40:
            risk = "Low Risk"
            advice = "No fungicide spray required."

        elif Y < 60:
            risk = "Moderate Risk"
            advice = "Monitor crop condition regularly."

        elif Y < 80:
            risk = "High Risk"
            advice = "Preventive fungicide spray recommended."

        else:
            risk = "Severe Risk"
            advice = "Immediate fungicide spray required!"

        return Y, risk, advice

    if st.button("Predict Disease"):

        Y, risk, advice = predict_disease(x1, x2, x3, x4, x5, model)

        st.success(f"Disease Severity: {Y:.2f}%")
        st.info(f"Risk Level: {risk}")
        st.warning(f"Advisory: {advice}")

# ===================================================
# PAGE 3 – DISEASE INFORMATION
# ===================================================
elif page == "Disease Information":

    st.markdown('<p class="section-title">About Late Leaf Spot Disease</p>', unsafe_allow_html=True)

    st.write("""
    Late Leaf Spot is a fungal disease affecting groundnut crops.
    It appears as dark brown to black lesions on leaves,
    leading to premature defoliation and yield loss.
    """)

    st.subheader("Symptoms:")
    st.write("""
    - Dark circular spots on leaves  
    - Yellow halo around lesions  
    - Leaf drop in severe cases  
    """)

    st.subheader("Management Practices:")
    st.write("""
    - Timely fungicide application  
    - Crop rotation  
    - Use of resistant varieties  
    - Proper field sanitation  
    """)

# ===================================================
# PAGE 4 – ABOUT DEVELOPER
# ===================================================
elif page == "About Developer":

    st.markdown('<p class="section-title">About the Developer</p>', unsafe_allow_html=True)

    st.write("""
    Developed by: **Kishor Kumar**  
    Specialization: Data Science & Agricultural Informatics  
    Year: 2026  
    """)

    st.write("""
    This application was developed as part of research work
    to assist farmers in early detection and management of
    Late Leaf Spot disease in groundnut crops.
    """)

