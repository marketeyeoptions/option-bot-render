import requests
import time
from datetime import datetime

def fetch_option_price():
    # هذا مثال وهمي، عدله حسب API Polygon.io
    response = requests.get("https://api.polygon.io/v3/snapshot/options/AAPL?apiKey=YOUR_API_KEY")
    if response.status_code == 200:
        data = response.json()
        price = data.get("results", [{}])[0].get("lastQuote", {}).get("bid", "N/A")
        print(f"[{datetime.now()}] Price: {price}")
    else:
        print(f"[{datetime.now()}] Failed to fetch data")

if __name__ == "__main__":
    fetch_option_price()