import requests
import time

# بيانات العقد
ticker = "O:NVDA250516P00110000"
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    try:
        result = data.get("results", [])
        if not result:
            return None, None
        quote = result[0].get("last_quote", {})
        bid = quote.get("bid", None)
        ask = quote.get("ask", None)
        return bid, ask
    except Exception as e:
        print("Price fetch error:", e)
        return None, None

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram error:", e)

def main():
    bid, ask = get_option_price(ticker)
    if bid is not None and ask is not None:
        message = f"سعر عرض وطلب العقد:\n{ticker}\nBid: {bid}\nAsk: {ask}"
    else:
        message = f"فشل في جلب سعر عرض وطلب العقد:\n{ticker}"
    send_telegram_message(message)

if __name__ == "__main__":
    main()
