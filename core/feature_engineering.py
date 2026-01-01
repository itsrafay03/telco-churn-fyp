import pandas as pd

# Applies the necessary feature engineering steps to the user input before passing it to the model.

def engineer_features(input_df):
    
    df = input_df.copy()
    
    # Tenure Grouping
    bins = [0, 12, 24, 48, 60, 100]
    labels = ['0-1 Year', '1-2 Years', '2-4 Years', '4-5 Years', '>5 Years']
    df['TenureGroup'] = pd.cut(df['tenure'], bins=bins, labels=labels, right=False)
    
    # Service Counts
    svc_cols = ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']
    df['NumAdditionalServices'] = (df[svc_cols] == 'Yes').sum(axis=1)
    
    # Security Flag
    df['HasSecurityService'] = ((df['OnlineSecurity'] == 'Yes') | (df['DeviceProtection'] == 'Yes')).astype(int)
    
    # Avg Monthly Charges
    df['AvgMonthlyCharges'] = df['TotalCharges'] / (df['tenure'] + 1)
    
    return df