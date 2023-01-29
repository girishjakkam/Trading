import yfinance as yf
import pandas as pd 
tickers = ['TSLA', 'TESLA', 'WSB', 'ACT', 'AH', 'AMC', 'WSB', 'YOLO', 'OK', 'US', 'GDP']

for ticker in tickers:
    stock_info = yf.Ticker(ticker)
    print(ticker,(stock_info.history(period="1mo").tail(6)))
