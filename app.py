import streamlit as st
from core.model_loader import load_assets
from core.feature_engineering import engineer_features
from core.predictor import make_prediction
from ui.sidebar import render_sidebar
from ui.result_cards import render_result_card
from charts.tenure_gauge import render_tenure_gauge
from charts.cost_comparison import render_cost_comparison
from charts.risk_factors import render_risk_factors
from charts.demographic_compare import render_demographic_comparison
from charts.macro_triggers import render_macro_triggers
from charts.financial_analysis import render_financial_analysis
from charts.tenure_patterns import render_tenure_patterns

# page metadata and layout
st.set_page_config(page_title="Telco Churn Analytics Dashboard", page_icon="📊", layout="wide")

# Css for result card: 
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ff4b4b;
    }
    .safe-card {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. Load Assets
model, preprocessor, selected_features, threshold, raw_data = load_assets()

# 2. Title selection:
st.title("📡 Telco Customer Prediction Dashboard")
st.markdown("Use this tool to predict customer churn risks and understand the **key drivers** behind customer decisions.")
st.divider()

if model is None:
    st.error("❌ Critical Error: Missing model files. Please check your folder.")
    st.stop()

# Sidebar input 
input_df = render_sidebar()

# ---------------------------------------------------------
# LOGIC & CONTROL FLOW
# ---------------------------------------------------------

# 1. Initialize the "Active" State
# We use this to determine if the dashboard should be visible.
if 'analysis_active' not in st.session_state:
    st.session_state['analysis_active'] = False

# 2. The Button triggers the activation
# When clicked, it turns the dashboard ON.
if st.sidebar.button("🚀 Predict Churn Risk", type="primary"):
    st.session_state['analysis_active'] = True

# 3. Main Dashboard Rendering
# This block runs only if the button has been pressed at least once.
# Because it is outside the button's 'if' block, it reruns on every sidebar change.
if st.session_state['analysis_active']:
    
    # --- Live Prediction ---
    # We calculate this every time the script reruns (i.e., when you change a slider)
    engineered_df = engineer_features(input_df)
    prob, prediction = make_prediction(model, preprocessor, selected_features, threshold, engineered_df)
    
    # --- Dashboard Visuals ---
    render_result_card(prob, prediction)
    st.divider()

    st.subheader("2. Prediction Analysis:")
    col1, col2 = st.columns(2)
    
    with col1:
        render_tenure_gauge(input_df)
    
    with col2:
        render_cost_comparison(input_df, raw_data)
    
    st.divider()

    # Strategic insights section
    st.subheader("3. Strategic Insights:")
    tab1, tab2 = st.tabs(["Personalized Risk Factors", "Demographic Context"])
    
    with tab1:
        render_risk_factors(input_df, raw_data)
        
    with tab2:
        render_demographic_comparison(input_df, raw_data, prediction)

else:
    # This shows when the app loads or before the button is pressed
    st.info("👈 Please adjust the customer profile in the sidebar and click 'Predict Churn Risk' to generate the live dashboard.")

# ---------------------------------------------------------
# 6. General Dataset Analysis
# ---------------------------------------------------------
st.divider()
st.subheader("4. DataSet Analysis")
st.write("Explore trends across the entire customer database to identify churn patterns.")

with st.expander("📊 Click to Open General Dataset Insights", expanded=False):
    macro_tab1, macro_tab2, macro_tab3 = st.tabs(["Top Churn Triggers", "Financial Impact", "Tenure Patterns"])
    
    with macro_tab1:
        render_macro_triggers(raw_data)
    with macro_tab2:
        render_financial_analysis(raw_data)
    with macro_tab3:
        render_tenure_patterns(raw_data)

# Footer
st.markdown("---")
st.markdown("### 🔍 Model Transparency")
st.markdown(f"**Model Used:** Random Forest Classifier (Optimized) | **Accuracy:** 80.3% | **Decision Threshold:** {threshold:.2f}")