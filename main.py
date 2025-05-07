import requests
import json
from telegram import Bot

# مفاتيح الوصول
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

# بيانات العقد
option_contract = "O:NVDA250516P00110000"
url = f"https://api.polygon.io/v3/snapshot/options/{option_contract}?apiKey={api_key}"

# إرسال رسالة تيليجرام
def send_telegram_message(message):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# جلب البيانات
try:
    response = requests.get(url)
    data = response.json()

    results = data.get("results")
    if results:
        details = results.get("details", {})
        greeks = results.get("greeks", {})

        price = results.get("last_quote", {}).get("ask", "N/A")
        volume = results.get("day", {}).get("volume", "N/A")
        open_interest = details.get("open_interest", "N/A")

        message = (
            f"تحديث عقد أوبشن:\n"
            f"السهم: NVDA\n"
            f"النوع: Put\n"
            f"السترايك: 110\n"
            f"الانتهاء: 16-05-2025\n"
            f"السعر (متأخر ١٥ د): {price}\n"
            f"الحجم: {volume}\n"
            f"الرمز: {option_contract}\n"
            f"#marketeye"
        )
    else:
        message = f"لم يتم العثور على بيانات للعقد:\n{option_contract}"

except Exception as e:
    message = f"خطأ أثناء جلب البيانات:\n{str(e)}"

send_telegram_message(message)
