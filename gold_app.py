import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("gold_price_model.pkl")

# Page config
st.set_page_config(
    page_title="Gold Price Predictor",
    page_icon="💰",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #fdf6ec;
    }
    .main {
        background-color: #fff8f0;
        padding: 20px;
        border-radius: 10px;
    }
    .prediction-box {
        background-color: #fff3cd;
        padding: 20px;
        border-left: 6px solid #ffbf00;
        border-radius: 8px;
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2983/2983783.png", width=100)
    st.title("💹 About")
    st.markdown("""
    This app uses a **Machine Learning model** to predict **Gold Prices** based on:

    - 📊 S&P 500 Index (SPX)
    - 🛢️ Oil ETF (USO)
    - 🪙 Silver ETF (SLV)
    - 💶 EUR/USD exchange rate

    Developed by **Manikanta** 💻
    """)

# Main section
st.title("💰 Gold Price Prediction App")
st.write("### Enter the economic indicators below:")

# Input form
with st.form("predict_form"):
    spx = st.number_input("📊 SPX (S&P 500 Index)", value=4000.00)
    uso = st.number_input("🛢️ USO (Oil ETF Price)", value=70.00)
    slv = st.number_input("🪙 SLV (Silver ETF Price)", value=25.00)
    eur_usd = st.number_input("💶 EUR/USD", value=1.10)

    submitted = st.form_submit_button("🚀 Predict Gold Price")

# Make prediction
if submitted:
    with st.spinner("🔍 Analyzing data and predicting..."):
        input_data = pd.DataFrame([[spx, uso, slv, eur_usd]], columns=["SPX", "USO", "SLV", "EUR/USD"])
        prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="prediction-box">
        📈 Predicted Gold Price: <span style='color: #d97706;'>${prediction:.2f}</span>
    </div>
    """, unsafe_allow_html=True)
