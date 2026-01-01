import plotly.express as px
import streamlit as st

def render_financial_analysis(df_history):
    
    col_fin1, col_fin2 = st.columns(2)
    
    with col_fin1:
        fig_box = px.box(df_history, x='Churn', y='MonthlyCharges', color='Churn',
                         title="Distribution of Monthly Charges by Churn Status",
                         color_discrete_map={'Yes': 'red', 'No': 'green'})
        st.plotly_chart(fig_box, use_container_width=True)
        st.caption("📊 Chart Type: Box Plot")
        st.caption("🧠 Working: Compares monthly charge distributions.")
        st.caption("If Red box > Green box, higher bills drive churn.")
        
    with col_fin2:
        fig_hist_fin = px.histogram(df_history, x='TotalCharges', color='Churn',
                                  title="Total Charges Distribution",
                                  marginal="box",
                                  opacity=0.7,
                                  color_discrete_map={'Yes': 'red', 'No': 'green'})
        st.plotly_chart(fig_hist_fin, use_container_width=True)
        st.caption("📊 Chart Type: Histogram with Marginal Box Plot")
        st.caption("🧠 Working: Shows total charges distribution.")