import plotly.graph_objects as go
import streamlit as st

def render_tenure_gauge(input_df):
    st.markdown("#### 📉 Contract & Tenure Analysis")
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = input_df['tenure'].iloc[0],
        # title = {'text': "Customer Tenure (Months)"},
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [None, 72]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 12], 'color': "red"},
                {'range': [12, 24], 'color': "orange"},
                {'range': [24, 72], 'color': "lightgreen"}],
        }
    ))
    fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=30, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)
    st.caption("📊 Chart Type: Gauge Chart (Radial Indicator)")
    st.caption("🧠 Working: Shows customer tenure on a fixed scale to highlight churn risk zones.")