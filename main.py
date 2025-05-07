import requests
import time
from telegram import Bot

# إعدادات
TELEGRAM_BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHANNEL_ID = '@marketeyeoptions'
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'

# بيانات العقد (Put على NVDA سترايك 110 - انتهاء 2025-05-16)
option_contract = "O:NVDA250516P00110000"
polygon_url = f"https://api.polygon.io/v3/reference/options/contracts/{option_contract}?apiKey={POLYGON_API_KEY}"

# تتبع آخر سعر تم إرساله
last_price = None

def fetch_option_price():
    try:
        response = requests.get(polygon_url)
        data = response.json()

        results = data.get("results", {})
        if isinstance(results, list) and results:
            option_data = results[0]
        elif isinstance(results, dict):
            option_data = results
        else:
            return f"فشل في جلب سعر عرض وطلب العقد:\n{option_contract}\n(النتائج غير متوفرة)", None

        strike_price = option_data.get("strike_price", "N/A")
        expiration_date = option_data.get("expiration_date", "N/A")
        option_type = option_data.get("contract_type", "N/A")
        last_price_value = option_data.get("last_price", "N/A")

        message = f"""تحديث عقد أوبشن NVDA:
النوع: Put
السترايك: {strike_price}
الانتهاء: {expiration_date}
السعر: {last_price_value}

#marketeye"""
        return message, last_price_value
    except Exception as e:
        return f"خطأ أثناء جلب البيانات:\n{e}", None

def main():
    global last_price
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    while True:
        message, current_price = fetch_option_price()

        if current_price and current_price != last_price:
            bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)
            last_price = current_price
        elif current_price is None:
            bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)

        time.sleep(300)

if __name__ == "__main__":
    main()
