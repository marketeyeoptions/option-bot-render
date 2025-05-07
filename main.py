import requests

# إعدادات
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8CihBxW0onfLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"
POLYGON_API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
OPTION_CONTRACT = "O:NVDA250516P00110000"

# استدعاء بيانات العقد من Polygon
url = f"https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={POLYGON_API_KEY}"
response = requests.get(url)
data = response.json()

# محاولة استخراج البيانات
try:
    last_price = data['results']['last_quote']['last']
    bid = data['results']['last_quote']['bid']
    ask = data['results']['last_quote']['ask']
    expiry = data['results']['details']['expiration_date']
    strike = data['results']['details']['strike_price']
except:
    last_price = "N/A"
    bid = "N/A"
    ask = "N/A"
    expiry = "N/A"
    strike = "N/A"

# إعداد نص الرسالة
message = f"""
توصية جديدة:  
العقد: {OPTION_CONTRACT}  
الاسترايك: {strike}  
الانتهاء: {expiry}  
السعر الحالي: {last_price}  
العرض (Bid): {bid}  
الطلب (Ask): {ask}  
#عين_السوق
"""

# إرسال الرسالة
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(telegram_url, data={
    "chat_id": CHANNEL_ID,
    "text": message
})
