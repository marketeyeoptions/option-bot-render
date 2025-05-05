import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

def fetch_closing_price():
    url = f"https://api.polygon.io/v2/aggs/ticker/NVDA/prev?adjusted=true&apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        data = response.json()
        price = data["results"][0]["c"]  # c = close price
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
    price = fetch_closing_price()
    if price:
        send_telegram_message(f"سعر إغلاق NVDA الأخير: ${price}")
    else:
        send_telegram_message("فشل في جلب سعر NVDA.")
