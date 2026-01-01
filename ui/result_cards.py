import streamlit as st

# Displays the prediction result card based on the prediction class.

def render_result_card(prob, prediction):

    st.subheader("1. Prediction Result")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if prediction == 1:
            st.markdown(f"""
            <div class="metric-card">
                <h2 style="color: #d32f2f;">⚠️ High Churn Risk</h2>
                <h3>Probability: {prob:.2%}</h3>
                <p>This customer is highly likely to leave. Immediate retention action is recommended.</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="safe-card">
                <h2 style="color: #2e7d32;">✅ Low Churn Risk</h2>
                <h3>Probability: {prob:.2%}</h3>
                <p>This customer appears stable. Continue standard engagement.</p>
            </div>
            """, unsafe_allow_html=True)