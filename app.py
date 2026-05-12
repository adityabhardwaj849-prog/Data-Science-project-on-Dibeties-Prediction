import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load(r"C:\Users\adity\OneDrive\Documents\New folder\project\diabetes_model.pkl", "r")

st.title("Diabetes Prediction System")

st.write("Enter patient details:")

preg = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose", 0, 300)
bp = st.number_input("Blood Pressure", 0, 200)
skin = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin", 0, 900)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 1, 120)

if st.button("Predict"):
    data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    result = model.predict(data)

    if result[0] == 1:
        st.error("Patient is Diabetic")
    else:
        st.success("Patient is Not Diabetic")