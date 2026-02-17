"""
Late Leaf Spot Disease Prediction System
------------------------------------------
Developed by: Kishor Kumar
Year: 2026

Weather-based decision support system for predicting
Late Leaf Spot disease severity in groundnut.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------
st.set_page_config(
    page_title="Late Leaf Spot Prediction",
    page_icon="🌿",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>
.main-title {
    font-size:42px;
    font-weight:bold;
    text-align:center;
    color:#1B5E20;
}
.section-title {
    font-size:28px;
    color:#2E7D32;
    margin-top:20px;
}
.stButton>button {
    background-color:#2E8B57;
    color:white;
    font-weight:bold;
    border-radius:8px;
}
.stButton>button:hover {
    background-color:#1B5E20;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Disease Prediction", "Disease Information", "About Developer"]
)

# ===================================================
# HOME PAGE (Professional Hero Banner)
# ===================================================
if page == "Home":

    st.markdown("""
    <style>
    .hero {
        position: relative;
        background-image: url('https://raw.githubusercontent.com/kishore16012003-cell/late-leaf-spot-app/main/banner.jpg');
        background-size: cover;
        background-position: center;
        height: 500px;
        border-radius: 15px;
    }

    .overlay {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: rgba(0,0,0,0.55);
        border-radius: 15px;
    }

    .hero-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        text-align: center;
    }

    .hero-text h1 {
        font-size: 48px;
        font-weight: bold;
    }

    .hero-text p {
        font-size: 22px;
    }
    </style>

    <div class="hero">
        <div class="overlay"></div>
        <div class="hero-text">
            <h1>🌿 Late Leaf Spot Disease Prediction</h1>
            <p>Weather-Based Decision Support System for Groundnut</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.write("""
    This decision support system predicts Late Leaf Spot disease severity 
    using weather-based regression models. It assists farmers in taking 
    timely preventive management decisions.
    """)

# ===================================================
# DISEASE PREDICTION PAGE
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

        Y = max(0, min(Y, 100))

        if Y < 40:
            risk, advice, color = "Low Risk", "No fungicide spray required.", "green"
        elif Y < 60:
            risk, advice, color = "Moderate Risk", "Monitor crop regularly.", "gold"
        elif Y < 80:
            risk, advice, color = "High Risk", "Preventive fungicide spray recommended.", "orange"
        else:
            risk, advice, color = "Severe Risk", "Immediate fungicide spray required!", "red"

        return Y, risk, advice, color

    if st.button("Predict Disease"):

        Y, risk, advice, color = predict_disease(x1, x2, x3, x4, x5, model)

        st.markdown(
            f"<h2 style='color:{color};'>Predicted Severity: {Y:.2f}% ({risk})</h2>",
            unsafe_allow_html=True
        )

        st.warning(f"Advisory: {advice}")

        # Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=Y,
            title={'text': "Disease Severity (%)"},
            gauge={
                'axis': {'range': [0, 100]},
                'steps': [
                    {'range': [0, 40], 'color': "lightgreen"},
                    {'range': [40, 60], 'color': "yellow"},
                    {'range': [60, 80], 'color': "orange"},
                    {'range': [80, 100], 'color': "red"}
                ],
            }
        ))
        st.plotly_chart(fig, use_container_width=True)

        # Weather Bar Chart
        weather_data = pd.DataFrame({
            "Parameter": ["Max Temp", "Min Temp", "Morning RH", "Evening RH", "Rainfall"],
            "Value": [x1, x2, x3, x4, x5]
        })

        fig2 = px.bar(weather_data, x="Parameter", y="Value",
                      title="Weather Parameters Used for Prediction")
        st.plotly_chart(fig2, use_container_width=True)

        # Animated Severity Trend
        weeks = list(range(1, 11))
        trend_values = np.linspace(max(5, Y-30), Y, 10)

        trend_data = pd.DataFrame({
            "Week": weeks,
            "Severity": trend_values
        })

        fig_trend = px.line(
            trend_data,
            x="Week",
            y="Severity",
            markers=True,
            range_y=[0, 100],
            title="Animated Weekly Severity Trend",
            animation_frame="Week"
        )

        st.plotly_chart(fig_trend, use_container_width=True)

# ===================================================
# DISEASE INFORMATION PAGE
# ===================================================
elif page == "Disease Information":

    st.markdown('<p class="section-title">About Late Leaf Spot Disease</p>', unsafe_allow_html=True)

    st.write("""
    Late Leaf Spot is a fungal disease affecting groundnut crops.
    It appears as dark brown to black circular lesions on leaves,
    leading to premature defoliation and yield loss.
    """)

    st.subheader("Symptoms:")
    st.write("""
    - Dark circular spots  
    - Yellow halo around lesions  
    - Severe leaf drop  
    """)

    st.subheader("Management:")
    st.write("""
    - Timely fungicide application  
    - Crop rotation  
    - Use of resistant varieties  
    - Proper sanitation  
    """)

# ===================================================
# ABOUT PAGE
# ===================================================
elif page == "About Developer":

    st.markdown('<p class="section-title">About the Developer</p>', unsafe_allow_html=True)

    st.write("""
    Developed by: **Kishor Kumar**  
    Specialization: Data Science & Agricultural Informatics  
    Year: 2026  
    """)

    st.write("""
    This system was developed as part of research work
    to assist farmers in early disease prediction
    and management of Late Leaf Spot in groundnut.
    """)
