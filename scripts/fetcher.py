import requests
import pandas as pd
from io import StringIO
from pathlib import Path
import yaml

def load_config():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)

def fetch_data(symbol):
    config = load_config()
    api_key = config["alpha_vantage"]["api_key"]
    interval = config["alpha_vantage"]["interval"]
    output_size = config["alpha_vantage"]["output_size"]
    
    url = (
        f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY"
        f"&symbol={symbol}&interval={interval}&outputsize={output_size}"
        f"&apikey={api_key}&datatype=csv"
    )
    response = requests.get(url)
    if response.status_code != 200 or "Error" in response.text:
        raise Exception("Failed to fetch data")
    
    df = pd.read_csv(StringIO(response.text))
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)
    df = df.sort_index()
    return df
