
import streamlit as st
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('bmi_model.pkl', 'rb'))

st.title('BMI Category Prediction')

# Input fields for height and weight
height = st.number_input('Height (cm)', min_value=140, max_value=200, value=170)
weight = st.number_input('Weight (kg)', min_value=50, max_value=160, value=70)

# Predict button
if st.button('Predict BMI Category'):
    input_data = np.array([[height, weight]])
    prediction = model.predict(input_data)
    category = prediction[0]
    
    st.write(f'The predicted BMI category is: {category}')
