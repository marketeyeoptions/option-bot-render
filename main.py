import requests

# إعدادات
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8CihBxW0onfLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"
POLYGON_API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"
OPTION_CONTRACT = "O:NVDA250516P00110000"

# استدعاء بيانات السعر من Polygon
polygon_url = f"https://api.polygon.io/v3/snapshot/options/{OPTION_CONTRACT}?apiKey={POLYGON_API_KEY}"
response = requests.get(polygon_url)
data = response.json()

# استخراج السعر الحالي
try:
    current_price = data['results']['last_quote']['ask'] or data['results']['last_quote']['bid']
except Exception:
    current_price = "N/A"

# نص الرسالة مع السعر
message = f"""
توصية جديدة:  
السهم: NVDA  
النوع: Put  
الاسترايك: 110  
الانتهاء: 2025-05-16  
السعر الحالي: {current_price}  
#عين_السوق
"""

# إرسال الرسالة إلى تيليجرام
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(telegram_url, data={
    "chat_id": CHANNEL_ID,
    "text": message
})
