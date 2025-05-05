import requests

# بيانات الاتصال
TELEGRAM_BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
TELEGRAM_CHAT_ID = "@marketeyeoptions"
POLYGON_API_KEY = "8X2aox8AI9r_jRp3t2OtsfF56YW3pEy3"

# بيانات العقد المستهدف
UNDERLYING = "NVDA"
STRIKE = 110
EXPIRATION = "2025-05-16"
CONTRACT_TYPE = "put"

# دالة جلب رمز العقد
def get_option_contract_ticker():
    url = f"https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={UNDERLYING}&contract_type={CONTRACT_TYPE}&expiration_date={EXPIRATION}&strike_price={STRIKE}&order=asc&limit=1&sort=ticker&apiKey={POLYGON_API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        results = data.get("results")
        if results and isinstance(results, list) and "ticker" in results[0]:
            return results[0]["ticker"]
    return None

# دالة جلب سعر العرض والطلب
def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={POLYGON_API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        results = data.get("results", {})
        if isinstance(results, dict):
            quote = results.get("last_quote", {})
            bid = quote.get("bid")
            ask = quote.get("ask")
            return bid, ask
    return None, None

# إرسال رسالة إلى تيليجرام
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": text}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

# تشغيل البوت
if __name__ == "__main__":
    ticker = get_option_contract_ticker()
    if ticker:
        bid, ask = get_option_price(ticker)
        if bid is not None and ask is not None:
            msg = f"سعر عرض وطلب عقد:\n{ticker}\nالعرض: {bid}\nالطلب: {ask}"
        else:
            msg = f"فشل في جلب سعر عرض وطلب العقد:\n{ticker}"
    else:
        msg = "فشل في جلب بيانات العقد."

    send_telegram_message(msg)
