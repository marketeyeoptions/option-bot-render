# كود 2 - بدون صورة
import requests
from datetime import datetime

# بيانات البوت و القناة
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8CihBxW0onfLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"

# نص التوصية
message = f"""
توصية جديدة
السهم: NVDA
النوع: Put
السعر: 110
الانتهاء: 16-05-2025
التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M')}
#عين_السوق
"""

# رابط API
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# البيانات المطلوبة
data = {
    "chat_id": CHANNEL_ID,
    "text": message
}

# إرسال الرسالة
response = requests.post(url, data=data)

# طباعة النتيجة
print("Status:", response.status_code)
print("Response:", response.text)
