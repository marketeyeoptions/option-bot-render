import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

def get_contract_ticker():
    url = "https://api.polygon.io/v3/reference/options/contracts"
    params = {
        "underlying_ticker": "NVDA",
        "contract_type": "put",
        "expiration_date": "2025-05-16",
        "strike_price": "110",
        "limit": "1",
        "apiKey": POLYGON_API_KEY
    }
    response = requests.get(url, params=params)
    try:
        ticker = response.json()["results"][0]["ticker"]
        return ticker
    except Exception as e:
        print(f"Contract fetch error: {e}")
        return None

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    try:
        data = response.json()
        result = data.get("results", [])
        quote = result[0].get("last_quote", {}) if result else {}
        bid = quote.get("bid")
        ask = quote.get("ask")
        return bid, ask
    except Exception as e:
        print(f"Price fetch error: {e}")
        return None, None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

if __name__ == "__main__":
    ticker = get_contract_ticker()
    if ticker:
        bid, ask = get_option_price(ticker)
        if bid is not None and ask is not None:
            send_telegram_message(f"سعر عرض وطلب عقد NVDA 110 Put:\nالعرض: {bid}\nالطلب: {ask}")
        else:
            send_telegram_message(f"فشل في جلب سعر عرض وطلب العقد:\n{ticker}")
    else:
        send_telegram_message("فشل في جلب بيانات العقد.")
