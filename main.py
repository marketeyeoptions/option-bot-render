import requests

# بيانات الاتصال
TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "BwIqC9PU9vXhHDympuBEb3_JLE4_FWIf"

# إعدادات العقد المطلوب
TICKER_SYMBOL = "NVDA"
EXPIRATION_DATE = "2025-05-16"
STRIKE_PRICE = 110
CONTRACT_TYPE = "put"

def get_option_ticker():
    url = (
        f"https://api.polygon.io/v3/reference/options/contracts?"
        f"underlying_ticker={TICKER_SYMBOL}&contract_type={CONTRACT_TYPE}"
        f"&expiration_date={EXPIRATION_DATE}&strike_price={STRIKE_PRICE}"
        f"&order=asc&limit=1&sort=ticker&apiKey={POLYGON_API_KEY}"
    )
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        results = data.get("results", [])
        if results:
            return results[0]["ticker"]
    return None

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        quote = data.get("results", {}).get("last_quote", {})
        bid = quote.get("bid")
        ask = quote.get("ask")
        return bid, ask
    return None, None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    ticker = get_option_ticker()
    if ticker:
        bid, ask = get_option_price(ticker)
        if bid is not None and ask is not None:
            send_telegram_message(f"عقد {ticker}\nالعرض: {bid}\nالطلب: {ask}")
        else:
            send_telegram_message(f"فشل في جلب سعر عرض وطلب العقد {ticker}")
    else:
        send_telegram_message("فشل في جلب بيانات العقد.")
