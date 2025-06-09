Statistical Analysis of Financial Data - README
📊 Project Overview
This project conducts a comprehensive statistical analysis of high-frequency stock market data using Python, Streamlit, and advanced econometric models. It includes time-series analysis, anomaly detection, and volatility forecasting to help traders and researchers better understand short-term risk and return dynamics.
🚀 Features
•	✅ Real-time data fetching from Alpha Vantage API
•	✅ Time-series transformation and log return computation
•	✅ Stationarity testing with Augmented Dickey-Fuller (ADF)
•	✅ Anomaly detection using configurable Z-score threshold
•	✅ Volatility forecasting using GARCH(1,1) model
•	✅ Interactive Streamlit dashboard with symbol input and download support
•	✅ Modular architecture suitable for extension and academic/professional submission
📁 Project Structure

statistical-analysis-microstructure/
├── dashboard/
│   └── app.py                # Streamlit dashboard entry point
├── scripts/
│   ├── __init__.py
│   ├── fetcher.py            # Alpha Vantage stock data fetcher
│   ├── processor.py          # Log return + anomaly detection logic
│   ├── stats_tests.py        # ADF stationarity test
│   └── volatility_model.py   # GARCH(1,1) volatility prediction
├── requirements.txt
└── README.md

📊 How It Works
•	• Enter a stock symbol (e.g., AAPL, MSFT) in the dashboard.
•	• Fetches 1-minute historical data using Alpha Vantage API.
•	• Computes log returns and tests for stationarity using the ADF test.
•	• Detects statistical anomalies using a configurable Z-score threshold.
•	• Forecasts future volatility using a GARCH(1,1) model.
•	• Displays outputs in a clean, interactive UI with charts and downloadable CSVs.
📉 Sample Outputs
•	- Log return time series chart
•	- Anomalous points highlighted in red
•	- ADF test summary and interpretation
•	- 5-step ahead volatility forecast using GARCH
⚙️ Installation
1. Clone the repo:
git clone https://github.com/EkantheswarB/statistical-analysis-financial-data.git
cd statistical-analysis-microstructure
2. Set up a conda environment:
conda create -n finance-env python=3.10
conda activate finance-env
pip install -r requirements.txt
3. Set your Alpha Vantage API key as an environment variable:
export ALPHA_VANTAGE_API_KEY="your_api_key_here"  # For Linux/macOS
set ALPHA_VANTAGE_API_KEY="your_api_key_here"    # For Windows CMD
4. Run the dashboard:
streamlit run dashboard/app.py
📦 Dependencies
•	- Python 3.10
•	- streamlit
•	- pandas
•	- numpy
•	- matplotlib
•	- arch
•	- requests
📚 Future Enhancements
•	- Support for multiple data vendors (e.g., Yahoo Finance)
•	- Advanced anomaly models (e.g., Isolation Forest)
•	- Regime classification based on volatility shifts
•	- Multi-stock correlation and co-integration analysis
👨‍💻 Author
Ekantheswar Bandarupalli
LinkedIn: https://linkedin.com/in/ekantheswar
GitHub: https://github.com/EkantheswarB
