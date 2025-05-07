import requests
from telegram import Bot

# إعدادات
TELEGRAM_BOT_TOKEN = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
TELEGRAM_CHANNEL_ID = '@marketeyeoptions'
POLYGON_API_KEY = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'

# بيانات العقد
option_contract = "O:NVDA250516P00110000"
polygon_url = f"https://api.polygon.io/v3/quotes/options/{option_contract}/last?apiKey={POLYGON_API_KEY}"

def fetch_option_price():
    try:
        response = requests.get(polygon_url)
        data = response.json()

        results = data.get("results")
        if not results:
            return f"فشل في جلب السعر اللحظي للعقد:\n{option_contract}"

        last = results.get("last", {})
        bid = last.get("bid", "N/A")
        ask = last.get("ask", "N/A")
        price = last.get("price", "N/A")
        timestamp = results.get("sip_timestamp", "N/A")

        message = f"""تحديث عقد أوبشن NVDA:
النوع: Put
السترايك: 110
الانتهاء: 2025-05-16
السعر: {price}
العرض: {bid}
الطلب: {ask}

#marketeye"""
        return message
    except Exception as e:
        return f"خطأ أثناء جلب السعر:\n{e}"

def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    message = fetch_option_price()
    bot.send_message(chat_id=TELEGRAM_CHANNEL_ID, text=message)

if __name__ == "__main__":
    main()
