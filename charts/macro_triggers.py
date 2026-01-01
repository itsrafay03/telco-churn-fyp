import plotly.express as px
import pandas as pd
import streamlit as st

def render_macro_triggers(df_history):
    
    cat_cols_for_analysis = ['Gender', 'SeniorCitizen', 'Partner', 'Dependents', 
                           'PhoneService', 'MultipleLines', 'InternetService', 
                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 
                           'TechSupport', 'StreamingTV', 'StreamingMovies', 
                           'Contract', 'PaperlessBilling', 'PaymentMethod']
    
    risk_data = []
    
    for col in cat_cols_for_analysis:
        if col in df_history.columns:
            summary = df_history.groupby(col)['Churn'].apply(lambda x: (x == 'Yes').mean()).reset_index()
            summary.columns = ['Value', 'ChurnRate']
            summary['Feature'] = col
            summary = summary[summary['ChurnRate'] > 0.0] 
            risk_data.append(summary)
    
    if risk_data:
        all_risks = pd.concat(risk_data)
        top_risks = all_risks.sort_values(by='ChurnRate', ascending=False).head(10)
        top_risks['Label'] = top_risks['Feature'] + ": " + top_risks['Value'].astype(str)
        
        fig_triggers = px.bar(top_risks, x='ChurnRate', y='Label', orientation='h',
                              title="Top 10 High-Risk Customer Attributes (Global)",
                              labels={'Label': 'Attribute', 'ChurnRate': 'Churn Rate'},
                              color='ChurnRate', color_continuous_scale='Reds')
        
        fig_triggers.update_layout(yaxis={'categoryorder':'total ascending'}, height=500)
        st.plotly_chart(fig_triggers, use_container_width=True)
        st.caption("📊 Chart Type: Horizontal Bar Chart (Global Risk Ranking)")
        st.caption("🧠 Working: Ranks customer attributes by churn rate.")

        st.info("💡 **Insight:** The attributes at the top of this chart represent the most dangerous segments.")