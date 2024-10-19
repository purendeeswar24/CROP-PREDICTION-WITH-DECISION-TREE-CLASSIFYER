import streamlit as st
import joblib
import numpy as np

model = joblib.load("des.pkl")

st.title("Crop Recommendation")

# User inputs
N = st.number_input("Enter nitrogen:", min_value=2, max_value=600)
P = st.number_input("Enter phosphorus value:", min_value=2, max_value=150)
K = st.number_input("Enter potassium value:", min_value=2, max_value=150)
temperature = st.number_input("Enter temperature:", min_value=2, max_value=50)
humidity = st.number_input("Enter humidity value:", min_value=20, max_value=150)
ph = st.number_input("Enter pH value:", min_value=3, max_value=10)
rainfall = st.number_input("Enter rainfall:", min_value=10, max_value=1000)

# Prediction
if st.button("Predict Crop"):
    user_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])  # Corrected this line
    prediction = model.predict(user_data)[0]
    st.success(f"The predicted crop is: {prediction}")
