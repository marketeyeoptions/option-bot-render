import requests
from datetime import datetime

# بيانات التوكن والقناة
BOT_TOKEN = "7710712900:AAH8WFVY9GzhCjisF8CihBxW0onfLBN9LZQ"
CHANNEL_ID = "@marketeyeoptions"

# نص الرسالة
message = f"""توصية جديدة:
السهم: NVDA
النوع: Put
السترايك: 110
الانتهاء: 2025-05-16
التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M')}
#عين_السوق"""

# رابط API للإرسال
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# البيانات المطلوبة
data = {
    "chat_id": CHANNEL_ID,
    "text": message
}

# تنفيذ الطلب
response = requests.post(url, data=data)

# عرض النتيجة
print("Status:", response.status_code)
print("Response:", response.text)
