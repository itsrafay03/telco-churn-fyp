# 📊 Telco Customer Churn Prediction System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green.svg)

[cite_start]An end-to-end Machine Learning solution designed to predict customer churn in the telecommunications sector[cite: 54, 56]. [cite_start]This project leverages historical data to identify at-risk customers, enabling businesses to execute proactive retention strategies[cite: 54, 80].

## 🎓 Supervision / Course Context

[cite_start]This project was developed as a Final Year Project requirement for the **BS Computer Science (2022-2026)**[cite: 8, 63].
[cite_start]**Supervisor:** Dr. Omer Ajmal (Lecturer, Department of Computer Science, The Islamia University of Bahawalpur)[cite: 17, 31].

---

## 🚀 Live Demo

**Explore the interactive dashboard here:** [telco-churn-fyp.streamlit.app](https://telco-churn-fyp.streamlit.app/)

---

## 📖 Project Overview

[cite_start]Customer churn is a critical challenge where users stop doing business with a company[cite: 76, 109]. [cite_start]This system addresses the inefficiency of manual reviews by providing a data-driven, automated prediction tool[cite: 110, 117, 148].

### Key Features:

- [cite_start]**Predictive Analytics:** Uses an optimized **Random Forest** model to determine churn probability[cite: 58, 574].
- [cite_start]**Interactive Dashboard:** A user-friendly Streamlit interface for real-time predictions[cite: 58, 416].
- [cite_start]**Visual Insights:** Dynamic charts including Gauge meters for tenure analysis and Box plots for monthly charges[cite: 458, 500, 521].
- [cite_start]**Global Analysis:** Visualizes top churn triggers like contract types and payment methods[cite: 460, 506].

---

## 🛠️ Technical Workflow

[cite_start]The project follows a rigorous Data Science lifecycle[cite: 61, 98]:

1. [cite_start]**Data Acquisition & Engineering:** Sourced and cleaned the Kaggle dataset, handled missing values, scaled features, and applied **SMOTE** to balance the data and prevent overfitting[cite: 57, 132, 385, 387, 390].
2. [cite_start]**Experimental Phase (Google Colab):** Evaluated ten distinct classification models including Logistic Regression, SVC, KNN, XGBoost, and Gradient Boost[cite: 61, 102, 572].
3. [cite_start]**Model Selection:** Identified **Random Forest** as the optimal performer based on Accuracy, F1-Score, and ROC-AUC metrics[cite: 90, 574].
4. [cite_start]**Refinement (VS Code):** Transitioned to a local environment for final parameter tuning, feature scaling, and Streamlit development[cite: 412].
5. [cite_start]**Deployment:** Integrated version control via GitHub and hosted the live app on Streamlit Cloud[cite: 59, 107].

---

## 🧰 Tech Stack

- [cite_start]**Language:** Python [cite: 60, 129]
- [cite_start]**Data Processing:** Pandas, NumPy [cite: 60, 130]
- [cite_start]**Machine Learning:** Scikit-learn, SMOTE (for handling class imbalance) [cite: 60, 85, 130]
- [cite_start]**Visualization:** Matplotlib, Seaborn, Plotly [cite: 60, 130, 461]
- [cite_start]**Deployment:** Streamlit, GitHub [cite: 60, 71, 133]

---

## 📂 Project Structure

```text
├── .devcontainer/
│   └── devcontainer.json
├── data/                           # WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── Telco-Customer-Churn.csv
├── models/                         # model.pkl and scaler.pkl
│   ├── model.pkl
│   └── scaler.pkl
├── app.py                          # Main Streamlit application code
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```
