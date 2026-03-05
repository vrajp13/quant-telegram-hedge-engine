
import yfinance as yf

def fetch_price_data(tickers, period="1y"):
    return yf.download(tickers, period=period)["Adj Close"].dropna()
