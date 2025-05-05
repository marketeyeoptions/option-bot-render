import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

# إعدادات العقد المطلوب
underlying_ticker = "NVDA"
strike_price = 110
expiration_date = "2025-05-16"
contract_type = "put"

def get_option_contract():
    url = f"https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={underlying_ticker}&contract_type={contract_type}&expiration_date={expiration_date}&strike_price={strike_price}&apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Contract API Status: {response.status_code}")
    data = response.json()
    results = data.get("results", [])
    if isinstance(results, list) and len(results) > 0:
        return results[0]["ticker"]
    return None

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print(f"Snapshot API Status: {response.status_code}")
    data = response.json()
    results = data.get("results", {})
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
    ticker = get_option_contract()
    if ticker:
        bid, ask = get_option_price(ticker)
        if bid is not None and ask is not None:
            send_telegram_message(f"سعر عرض وطلب عقد NVDA 110 Put:\nالعرض: {bid}\nالطلب: {ask}")
        else:
            send_telegram_message(f"فشل في جلب سعر عرض وطلب العقد:\n{ticker}")
    else:
        send_telegram_message("فشل في جلب بيانات العقد المطلوب.")
