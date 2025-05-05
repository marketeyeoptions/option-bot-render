import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"
OPTION_CONTRACT = "O:NVDA250516P00110000"  # عقد بوت NVDA سترايك 110، انتهاء 16 مايو

def fetch_option_bid_ask():
    url = f"https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results = data.get("results")
        if isinstance(results, dict):
            quote = results.get("last_quote", {})
            bid = quote.get("bid")
            ask = quote.get("ask")
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
        send_telegram_message(f"سعر عرض وطلب عقد NVDA 110 Put:\nالعرض: {bid}\nالطلب: {ask}")
    else:
        send_telegram_message(f"فشل في جلب سعر عرض وطلب للعقد:\n{OPTION_CONTRACT}")
