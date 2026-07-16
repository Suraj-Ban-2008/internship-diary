import streamlit as st
import pandas as pd
import joblib

st.title("Grape Quality Prediction")
st.write("put the values and know the quality of ur grapes")

# Model load
model = joblib.load("rf_classifier.pkl")
scaler = joblib.load('rf_scaler.pkl')

# Input boxes - NAAM BHI AUR LABEL BHI SAME
COLOR_INTENSITY = st.number_input("COLOR_INTENSITY")
FLAVANOIDS = st.number_input("FLAVANOIDS")
PROLINE = st.number_input("PROLINE")
WATER_O2_PER = st.number_input("WATER_O2_PER") # yaha TEMPERATURE mat likhna
FER_P2O5_PER = st.number_input("FER_P2O5_PER")

# DataFrame banao
user_input = pd.DataFrame({
    'COLOR_INTENSITY': [COLOR_INTENSITY],
    'FLAVANOIDS': [FLAVANOIDS],
    'PROLINE': [PROLINE],
    'WATER_O2_PER': [WATER_O2_PER],
    'FER_P2O5_PER': [FER_P2O5_PER]
})

if st.button("click"):
    scaled_input = scaler.transform(user_input)
    prediction = model.predict(scaled_input)
    st.success(f"grape quality is: {prediction[0]}")