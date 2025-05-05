import requests
import time
import telegram

# إعدادات
api_key = '8X2aox8AI9r_jRp3t20tsFf56YW3pEy3'
contract = 'O:NVDA250516P00110000'
bot_token = '7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4'
chat_id = '@marketeyeoptions'

# الطلب من بوليجون
url = f"https://api.polygon.io/v3/quotes/options/{contract}?apiKey={api_key}"

try:
    response = requests.get(url)
    data = response.json()
    print("Raw Response from Polygon:", data)

    quote = data.get("results", [{}])[0]

    ask = quote.get("ask_price", "N/A")
    bid = quote.get("bid_price", "N/A")

    message = f"""عقد NVDA 110 Put
العرض: {bid}
الطلب: {ask}
الانتهاء: 16-05-2025
#عين_السوق"""

except Exception as e:
    message = f"فشل في جلب سعر عرض وطلب العقد:\n{contract}\nخطأ داخلي: {str(e)}"

# إرسال إلى تيليجرام
bot = telegram.Bot(token=bot_token)
bot.send_message(chat_id=chat_id, text=message)
