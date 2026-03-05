
def volatility_spike(price_df, threshold=2.0):
    returns = price_df.pct_change()
    vol = returns.rolling(30).std()
    z = (vol.iloc[-1] - vol.mean()) / vol.std()
    return z[z > threshold].index.tolist()
