import plotly.graph_objects as go
import streamlit as st

def render_demographic_comparison(input_df, df_history, prediction):
    st.markdown("**Compare this customer to others in the same group**")
    
    comparison_metric = st.selectbox("Compare Churn Rates based on:", 
                                     ["InternetService", "Contract", "PaymentMethod", "SeniorCitizen", "Partner", "Dependents", "TechSupport"])
    
    user_group_val = input_df[comparison_metric].iloc[0]
    
    if comparison_metric == 'SeniorCitizen':
         user_group_val = 1 if user_group_val == "Yes" else 0

    group_churn_rates = df_history.groupby(comparison_metric)['Churn'].apply(lambda x: (x == 'Yes').mean()).reset_index(name='ChurnRate')
    
    colors = ['lightgrey'] * len(group_churn_rates)
    categories = group_churn_rates[comparison_metric].tolist()
    
    try:
        if comparison_metric == 'SeniorCitizen':
             categories = [1 if c == 1 else 0 for c in categories]
        
        user_idx = categories.index(user_group_val)
        colors[user_idx] = '#d32f2f' if prediction == 1 else '#2e7d32'
    except ValueError:
        pass 

    fig_demo = go.Figure(data=[go.Bar(
        x=group_churn_rates[comparison_metric],
        y=group_churn_rates['ChurnRate'],
        marker_color=colors,
        text=group_churn_rates['ChurnRate'].apply(lambda x: f"{x:.1%}"),
        textposition='auto'
    )])
    
    fig_demo.update_layout(title=f"Churn Rate by {comparison_metric} (User is in: {user_group_val})",
                           yaxis_tickformat=".0%", yaxis_title="Churn Rate")
    
    st.plotly_chart(fig_demo, use_container_width=True)
    st.caption("📊 Chart Type: Categorical Bar Chart")
    st.caption("🧠 Working: Compares churn rates across categories.")