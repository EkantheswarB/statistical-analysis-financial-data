import numpy as np
import pandas as pd

def compute_log_returns(df):
    df['log_return'] = np.log(df['close'] / df['close'].shift(1))
    return df.dropna()

def detect_anomalies(df, threshold=3):
    z_scores = (df['log_return'] - df['log_return'].mean()) / df['log_return'].std()
    df['anomaly'] = z_scores.abs() > threshold
    return df
