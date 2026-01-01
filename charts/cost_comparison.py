import plotly.graph_objects as go
import streamlit as st

def render_cost_comparison(input_df, df_history):
    st.markdown("#### 💸 Monthly Charges vs Market Average")
    # avg_churn_cost = 74.44
    # avg_retain_cost = 61.26
    avg_churn_cost = df_history[df_history['Churn'] == 'Yes']['MonthlyCharges'].mean()
    avg_retain_cost = df_history[df_history['Churn'] == 'No']['MonthlyCharges'].mean()
    user_cost = input_df['MonthlyCharges'].iloc[0]
    
    fig_bar = go.Figure(data=[
        go.Bar(name='This Customer', x=['Charges'], y=[user_cost], marker_color='blue'),
        go.Bar(name='Avg Churned User', x=['Charges'], y=[avg_churn_cost], marker_color='red', opacity=0.5),
        go.Bar(name='Avg Loyal User', x=['Charges'], y=[avg_retain_cost], marker_color='green', opacity=0.5)
    ])
    fig_bar.update_layout(barmode='group', title_text="Cost Comparison", height=250)
    st.plotly_chart(fig_bar, use_container_width=True)
    st.caption("📊 Chart Type: Grouped Bar Chart")
    st.caption("🧠 Working: Compares individual monthly charges against average churned and retained customer charges.")