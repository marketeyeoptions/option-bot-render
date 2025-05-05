import requests
import time
import telegram

# إعداد التوكن والبوت
bot = telegram.Bot(token="7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4")
chat_id = "@marketeyeoptions"

# معلومات العقد
symbol = "O:NVDA250516P00110000"

# استدعاء API
url = f"https://api.polygon.io/v3/snapshot/options/{symbol}?apiKey=8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"

try:
    response = requests.get(url)
    data = response.json()

    # طباعة الرد في اللوق
    print("Raw Response from Polygon:", data)

    option = data['results']
    if not option:
        raise Exception("النتائج فارغة")

    option = option[0]

    # استخراج البيانات
    bid = option['last_quote']['bid'] or "N/A"
    ask = option['last_quote']['ask'] or "N/A"
    option_type = option['details']['contract_type']
    strike = option['details']['strike_price']
    expiry = option['details']['expiration_date']

    # تنسيق الرسالة
    msg = (
        f"عقد NVDA {strike} {option_type}\n"
        f"العرض: {bid}\n"
        f"الطلب: {ask}\n"
        f"الانتهاء: {expiry}\n"
        f"#عين_السوق"
    )

    # إرسال إلى تيليجرام
    bot.send_message(chat_id=chat_id, text=msg)

except Exception as e:
    msg = f"فشل في جلب سعر عرض وطلب العقد:\n{symbol}\nخطأ داخلي: {e}"
    bot.send_message(chat_id=chat_id, text=msg)
