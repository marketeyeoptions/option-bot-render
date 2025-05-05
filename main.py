import requests
import time
import telegram

# بيانات الاتصال
API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHANNEL_ID = "@marketeyeoptions"

# بيانات العقد المطلوب
TICKER = "O:NVDA250516P00110000"

# إعداد البوت
bot = telegram.Bot(token=BOT_TOKEN)

def get_option_price(ticker):
    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    try:
        if "results" not in data or not isinstance(data["results"], dict):
            raise Exception("Empty or invalid results")

        quote = data["results"].get("last_quote", {})
        bid = quote.get("bid", "N/A")
        ask = quote.get("ask", "N/A")
        return bid, ask
    except Exception as e:
        print("Price fetch error:", e)
        return None, None

def send_update(bid, ask):
    message = f"NVDA 110 Put\nعرض: {ask} | طلب: {bid}\nالعقد: {TICKER}\n#عين_السوق"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

def main():
    bid, ask = get_option_price(TICKER)
    if bid is not None and ask is not None:
        send_update(bid, ask)
    else:
        bot.send_message(chat_id=CHANNEL_ID, text=f"فشل في جلب سعر عرض وطلب العقد:\n{TICKER}")

if __name__ == "__main__":
    main()
