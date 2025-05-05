import requests

TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

# عقد NVDA Put سترايك 110 ينتهي 2025-05-16
CONTRACT_API_URL = (
    f"https://api.polygon.io/v3/reference/options/contracts"
    f"?underlying_ticker=NVDA&contract_type=put&expiration_date=2025-05-16"
    f"&strike_price=110&order=asc&limit=10&sort=ticker&apiKey={POLYGON_API_KEY}"
)

def get_option_ticker():
    response = requests.get(CONTRACT_API_URL)
    print("Contract API Status:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Full Contract Response:", data)
        results = data.get("results", [])
        if results and isinstance(results, list):
            return results[0].get("ticker")
    return None

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"
    response = requests.get(url)
    print("Snapshot API Status:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        print("Snapshot Raw Response:", data)
        results = data.get("results", {})
        if isinstance(results, dict):
            quote = results.get("last_quote", {})
            print("Quote Extracted:", quote)
            bid = quote.get("bid")
            ask = quote.get("ask")
            print("Bid:", bid, "| Ask:", ask)
            return bid, ask
    return None, None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)

if __name__ == "__main__":
    ticker = get_option_ticker()
    if ticker:
        bid, ask = get_option_price(ticker)
        if bid is not None and ask is not None:
            send_telegram_message(f"سعر عرض وطلب عقد {ticker}:\nالعرض: {bid}\nالطلب: {ask}")
        else:
            send_telegram_message(f"فشل في جلب سعر عرض وطلب للعقد:\n{ticker}")
    else:
        send_telegram_message("فشل في جلب بيانات العقد NVDA 110.")
