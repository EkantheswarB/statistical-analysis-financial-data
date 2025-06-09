import argparse
from scripts.fetcher import fetch_data
from scripts.processor import compute_log_returns, detect_anomalies
from scripts.stats_tests import run_adf_test

def main(symbol):
    print(f"Running analysis for {symbol}")
    df = fetch_data(symbol)
    df = compute_log_returns(df)
    df = detect_anomalies(df)
    adf_result = run_adf_test(df['log_return'])
    print("ADF Test Result:", adf_result)
    df.to_csv(f"data/cleaned/{symbol}_processed.csv")
    print(f"Saved to data/cleaned/{symbol}_processed.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", type=str, default="AAPL", help="Stock symbol")
    args = parser.parse_args()
    main(args.symbol.upper())
