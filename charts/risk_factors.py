import plotly.express as px
import pandas as pd
import streamlit as st

def render_risk_factors(input_df, df_history):
    st.markdown(f"**Customer's attributes which contribute most to churn.**")
    
    risk_factors = []
    
    features_to_check = ['Contract', 'InternetService', 'PaymentMethod', 'TechSupport', 'OnlineSecurity']
    
    for feature in features_to_check:
        selected_val = input_df[feature].iloc[0]
        # Safe get: if category doesn't exist default to 0
        risk_score = df_history[df_history[feature] == selected_val]['Churn'].value_counts(normalize=True).get('Yes', 0)
        risk_factors.append({'Feature': feature, 'Value': selected_val, 'Risk_Score': risk_score})

    risk_df = pd.DataFrame(risk_factors).sort_values(by='Risk_Score', ascending=True)
    
    fig_risk = px.bar(risk_df, x='Risk_Score', y='Feature', orientation='h', text='Value',
                      title="Risk Contribution of Selected Features",
                      labels={'Risk_Score': 'Churn Rate'},
                      color='Risk_Score', color_continuous_scale='Reds')
    
    fig_risk.update_traces(textposition='inside', textfont=dict(color='white'))
    fig_risk.update_layout(xaxis_tickformat=".0%")
    st.plotly_chart(fig_risk, use_container_width=True)
    st.caption("📊 Chart Type: Bar Chart")
    st.caption("🧠 Working: Displays historical churn rates of selected customer attributes.")