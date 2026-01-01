import joblib
import pandas as pd
import streamlit as st
import os

# Loads machine learning models, preprocessors, and the dataset.
# Thsi function is called once in app startup.

@st.cache_resource
def load_assets():

    try:
        # Paths are relative to the main app.py
        model = joblib.load('assets/churn_model.pkl')
        preprocessor = joblib.load('assets/preprocessor.pkl')
        features = joblib.load('assets/selected_features.pkl')
        threshold = joblib.load('assets/model_threshold.pkl')
        
        # Load raw data for historical comparison
        raw_data = pd.read_csv("data/Telco-Customer-Churn.csv")
        raw_data['TotalCharges'] = pd.to_numeric(raw_data['TotalCharges'], errors='coerce').fillna(0)
        
        return model, preprocessor, features, threshold, raw_data
    except Exception as e:
        st.error(f"Error loading assets: {e}")
        return None, None, None, None, None