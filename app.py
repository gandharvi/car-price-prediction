import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib


model = joblib.load('car_price_model.joblib')


encoders = {}
categorical_columns = ['Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type', 'Gear box type', 'Drive wheels', 'Wheel', 'Color']
for col in categorical_columns:
    encoders[col] = joblib.load(f'{col}_encoder.joblib')

st.title('Car Price Prediction App')

manufacturer = st.selectbox('Manufacturer', encoders['Manufacturer'].classes_)
model_name = st.selectbox('Model', encoders['Model'].classes_)
category = st.selectbox('Category', encoders['Category'].classes_)
leather_interior = st.selectbox('Leather interior', encoders['Leather interior'].classes_)
fuel_type = st.selectbox('Fuel type', encoders['Fuel type'].classes_)
gear_box_type = st.selectbox('Gear box type', encoders['Gear box type'].classes_)
drive_wheels = st.selectbox('Drive wheels', encoders['Drive wheels'].classes_)
wheel = st.selectbox('Wheel', encoders['Wheel'].classes_)
color = st.selectbox('Color', encoders['Color'].classes_)
levy = st.number_input('Levy', min_value=0, value=0)
engine_volume = st.number_input('Engine volume', min_value=0.0, value=1.0)
mileage = st.number_input('Mileage', min_value=0, value=0)
cylinders = st.number_input('Cylinders', min_value=0, value=4)
airbags = st.number_input('Airbags', min_value=0, value=2)
age = st.number_input('Age', min_value=0, value=0)

encoded_inputs = {
    'Manufacturer': encoders['Manufacturer'].transform([manufacturer])[0],
    'Model': encoders['Model'].transform([model_name])[0],
    'Category': encoders['Category'].transform([category])[0],
    'Leather interior': encoders['Leather interior'].transform([leather_interior])[0],
    'Fuel type': encoders['Fuel type'].transform([fuel_type])[0],
    'Gear box type': encoders['Gear box type'].transform([gear_box_type])[0],
    'Drive wheels': encoders['Drive wheels'].transform([drive_wheels])[0],
    'Wheel': encoders['Wheel'].transform([wheel])[0],
    'Color': encoders['Color'].transform([color])[0],
    'Levy': levy,
    'Engine volume': engine_volume,
    'Mileage': mileage,
    'Cylinders': cylinders,
    'Airbags': airbags,
    'Age': age
}

input_df = pd.DataFrame([encoded_inputs])

if st.button('Predict Price'):
    prediction = model.predict(input_df)
    st.write(f'The predicted price of the car is: {prediction[0]}')
