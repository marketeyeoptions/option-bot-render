import requests
import telegram

API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHAT_ID = "@marketeyeoptions"
OPTION_TICKER = "O:NVDA250516P00110000"

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        results = data.get("results", [])
        if not results or not isinstance(results, list):
            raise Exception("Empty or invalid results")

        option_data = results[0]  # Corrected access
        quote = option_data.get("last_quote", {})

        bid = quote.get("bid", "N/A")
        ask = quote.get("ask", "N/A")
        return bid, ask
    except Exception as e:
        print("Price fetch error:", e)
        return None, None

def send_telegram_message(message):
    bot = telegram.Bot(token=BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    bid, ask = get_option_price(OPTION_TICKER)

    if bid is not None and ask is not None:
        message = f"NVDA 110 Put\nسعر العرض: {bid}\nسعر الطلب: {ask}"
    else:
        message = f"فشل في جلب سعر عرض وطلب العقد:\n{OPTION_TICKER}"
    send_telegram_message(message)

if __name__ == "__main__":
    main()
