import requests
import json
import telegram
import os

# إعدادات
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"
option_contract = "O:NVDA250516P00110000"
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"

# رابط API من بوليجون
url = f"https://api.polygon.io/v3/snapshot/options/{option_contract}?apiKey={api_key}"

# إرسال رسالة تيليجرام
def send_telegram(message):
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

try:
    response = requests.get(url)
    data = response.json()

    if "results" in data and data["results"]:
        result = data["results"]
        ask = result["details"]["ask"]
        bid = result["details"]["bid"]
        strike_price = result["breakdown"]["strike_price"]
        expiry_date = result["breakdown"]["expiration_date"]
        option_type = result["breakdown"]["option_type"]

        message = f"""عقد NVDA {strike_price} {option_type}
العرض: {bid}
الطلب: {ask}
الانتهاء: {expiry_date}
#عين_السوق"""
        send_telegram(message)

    else:
        send_telegram(f"فشل في جلب سعر عرض وطلب العقد:\n{option_contract}\n(النتائج فارغة)")
        print("Raw Response from Polygon:", response.text)

except Exception as e:
    send_telegram(f"فشل في جلب سعر عرض وطلب العقد:\n{option_contract}\nخطأ داخلي: {e}")
