import streamlit as st
import joblib

# 1. Model load
model = joblib.load('balance_model.pkl')

st.title("⚖️ Balance Predictor")

# 2. 4 input box
lw = st.number_input("Left-Weight", 1, 5, 2)
ld = st.number_input("Left-Distance", 1, 5, 4)
rw = st.number_input("Right-Weight", 1, 5, 3)
rd = st.number_input("Right-Distance", 1, 5, 2)

# 3. Predict button
if st.button("Predict"):
    pred = model.predict([[lw, ld, rw, rd]])[0]

    out = {'B': 'Balance ✅', 'L': 'Left Heavy ⬅️', 'R': 'Right Heavy ➡️'}
    st.success(out[pred])