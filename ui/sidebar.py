import streamlit as st
import pandas as pd

# Renders the sidebar inputs and returns a DataFrame of the user's raw inputs.
def render_sidebar():

    st.sidebar.header("📝 Customer Profile")

    with st.sidebar.expander("👤 Demographics", expanded=True):
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])

    with st.sidebar.expander("📞 Services", expanded=True):
        tenure = st.slider("Tenure (Months)", 0, 72, 24)
        phone = st.selectbox("Phone Service", ["Yes", "No"])
        multi_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
        internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        sec = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
        back = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
        dev = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
        tech = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
        tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
        mov = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])

    with st.sidebar.expander("💰 Billing & Contract", expanded=True):
        contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        monthly = st.number_input("Monthly Charges ($)", 0.0, 200.0, 70.0)
        total = st.number_input("Total Charges ($)", 0.0, 10000.0, monthly * tenure)

    data = {
        'gender': gender, 'SeniorCitizen': senior, 'Partner': partner, 'Dependents': dependents,
        'tenure': tenure, 'PhoneService': phone, 'MultipleLines': multi_lines,
        'InternetService': internet, 'OnlineSecurity': sec, 'OnlineBackup': back,
        'DeviceProtection': dev, 'TechSupport': tech, 'StreamingTV': tv, 'StreamingMovies': mov,
        'Contract': contract, 'PaperlessBilling': paperless, 'PaymentMethod': payment,
        'MonthlyCharges': monthly, 'TotalCharges': total
    }
    
    return pd.DataFrame(data, index=[0])