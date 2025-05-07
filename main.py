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

# محاولة استخراج البيانات بأمان
try:
    quote = data['results']['last_quote']
    details = data['results']['details']

    last_price = quote.get('last') or "غير متوفر"
    bid = quote.get('bid') or "غير متوفر"
    ask = quote.get('ask') or "غير متوفر"
    strike = details.get('strike_price') or "غير متوفر"
    expiry = details.get('expiration_date') or "غير متوفر"
    volume = details.get('volume') or "غير متوفر"
    oi = details.get('open_interest') or "غير متوفر"
except:
    last_price = bid = ask = strike = expiry = volume = oi = "غير متوفر"

# إعداد نص الرسالة
message = f"""
توصية جديدة:  
العقد: {OPTION_CONTRACT}  
الاسترايك: {strike}  
الانتهاء: {expiry}  
السعر الحالي: {last_price}  
العرض (Bid): {bid}  
الطلب (Ask): {ask}  
الحجم (Volume): {volume}  
Open Interest: {oi}  
#عين_السوق
"""

# إرسال الرسالة
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(telegram_url, data={
    "chat_id": CHANNEL_ID,
    "text": message
})
