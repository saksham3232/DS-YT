from math import e

import streamlit as st
import joblib
import pandas as pd

model = joblib.load('heart_disease_model.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title("Heart Disease Prediction App by Saksham❤️")

st.markdown("""
This app predicts the likelihood of heart disease based on user input. Please fill in the required information below and click the 'Predict' button to see the results.
""")

age = st.slider("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", options=["Male", "Female"])
chest_pain = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
resting_bp = st.number_input("Resting Blood Pressure (in mm Hg)", min_value=80, max_value=200, value=120)
cholesterol = st.number_input("Serum Cholesterol (in mg/dl)", min_value=100, max_value=600, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"])
resting_ecg = st.selectbox("Resting Electrocardiographic Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", options=["Yes", "No"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, value=1.0)
st_slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])


if st.button("Predict"):
    # Create a DataFrame from user input
    raw_input = {
        'Age': age,
        'Sex': 1 if sex == "Male" else 0,
        'ChestPainType': chest_pain,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': 1 if fasting_bs == "Yes" else 0,
        'RestingECG': resting_ecg,
        'MaxHR': max_hr,
        'ExerciseAngina': 1 if exercise_angina == "Yes" else 0,
        'Oldpeak': oldpeak,
        'ST_Slope': st_slope
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)

    if prediction == 1:
        st.error("The model predicts that you are likely to have heart disease. Please consult a healthcare professional for further evaluation.")
    else:
        st.success("The model predicts that you are unlikely to have heart disease. However, please consult a healthcare professional for a comprehensive assessment.")
