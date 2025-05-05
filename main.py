import requests
import telegram

# إعدادات الاتصال
API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
BOT_TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHANNEL_ID = "@marketeyeoptions"

# بيانات العقد المطلوب
TICKER = "O:NVDA250516P00110000"
UNDERLYING = "NVDA"

# إعداد بوت تيليجرام
bot = telegram.Bot(token=BOT_TOKEN)

def get_option_price():
    url = f"https://api.polygon.io/v3/snapshot/options/{UNDERLYING}/{TICKER}?apiKey={API_KEY}"
    response = requests.get(url)
    print(f"Status: {response.status_code}")
    data = response.json()

    results = data.get("results")
    if results and isinstance(results, dict):
        quote = results.get("last_quote", {})
        bid = quote.get("bid", "N/A")
        ask = quote.get("ask", "N/A")
        return bid, ask
    else:
        print("Price fetch error: results is empty or invalid.")
        return None, None

def send_to_telegram(bid, ask):
    message = f"عقد NVDA 110 Put\nالعرض: {bid}\nالطلب: {ask}\n#عين_السوق"
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    bid, ask = get_option_price()
    if bid is not None and ask is not None:
        send_to_telegram(bid, ask)
    else:
        bot.send_message(chat_id=CHANNEL_ID, text="فشل في جلب سعر عرض وطلب عقد NVDA 110.")
