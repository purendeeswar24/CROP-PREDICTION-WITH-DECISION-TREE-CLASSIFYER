import streamlit as st
import numpy as np 
import joblib
import os

# Custom CSS for styling the app
st.markdown("""
    <style>
    /* Background for the app */
    .stApp {
        background-color: #f0f4f7;
    }

    /* Title styling */
    .title h1 {
        font-size: 48px;
        font-weight: bold;
        color: #009688;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Subtle box shadow for input widgets */
    .stNumberInput, .stSelectbox {
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        border-radius: 8px;
        margin-bottom: 20px;
    }

    /* Button styling */
    .stButton button {
        background-color: #009688;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
        transition: background-color 0.3s ease;
    }

    /* Button hover effect */
    .stButton button:hover {
        background-color: #00796b;
    }

    /* Text area styling for results */
    .stTextArea {
        font-size: 18px;
        color: #424242;
        border: 1px solid #bdbdbd;
        padding: 20px;
        border-radius: 10px;
        background-color: #e0f7fa;
    }
    </style>
""", unsafe_allow_html=True)

# Load the model
model = joblib.load("dtc.pkl")

# Title with custom styling
st.markdown("<div class='title'><h1>Lung Cancer Finder</h1></div>", unsafe_allow_html=True)

# User inputs with section header
st.header("Please fill in the following details:")

# User inputs with custom placeholders and labels
gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
age = st.number_input("Enter your age", min_value=18, max_value=90, step=1, key="age")

smoke = st.number_input("Do you smoke? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="smoke")
YELLOW_FINGERS = st.number_input("Do you have yellow fingers? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="yellow_fingers")
ANXIETY = st.number_input("Do you feel anxious? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="anxiety")
PEER_PRESSURE = st.number_input("Do you experience peer pressure? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="peer_pressure")
CHRONIC_dcs = st.number_input("Do you have a chronic disease? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="chronic_dcs")
FATIGUE = st.number_input("Do you feel fatigue? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="fatigue")
ALLERGY = st.number_input("Do you have any allergies? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="allergy")
WHEEZING = st.number_input("Do you experience wheezing? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="wheezing")
ALCOHOL = st.number_input("Do you consume alcohol? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="alcohol")
COUGHING = st.number_input("Are you coughing? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="coughing")
SHORTNESS_BREATH = st.number_input("Do you experience shortness of breath? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="shortness_breath")
SWALLOWING = st.number_input("Do you have difficulty swallowing? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="swallowing")
chest_pain = st.number_input("Do you experience chest pain? (1 for Yes, 2 for No)", min_value=1, max_value=2, step=1, key="chest_pain")

# Map the values to numeric
gender_values = 1 if gender == "Male" else 2

# Combine input features (including COUGHING)
input_features = [[age, gender_values, smoke, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_dcs, FATIGUE, ALLERGY, WHEEZING, ALCOHOL, COUGHING, SHORTNESS_BREATH, SWALLOWING, chest_pain]]

# Prediction with a button
if st.button("Predict Lung Condition"):
    prediction = model.predict(input_features)

    if prediction == 1:
        st.text_area("Result", "You have a lung problem. Please contact a doctor as soon as possible.")
    else:
        st.text_area("Result", "You are healthy. Keep taking care of your health, no lung issues detected.")
