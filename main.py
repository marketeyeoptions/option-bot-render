import requests
from datetime import datetime

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

OPTION_TICKER = "O:NVDA250509C00115000"

def fetch_option_quote():
    url = f"https://api.polygon.io/v3/quotes/{OPTION_TICKER}/last?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        data = response.json()
        if "results" in data and "ask_price" in data["results"] and "bid_price" in data["results"]:
            ask = data["results"]["ask_price"]
            bid = data["results"]["bid_price"]
            return ask, bid
    return None, None

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
    ask, bid = fetch_option_quote()
    if ask is not None and bid is not None:
        send_telegram_message(f"NVDA 115 Call\nالعرض: ${bid}\nالطلب: ${ask}")
    else:
        send_telegram_message("فشل في جلب سعر عرض وطلب عقد NVDA 115.")
