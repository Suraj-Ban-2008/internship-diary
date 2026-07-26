import streamlit as st
import joblib
import numpy as np

# 1. Model load karo
model = joblib.load('prp_model.joblib')

st.title("Computer PRP Prediction - Decision Tree")
st.write("Enter 9 values to predict PRP")

# 2. 9 inpsut box ek saath
vendor = st.number_input("Vendor Code", 0, 50, 1)
model_no = st.number_input("Model Code", 0, 100, 5)
MYCT = st.number_input("MYCT", 10, 1000, 125)
MMIN = st.number_input("MMIN", 64, 2000, 256)
MMAX = st.number_input("MMAX", 1000, 8000, 6000)
CACH = st.number_input("CACH", 0, 1000, 256)
CHMIN = st.number_input("CHMIN", 0, 50, 16)
CHMAX = st.number_input("CHMAX", 0, 50, 8)
ERP = st.number_input("ERP", 0, 50, 10)

# 3. Predict button
if st.button("Predict"):
    new_entry = [[vendor, model_no, MYCT, MMIN, MMAX, CACH, CHMIN, CHMAX, ERP]]
    prediction = model.predict(new_entry)
    
    st.success(f"New : {new_entry}")
    st.success(f"Prediction: {prediction[0]:.2f}")