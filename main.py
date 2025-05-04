import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = "7613977084:AF-6aSy8X_YJcF_f8XY9PpaqE7AZiFUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JlLE4_FWlf"

def fetch_option_price():
    url = f"https://api.polygon.io/v3/snapshot/options/NVDA/NVDA250509C00115000?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    
    print(f"Status: {response.status_code}, Response: {response.text}")
    
    if response.status_code == 200:
        data = response.json()
        price = data["results"]["last_quote"]["midpoint"]
        return price
    else:
        return None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

if __name__ == "__main__":
    price = fetch_option_price()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if price:
        msg = f"Option Contract Update:\nDate: {timestamp}\nPrice: {price}"
    else:
        msg = f"[{timestamp}] Failed to fetch option price."
    send_telegram_message(msg)
