
import datetime
import numpy as np
from core.data import fetch_price_data
from core.telegram_bot import send_telegram_message
from core.volatility_monitor import volatility_spike
from core.pnl_tracker import compute_pnl

tickers = ["AAPL","MSFT","JNJ","PG","KO","XOM","CVX","PFE","ABBV","PEP"]
prices = fetch_price_data(tickers)

weights = np.repeat(1/len(tickers), len(tickers))

cum_return, drawdown = compute_pnl(prices, weights)

message = f"""
📊 <b>Quant Hedge Engine Report</b>

Portfolio Return: {cum_return:.2f}
Current Drawdown: {drawdown:.2%}
"""

if drawdown < -0.10:
    message += "\n⚠️ Drawdown exceeded -10%!"

spikes = volatility_spike(prices)
if spikes:
    message += f"\n🚨 Volatility Spike Detected in: {spikes}"

if datetime.datetime.today().weekday() == 4:
    message += "\n📅 Weekly summary included."

send_telegram_message(message)
