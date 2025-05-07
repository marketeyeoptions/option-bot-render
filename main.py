import requests
from telegram import Bot

TELEGRAM_BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHANNEL_ID = '@marketeyeoptions'
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'

# عقد بوت NVDA سترايك 110 - 2025-05-16
option_contract = "O:NVDA250516P00110000"
polygon_url = f"https://api.polygon.io/v3/trades/options/{option_contract}/last?apiKey={POLYGON_API_KEY}"

def fetch_option_price():
    try:
        response = requests.get(polygon_url)
        data = response.json()

        results = data.get("results", {})
        price = results.get("price", "N/A")
        size = results.get("size", "N/A")
        exchange = results.get("exchange", "N/A")
        timestamp = results.get("sip_timestamp", "N/A")

        message = f"""تحديث عقد أوبشن NVDA:
النوع: Put
السترايك: 110
الانتهاء: 2025-05-16
السعر: {price}
الحجم: {size}
منصة التداول: {exchange}

#marketeye"""
        return message
    except Exception as e:
        return f"خطأ أثناء جلب البيانات:\n{e}"

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = fetch_option_price()
    bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)

if __name__ == "__main__":
    main()
