import plotly.express as px
import streamlit as st

def render_tenure_patterns(df_history):
    
    fig_tenure = px.histogram(df_history, x='tenure', color='Churn', 
                              barmode='overlay',
                              title="Customer Tenure Distribution (Churn vs Retain)",
                              labels={'tenure': 'Months with Company'},
                              color_discrete_map={'Yes': 'red', 'No': 'green'},
                              opacity=0.6)
    
    fig_tenure.update_layout(xaxis_title="Tenure (Months)", yaxis_title="Count of Customers")
    st.plotly_chart(fig_tenure, use_container_width=True)
    st.caption("📊 Chart Type: Overlaid Histogram")
    st.caption("🧠 Working: Overlays tenure distributions to identify when churn occurs.")
    
    st.warning("⚠️ **Interpretation:** Look at the 'Red' spike on the left (0-12 months). This indicates new customers are the most vulnerable.")