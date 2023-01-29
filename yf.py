import yfinance as yf

# Get the information for the specified ticker
ticker = yf.Ticker("TSLA")

# Get the stock info
info = ticker.info

# Get the stock historical prices
history = ticker.history(period="max")

# Get the stock recommendations
recommendations = ticker.recommendations

# Get the stock earnings
earnings = ticker.earnings

# Get the stock sustainability
sustainability = ticker.sustainability

# Get the stock institutional holders
holders = ticker.institutional_holders

# Get the stock balance sheet
bs = ticker.balance_sheet

# Get the stock cash flow
cf = ticker.cashflow

# Get the stock options
options = ticker.options

# Get the stock recommendation trends
trend = ticker.recommendations

# Get ticket news
news = ticker.news

print(news)

input("Press Enter to close terminal window")

