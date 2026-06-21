import streamlit as st
import pandas as pd
import pickle
from sklearn.pipeline import Pipeline
from fastapi import FastAPI


app = FastAPI()

df = pd.read_csv('data/saudi_jobs_cleaned.csv')

with open('model.pkl', 'rb') as f:
    pipeline = pickle.load(f)

st.title("Saudi Labor Market — Salary Predictor")
st.markdown("Enter job details to predict the expected salary")

# Input
col1, col2 = st.columns(2)

with col1:
    region = st.selectbox("Region", sorted(df['region'].unique()))
    eco_activity = st.selectbox("Sector", sorted(df['eco_activity'].unique()))
    job_title = st.selectbox("Job Title", sorted(df['job_title'].unique()))

with col2:
    city = st.selectbox("City", sorted(df[df['region'] == region]['city'].unique()))
    comp_size = st.selectbox("Company Size", sorted(df['comp_size'].unique()))
    exper = st.slider("Years of Experience", 0, 12, 2)
    comp_type = st.radio("Company Type", ["Private", "Semi-Governmental"])

# Convert company type
comp_type_val = 1 if comp_type == "Private" else 0

# Predict button
if st.button("Predict Salary"):
    input_data = pd.DataFrame([{
        'region': region,
        'eco_activity': eco_activity,
        'city': city,
        'comp_size': comp_size,
        'job_title': job_title,
        'exper': exper,
        'comp_type': comp_type_val
    }])
    
    predicted = pipeline.predict(input_data)[0]
    st.success(f"Expected Salary: {predicted:,.0f} SAR")