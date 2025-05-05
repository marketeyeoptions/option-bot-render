import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

OPTION_CONTRACT = "O:NVDA250509C00115000"  # عقد كول NVDA سترايك 115 ينتهي 9 مايو

def fetch_option_bid_ask():
    url = f"https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Status: {response.status_code}, Response: {response.text}")

    if response.status_code == 200:
        data = response.json()
        if "results" in data and isinstance(data["results"], dict):
            last_quote = data["results"].get("last_quote", {})
            bid = last_quote.get("bid")
            ask = last_quote.get("ask")
            return bid, ask
    return None, None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

if __name__ == "__main__":
    bid, ask = fetch_option_bid_ask()
    if bid is not None and ask is not None:
        send_telegram_message(f"سعر عرض وطلب عقد NVDA 115 Call:\nالعرض: {bid}\nالطلب: {ask}")
    else:
        send_telegram_message("فشل في جلب سعر عرض وطلب عقد NVDA 115.")
