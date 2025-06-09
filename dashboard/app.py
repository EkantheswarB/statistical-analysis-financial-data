import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scripts.volatility_model import forecast_volatility
from scripts.fetcher import fetch_data
from scripts.processor import compute_log_returns, detect_anomalies
from scripts.stats_tests import run_adf_test

# Page setup
st.set_page_config(page_title="HFT Analysis Dashboard", layout="wide")
st.title("📊 High-Frequency Trading Dashboard")

# Sidebar Inputs
symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL").upper()
threshold = st.sidebar.slider("Z-score Threshold", min_value=1.0, max_value=5.0, value=3.0, step=0.1)
fetch_btn = st.sidebar.button("Fetch & Analyze")

# Main Execution
if fetch_btn:
    try:
        # Step 1: Fetch Data
        df = fetch_data(symbol)

        # Step 2: Compute Log Returns
        df = compute_log_returns(df)

        # Step 3: Anomaly Detection
        df = detect_anomalies(df, threshold=threshold)

        st.success(f"✅ Data successfully fetched and analyzed for {symbol}")

        # Close Price Chart
        st.subheader("📈 Close Price")
        st.line_chart(df['close'])

        # Log Returns Chart
        st.subheader("📉 Log Returns")
        st.line_chart(df['log_return'])

        # ADF Test
        st.subheader("📋 ADF Test for Stationarity")
        adf_result = run_adf_test(df['log_return'])
        st.write(f"**ADF Statistic**: {adf_result['ADF Statistic']:.4f}")
        st.write(f"**p-value**: {adf_result['p-value']:.4f}")

        if adf_result['p-value'] < 0.05:
            st.success("✅ The series is **stationary** (Reject H₀)")
        else:
            st.warning("❌ The series is **non-stationary** (Fail to reject H₀)")

        # Anomaly Detection Plot
        st.subheader(f"🚨 Anomaly Detection (Z-score > {threshold})")
        fig, ax = plt.subplots(figsize=(12, 5))
        ax.plot(df.index, df['log_return'], label='Log Return')
        ax.scatter(df[df['anomaly']].index, df[df['anomaly']]['log_return'],
                   color='red', label='Anomaly')
        ax.set_title("Log Returns with Anomalies")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)

        # Garch(1,1) volatility Forecast
        st.subheader("Garch(1,1) Volatility Forecast")
        forecast = forecast_volatility(df, horizon = 5)
        st.write("Forecasted Volatility (Standard Deviation %) for the Next 5 Periods")
        st.write(forecast.round(4))

        # Download Button
        st.download_button("📥 Download Processed CSV",
                           data=df.to_csv().encode("utf-8"),
                           file_name=f"{symbol}_analyzed.csv",
                           mime="text/csv")

    except Exception as e:
        st.error(f"❌ Error occurred: {e}")
