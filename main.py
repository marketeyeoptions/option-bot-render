import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

OPTION_CONTRACT_TICKER = "O:NVDA250509C00115000"

def fetch_option_bid_ask():
    url = f"https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT_TICKER}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        data = response.json()
        try:
            last_quote = data["results"][0]["last_quote"]
            bid = last_quote["bid"]
            ask = last_quote["ask"]
            return bid, ask
        except Exception as e:
            print("Error parsing bid/ask:", e)
            return None, None
    else:
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
    bid, ask = fetch_option_bid_ask()
    if bid is not None and ask is not None:
        message = f"NVDA 115 Call\nالعرض: ${bid}\nالطلب: ${ask}"
        send_telegram_message(message)
    else:
        send_telegram_message("فشل في جلب سعر عرض وطلب عقد NVDA 115.")
