import pandas as pd
import streamlit as st

# Transforms data, selects features, and returns probability and class.

def make_prediction(model, preprocessor, selected_features, threshold, input_df):

    # Preprocess
    processed_array = preprocessor.transform(input_df)
    processed_cols = preprocessor.get_feature_names_out()
    processed_df = pd.DataFrame(processed_array, columns=processed_cols)
    
    # Select Features
    final_df = processed_df[selected_features]
    
    # Predict
    prob = model.predict_proba(final_df)[:, 1][0]
    prediction = 1 if prob >= threshold else 0
    
    return prob, prediction