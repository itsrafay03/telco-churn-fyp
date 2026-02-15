# 📊 Telco Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green.svg)

An end-to-end Machine Learning solution designed to predict customer churn in the telecommunications sector. This project leverages historical data to identify at-risk customers, enabling businesses to execute proactive retention strategies.

## 🎓 Supervision / Course Context

This project was developed as a Final Year Project requirement for the **BS Computer Science (2022-2026)**.
**Supervisor:** Dr. Omer Ajmal (Lecturer, Department of Computer Science, The Islamia University of Bahawalpur).

---

## 🚀 Live Demo

**Explore the interactive dashboard here:** [telco-churn-fyp.streamlit.app](https://telco-churn-fyp.streamlit.app/)

---

## 📖 Project Overview

Customer churn is a critical challenge where users stop doing business with a company. This system addresses the inefficiency of manual reviews by providing a data-driven, automated prediction tool.

### Key Features:

- **Predictive Analytics:** Uses an optimized **Random Forest** model to determine churn probability.
- **Interactive Dashboard:** A user-friendly Streamlit interface for real-time predictions.
- **Visual Insights:** Dynamic charts including Gauge meters for tenure analysis and Box plots for monthly charges.
- **Global Analysis:** Visualizes top churn triggers like contract types and payment methods.

---

## 🛠️ Technical Workflow

The project follows a rigorous Data Science lifecycle:

1. **Data Acquisition & Engineering:** Sourced and cleaned the Kaggle dataset, handled missing values, scaled features, and applied **SMOTE** to balance the data and prevent overfitting.
2. Experimental Phase (Google Colab):\*\* Evaluated ten distinct classification models including Logistic Regression, SVC, KNN, XGBoost, and Gradient Boost.
3. Model Selection:** Identified **Random Forest\*\* as the optimal performer based on Accuracy, F1-Score, and ROC-AUC metrics.
4. **Refinement (VS Code):** Transitioned to a local environment for final parameter tuning, feature scaling, and Streamlit development.
5. **Deployment:** Integrated version control via GitHub and hosted the live app on Streamlit Cloud.

---

## 🧰 Tech Stack

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, SMOTE (for handling class imbalance)
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Deployment:** Streamlit, GitHub

---

## 📂 Project Structure

```text
├── .devcontainer/          # devcontainer.json
├── data/                   # Telco-Customer-Churn.csv
├── models/                 # model.pkl and scaler.pkl
├── app.py                  # Main Streamlit application code
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```
