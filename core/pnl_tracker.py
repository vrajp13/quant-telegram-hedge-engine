
def compute_pnl(price_df, weights):
    returns = price_df.pct_change().dropna()
    portfolio = returns @ weights
    cumulative = (1 + portfolio).cumprod()
    drawdown = cumulative / cumulative.cummax() - 1
    return cumulative.iloc[-1], drawdown.iloc[-1]
