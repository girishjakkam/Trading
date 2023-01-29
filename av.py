import requests
import pandas as pd

api_key = "YDSPE8OO05C9IA2Q"
symbol = "AAPL"
function = "TIME_SERIES_DAILY_ADJUSTED"

url = f"https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}"

response = requests.get(url)
data = response.json()


print(type(data))
input("Press Enter to close terminal window")

