import streamlit as st
import joblib

model = joblib.load("logistic_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Seed Prediction")

AREA = st.number_input("AREA")
PERIMETER = st.number_input("PERIMETER")
COMPACTNESS = st.number_input("COMPACTNESS")
LENGTH = st.number_input("LENGTH")
WIDTH = st.number_input("WIDTH")
ASYMMETRY = st.number_input("ASYMMETRY")
GROOVE = st.number_input("GROOVE")

if st.button("Predict"):
    data = [[AREA, PERIMETER, COMPACTNESS, LENGTH, WIDTH, ASYMMETRY, GROOVE]]
    data = scaler.transform(data)
    pred = model.predict(data)[0]
    st.write("Predicted Class:", pred)