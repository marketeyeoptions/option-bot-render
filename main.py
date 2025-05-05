import requests
import time
import telegram

# إعدادات
symbol = "O:NVDA250516P00110000"
api_key = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
bot_token = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
chat_id = "@marketeyeoptions"

# الدالة الرئيسية
def get_option_price():
    url = f"https://api.polygon.io/v3/snapshot/options/{symbol}?apiKey={api_key}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Price fetch error: Empty or invalid results")
            return None

        data = response.json()
        results = data.get("results", [])
        if not results or not isinstance(results, list):
            print("Price fetch error: No data")
            return None

        result = results[0]
        ask = result.get("last_quote", {}).get("ask", "N/A")
        bid = result.get("last_quote", {}).get("bid", "N/A")

        return ask, bid

    except Exception as e:
        print(f"Error: {e}")
        return None

# إرسال البيانات إلى تيليجرام
def send_to_telegram():
    price = get_option_price()
    if price:
        ask, bid = price
        message = f"""عقد NVDA 110 Put  
العرض: {bid}  
الطلب: {ask}  
#عين_السوق"""
    else:
        message = f"فشل في جلب سعر عرض وطلب العقد:\n{symbol}\n(النتائج فارغة)"

    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# تشغيل البوت
send_to_telegram()
