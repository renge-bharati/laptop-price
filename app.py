import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("laptop_price_model.pkl", "rb"))

st.title("💻 Laptop Price Prediction App")

company = st.number_input("Company (encoded number)")
ram = st.number_input("RAM (GB)")
weight = st.number_input("Weight (kg)")
screen_size = st.number_input("Screen Size (inch)")

if st.button("Predict Price"):
    input_data = np.array([[company, ram, weight, screen_size]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Laptop Price: ₹ {round(prediction[0],2)}")
