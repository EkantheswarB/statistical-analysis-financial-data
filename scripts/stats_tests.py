from statsmodels.tsa.stattools import adfuller

def run_adf_test(series):
    result = adfuller(series)
    return {"ADF Statistic": result[0], "p-value": result[1]}
