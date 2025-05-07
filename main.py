import requests
import telegram
from datetime import datetime

# إعدادات الاتصال
TOKEN = "7613977084:AAF-65aYBx_YJcF_f8Xf9PaaqE7AZ1FUjI4"
CHAT_ID = "@marketeyeoptions"
API_KEY = "8X2aox8AI9r_jRp3t20tsFf56YW3pEy3"

# معلومات العقد
contract_symbol = "O:NVDA250516P00110000"

# رابط API من Polygon
url = f"https://api.polygon.io/v3/snapshot/options/{contract_symbol}?apiKey={API_KEY}"

# تنفيذ الطلب
response = requests.get(url)
data = response.json()

# استخراج البيانات
results = data.get("results")
if results and isinstance(results, dict):
    last_quote = results.get("last_quote", {})
    price = last_quote.get("mid_price", "N/A")
    volume = results.get("volume", "N/A")
    oi = results.get("open_interest", "N/A")

    # تجهيز الرسالة
    message = f"""تحديث عقد أوبشن:
السهم: NVDA
النوع: Put
السعر: 110
الانتهاء: 16-05-2025
السعر (متأخر 15 د): {price}
الحجم: {volume}
الرغبة: {oi}
الرمز: {contract_symbol}

#marketeye"""
else:
    message = f"لم يتم العثور على بيانات للعقد:\n{contract_symbol}"

# إرسال الرسالة
bot = telegram.Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text=message)
