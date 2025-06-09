import pandas as pd
from arch import arch_model

def forecast_volatility(df, horizon=5):
    """
    Fit a GARCH(1,1) model to log returns and forecast future volatility.

    Parameters:
        df (pd.DataFrame) : DataFrame with a 'log_return' column.
        horizon (int): Number of future time steps to forecast.

    Returns:
        pd.Series: Forecasted conditional volatility (standard deviation, in %) for the next 'horizon' steps.
    """

    #Drop NaNs and scale to percentage
    returns = df['log_return'].dropna()*100  # Convert to percentage scale
    
    # Fit GARCH(1,1) model
    model = arch_model(returns, vol='Garch', p=1, q=1)
    fitted_model = model.fit(disp='off')

    # Forecast future volatility
    forecast = fitted_model.forecast(horizon=horizon)
    
    # Convert forecasted variance to standard deviation (volatility)
    volatility = forecast.variance.iloc[-1] ** 0.5
    return volatility